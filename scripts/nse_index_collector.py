#!/usr/bin/env python3
import argparse,csv,hashlib,json,time
from datetime import datetime,timedelta
from pathlib import Path
import requests
URL='https://www.nseindia.com/api/historicalOR/indicesHistory'
HOME='https://www.nseindia.com/'
HEAD={'User-Agent':'Mozilla/5.0 (compatible; IndianMarketResearch/1.0)','Accept':'application/json,text/plain,*/*','Referer':HOME}
BASE=['date','index','open','high','low','close','shares_traded','turnover_cr','source_url','retrieved_at','response_sha256']
CHANGE=['open_change_amount','open_change_percent','high_change_amount','high_change_percent','low_change_amount','low_change_percent','close_change_amount','close_change_percent','volume_change_amount','volume_change_percent','direction']
def val(x):
 try: return float(str(x).replace(',','').strip())
 except: return None
def diff(now,old):
 a,b=val(now),val(old)
 if a is None or b is None:return '',''
 return round(a-b,6),round((a-b)/b*100,6) if b else ''
def main():
 p=argparse.ArgumentParser();p.add_argument('--index',required=True);p.add_argument('--from-date',required=True);p.add_argument('--to-date',required=True);p.add_argument('--output',default='data/nse-official');a=p.parse_args()
 start=datetime.strptime(a.from_date,'%d-%m-%Y').date();end=datetime.strptime(a.to_date,'%d-%m-%Y').date()
 if start>end: raise SystemExit('from-date must not be after to-date')
 safe=''.join(c.lower() if c.isalnum() else '_' for c in a.index).strip('_');root=Path(a.output)/safe;raw=root/'raw_json';raw.mkdir(parents=True,exist_ok=True)
 s=requests.Session();s.headers.update(HEAD);s.get(HOME,timeout=30);rows=[];windows=[];cur=start
 while cur<=end:
  stop=min(cur+timedelta(days=364),end);params={'indexType':a.index,'from':cur.strftime('%d-%m-%Y'),'to':stop.strftime('%d-%m-%Y')};got=datetime.utcnow().replace(microsecond=0).isoformat()+'Z';r=None
  for n in range(3):
   r=s.get(URL,params=params,timeout=60)
   if r.status_code==200: break
   time.sleep(2**n)
  r.raise_for_status();digest=hashlib.sha256(r.content).hexdigest();rawfile=raw/f'{cur:%Y%m%d}_{stop:%Y%m%d}.json';rawfile.write_bytes(r.content);payload=r.json();data=payload.get('data',[]) if isinstance(payload,dict) else []
  if isinstance(data,dict): data=data.get('indexCloseOnlineRecords',[])
  for x in data:
   rows.append({'date':x.get('EOD_TIMESTAMP',''),'index':x.get('EOD_INDEX_NAME',a.index),'open':x.get('EOD_OPEN_INDEX_VAL',''),'high':x.get('EOD_HIGH_INDEX_VAL',''),'low':x.get('EOD_LOW_INDEX_VAL',''),'close':x.get('EOD_CLOSE_INDEX_VAL',''),'shares_traded':x.get('HIT_TRADED_QTY',x.get('EOD_TRADED_QTY','')),'turnover_cr':x.get('HIT_TURN_OVER',x.get('EOD_TURN_OVER','')),'source_url':r.url,'retrieved_at':got,'response_sha256':digest})
  windows.append({'from':cur.isoformat(),'to':stop.isoformat(),'rows_returned':len(data),'raw_file':str(rawfile),'response_sha256':digest,'source_url':r.url,'retrieved_at':got});cur=stop+timedelta(days=1);time.sleep(1)
 rows.sort(key=lambda x:x['date']);prev=None
 for row in rows:
  for field,source in [('open','open'),('high','high'),('low','low'),('close','close'),('volume','shares_traded')]:
   amount,pct=diff(row[source],prev[source]) if prev else ('','')
   row[field+'_change_amount']=amount;row[field+'_change_percent']=pct
  c=val(row['close']);pc=val(prev['close']) if prev else None
  row['direction']='' if c is None or pc is None else ('UP' if c>pc else 'DOWN' if c<pc else 'FLAT');prev=row
 out=root/'historical.csv';fields=BASE+CHANGE
 with out.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 (root/'manifest.json').write_text(json.dumps({'index':a.index,'requested_from':start.isoformat(),'requested_to':end.isoformat(),'rows_written':len(rows),'change_basis':'previous trading-day row; first row blank; no interpolation','windows':windows},indent=2),encoding='utf-8')
 print(json.dumps({'index':a.index,'rows':len(rows),'output':str(out)}))
if __name__=='__main__': main()
