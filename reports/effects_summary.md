# Celestial Indices — Effects Summary

*Generated 2026-11-09T23:27:59*

Every finding below compares the market's forward return around an astrological event with the unconditional base rate for the same index and forward window.

## 1. Dataset

| Item | Value |
| --- | --- |
| Aligned trading days | 6,631 |
| Index bars (date x index) | 25,887 |
| Calendar trading days | 6,631 |
| Planetary events detected | 11,801 |
| Special (Muhurat) sessions retained | 0 |
| Date range | 2000-01-03 to 2026-11-06 |
| Indices | Nifty 50, Nifty Bank, Nifty Midcap 100, Nifty Midcap 150, BSE Sensex |

Events by category:

| Category | Events | Distinct event types |
| --- | --- | --- |
| Major aspects (Trine / Square / Opposition) | 4,617 | 97 |
| Conjunctions (Yuti) | 1,216 | 35 |
| Direct stations (Anuvakra) | 162 | 5 |
| Retrograde stations (Vakra) | 164 | 5 |
| Sign ingress (Rashi Sankranti) | 5,642 | 9 |

## 2. Method

* Forward returns are close-to-close over **trading** days, so weekends and holidays never stretch a window.
* Windows studied: 1d, 3d, 5d, 10d, 20d.
* An event falling on a non-trading day is attributed to the next trading session — the first session in which it could be traded.
* `base_rate` is the unconditional mean forward return for that index and window across every session.
* `p_value` comes from Welch's two-sample t-test comparing event windows against the full unconditional distribution; a one-sample test against the base rate is also computed and stored.
* **Multiple testing.** Several thousand event x index x window combinations are tested at once, so the nominal p-value is optimistic. Every result therefore also carries a **Benjamini-Hochberg q-value** that controls the false discovery rate across the whole study, and the headline sections are reported on the corrected basis.
* **Caveat:** overlapping forward windows make consecutive event observations correlated, so p-values are optimistic for densely clustered event types. Treat effect sizes and direction as the primary evidence, not the p-value alone.

## 3. Headline results (5-day forward window)

Mean forward return around each event, the unconditional base rate, and the two-sided p-value.

| Event | Index | N | Mean ret | Base rate | Excess | Win % | p-value | q (BH) | BH sig |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jupiter Sign Ingress | Nifty 50 | 39 | 1.852 | 0.2178 | 1.634 | 56.41 | 0.02104 | 0.06844 | no |
| Jupiter Sign Ingress | Nifty Bank | 39 | 2.125 | 0.3 | 1.825 | 61.54 | 0.02277 | 0.07259 | no |
| Jupiter Sign Ingress | Nifty Midcap 100 | 39 | -0.2945 | 0.266 | -0.5605 | 41.03 | 0.255 | 0.4274 | no |
| Jupiter Sign Ingress | Nifty Midcap 150 | 39 | 0.3856 | 0.2642 | 0.1214 | 56.41 | 0.7167 | 0.836 | no |
| Jupiter Sign Ingress | BSE Sensex | 39 | 0.1765 | 0.2506 | -0.07409 | 48.72 | 0.8258 | 0.9052 | no |
| Ketu Sign Ingress | Nifty 50 | 17 | 3.255 | 0.2178 | 3.037 | 76.47 | 0.01399 | 0.04946 | yes |
| Ketu Sign Ingress | Nifty Bank | 17 | 3.869 | 0.3 | 3.569 | 70.59 | 0.01152 | 0.04268 | yes |
| Ketu Sign Ingress | Nifty Midcap 100 | 17 | -0.3651 | 0.266 | -0.6311 | 41.18 | 0.1295 | 0.2638 | no |
| Ketu Sign Ingress | Nifty Midcap 150 | 17 | 0.8419 | 0.2642 | 0.5777 | 76.47 | 0.1251 | 0.2567 | no |
| Ketu Sign Ingress | BSE Sensex | 17 | 0.09859 | 0.2506 | -0.152 | 58.82 | 0.7718 | 0.8717 | no |
| Mars Sign Ingress | Nifty 50 | 185 | 2.851 | 0.2178 | 2.633 | 65.41 | 3.478e-11 | 2.557e-09 | yes |
| Mars Sign Ingress | Nifty Bank | 185 | 3.315 | 0.3 | 3.015 | 67.03 | 3.748e-11 | 2.703e-09 | yes |
| Mars Sign Ingress | Nifty Midcap 100 | 185 | -0.03209 | 0.266 | -0.2981 | 34.05 | 0.1994 | 0.3599 | no |
| Mars Sign Ingress | Nifty Midcap 150 | 185 | 0.3853 | 0.2642 | 0.121 | 63.78 | 0.5612 | 0.7254 | no |
| Mars Sign Ingress | BSE Sensex | 185 | 0.0872 | 0.2506 | -0.1634 | 50.81 | 0.485 | 0.6626 | no |
| Mercury Sign Ingress | Nifty 50 | 394 | 3.058 | 0.2178 | 2.84 | 69.54 | 7.562e-28 | 1.89e-25 | yes |
| Mercury Sign Ingress | Nifty Bank | 394 | 3.487 | 0.3 | 3.187 | 68.53 | 6.807e-25 | 1.276e-22 | yes |
| Mercury Sign Ingress | Nifty Midcap 100 | 394 | 0.204 | 0.266 | -0.06203 | 40.36 | 0.6917 | 0.8183 | no |
| Mercury Sign Ingress | Nifty Midcap 150 | 394 | 0.7312 | 0.2642 | 0.467 | 69.04 | 0.0002803 | 0.002167 | yes |
| Mercury Sign Ingress | BSE Sensex | 394 | 0.4025 | 0.2506 | 0.1519 | 58.38 | 0.3308 | 0.51 | no |
| Moon Sign Ingress | Nifty 50 | 4302 | 2.953 | 0.2178 | 2.735 | 68.64 | 6.041e-203 | 1.133e-199 | yes |
| Moon Sign Ingress | Nifty Bank | 4302 | 3.363 | 0.3 | 3.063 | 67.76 | 5.267e-169 | 3.292e-166 | yes |
| Moon Sign Ingress | Nifty Midcap 100 | 4302 | 0.1006 | 0.266 | -0.1654 | 39.61 | 0.01304 | 0.04719 | yes |
| Moon Sign Ingress | Nifty Midcap 150 | 4302 | 0.5583 | 0.2642 | 0.2941 | 66.97 | 5.888e-07 | 1.512e-05 | yes |
| Moon Sign Ingress | BSE Sensex | 4302 | 0.248 | 0.2506 | -0.002585 | 56.23 | 0.9665 | 0.9869 | no |
| Rahu Sign Ingress | Nifty 50 | 17 | 3.255 | 0.2178 | 3.037 | 76.47 | 0.01399 | 0.04946 | yes |
| Rahu Sign Ingress | Nifty Bank | 17 | 3.869 | 0.3 | 3.569 | 70.59 | 0.01152 | 0.04268 | yes |
| Rahu Sign Ingress | Nifty Midcap 100 | 17 | -0.3651 | 0.266 | -0.6311 | 41.18 | 0.1295 | 0.2638 | no |
| Rahu Sign Ingress | Nifty Midcap 150 | 17 | 0.8419 | 0.2642 | 0.5777 | 76.47 | 0.1251 | 0.2567 | no |
| Rahu Sign Ingress | BSE Sensex | 17 | 0.09859 | 0.2506 | -0.152 | 58.82 | 0.7718 | 0.8717 | no |
| Saturn Sign Ingress | Nifty 50 | 23 | 3.899 | 0.2178 | 3.681 | 73.91 | 0.0044 | 0.0191 | yes |
| Saturn Sign Ingress | Nifty Bank | 23 | 4.75 | 0.3 | 4.45 | 69.57 | 0.002022 | 0.01014 | yes |
| Saturn Sign Ingress | Nifty Midcap 100 | 23 | -0.446 | 0.266 | -0.712 | 21.74 | 0.1594 | 0.3083 | no |
| Saturn Sign Ingress | Nifty Midcap 150 | 23 | 0.3587 | 0.2642 | 0.0945 | 69.57 | 0.8508 | 0.9192 | no |
| Saturn Sign Ingress | BSE Sensex | 23 | -0.3734 | 0.2506 | -0.6239 | 47.83 | 0.2826 | 0.4582 | no |
| Sun Sign Ingress | Nifty 50 | 322 | 2.795 | 0.2178 | 2.577 | 67.08 | 3.665e-16 | 3.927e-14 | yes |
| Sun Sign Ingress | Nifty Bank | 322 | 3.226 | 0.3 | 2.926 | 66.15 | 3.614e-14 | 3.566e-12 | yes |
| Sun Sign Ingress | Nifty Midcap 100 | 322 | -0.02377 | 0.266 | -0.2898 | 35.71 | 0.06101 | 0.1507 | no |
| Sun Sign Ingress | Nifty Midcap 150 | 322 | 0.4073 | 0.2642 | 0.143 | 66.77 | 0.4451 | 0.6251 | no |
| Sun Sign Ingress | BSE Sensex | 322 | -0.04855 | 0.2506 | -0.2991 | 54.04 | 0.1324 | 0.2687 | no |
| Venus Sign Ingress | Nifty 50 | 337 | 3.061 | 0.2178 | 2.843 | 69.73 | 8.929e-23 | 1.456e-20 | yes |
| Venus Sign Ingress | Nifty Bank | 337 | 3.46 | 0.3 | 3.16 | 68.25 | 2.262e-20 | 2.925e-18 | yes |
| Venus Sign Ingress | Nifty Midcap 100 | 337 | 0.2496 | 0.266 | -0.01642 | 41.25 | 0.922 | 0.9665 | no |
| Venus Sign Ingress | Nifty Midcap 150 | 337 | 0.6305 | 0.2642 | 0.3663 | 67.06 | 0.01282 | 0.04658 | yes |
| Venus Sign Ingress | BSE Sensex | 337 | 0.3659 | 0.2506 | 0.1153 | 57.57 | 0.4969 | 0.6739 | no |
| Jupiter Retrograde Station | Nifty 50 | 24 | 2.592 | 0.2178 | 2.374 | 62.5 | 0.02935 | 0.08728 | no |
| Jupiter Retrograde Station | Nifty Bank | 24 | 3.176 | 0.3 | 2.876 | 70.83 | 0.02247 | 0.07184 | no |
| Jupiter Retrograde Station | Nifty Midcap 100 | 24 | 0.4221 | 0.266 | 0.1561 | 41.67 | 0.6999 | 0.8225 | no |
| Jupiter Retrograde Station | Nifty Midcap 150 | 24 | 0.3023 | 0.2642 | 0.03803 | 62.5 | 0.9303 | 0.9709 | no |
| Jupiter Retrograde Station | BSE Sensex | 24 | 0.07662 | 0.2506 | -0.174 | 62.5 | 0.7016 | 0.8237 | no |
| Mars Retrograde Station | Nifty 50 | 12 | 3.125 | 0.2178 | 2.907 | 91.67 | 0.06412 | 0.1557 | no |
| Mars Retrograde Station | Nifty Bank | 12 | 4.393 | 0.3 | 4.093 | 83.33 | 0.03503 | 0.09944 | no |
| Mars Retrograde Station | Nifty Midcap 100 | 12 | 0.4152 | 0.266 | 0.1492 | 50 | 0.8795 | 0.9383 | no |
| Mars Retrograde Station | Nifty Midcap 150 | 12 | 1.136 | 0.2642 | 0.8716 | 91.67 | 0.2821 | 0.4582 | no |
| Mars Retrograde Station | BSE Sensex | 12 | 0.6273 | 0.2506 | 0.3767 | 83.33 | 0.6643 | 0.8011 | no |
| Mercury Retrograde Station | Nifty 50 | 85 | 2.791 | 0.2178 | 2.573 | 65.88 | 5.85e-06 | 0.0001016 | yes |
| Mercury Retrograde Station | Nifty Bank | 85 | 3.186 | 0.3 | 2.886 | 63.53 | 6.789e-06 | 0.0001152 | yes |
| Mercury Retrograde Station | Nifty Midcap 100 | 85 | -0.2045 | 0.266 | -0.4705 | 37.65 | 0.1431 | 0.2838 | no |
| Mercury Retrograde Station | Nifty Midcap 150 | 85 | 0.4242 | 0.2642 | 0.16 | 62.35 | 0.5103 | 0.6841 | no |
| Mercury Retrograde Station | BSE Sensex | 85 | 0.06236 | 0.2506 | -0.1882 | 58.82 | 0.5101 | 0.6841 | no |
| Saturn Retrograde Station | Nifty 50 | 26 | 2.306 | 0.2178 | 2.088 | 61.54 | 0.06853 | 0.1632 | no |
| Saturn Retrograde Station | Nifty Bank | 26 | 3.001 | 0.3 | 2.701 | 65.38 | 0.04815 | 0.1249 | no |
| Saturn Retrograde Station | Nifty Midcap 100 | 26 | -0.1748 | 0.266 | -0.4408 | 30.77 | 0.5308 | 0.7014 | no |
| Saturn Retrograde Station | Nifty Midcap 150 | 26 | -0.1689 | 0.2642 | -0.4332 | 57.69 | 0.5356 | 0.7036 | no |
| Saturn Retrograde Station | BSE Sensex | 26 | -0.3246 | 0.2506 | -0.5752 | 46.15 | 0.4841 | 0.6622 | no |
| Venus Retrograde Station | Nifty 50 | 17 | 3.761 | 0.2178 | 3.543 | 82.35 | 0.00606 | 0.02493 | yes |
| Venus Retrograde Station | Nifty Bank | 17 | 3.974 | 0.3 | 3.674 | 82.35 | 0.02313 | 0.07346 | no |
| Venus Retrograde Station | Nifty Midcap 100 | 17 | 0.6628 | 0.266 | 0.3968 | 52.94 | 0.5616 | 0.7257 | no |
| Venus Retrograde Station | Nifty Midcap 150 | 17 | 1.208 | 0.2642 | 0.9435 | 70.59 | 0.1592 | 0.3081 | no |
| Venus Retrograde Station | BSE Sensex | 17 | 0.9581 | 0.2506 | 0.7075 | 64.71 | 0.3822 | 0.5648 | no |
| Jupiter Direct Station | Nifty 50 | 24 | 1.795 | 0.2178 | 1.578 | 45.83 | 0.1799 | 0.3345 | no |
| Jupiter Direct Station | Nifty Bank | 24 | 2.244 | 0.3 | 1.944 | 50 | 0.1347 | 0.2718 | no |
| Jupiter Direct Station | Nifty Midcap 100 | 24 | -0.994 | 0.266 | -1.26 | 37.5 | 0.04012 | 0.1087 | no |
| Jupiter Direct Station | Nifty Midcap 150 | 24 | -0.7936 | 0.2642 | -1.058 | 41.67 | 0.04366 | 0.1158 | no |
| Jupiter Direct Station | BSE Sensex | 24 | -1.312 | 0.2506 | -1.563 | 37.5 | 0.006207 | 0.0254 | yes |
| Mars Direct Station | Nifty 50 | 12 | 2.474 | 0.2178 | 2.257 | 66.67 | 0.1129 | 0.2375 | no |
| Mars Direct Station | Nifty Bank | 12 | 2.291 | 0.3 | 1.991 | 58.33 | 0.2281 | 0.394 | no |
| Mars Direct Station | Nifty Midcap 100 | 12 | 0.407 | 0.266 | 0.141 | 50 | 0.8525 | 0.9199 | no |
| Mars Direct Station | Nifty Midcap 150 | 12 | 0.4524 | 0.2642 | 0.1882 | 66.67 | 0.6741 | 0.8079 | no |
| Mars Direct Station | BSE Sensex | 12 | 0.473 | 0.2506 | 0.2225 | 58.33 | 0.7375 | 0.8481 | no |
| Mercury Direct Station | Nifty 50 | 84 | 2.592 | 0.2178 | 2.375 | 64.29 | 0.0002308 | 0.001842 | yes |
| Mercury Direct Station | Nifty Bank | 84 | 2.652 | 0.3 | 2.352 | 63.1 | 0.002853 | 0.01347 | yes |
| Mercury Direct Station | Nifty Midcap 100 | 84 | -0.1337 | 0.266 | -0.3997 | 42.86 | 0.3351 | 0.5142 | no |
| Mercury Direct Station | Nifty Midcap 150 | 84 | 0.2508 | 0.2642 | -0.0134 | 64.29 | 0.9721 | 0.9892 | no |
| Mercury Direct Station | BSE Sensex | 84 | -0.1652 | 0.2506 | -0.4157 | 52.38 | 0.3137 | 0.4908 | no |
| Saturn Direct Station | Nifty 50 | 26 | 3.513 | 0.2178 | 3.296 | 69.23 | 0.001739 | 0.009071 | yes |
| Saturn Direct Station | Nifty Bank | 26 | 4.329 | 0.3 | 4.029 | 69.23 | 0.0009173 | 0.00546 | yes |
| Saturn Direct Station | Nifty Midcap 100 | 26 | 0.5849 | 0.266 | 0.3188 | 42.31 | 0.6867 | 0.8141 | no |
| Saturn Direct Station | Nifty Midcap 150 | 26 | 0.9703 | 0.2642 | 0.7061 | 73.08 | 0.1198 | 0.2484 | no |
| Saturn Direct Station | BSE Sensex | 26 | 0.2767 | 0.2506 | 0.02614 | 50 | 0.9641 | 0.9862 | no |
| Venus Direct Station | Nifty 50 | 16 | 4.137 | 0.2178 | 3.919 | 81.25 | 0.002333 | 0.01129 | yes |
| Venus Direct Station | Nifty Bank | 16 | 5.063 | 0.3 | 4.763 | 93.75 | 0.00123 | 0.006989 | yes |
| Venus Direct Station | Nifty Midcap 100 | 16 | 1.056 | 0.266 | 0.7903 | 50 | 0.2471 | 0.4167 | no |
| Venus Direct Station | Nifty Midcap 150 | 16 | 1.582 | 0.2642 | 1.318 | 75 | 0.0186 | 0.063 | no |
| Venus Direct Station | BSE Sensex | 16 | 1.533 | 0.2506 | 1.282 | 68.75 | 0.07394 | 0.1727 | no |
| Jupiter-Ketu Conjunction | Nifty 50 | 3 | 5.222 | 0.2178 | 5.004 | 100 | 0.157 | 0.3048 | no |
| Jupiter-Ketu Conjunction | Nifty Bank | 3 | 6.349 | 0.3 | 6.049 | 100 | 0.1251 | 0.2567 | no |
| Jupiter-Ketu Conjunction | Nifty Midcap 100 | 3 | 0.808 | 0.266 | 0.542 | 66.67 | 0.5334 | 0.7018 | no |
| Jupiter-Ketu Conjunction | Nifty Midcap 150 | 3 | 2.607 | 0.2642 | 2.342 | 100 | 0.04725 | 0.1231 | no |
| Jupiter-Ketu Conjunction | BSE Sensex | 3 | 1.511 | 0.2506 | 1.261 | 66.67 | 0.4634 | 0.6414 | no |
| Jupiter-Mars Conjunction | Nifty 50 | 12 | 2.878 | 0.2178 | 2.661 | 50 | 0.1095 | 0.2321 | no |
| Jupiter-Mars Conjunction | Nifty Bank | 12 | 2.498 | 0.3 | 2.198 | 50 | 0.284 | 0.4596 | no |
| Jupiter-Mars Conjunction | Nifty Midcap 100 | 12 | 0.8169 | 0.266 | 0.5508 | 58.33 | 0.2457 | 0.4153 | no |
| Jupiter-Mars Conjunction | Nifty Midcap 150 | 12 | 0.1188 | 0.2642 | -0.1455 | 50 | 0.8002 | 0.8881 | no |
| Jupiter-Mars Conjunction | BSE Sensex | 12 | 0.8329 | 0.2506 | 0.5824 | 50 | 0.4802 | 0.6584 | no |
| Jupiter-Mercury Conjunction | Nifty 50 | 39 | 2.787 | 0.2178 | 2.569 | 56.41 | 0.002394 | 0.01157 | yes |
| Jupiter-Mercury Conjunction | Nifty Bank | 39 | 2.917 | 0.3 | 2.617 | 58.97 | 0.008422 | 0.0328 | yes |
| Jupiter-Mercury Conjunction | Nifty Midcap 100 | 39 | 0.4081 | 0.266 | 0.1421 | 43.59 | 0.7429 | 0.851 | no |
| Jupiter-Mercury Conjunction | Nifty Midcap 150 | 39 | 0.5206 | 0.2642 | 0.2564 | 53.85 | 0.5071 | 0.6827 | no |
| Jupiter-Mercury Conjunction | BSE Sensex | 39 | -0.06 | 0.2506 | -0.3106 | 43.59 | 0.4957 | 0.6734 | no |
| Jupiter-Moon Conjunction | Nifty 50 | 55 | 3.297 | 0.2178 | 3.08 | 63.64 | 3.224e-05 | 0.0004043 | yes |
| Jupiter-Moon Conjunction | Nifty Bank | 55 | 3.643 | 0.3 | 3.343 | 67.27 | 0.000216 | 0.001759 | yes |
| Jupiter-Moon Conjunction | Nifty Midcap 100 | 55 | 0.1157 | 0.266 | -0.1503 | 36.36 | 0.6698 | 0.8046 | no |
| Jupiter-Moon Conjunction | Nifty Midcap 150 | 55 | 0.4662 | 0.2642 | 0.2019 | 61.82 | 0.5401 | 0.7079 | no |
| Jupiter-Moon Conjunction | BSE Sensex | 55 | 0.1722 | 0.2506 | -0.07834 | 50.91 | 0.8442 | 0.9163 | no |
| Jupiter-Rahu Conjunction | Nifty 50 | 4 | 2.002 | 0.2178 | 1.784 | 50 | 0.607 | 0.7565 | no |
| Jupiter-Rahu Conjunction | Nifty Bank | 4 | 1.075 | 0.3 | 0.7755 | 50 | 0.8666 | 0.9304 | no |
| Jupiter-Rahu Conjunction | Nifty Midcap 100 | 4 | -1.201 | 0.266 | -1.467 | 25 | 0.4494 | 0.6292 | no |
| Jupiter-Rahu Conjunction | Nifty Midcap 150 | 4 | 0.06911 | 0.2642 | -0.1951 | 75 | 0.9245 | 0.9669 | no |
| Jupiter-Rahu Conjunction | BSE Sensex | 4 | -0.6045 | 0.2506 | -0.8551 | 50 | 0.7015 | 0.8237 | no |
| Jupiter-Saturn Conjunction | Nifty 50 | 2 | 7.134 | 0.2178 | 6.916 | 100 | 0.2289 | 0.3952 | no |
| Jupiter-Saturn Conjunction | Nifty Bank | 2 | 8.632 | 0.3 | 8.332 | 100 | 0.1711 | 0.3249 | no |
| Jupiter-Saturn Conjunction | Nifty Midcap 100 | 2 | 2.983 | 0.266 | 2.717 | 50 | 0.559 | 0.7248 | no |
| Jupiter-Saturn Conjunction | Nifty Midcap 150 | 2 | 3.049 | 0.2642 | 2.785 | 100 | 0.3082 | 0.4866 | no |
| Jupiter-Saturn Conjunction | BSE Sensex | 2 | 6.338 | 0.2506 | 6.087 | 100 | 0.1846 | 0.3415 | no |
| Jupiter-Sun Conjunction | Nifty 50 | 25 | 3.416 | 0.2178 | 3.198 | 72 | 0.002891 | 0.01358 | yes |
| Jupiter-Sun Conjunction | Nifty Bank | 25 | 4.224 | 0.3 | 3.924 | 80 | 0.002774 | 0.01315 | yes |
| Jupiter-Sun Conjunction | Nifty Midcap 100 | 25 | -0.01282 | 0.266 | -0.2788 | 40 | 0.6295 | 0.7765 | no |
| Jupiter-Sun Conjunction | Nifty Midcap 150 | 25 | 1.102 | 0.2642 | 0.8377 | 68 | 0.1242 | 0.2557 | no |
| Jupiter-Sun Conjunction | BSE Sensex | 25 | 0.3009 | 0.2506 | 0.05032 | 44 | 0.94 | 0.9756 | no |
| Jupiter-Venus Conjunction | Nifty 50 | 27 | 2.088 | 0.2178 | 1.87 | 51.85 | 0.06663 | 0.1599 | no |
| Jupiter-Venus Conjunction | Nifty Bank | 27 | 2.586 | 0.3 | 2.286 | 59.26 | 0.05498 | 0.1382 | no |
| Jupiter-Venus Conjunction | Nifty Midcap 100 | 27 | -0.3817 | 0.266 | -0.6477 | 33.33 | 0.07635 | 0.1767 | no |
| Jupiter-Venus Conjunction | Nifty Midcap 150 | 27 | 0.01968 | 0.2642 | -0.2446 | 51.85 | 0.597 | 0.7511 | no |
| Jupiter-Venus Conjunction | BSE Sensex | 27 | -0.2375 | 0.2506 | -0.4881 | 44.44 | 0.4026 | 0.5848 | no |
| Ketu-Mars Conjunction | Nifty 50 | 17 | 1.476 | 0.2178 | 1.258 | 58.82 | 0.379 | 0.5608 | no |
| Ketu-Mars Conjunction | Nifty Bank | 17 | 1.615 | 0.3 | 1.315 | 58.82 | 0.4647 | 0.6421 | no |
| Ketu-Mars Conjunction | Nifty Midcap 100 | 17 | -0.6499 | 0.266 | -0.9159 | 29.41 | 0.2189 | 0.3844 | no |
| Ketu-Mars Conjunction | Nifty Midcap 150 | 17 | -0.7194 | 0.2642 | -0.9837 | 52.94 | 0.2784 | 0.4549 | no |
| Ketu-Mars Conjunction | BSE Sensex | 17 | -1.389 | 0.2506 | -1.64 | 41.18 | 0.08399 | 0.1894 | no |
| Ketu-Mercury Conjunction | Nifty 50 | 28 | 3.075 | 0.2178 | 2.857 | 67.86 | 0.005301 | 0.02236 | yes |
| Ketu-Mercury Conjunction | Nifty Bank | 28 | 3.554 | 0.3 | 3.254 | 64.29 | 0.008123 | 0.03179 | yes |
| Ketu-Mercury Conjunction | Nifty Midcap 100 | 28 | 0.5095 | 0.266 | 0.2435 | 46.43 | 0.4366 | 0.6173 | no |
| Ketu-Mercury Conjunction | Nifty Midcap 150 | 28 | 0.7172 | 0.2642 | 0.453 | 67.86 | 0.3317 | 0.511 | no |
| Ketu-Mercury Conjunction | BSE Sensex | 28 | 0.3807 | 0.2506 | 0.1301 | 53.57 | 0.7969 | 0.8854 | no |
| Ketu-Moon Conjunction | Nifty 50 | 57 | 3.297 | 0.2178 | 3.079 | 68.42 | 1.705e-05 | 0.0002488 | yes |
| Ketu-Moon Conjunction | Nifty Bank | 57 | 3.726 | 0.3 | 3.426 | 57.89 | 4.114e-05 | 0.0004806 | yes |
| Ketu-Moon Conjunction | Nifty Midcap 100 | 57 | 0.1268 | 0.266 | -0.1392 | 43.86 | 0.6922 | 0.8183 | no |
| Ketu-Moon Conjunction | Nifty Midcap 150 | 57 | 0.4116 | 0.2642 | 0.1474 | 66.67 | 0.6627 | 0.7996 | no |
| Ketu-Moon Conjunction | BSE Sensex | 57 | 0.5057 | 0.2506 | 0.2551 | 54.39 | 0.5676 | 0.7282 | no |
| Ketu-Saturn Conjunction | Nifty 50 | 2 | -1.554 | 0.2178 | -1.771 | 50 | 0.5913 | 0.7471 | no |
| Ketu-Saturn Conjunction | Nifty Bank | 2 | -1.772 | 0.3 | -2.072 | 50 | 0.7336 | 0.8454 | no |
| Ketu-Saturn Conjunction | Nifty Midcap 100 | 2 | -1.123 | 0.266 | -1.389 | 50 | 0.5147 | 0.6878 | no |
| Ketu-Saturn Conjunction | Nifty Midcap 150 | 2 | -1.792 | 0.2642 | -2.056 | 50 | 0.5966 | 0.7511 | no |
| Ketu-Saturn Conjunction | BSE Sensex | 2 | -1.912 | 0.2506 | -2.162 | 50 | 0.576 | 0.7342 | no |
| Ketu-Sun Conjunction | Nifty 50 | 29 | 2.513 | 0.2178 | 2.295 | 55.17 | 0.02786 | 0.08406 | no |
| Ketu-Sun Conjunction | Nifty Bank | 29 | 2.732 | 0.3 | 2.432 | 55.17 | 0.04765 | 0.1238 | no |
| Ketu-Sun Conjunction | Nifty Midcap 100 | 29 | 0.3909 | 0.266 | 0.1248 | 41.38 | 0.7999 | 0.888 | no |
| Ketu-Sun Conjunction | Nifty Midcap 150 | 29 | -0.02152 | 0.2642 | -0.2858 | 55.17 | 0.5211 | 0.6939 | no |
| Ketu-Sun Conjunction | BSE Sensex | 29 | -0.9889 | 0.2506 | -1.239 | 34.48 | 0.01914 | 0.06436 | no |
| Ketu-Venus Conjunction | Nifty 50 | 29 | 2.733 | 0.2178 | 2.515 | 75.86 | 0.01173 | 0.04321 | yes |
| Ketu-Venus Conjunction | Nifty Bank | 29 | 3.227 | 0.3 | 2.927 | 72.41 | 0.009377 | 0.03581 | yes |
| Ketu-Venus Conjunction | Nifty Midcap 100 | 29 | 0.5009 | 0.266 | 0.2349 | 48.28 | 0.6676 | 0.8036 | no |
| Ketu-Venus Conjunction | Nifty Midcap 150 | 29 | 0.4392 | 0.2642 | 0.175 | 72.41 | 0.7183 | 0.8361 | no |
| Ketu-Venus Conjunction | BSE Sensex | 29 | 0.5649 | 0.2506 | 0.3143 | 62.07 | 0.5643 | 0.7258 | no |
| Mars-Mercury Conjunction | Nifty 50 | 43 | 1.878 | 0.2178 | 1.66 | 65.12 | 0.03318 | 0.09549 | no |
| Mars-Mercury Conjunction | Nifty Bank | 43 | 2.121 | 0.3 | 1.821 | 65.12 | 0.04804 | 0.1247 | no |
| Mars-Mercury Conjunction | Nifty Midcap 100 | 43 | -0.5072 | 0.266 | -0.7732 | 41.86 | 0.1268 | 0.2598 | no |
| Mars-Mercury Conjunction | Nifty Midcap 150 | 43 | -0.04662 | 0.2642 | -0.3109 | 65.12 | 0.4261 | 0.6078 | no |
| Mars-Mercury Conjunction | BSE Sensex | 43 | -0.2538 | 0.2506 | -0.5043 | 58.14 | 0.2146 | 0.3781 | no |
| Mars-Moon Conjunction | Nifty 50 | 54 | 2.278 | 0.2178 | 2.06 | 62.96 | 0.003425 | 0.01565 | yes |
| Mars-Moon Conjunction | Nifty Bank | 54 | 2.611 | 0.3 | 2.311 | 62.96 | 0.007003 | 0.02797 | yes |
| Mars-Moon Conjunction | Nifty Midcap 100 | 54 | -0.3853 | 0.266 | -0.6513 | 37.04 | 0.07767 | 0.179 | no |
| Mars-Moon Conjunction | Nifty Midcap 150 | 54 | 0.2199 | 0.2642 | -0.04438 | 62.96 | 0.8931 | 0.9466 | no |
| Mars-Moon Conjunction | BSE Sensex | 54 | -0.2034 | 0.2506 | -0.454 | 53.7 | 0.176 | 0.33 | no |
| Mars-Rahu Conjunction | Nifty 50 | 16 | 3.137 | 0.2178 | 2.919 | 68.75 | 0.02918 | 0.08691 | no |
| Mars-Rahu Conjunction | Nifty Bank | 16 | 3.074 | 0.3 | 2.774 | 68.75 | 0.1054 | 0.2251 | no |
| Mars-Rahu Conjunction | Nifty Midcap 100 | 16 | 0.2327 | 0.266 | -0.03334 | 37.5 | 0.9557 | 0.982 | no |
| Mars-Rahu Conjunction | Nifty Midcap 150 | 16 | 0.5239 | 0.2642 | 0.2597 | 75 | 0.5485 | 0.7152 | no |
| Mars-Rahu Conjunction | BSE Sensex | 16 | 0.1872 | 0.2506 | -0.06341 | 50 | 0.9246 | 0.9669 | no |
| Mars-Saturn Conjunction | Nifty 50 | 14 | 2.892 | 0.2178 | 2.674 | 71.43 | 0.07596 | 0.176 | no |
| Mars-Saturn Conjunction | Nifty Bank | 14 | 3.304 | 0.3 | 3.004 | 64.29 | 0.06634 | 0.1593 | no |
| Mars-Saturn Conjunction | Nifty Midcap 100 | 14 | -1.908 | 0.266 | -2.174 | 21.43 | 0.07965 | 0.1822 | no |
| Mars-Saturn Conjunction | Nifty Midcap 150 | 14 | 0.5639 | 0.2642 | 0.2996 | 71.43 | 0.6865 | 0.8141 | no |
| Mars-Saturn Conjunction | BSE Sensex | 14 | -0.7169 | 0.2506 | -0.9674 | 57.14 | 0.3332 | 0.512 | no |
| Mars-Sun Conjunction | Nifty 50 | 13 | 4.533 | 0.2178 | 4.315 | 76.92 | 0.004496 | 0.01949 | yes |
| Mars-Sun Conjunction | Nifty Bank | 13 | 5.359 | 0.3 | 5.059 | 92.31 | 0.001902 | 0.009772 | yes |
| Mars-Sun Conjunction | Nifty Midcap 100 | 13 | -0.3909 | 0.266 | -0.6569 | 23.08 | 0.1965 | 0.3556 | no |
| Mars-Sun Conjunction | Nifty Midcap 150 | 13 | 2.177 | 0.2642 | 1.913 | 84.62 | 0.02605 | 0.07975 | no |
| Mars-Sun Conjunction | BSE Sensex | 13 | 2.182 | 0.2506 | 1.932 | 76.92 | 0.02317 | 0.07348 | no |
| Mars-Venus Conjunction | Nifty 50 | 21 | 2.731 | 0.2178 | 2.513 | 61.9 | 0.02194 | 0.07068 | no |
| Mars-Venus Conjunction | Nifty Bank | 21 | 3.513 | 0.3 | 3.213 | 66.67 | 0.01272 | 0.0463 | yes |
| Mars-Venus Conjunction | Nifty Midcap 100 | 21 | 0.3583 | 0.266 | 0.0923 | 38.1 | 0.9149 | 0.9623 | no |
| Mars-Venus Conjunction | Nifty Midcap 150 | 21 | 0.8765 | 0.2642 | 0.6123 | 57.14 | 0.2541 | 0.4265 | no |
| Mars-Venus Conjunction | BSE Sensex | 21 | 0.2542 | 0.2506 | 0.003632 | 42.86 | 0.9951 | 0.9976 | no |
| Mercury-Moon Conjunction | Nifty 50 | 57 | 2.894 | 0.2178 | 2.676 | 68.42 | 0.0006101 | 0.003958 | yes |
| Mercury-Moon Conjunction | Nifty Bank | 57 | 3.425 | 0.3 | 3.125 | 68.42 | 0.0008795 | 0.005311 | yes |
| Mercury-Moon Conjunction | Nifty Midcap 100 | 57 | -0.3649 | 0.266 | -0.6309 | 36.84 | 0.1965 | 0.3556 | no |
| Mercury-Moon Conjunction | Nifty Midcap 150 | 57 | 0.7866 | 0.2642 | 0.5224 | 66.67 | 0.3254 | 0.5035 | no |
| Mercury-Moon Conjunction | BSE Sensex | 57 | 0.4598 | 0.2506 | 0.2093 | 61.4 | 0.7107 | 0.8312 | no |
| Mercury-Rahu Conjunction | Nifty 50 | 42 | 1.764 | 0.2178 | 1.546 | 66.67 | 0.03964 | 0.1078 | no |
| Mercury-Rahu Conjunction | Nifty Bank | 42 | 1.778 | 0.3 | 1.478 | 69.05 | 0.1234 | 0.2544 | no |
| Mercury-Rahu Conjunction | Nifty Midcap 100 | 42 | -0.04448 | 0.266 | -0.3105 | 40.48 | 0.4363 | 0.6173 | no |
| Mercury-Rahu Conjunction | Nifty Midcap 150 | 42 | 0.2129 | 0.2642 | -0.05132 | 66.67 | 0.9111 | 0.9595 | no |
| Mercury-Rahu Conjunction | BSE Sensex | 42 | -0.0591 | 0.2506 | -0.3097 | 59.52 | 0.5251 | 0.6971 | no |
| Mercury-Saturn Conjunction | Nifty 50 | 32 | 3.051 | 0.2178 | 2.833 | 65.62 | 0.0008392 | 0.005134 | yes |
| Mercury-Saturn Conjunction | Nifty Bank | 32 | 3.615 | 0.3 | 3.315 | 71.88 | 0.0009029 | 0.0054 | yes |
| Mercury-Saturn Conjunction | Nifty Midcap 100 | 32 | 0.8028 | 0.266 | 0.5368 | 46.88 | 0.4053 | 0.5875 | no |
| Mercury-Saturn Conjunction | Nifty Midcap 150 | 32 | 1.025 | 0.2642 | 0.7604 | 68.75 | 0.02536 | 0.07841 | no |
| Mercury-Saturn Conjunction | BSE Sensex | 32 | 0.6481 | 0.2506 | 0.3976 | 62.5 | 0.3712 | 0.5533 | no |
| Mercury-Sun Conjunction | Nifty 50 | 168 | 3.162 | 0.2178 | 2.944 | 72.02 | 2.654e-13 | 2.211e-11 | yes |
| Mercury-Sun Conjunction | Nifty Bank | 168 | 3.805 | 0.3 | 3.505 | 69.64 | 1.434e-13 | 1.25e-11 | yes |
| Mercury-Sun Conjunction | Nifty Midcap 100 | 168 | 0.3226 | 0.266 | 0.05657 | 41.07 | 0.8054 | 0.891 | no |
| Mercury-Sun Conjunction | Nifty Midcap 150 | 168 | 0.7144 | 0.2642 | 0.4502 | 69.05 | 0.02543 | 0.07842 | no |
| Mercury-Sun Conjunction | BSE Sensex | 168 | 0.4046 | 0.2506 | 0.154 | 55.36 | 0.5011 | 0.6771 | no |
| Mercury-Venus Conjunction | Nifty 50 | 61 | 2.933 | 0.2178 | 2.715 | 72.13 | 7.818e-05 | 0.0008076 | yes |
| Mercury-Venus Conjunction | Nifty Bank | 61 | 3.185 | 0.3 | 2.885 | 70.49 | 0.0005386 | 0.003631 | yes |
| Mercury-Venus Conjunction | Nifty Midcap 100 | 61 | 0.2685 | 0.266 | 0.002452 | 42.62 | 0.9952 | 0.9976 | no |
| Mercury-Venus Conjunction | Nifty Midcap 150 | 61 | 0.8287 | 0.2642 | 0.5645 | 70.49 | 0.1395 | 0.2786 | no |
| Mercury-Venus Conjunction | BSE Sensex | 61 | 0.3596 | 0.2506 | 0.1091 | 60.66 | 0.7964 | 0.8854 | no |
| Moon-Rahu Conjunction | Nifty 50 | 54 | 3.089 | 0.2178 | 2.871 | 68.52 | 0.0002346 | 0.001864 | yes |
| Moon-Rahu Conjunction | Nifty Bank | 54 | 3.366 | 0.3 | 3.066 | 68.52 | 0.001348 | 0.007413 | yes |
| Moon-Rahu Conjunction | Nifty Midcap 100 | 54 | -0.1495 | 0.266 | -0.4155 | 40.74 | 0.221 | 0.3854 | no |
| Moon-Rahu Conjunction | Nifty Midcap 150 | 54 | 0.7504 | 0.2642 | 0.4861 | 66.67 | 0.2911 | 0.466 | no |
| Moon-Rahu Conjunction | BSE Sensex | 54 | 0.574 | 0.2506 | 0.3234 | 59.26 | 0.4728 | 0.6502 | no |
| Moon-Saturn Conjunction | Nifty 50 | 55 | 2.861 | 0.2178 | 2.643 | 63.64 | 0.000169 | 0.001484 | yes |
| Moon-Saturn Conjunction | Nifty Bank | 55 | 3.458 | 0.3 | 3.158 | 63.64 | 0.0002047 | 0.0017 | yes |
| Moon-Saturn Conjunction | Nifty Midcap 100 | 55 | -0.407 | 0.266 | -0.6731 | 29.09 | 0.114 | 0.239 | no |
| Moon-Saturn Conjunction | Nifty Midcap 150 | 55 | 0.3401 | 0.2642 | 0.07588 | 60 | 0.7964 | 0.8854 | no |
| Moon-Saturn Conjunction | BSE Sensex | 55 | 0.2483 | 0.2506 | -0.002271 | 54.55 | 0.9948 | 0.9976 | no |
| Moon-Sun Conjunction | Nifty 50 | 60 | 3.242 | 0.2178 | 3.025 | 73.33 | 1.237e-05 | 0.000191 | yes |
| Moon-Sun Conjunction | Nifty Bank | 60 | 3.836 | 0.3 | 3.536 | 76.67 | 7.706e-06 | 0.0001267 | yes |
| Moon-Sun Conjunction | Nifty Midcap 100 | 60 | -0.0258 | 0.266 | -0.2918 | 43.33 | 0.4967 | 0.6739 | no |
| Moon-Sun Conjunction | Nifty Midcap 150 | 60 | 1.023 | 0.2642 | 0.7587 | 75 | 0.04266 | 0.1137 | no |
| Moon-Sun Conjunction | BSE Sensex | 60 | 0.5628 | 0.2506 | 0.3123 | 60 | 0.4506 | 0.6302 | no |
| Moon-Venus Conjunction | Nifty 50 | 44 | 1.757 | 0.2178 | 1.539 | 61.36 | 0.03053 | 0.08979 | no |
| Moon-Venus Conjunction | Nifty Bank | 44 | 1.912 | 0.3 | 1.612 | 56.82 | 0.05582 | 0.14 | no |
| Moon-Venus Conjunction | Nifty Midcap 100 | 44 | -0.2711 | 0.266 | -0.5371 | 36.36 | 0.3173 | 0.4943 | no |
| Moon-Venus Conjunction | Nifty Midcap 150 | 44 | 0.03826 | 0.2642 | -0.226 | 61.36 | 0.494 | 0.6724 | no |
| Moon-Venus Conjunction | BSE Sensex | 44 | -0.1416 | 0.2506 | -0.3922 | 50 | 0.322 | 0.4997 | no |
| Rahu-Saturn Conjunction | Nifty 50 | 3 | 4.878 | 0.2178 | 4.66 | 100 | 0.2208 | 0.3854 | no |
| Rahu-Saturn Conjunction | Nifty Bank | 3 | 6.013 | 0.3 | 5.713 | 100 | 0.1737 | 0.3269 | no |
| Rahu-Saturn Conjunction | Nifty Midcap 100 | 3 | 2.752 | 0.266 | 2.486 | 66.67 | 0.3334 | 0.512 | no |
| Rahu-Saturn Conjunction | Nifty Midcap 150 | 3 | 2.19 | 0.2642 | 1.926 | 100 | 0.2122 | 0.3749 | no |
| Rahu-Saturn Conjunction | BSE Sensex | 3 | 2.076 | 0.2506 | 1.826 | 100 | 0.2759 | 0.453 | no |
| Rahu-Sun Conjunction | Nifty 50 | 28 | 2.879 | 0.2178 | 2.661 | 71.43 | 0.008166 | 0.03186 | yes |
| Rahu-Sun Conjunction | Nifty Bank | 28 | 2.757 | 0.3 | 2.457 | 60.71 | 0.04552 | 0.1196 | no |
| Rahu-Sun Conjunction | Nifty Midcap 100 | 28 | 0.4431 | 0.266 | 0.1771 | 42.86 | 0.7556 | 0.8594 | no |
| Rahu-Sun Conjunction | Nifty Midcap 150 | 28 | 0.6559 | 0.2642 | 0.3916 | 71.43 | 0.4065 | 0.5885 | no |
| Rahu-Sun Conjunction | BSE Sensex | 28 | -0.3074 | 0.2506 | -0.558 | 53.57 | 0.3967 | 0.5802 | no |
| Rahu-Venus Conjunction | Nifty 50 | 30 | 1.567 | 0.2178 | 1.349 | 50 | 0.1939 | 0.3523 | no |
| Rahu-Venus Conjunction | Nifty Bank | 30 | 1.924 | 0.3 | 1.624 | 53.33 | 0.1861 | 0.3428 | no |
| Rahu-Venus Conjunction | Nifty Midcap 100 | 30 | -1.225 | 0.266 | -1.492 | 26.67 | 0.02972 | 0.08817 | no |
| Rahu-Venus Conjunction | Nifty Midcap 150 | 30 | -0.7016 | 0.2642 | -0.9658 | 50 | 0.06261 | 0.1533 | no |
| Rahu-Venus Conjunction | BSE Sensex | 30 | -1.479 | 0.2506 | -1.73 | 26.67 | 0.001279 | 0.007175 | yes |
| Saturn-Sun Conjunction | Nifty 50 | 26 | 2.748 | 0.2178 | 2.53 | 57.69 | 0.01664 | 0.05708 | no |
| Saturn-Sun Conjunction | Nifty Bank | 26 | 3.333 | 0.3 | 3.033 | 57.69 | 0.0166 | 0.05701 | no |
| Saturn-Sun Conjunction | Nifty Midcap 100 | 26 | -0.1789 | 0.266 | -0.4449 | 26.92 | 0.1832 | 0.339 | no |
| Saturn-Sun Conjunction | Nifty Midcap 150 | 26 | 0.5266 | 0.2642 | 0.2623 | 61.54 | 0.5672 | 0.7282 | no |
| Saturn-Sun Conjunction | BSE Sensex | 26 | 0.2441 | 0.2506 | -0.006433 | 50 | 0.9905 | 0.9964 | no |
| Saturn-Venus Conjunction | Nifty 50 | 30 | 2.731 | 0.2178 | 2.513 | 63.33 | 0.01688 | 0.05765 | no |
| Saturn-Venus Conjunction | Nifty Bank | 30 | 2.917 | 0.3 | 2.617 | 66.67 | 0.03937 | 0.1074 | no |
| Saturn-Venus Conjunction | Nifty Midcap 100 | 30 | 0.02448 | 0.266 | -0.2415 | 43.33 | 0.42 | 0.6018 | no |
| Saturn-Venus Conjunction | Nifty Midcap 150 | 30 | -0.01546 | 0.2642 | -0.2797 | 60 | 0.6515 | 0.7932 | no |
| Saturn-Venus Conjunction | BSE Sensex | 30 | -0.3058 | 0.2506 | -0.5563 | 50 | 0.3552 | 0.5353 | no |
| Sun-Venus Conjunction | Nifty 50 | 34 | 3.501 | 0.2178 | 3.284 | 76.47 | 0.0003889 | 0.002821 | yes |
| Sun-Venus Conjunction | Nifty Bank | 34 | 3.384 | 0.3 | 3.084 | 61.76 | 0.004266 | 0.01865 | yes |
| Sun-Venus Conjunction | Nifty Midcap 100 | 34 | 1.051 | 0.266 | 0.7846 | 50 | 0.1437 | 0.2846 | no |
| Sun-Venus Conjunction | Nifty Midcap 150 | 34 | 1.147 | 0.2642 | 0.8824 | 76.47 | 0.06733 | 0.1609 | no |
| Sun-Venus Conjunction | BSE Sensex | 34 | 0.8256 | 0.2506 | 0.575 | 67.65 | 0.2387 | 0.4066 | no |
| Jupiter-Ketu Opposition | Nifty 50 | 4 | 2.002 | 0.2178 | 1.784 | 50 | 0.607 | 0.7565 | no |
| Jupiter-Ketu Opposition | Nifty Bank | 4 | 1.075 | 0.3 | 0.7755 | 50 | 0.8666 | 0.9304 | no |
| Jupiter-Ketu Opposition | Nifty Midcap 100 | 4 | -1.201 | 0.266 | -1.467 | 25 | 0.4494 | 0.6292 | no |
| Jupiter-Ketu Opposition | Nifty Midcap 150 | 4 | 0.06911 | 0.2642 | -0.1951 | 75 | 0.9245 | 0.9669 | no |
| Jupiter-Ketu Opposition | BSE Sensex | 4 | -0.6045 | 0.2506 | -0.8551 | 50 | 0.7015 | 0.8237 | no |
| Jupiter-Ketu Square | Nifty 50 | 8 | 4.077 | 0.2178 | 3.859 | 75 | 0.06384 | 0.1552 | no |
| Jupiter-Ketu Square | Nifty Bank | 8 | 4.799 | 0.3 | 4.499 | 75 | 0.04589 | 0.1204 | no |
| Jupiter-Ketu Square | Nifty Midcap 100 | 8 | 0.3051 | 0.266 | 0.03911 | 37.5 | 0.9649 | 0.9862 | no |
| Jupiter-Ketu Square | Nifty Midcap 150 | 8 | -0.1319 | 0.2642 | -0.3962 | 62.5 | 0.7675 | 0.8687 | no |
| Jupiter-Ketu Square | BSE Sensex | 8 | -0.5866 | 0.2506 | -0.8371 | 50 | 0.6045 | 0.7556 | no |
| Jupiter-Ketu Trine | Nifty 50 | 8 | 3.36 | 0.2178 | 3.142 | 87.5 | 0.07245 | 0.1701 | no |
| Jupiter-Ketu Trine | Nifty Bank | 8 | 3.59 | 0.3 | 3.29 | 87.5 | 0.1089 | 0.231 | no |
| Jupiter-Ketu Trine | Nifty Midcap 100 | 8 | -0.4667 | 0.266 | -0.7328 | 50 | 0.4448 | 0.6249 | no |
| Jupiter-Ketu Trine | Nifty Midcap 150 | 8 | 1.36 | 0.2642 | 1.095 | 75 | 0.09443 | 0.2083 | no |
| Jupiter-Ketu Trine | BSE Sensex | 8 | 1.529 | 0.2506 | 1.278 | 62.5 | 0.1639 | 0.3154 | no |
| Jupiter-Mars Opposition | Nifty 50 | 20 | 5.08 | 0.2178 | 4.862 | 80 | 0.00041 | 0.002945 | yes |
| Jupiter-Mars Opposition | Nifty Bank | 20 | 6.081 | 0.3 | 5.781 | 80 | 0.0001187 | 0.001129 | yes |
| Jupiter-Mars Opposition | Nifty Midcap 100 | 20 | 0.1886 | 0.266 | -0.07739 | 30 | 0.8764 | 0.9372 | no |
| Jupiter-Mars Opposition | Nifty Midcap 150 | 20 | 1.478 | 0.2642 | 1.214 | 80 | 0.03324 | 0.0955 | no |
| Jupiter-Mars Opposition | BSE Sensex | 20 | 0.8479 | 0.2506 | 0.5973 | 65 | 0.4649 | 0.6421 | no |
| Jupiter-Mars Square | Nifty 50 | 28 | 2.071 | 0.2178 | 1.854 | 64.29 | 0.0682 | 0.1625 | no |
| Jupiter-Mars Square | Nifty Bank | 28 | 2.445 | 0.3 | 2.145 | 57.14 | 0.06445 | 0.1561 | no |
| Jupiter-Mars Square | Nifty Midcap 100 | 28 | -0.2105 | 0.266 | -0.4765 | 39.29 | 0.3834 | 0.5656 | no |
| Jupiter-Mars Square | Nifty Midcap 150 | 28 | -0.1722 | 0.2642 | -0.4365 | 57.14 | 0.3946 | 0.5783 | no |
| Jupiter-Mars Square | BSE Sensex | 28 | -0.6816 | 0.2506 | -0.9322 | 50 | 0.1119 | 0.2361 | no |
| Jupiter-Mars Trine | Nifty 50 | 26 | 2.091 | 0.2178 | 1.873 | 53.85 | 0.06587 | 0.1585 | no |
| Jupiter-Mars Trine | Nifty Bank | 26 | 2.489 | 0.3 | 2.189 | 57.69 | 0.06183 | 0.1521 | no |
| Jupiter-Mars Trine | Nifty Midcap 100 | 26 | 0.2693 | 0.266 | 0.003248 | 42.31 | 0.995 | 0.9976 | no |
| Jupiter-Mars Trine | Nifty Midcap 150 | 26 | -0.4878 | 0.2642 | -0.752 | 42.31 | 0.06622 | 0.1591 | no |
| Jupiter-Mars Trine | BSE Sensex | 26 | -0.7098 | 0.2506 | -0.9603 | 34.62 | 0.0463 | 0.1213 | no |
| Jupiter-Mercury Opposition | Nifty 50 | 28 | 2.927 | 0.2178 | 2.709 | 71.43 | 0.002592 | 0.0124 | yes |
| Jupiter-Mercury Opposition | Nifty Bank | 28 | 2.932 | 0.3 | 2.632 | 60.71 | 0.01378 | 0.04906 | yes |
| Jupiter-Mercury Opposition | Nifty Midcap 100 | 28 | 1.129 | 0.266 | 0.8632 | 57.14 | 0.03712 | 0.1037 | no |
| Jupiter-Mercury Opposition | Nifty Midcap 150 | 28 | 0.3178 | 0.2642 | 0.05356 | 64.29 | 0.9237 | 0.9669 | no |
| Jupiter-Mercury Opposition | BSE Sensex | 28 | 0.1925 | 0.2506 | -0.05809 | 64.29 | 0.9149 | 0.9623 | no |
| Jupiter-Mercury Square | Nifty 50 | 65 | 2.972 | 0.2178 | 2.754 | 66.15 | 0.0001911 | 0.001633 | yes |
| Jupiter-Mercury Square | Nifty Bank | 65 | 3.683 | 0.3 | 3.383 | 66.15 | 0.0001086 | 0.001049 | yes |
| Jupiter-Mercury Square | Nifty Midcap 100 | 65 | 0.01289 | 0.266 | -0.2531 | 40 | 0.5645 | 0.7258 | no |
| Jupiter-Mercury Square | Nifty Midcap 150 | 65 | 0.6562 | 0.2642 | 0.3919 | 64.62 | 0.3883 | 0.5706 | no |
| Jupiter-Mercury Square | BSE Sensex | 65 | 0.4667 | 0.2506 | 0.2161 | 55.38 | 0.696 | 0.82 | no |
| Jupiter-Mercury Trine | Nifty 50 | 63 | 2.501 | 0.2178 | 2.283 | 73.02 | 0.0002957 | 0.002249 | yes |
| Jupiter-Mercury Trine | Nifty Bank | 63 | 2.88 | 0.3 | 2.58 | 69.84 | 0.0005369 | 0.003628 | yes |
| Jupiter-Mercury Trine | Nifty Midcap 100 | 63 | -0.03839 | 0.266 | -0.3044 | 39.68 | 0.3195 | 0.4967 | no |
| Jupiter-Mercury Trine | Nifty Midcap 150 | 63 | 0.2169 | 0.2642 | -0.04738 | 68.25 | 0.8763 | 0.9372 | no |
| Jupiter-Mercury Trine | BSE Sensex | 63 | -0.3471 | 0.2506 | -0.5977 | 55.56 | 0.08847 | 0.1975 | no |
| Jupiter-Moon Opposition | Nifty 50 | 56 | 3.634 | 0.2178 | 3.417 | 66.07 | 2.918e-06 | 6.046e-05 | yes |
| Jupiter-Moon Opposition | Nifty Bank | 56 | 4.153 | 0.3 | 3.853 | 69.64 | 4.728e-06 | 8.662e-05 | yes |
| Jupiter-Moon Opposition | Nifty Midcap 100 | 56 | 0.2699 | 0.266 | 0.003898 | 39.29 | 0.9897 | 0.9958 | no |
| Jupiter-Moon Opposition | Nifty Midcap 150 | 56 | 0.7393 | 0.2642 | 0.4751 | 67.86 | 0.1455 | 0.2877 | no |
| Jupiter-Moon Opposition | BSE Sensex | 56 | 0.6119 | 0.2506 | 0.3614 | 57.14 | 0.3324 | 0.5119 | no |
| Jupiter-Moon Square | Nifty 50 | 122 | 2.831 | 0.2178 | 2.614 | 68.85 | 1.257e-07 | 4.405e-06 | yes |
| Jupiter-Moon Square | Nifty Bank | 122 | 3.255 | 0.3 | 2.955 | 66.39 | 3.238e-07 | 9.871e-06 | yes |
| Jupiter-Moon Square | Nifty Midcap 100 | 122 | 0.2484 | 0.266 | -0.01762 | 45.9 | 0.9537 | 0.982 | no |
| Jupiter-Moon Square | Nifty Midcap 150 | 122 | 0.8298 | 0.2642 | 0.5656 | 66.39 | 0.0632 | 0.1544 | no |
| Jupiter-Moon Square | BSE Sensex | 122 | 0.262 | 0.2506 | 0.01139 | 58.2 | 0.9739 | 0.9895 | no |
| Jupiter-Moon Trine | Nifty 50 | 96 | 2.854 | 0.2178 | 2.636 | 70.83 | 5.39e-07 | 1.413e-05 | yes |
| Jupiter-Moon Trine | Nifty Bank | 96 | 3.121 | 0.3 | 2.821 | 65.62 | 3.455e-06 | 6.82e-05 | yes |
| Jupiter-Moon Trine | Nifty Midcap 100 | 96 | 0.2689 | 0.266 | 0.002927 | 45.83 | 0.9919 | 0.9968 | no |
| Jupiter-Moon Trine | Nifty Midcap 150 | 96 | 0.5863 | 0.2642 | 0.3221 | 69.79 | 0.1664 | 0.3183 | no |
| Jupiter-Moon Trine | BSE Sensex | 96 | 0.3546 | 0.2506 | 0.104 | 59.38 | 0.7213 | 0.8384 | no |
| Jupiter-Rahu Opposition | Nifty 50 | 3 | 5.222 | 0.2178 | 5.004 | 100 | 0.157 | 0.3048 | no |
| Jupiter-Rahu Opposition | Nifty Bank | 3 | 6.349 | 0.3 | 6.049 | 100 | 0.1251 | 0.2567 | no |
| Jupiter-Rahu Opposition | Nifty Midcap 100 | 3 | 0.808 | 0.266 | 0.542 | 66.67 | 0.5334 | 0.7018 | no |
| Jupiter-Rahu Opposition | Nifty Midcap 150 | 3 | 2.607 | 0.2642 | 2.342 | 100 | 0.04725 | 0.1231 | no |
| Jupiter-Rahu Opposition | BSE Sensex | 3 | 1.511 | 0.2506 | 1.261 | 66.67 | 0.4634 | 0.6414 | no |
| Jupiter-Rahu Square | Nifty 50 | 8 | 4.077 | 0.2178 | 3.859 | 75 | 0.06384 | 0.1552 | no |
| Jupiter-Rahu Square | Nifty Bank | 8 | 4.799 | 0.3 | 4.499 | 75 | 0.04589 | 0.1204 | no |
| Jupiter-Rahu Square | Nifty Midcap 100 | 8 | 0.3051 | 0.266 | 0.03911 | 37.5 | 0.9649 | 0.9862 | no |
| Jupiter-Rahu Square | Nifty Midcap 150 | 8 | -0.1319 | 0.2642 | -0.3962 | 62.5 | 0.7675 | 0.8687 | no |
| Jupiter-Rahu Square | BSE Sensex | 8 | -0.5866 | 0.2506 | -0.8371 | 50 | 0.6045 | 0.7556 | no |
| Jupiter-Rahu Trine | Nifty 50 | 9 | 4.744 | 0.2178 | 4.526 | 77.78 | 0.02299 | 0.07316 | no |
| Jupiter-Rahu Trine | Nifty Bank | 9 | 5.002 | 0.3 | 4.702 | 77.78 | 0.04535 | 0.1193 | no |
| Jupiter-Rahu Trine | Nifty Midcap 100 | 9 | 0.6893 | 0.266 | 0.4233 | 44.44 | 0.3975 | 0.5805 | no |
| Jupiter-Rahu Trine | Nifty Midcap 150 | 9 | 1.295 | 0.2642 | 1.031 | 88.89 | 0.03857 | 0.1063 | no |
| Jupiter-Rahu Trine | BSE Sensex | 9 | 1.719 | 0.2506 | 1.468 | 77.78 | 0.05034 | 0.1289 | no |
| Jupiter-Saturn Opposition | Nifty 50 | 3 | 3.026 | 0.2178 | 2.809 | 100 | 0.02515 | 0.07793 | no |
| Jupiter-Saturn Opposition | Nifty Bank | 3 | 3.122 | 0.3 | 2.822 | 100 | 0.01974 | 0.06552 | no |
| Jupiter-Saturn Opposition | Nifty Midcap 100 | 3 | 2.948 | 0.266 | 2.682 | 100 | 0.1375 | 0.2754 | no |
| Jupiter-Saturn Opposition | Nifty Midcap 150 | 3 | 3.062 | 0.2642 | 2.798 | 100 | 0.02647 | 0.08069 | no |
| Jupiter-Saturn Opposition | BSE Sensex | 3 | 2.959 | 0.2506 | 2.708 | 100 | 0.04293 | 0.1143 | no |
| Jupiter-Saturn Square | Nifty 50 | 9 | 3.837 | 0.2178 | 3.62 | 77.78 | 0.04224 | 0.1128 | no |
| Jupiter-Saturn Square | Nifty Bank | 9 | 4.243 | 0.3 | 3.943 | 88.89 | 0.04734 | 0.1232 | no |
| Jupiter-Saturn Square | Nifty Midcap 100 | 9 | 0.1949 | 0.266 | -0.07114 | 44.44 | 0.8417 | 0.9146 | no |
| Jupiter-Saturn Square | Nifty Midcap 150 | 9 | 0.4458 | 0.2642 | 0.1816 | 66.67 | 0.7778 | 0.8736 | no |
| Jupiter-Saturn Square | BSE Sensex | 9 | 0.3912 | 0.2506 | 0.1406 | 55.56 | 0.8323 | 0.9097 | no |
| Jupiter-Saturn Trine | Nifty 50 | 10 | 1.161 | 0.2178 | 0.9436 | 60 | 0.5935 | 0.7488 | no |
| Jupiter-Saturn Trine | Nifty Bank | 10 | 1.899 | 0.3 | 1.599 | 40 | 0.433 | 0.6156 | no |
| Jupiter-Saturn Trine | Nifty Midcap 100 | 10 | -0.09677 | 0.266 | -0.3628 | 50 | 0.8339 | 0.9109 | no |
| Jupiter-Saturn Trine | Nifty Midcap 150 | 10 | -0.2381 | 0.2642 | -0.5024 | 60 | 0.6547 | 0.7938 | no |
| Jupiter-Saturn Trine | BSE Sensex | 10 | -0.2091 | 0.2506 | -0.4597 | 50 | 0.697 | 0.8201 | no |
| Jupiter-Sun Opposition | Nifty 50 | 24 | 2.671 | 0.2178 | 2.453 | 62.5 | 0.02846 | 0.08543 | no |
| Jupiter-Sun Opposition | Nifty Bank | 24 | 3.182 | 0.3 | 2.882 | 70.83 | 0.02536 | 0.07841 | no |
| Jupiter-Sun Opposition | Nifty Midcap 100 | 24 | -0.4503 | 0.266 | -0.7163 | 29.17 | 0.419 | 0.6006 | no |
| Jupiter-Sun Opposition | Nifty Midcap 150 | 24 | 0.09332 | 0.2642 | -0.1709 | 58.33 | 0.7342 | 0.8459 | no |
| Jupiter-Sun Opposition | BSE Sensex | 24 | -0.3506 | 0.2506 | -0.6012 | 50 | 0.3084 | 0.4867 | no |
| Jupiter-Sun Square | Nifty 50 | 49 | 3.407 | 0.2178 | 3.189 | 77.55 | 1.999e-05 | 0.0002829 | yes |
| Jupiter-Sun Square | Nifty Bank | 49 | 4.165 | 0.3 | 3.865 | 81.63 | 3.158e-06 | 6.402e-05 | yes |
| Jupiter-Sun Square | Nifty Midcap 100 | 49 | 0.02408 | 0.266 | -0.2419 | 36.73 | 0.6319 | 0.7778 | no |
| Jupiter-Sun Square | Nifty Midcap 150 | 49 | 0.8348 | 0.2642 | 0.5706 | 71.43 | 0.06857 | 0.1632 | no |
| Jupiter-Sun Square | BSE Sensex | 49 | 0.8184 | 0.2506 | 0.5678 | 71.43 | 0.1287 | 0.2627 | no |
| Jupiter-Sun Trine | Nifty 50 | 48 | 2.903 | 0.2178 | 2.685 | 68.75 | 0.0003138 | 0.002368 | yes |
| Jupiter-Sun Trine | Nifty Bank | 48 | 3.564 | 0.3 | 3.264 | 72.92 | 0.000198 | 0.001673 | yes |
| Jupiter-Sun Trine | Nifty Midcap 100 | 48 | 0.2858 | 0.266 | 0.01983 | 39.58 | 0.9556 | 0.982 | no |
| Jupiter-Sun Trine | Nifty Midcap 150 | 48 | 0.5518 | 0.2642 | 0.2876 | 70.83 | 0.3237 | 0.5018 | no |
| Jupiter-Sun Trine | BSE Sensex | 48 | 0.4261 | 0.2506 | 0.1756 | 62.5 | 0.6273 | 0.7741 | no |
| Jupiter-Venus Opposition | Nifty 50 | 24 | 3.877 | 0.2178 | 3.66 | 79.17 | 0.0002413 | 0.001913 | yes |
| Jupiter-Venus Opposition | Nifty Bank | 24 | 5.196 | 0.3 | 4.896 | 91.67 | 1.914e-05 | 0.000275 | yes |
| Jupiter-Venus Opposition | Nifty Midcap 100 | 24 | 1.215 | 0.266 | 0.9489 | 50 | 0.05369 | 0.1354 | no |
| Jupiter-Venus Opposition | Nifty Midcap 150 | 24 | 1.007 | 0.2642 | 0.7429 | 70.83 | 0.1775 | 0.3313 | no |
| Jupiter-Venus Opposition | BSE Sensex | 24 | 0.853 | 0.2506 | 0.6024 | 62.5 | 0.3238 | 0.5018 | no |
| Jupiter-Venus Square | Nifty 50 | 55 | 3.07 | 0.2178 | 2.852 | 65.45 | 0.0001571 | 0.001396 | yes |
| Jupiter-Venus Square | Nifty Bank | 55 | 3.581 | 0.3 | 3.281 | 67.27 | 0.0001084 | 0.001049 | yes |
| Jupiter-Venus Square | Nifty Midcap 100 | 55 | -0.4752 | 0.266 | -0.7413 | 32.73 | 0.07454 | 0.1738 | no |
| Jupiter-Venus Square | Nifty Midcap 150 | 55 | 0.4563 | 0.2642 | 0.1921 | 65.45 | 0.5642 | 0.7258 | no |
| Jupiter-Venus Square | BSE Sensex | 55 | 0.2104 | 0.2506 | -0.04012 | 54.55 | 0.919 | 0.9648 | no |
| Jupiter-Venus Trine | Nifty 50 | 49 | 2.837 | 0.2178 | 2.619 | 65.31 | 0.0007121 | 0.0045 | yes |
| Jupiter-Venus Trine | Nifty Bank | 49 | 3.089 | 0.3 | 2.789 | 61.22 | 0.001616 | 0.008558 | yes |
| Jupiter-Venus Trine | Nifty Midcap 100 | 49 | -0.1821 | 0.266 | -0.4481 | 32.65 | 0.1898 | 0.3479 | no |
| Jupiter-Venus Trine | Nifty Midcap 150 | 49 | 0.1841 | 0.2642 | -0.08012 | 61.22 | 0.8102 | 0.8947 | no |
| Jupiter-Venus Trine | BSE Sensex | 49 | -0.3968 | 0.2506 | -0.6474 | 42.86 | 0.06732 | 0.1609 | no |
| Ketu-Mars Opposition | Nifty 50 | 16 | 3.137 | 0.2178 | 2.919 | 68.75 | 0.02918 | 0.08691 | no |
| Ketu-Mars Opposition | Nifty Bank | 16 | 3.074 | 0.3 | 2.774 | 68.75 | 0.1054 | 0.2251 | no |
| Ketu-Mars Opposition | Nifty Midcap 100 | 16 | 0.2327 | 0.266 | -0.03334 | 37.5 | 0.9557 | 0.982 | no |
| Ketu-Mars Opposition | Nifty Midcap 150 | 16 | 0.5239 | 0.2642 | 0.2597 | 75 | 0.5485 | 0.7152 | no |
| Ketu-Mars Opposition | BSE Sensex | 16 | 0.1872 | 0.2506 | -0.06341 | 50 | 0.9246 | 0.9669 | no |
| Ketu-Mars Square | Nifty 50 | 34 | 3.683 | 0.2178 | 3.465 | 79.41 | 0.000583 | 0.003856 | yes |
| Ketu-Mars Square | Nifty Bank | 34 | 4.121 | 0.3 | 3.821 | 70.59 | 0.00197 | 0.009983 | yes |
| Ketu-Mars Square | Nifty Midcap 100 | 34 | 0.7492 | 0.266 | 0.4832 | 44.12 | 0.3938 | 0.5773 | no |
| Ketu-Mars Square | Nifty Midcap 150 | 34 | 1.15 | 0.2642 | 0.8856 | 73.53 | 0.1632 | 0.3146 | no |
| Ketu-Mars Square | BSE Sensex | 34 | 0.9129 | 0.2506 | 0.6623 | 58.82 | 0.3331 | 0.512 | no |
| Ketu-Mars Trine | Nifty 50 | 34 | 3.557 | 0.2178 | 3.339 | 79.41 | 0.0002949 | 0.002248 | yes |
| Ketu-Mars Trine | Nifty Bank | 34 | 4.35 | 0.3 | 4.05 | 79.41 | 0.0001378 | 0.00126 | yes |
| Ketu-Mars Trine | Nifty Midcap 100 | 34 | 0.2642 | 0.266 | -0.00185 | 35.29 | 0.9974 | 0.9993 | no |
| Ketu-Mars Trine | Nifty Midcap 150 | 34 | 1.045 | 0.2642 | 0.781 | 73.53 | 0.09329 | 0.2062 | no |
| Ketu-Mars Trine | BSE Sensex | 34 | 1.039 | 0.2506 | 0.7885 | 61.76 | 0.1729 | 0.3265 | no |
| Ketu-Mercury Opposition | Nifty 50 | 42 | 1.764 | 0.2178 | 1.546 | 66.67 | 0.03964 | 0.1078 | no |
| Ketu-Mercury Opposition | Nifty Bank | 42 | 1.778 | 0.3 | 1.478 | 69.05 | 0.1234 | 0.2544 | no |
| Ketu-Mercury Opposition | Nifty Midcap 100 | 42 | -0.04448 | 0.266 | -0.3105 | 40.48 | 0.4363 | 0.6173 | no |
| Ketu-Mercury Opposition | Nifty Midcap 150 | 42 | 0.2129 | 0.2642 | -0.05132 | 66.67 | 0.9111 | 0.9595 | no |
| Ketu-Mercury Opposition | BSE Sensex | 42 | -0.0591 | 0.2506 | -0.3097 | 59.52 | 0.5251 | 0.6971 | no |
| Ketu-Mercury Square | Nifty 50 | 56 | 2.614 | 0.2178 | 2.397 | 66.07 | 0.0008148 | 0.005034 | yes |
| Ketu-Mercury Square | Nifty Bank | 56 | 2.715 | 0.3 | 2.415 | 67.86 | 0.004149 | 0.01826 | yes |
| Ketu-Mercury Square | Nifty Midcap 100 | 56 | 0.505 | 0.266 | 0.239 | 42.86 | 0.5283 | 0.6998 | no |
| Ketu-Mercury Square | Nifty Midcap 150 | 56 | 0.0489 | 0.2642 | -0.2153 | 62.5 | 0.5599 | 0.7248 | no |
| Ketu-Mercury Square | BSE Sensex | 56 | -0.171 | 0.2506 | -0.4215 | 46.43 | 0.3436 | 0.5236 | no |
| Ketu-Mercury Trine | Nifty 50 | 56 | 3.684 | 0.2178 | 3.466 | 78.57 | 5.384e-07 | 1.413e-05 | yes |
| Ketu-Mercury Trine | Nifty Bank | 56 | 4.575 | 0.3 | 4.275 | 82.14 | 9.523e-08 | 3.493e-06 | yes |
| Ketu-Mercury Trine | Nifty Midcap 100 | 56 | 0.2188 | 0.266 | -0.04721 | 37.5 | 0.9072 | 0.9583 | no |
| Ketu-Mercury Trine | Nifty Midcap 150 | 56 | 1.391 | 0.2642 | 1.127 | 76.79 | 0.002181 | 0.01068 | yes |
| Ketu-Mercury Trine | BSE Sensex | 56 | 0.7018 | 0.2506 | 0.4513 | 58.93 | 0.2797 | 0.4561 | no |
| Ketu-Moon Opposition | Nifty 50 | 54 | 3.089 | 0.2178 | 2.871 | 68.52 | 0.0002346 | 0.001864 | yes |
| Ketu-Moon Opposition | Nifty Bank | 54 | 3.366 | 0.3 | 3.066 | 68.52 | 0.001348 | 0.007413 | yes |
| Ketu-Moon Opposition | Nifty Midcap 100 | 54 | -0.1495 | 0.266 | -0.4155 | 40.74 | 0.221 | 0.3854 | no |
| Ketu-Moon Opposition | Nifty Midcap 150 | 54 | 0.7504 | 0.2642 | 0.4861 | 66.67 | 0.2911 | 0.466 | no |
| Ketu-Moon Opposition | BSE Sensex | 54 | 0.574 | 0.2506 | 0.3234 | 59.26 | 0.4728 | 0.6502 | no |
| Ketu-Moon Square | Nifty 50 | 113 | 2.064 | 0.2178 | 1.846 | 60.18 | 0.0002204 | 0.00177 | yes |
| Ketu-Moon Square | Nifty Bank | 113 | 2.334 | 0.3 | 2.034 | 61.06 | 0.0005221 | 0.003559 | yes |
| Ketu-Moon Square | Nifty Midcap 100 | 113 | -0.142 | 0.266 | -0.408 | 38.05 | 0.1726 | 0.3264 | no |
| Ketu-Moon Square | Nifty Midcap 150 | 113 | 0.08407 | 0.2642 | -0.1802 | 59.29 | 0.5178 | 0.691 | no |
| Ketu-Moon Square | BSE Sensex | 113 | -0.183 | 0.2506 | -0.4335 | 50.44 | 0.1365 | 0.2741 | no |
| Ketu-Moon Trine | Nifty 50 | 115 | 3.485 | 0.2178 | 3.267 | 70.43 | 5.94e-10 | 3.713e-08 | yes |
| Ketu-Moon Trine | Nifty Bank | 115 | 4.137 | 0.3 | 3.837 | 69.57 | 1.963e-09 | 1.078e-07 | yes |
| Ketu-Moon Trine | Nifty Midcap 100 | 115 | 0.2643 | 0.266 | -0.00174 | 40.87 | 0.9952 | 0.9976 | no |
| Ketu-Moon Trine | Nifty Midcap 150 | 115 | 0.9546 | 0.2642 | 0.6903 | 68.7 | 0.02795 | 0.08413 | no |
| Ketu-Moon Trine | BSE Sensex | 115 | 0.6865 | 0.2506 | 0.436 | 58.26 | 0.2087 | 0.371 | no |
| Ketu-Rahu Opposition | Nifty 50 | 1 | 9.735 | 0.2178 | 9.517 | 100 | n/a | n/a | no |
| Ketu-Rahu Opposition | Nifty Bank | 1 | 10.93 | 0.3 | 10.63 | 100 | n/a | n/a | no |
| Ketu-Rahu Opposition | Nifty Midcap 100 | 1 | -0.2908 | 0.266 | -0.5568 | 0 | n/a | n/a | no |
| Ketu-Rahu Opposition | Nifty Midcap 150 | 1 | 1.583 | 0.2642 | 1.319 | 100 | n/a | n/a | no |
| Ketu-Rahu Opposition | BSE Sensex | 1 | -3.546 | 0.2506 | -3.797 | 0 | n/a | n/a | no |
| Ketu-Saturn Opposition | Nifty 50 | 3 | 4.878 | 0.2178 | 4.66 | 100 | 0.2208 | 0.3854 | no |
| Ketu-Saturn Opposition | Nifty Bank | 3 | 6.013 | 0.3 | 5.713 | 100 | 0.1737 | 0.3269 | no |
| Ketu-Saturn Opposition | Nifty Midcap 100 | 3 | 2.752 | 0.266 | 2.486 | 66.67 | 0.3334 | 0.512 | no |
| Ketu-Saturn Opposition | Nifty Midcap 150 | 3 | 2.19 | 0.2642 | 1.926 | 100 | 0.2122 | 0.3749 | no |
| Ketu-Saturn Opposition | BSE Sensex | 3 | 2.076 | 0.2506 | 1.826 | 100 | 0.2759 | 0.453 | no |
| Ketu-Saturn Square | Nifty 50 | 4 | 2.778 | 0.2178 | 2.56 | 75 | 0.3636 | 0.545 | no |
| Ketu-Saturn Square | Nifty Bank | 4 | 3.274 | 0.3 | 2.974 | 50 | 0.3531 | 0.533 | no |
| Ketu-Saturn Square | Nifty Midcap 100 | 4 | -0.1538 | 0.266 | -0.4198 | 25 | 0.655 | 0.7938 | no |
| Ketu-Saturn Square | Nifty Midcap 150 | 4 | 0.8223 | 0.2642 | 0.558 | 75 | 0.4426 | 0.6228 | no |
| Ketu-Saturn Square | BSE Sensex | 4 | 1.387 | 0.2506 | 1.136 | 50 | 0.4141 | 0.5961 | no |
| Ketu-Saturn Trine | Nifty 50 | 5 | 5.09 | 0.2178 | 4.872 | 100 | 0.07421 | 0.1732 | no |
| Ketu-Saturn Trine | Nifty Bank | 5 | 4.86 | 0.3 | 4.56 | 80 | 0.156 | 0.303 | no |
| Ketu-Saturn Trine | Nifty Midcap 100 | 5 | 0.9932 | 0.266 | 0.7272 | 60 | 0.3876 | 0.5702 | no |
| Ketu-Saturn Trine | Nifty Midcap 150 | 5 | 1.789 | 0.2642 | 1.524 | 100 | 0.1213 | 0.2507 | no |
| Ketu-Saturn Trine | BSE Sensex | 5 | 4.257 | 0.2506 | 4.006 | 100 | 0.186 | 0.3428 | no |
| Ketu-Sun Opposition | Nifty 50 | 28 | 2.879 | 0.2178 | 2.661 | 71.43 | 0.008166 | 0.03186 | yes |
| Ketu-Sun Opposition | Nifty Bank | 28 | 2.757 | 0.3 | 2.457 | 60.71 | 0.04552 | 0.1196 | no |
| Ketu-Sun Opposition | Nifty Midcap 100 | 28 | 0.4431 | 0.266 | 0.1771 | 42.86 | 0.7556 | 0.8594 | no |
| Ketu-Sun Opposition | Nifty Midcap 150 | 28 | 0.6559 | 0.2642 | 0.3916 | 71.43 | 0.4065 | 0.5885 | no |
| Ketu-Sun Opposition | BSE Sensex | 28 | -0.3074 | 0.2506 | -0.558 | 53.57 | 0.3967 | 0.5802 | no |
| Ketu-Sun Square | Nifty 50 | 56 | 3.147 | 0.2178 | 2.93 | 71.43 | 3.353e-05 | 0.0004136 | yes |
| Ketu-Sun Square | Nifty Bank | 56 | 3.206 | 0.3 | 2.906 | 67.86 | 0.0005297 | 0.003592 | yes |
| Ketu-Sun Square | Nifty Midcap 100 | 56 | 1.187 | 0.266 | 0.9208 | 50 | 0.01438 | 0.05035 | no |
| Ketu-Sun Square | Nifty Midcap 150 | 56 | 0.811 | 0.2642 | 0.5467 | 66.07 | 0.118 | 0.2457 | no |
| Ketu-Sun Square | BSE Sensex | 56 | 0.5313 | 0.2506 | 0.2808 | 58.93 | 0.4501 | 0.6298 | no |
| Ketu-Sun Trine | Nifty 50 | 56 | 3.532 | 0.2178 | 3.314 | 75 | 1.437e-06 | 3.267e-05 | yes |
| Ketu-Sun Trine | Nifty Bank | 56 | 4.227 | 0.3 | 3.927 | 69.64 | 2.964e-06 | 6.106e-05 | yes |
| Ketu-Sun Trine | Nifty Midcap 100 | 56 | 0.275 | 0.266 | 0.008948 | 41.07 | 0.9763 | 0.9901 | no |
| Ketu-Sun Trine | Nifty Midcap 150 | 56 | 1.18 | 0.2642 | 0.9155 | 69.64 | 0.007978 | 0.03143 | yes |
| Ketu-Sun Trine | BSE Sensex | 56 | 0.5594 | 0.2506 | 0.3088 | 60.71 | 0.4524 | 0.6318 | no |
| Ketu-Venus Opposition | Nifty 50 | 30 | 1.567 | 0.2178 | 1.349 | 50 | 0.1939 | 0.3523 | no |
| Ketu-Venus Opposition | Nifty Bank | 30 | 1.924 | 0.3 | 1.624 | 53.33 | 0.1861 | 0.3428 | no |
| Ketu-Venus Opposition | Nifty Midcap 100 | 30 | -1.225 | 0.266 | -1.492 | 26.67 | 0.02972 | 0.08817 | no |
| Ketu-Venus Opposition | Nifty Midcap 150 | 30 | -0.7016 | 0.2642 | -0.9658 | 50 | 0.06261 | 0.1533 | no |
| Ketu-Venus Opposition | BSE Sensex | 30 | -1.479 | 0.2506 | -1.73 | 26.67 | 0.001279 | 0.007175 | yes |
| Ketu-Venus Square | Nifty 50 | 60 | 3.025 | 0.2178 | 2.807 | 70 | 3.384e-05 | 0.0004147 | yes |
| Ketu-Venus Square | Nifty Bank | 60 | 3.455 | 0.3 | 3.155 | 70 | 0.000105 | 0.001021 | yes |
| Ketu-Venus Square | Nifty Midcap 100 | 60 | 0.07563 | 0.266 | -0.1904 | 35 | 0.6228 | 0.77 | no |
| Ketu-Venus Square | Nifty Midcap 150 | 60 | 0.4229 | 0.2642 | 0.1586 | 65 | 0.5809 | 0.7388 | no |
| Ketu-Venus Square | BSE Sensex | 60 | 0.06512 | 0.2506 | -0.1854 | 55 | 0.5919 | 0.7474 | no |
| Ketu-Venus Trine | Nifty 50 | 60 | 2.942 | 0.2178 | 2.724 | 66.67 | 0.0001148 | 0.001101 | yes |
| Ketu-Venus Trine | Nifty Bank | 60 | 3.363 | 0.3 | 3.063 | 68.33 | 0.0003037 | 0.002296 | yes |
| Ketu-Venus Trine | Nifty Midcap 100 | 60 | 0.2248 | 0.266 | -0.04123 | 48.33 | 0.9327 | 0.9724 | no |
| Ketu-Venus Trine | Nifty Midcap 150 | 60 | 0.8065 | 0.2642 | 0.5422 | 70 | 0.1746 | 0.3283 | no |
| Ketu-Venus Trine | BSE Sensex | 60 | 0.6763 | 0.2506 | 0.4258 | 63.33 | 0.3397 | 0.5205 | no |
| Mars-Mercury Opposition | Nifty 50 | 12 | 3.312 | 0.2178 | 3.095 | 83.33 | 0.03193 | 0.09283 | no |
| Mars-Mercury Opposition | Nifty Bank | 12 | 4.127 | 0.3 | 3.827 | 83.33 | 0.02461 | 0.07685 | no |
| Mars-Mercury Opposition | Nifty Midcap 100 | 12 | 0.3133 | 0.266 | 0.04729 | 41.67 | 0.949 | 0.9798 | no |
| Mars-Mercury Opposition | Nifty Midcap 150 | 12 | 1.314 | 0.2642 | 1.05 | 75 | 0.09969 | 0.2164 | no |
| Mars-Mercury Opposition | BSE Sensex | 12 | 0.8308 | 0.2506 | 0.5803 | 58.33 | 0.5494 | 0.7161 | no |
| Mars-Mercury Square | Nifty 50 | 53 | 3.563 | 0.2178 | 3.346 | 66.04 | 1.831e-05 | 0.0002641 | yes |
| Mars-Mercury Square | Nifty Bank | 53 | 4.089 | 0.3 | 3.789 | 66.04 | 3.455e-05 | 0.000422 | yes |
| Mars-Mercury Square | Nifty Midcap 100 | 53 | 0.4646 | 0.266 | 0.1986 | 41.51 | 0.5921 | 0.7474 | no |
| Mars-Mercury Square | Nifty Midcap 150 | 53 | 0.6617 | 0.2642 | 0.3975 | 64.15 | 0.2414 | 0.4096 | no |
| Mars-Mercury Square | BSE Sensex | 53 | 0.6515 | 0.2506 | 0.4009 | 56.6 | 0.3273 | 0.5054 | no |
| Mars-Mercury Trine | Nifty 50 | 32 | 2.704 | 0.2178 | 2.486 | 75 | 0.001686 | 0.008831 | yes |
| Mars-Mercury Trine | Nifty Bank | 32 | 3.372 | 0.3 | 3.072 | 75 | 0.001138 | 0.006534 | yes |
| Mars-Mercury Trine | Nifty Midcap 100 | 32 | 0.8942 | 0.266 | 0.6282 | 46.88 | 0.3172 | 0.4943 | no |
| Mars-Mercury Trine | Nifty Midcap 150 | 32 | 1.229 | 0.2642 | 0.9646 | 75 | 0.02241 | 0.07178 | no |
| Mars-Mercury Trine | BSE Sensex | 32 | 1.066 | 0.2506 | 0.8149 | 68.75 | 0.1148 | 0.2402 | no |
| Mars-Moon Opposition | Nifty 50 | 50 | 2.296 | 0.2178 | 2.078 | 68 | 0.003902 | 0.01736 | yes |
| Mars-Moon Opposition | Nifty Bank | 50 | 2.443 | 0.3 | 2.143 | 66 | 0.01148 | 0.04268 | yes |
| Mars-Moon Opposition | Nifty Midcap 100 | 50 | -0.1026 | 0.266 | -0.3686 | 40 | 0.4438 | 0.6243 | no |
| Mars-Moon Opposition | Nifty Midcap 150 | 50 | 0.3403 | 0.2642 | 0.07608 | 66 | 0.8275 | 0.9058 | no |
| Mars-Moon Opposition | BSE Sensex | 50 | 0.04234 | 0.2506 | -0.2082 | 60 | 0.6299 | 0.7766 | no |
| Mars-Moon Square | Nifty 50 | 110 | 2.769 | 0.2178 | 2.551 | 70 | 1.937e-08 | 9.08e-07 | yes |
| Mars-Moon Square | Nifty Bank | 110 | 3.067 | 0.3 | 2.767 | 70 | 1.015e-07 | 3.626e-06 | yes |
| Mars-Moon Square | Nifty Midcap 100 | 110 | 0.446 | 0.266 | 0.18 | 47.27 | 0.5463 | 0.7143 | no |
| Mars-Moon Square | Nifty Midcap 150 | 110 | 0.659 | 0.2642 | 0.3947 | 65.45 | 0.06758 | 0.1613 | no |
| Mars-Moon Square | BSE Sensex | 110 | 0.3451 | 0.2506 | 0.09448 | 56.36 | 0.7132 | 0.8334 | no |
| Mars-Moon Trine | Nifty 50 | 100 | 2.133 | 0.2178 | 1.916 | 64 | 0.0006546 | 0.00421 | yes |
| Mars-Moon Trine | Nifty Bank | 100 | 2.71 | 0.3 | 2.41 | 66 | 0.000136 | 0.00125 | yes |
| Mars-Moon Trine | Nifty Midcap 100 | 100 | -0.5802 | 0.266 | -0.8462 | 39 | 0.01826 | 0.06196 | no |
| Mars-Moon Trine | Nifty Midcap 150 | 100 | 0.04442 | 0.2642 | -0.2198 | 61 | 0.496 | 0.6734 | no |
| Mars-Moon Trine | BSE Sensex | 100 | -0.2938 | 0.2506 | -0.5444 | 54 | 0.1212 | 0.2507 | no |
| Mars-Rahu Opposition | Nifty 50 | 17 | 1.476 | 0.2178 | 1.258 | 58.82 | 0.379 | 0.5608 | no |
| Mars-Rahu Opposition | Nifty Bank | 17 | 1.615 | 0.3 | 1.315 | 58.82 | 0.4647 | 0.6421 | no |
| Mars-Rahu Opposition | Nifty Midcap 100 | 17 | -0.6499 | 0.266 | -0.9159 | 29.41 | 0.2189 | 0.3844 | no |
| Mars-Rahu Opposition | Nifty Midcap 150 | 17 | -0.7194 | 0.2642 | -0.9837 | 52.94 | 0.2784 | 0.4549 | no |
| Mars-Rahu Opposition | BSE Sensex | 17 | -1.389 | 0.2506 | -1.64 | 41.18 | 0.08399 | 0.1894 | no |
| Mars-Rahu Square | Nifty 50 | 34 | 3.683 | 0.2178 | 3.465 | 79.41 | 0.000583 | 0.003856 | yes |
| Mars-Rahu Square | Nifty Bank | 34 | 4.121 | 0.3 | 3.821 | 70.59 | 0.00197 | 0.009983 | yes |
| Mars-Rahu Square | Nifty Midcap 100 | 34 | 0.7492 | 0.266 | 0.4832 | 44.12 | 0.3938 | 0.5773 | no |
| Mars-Rahu Square | Nifty Midcap 150 | 34 | 1.15 | 0.2642 | 0.8856 | 73.53 | 0.1632 | 0.3146 | no |
| Mars-Rahu Square | BSE Sensex | 34 | 0.9129 | 0.2506 | 0.6623 | 58.82 | 0.3331 | 0.512 | no |
| Mars-Rahu Trine | Nifty 50 | 36 | 3.253 | 0.2178 | 3.035 | 72.22 | 0.0005087 | 0.003504 | yes |
| Mars-Rahu Trine | Nifty Bank | 36 | 3.534 | 0.3 | 3.235 | 75 | 0.002086 | 0.01039 | yes |
| Mars-Rahu Trine | Nifty Midcap 100 | 36 | 0.4552 | 0.266 | 0.1892 | 41.67 | 0.7953 | 0.8851 | no |
| Mars-Rahu Trine | Nifty Midcap 150 | 36 | 0.8312 | 0.2642 | 0.567 | 69.44 | 0.3131 | 0.4908 | no |
| Mars-Rahu Trine | BSE Sensex | 36 | 0.7058 | 0.2506 | 0.4552 | 66.67 | 0.417 | 0.5988 | no |
| Mars-Saturn Opposition | Nifty 50 | 13 | 3.713 | 0.2178 | 3.496 | 84.62 | 0.01398 | 0.04946 | yes |
| Mars-Saturn Opposition | Nifty Bank | 13 | 4.544 | 0.3 | 4.244 | 84.62 | 0.01159 | 0.04282 | yes |
| Mars-Saturn Opposition | Nifty Midcap 100 | 13 | 0.3991 | 0.266 | 0.1331 | 38.46 | 0.8407 | 0.914 | no |
| Mars-Saturn Opposition | Nifty Midcap 150 | 13 | 1.053 | 0.2642 | 0.7889 | 76.92 | 0.07637 | 0.1767 | no |
| Mars-Saturn Opposition | BSE Sensex | 13 | 0.5179 | 0.2506 | 0.2674 | 61.54 | 0.5883 | 0.7459 | no |
| Mars-Saturn Square | Nifty 50 | 31 | 3.866 | 0.2178 | 3.648 | 77.42 | 9.61e-05 | 0.0009508 | yes |
| Mars-Saturn Square | Nifty Bank | 31 | 4.552 | 0.3 | 4.252 | 77.42 | 5.453e-05 | 0.0006159 | yes |
| Mars-Saturn Square | Nifty Midcap 100 | 31 | 0.4781 | 0.266 | 0.2121 | 41.94 | 0.6624 | 0.7996 | no |
| Mars-Saturn Square | Nifty Midcap 150 | 31 | 1.375 | 0.2642 | 1.111 | 77.42 | 0.003658 | 0.01657 | yes |
| Mars-Saturn Square | BSE Sensex | 31 | 1.011 | 0.2506 | 0.7607 | 67.74 | 0.08125 | 0.185 | no |
| Mars-Saturn Trine | Nifty 50 | 33 | 3.074 | 0.2178 | 2.856 | 66.67 | 0.001945 | 0.009906 | yes |
| Mars-Saturn Trine | Nifty Bank | 33 | 3.525 | 0.3 | 3.225 | 66.67 | 0.00275 | 0.01306 | yes |
| Mars-Saturn Trine | Nifty Midcap 100 | 33 | 0.2558 | 0.266 | -0.01023 | 48.48 | 0.975 | 0.9897 | no |
| Mars-Saturn Trine | Nifty Midcap 150 | 33 | 0.6562 | 0.2642 | 0.3919 | 66.67 | 0.3097 | 0.4871 | no |
| Mars-Saturn Trine | BSE Sensex | 33 | 0.7866 | 0.2506 | 0.536 | 63.64 | 0.1824 | 0.3379 | no |
| Mars-Sun Opposition | Nifty 50 | 12 | 2.986 | 0.2178 | 2.768 | 58.33 | 0.06423 | 0.1558 | no |
| Mars-Sun Opposition | Nifty Bank | 12 | 3.65 | 0.3 | 3.35 | 66.67 | 0.05464 | 0.1374 | no |
| Mars-Sun Opposition | Nifty Midcap 100 | 12 | -0.2508 | 0.266 | -0.5168 | 41.67 | 0.4838 | 0.6622 | no |
| Mars-Sun Opposition | Nifty Midcap 150 | 12 | 0.9936 | 0.2642 | 0.7293 | 58.33 | 0.2885 | 0.4633 | no |
| Mars-Sun Opposition | BSE Sensex | 12 | 0.7815 | 0.2506 | 0.5309 | 50 | 0.519 | 0.6924 | no |
| Mars-Sun Square | Nifty 50 | 24 | 2.65 | 0.2178 | 2.432 | 66.67 | 0.02969 | 0.08817 | no |
| Mars-Sun Square | Nifty Bank | 24 | 3.023 | 0.3 | 2.723 | 66.67 | 0.03861 | 0.1063 | no |
| Mars-Sun Square | Nifty Midcap 100 | 24 | 0.2732 | 0.266 | 0.007232 | 41.67 | 0.9888 | 0.9956 | no |
| Mars-Sun Square | Nifty Midcap 150 | 24 | 0.5913 | 0.2642 | 0.3271 | 70.83 | 0.5989 | 0.7519 | no |
| Mars-Sun Square | BSE Sensex | 24 | 0.427 | 0.2506 | 0.1765 | 66.67 | 0.7717 | 0.8717 | no |
| Mars-Sun Trine | Nifty 50 | 24 | 2.976 | 0.2178 | 2.759 | 83.33 | 0.005742 | 0.02392 | yes |
| Mars-Sun Trine | Nifty Bank | 24 | 3.738 | 0.3 | 3.438 | 83.33 | 0.002525 | 0.01215 | yes |
| Mars-Sun Trine | Nifty Midcap 100 | 24 | 0.01345 | 0.266 | -0.2526 | 45.83 | 0.653 | 0.7932 | no |
| Mars-Sun Trine | Nifty Midcap 150 | 24 | 1.073 | 0.2642 | 0.8092 | 83.33 | 0.0655 | 0.1578 | no |
| Mars-Sun Trine | BSE Sensex | 24 | 1.551 | 0.2506 | 1.3 | 79.17 | 0.03955 | 0.1077 | no |
| Mars-Venus Opposition | Nifty 50 | 12 | 3.318 | 0.2178 | 3.1 | 75 | 0.0305 | 0.08979 | no |
| Mars-Venus Opposition | Nifty Bank | 12 | 5.394 | 0.3 | 5.094 | 83.33 | 0.00386 | 0.01725 | yes |
| Mars-Venus Opposition | Nifty Midcap 100 | 12 | -0.2907 | 0.266 | -0.5567 | 41.67 | 0.432 | 0.6145 | no |
| Mars-Venus Opposition | Nifty Midcap 150 | 12 | 1.439 | 0.2642 | 1.174 | 75 | 0.08138 | 0.185 | no |
| Mars-Venus Opposition | BSE Sensex | 12 | 0.5991 | 0.2506 | 0.3485 | 58.33 | 0.6471 | 0.7906 | no |
| Mars-Venus Square | Nifty 50 | 36 | 2.677 | 0.2178 | 2.459 | 72.22 | 0.001423 | 0.007773 | yes |
| Mars-Venus Square | Nifty Bank | 36 | 3.171 | 0.3 | 2.871 | 72.22 | 0.002552 | 0.01225 | yes |
| Mars-Venus Square | Nifty Midcap 100 | 36 | 0.3108 | 0.266 | 0.04484 | 36.11 | 0.9374 | 0.9749 | no |
| Mars-Venus Square | Nifty Midcap 150 | 36 | 0.5521 | 0.2642 | 0.2879 | 63.89 | 0.4484 | 0.6286 | no |
| Mars-Venus Square | BSE Sensex | 36 | 0.4493 | 0.2506 | 0.1987 | 58.33 | 0.6177 | 0.765 | no |
| Mars-Venus Trine | Nifty 50 | 32 | 3.614 | 0.2178 | 3.396 | 75 | 0.0004917 | 0.003408 | yes |
| Mars-Venus Trine | Nifty Bank | 32 | 4.24 | 0.3 | 3.94 | 71.88 | 0.0005294 | 0.003592 | yes |
| Mars-Venus Trine | Nifty Midcap 100 | 32 | 1.034 | 0.266 | 0.7679 | 56.25 | 0.1333 | 0.2699 | no |
| Mars-Venus Trine | Nifty Midcap 150 | 32 | 1.145 | 0.2642 | 0.8812 | 71.88 | 0.07168 | 0.1691 | no |
| Mars-Venus Trine | BSE Sensex | 32 | 1.214 | 0.2506 | 0.963 | 65.62 | 0.08685 | 0.1943 | no |
| Mercury-Moon Opposition | Nifty 50 | 62 | 3.147 | 0.2178 | 2.93 | 72.58 | 1.098e-05 | 0.0001723 | yes |
| Mercury-Moon Opposition | Nifty Bank | 62 | 3.424 | 0.3 | 3.124 | 74.19 | 7.124e-05 | 0.0007568 | yes |
| Mercury-Moon Opposition | Nifty Midcap 100 | 62 | 0.1827 | 0.266 | -0.08331 | 41.94 | 0.7824 | 0.8763 | no |
| Mercury-Moon Opposition | Nifty Midcap 150 | 62 | 0.6997 | 0.2642 | 0.4355 | 70.97 | 0.1907 | 0.3485 | no |
| Mercury-Moon Opposition | BSE Sensex | 62 | 0.2538 | 0.2506 | 0.003195 | 61.29 | 0.9943 | 0.9976 | no |
| Mercury-Moon Square | Nifty 50 | 126 | 2.895 | 0.2178 | 2.677 | 68.25 | 8.016e-08 | 3.036e-06 | yes |
| Mercury-Moon Square | Nifty Bank | 126 | 3.051 | 0.3 | 2.751 | 66.67 | 5.61e-06 | 9.877e-05 | yes |
| Mercury-Moon Square | Nifty Midcap 100 | 126 | 0.05205 | 0.266 | -0.214 | 42.06 | 0.4592 | 0.6373 | no |
| Mercury-Moon Square | Nifty Midcap 150 | 126 | 0.4723 | 0.2642 | 0.2081 | 66.67 | 0.4374 | 0.618 | no |
| Mercury-Moon Square | BSE Sensex | 126 | 0.09819 | 0.2506 | -0.1524 | 51.59 | 0.5965 | 0.7511 | no |
| Mercury-Moon Trine | Nifty 50 | 94 | 3.358 | 0.2178 | 3.14 | 70.21 | 2.996e-08 | 1.306e-06 | yes |
| Mercury-Moon Trine | Nifty Bank | 94 | 3.731 | 0.3 | 3.431 | 71.28 | 3.324e-07 | 1.005e-05 | yes |
| Mercury-Moon Trine | Nifty Midcap 100 | 94 | -0.3519 | 0.266 | -0.6179 | 31.91 | 0.03858 | 0.1063 | no |
| Mercury-Moon Trine | Nifty Midcap 150 | 94 | 0.6802 | 0.2642 | 0.416 | 70.21 | 0.07959 | 0.1822 | no |
| Mercury-Moon Trine | BSE Sensex | 94 | -0.292 | 0.2506 | -0.5425 | 53.19 | 0.1648 | 0.3163 | no |
| Mercury-Rahu Opposition | Nifty 50 | 28 | 3.075 | 0.2178 | 2.857 | 67.86 | 0.005301 | 0.02236 | yes |
| Mercury-Rahu Opposition | Nifty Bank | 28 | 3.554 | 0.3 | 3.254 | 64.29 | 0.008123 | 0.03179 | yes |
| Mercury-Rahu Opposition | Nifty Midcap 100 | 28 | 0.5095 | 0.266 | 0.2435 | 46.43 | 0.4366 | 0.6173 | no |
| Mercury-Rahu Opposition | Nifty Midcap 150 | 28 | 0.7172 | 0.2642 | 0.453 | 67.86 | 0.3317 | 0.511 | no |
| Mercury-Rahu Opposition | BSE Sensex | 28 | 0.3807 | 0.2506 | 0.1301 | 53.57 | 0.7969 | 0.8854 | no |
| Mercury-Rahu Square | Nifty 50 | 56 | 2.614 | 0.2178 | 2.397 | 66.07 | 0.0008148 | 0.005034 | yes |
| Mercury-Rahu Square | Nifty Bank | 56 | 2.715 | 0.3 | 2.415 | 67.86 | 0.004149 | 0.01826 | yes |
| Mercury-Rahu Square | Nifty Midcap 100 | 56 | 0.505 | 0.266 | 0.239 | 42.86 | 0.5283 | 0.6998 | no |
| Mercury-Rahu Square | Nifty Midcap 150 | 56 | 0.0489 | 0.2642 | -0.2153 | 62.5 | 0.5599 | 0.7248 | no |
| Mercury-Rahu Square | BSE Sensex | 56 | -0.171 | 0.2506 | -0.4215 | 46.43 | 0.3436 | 0.5236 | no |
| Mercury-Rahu Trine | Nifty 50 | 114 | 3.013 | 0.2178 | 2.796 | 71.05 | 1.903e-08 | 9.034e-07 | yes |
| Mercury-Rahu Trine | Nifty Bank | 114 | 3.605 | 0.3 | 3.305 | 71.05 | 2.859e-08 | 1.262e-06 | yes |
| Mercury-Rahu Trine | Nifty Midcap 100 | 114 | 0.0908 | 0.266 | -0.1752 | 40.35 | 0.4761 | 0.6536 | no |
| Mercury-Rahu Trine | Nifty Midcap 150 | 114 | 0.8227 | 0.2642 | 0.5584 | 65.79 | 0.06744 | 0.1611 | no |
| Mercury-Rahu Trine | BSE Sensex | 114 | 0.5518 | 0.2506 | 0.3013 | 62.28 | 0.3697 | 0.5519 | no |
| Mercury-Saturn Opposition | Nifty 50 | 28 | 3.949 | 0.2178 | 3.731 | 71.43 | 0.0004764 | 0.003327 | yes |
| Mercury-Saturn Opposition | Nifty Bank | 28 | 4.655 | 0.3 | 4.356 | 71.43 | 0.0006759 | 0.004311 | yes |
| Mercury-Saturn Opposition | Nifty Midcap 100 | 28 | 0.3224 | 0.266 | 0.05641 | 25 | 0.9308 | 0.9709 | no |
| Mercury-Saturn Opposition | Nifty Midcap 150 | 28 | 1.183 | 0.2642 | 0.9187 | 67.86 | 0.09953 | 0.2162 | no |
| Mercury-Saturn Opposition | BSE Sensex | 28 | 1.777 | 0.2506 | 1.526 | 71.43 | 0.0235 | 0.07425 | no |
| Mercury-Saturn Square | Nifty 50 | 66 | 3.069 | 0.2178 | 2.851 | 69.7 | 1.298e-05 | 0.0001994 | yes |
| Mercury-Saturn Square | Nifty Bank | 66 | 3.412 | 0.3 | 3.112 | 66.67 | 4.1e-05 | 0.0004806 | yes |
| Mercury-Saturn Square | Nifty Midcap 100 | 66 | 0.01046 | 0.266 | -0.2556 | 31.82 | 0.34 | 0.5208 | no |
| Mercury-Saturn Square | Nifty Midcap 150 | 66 | 0.382 | 0.2642 | 0.1177 | 66.67 | 0.694 | 0.8191 | no |
| Mercury-Saturn Square | BSE Sensex | 66 | -0.06946 | 0.2506 | -0.32 | 54.55 | 0.2983 | 0.4749 | no |
| Mercury-Saturn Trine | Nifty 50 | 63 | 3.566 | 0.2178 | 3.348 | 77.78 | 1.973e-07 | 6.433e-06 | yes |
| Mercury-Saturn Trine | Nifty Bank | 63 | 4.124 | 0.3 | 3.824 | 76.19 | 3.56e-07 | 1.06e-05 | yes |
| Mercury-Saturn Trine | Nifty Midcap 100 | 63 | 0.3727 | 0.266 | 0.1067 | 38.1 | 0.7074 | 0.829 | no |
| Mercury-Saturn Trine | Nifty Midcap 150 | 63 | 1.093 | 0.2642 | 0.8283 | 74.6 | 0.002136 | 0.0105 | yes |
| Mercury-Saturn Trine | BSE Sensex | 63 | 0.5154 | 0.2506 | 0.2649 | 63.49 | 0.4109 | 0.5926 | no |
| Moon-Rahu Opposition | Nifty 50 | 57 | 3.297 | 0.2178 | 3.079 | 68.42 | 1.705e-05 | 0.0002488 | yes |
| Moon-Rahu Opposition | Nifty Bank | 57 | 3.726 | 0.3 | 3.426 | 57.89 | 4.114e-05 | 0.0004806 | yes |
| Moon-Rahu Opposition | Nifty Midcap 100 | 57 | 0.1268 | 0.266 | -0.1392 | 43.86 | 0.6922 | 0.8183 | no |
| Moon-Rahu Opposition | Nifty Midcap 150 | 57 | 0.4116 | 0.2642 | 0.1474 | 66.67 | 0.6627 | 0.7996 | no |
| Moon-Rahu Opposition | BSE Sensex | 57 | 0.5057 | 0.2506 | 0.2551 | 54.39 | 0.5676 | 0.7282 | no |
| Moon-Rahu Square | Nifty 50 | 113 | 2.064 | 0.2178 | 1.846 | 60.18 | 0.0002204 | 0.00177 | yes |
| Moon-Rahu Square | Nifty Bank | 113 | 2.334 | 0.3 | 2.034 | 61.06 | 0.0005221 | 0.003559 | yes |
| Moon-Rahu Square | Nifty Midcap 100 | 113 | -0.142 | 0.266 | -0.408 | 38.05 | 0.1726 | 0.3264 | no |
| Moon-Rahu Square | Nifty Midcap 150 | 113 | 0.08407 | 0.2642 | -0.1802 | 59.29 | 0.5178 | 0.691 | no |
| Moon-Rahu Square | BSE Sensex | 113 | -0.183 | 0.2506 | -0.4335 | 50.44 | 0.1365 | 0.2741 | no |
| Moon-Rahu Trine | Nifty 50 | 119 | 2.578 | 0.2178 | 2.36 | 67.23 | 1.818e-06 | 3.961e-05 | yes |
| Moon-Rahu Trine | Nifty Bank | 119 | 2.942 | 0.3 | 2.642 | 64.71 | 5.57e-06 | 9.852e-05 | yes |
| Moon-Rahu Trine | Nifty Midcap 100 | 119 | -0.1513 | 0.266 | -0.4174 | 36.13 | 0.09636 | 0.2109 | no |
| Moon-Rahu Trine | Nifty Midcap 150 | 119 | 0.1995 | 0.2642 | -0.06474 | 63.03 | 0.8155 | 0.897 | no |
| Moon-Rahu Trine | BSE Sensex | 119 | 0.1934 | 0.2506 | -0.05719 | 57.14 | 0.8387 | 0.9128 | no |
| Moon-Saturn Opposition | Nifty 50 | 57 | 3.553 | 0.2178 | 3.336 | 75.44 | 1.6e-05 | 0.0002391 | yes |
| Moon-Saturn Opposition | Nifty Bank | 57 | 4.269 | 0.3 | 3.969 | 75.44 | 1.62e-05 | 0.000241 | yes |
| Moon-Saturn Opposition | Nifty Midcap 100 | 57 | 0.7224 | 0.266 | 0.4564 | 59.65 | 0.2032 | 0.3645 | no |
| Moon-Saturn Opposition | Nifty Midcap 150 | 57 | 1.142 | 0.2642 | 0.8776 | 70.18 | 0.09457 | 0.2084 | no |
| Moon-Saturn Opposition | BSE Sensex | 57 | 0.9701 | 0.2506 | 0.7195 | 66.67 | 0.1648 | 0.3163 | no |
| Moon-Saturn Square | Nifty 50 | 109 | 2.808 | 0.2178 | 2.59 | 65.14 | 1.469e-07 | 4.961e-06 | yes |
| Moon-Saturn Square | Nifty Bank | 109 | 3.277 | 0.3 | 2.977 | 65.14 | 1.607e-07 | 5.323e-06 | yes |
| Moon-Saturn Square | Nifty Midcap 100 | 109 | -0.0793 | 0.266 | -0.3453 | 33.94 | 0.1432 | 0.2838 | no |
| Moon-Saturn Square | Nifty Midcap 150 | 109 | 0.469 | 0.2642 | 0.2047 | 64.22 | 0.318 | 0.4952 | no |
| Moon-Saturn Square | BSE Sensex | 109 | -0.01587 | 0.2506 | -0.2664 | 55.05 | 0.3649 | 0.5465 | no |
| Moon-Saturn Trine | Nifty 50 | 104 | 2.697 | 0.2178 | 2.479 | 69.23 | 3.45e-06 | 6.82e-05 | yes |
| Moon-Saturn Trine | Nifty Bank | 104 | 2.875 | 0.3 | 2.575 | 64.42 | 6.324e-05 | 0.0006955 | yes |
| Moon-Saturn Trine | Nifty Midcap 100 | 104 | 0.4149 | 0.266 | 0.1489 | 48.08 | 0.6408 | 0.7845 | no |
| Moon-Saturn Trine | Nifty Midcap 150 | 104 | 0.5717 | 0.2642 | 0.3075 | 71.15 | 0.3104 | 0.4872 | no |
| Moon-Saturn Trine | BSE Sensex | 104 | 0.2497 | 0.2506 | -0.0008682 | 59.62 | 0.9979 | 0.9993 | no |
| Moon-Sun Opposition | Nifty 50 | 63 | 2.945 | 0.2178 | 2.727 | 63.49 | 2.51e-05 | 0.0003325 | yes |
| Moon-Sun Opposition | Nifty Bank | 63 | 3.349 | 0.3 | 3.049 | 66.67 | 6.491e-05 | 0.0007006 | yes |
| Moon-Sun Opposition | Nifty Midcap 100 | 63 | 0.01965 | 0.266 | -0.2464 | 41.27 | 0.392 | 0.5753 | no |
| Moon-Sun Opposition | Nifty Midcap 150 | 63 | 0.6779 | 0.2642 | 0.4137 | 63.49 | 0.1333 | 0.2699 | no |
| Moon-Sun Opposition | BSE Sensex | 63 | 0.4255 | 0.2506 | 0.1749 | 52.38 | 0.5894 | 0.7459 | no |
| Moon-Sun Square | Nifty 50 | 114 | 2.451 | 0.2178 | 2.234 | 64.04 | 2.373e-05 | 0.000319 | yes |
| Moon-Sun Square | Nifty Bank | 114 | 2.702 | 0.3 | 2.402 | 63.16 | 0.000137 | 0.001257 | yes |
| Moon-Sun Square | Nifty Midcap 100 | 114 | 0.2145 | 0.266 | -0.05147 | 38.6 | 0.8717 | 0.9339 | no |
| Moon-Sun Square | Nifty Midcap 150 | 114 | 0.3634 | 0.2642 | 0.09916 | 64.91 | 0.7591 | 0.8618 | no |
| Moon-Sun Square | BSE Sensex | 114 | 0.2878 | 0.2506 | 0.03721 | 57.02 | 0.9157 | 0.9627 | no |
| Moon-Sun Trine | Nifty 50 | 108 | 3.044 | 0.2178 | 2.826 | 64.81 | 2.155e-08 | 9.977e-07 | yes |
| Moon-Sun Trine | Nifty Bank | 108 | 3.218 | 0.3 | 2.918 | 64.81 | 1.324e-06 | 3.046e-05 | yes |
| Moon-Sun Trine | Nifty Midcap 100 | 108 | 0.1954 | 0.266 | -0.07063 | 34.26 | 0.7899 | 0.8811 | no |
| Moon-Sun Trine | Nifty Midcap 150 | 108 | 0.5075 | 0.2642 | 0.2432 | 62.96 | 0.2368 | 0.4046 | no |
| Moon-Sun Trine | BSE Sensex | 108 | -0.1337 | 0.2506 | -0.3843 | 47.22 | 0.1253 | 0.2569 | no |
| Moon-Venus Opposition | Nifty 50 | 61 | 2.462 | 0.2178 | 2.244 | 67.21 | 0.0007116 | 0.0045 | yes |
| Moon-Venus Opposition | Nifty Bank | 61 | 2.902 | 0.3 | 2.602 | 65.57 | 0.001061 | 0.006216 | yes |
| Moon-Venus Opposition | Nifty Midcap 100 | 61 | -0.07769 | 0.266 | -0.3437 | 36.07 | 0.3261 | 0.5038 | no |
| Moon-Venus Opposition | Nifty Midcap 150 | 61 | 0.4496 | 0.2642 | 0.1853 | 65.57 | 0.6061 | 0.7563 | no |
| Moon-Venus Opposition | BSE Sensex | 61 | -0.02295 | 0.2506 | -0.2735 | 55.74 | 0.5014 | 0.6771 | no |
| Moon-Venus Square | Nifty 50 | 117 | 2.626 | 0.2178 | 2.408 | 66.67 | 1.314e-06 | 3.046e-05 | yes |
| Moon-Venus Square | Nifty Bank | 117 | 3.006 | 0.3 | 2.706 | 67.52 | 1.005e-05 | 0.0001611 | yes |
| Moon-Venus Square | Nifty Midcap 100 | 117 | 0.1116 | 0.266 | -0.1544 | 42.74 | 0.5987 | 0.7519 | no |
| Moon-Venus Square | Nifty Midcap 150 | 117 | 0.7304 | 0.2642 | 0.4661 | 68.38 | 0.1284 | 0.2622 | no |
| Moon-Venus Square | BSE Sensex | 117 | 0.2499 | 0.2506 | -0.0006955 | 51.28 | 0.9982 | 0.9993 | no |
| Moon-Venus Trine | Nifty 50 | 93 | 2.486 | 0.2178 | 2.268 | 68.82 | 6.398e-05 | 0.0006995 | yes |
| Moon-Venus Trine | Nifty Bank | 93 | 2.671 | 0.3 | 2.371 | 65.59 | 0.0003546 | 0.002623 | yes |
| Moon-Venus Trine | Nifty Midcap 100 | 93 | -0.01701 | 0.266 | -0.283 | 40.86 | 0.3735 | 0.5549 | no |
| Moon-Venus Trine | Nifty Midcap 150 | 93 | 0.4781 | 0.2642 | 0.2138 | 66.67 | 0.524 | 0.6961 | no |
| Moon-Venus Trine | BSE Sensex | 93 | 0.1203 | 0.2506 | -0.1303 | 55.91 | 0.7108 | 0.8312 | no |
| Rahu-Saturn Opposition | Nifty 50 | 2 | -1.554 | 0.2178 | -1.771 | 50 | 0.5913 | 0.7471 | no |
| Rahu-Saturn Opposition | Nifty Bank | 2 | -1.772 | 0.3 | -2.072 | 50 | 0.7336 | 0.8454 | no |
| Rahu-Saturn Opposition | Nifty Midcap 100 | 2 | -1.123 | 0.266 | -1.389 | 50 | 0.5147 | 0.6878 | no |
| Rahu-Saturn Opposition | Nifty Midcap 150 | 2 | -1.792 | 0.2642 | -2.056 | 50 | 0.5966 | 0.7511 | no |
| Rahu-Saturn Opposition | BSE Sensex | 2 | -1.912 | 0.2506 | -2.162 | 50 | 0.576 | 0.7342 | no |
| Rahu-Saturn Square | Nifty 50 | 4 | 2.778 | 0.2178 | 2.56 | 75 | 0.3636 | 0.545 | no |
| Rahu-Saturn Square | Nifty Bank | 4 | 3.274 | 0.3 | 2.974 | 50 | 0.3531 | 0.533 | no |
| Rahu-Saturn Square | Nifty Midcap 100 | 4 | -0.1538 | 0.266 | -0.4198 | 25 | 0.655 | 0.7938 | no |
| Rahu-Saturn Square | Nifty Midcap 150 | 4 | 0.8223 | 0.2642 | 0.558 | 75 | 0.4426 | 0.6228 | no |
| Rahu-Saturn Square | BSE Sensex | 4 | 1.387 | 0.2506 | 1.136 | 50 | 0.4141 | 0.5961 | no |
| Rahu-Saturn Trine | Nifty 50 | 4 | 2.399 | 0.2178 | 2.182 | 75 | 0.4487 | 0.6288 | no |
| Rahu-Saturn Trine | Nifty Bank | 4 | 2.854 | 0.3 | 2.554 | 75 | 0.4137 | 0.5961 | no |
| Rahu-Saturn Trine | Nifty Midcap 100 | 4 | -1.487 | 0.266 | -1.753 | 0 | 0.2874 | 0.4622 | no |
| Rahu-Saturn Trine | Nifty Midcap 150 | 4 | 0.1603 | 0.2642 | -0.1039 | 75 | 0.8481 | 0.9178 | no |
| Rahu-Saturn Trine | BSE Sensex | 4 | -0.1085 | 0.2506 | -0.359 | 75 | 0.5436 | 0.7115 | no |
| Rahu-Sun Opposition | Nifty 50 | 29 | 2.513 | 0.2178 | 2.295 | 55.17 | 0.02786 | 0.08406 | no |
| Rahu-Sun Opposition | Nifty Bank | 29 | 2.732 | 0.3 | 2.432 | 55.17 | 0.04765 | 0.1238 | no |
| Rahu-Sun Opposition | Nifty Midcap 100 | 29 | 0.3909 | 0.266 | 0.1248 | 41.38 | 0.7999 | 0.888 | no |
| Rahu-Sun Opposition | Nifty Midcap 150 | 29 | -0.02152 | 0.2642 | -0.2858 | 55.17 | 0.5211 | 0.6939 | no |
| Rahu-Sun Opposition | BSE Sensex | 29 | -0.9889 | 0.2506 | -1.239 | 34.48 | 0.01914 | 0.06436 | no |
| Rahu-Sun Square | Nifty 50 | 56 | 3.147 | 0.2178 | 2.93 | 71.43 | 3.353e-05 | 0.0004136 | yes |
| Rahu-Sun Square | Nifty Bank | 56 | 3.206 | 0.3 | 2.906 | 67.86 | 0.0005297 | 0.003592 | yes |
| Rahu-Sun Square | Nifty Midcap 100 | 56 | 1.187 | 0.266 | 0.9208 | 50 | 0.01438 | 0.05035 | no |
| Rahu-Sun Square | Nifty Midcap 150 | 56 | 0.811 | 0.2642 | 0.5467 | 66.07 | 0.118 | 0.2457 | no |
| Rahu-Sun Square | BSE Sensex | 56 | 0.5313 | 0.2506 | 0.2808 | 58.93 | 0.4501 | 0.6298 | no |
| Rahu-Sun Trine | Nifty 50 | 57 | 2.802 | 0.2178 | 2.585 | 66.67 | 0.000192 | 0.001636 | yes |
| Rahu-Sun Trine | Nifty Bank | 57 | 3.614 | 0.3 | 3.314 | 77.19 | 1.511e-05 | 0.0002276 | yes |
| Rahu-Sun Trine | Nifty Midcap 100 | 57 | -0.09503 | 0.266 | -0.361 | 31.58 | 0.399 | 0.5817 | no |
| Rahu-Sun Trine | Nifty Midcap 150 | 57 | 0.6177 | 0.2642 | 0.3535 | 66.67 | 0.274 | 0.4503 | no |
| Rahu-Sun Trine | BSE Sensex | 57 | 0.1298 | 0.2506 | -0.1207 | 57.89 | 0.7527 | 0.858 | no |
| Rahu-Venus Opposition | Nifty 50 | 29 | 2.733 | 0.2178 | 2.515 | 75.86 | 0.01173 | 0.04321 | yes |
| Rahu-Venus Opposition | Nifty Bank | 29 | 3.227 | 0.3 | 2.927 | 72.41 | 0.009377 | 0.03581 | yes |
| Rahu-Venus Opposition | Nifty Midcap 100 | 29 | 0.5009 | 0.266 | 0.2349 | 48.28 | 0.6676 | 0.8036 | no |
| Rahu-Venus Opposition | Nifty Midcap 150 | 29 | 0.4392 | 0.2642 | 0.175 | 72.41 | 0.7183 | 0.8361 | no |
| Rahu-Venus Opposition | BSE Sensex | 29 | 0.5649 | 0.2506 | 0.3143 | 62.07 | 0.5643 | 0.7258 | no |
| Rahu-Venus Square | Nifty 50 | 60 | 3.025 | 0.2178 | 2.807 | 70 | 3.384e-05 | 0.0004147 | yes |
| Rahu-Venus Square | Nifty Bank | 60 | 3.455 | 0.3 | 3.155 | 70 | 0.000105 | 0.001021 | yes |
| Rahu-Venus Square | Nifty Midcap 100 | 60 | 0.07563 | 0.266 | -0.1904 | 35 | 0.6228 | 0.77 | no |
| Rahu-Venus Square | Nifty Midcap 150 | 60 | 0.4229 | 0.2642 | 0.1586 | 65 | 0.5809 | 0.7388 | no |
| Rahu-Venus Square | BSE Sensex | 60 | 0.06512 | 0.2506 | -0.1854 | 55 | 0.5919 | 0.7474 | no |
| Rahu-Venus Trine | Nifty 50 | 59 | 2.564 | 0.2178 | 2.346 | 64.41 | 0.0007129 | 0.0045 | yes |
| Rahu-Venus Trine | Nifty Bank | 59 | 2.601 | 0.3 | 2.301 | 59.32 | 0.005509 | 0.02316 | yes |
| Rahu-Venus Trine | Nifty Midcap 100 | 59 | 0.4259 | 0.266 | 0.1599 | 44.07 | 0.6097 | 0.7591 | no |
| Rahu-Venus Trine | Nifty Midcap 150 | 59 | 0.1914 | 0.2642 | -0.07284 | 61.02 | 0.8063 | 0.8912 | no |
| Rahu-Venus Trine | BSE Sensex | 59 | -0.09936 | 0.2506 | -0.3499 | 52.54 | 0.3429 | 0.5231 | no |
| Saturn-Sun Opposition | Nifty 50 | 26 | 3.116 | 0.2178 | 2.898 | 73.08 | 0.004337 | 0.01893 | yes |
| Saturn-Sun Opposition | Nifty Bank | 26 | 3.586 | 0.3 | 3.286 | 76.92 | 0.006831 | 0.02736 | yes |
| Saturn-Sun Opposition | Nifty Midcap 100 | 26 | 0.02903 | 0.266 | -0.237 | 34.62 | 0.7288 | 0.8422 | no |
| Saturn-Sun Opposition | Nifty Midcap 150 | 26 | 0.8944 | 0.2642 | 0.6302 | 73.08 | 0.201 | 0.362 | no |
| Saturn-Sun Opposition | BSE Sensex | 26 | 1.056 | 0.2506 | 0.8056 | 69.23 | 0.1641 | 0.3154 | no |
| Saturn-Sun Square | Nifty 50 | 52 | 3.217 | 0.2178 | 2.999 | 69.23 | 1.809e-05 | 0.000262 | yes |
| Saturn-Sun Square | Nifty Bank | 52 | 3.688 | 0.3 | 3.388 | 69.23 | 4.15e-05 | 0.0004833 | yes |
| Saturn-Sun Square | Nifty Midcap 100 | 52 | 0.7097 | 0.266 | 0.4437 | 46.15 | 0.1496 | 0.293 | no |
| Saturn-Sun Square | Nifty Midcap 150 | 52 | 0.9883 | 0.2642 | 0.7241 | 71.15 | 0.01357 | 0.04865 | yes |
| Saturn-Sun Square | BSE Sensex | 52 | 0.572 | 0.2506 | 0.3214 | 59.62 | 0.4288 | 0.6103 | no |
| Saturn-Sun Trine | Nifty 50 | 51 | 3.061 | 0.2178 | 2.843 | 72.55 | 7.074e-05 | 0.0007536 | yes |
| Saturn-Sun Trine | Nifty Bank | 51 | 3.505 | 0.3 | 3.205 | 64.71 | 0.0001999 | 0.001677 | yes |
| Saturn-Sun Trine | Nifty Midcap 100 | 51 | -0.07582 | 0.266 | -0.3418 | 41.18 | 0.3201 | 0.4975 | no |
| Saturn-Sun Trine | Nifty Midcap 150 | 51 | 0.9224 | 0.2642 | 0.6582 | 72.55 | 0.04904 | 0.1266 | no |
| Saturn-Sun Trine | BSE Sensex | 51 | 0.888 | 0.2506 | 0.6374 | 62.75 | 0.109 | 0.2312 | no |
| Saturn-Venus Opposition | Nifty 50 | 26 | 2.908 | 0.2178 | 2.69 | 65.38 | 0.007921 | 0.03127 | yes |
| Saturn-Venus Opposition | Nifty Bank | 26 | 3.141 | 0.3 | 2.841 | 57.69 | 0.01699 | 0.05791 | no |
| Saturn-Venus Opposition | Nifty Midcap 100 | 26 | 0.4395 | 0.266 | 0.1735 | 42.31 | 0.7736 | 0.8721 | no |
| Saturn-Venus Opposition | Nifty Midcap 150 | 26 | 0.5994 | 0.2642 | 0.3351 | 61.54 | 0.4544 | 0.6337 | no |
| Saturn-Venus Opposition | BSE Sensex | 26 | 0.6775 | 0.2506 | 0.427 | 57.69 | 0.4655 | 0.6423 | no |
| Saturn-Venus Square | Nifty 50 | 55 | 2.631 | 0.2178 | 2.413 | 65.45 | 0.0004885 | 0.003396 | yes |
| Saturn-Venus Square | Nifty Bank | 55 | 2.889 | 0.3 | 2.589 | 69.09 | 0.001665 | 0.008745 | yes |
| Saturn-Venus Square | Nifty Midcap 100 | 55 | 0.1489 | 0.266 | -0.1171 | 38.18 | 0.7368 | 0.8481 | no |
| Saturn-Venus Square | Nifty Midcap 150 | 55 | 0.304 | 0.2642 | 0.03972 | 60 | 0.9094 | 0.959 | no |
| Saturn-Venus Square | BSE Sensex | 55 | 0.01891 | 0.2506 | -0.2317 | 52.73 | 0.5544 | 0.7203 | no |
| Saturn-Venus Trine | Nifty 50 | 53 | 3.361 | 0.2178 | 3.143 | 73.58 | 3.255e-06 | 6.563e-05 | yes |
| Saturn-Venus Trine | Nifty Bank | 53 | 3.938 | 0.3 | 3.638 | 73.58 | 3.546e-06 | 6.925e-05 | yes |
| Saturn-Venus Trine | Nifty Midcap 100 | 53 | 0.2026 | 0.266 | -0.06344 | 41.51 | 0.8353 | 0.9119 | no |
| Saturn-Venus Trine | Nifty Midcap 150 | 53 | 0.751 | 0.2642 | 0.4868 | 69.81 | 0.105 | 0.2249 | no |
| Saturn-Venus Trine | BSE Sensex | 53 | 0.3597 | 0.2506 | 0.1092 | 58.49 | 0.7574 | 0.8604 | no |

## 4. Findings in words (5-day window)

### Major aspects (Trine / Square / Opposition)

* When Jupiter opposed Ketu (4 events since 2001), Nifty 50 averaged +2.00% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is +1.78 pp above the unconditional baseline. Not statistically significant (p=0.607, q=0.7565 after Benjamini-Hochberg correction).
* When Jupiter opposed Ketu (4 events since 2001), Nifty Bank averaged +1.08% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is +0.78 pp above the unconditional baseline. Not statistically significant (p=0.8666, q=0.9304 after Benjamini-Hochberg correction).
* When Jupiter opposed Ketu (4 events since 2001), Nifty Midcap 100 averaged -1.20% over the next 5 trading days (base rate +0.27%). Win rate 25.0%. That is -1.47 pp below the unconditional baseline. Not statistically significant (p=0.4494, q=0.6292 after Benjamini-Hochberg correction).
* When Jupiter opposed Ketu (4 events since 2001), Nifty Midcap 150 averaged +0.07% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is -0.20 pp below the unconditional baseline. Not statistically significant (p=0.9245, q=0.9669 after Benjamini-Hochberg correction).
* When Jupiter opposed Ketu (4 events since 2001), BSE Sensex averaged -0.60% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.86 pp below the unconditional baseline. Not statistically significant (p=0.7015, q=0.8237 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Ketu (8 events since 2000), Nifty 50 averaged +4.08% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +3.86 pp above the unconditional baseline. Not statistically significant (p=0.06384, q=0.1552 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Ketu (8 events since 2000), Nifty Bank averaged +4.80% over the next 5 trading days (base rate +0.30%). Win rate 75.0%. That is +4.50 pp above the unconditional baseline. Nominally significant at p=0.04589, but it does not survive Benjamini-Hochberg correction (q=0.1204).
* When Jupiter formed a square with Ketu (8 events since 2000), Nifty Midcap 100 averaged +0.31% over the next 5 trading days (base rate +0.27%). Win rate 37.5%. That is +0.04 pp above the unconditional baseline. Not statistically significant (p=0.9649, q=0.9862 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Ketu (8 events since 2000), Nifty Midcap 150 averaged -0.13% over the next 5 trading days (base rate +0.26%). Win rate 62.5%. That is -0.40 pp below the unconditional baseline. Not statistically significant (p=0.7675, q=0.8687 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Ketu (8 events since 2000), BSE Sensex averaged -0.59% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.84 pp below the unconditional baseline. Not statistically significant (p=0.6045, q=0.7556 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Ketu (8 events since 2000), Nifty 50 averaged +3.36% over the next 5 trading days (base rate +0.22%). Win rate 87.5%. That is +3.14 pp above the unconditional baseline. Not statistically significant (p=0.07245, q=0.1701 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Ketu (8 events since 2000), Nifty Bank averaged +3.59% over the next 5 trading days (base rate +0.30%). Win rate 87.5%. That is +3.29 pp above the unconditional baseline. Not statistically significant (p=0.1089, q=0.231 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Ketu (8 events since 2000), Nifty Midcap 100 averaged -0.47% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is -0.73 pp below the unconditional baseline. Not statistically significant (p=0.4448, q=0.6249 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Ketu (8 events since 2000), Nifty Midcap 150 averaged +1.36% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +1.10 pp above the unconditional baseline. Not statistically significant (p=0.09443, q=0.2083 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Ketu (8 events since 2000), BSE Sensex averaged +1.53% over the next 5 trading days (base rate +0.25%). Win rate 62.5%. That is +1.28 pp above the unconditional baseline. Not statistically significant (p=0.1639, q=0.3154 after Benjamini-Hochberg correction).

* When Jupiter opposed Mars (20 events since 2001), Nifty 50 averaged +5.08% over the next 5 trading days (base rate +0.22%). Win rate 80.0%. That is +4.86 pp above the unconditional baseline. Statistically significant at p=0.00041 and after Benjamini-Hochberg correction (q=0.002945).
* When Jupiter opposed Mars (20 events since 2001), Nifty Bank averaged +6.08% over the next 5 trading days (base rate +0.30%). Win rate 80.0%. That is +5.78 pp above the unconditional baseline. Statistically significant at p=0.0001187 and after Benjamini-Hochberg correction (q=0.001129).
* When Jupiter opposed Mars (20 events since 2001), Nifty Midcap 100 averaged +0.19% over the next 5 trading days (base rate +0.27%). Win rate 30.0%. That is -0.08 pp below the unconditional baseline. Not statistically significant (p=0.8764, q=0.9372 after Benjamini-Hochberg correction).
* When Jupiter opposed Mars (20 events since 2001), Nifty Midcap 150 averaged +1.48% over the next 5 trading days (base rate +0.26%). Win rate 80.0%. That is +1.21 pp above the unconditional baseline. Nominally significant at p=0.03324, but it does not survive Benjamini-Hochberg correction (q=0.0955).
* When Jupiter opposed Mars (20 events since 2001), BSE Sensex averaged +0.85% over the next 5 trading days (base rate +0.25%). Win rate 65.0%. That is +0.60 pp above the unconditional baseline. Not statistically significant (p=0.4649, q=0.6421 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Mars (28 events since 2000), Nifty 50 averaged +2.07% over the next 5 trading days (base rate +0.22%). Win rate 64.3%. That is +1.85 pp above the unconditional baseline. Not statistically significant (p=0.0682, q=0.1625 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Mars (28 events since 2000), Nifty Bank averaged +2.45% over the next 5 trading days (base rate +0.30%). Win rate 57.1%. That is +2.15 pp above the unconditional baseline. Not statistically significant (p=0.06445, q=0.1561 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Mars (28 events since 2000), Nifty Midcap 100 averaged -0.21% over the next 5 trading days (base rate +0.27%). Win rate 39.3%. That is -0.48 pp below the unconditional baseline. Not statistically significant (p=0.3834, q=0.5656 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Mars (28 events since 2000), Nifty Midcap 150 averaged -0.17% over the next 5 trading days (base rate +0.26%). Win rate 57.1%. That is -0.44 pp below the unconditional baseline. Not statistically significant (p=0.3946, q=0.5783 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Mars (28 events since 2000), BSE Sensex averaged -0.68% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.93 pp below the unconditional baseline. Not statistically significant (p=0.1119, q=0.2361 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Mars (26 events since 2000), Nifty 50 averaged +2.09% over the next 5 trading days (base rate +0.22%). Win rate 53.8%. That is +1.87 pp above the unconditional baseline. Not statistically significant (p=0.06587, q=0.1585 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Mars (26 events since 2000), Nifty Bank averaged +2.49% over the next 5 trading days (base rate +0.30%). Win rate 57.7%. That is +2.19 pp above the unconditional baseline. Not statistically significant (p=0.06183, q=0.1521 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Mars (26 events since 2000), Nifty Midcap 100 averaged +0.27% over the next 5 trading days (base rate +0.27%). Win rate 42.3%. Not statistically significant (p=0.995, q=0.9976 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Mars (26 events since 2000), Nifty Midcap 150 averaged -0.49% over the next 5 trading days (base rate +0.26%). Win rate 42.3%. That is -0.75 pp below the unconditional baseline. Not statistically significant (p=0.06622, q=0.1591 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Mars (26 events since 2000), BSE Sensex averaged -0.71% over the next 5 trading days (base rate +0.25%). Win rate 34.6%. That is -0.96 pp below the unconditional baseline. Nominally significant at p=0.0463, but it does not survive Benjamini-Hochberg correction (q=0.1213).

* When Jupiter opposed Mercury (28 events since 2000), Nifty 50 averaged +2.93% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +2.71 pp above the unconditional baseline. Statistically significant at p=0.002592 and after Benjamini-Hochberg correction (q=0.0124).
* When Jupiter opposed Mercury (28 events since 2000), Nifty Bank averaged +2.93% over the next 5 trading days (base rate +0.30%). Win rate 60.7%. That is +2.63 pp above the unconditional baseline. Statistically significant at p=0.01378 and after Benjamini-Hochberg correction (q=0.04906).
* When Jupiter opposed Mercury (28 events since 2000), Nifty Midcap 100 averaged +1.13% over the next 5 trading days (base rate +0.27%). Win rate 57.1%. That is +0.86 pp above the unconditional baseline. Nominally significant at p=0.03712, but it does not survive Benjamini-Hochberg correction (q=0.1037).
* When Jupiter opposed Mercury (28 events since 2000), Nifty Midcap 150 averaged +0.32% over the next 5 trading days (base rate +0.26%). Win rate 64.3%. That is +0.05 pp above the unconditional baseline. Not statistically significant (p=0.9237, q=0.9669 after Benjamini-Hochberg correction).
* When Jupiter opposed Mercury (28 events since 2000), BSE Sensex averaged +0.19% over the next 5 trading days (base rate +0.25%). Win rate 64.3%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.9149, q=0.9623 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Mercury (65 events since 2000), Nifty 50 averaged +2.97% over the next 5 trading days (base rate +0.22%). Win rate 66.2%. That is +2.75 pp above the unconditional baseline. Statistically significant at p=0.0001911 and after Benjamini-Hochberg correction (q=0.001633).
* When Jupiter formed a square with Mercury (65 events since 2000), Nifty Bank averaged +3.68% over the next 5 trading days (base rate +0.30%). Win rate 66.2%. That is +3.38 pp above the unconditional baseline. Statistically significant at p=0.0001086 and after Benjamini-Hochberg correction (q=0.001049).
* When Jupiter formed a square with Mercury (65 events since 2000), Nifty Midcap 100 averaged +0.01% over the next 5 trading days (base rate +0.27%). Win rate 40.0%. That is -0.25 pp below the unconditional baseline. Not statistically significant (p=0.5645, q=0.7258 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Mercury (65 events since 2000), Nifty Midcap 150 averaged +0.66% over the next 5 trading days (base rate +0.26%). Win rate 64.6%. That is +0.39 pp above the unconditional baseline. Not statistically significant (p=0.3883, q=0.5706 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Mercury (65 events since 2000), BSE Sensex averaged +0.47% over the next 5 trading days (base rate +0.25%). Win rate 55.4%. That is +0.22 pp above the unconditional baseline. Not statistically significant (p=0.696, q=0.82 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Mercury (63 events since 2000), Nifty 50 averaged +2.50% over the next 5 trading days (base rate +0.22%). Win rate 73.0%. That is +2.28 pp above the unconditional baseline. Statistically significant at p=0.0002957 and after Benjamini-Hochberg correction (q=0.002249).
* When Jupiter formed a trine with Mercury (63 events since 2000), Nifty Bank averaged +2.88% over the next 5 trading days (base rate +0.30%). Win rate 69.8%. That is +2.58 pp above the unconditional baseline. Statistically significant at p=0.0005369 and after Benjamini-Hochberg correction (q=0.003628).
* When Jupiter formed a trine with Mercury (63 events since 2000), Nifty Midcap 100 averaged -0.04% over the next 5 trading days (base rate +0.27%). Win rate 39.7%. That is -0.30 pp below the unconditional baseline. Not statistically significant (p=0.3195, q=0.4967 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Mercury (63 events since 2000), Nifty Midcap 150 averaged +0.22% over the next 5 trading days (base rate +0.26%). Win rate 68.3%. That is -0.05 pp below the unconditional baseline. Not statistically significant (p=0.8763, q=0.9372 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Mercury (63 events since 2000), BSE Sensex averaged -0.35% over the next 5 trading days (base rate +0.25%). Win rate 55.6%. That is -0.60 pp below the unconditional baseline. Not statistically significant (p=0.08847, q=0.1975 after Benjamini-Hochberg correction).

* When Jupiter opposed Moon (56 events since 2000), Nifty 50 averaged +3.63% over the next 5 trading days (base rate +0.22%). Win rate 66.1%. That is +3.42 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.046e-05).
* When Jupiter opposed Moon (56 events since 2000), Nifty Bank averaged +4.15% over the next 5 trading days (base rate +0.30%). Win rate 69.6%. That is +3.85 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=8.662e-05).
* When Jupiter opposed Moon (56 events since 2000), Nifty Midcap 100 averaged +0.27% over the next 5 trading days (base rate +0.27%). Win rate 39.3%. Not statistically significant (p=0.9897, q=0.9958 after Benjamini-Hochberg correction).
* When Jupiter opposed Moon (56 events since 2000), Nifty Midcap 150 averaged +0.74% over the next 5 trading days (base rate +0.26%). Win rate 67.9%. That is +0.48 pp above the unconditional baseline. Not statistically significant (p=0.1455, q=0.2877 after Benjamini-Hochberg correction).
* When Jupiter opposed Moon (56 events since 2000), BSE Sensex averaged +0.61% over the next 5 trading days (base rate +0.25%). Win rate 57.1%. That is +0.36 pp above the unconditional baseline. Not statistically significant (p=0.3324, q=0.5119 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Moon (122 events since 2000), Nifty 50 averaged +2.83% over the next 5 trading days (base rate +0.22%). Win rate 68.9%. That is +2.61 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=4.405e-06).
* When Jupiter formed a square with Moon (122 events since 2000), Nifty Bank averaged +3.26% over the next 5 trading days (base rate +0.30%). Win rate 66.4%. That is +2.96 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=9.871e-06).
* When Jupiter formed a square with Moon (122 events since 2000), Nifty Midcap 100 averaged +0.25% over the next 5 trading days (base rate +0.27%). Win rate 45.9%. That is -0.02 pp below the unconditional baseline. Not statistically significant (p=0.9537, q=0.982 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Moon (122 events since 2000), Nifty Midcap 150 averaged +0.83% over the next 5 trading days (base rate +0.26%). Win rate 66.4%. That is +0.57 pp above the unconditional baseline. Not statistically significant (p=0.0632, q=0.1544 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Moon (122 events since 2000), BSE Sensex averaged +0.26% over the next 5 trading days (base rate +0.25%). Win rate 58.2%. That is +0.01 pp above the unconditional baseline. Not statistically significant (p=0.9739, q=0.9895 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Moon (96 events since 2000), Nifty 50 averaged +2.85% over the next 5 trading days (base rate +0.22%). Win rate 70.8%. That is +2.64 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.413e-05).
* When Jupiter formed a trine with Moon (96 events since 2000), Nifty Bank averaged +3.12% over the next 5 trading days (base rate +0.30%). Win rate 65.6%. That is +2.82 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.82e-05).
* When Jupiter formed a trine with Moon (96 events since 2000), Nifty Midcap 100 averaged +0.27% over the next 5 trading days (base rate +0.27%). Win rate 45.8%. Not statistically significant (p=0.9919, q=0.9968 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Moon (96 events since 2000), Nifty Midcap 150 averaged +0.59% over the next 5 trading days (base rate +0.26%). Win rate 69.8%. That is +0.32 pp above the unconditional baseline. Not statistically significant (p=0.1664, q=0.3183 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Moon (96 events since 2000), BSE Sensex averaged +0.35% over the next 5 trading days (base rate +0.25%). Win rate 59.4%. That is +0.10 pp above the unconditional baseline. Not statistically significant (p=0.7213, q=0.8384 after Benjamini-Hochberg correction).

* When Jupiter opposed Rahu (3 events since 2005), Nifty 50 averaged +5.22% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +5.00 pp above the unconditional baseline. Not statistically significant (p=0.157, q=0.3048 after Benjamini-Hochberg correction).
* When Jupiter opposed Rahu (3 events since 2005), Nifty Bank averaged +6.35% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +6.05 pp above the unconditional baseline. Not statistically significant (p=0.1251, q=0.2567 after Benjamini-Hochberg correction).
* When Jupiter opposed Rahu (3 events since 2005), Nifty Midcap 100 averaged +0.81% over the next 5 trading days (base rate +0.27%). Win rate 66.7%. That is +0.54 pp above the unconditional baseline. Not statistically significant (p=0.5334, q=0.7018 after Benjamini-Hochberg correction).
* When Jupiter opposed Rahu (3 events since 2005), Nifty Midcap 150 averaged +2.61% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +2.34 pp above the unconditional baseline. Nominally significant at p=0.04725, but it does not survive Benjamini-Hochberg correction (q=0.1231).
* When Jupiter opposed Rahu (3 events since 2005), BSE Sensex averaged +1.51% over the next 5 trading days (base rate +0.25%). Win rate 66.7%. That is +1.26 pp above the unconditional baseline. Not statistically significant (p=0.4634, q=0.6414 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Rahu (8 events since 2000), Nifty 50 averaged +4.08% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +3.86 pp above the unconditional baseline. Not statistically significant (p=0.06384, q=0.1552 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Rahu (8 events since 2000), Nifty Bank averaged +4.80% over the next 5 trading days (base rate +0.30%). Win rate 75.0%. That is +4.50 pp above the unconditional baseline. Nominally significant at p=0.04589, but it does not survive Benjamini-Hochberg correction (q=0.1204).
* When Jupiter formed a square with Rahu (8 events since 2000), Nifty Midcap 100 averaged +0.31% over the next 5 trading days (base rate +0.27%). Win rate 37.5%. That is +0.04 pp above the unconditional baseline. Not statistically significant (p=0.9649, q=0.9862 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Rahu (8 events since 2000), Nifty Midcap 150 averaged -0.13% over the next 5 trading days (base rate +0.26%). Win rate 62.5%. That is -0.40 pp below the unconditional baseline. Not statistically significant (p=0.7675, q=0.8687 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Rahu (8 events since 2000), BSE Sensex averaged -0.59% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.84 pp below the unconditional baseline. Not statistically significant (p=0.6045, q=0.7556 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Rahu (9 events since 2003), Nifty 50 averaged +4.74% over the next 5 trading days (base rate +0.22%). Win rate 77.8%. That is +4.53 pp above the unconditional baseline. Nominally significant at p=0.02299, but it does not survive Benjamini-Hochberg correction (q=0.07316).
* When Jupiter formed a trine with Rahu (9 events since 2003), Nifty Bank averaged +5.00% over the next 5 trading days (base rate +0.30%). Win rate 77.8%. That is +4.70 pp above the unconditional baseline. Nominally significant at p=0.04535, but it does not survive Benjamini-Hochberg correction (q=0.1193).
* When Jupiter formed a trine with Rahu (9 events since 2003), Nifty Midcap 100 averaged +0.69% over the next 5 trading days (base rate +0.27%). Win rate 44.4%. That is +0.42 pp above the unconditional baseline. Not statistically significant (p=0.3975, q=0.5805 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Rahu (9 events since 2003), Nifty Midcap 150 averaged +1.29% over the next 5 trading days (base rate +0.26%). Win rate 88.9%. That is +1.03 pp above the unconditional baseline. Nominally significant at p=0.03857, but it does not survive Benjamini-Hochberg correction (q=0.1063).
* When Jupiter formed a trine with Rahu (9 events since 2003), BSE Sensex averaged +1.72% over the next 5 trading days (base rate +0.25%). Win rate 77.8%. That is +1.47 pp above the unconditional baseline. Not statistically significant (p=0.05034, q=0.1289 after Benjamini-Hochberg correction).

* When Jupiter opposed Saturn (3 events since 2010), Nifty 50 averaged +3.03% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +2.81 pp above the unconditional baseline. Nominally significant at p=0.02515, but it does not survive Benjamini-Hochberg correction (q=0.07793).
* When Jupiter opposed Saturn (3 events since 2010), Nifty Bank averaged +3.12% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +2.82 pp above the unconditional baseline. Nominally significant at p=0.01974, but it does not survive Benjamini-Hochberg correction (q=0.06552).
* When Jupiter opposed Saturn (3 events since 2010), Nifty Midcap 100 averaged +2.95% over the next 5 trading days (base rate +0.27%). Win rate 100.0%. That is +2.68 pp above the unconditional baseline. Not statistically significant (p=0.1375, q=0.2754 after Benjamini-Hochberg correction).
* When Jupiter opposed Saturn (3 events since 2010), Nifty Midcap 150 averaged +3.06% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +2.80 pp above the unconditional baseline. Nominally significant at p=0.02647, but it does not survive Benjamini-Hochberg correction (q=0.08069).
* When Jupiter opposed Saturn (3 events since 2010), BSE Sensex averaged +2.96% over the next 5 trading days (base rate +0.25%). Win rate 100.0%. That is +2.71 pp above the unconditional baseline. Nominally significant at p=0.04293, but it does not survive Benjamini-Hochberg correction (q=0.1143).

* When Jupiter formed a square with Saturn (9 events since 2005), Nifty 50 averaged +3.84% over the next 5 trading days (base rate +0.22%). Win rate 77.8%. That is +3.62 pp above the unconditional baseline. Nominally significant at p=0.04224, but it does not survive Benjamini-Hochberg correction (q=0.1128).
* When Jupiter formed a square with Saturn (9 events since 2005), Nifty Bank averaged +4.24% over the next 5 trading days (base rate +0.30%). Win rate 88.9%. That is +3.94 pp above the unconditional baseline. Nominally significant at p=0.04734, but it does not survive Benjamini-Hochberg correction (q=0.1232).
* When Jupiter formed a square with Saturn (9 events since 2005), Nifty Midcap 100 averaged +0.19% over the next 5 trading days (base rate +0.27%). Win rate 44.4%. That is -0.07 pp below the unconditional baseline. Not statistically significant (p=0.8417, q=0.9146 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Saturn (9 events since 2005), Nifty Midcap 150 averaged +0.45% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.18 pp above the unconditional baseline. Not statistically significant (p=0.7778, q=0.8736 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Saturn (9 events since 2005), BSE Sensex averaged +0.39% over the next 5 trading days (base rate +0.25%). Win rate 55.6%. That is +0.14 pp above the unconditional baseline. Not statistically significant (p=0.8323, q=0.9097 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Saturn (10 events since 2007), Nifty 50 averaged +1.16% over the next 5 trading days (base rate +0.22%). Win rate 60.0%. That is +0.94 pp above the unconditional baseline. Not statistically significant (p=0.5935, q=0.7488 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Saturn (10 events since 2007), Nifty Bank averaged +1.90% over the next 5 trading days (base rate +0.30%). Win rate 40.0%. That is +1.60 pp above the unconditional baseline. Not statistically significant (p=0.433, q=0.6156 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Saturn (10 events since 2007), Nifty Midcap 100 averaged -0.10% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is -0.36 pp below the unconditional baseline. Not statistically significant (p=0.8339, q=0.9109 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Saturn (10 events since 2007), Nifty Midcap 150 averaged -0.24% over the next 5 trading days (base rate +0.26%). Win rate 60.0%. That is -0.50 pp below the unconditional baseline. Not statistically significant (p=0.6547, q=0.7938 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Saturn (10 events since 2007), BSE Sensex averaged -0.21% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.46 pp below the unconditional baseline. Not statistically significant (p=0.697, q=0.8201 after Benjamini-Hochberg correction).

* When Jupiter opposed Sun (24 events since 2000), Nifty 50 averaged +2.67% over the next 5 trading days (base rate +0.22%). Win rate 62.5%. That is +2.45 pp above the unconditional baseline. Nominally significant at p=0.02846, but it does not survive Benjamini-Hochberg correction (q=0.08543).
* When Jupiter opposed Sun (24 events since 2000), Nifty Bank averaged +3.18% over the next 5 trading days (base rate +0.30%). Win rate 70.8%. That is +2.88 pp above the unconditional baseline. Nominally significant at p=0.02536, but it does not survive Benjamini-Hochberg correction (q=0.07841).
* When Jupiter opposed Sun (24 events since 2000), Nifty Midcap 100 averaged -0.45% over the next 5 trading days (base rate +0.27%). Win rate 29.2%. That is -0.72 pp below the unconditional baseline. Not statistically significant (p=0.419, q=0.6006 after Benjamini-Hochberg correction).
* When Jupiter opposed Sun (24 events since 2000), Nifty Midcap 150 averaged +0.09% over the next 5 trading days (base rate +0.26%). Win rate 58.3%. That is -0.17 pp below the unconditional baseline. Not statistically significant (p=0.7342, q=0.8459 after Benjamini-Hochberg correction).
* When Jupiter opposed Sun (24 events since 2000), BSE Sensex averaged -0.35% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.60 pp below the unconditional baseline. Not statistically significant (p=0.3084, q=0.4867 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Sun (49 events since 2000), Nifty 50 averaged +3.41% over the next 5 trading days (base rate +0.22%). Win rate 77.6%. That is +3.19 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0002829).
* When Jupiter formed a square with Sun (49 events since 2000), Nifty Bank averaged +4.16% over the next 5 trading days (base rate +0.30%). Win rate 81.6%. That is +3.86 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.402e-05).
* When Jupiter formed a square with Sun (49 events since 2000), Nifty Midcap 100 averaged +0.02% over the next 5 trading days (base rate +0.27%). Win rate 36.7%. That is -0.24 pp below the unconditional baseline. Not statistically significant (p=0.6319, q=0.7778 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Sun (49 events since 2000), Nifty Midcap 150 averaged +0.83% over the next 5 trading days (base rate +0.26%). Win rate 71.4%. That is +0.57 pp above the unconditional baseline. Not statistically significant (p=0.06857, q=0.1632 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Sun (49 events since 2000), BSE Sensex averaged +0.82% over the next 5 trading days (base rate +0.25%). Win rate 71.4%. That is +0.57 pp above the unconditional baseline. Not statistically significant (p=0.1287, q=0.2627 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Sun (48 events since 2000), Nifty 50 averaged +2.90% over the next 5 trading days (base rate +0.22%). Win rate 68.8%. That is +2.69 pp above the unconditional baseline. Statistically significant at p=0.0003138 and after Benjamini-Hochberg correction (q=0.002368).
* When Jupiter formed a trine with Sun (48 events since 2000), Nifty Bank averaged +3.56% over the next 5 trading days (base rate +0.30%). Win rate 72.9%. That is +3.26 pp above the unconditional baseline. Statistically significant at p=0.000198 and after Benjamini-Hochberg correction (q=0.001673).
* When Jupiter formed a trine with Sun (48 events since 2000), Nifty Midcap 100 averaged +0.29% over the next 5 trading days (base rate +0.27%). Win rate 39.6%. That is +0.02 pp above the unconditional baseline. Not statistically significant (p=0.9556, q=0.982 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Sun (48 events since 2000), Nifty Midcap 150 averaged +0.55% over the next 5 trading days (base rate +0.26%). Win rate 70.8%. That is +0.29 pp above the unconditional baseline. Not statistically significant (p=0.3237, q=0.5018 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Sun (48 events since 2000), BSE Sensex averaged +0.43% over the next 5 trading days (base rate +0.25%). Win rate 62.5%. That is +0.18 pp above the unconditional baseline. Not statistically significant (p=0.6273, q=0.7741 after Benjamini-Hochberg correction).

* When Jupiter opposed Venus (24 events since 2000), Nifty 50 averaged +3.88% over the next 5 trading days (base rate +0.22%). Win rate 79.2%. That is +3.66 pp above the unconditional baseline. Statistically significant at p=0.0002413 and after Benjamini-Hochberg correction (q=0.001913).
* When Jupiter opposed Venus (24 events since 2000), Nifty Bank averaged +5.20% over the next 5 trading days (base rate +0.30%). Win rate 91.7%. That is +4.90 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000275).
* When Jupiter opposed Venus (24 events since 2000), Nifty Midcap 100 averaged +1.21% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.95 pp above the unconditional baseline. Not statistically significant (p=0.05369, q=0.1354 after Benjamini-Hochberg correction).
* When Jupiter opposed Venus (24 events since 2000), Nifty Midcap 150 averaged +1.01% over the next 5 trading days (base rate +0.26%). Win rate 70.8%. That is +0.74 pp above the unconditional baseline. Not statistically significant (p=0.1775, q=0.3313 after Benjamini-Hochberg correction).
* When Jupiter opposed Venus (24 events since 2000), BSE Sensex averaged +0.85% over the next 5 trading days (base rate +0.25%). Win rate 62.5%. That is +0.60 pp above the unconditional baseline. Not statistically significant (p=0.3238, q=0.5018 after Benjamini-Hochberg correction).

* When Jupiter formed a square with Venus (55 events since 2000), Nifty 50 averaged +3.07% over the next 5 trading days (base rate +0.22%). Win rate 65.5%. That is +2.85 pp above the unconditional baseline. Statistically significant at p=0.0001571 and after Benjamini-Hochberg correction (q=0.001396).
* When Jupiter formed a square with Venus (55 events since 2000), Nifty Bank averaged +3.58% over the next 5 trading days (base rate +0.30%). Win rate 67.3%. That is +3.28 pp above the unconditional baseline. Statistically significant at p=0.0001084 and after Benjamini-Hochberg correction (q=0.001049).
* When Jupiter formed a square with Venus (55 events since 2000), Nifty Midcap 100 averaged -0.48% over the next 5 trading days (base rate +0.27%). Win rate 32.7%. That is -0.74 pp below the unconditional baseline. Not statistically significant (p=0.07454, q=0.1738 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Venus (55 events since 2000), Nifty Midcap 150 averaged +0.46% over the next 5 trading days (base rate +0.26%). Win rate 65.5%. That is +0.19 pp above the unconditional baseline. Not statistically significant (p=0.5642, q=0.7258 after Benjamini-Hochberg correction).
* When Jupiter formed a square with Venus (55 events since 2000), BSE Sensex averaged +0.21% over the next 5 trading days (base rate +0.25%). Win rate 54.5%. That is -0.04 pp below the unconditional baseline. Not statistically significant (p=0.919, q=0.9648 after Benjamini-Hochberg correction).

* When Jupiter formed a trine with Venus (49 events since 2000), Nifty 50 averaged +2.84% over the next 5 trading days (base rate +0.22%). Win rate 65.3%. That is +2.62 pp above the unconditional baseline. Statistically significant at p=0.0007121 and after Benjamini-Hochberg correction (q=0.0045).
* When Jupiter formed a trine with Venus (49 events since 2000), Nifty Bank averaged +3.09% over the next 5 trading days (base rate +0.30%). Win rate 61.2%. That is +2.79 pp above the unconditional baseline. Statistically significant at p=0.001616 and after Benjamini-Hochberg correction (q=0.008558).
* When Jupiter formed a trine with Venus (49 events since 2000), Nifty Midcap 100 averaged -0.18% over the next 5 trading days (base rate +0.27%). Win rate 32.7%. That is -0.45 pp below the unconditional baseline. Not statistically significant (p=0.1898, q=0.3479 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Venus (49 events since 2000), Nifty Midcap 150 averaged +0.18% over the next 5 trading days (base rate +0.26%). Win rate 61.2%. That is -0.08 pp below the unconditional baseline. Not statistically significant (p=0.8102, q=0.8947 after Benjamini-Hochberg correction).
* When Jupiter formed a trine with Venus (49 events since 2000), BSE Sensex averaged -0.40% over the next 5 trading days (base rate +0.25%). Win rate 42.9%. That is -0.65 pp below the unconditional baseline. Not statistically significant (p=0.06732, q=0.1609 after Benjamini-Hochberg correction).

* When Ketu opposed Mars (16 events since 2000), Nifty 50 averaged +3.14% over the next 5 trading days (base rate +0.22%). Win rate 68.8%. That is +2.92 pp above the unconditional baseline. Nominally significant at p=0.02918, but it does not survive Benjamini-Hochberg correction (q=0.08691).
* When Ketu opposed Mars (16 events since 2000), Nifty Bank averaged +3.07% over the next 5 trading days (base rate +0.30%). Win rate 68.8%. That is +2.77 pp above the unconditional baseline. Not statistically significant (p=0.1054, q=0.2251 after Benjamini-Hochberg correction).
* When Ketu opposed Mars (16 events since 2000), Nifty Midcap 100 averaged +0.23% over the next 5 trading days (base rate +0.27%). Win rate 37.5%. That is -0.03 pp below the unconditional baseline. Not statistically significant (p=0.9557, q=0.982 after Benjamini-Hochberg correction).
* When Ketu opposed Mars (16 events since 2000), Nifty Midcap 150 averaged +0.52% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.5485, q=0.7152 after Benjamini-Hochberg correction).
* When Ketu opposed Mars (16 events since 2000), BSE Sensex averaged +0.19% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.9246, q=0.9669 after Benjamini-Hochberg correction).

* When Ketu formed a square with Mars (34 events since 2000), Nifty 50 averaged +3.68% over the next 5 trading days (base rate +0.22%). Win rate 79.4%. That is +3.46 pp above the unconditional baseline. Statistically significant at p=0.000583 and after Benjamini-Hochberg correction (q=0.003856).
* When Ketu formed a square with Mars (34 events since 2000), Nifty Bank averaged +4.12% over the next 5 trading days (base rate +0.30%). Win rate 70.6%. That is +3.82 pp above the unconditional baseline. Statistically significant at p=0.00197 and after Benjamini-Hochberg correction (q=0.009983).
* When Ketu formed a square with Mars (34 events since 2000), Nifty Midcap 100 averaged +0.75% over the next 5 trading days (base rate +0.27%). Win rate 44.1%. That is +0.48 pp above the unconditional baseline. Not statistically significant (p=0.3938, q=0.5773 after Benjamini-Hochberg correction).
* When Ketu formed a square with Mars (34 events since 2000), Nifty Midcap 150 averaged +1.15% over the next 5 trading days (base rate +0.26%). Win rate 73.5%. That is +0.89 pp above the unconditional baseline. Not statistically significant (p=0.1632, q=0.3146 after Benjamini-Hochberg correction).
* When Ketu formed a square with Mars (34 events since 2000), BSE Sensex averaged +0.91% over the next 5 trading days (base rate +0.25%). Win rate 58.8%. That is +0.66 pp above the unconditional baseline. Not statistically significant (p=0.3331, q=0.512 after Benjamini-Hochberg correction).

* When Ketu formed a trine with Mars (34 events since 2000), Nifty 50 averaged +3.56% over the next 5 trading days (base rate +0.22%). Win rate 79.4%. That is +3.34 pp above the unconditional baseline. Statistically significant at p=0.0002949 and after Benjamini-Hochberg correction (q=0.002248).
* When Ketu formed a trine with Mars (34 events since 2000), Nifty Bank averaged +4.35% over the next 5 trading days (base rate +0.30%). Win rate 79.4%. That is +4.05 pp above the unconditional baseline. Statistically significant at p=0.0001378 and after Benjamini-Hochberg correction (q=0.00126).
* When Ketu formed a trine with Mars (34 events since 2000), Nifty Midcap 100 averaged +0.26% over the next 5 trading days (base rate +0.27%). Win rate 35.3%. Not statistically significant (p=0.9974, q=0.9993 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Mars (34 events since 2000), Nifty Midcap 150 averaged +1.05% over the next 5 trading days (base rate +0.26%). Win rate 73.5%. That is +0.78 pp above the unconditional baseline. Not statistically significant (p=0.09329, q=0.2062 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Mars (34 events since 2000), BSE Sensex averaged +1.04% over the next 5 trading days (base rate +0.25%). Win rate 61.8%. That is +0.79 pp above the unconditional baseline. Not statistically significant (p=0.1729, q=0.3265 after Benjamini-Hochberg correction).

* When Ketu opposed Mercury (42 events since 2000), Nifty 50 averaged +1.76% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +1.55 pp above the unconditional baseline. Nominally significant at p=0.03964, but it does not survive Benjamini-Hochberg correction (q=0.1078).
* When Ketu opposed Mercury (42 events since 2000), Nifty Bank averaged +1.78% over the next 5 trading days (base rate +0.30%). Win rate 69.0%. That is +1.48 pp above the unconditional baseline. Not statistically significant (p=0.1234, q=0.2544 after Benjamini-Hochberg correction).
* When Ketu opposed Mercury (42 events since 2000), Nifty Midcap 100 averaged -0.04% over the next 5 trading days (base rate +0.27%). Win rate 40.5%. That is -0.31 pp below the unconditional baseline. Not statistically significant (p=0.4363, q=0.6173 after Benjamini-Hochberg correction).
* When Ketu opposed Mercury (42 events since 2000), Nifty Midcap 150 averaged +0.21% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is -0.05 pp below the unconditional baseline. Not statistically significant (p=0.9111, q=0.9595 after Benjamini-Hochberg correction).
* When Ketu opposed Mercury (42 events since 2000), BSE Sensex averaged -0.06% over the next 5 trading days (base rate +0.25%). Win rate 59.5%. That is -0.31 pp below the unconditional baseline. Not statistically significant (p=0.5251, q=0.6971 after Benjamini-Hochberg correction).

* When Ketu formed a square with Mercury (56 events since 2000), Nifty 50 averaged +2.61% over the next 5 trading days (base rate +0.22%). Win rate 66.1%. That is +2.40 pp above the unconditional baseline. Statistically significant at p=0.0008148 and after Benjamini-Hochberg correction (q=0.005034).
* When Ketu formed a square with Mercury (56 events since 2000), Nifty Bank averaged +2.71% over the next 5 trading days (base rate +0.30%). Win rate 67.9%. That is +2.41 pp above the unconditional baseline. Statistically significant at p=0.004149 and after Benjamini-Hochberg correction (q=0.01826).
* When Ketu formed a square with Mercury (56 events since 2000), Nifty Midcap 100 averaged +0.50% over the next 5 trading days (base rate +0.27%). Win rate 42.9%. That is +0.24 pp above the unconditional baseline. Not statistically significant (p=0.5283, q=0.6998 after Benjamini-Hochberg correction).
* When Ketu formed a square with Mercury (56 events since 2000), Nifty Midcap 150 averaged +0.05% over the next 5 trading days (base rate +0.26%). Win rate 62.5%. That is -0.22 pp below the unconditional baseline. Not statistically significant (p=0.5599, q=0.7248 after Benjamini-Hochberg correction).
* When Ketu formed a square with Mercury (56 events since 2000), BSE Sensex averaged -0.17% over the next 5 trading days (base rate +0.25%). Win rate 46.4%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.3436, q=0.5236 after Benjamini-Hochberg correction).

* When Ketu formed a trine with Mercury (56 events since 2000), Nifty 50 averaged +3.68% over the next 5 trading days (base rate +0.22%). Win rate 78.6%. That is +3.47 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.413e-05).
* When Ketu formed a trine with Mercury (56 events since 2000), Nifty Bank averaged +4.58% over the next 5 trading days (base rate +0.30%). Win rate 82.1%. That is +4.28 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.493e-06).
* When Ketu formed a trine with Mercury (56 events since 2000), Nifty Midcap 100 averaged +0.22% over the next 5 trading days (base rate +0.27%). Win rate 37.5%. That is -0.05 pp below the unconditional baseline. Not statistically significant (p=0.9072, q=0.9583 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Mercury (56 events since 2000), Nifty Midcap 150 averaged +1.39% over the next 5 trading days (base rate +0.26%). Win rate 76.8%. That is +1.13 pp above the unconditional baseline. Statistically significant at p=0.002181 and after Benjamini-Hochberg correction (q=0.01068).
* When Ketu formed a trine with Mercury (56 events since 2000), BSE Sensex averaged +0.70% over the next 5 trading days (base rate +0.25%). Win rate 58.9%. That is +0.45 pp above the unconditional baseline. Not statistically significant (p=0.2797, q=0.4561 after Benjamini-Hochberg correction).

* When Ketu opposed Moon (54 events since 2000), Nifty 50 averaged +3.09% over the next 5 trading days (base rate +0.22%). Win rate 68.5%. That is +2.87 pp above the unconditional baseline. Statistically significant at p=0.0002346 and after Benjamini-Hochberg correction (q=0.001864).
* When Ketu opposed Moon (54 events since 2000), Nifty Bank averaged +3.37% over the next 5 trading days (base rate +0.30%). Win rate 68.5%. That is +3.07 pp above the unconditional baseline. Statistically significant at p=0.001348 and after Benjamini-Hochberg correction (q=0.007413).
* When Ketu opposed Moon (54 events since 2000), Nifty Midcap 100 averaged -0.15% over the next 5 trading days (base rate +0.27%). Win rate 40.7%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.221, q=0.3854 after Benjamini-Hochberg correction).
* When Ketu opposed Moon (54 events since 2000), Nifty Midcap 150 averaged +0.75% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.49 pp above the unconditional baseline. Not statistically significant (p=0.2911, q=0.466 after Benjamini-Hochberg correction).
* When Ketu opposed Moon (54 events since 2000), BSE Sensex averaged +0.57% over the next 5 trading days (base rate +0.25%). Win rate 59.3%. That is +0.32 pp above the unconditional baseline. Not statistically significant (p=0.4728, q=0.6502 after Benjamini-Hochberg correction).

* When Ketu formed a square with Moon (113 events since 2000), Nifty 50 averaged +2.06% over the next 5 trading days (base rate +0.22%). Win rate 60.2%. That is +1.85 pp above the unconditional baseline. Statistically significant at p=0.0002204 and after Benjamini-Hochberg correction (q=0.00177).
* When Ketu formed a square with Moon (113 events since 2000), Nifty Bank averaged +2.33% over the next 5 trading days (base rate +0.30%). Win rate 61.1%. That is +2.03 pp above the unconditional baseline. Statistically significant at p=0.0005221 and after Benjamini-Hochberg correction (q=0.003559).
* When Ketu formed a square with Moon (113 events since 2000), Nifty Midcap 100 averaged -0.14% over the next 5 trading days (base rate +0.27%). Win rate 38.1%. That is -0.41 pp below the unconditional baseline. Not statistically significant (p=0.1726, q=0.3264 after Benjamini-Hochberg correction).
* When Ketu formed a square with Moon (113 events since 2000), Nifty Midcap 150 averaged +0.08% over the next 5 trading days (base rate +0.26%). Win rate 59.3%. That is -0.18 pp below the unconditional baseline. Not statistically significant (p=0.5178, q=0.691 after Benjamini-Hochberg correction).
* When Ketu formed a square with Moon (113 events since 2000), BSE Sensex averaged -0.18% over the next 5 trading days (base rate +0.25%). Win rate 50.4%. That is -0.43 pp below the unconditional baseline. Not statistically significant (p=0.1365, q=0.2741 after Benjamini-Hochberg correction).

* When Ketu formed a trine with Moon (115 events since 2000), Nifty 50 averaged +3.49% over the next 5 trading days (base rate +0.22%). Win rate 70.4%. That is +3.27 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.713e-08).
* When Ketu formed a trine with Moon (115 events since 2000), Nifty Bank averaged +4.14% over the next 5 trading days (base rate +0.30%). Win rate 69.6%. That is +3.84 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.078e-07).
* When Ketu formed a trine with Moon (115 events since 2000), Nifty Midcap 100 averaged +0.26% over the next 5 trading days (base rate +0.27%). Win rate 40.9%. Not statistically significant (p=0.9952, q=0.9976 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Moon (115 events since 2000), Nifty Midcap 150 averaged +0.95% over the next 5 trading days (base rate +0.26%). Win rate 68.7%. That is +0.69 pp above the unconditional baseline. Nominally significant at p=0.02795, but it does not survive Benjamini-Hochberg correction (q=0.08413).
* When Ketu formed a trine with Moon (115 events since 2000), BSE Sensex averaged +0.69% over the next 5 trading days (base rate +0.25%). Win rate 58.3%. That is +0.44 pp above the unconditional baseline. Not statistically significant (p=0.2087, q=0.371 after Benjamini-Hochberg correction).

* When Ketu opposed Rahu (1 event since 2000), Nifty 50 averaged +9.73% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +9.52 pp above the unconditional baseline. Not statistically significant (p=nan).
* When Ketu opposed Rahu (1 event since 2000), Nifty Bank averaged +10.93% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +10.63 pp above the unconditional baseline. Not statistically significant (p=nan).
* When Ketu opposed Rahu (1 event since 2000), Nifty Midcap 100 averaged -0.29% over the next 5 trading days (base rate +0.27%). Win rate 0.0%. That is -0.56 pp below the unconditional baseline. Not statistically significant (p=nan).
* When Ketu opposed Rahu (1 event since 2000), Nifty Midcap 150 averaged +1.58% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +1.32 pp above the unconditional baseline. Not statistically significant (p=nan).
* When Ketu opposed Rahu (1 event since 2000), BSE Sensex averaged -3.55% over the next 5 trading days (base rate +0.25%). Win rate 0.0%. That is -3.80 pp below the unconditional baseline. Not statistically significant (p=nan).

* When Ketu opposed Saturn (3 events since 2002), Nifty 50 averaged +4.88% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +4.66 pp above the unconditional baseline. Not statistically significant (p=0.2208, q=0.3854 after Benjamini-Hochberg correction).
* When Ketu opposed Saturn (3 events since 2002), Nifty Bank averaged +6.01% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +5.71 pp above the unconditional baseline. Not statistically significant (p=0.1737, q=0.3269 after Benjamini-Hochberg correction).
* When Ketu opposed Saturn (3 events since 2002), Nifty Midcap 100 averaged +2.75% over the next 5 trading days (base rate +0.27%). Win rate 66.7%. That is +2.49 pp above the unconditional baseline. Not statistically significant (p=0.3334, q=0.512 after Benjamini-Hochberg correction).
* When Ketu opposed Saturn (3 events since 2002), Nifty Midcap 150 averaged +2.19% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +1.93 pp above the unconditional baseline. Not statistically significant (p=0.2122, q=0.3749 after Benjamini-Hochberg correction).
* When Ketu opposed Saturn (3 events since 2002), BSE Sensex averaged +2.08% over the next 5 trading days (base rate +0.25%). Win rate 100.0%. That is +1.83 pp above the unconditional baseline. Not statistically significant (p=0.2759, q=0.453 after Benjamini-Hochberg correction).

* When Ketu formed a square with Saturn (4 events since 2005), Nifty 50 averaged +2.78% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +2.56 pp above the unconditional baseline. Not statistically significant (p=0.3636, q=0.545 after Benjamini-Hochberg correction).
* When Ketu formed a square with Saturn (4 events since 2005), Nifty Bank averaged +3.27% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is +2.97 pp above the unconditional baseline. Not statistically significant (p=0.3531, q=0.533 after Benjamini-Hochberg correction).
* When Ketu formed a square with Saturn (4 events since 2005), Nifty Midcap 100 averaged -0.15% over the next 5 trading days (base rate +0.27%). Win rate 25.0%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.655, q=0.7938 after Benjamini-Hochberg correction).
* When Ketu formed a square with Saturn (4 events since 2005), Nifty Midcap 150 averaged +0.82% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +0.56 pp above the unconditional baseline. Not statistically significant (p=0.4426, q=0.6228 after Benjamini-Hochberg correction).
* When Ketu formed a square with Saturn (4 events since 2005), BSE Sensex averaged +1.39% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is +1.14 pp above the unconditional baseline. Not statistically significant (p=0.4141, q=0.5961 after Benjamini-Hochberg correction).

* When Ketu formed a trine with Saturn (5 events since 2000), Nifty 50 averaged +5.09% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +4.87 pp above the unconditional baseline. Not statistically significant (p=0.07421, q=0.1732 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Saturn (5 events since 2000), Nifty Bank averaged +4.86% over the next 5 trading days (base rate +0.30%). Win rate 80.0%. That is +4.56 pp above the unconditional baseline. Not statistically significant (p=0.156, q=0.303 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Saturn (5 events since 2000), Nifty Midcap 100 averaged +0.99% over the next 5 trading days (base rate +0.27%). Win rate 60.0%. That is +0.73 pp above the unconditional baseline. Not statistically significant (p=0.3876, q=0.5702 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Saturn (5 events since 2000), Nifty Midcap 150 averaged +1.79% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +1.52 pp above the unconditional baseline. Not statistically significant (p=0.1213, q=0.2507 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Saturn (5 events since 2000), BSE Sensex averaged +4.26% over the next 5 trading days (base rate +0.25%). Win rate 100.0%. That is +4.01 pp above the unconditional baseline. Not statistically significant (p=0.186, q=0.3428 after Benjamini-Hochberg correction).

* When Ketu opposed Sun (28 events since 2000), Nifty 50 averaged +2.88% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +2.66 pp above the unconditional baseline. Statistically significant at p=0.008166 and after Benjamini-Hochberg correction (q=0.03186).
* When Ketu opposed Sun (28 events since 2000), Nifty Bank averaged +2.76% over the next 5 trading days (base rate +0.30%). Win rate 60.7%. That is +2.46 pp above the unconditional baseline. Nominally significant at p=0.04552, but it does not survive Benjamini-Hochberg correction (q=0.1196).
* When Ketu opposed Sun (28 events since 2000), Nifty Midcap 100 averaged +0.44% over the next 5 trading days (base rate +0.27%). Win rate 42.9%. That is +0.18 pp above the unconditional baseline. Not statistically significant (p=0.7556, q=0.8594 after Benjamini-Hochberg correction).
* When Ketu opposed Sun (28 events since 2000), Nifty Midcap 150 averaged +0.66% over the next 5 trading days (base rate +0.26%). Win rate 71.4%. That is +0.39 pp above the unconditional baseline. Not statistically significant (p=0.4065, q=0.5885 after Benjamini-Hochberg correction).
* When Ketu opposed Sun (28 events since 2000), BSE Sensex averaged -0.31% over the next 5 trading days (base rate +0.25%). Win rate 53.6%. That is -0.56 pp below the unconditional baseline. Not statistically significant (p=0.3967, q=0.5802 after Benjamini-Hochberg correction).

* When Ketu formed a square with Sun (56 events since 2000), Nifty 50 averaged +3.15% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +2.93 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004136).
* When Ketu formed a square with Sun (56 events since 2000), Nifty Bank averaged +3.21% over the next 5 trading days (base rate +0.30%). Win rate 67.9%. That is +2.91 pp above the unconditional baseline. Statistically significant at p=0.0005297 and after Benjamini-Hochberg correction (q=0.003592).
* When Ketu formed a square with Sun (56 events since 2000), Nifty Midcap 100 averaged +1.19% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.92 pp above the unconditional baseline. Nominally significant at p=0.01438, but it does not survive Benjamini-Hochberg correction (q=0.05035).
* When Ketu formed a square with Sun (56 events since 2000), Nifty Midcap 150 averaged +0.81% over the next 5 trading days (base rate +0.26%). Win rate 66.1%. That is +0.55 pp above the unconditional baseline. Not statistically significant (p=0.118, q=0.2457 after Benjamini-Hochberg correction).
* When Ketu formed a square with Sun (56 events since 2000), BSE Sensex averaged +0.53% over the next 5 trading days (base rate +0.25%). Win rate 58.9%. That is +0.28 pp above the unconditional baseline. Not statistically significant (p=0.4501, q=0.6298 after Benjamini-Hochberg correction).

* When Ketu formed a trine with Sun (56 events since 2000), Nifty 50 averaged +3.53% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +3.31 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.267e-05).
* When Ketu formed a trine with Sun (56 events since 2000), Nifty Bank averaged +4.23% over the next 5 trading days (base rate +0.30%). Win rate 69.6%. That is +3.93 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.106e-05).
* When Ketu formed a trine with Sun (56 events since 2000), Nifty Midcap 100 averaged +0.27% over the next 5 trading days (base rate +0.27%). Win rate 41.1%. Not statistically significant (p=0.9763, q=0.9901 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Sun (56 events since 2000), Nifty Midcap 150 averaged +1.18% over the next 5 trading days (base rate +0.26%). Win rate 69.6%. That is +0.92 pp above the unconditional baseline. Statistically significant at p=0.007978 and after Benjamini-Hochberg correction (q=0.03143).
* When Ketu formed a trine with Sun (56 events since 2000), BSE Sensex averaged +0.56% over the next 5 trading days (base rate +0.25%). Win rate 60.7%. That is +0.31 pp above the unconditional baseline. Not statistically significant (p=0.4524, q=0.6318 after Benjamini-Hochberg correction).

* When Ketu opposed Venus (30 events since 2000), Nifty 50 averaged +1.57% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is +1.35 pp above the unconditional baseline. Not statistically significant (p=0.1939, q=0.3523 after Benjamini-Hochberg correction).
* When Ketu opposed Venus (30 events since 2000), Nifty Bank averaged +1.92% over the next 5 trading days (base rate +0.30%). Win rate 53.3%. That is +1.62 pp above the unconditional baseline. Not statistically significant (p=0.1861, q=0.3428 after Benjamini-Hochberg correction).
* When Ketu opposed Venus (30 events since 2000), Nifty Midcap 100 averaged -1.23% over the next 5 trading days (base rate +0.27%). Win rate 26.7%. That is -1.49 pp below the unconditional baseline. Nominally significant at p=0.02972, but it does not survive Benjamini-Hochberg correction (q=0.08817).
* When Ketu opposed Venus (30 events since 2000), Nifty Midcap 150 averaged -0.70% over the next 5 trading days (base rate +0.26%). Win rate 50.0%. That is -0.97 pp below the unconditional baseline. Not statistically significant (p=0.06261, q=0.1533 after Benjamini-Hochberg correction).
* When Ketu opposed Venus (30 events since 2000), BSE Sensex averaged -1.48% over the next 5 trading days (base rate +0.25%). Win rate 26.7%. That is -1.73 pp below the unconditional baseline. Statistically significant at p=0.001279 and after Benjamini-Hochberg correction (q=0.007175).

* When Ketu formed a square with Venus (60 events since 2000), Nifty 50 averaged +3.02% over the next 5 trading days (base rate +0.22%). Win rate 70.0%. That is +2.81 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004147).
* When Ketu formed a square with Venus (60 events since 2000), Nifty Bank averaged +3.46% over the next 5 trading days (base rate +0.30%). Win rate 70.0%. That is +3.16 pp above the unconditional baseline. Statistically significant at p=0.000105 and after Benjamini-Hochberg correction (q=0.001021).
* When Ketu formed a square with Venus (60 events since 2000), Nifty Midcap 100 averaged +0.08% over the next 5 trading days (base rate +0.27%). Win rate 35.0%. That is -0.19 pp below the unconditional baseline. Not statistically significant (p=0.6228, q=0.77 after Benjamini-Hochberg correction).
* When Ketu formed a square with Venus (60 events since 2000), Nifty Midcap 150 averaged +0.42% over the next 5 trading days (base rate +0.26%). Win rate 65.0%. That is +0.16 pp above the unconditional baseline. Not statistically significant (p=0.5809, q=0.7388 after Benjamini-Hochberg correction).
* When Ketu formed a square with Venus (60 events since 2000), BSE Sensex averaged +0.07% over the next 5 trading days (base rate +0.25%). Win rate 55.0%. That is -0.19 pp below the unconditional baseline. Not statistically significant (p=0.5919, q=0.7474 after Benjamini-Hochberg correction).

* When Ketu formed a trine with Venus (60 events since 2000), Nifty 50 averaged +2.94% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +2.72 pp above the unconditional baseline. Statistically significant at p=0.0001148 and after Benjamini-Hochberg correction (q=0.001101).
* When Ketu formed a trine with Venus (60 events since 2000), Nifty Bank averaged +3.36% over the next 5 trading days (base rate +0.30%). Win rate 68.3%. That is +3.06 pp above the unconditional baseline. Statistically significant at p=0.0003037 and after Benjamini-Hochberg correction (q=0.002296).
* When Ketu formed a trine with Venus (60 events since 2000), Nifty Midcap 100 averaged +0.22% over the next 5 trading days (base rate +0.27%). Win rate 48.3%. That is -0.04 pp below the unconditional baseline. Not statistically significant (p=0.9327, q=0.9724 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Venus (60 events since 2000), Nifty Midcap 150 averaged +0.81% over the next 5 trading days (base rate +0.26%). Win rate 70.0%. That is +0.54 pp above the unconditional baseline. Not statistically significant (p=0.1746, q=0.3283 after Benjamini-Hochberg correction).
* When Ketu formed a trine with Venus (60 events since 2000), BSE Sensex averaged +0.68% over the next 5 trading days (base rate +0.25%). Win rate 63.3%. That is +0.43 pp above the unconditional baseline. Not statistically significant (p=0.3397, q=0.5205 after Benjamini-Hochberg correction).

* When Mars opposed Mercury (12 events since 2001), Nifty 50 averaged +3.31% over the next 5 trading days (base rate +0.22%). Win rate 83.3%. That is +3.09 pp above the unconditional baseline. Nominally significant at p=0.03193, but it does not survive Benjamini-Hochberg correction (q=0.09283).
* When Mars opposed Mercury (12 events since 2001), Nifty Bank averaged +4.13% over the next 5 trading days (base rate +0.30%). Win rate 83.3%. That is +3.83 pp above the unconditional baseline. Nominally significant at p=0.02461, but it does not survive Benjamini-Hochberg correction (q=0.07685).
* When Mars opposed Mercury (12 events since 2001), Nifty Midcap 100 averaged +0.31% over the next 5 trading days (base rate +0.27%). Win rate 41.7%. That is +0.05 pp above the unconditional baseline. Not statistically significant (p=0.949, q=0.9798 after Benjamini-Hochberg correction).
* When Mars opposed Mercury (12 events since 2001), Nifty Midcap 150 averaged +1.31% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +1.05 pp above the unconditional baseline. Not statistically significant (p=0.09969, q=0.2164 after Benjamini-Hochberg correction).
* When Mars opposed Mercury (12 events since 2001), BSE Sensex averaged +0.83% over the next 5 trading days (base rate +0.25%). Win rate 58.3%. That is +0.58 pp above the unconditional baseline. Not statistically significant (p=0.5494, q=0.7161 after Benjamini-Hochberg correction).

* When Mars formed a square with Mercury (53 events since 2001), Nifty 50 averaged +3.56% over the next 5 trading days (base rate +0.22%). Win rate 66.0%. That is +3.35 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0002641).
* When Mars formed a square with Mercury (53 events since 2001), Nifty Bank averaged +4.09% over the next 5 trading days (base rate +0.30%). Win rate 66.0%. That is +3.79 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000422).
* When Mars formed a square with Mercury (53 events since 2001), Nifty Midcap 100 averaged +0.46% over the next 5 trading days (base rate +0.27%). Win rate 41.5%. That is +0.20 pp above the unconditional baseline. Not statistically significant (p=0.5921, q=0.7474 after Benjamini-Hochberg correction).
* When Mars formed a square with Mercury (53 events since 2001), Nifty Midcap 150 averaged +0.66% over the next 5 trading days (base rate +0.26%). Win rate 64.2%. That is +0.40 pp above the unconditional baseline. Not statistically significant (p=0.2414, q=0.4096 after Benjamini-Hochberg correction).
* When Mars formed a square with Mercury (53 events since 2001), BSE Sensex averaged +0.65% over the next 5 trading days (base rate +0.25%). Win rate 56.6%. That is +0.40 pp above the unconditional baseline. Not statistically significant (p=0.3273, q=0.5054 after Benjamini-Hochberg correction).

* When Mars formed a trine with Mercury (32 events since 2001), Nifty 50 averaged +2.70% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +2.49 pp above the unconditional baseline. Statistically significant at p=0.001686 and after Benjamini-Hochberg correction (q=0.008831).
* When Mars formed a trine with Mercury (32 events since 2001), Nifty Bank averaged +3.37% over the next 5 trading days (base rate +0.30%). Win rate 75.0%. That is +3.07 pp above the unconditional baseline. Statistically significant at p=0.001138 and after Benjamini-Hochberg correction (q=0.006534).
* When Mars formed a trine with Mercury (32 events since 2001), Nifty Midcap 100 averaged +0.89% over the next 5 trading days (base rate +0.27%). Win rate 46.9%. That is +0.63 pp above the unconditional baseline. Not statistically significant (p=0.3172, q=0.4943 after Benjamini-Hochberg correction).
* When Mars formed a trine with Mercury (32 events since 2001), Nifty Midcap 150 averaged +1.23% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +0.96 pp above the unconditional baseline. Nominally significant at p=0.02241, but it does not survive Benjamini-Hochberg correction (q=0.07178).
* When Mars formed a trine with Mercury (32 events since 2001), BSE Sensex averaged +1.07% over the next 5 trading days (base rate +0.25%). Win rate 68.8%. That is +0.81 pp above the unconditional baseline. Not statistically significant (p=0.1148, q=0.2402 after Benjamini-Hochberg correction).

* When Mars opposed Moon (50 events since 2000), Nifty 50 averaged +2.30% over the next 5 trading days (base rate +0.22%). Win rate 68.0%. That is +2.08 pp above the unconditional baseline. Statistically significant at p=0.003902 and after Benjamini-Hochberg correction (q=0.01736).
* When Mars opposed Moon (50 events since 2000), Nifty Bank averaged +2.44% over the next 5 trading days (base rate +0.30%). Win rate 66.0%. That is +2.14 pp above the unconditional baseline. Statistically significant at p=0.01148 and after Benjamini-Hochberg correction (q=0.04268).
* When Mars opposed Moon (50 events since 2000), Nifty Midcap 100 averaged -0.10% over the next 5 trading days (base rate +0.27%). Win rate 40.0%. That is -0.37 pp below the unconditional baseline. Not statistically significant (p=0.4438, q=0.6243 after Benjamini-Hochberg correction).
* When Mars opposed Moon (50 events since 2000), Nifty Midcap 150 averaged +0.34% over the next 5 trading days (base rate +0.26%). Win rate 66.0%. That is +0.08 pp above the unconditional baseline. Not statistically significant (p=0.8275, q=0.9058 after Benjamini-Hochberg correction).
* When Mars opposed Moon (50 events since 2000), BSE Sensex averaged +0.04% over the next 5 trading days (base rate +0.25%). Win rate 60.0%. That is -0.21 pp below the unconditional baseline. Not statistically significant (p=0.6299, q=0.7766 after Benjamini-Hochberg correction).

* When Mars formed a square with Moon (110 events since 2000), Nifty 50 averaged +2.77% over the next 5 trading days (base rate +0.22%). Win rate 70.0%. That is +2.55 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=9.08e-07).
* When Mars formed a square with Moon (110 events since 2000), Nifty Bank averaged +3.07% over the next 5 trading days (base rate +0.30%). Win rate 70.0%. That is +2.77 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.626e-06).
* When Mars formed a square with Moon (110 events since 2000), Nifty Midcap 100 averaged +0.45% over the next 5 trading days (base rate +0.27%). Win rate 47.3%. That is +0.18 pp above the unconditional baseline. Not statistically significant (p=0.5463, q=0.7143 after Benjamini-Hochberg correction).
* When Mars formed a square with Moon (110 events since 2000), Nifty Midcap 150 averaged +0.66% over the next 5 trading days (base rate +0.26%). Win rate 65.5%. That is +0.39 pp above the unconditional baseline. Not statistically significant (p=0.06758, q=0.1613 after Benjamini-Hochberg correction).
* When Mars formed a square with Moon (110 events since 2000), BSE Sensex averaged +0.35% over the next 5 trading days (base rate +0.25%). Win rate 56.4%. That is +0.09 pp above the unconditional baseline. Not statistically significant (p=0.7132, q=0.8334 after Benjamini-Hochberg correction).

* When Mars formed a trine with Moon (100 events since 2000), Nifty 50 averaged +2.13% over the next 5 trading days (base rate +0.22%). Win rate 64.0%. That is +1.92 pp above the unconditional baseline. Statistically significant at p=0.0006546 and after Benjamini-Hochberg correction (q=0.00421).
* When Mars formed a trine with Moon (100 events since 2000), Nifty Bank averaged +2.71% over the next 5 trading days (base rate +0.30%). Win rate 66.0%. That is +2.41 pp above the unconditional baseline. Statistically significant at p=0.000136 and after Benjamini-Hochberg correction (q=0.00125).
* When Mars formed a trine with Moon (100 events since 2000), Nifty Midcap 100 averaged -0.58% over the next 5 trading days (base rate +0.27%). Win rate 39.0%. That is -0.85 pp below the unconditional baseline. Nominally significant at p=0.01826, but it does not survive Benjamini-Hochberg correction (q=0.06196).
* When Mars formed a trine with Moon (100 events since 2000), Nifty Midcap 150 averaged +0.04% over the next 5 trading days (base rate +0.26%). Win rate 61.0%. That is -0.22 pp below the unconditional baseline. Not statistically significant (p=0.496, q=0.6734 after Benjamini-Hochberg correction).
* When Mars formed a trine with Moon (100 events since 2000), BSE Sensex averaged -0.29% over the next 5 trading days (base rate +0.25%). Win rate 54.0%. That is -0.54 pp below the unconditional baseline. Not statistically significant (p=0.1212, q=0.2507 after Benjamini-Hochberg correction).

* When Mars opposed Rahu (17 events since 2001), Nifty 50 averaged +1.48% over the next 5 trading days (base rate +0.22%). Win rate 58.8%. That is +1.26 pp above the unconditional baseline. Not statistically significant (p=0.379, q=0.5608 after Benjamini-Hochberg correction).
* When Mars opposed Rahu (17 events since 2001), Nifty Bank averaged +1.61% over the next 5 trading days (base rate +0.30%). Win rate 58.8%. That is +1.31 pp above the unconditional baseline. Not statistically significant (p=0.4647, q=0.6421 after Benjamini-Hochberg correction).
* When Mars opposed Rahu (17 events since 2001), Nifty Midcap 100 averaged -0.65% over the next 5 trading days (base rate +0.27%). Win rate 29.4%. That is -0.92 pp below the unconditional baseline. Not statistically significant (p=0.2189, q=0.3844 after Benjamini-Hochberg correction).
* When Mars opposed Rahu (17 events since 2001), Nifty Midcap 150 averaged -0.72% over the next 5 trading days (base rate +0.26%). Win rate 52.9%. That is -0.98 pp below the unconditional baseline. Not statistically significant (p=0.2784, q=0.4549 after Benjamini-Hochberg correction).
* When Mars opposed Rahu (17 events since 2001), BSE Sensex averaged -1.39% over the next 5 trading days (base rate +0.25%). Win rate 41.2%. That is -1.64 pp below the unconditional baseline. Not statistically significant (p=0.08399, q=0.1894 after Benjamini-Hochberg correction).

* When Mars formed a square with Rahu (34 events since 2000), Nifty 50 averaged +3.68% over the next 5 trading days (base rate +0.22%). Win rate 79.4%. That is +3.46 pp above the unconditional baseline. Statistically significant at p=0.000583 and after Benjamini-Hochberg correction (q=0.003856).
* When Mars formed a square with Rahu (34 events since 2000), Nifty Bank averaged +4.12% over the next 5 trading days (base rate +0.30%). Win rate 70.6%. That is +3.82 pp above the unconditional baseline. Statistically significant at p=0.00197 and after Benjamini-Hochberg correction (q=0.009983).
* When Mars formed a square with Rahu (34 events since 2000), Nifty Midcap 100 averaged +0.75% over the next 5 trading days (base rate +0.27%). Win rate 44.1%. That is +0.48 pp above the unconditional baseline. Not statistically significant (p=0.3938, q=0.5773 after Benjamini-Hochberg correction).
* When Mars formed a square with Rahu (34 events since 2000), Nifty Midcap 150 averaged +1.15% over the next 5 trading days (base rate +0.26%). Win rate 73.5%. That is +0.89 pp above the unconditional baseline. Not statistically significant (p=0.1632, q=0.3146 after Benjamini-Hochberg correction).
* When Mars formed a square with Rahu (34 events since 2000), BSE Sensex averaged +0.91% over the next 5 trading days (base rate +0.25%). Win rate 58.8%. That is +0.66 pp above the unconditional baseline. Not statistically significant (p=0.3331, q=0.512 after Benjamini-Hochberg correction).

* When Mars formed a trine with Rahu (36 events since 2000), Nifty 50 averaged +3.25% over the next 5 trading days (base rate +0.22%). Win rate 72.2%. That is +3.04 pp above the unconditional baseline. Statistically significant at p=0.0005087 and after Benjamini-Hochberg correction (q=0.003504).
* When Mars formed a trine with Rahu (36 events since 2000), Nifty Bank averaged +3.53% over the next 5 trading days (base rate +0.30%). Win rate 75.0%. That is +3.23 pp above the unconditional baseline. Statistically significant at p=0.002086 and after Benjamini-Hochberg correction (q=0.01039).
* When Mars formed a trine with Rahu (36 events since 2000), Nifty Midcap 100 averaged +0.46% over the next 5 trading days (base rate +0.27%). Win rate 41.7%. That is +0.19 pp above the unconditional baseline. Not statistically significant (p=0.7953, q=0.8851 after Benjamini-Hochberg correction).
* When Mars formed a trine with Rahu (36 events since 2000), Nifty Midcap 150 averaged +0.83% over the next 5 trading days (base rate +0.26%). Win rate 69.4%. That is +0.57 pp above the unconditional baseline. Not statistically significant (p=0.3131, q=0.4908 after Benjamini-Hochberg correction).
* When Mars formed a trine with Rahu (36 events since 2000), BSE Sensex averaged +0.71% over the next 5 trading days (base rate +0.25%). Win rate 66.7%. That is +0.46 pp above the unconditional baseline. Not statistically significant (p=0.417, q=0.5988 after Benjamini-Hochberg correction).

* When Mars opposed Saturn (13 events since 2001), Nifty 50 averaged +3.71% over the next 5 trading days (base rate +0.22%). Win rate 84.6%. That is +3.50 pp above the unconditional baseline. Statistically significant at p=0.01398 and after Benjamini-Hochberg correction (q=0.04946).
* When Mars opposed Saturn (13 events since 2001), Nifty Bank averaged +4.54% over the next 5 trading days (base rate +0.30%). Win rate 84.6%. That is +4.24 pp above the unconditional baseline. Statistically significant at p=0.01159 and after Benjamini-Hochberg correction (q=0.04282).
* When Mars opposed Saturn (13 events since 2001), Nifty Midcap 100 averaged +0.40% over the next 5 trading days (base rate +0.27%). Win rate 38.5%. That is +0.13 pp above the unconditional baseline. Not statistically significant (p=0.8407, q=0.914 after Benjamini-Hochberg correction).
* When Mars opposed Saturn (13 events since 2001), Nifty Midcap 150 averaged +1.05% over the next 5 trading days (base rate +0.26%). Win rate 76.9%. That is +0.79 pp above the unconditional baseline. Not statistically significant (p=0.07637, q=0.1767 after Benjamini-Hochberg correction).
* When Mars opposed Saturn (13 events since 2001), BSE Sensex averaged +0.52% over the next 5 trading days (base rate +0.25%). Win rate 61.5%. That is +0.27 pp above the unconditional baseline. Not statistically significant (p=0.5883, q=0.7459 after Benjamini-Hochberg correction).

* When Mars formed a square with Saturn (31 events since 2000), Nifty 50 averaged +3.87% over the next 5 trading days (base rate +0.22%). Win rate 77.4%. That is +3.65 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0009508).
* When Mars formed a square with Saturn (31 events since 2000), Nifty Bank averaged +4.55% over the next 5 trading days (base rate +0.30%). Win rate 77.4%. That is +4.25 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0006159).
* When Mars formed a square with Saturn (31 events since 2000), Nifty Midcap 100 averaged +0.48% over the next 5 trading days (base rate +0.27%). Win rate 41.9%. That is +0.21 pp above the unconditional baseline. Not statistically significant (p=0.6624, q=0.7996 after Benjamini-Hochberg correction).
* When Mars formed a square with Saturn (31 events since 2000), Nifty Midcap 150 averaged +1.38% over the next 5 trading days (base rate +0.26%). Win rate 77.4%. That is +1.11 pp above the unconditional baseline. Statistically significant at p=0.003658 and after Benjamini-Hochberg correction (q=0.01657).
* When Mars formed a square with Saturn (31 events since 2000), BSE Sensex averaged +1.01% over the next 5 trading days (base rate +0.25%). Win rate 67.7%. That is +0.76 pp above the unconditional baseline. Not statistically significant (p=0.08125, q=0.185 after Benjamini-Hochberg correction).

* When Mars formed a trine with Saturn (33 events since 2000), Nifty 50 averaged +3.07% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +2.86 pp above the unconditional baseline. Statistically significant at p=0.001945 and after Benjamini-Hochberg correction (q=0.009906).
* When Mars formed a trine with Saturn (33 events since 2000), Nifty Bank averaged +3.52% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +3.22 pp above the unconditional baseline. Statistically significant at p=0.00275 and after Benjamini-Hochberg correction (q=0.01306).
* When Mars formed a trine with Saturn (33 events since 2000), Nifty Midcap 100 averaged +0.26% over the next 5 trading days (base rate +0.27%). Win rate 48.5%. That is -0.01 pp below the unconditional baseline. Not statistically significant (p=0.975, q=0.9897 after Benjamini-Hochberg correction).
* When Mars formed a trine with Saturn (33 events since 2000), Nifty Midcap 150 averaged +0.66% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.39 pp above the unconditional baseline. Not statistically significant (p=0.3097, q=0.4871 after Benjamini-Hochberg correction).
* When Mars formed a trine with Saturn (33 events since 2000), BSE Sensex averaged +0.79% over the next 5 trading days (base rate +0.25%). Win rate 63.6%. That is +0.54 pp above the unconditional baseline. Not statistically significant (p=0.1824, q=0.3379 after Benjamini-Hochberg correction).

* When Mars opposed Sun (12 events since 2001), Nifty 50 averaged +2.99% over the next 5 trading days (base rate +0.22%). Win rate 58.3%. That is +2.77 pp above the unconditional baseline. Not statistically significant (p=0.06423, q=0.1558 after Benjamini-Hochberg correction).
* When Mars opposed Sun (12 events since 2001), Nifty Bank averaged +3.65% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +3.35 pp above the unconditional baseline. Not statistically significant (p=0.05464, q=0.1374 after Benjamini-Hochberg correction).
* When Mars opposed Sun (12 events since 2001), Nifty Midcap 100 averaged -0.25% over the next 5 trading days (base rate +0.27%). Win rate 41.7%. That is -0.52 pp below the unconditional baseline. Not statistically significant (p=0.4838, q=0.6622 after Benjamini-Hochberg correction).
* When Mars opposed Sun (12 events since 2001), Nifty Midcap 150 averaged +0.99% over the next 5 trading days (base rate +0.26%). Win rate 58.3%. That is +0.73 pp above the unconditional baseline. Not statistically significant (p=0.2885, q=0.4633 after Benjamini-Hochberg correction).
* When Mars opposed Sun (12 events since 2001), BSE Sensex averaged +0.78% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is +0.53 pp above the unconditional baseline. Not statistically significant (p=0.519, q=0.6924 after Benjamini-Hochberg correction).

* When Mars formed a square with Sun (24 events since 2001), Nifty 50 averaged +2.65% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +2.43 pp above the unconditional baseline. Nominally significant at p=0.02969, but it does not survive Benjamini-Hochberg correction (q=0.08817).
* When Mars formed a square with Sun (24 events since 2001), Nifty Bank averaged +3.02% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +2.72 pp above the unconditional baseline. Nominally significant at p=0.03861, but it does not survive Benjamini-Hochberg correction (q=0.1063).
* When Mars formed a square with Sun (24 events since 2001), Nifty Midcap 100 averaged +0.27% over the next 5 trading days (base rate +0.27%). Win rate 41.7%. Not statistically significant (p=0.9888, q=0.9956 after Benjamini-Hochberg correction).
* When Mars formed a square with Sun (24 events since 2001), Nifty Midcap 150 averaged +0.59% over the next 5 trading days (base rate +0.26%). Win rate 70.8%. That is +0.33 pp above the unconditional baseline. Not statistically significant (p=0.5989, q=0.7519 after Benjamini-Hochberg correction).
* When Mars formed a square with Sun (24 events since 2001), BSE Sensex averaged +0.43% over the next 5 trading days (base rate +0.25%). Win rate 66.7%. That is +0.18 pp above the unconditional baseline. Not statistically significant (p=0.7717, q=0.8717 after Benjamini-Hochberg correction).

* When Mars formed a trine with Sun (24 events since 2001), Nifty 50 averaged +2.98% over the next 5 trading days (base rate +0.22%). Win rate 83.3%. That is +2.76 pp above the unconditional baseline. Statistically significant at p=0.005742 and after Benjamini-Hochberg correction (q=0.02392).
* When Mars formed a trine with Sun (24 events since 2001), Nifty Bank averaged +3.74% over the next 5 trading days (base rate +0.30%). Win rate 83.3%. That is +3.44 pp above the unconditional baseline. Statistically significant at p=0.002525 and after Benjamini-Hochberg correction (q=0.01215).
* When Mars formed a trine with Sun (24 events since 2001), Nifty Midcap 100 averaged +0.01% over the next 5 trading days (base rate +0.27%). Win rate 45.8%. That is -0.25 pp below the unconditional baseline. Not statistically significant (p=0.653, q=0.7932 after Benjamini-Hochberg correction).
* When Mars formed a trine with Sun (24 events since 2001), Nifty Midcap 150 averaged +1.07% over the next 5 trading days (base rate +0.26%). Win rate 83.3%. That is +0.81 pp above the unconditional baseline. Not statistically significant (p=0.0655, q=0.1578 after Benjamini-Hochberg correction).
* When Mars formed a trine with Sun (24 events since 2001), BSE Sensex averaged +1.55% over the next 5 trading days (base rate +0.25%). Win rate 79.2%. That is +1.30 pp above the unconditional baseline. Nominally significant at p=0.03955, but it does not survive Benjamini-Hochberg correction (q=0.1077).

* When Mars opposed Venus (12 events since 2001), Nifty 50 averaged +3.32% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +3.10 pp above the unconditional baseline. Nominally significant at p=0.0305, but it does not survive Benjamini-Hochberg correction (q=0.08979).
* When Mars opposed Venus (12 events since 2001), Nifty Bank averaged +5.39% over the next 5 trading days (base rate +0.30%). Win rate 83.3%. That is +5.09 pp above the unconditional baseline. Statistically significant at p=0.00386 and after Benjamini-Hochberg correction (q=0.01725).
* When Mars opposed Venus (12 events since 2001), Nifty Midcap 100 averaged -0.29% over the next 5 trading days (base rate +0.27%). Win rate 41.7%. That is -0.56 pp below the unconditional baseline. Not statistically significant (p=0.432, q=0.6145 after Benjamini-Hochberg correction).
* When Mars opposed Venus (12 events since 2001), Nifty Midcap 150 averaged +1.44% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +1.17 pp above the unconditional baseline. Not statistically significant (p=0.08138, q=0.185 after Benjamini-Hochberg correction).
* When Mars opposed Venus (12 events since 2001), BSE Sensex averaged +0.60% over the next 5 trading days (base rate +0.25%). Win rate 58.3%. That is +0.35 pp above the unconditional baseline. Not statistically significant (p=0.6471, q=0.7906 after Benjamini-Hochberg correction).

* When Mars formed a square with Venus (36 events since 2000), Nifty 50 averaged +2.68% over the next 5 trading days (base rate +0.22%). Win rate 72.2%. That is +2.46 pp above the unconditional baseline. Statistically significant at p=0.001423 and after Benjamini-Hochberg correction (q=0.007773).
* When Mars formed a square with Venus (36 events since 2000), Nifty Bank averaged +3.17% over the next 5 trading days (base rate +0.30%). Win rate 72.2%. That is +2.87 pp above the unconditional baseline. Statistically significant at p=0.002552 and after Benjamini-Hochberg correction (q=0.01225).
* When Mars formed a square with Venus (36 events since 2000), Nifty Midcap 100 averaged +0.31% over the next 5 trading days (base rate +0.27%). Win rate 36.1%. That is +0.04 pp above the unconditional baseline. Not statistically significant (p=0.9374, q=0.9749 after Benjamini-Hochberg correction).
* When Mars formed a square with Venus (36 events since 2000), Nifty Midcap 150 averaged +0.55% over the next 5 trading days (base rate +0.26%). Win rate 63.9%. That is +0.29 pp above the unconditional baseline. Not statistically significant (p=0.4484, q=0.6286 after Benjamini-Hochberg correction).
* When Mars formed a square with Venus (36 events since 2000), BSE Sensex averaged +0.45% over the next 5 trading days (base rate +0.25%). Win rate 58.3%. That is +0.20 pp above the unconditional baseline. Not statistically significant (p=0.6177, q=0.765 after Benjamini-Hochberg correction).

* When Mars formed a trine with Venus (32 events since 2001), Nifty 50 averaged +3.61% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +3.40 pp above the unconditional baseline. Statistically significant at p=0.0004917 and after Benjamini-Hochberg correction (q=0.003408).
* When Mars formed a trine with Venus (32 events since 2001), Nifty Bank averaged +4.24% over the next 5 trading days (base rate +0.30%). Win rate 71.9%. That is +3.94 pp above the unconditional baseline. Statistically significant at p=0.0005294 and after Benjamini-Hochberg correction (q=0.003592).
* When Mars formed a trine with Venus (32 events since 2001), Nifty Midcap 100 averaged +1.03% over the next 5 trading days (base rate +0.27%). Win rate 56.2%. That is +0.77 pp above the unconditional baseline. Not statistically significant (p=0.1333, q=0.2699 after Benjamini-Hochberg correction).
* When Mars formed a trine with Venus (32 events since 2001), Nifty Midcap 150 averaged +1.15% over the next 5 trading days (base rate +0.26%). Win rate 71.9%. That is +0.88 pp above the unconditional baseline. Not statistically significant (p=0.07168, q=0.1691 after Benjamini-Hochberg correction).
* When Mars formed a trine with Venus (32 events since 2001), BSE Sensex averaged +1.21% over the next 5 trading days (base rate +0.25%). Win rate 65.6%. That is +0.96 pp above the unconditional baseline. Not statistically significant (p=0.08685, q=0.1943 after Benjamini-Hochberg correction).

* When Mercury opposed Moon (62 events since 2000), Nifty 50 averaged +3.15% over the next 5 trading days (base rate +0.22%). Win rate 72.6%. That is +2.93 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0001723).
* When Mercury opposed Moon (62 events since 2000), Nifty Bank averaged +3.42% over the next 5 trading days (base rate +0.30%). Win rate 74.2%. That is +3.12 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0007568).
* When Mercury opposed Moon (62 events since 2000), Nifty Midcap 100 averaged +0.18% over the next 5 trading days (base rate +0.27%). Win rate 41.9%. That is -0.08 pp below the unconditional baseline. Not statistically significant (p=0.7824, q=0.8763 after Benjamini-Hochberg correction).
* When Mercury opposed Moon (62 events since 2000), Nifty Midcap 150 averaged +0.70% over the next 5 trading days (base rate +0.26%). Win rate 71.0%. That is +0.44 pp above the unconditional baseline. Not statistically significant (p=0.1907, q=0.3485 after Benjamini-Hochberg correction).
* When Mercury opposed Moon (62 events since 2000), BSE Sensex averaged +0.25% over the next 5 trading days (base rate +0.25%). Win rate 61.3%. Not statistically significant (p=0.9943, q=0.9976 after Benjamini-Hochberg correction).

* When Mercury formed a square with Moon (126 events since 2000), Nifty 50 averaged +2.90% over the next 5 trading days (base rate +0.22%). Win rate 68.3%. That is +2.68 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.036e-06).
* When Mercury formed a square with Moon (126 events since 2000), Nifty Bank averaged +3.05% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +2.75 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=9.877e-05).
* When Mercury formed a square with Moon (126 events since 2000), Nifty Midcap 100 averaged +0.05% over the next 5 trading days (base rate +0.27%). Win rate 42.1%. That is -0.21 pp below the unconditional baseline. Not statistically significant (p=0.4592, q=0.6373 after Benjamini-Hochberg correction).
* When Mercury formed a square with Moon (126 events since 2000), Nifty Midcap 150 averaged +0.47% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.21 pp above the unconditional baseline. Not statistically significant (p=0.4374, q=0.618 after Benjamini-Hochberg correction).
* When Mercury formed a square with Moon (126 events since 2000), BSE Sensex averaged +0.10% over the next 5 trading days (base rate +0.25%). Win rate 51.6%. That is -0.15 pp below the unconditional baseline. Not statistically significant (p=0.5965, q=0.7511 after Benjamini-Hochberg correction).

* When Mercury formed a trine with Moon (94 events since 2000), Nifty 50 averaged +3.36% over the next 5 trading days (base rate +0.22%). Win rate 70.2%. That is +3.14 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.306e-06).
* When Mercury formed a trine with Moon (94 events since 2000), Nifty Bank averaged +3.73% over the next 5 trading days (base rate +0.30%). Win rate 71.3%. That is +3.43 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.005e-05).
* When Mercury formed a trine with Moon (94 events since 2000), Nifty Midcap 100 averaged -0.35% over the next 5 trading days (base rate +0.27%). Win rate 31.9%. That is -0.62 pp below the unconditional baseline. Nominally significant at p=0.03858, but it does not survive Benjamini-Hochberg correction (q=0.1063).
* When Mercury formed a trine with Moon (94 events since 2000), Nifty Midcap 150 averaged +0.68% over the next 5 trading days (base rate +0.26%). Win rate 70.2%. That is +0.42 pp above the unconditional baseline. Not statistically significant (p=0.07959, q=0.1822 after Benjamini-Hochberg correction).
* When Mercury formed a trine with Moon (94 events since 2000), BSE Sensex averaged -0.29% over the next 5 trading days (base rate +0.25%). Win rate 53.2%. That is -0.54 pp below the unconditional baseline. Not statistically significant (p=0.1648, q=0.3163 after Benjamini-Hochberg correction).

* When Mercury opposed Rahu (28 events since 2000), Nifty 50 averaged +3.08% over the next 5 trading days (base rate +0.22%). Win rate 67.9%. That is +2.86 pp above the unconditional baseline. Statistically significant at p=0.005301 and after Benjamini-Hochberg correction (q=0.02236).
* When Mercury opposed Rahu (28 events since 2000), Nifty Bank averaged +3.55% over the next 5 trading days (base rate +0.30%). Win rate 64.3%. That is +3.25 pp above the unconditional baseline. Statistically significant at p=0.008123 and after Benjamini-Hochberg correction (q=0.03179).
* When Mercury opposed Rahu (28 events since 2000), Nifty Midcap 100 averaged +0.51% over the next 5 trading days (base rate +0.27%). Win rate 46.4%. That is +0.24 pp above the unconditional baseline. Not statistically significant (p=0.4366, q=0.6173 after Benjamini-Hochberg correction).
* When Mercury opposed Rahu (28 events since 2000), Nifty Midcap 150 averaged +0.72% over the next 5 trading days (base rate +0.26%). Win rate 67.9%. That is +0.45 pp above the unconditional baseline. Not statistically significant (p=0.3317, q=0.511 after Benjamini-Hochberg correction).
* When Mercury opposed Rahu (28 events since 2000), BSE Sensex averaged +0.38% over the next 5 trading days (base rate +0.25%). Win rate 53.6%. That is +0.13 pp above the unconditional baseline. Not statistically significant (p=0.7969, q=0.8854 after Benjamini-Hochberg correction).

* When Mercury formed a square with Rahu (56 events since 2000), Nifty 50 averaged +2.61% over the next 5 trading days (base rate +0.22%). Win rate 66.1%. That is +2.40 pp above the unconditional baseline. Statistically significant at p=0.0008148 and after Benjamini-Hochberg correction (q=0.005034).
* When Mercury formed a square with Rahu (56 events since 2000), Nifty Bank averaged +2.71% over the next 5 trading days (base rate +0.30%). Win rate 67.9%. That is +2.41 pp above the unconditional baseline. Statistically significant at p=0.004149 and after Benjamini-Hochberg correction (q=0.01826).
* When Mercury formed a square with Rahu (56 events since 2000), Nifty Midcap 100 averaged +0.50% over the next 5 trading days (base rate +0.27%). Win rate 42.9%. That is +0.24 pp above the unconditional baseline. Not statistically significant (p=0.5283, q=0.6998 after Benjamini-Hochberg correction).
* When Mercury formed a square with Rahu (56 events since 2000), Nifty Midcap 150 averaged +0.05% over the next 5 trading days (base rate +0.26%). Win rate 62.5%. That is -0.22 pp below the unconditional baseline. Not statistically significant (p=0.5599, q=0.7248 after Benjamini-Hochberg correction).
* When Mercury formed a square with Rahu (56 events since 2000), BSE Sensex averaged -0.17% over the next 5 trading days (base rate +0.25%). Win rate 46.4%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.3436, q=0.5236 after Benjamini-Hochberg correction).

* When Mercury formed a trine with Rahu (114 events since 2000), Nifty 50 averaged +3.01% over the next 5 trading days (base rate +0.22%). Win rate 71.1%. That is +2.80 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=9.034e-07).
* When Mercury formed a trine with Rahu (114 events since 2000), Nifty Bank averaged +3.60% over the next 5 trading days (base rate +0.30%). Win rate 71.1%. That is +3.30 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.262e-06).
* When Mercury formed a trine with Rahu (114 events since 2000), Nifty Midcap 100 averaged +0.09% over the next 5 trading days (base rate +0.27%). Win rate 40.4%. That is -0.18 pp below the unconditional baseline. Not statistically significant (p=0.4761, q=0.6536 after Benjamini-Hochberg correction).
* When Mercury formed a trine with Rahu (114 events since 2000), Nifty Midcap 150 averaged +0.82% over the next 5 trading days (base rate +0.26%). Win rate 65.8%. That is +0.56 pp above the unconditional baseline. Not statistically significant (p=0.06744, q=0.1611 after Benjamini-Hochberg correction).
* When Mercury formed a trine with Rahu (114 events since 2000), BSE Sensex averaged +0.55% over the next 5 trading days (base rate +0.25%). Win rate 62.3%. That is +0.30 pp above the unconditional baseline. Not statistically significant (p=0.3697, q=0.5519 after Benjamini-Hochberg correction).

* When Mercury opposed Saturn (28 events since 2000), Nifty 50 averaged +3.95% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +3.73 pp above the unconditional baseline. Statistically significant at p=0.0004764 and after Benjamini-Hochberg correction (q=0.003327).
* When Mercury opposed Saturn (28 events since 2000), Nifty Bank averaged +4.66% over the next 5 trading days (base rate +0.30%). Win rate 71.4%. That is +4.36 pp above the unconditional baseline. Statistically significant at p=0.0006759 and after Benjamini-Hochberg correction (q=0.004311).
* When Mercury opposed Saturn (28 events since 2000), Nifty Midcap 100 averaged +0.32% over the next 5 trading days (base rate +0.27%). Win rate 25.0%. That is +0.06 pp above the unconditional baseline. Not statistically significant (p=0.9308, q=0.9709 after Benjamini-Hochberg correction).
* When Mercury opposed Saturn (28 events since 2000), Nifty Midcap 150 averaged +1.18% over the next 5 trading days (base rate +0.26%). Win rate 67.9%. That is +0.92 pp above the unconditional baseline. Not statistically significant (p=0.09953, q=0.2162 after Benjamini-Hochberg correction).
* When Mercury opposed Saturn (28 events since 2000), BSE Sensex averaged +1.78% over the next 5 trading days (base rate +0.25%). Win rate 71.4%. That is +1.53 pp above the unconditional baseline. Nominally significant at p=0.0235, but it does not survive Benjamini-Hochberg correction (q=0.07425).

* When Mercury formed a square with Saturn (66 events since 2000), Nifty 50 averaged +3.07% over the next 5 trading days (base rate +0.22%). Win rate 69.7%. That is +2.85 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0001994).
* When Mercury formed a square with Saturn (66 events since 2000), Nifty Bank averaged +3.41% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +3.11 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004806).
* When Mercury formed a square with Saturn (66 events since 2000), Nifty Midcap 100 averaged +0.01% over the next 5 trading days (base rate +0.27%). Win rate 31.8%. That is -0.26 pp below the unconditional baseline. Not statistically significant (p=0.34, q=0.5208 after Benjamini-Hochberg correction).
* When Mercury formed a square with Saturn (66 events since 2000), Nifty Midcap 150 averaged +0.38% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.12 pp above the unconditional baseline. Not statistically significant (p=0.694, q=0.8191 after Benjamini-Hochberg correction).
* When Mercury formed a square with Saturn (66 events since 2000), BSE Sensex averaged -0.07% over the next 5 trading days (base rate +0.25%). Win rate 54.5%. That is -0.32 pp below the unconditional baseline. Not statistically significant (p=0.2983, q=0.4749 after Benjamini-Hochberg correction).

* When Mercury formed a trine with Saturn (63 events since 2000), Nifty 50 averaged +3.57% over the next 5 trading days (base rate +0.22%). Win rate 77.8%. That is +3.35 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.433e-06).
* When Mercury formed a trine with Saturn (63 events since 2000), Nifty Bank averaged +4.12% over the next 5 trading days (base rate +0.30%). Win rate 76.2%. That is +3.82 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.06e-05).
* When Mercury formed a trine with Saturn (63 events since 2000), Nifty Midcap 100 averaged +0.37% over the next 5 trading days (base rate +0.27%). Win rate 38.1%. That is +0.11 pp above the unconditional baseline. Not statistically significant (p=0.7074, q=0.829 after Benjamini-Hochberg correction).
* When Mercury formed a trine with Saturn (63 events since 2000), Nifty Midcap 150 averaged +1.09% over the next 5 trading days (base rate +0.26%). Win rate 74.6%. That is +0.83 pp above the unconditional baseline. Statistically significant at p=0.002136 and after Benjamini-Hochberg correction (q=0.0105).
* When Mercury formed a trine with Saturn (63 events since 2000), BSE Sensex averaged +0.52% over the next 5 trading days (base rate +0.25%). Win rate 63.5%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.4109, q=0.5926 after Benjamini-Hochberg correction).

* When Moon opposed Rahu (57 events since 2000), Nifty 50 averaged +3.30% over the next 5 trading days (base rate +0.22%). Win rate 68.4%. That is +3.08 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0002488).
* When Moon opposed Rahu (57 events since 2000), Nifty Bank averaged +3.73% over the next 5 trading days (base rate +0.30%). Win rate 57.9%. That is +3.43 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004806).
* When Moon opposed Rahu (57 events since 2000), Nifty Midcap 100 averaged +0.13% over the next 5 trading days (base rate +0.27%). Win rate 43.9%. That is -0.14 pp below the unconditional baseline. Not statistically significant (p=0.6922, q=0.8183 after Benjamini-Hochberg correction).
* When Moon opposed Rahu (57 events since 2000), Nifty Midcap 150 averaged +0.41% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.15 pp above the unconditional baseline. Not statistically significant (p=0.6627, q=0.7996 after Benjamini-Hochberg correction).
* When Moon opposed Rahu (57 events since 2000), BSE Sensex averaged +0.51% over the next 5 trading days (base rate +0.25%). Win rate 54.4%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.5676, q=0.7282 after Benjamini-Hochberg correction).

* When Moon formed a square with Rahu (113 events since 2000), Nifty 50 averaged +2.06% over the next 5 trading days (base rate +0.22%). Win rate 60.2%. That is +1.85 pp above the unconditional baseline. Statistically significant at p=0.0002204 and after Benjamini-Hochberg correction (q=0.00177).
* When Moon formed a square with Rahu (113 events since 2000), Nifty Bank averaged +2.33% over the next 5 trading days (base rate +0.30%). Win rate 61.1%. That is +2.03 pp above the unconditional baseline. Statistically significant at p=0.0005221 and after Benjamini-Hochberg correction (q=0.003559).
* When Moon formed a square with Rahu (113 events since 2000), Nifty Midcap 100 averaged -0.14% over the next 5 trading days (base rate +0.27%). Win rate 38.1%. That is -0.41 pp below the unconditional baseline. Not statistically significant (p=0.1726, q=0.3264 after Benjamini-Hochberg correction).
* When Moon formed a square with Rahu (113 events since 2000), Nifty Midcap 150 averaged +0.08% over the next 5 trading days (base rate +0.26%). Win rate 59.3%. That is -0.18 pp below the unconditional baseline. Not statistically significant (p=0.5178, q=0.691 after Benjamini-Hochberg correction).
* When Moon formed a square with Rahu (113 events since 2000), BSE Sensex averaged -0.18% over the next 5 trading days (base rate +0.25%). Win rate 50.4%. That is -0.43 pp below the unconditional baseline. Not statistically significant (p=0.1365, q=0.2741 after Benjamini-Hochberg correction).

* When Moon formed a trine with Rahu (119 events since 2000), Nifty 50 averaged +2.58% over the next 5 trading days (base rate +0.22%). Win rate 67.2%. That is +2.36 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.961e-05).
* When Moon formed a trine with Rahu (119 events since 2000), Nifty Bank averaged +2.94% over the next 5 trading days (base rate +0.30%). Win rate 64.7%. That is +2.64 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=9.852e-05).
* When Moon formed a trine with Rahu (119 events since 2000), Nifty Midcap 100 averaged -0.15% over the next 5 trading days (base rate +0.27%). Win rate 36.1%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.09636, q=0.2109 after Benjamini-Hochberg correction).
* When Moon formed a trine with Rahu (119 events since 2000), Nifty Midcap 150 averaged +0.20% over the next 5 trading days (base rate +0.26%). Win rate 63.0%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.8155, q=0.897 after Benjamini-Hochberg correction).
* When Moon formed a trine with Rahu (119 events since 2000), BSE Sensex averaged +0.19% over the next 5 trading days (base rate +0.25%). Win rate 57.1%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.8387, q=0.9128 after Benjamini-Hochberg correction).

* When Moon opposed Saturn (57 events since 2000), Nifty 50 averaged +3.55% over the next 5 trading days (base rate +0.22%). Win rate 75.4%. That is +3.34 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0002391).
* When Moon opposed Saturn (57 events since 2000), Nifty Bank averaged +4.27% over the next 5 trading days (base rate +0.30%). Win rate 75.4%. That is +3.97 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000241).
* When Moon opposed Saturn (57 events since 2000), Nifty Midcap 100 averaged +0.72% over the next 5 trading days (base rate +0.27%). Win rate 59.6%. That is +0.46 pp above the unconditional baseline. Not statistically significant (p=0.2032, q=0.3645 after Benjamini-Hochberg correction).
* When Moon opposed Saturn (57 events since 2000), Nifty Midcap 150 averaged +1.14% over the next 5 trading days (base rate +0.26%). Win rate 70.2%. That is +0.88 pp above the unconditional baseline. Not statistically significant (p=0.09457, q=0.2084 after Benjamini-Hochberg correction).
* When Moon opposed Saturn (57 events since 2000), BSE Sensex averaged +0.97% over the next 5 trading days (base rate +0.25%). Win rate 66.7%. That is +0.72 pp above the unconditional baseline. Not statistically significant (p=0.1648, q=0.3163 after Benjamini-Hochberg correction).

* When Moon formed a square with Saturn (109 events since 2000), Nifty 50 averaged +2.81% over the next 5 trading days (base rate +0.22%). Win rate 65.1%. That is +2.59 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=4.961e-06).
* When Moon formed a square with Saturn (109 events since 2000), Nifty Bank averaged +3.28% over the next 5 trading days (base rate +0.30%). Win rate 65.1%. That is +2.98 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=5.323e-06).
* When Moon formed a square with Saturn (109 events since 2000), Nifty Midcap 100 averaged -0.08% over the next 5 trading days (base rate +0.27%). Win rate 33.9%. That is -0.35 pp below the unconditional baseline. Not statistically significant (p=0.1432, q=0.2838 after Benjamini-Hochberg correction).
* When Moon formed a square with Saturn (109 events since 2000), Nifty Midcap 150 averaged +0.47% over the next 5 trading days (base rate +0.26%). Win rate 64.2%. That is +0.20 pp above the unconditional baseline. Not statistically significant (p=0.318, q=0.4952 after Benjamini-Hochberg correction).
* When Moon formed a square with Saturn (109 events since 2000), BSE Sensex averaged -0.02% over the next 5 trading days (base rate +0.25%). Win rate 55.0%. That is -0.27 pp below the unconditional baseline. Not statistically significant (p=0.3649, q=0.5465 after Benjamini-Hochberg correction).

* When Moon formed a trine with Saturn (104 events since 2000), Nifty 50 averaged +2.70% over the next 5 trading days (base rate +0.22%). Win rate 69.2%. That is +2.48 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.82e-05).
* When Moon formed a trine with Saturn (104 events since 2000), Nifty Bank averaged +2.88% over the next 5 trading days (base rate +0.30%). Win rate 64.4%. That is +2.58 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0006955).
* When Moon formed a trine with Saturn (104 events since 2000), Nifty Midcap 100 averaged +0.41% over the next 5 trading days (base rate +0.27%). Win rate 48.1%. That is +0.15 pp above the unconditional baseline. Not statistically significant (p=0.6408, q=0.7845 after Benjamini-Hochberg correction).
* When Moon formed a trine with Saturn (104 events since 2000), Nifty Midcap 150 averaged +0.57% over the next 5 trading days (base rate +0.26%). Win rate 71.2%. That is +0.31 pp above the unconditional baseline. Not statistically significant (p=0.3104, q=0.4872 after Benjamini-Hochberg correction).
* When Moon formed a trine with Saturn (104 events since 2000), BSE Sensex averaged +0.25% over the next 5 trading days (base rate +0.25%). Win rate 59.6%. Not statistically significant (p=0.9979, q=0.9993 after Benjamini-Hochberg correction).

* When Moon opposed Sun (63 events since 2000), Nifty 50 averaged +2.94% over the next 5 trading days (base rate +0.22%). Win rate 63.5%. That is +2.73 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0003325).
* When Moon opposed Sun (63 events since 2000), Nifty Bank averaged +3.35% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +3.05 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0007006).
* When Moon opposed Sun (63 events since 2000), Nifty Midcap 100 averaged +0.02% over the next 5 trading days (base rate +0.27%). Win rate 41.3%. That is -0.25 pp below the unconditional baseline. Not statistically significant (p=0.392, q=0.5753 after Benjamini-Hochberg correction).
* When Moon opposed Sun (63 events since 2000), Nifty Midcap 150 averaged +0.68% over the next 5 trading days (base rate +0.26%). Win rate 63.5%. That is +0.41 pp above the unconditional baseline. Not statistically significant (p=0.1333, q=0.2699 after Benjamini-Hochberg correction).
* When Moon opposed Sun (63 events since 2000), BSE Sensex averaged +0.43% over the next 5 trading days (base rate +0.25%). Win rate 52.4%. That is +0.17 pp above the unconditional baseline. Not statistically significant (p=0.5894, q=0.7459 after Benjamini-Hochberg correction).

* When Moon formed a square with Sun (114 events since 2000), Nifty 50 averaged +2.45% over the next 5 trading days (base rate +0.22%). Win rate 64.0%. That is +2.23 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000319).
* When Moon formed a square with Sun (114 events since 2000), Nifty Bank averaged +2.70% over the next 5 trading days (base rate +0.30%). Win rate 63.2%. That is +2.40 pp above the unconditional baseline. Statistically significant at p=0.000137 and after Benjamini-Hochberg correction (q=0.001257).
* When Moon formed a square with Sun (114 events since 2000), Nifty Midcap 100 averaged +0.21% over the next 5 trading days (base rate +0.27%). Win rate 38.6%. That is -0.05 pp below the unconditional baseline. Not statistically significant (p=0.8717, q=0.9339 after Benjamini-Hochberg correction).
* When Moon formed a square with Sun (114 events since 2000), Nifty Midcap 150 averaged +0.36% over the next 5 trading days (base rate +0.26%). Win rate 64.9%. That is +0.10 pp above the unconditional baseline. Not statistically significant (p=0.7591, q=0.8618 after Benjamini-Hochberg correction).
* When Moon formed a square with Sun (114 events since 2000), BSE Sensex averaged +0.29% over the next 5 trading days (base rate +0.25%). Win rate 57.0%. That is +0.04 pp above the unconditional baseline. Not statistically significant (p=0.9157, q=0.9627 after Benjamini-Hochberg correction).

* When Moon formed a trine with Sun (108 events since 2000), Nifty 50 averaged +3.04% over the next 5 trading days (base rate +0.22%). Win rate 64.8%. That is +2.83 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=9.977e-07).
* When Moon formed a trine with Sun (108 events since 2000), Nifty Bank averaged +3.22% over the next 5 trading days (base rate +0.30%). Win rate 64.8%. That is +2.92 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.046e-05).
* When Moon formed a trine with Sun (108 events since 2000), Nifty Midcap 100 averaged +0.20% over the next 5 trading days (base rate +0.27%). Win rate 34.3%. That is -0.07 pp below the unconditional baseline. Not statistically significant (p=0.7899, q=0.8811 after Benjamini-Hochberg correction).
* When Moon formed a trine with Sun (108 events since 2000), Nifty Midcap 150 averaged +0.51% over the next 5 trading days (base rate +0.26%). Win rate 63.0%. That is +0.24 pp above the unconditional baseline. Not statistically significant (p=0.2368, q=0.4046 after Benjamini-Hochberg correction).
* When Moon formed a trine with Sun (108 events since 2000), BSE Sensex averaged -0.13% over the next 5 trading days (base rate +0.25%). Win rate 47.2%. That is -0.38 pp below the unconditional baseline. Not statistically significant (p=0.1253, q=0.2569 after Benjamini-Hochberg correction).

* When Moon opposed Venus (61 events since 2000), Nifty 50 averaged +2.46% over the next 5 trading days (base rate +0.22%). Win rate 67.2%. That is +2.24 pp above the unconditional baseline. Statistically significant at p=0.0007116 and after Benjamini-Hochberg correction (q=0.0045).
* When Moon opposed Venus (61 events since 2000), Nifty Bank averaged +2.90% over the next 5 trading days (base rate +0.30%). Win rate 65.6%. That is +2.60 pp above the unconditional baseline. Statistically significant at p=0.001061 and after Benjamini-Hochberg correction (q=0.006216).
* When Moon opposed Venus (61 events since 2000), Nifty Midcap 100 averaged -0.08% over the next 5 trading days (base rate +0.27%). Win rate 36.1%. That is -0.34 pp below the unconditional baseline. Not statistically significant (p=0.3261, q=0.5038 after Benjamini-Hochberg correction).
* When Moon opposed Venus (61 events since 2000), Nifty Midcap 150 averaged +0.45% over the next 5 trading days (base rate +0.26%). Win rate 65.6%. That is +0.19 pp above the unconditional baseline. Not statistically significant (p=0.6061, q=0.7563 after Benjamini-Hochberg correction).
* When Moon opposed Venus (61 events since 2000), BSE Sensex averaged -0.02% over the next 5 trading days (base rate +0.25%). Win rate 55.7%. That is -0.27 pp below the unconditional baseline. Not statistically significant (p=0.5014, q=0.6771 after Benjamini-Hochberg correction).

* When Moon formed a square with Venus (117 events since 2000), Nifty 50 averaged +2.63% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +2.41 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.046e-05).
* When Moon formed a square with Venus (117 events since 2000), Nifty Bank averaged +3.01% over the next 5 trading days (base rate +0.30%). Win rate 67.5%. That is +2.71 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0001611).
* When Moon formed a square with Venus (117 events since 2000), Nifty Midcap 100 averaged +0.11% over the next 5 trading days (base rate +0.27%). Win rate 42.7%. That is -0.15 pp below the unconditional baseline. Not statistically significant (p=0.5987, q=0.7519 after Benjamini-Hochberg correction).
* When Moon formed a square with Venus (117 events since 2000), Nifty Midcap 150 averaged +0.73% over the next 5 trading days (base rate +0.26%). Win rate 68.4%. That is +0.47 pp above the unconditional baseline. Not statistically significant (p=0.1284, q=0.2622 after Benjamini-Hochberg correction).
* When Moon formed a square with Venus (117 events since 2000), BSE Sensex averaged +0.25% over the next 5 trading days (base rate +0.25%). Win rate 51.3%. Not statistically significant (p=0.9982, q=0.9993 after Benjamini-Hochberg correction).

* When Moon formed a trine with Venus (93 events since 2000), Nifty 50 averaged +2.49% over the next 5 trading days (base rate +0.22%). Win rate 68.8%. That is +2.27 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0006995).
* When Moon formed a trine with Venus (93 events since 2000), Nifty Bank averaged +2.67% over the next 5 trading days (base rate +0.30%). Win rate 65.6%. That is +2.37 pp above the unconditional baseline. Statistically significant at p=0.0003546 and after Benjamini-Hochberg correction (q=0.002623).
* When Moon formed a trine with Venus (93 events since 2000), Nifty Midcap 100 averaged -0.02% over the next 5 trading days (base rate +0.27%). Win rate 40.9%. That is -0.28 pp below the unconditional baseline. Not statistically significant (p=0.3735, q=0.5549 after Benjamini-Hochberg correction).
* When Moon formed a trine with Venus (93 events since 2000), Nifty Midcap 150 averaged +0.48% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.21 pp above the unconditional baseline. Not statistically significant (p=0.524, q=0.6961 after Benjamini-Hochberg correction).
* When Moon formed a trine with Venus (93 events since 2000), BSE Sensex averaged +0.12% over the next 5 trading days (base rate +0.25%). Win rate 55.9%. That is -0.13 pp below the unconditional baseline. Not statistically significant (p=0.7108, q=0.8312 after Benjamini-Hochberg correction).

* When Rahu opposed Saturn (2 events since 2007), Nifty 50 averaged -1.55% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is -1.77 pp below the unconditional baseline. Not statistically significant (p=0.5913, q=0.7471 after Benjamini-Hochberg correction).
* When Rahu opposed Saturn (2 events since 2007), Nifty Bank averaged -1.77% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is -2.07 pp below the unconditional baseline. Not statistically significant (p=0.7336, q=0.8454 after Benjamini-Hochberg correction).
* When Rahu opposed Saturn (2 events since 2007), Nifty Midcap 100 averaged -1.12% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is -1.39 pp below the unconditional baseline. Not statistically significant (p=0.5147, q=0.6878 after Benjamini-Hochberg correction).
* When Rahu opposed Saturn (2 events since 2007), Nifty Midcap 150 averaged -1.79% over the next 5 trading days (base rate +0.26%). Win rate 50.0%. That is -2.06 pp below the unconditional baseline. Not statistically significant (p=0.5966, q=0.7511 after Benjamini-Hochberg correction).
* When Rahu opposed Saturn (2 events since 2007), BSE Sensex averaged -1.91% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -2.16 pp below the unconditional baseline. Not statistically significant (p=0.576, q=0.7342 after Benjamini-Hochberg correction).

* When Rahu formed a square with Saturn (4 events since 2005), Nifty 50 averaged +2.78% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +2.56 pp above the unconditional baseline. Not statistically significant (p=0.3636, q=0.545 after Benjamini-Hochberg correction).
* When Rahu formed a square with Saturn (4 events since 2005), Nifty Bank averaged +3.27% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is +2.97 pp above the unconditional baseline. Not statistically significant (p=0.3531, q=0.533 after Benjamini-Hochberg correction).
* When Rahu formed a square with Saturn (4 events since 2005), Nifty Midcap 100 averaged -0.15% over the next 5 trading days (base rate +0.27%). Win rate 25.0%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.655, q=0.7938 after Benjamini-Hochberg correction).
* When Rahu formed a square with Saturn (4 events since 2005), Nifty Midcap 150 averaged +0.82% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +0.56 pp above the unconditional baseline. Not statistically significant (p=0.4426, q=0.6228 after Benjamini-Hochberg correction).
* When Rahu formed a square with Saturn (4 events since 2005), BSE Sensex averaged +1.39% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is +1.14 pp above the unconditional baseline. Not statistically significant (p=0.4141, q=0.5961 after Benjamini-Hochberg correction).

* When Rahu formed a trine with Saturn (4 events since 2006), Nifty 50 averaged +2.40% over the next 5 trading days (base rate +0.22%). Win rate 75.0%. That is +2.18 pp above the unconditional baseline. Not statistically significant (p=0.4487, q=0.6288 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Saturn (4 events since 2006), Nifty Bank averaged +2.85% over the next 5 trading days (base rate +0.30%). Win rate 75.0%. That is +2.55 pp above the unconditional baseline. Not statistically significant (p=0.4137, q=0.5961 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Saturn (4 events since 2006), Nifty Midcap 100 averaged -1.49% over the next 5 trading days (base rate +0.27%). Win rate 0.0%. That is -1.75 pp below the unconditional baseline. Not statistically significant (p=0.2874, q=0.4622 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Saturn (4 events since 2006), Nifty Midcap 150 averaged +0.16% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is -0.10 pp below the unconditional baseline. Not statistically significant (p=0.8481, q=0.9178 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Saturn (4 events since 2006), BSE Sensex averaged -0.11% over the next 5 trading days (base rate +0.25%). Win rate 75.0%. That is -0.36 pp below the unconditional baseline. Not statistically significant (p=0.5436, q=0.7115 after Benjamini-Hochberg correction).

* When Rahu opposed Sun (29 events since 2000), Nifty 50 averaged +2.51% over the next 5 trading days (base rate +0.22%). Win rate 55.2%. That is +2.30 pp above the unconditional baseline. Nominally significant at p=0.02786, but it does not survive Benjamini-Hochberg correction (q=0.08406).
* When Rahu opposed Sun (29 events since 2000), Nifty Bank averaged +2.73% over the next 5 trading days (base rate +0.30%). Win rate 55.2%. That is +2.43 pp above the unconditional baseline. Nominally significant at p=0.04765, but it does not survive Benjamini-Hochberg correction (q=0.1238).
* When Rahu opposed Sun (29 events since 2000), Nifty Midcap 100 averaged +0.39% over the next 5 trading days (base rate +0.27%). Win rate 41.4%. That is +0.12 pp above the unconditional baseline. Not statistically significant (p=0.7999, q=0.888 after Benjamini-Hochberg correction).
* When Rahu opposed Sun (29 events since 2000), Nifty Midcap 150 averaged -0.02% over the next 5 trading days (base rate +0.26%). Win rate 55.2%. That is -0.29 pp below the unconditional baseline. Not statistically significant (p=0.5211, q=0.6939 after Benjamini-Hochberg correction).
* When Rahu opposed Sun (29 events since 2000), BSE Sensex averaged -0.99% over the next 5 trading days (base rate +0.25%). Win rate 34.5%. That is -1.24 pp below the unconditional baseline. Nominally significant at p=0.01914, but it does not survive Benjamini-Hochberg correction (q=0.06436).

* When Rahu formed a square with Sun (56 events since 2000), Nifty 50 averaged +3.15% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +2.93 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004136).
* When Rahu formed a square with Sun (56 events since 2000), Nifty Bank averaged +3.21% over the next 5 trading days (base rate +0.30%). Win rate 67.9%. That is +2.91 pp above the unconditional baseline. Statistically significant at p=0.0005297 and after Benjamini-Hochberg correction (q=0.003592).
* When Rahu formed a square with Sun (56 events since 2000), Nifty Midcap 100 averaged +1.19% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.92 pp above the unconditional baseline. Nominally significant at p=0.01438, but it does not survive Benjamini-Hochberg correction (q=0.05035).
* When Rahu formed a square with Sun (56 events since 2000), Nifty Midcap 150 averaged +0.81% over the next 5 trading days (base rate +0.26%). Win rate 66.1%. That is +0.55 pp above the unconditional baseline. Not statistically significant (p=0.118, q=0.2457 after Benjamini-Hochberg correction).
* When Rahu formed a square with Sun (56 events since 2000), BSE Sensex averaged +0.53% over the next 5 trading days (base rate +0.25%). Win rate 58.9%. That is +0.28 pp above the unconditional baseline. Not statistically significant (p=0.4501, q=0.6298 after Benjamini-Hochberg correction).

* When Rahu formed a trine with Sun (57 events since 2000), Nifty 50 averaged +2.80% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +2.58 pp above the unconditional baseline. Statistically significant at p=0.000192 and after Benjamini-Hochberg correction (q=0.001636).
* When Rahu formed a trine with Sun (57 events since 2000), Nifty Bank averaged +3.61% over the next 5 trading days (base rate +0.30%). Win rate 77.2%. That is +3.31 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0002276).
* When Rahu formed a trine with Sun (57 events since 2000), Nifty Midcap 100 averaged -0.10% over the next 5 trading days (base rate +0.27%). Win rate 31.6%. That is -0.36 pp below the unconditional baseline. Not statistically significant (p=0.399, q=0.5817 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Sun (57 events since 2000), Nifty Midcap 150 averaged +0.62% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.35 pp above the unconditional baseline. Not statistically significant (p=0.274, q=0.4503 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Sun (57 events since 2000), BSE Sensex averaged +0.13% over the next 5 trading days (base rate +0.25%). Win rate 57.9%. That is -0.12 pp below the unconditional baseline. Not statistically significant (p=0.7527, q=0.858 after Benjamini-Hochberg correction).

* When Rahu opposed Venus (29 events since 2000), Nifty 50 averaged +2.73% over the next 5 trading days (base rate +0.22%). Win rate 75.9%. That is +2.52 pp above the unconditional baseline. Statistically significant at p=0.01173 and after Benjamini-Hochberg correction (q=0.04321).
* When Rahu opposed Venus (29 events since 2000), Nifty Bank averaged +3.23% over the next 5 trading days (base rate +0.30%). Win rate 72.4%. That is +2.93 pp above the unconditional baseline. Statistically significant at p=0.009377 and after Benjamini-Hochberg correction (q=0.03581).
* When Rahu opposed Venus (29 events since 2000), Nifty Midcap 100 averaged +0.50% over the next 5 trading days (base rate +0.27%). Win rate 48.3%. That is +0.23 pp above the unconditional baseline. Not statistically significant (p=0.6676, q=0.8036 after Benjamini-Hochberg correction).
* When Rahu opposed Venus (29 events since 2000), Nifty Midcap 150 averaged +0.44% over the next 5 trading days (base rate +0.26%). Win rate 72.4%. That is +0.17 pp above the unconditional baseline. Not statistically significant (p=0.7183, q=0.8361 after Benjamini-Hochberg correction).
* When Rahu opposed Venus (29 events since 2000), BSE Sensex averaged +0.56% over the next 5 trading days (base rate +0.25%). Win rate 62.1%. That is +0.31 pp above the unconditional baseline. Not statistically significant (p=0.5643, q=0.7258 after Benjamini-Hochberg correction).

* When Rahu formed a square with Venus (60 events since 2000), Nifty 50 averaged +3.02% over the next 5 trading days (base rate +0.22%). Win rate 70.0%. That is +2.81 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004147).
* When Rahu formed a square with Venus (60 events since 2000), Nifty Bank averaged +3.46% over the next 5 trading days (base rate +0.30%). Win rate 70.0%. That is +3.16 pp above the unconditional baseline. Statistically significant at p=0.000105 and after Benjamini-Hochberg correction (q=0.001021).
* When Rahu formed a square with Venus (60 events since 2000), Nifty Midcap 100 averaged +0.08% over the next 5 trading days (base rate +0.27%). Win rate 35.0%. That is -0.19 pp below the unconditional baseline. Not statistically significant (p=0.6228, q=0.77 after Benjamini-Hochberg correction).
* When Rahu formed a square with Venus (60 events since 2000), Nifty Midcap 150 averaged +0.42% over the next 5 trading days (base rate +0.26%). Win rate 65.0%. That is +0.16 pp above the unconditional baseline. Not statistically significant (p=0.5809, q=0.7388 after Benjamini-Hochberg correction).
* When Rahu formed a square with Venus (60 events since 2000), BSE Sensex averaged +0.07% over the next 5 trading days (base rate +0.25%). Win rate 55.0%. That is -0.19 pp below the unconditional baseline. Not statistically significant (p=0.5919, q=0.7474 after Benjamini-Hochberg correction).

* When Rahu formed a trine with Venus (59 events since 2000), Nifty 50 averaged +2.56% over the next 5 trading days (base rate +0.22%). Win rate 64.4%. That is +2.35 pp above the unconditional baseline. Statistically significant at p=0.0007129 and after Benjamini-Hochberg correction (q=0.0045).
* When Rahu formed a trine with Venus (59 events since 2000), Nifty Bank averaged +2.60% over the next 5 trading days (base rate +0.30%). Win rate 59.3%. That is +2.30 pp above the unconditional baseline. Statistically significant at p=0.005509 and after Benjamini-Hochberg correction (q=0.02316).
* When Rahu formed a trine with Venus (59 events since 2000), Nifty Midcap 100 averaged +0.43% over the next 5 trading days (base rate +0.27%). Win rate 44.1%. That is +0.16 pp above the unconditional baseline. Not statistically significant (p=0.6097, q=0.7591 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Venus (59 events since 2000), Nifty Midcap 150 averaged +0.19% over the next 5 trading days (base rate +0.26%). Win rate 61.0%. That is -0.07 pp below the unconditional baseline. Not statistically significant (p=0.8063, q=0.8912 after Benjamini-Hochberg correction).
* When Rahu formed a trine with Venus (59 events since 2000), BSE Sensex averaged -0.10% over the next 5 trading days (base rate +0.25%). Win rate 52.5%. That is -0.35 pp below the unconditional baseline. Not statistically significant (p=0.3429, q=0.5231 after Benjamini-Hochberg correction).

* When Saturn opposed Sun (26 events since 2000), Nifty 50 averaged +3.12% over the next 5 trading days (base rate +0.22%). Win rate 73.1%. That is +2.90 pp above the unconditional baseline. Statistically significant at p=0.004337 and after Benjamini-Hochberg correction (q=0.01893).
* When Saturn opposed Sun (26 events since 2000), Nifty Bank averaged +3.59% over the next 5 trading days (base rate +0.30%). Win rate 76.9%. That is +3.29 pp above the unconditional baseline. Statistically significant at p=0.006831 and after Benjamini-Hochberg correction (q=0.02736).
* When Saturn opposed Sun (26 events since 2000), Nifty Midcap 100 averaged +0.03% over the next 5 trading days (base rate +0.27%). Win rate 34.6%. That is -0.24 pp below the unconditional baseline. Not statistically significant (p=0.7288, q=0.8422 after Benjamini-Hochberg correction).
* When Saturn opposed Sun (26 events since 2000), Nifty Midcap 150 averaged +0.89% over the next 5 trading days (base rate +0.26%). Win rate 73.1%. That is +0.63 pp above the unconditional baseline. Not statistically significant (p=0.201, q=0.362 after Benjamini-Hochberg correction).
* When Saturn opposed Sun (26 events since 2000), BSE Sensex averaged +1.06% over the next 5 trading days (base rate +0.25%). Win rate 69.2%. That is +0.81 pp above the unconditional baseline. Not statistically significant (p=0.1641, q=0.3154 after Benjamini-Hochberg correction).

* When Saturn formed a square with Sun (52 events since 2000), Nifty 50 averaged +3.22% over the next 5 trading days (base rate +0.22%). Win rate 69.2%. That is +3.00 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000262).
* When Saturn formed a square with Sun (52 events since 2000), Nifty Bank averaged +3.69% over the next 5 trading days (base rate +0.30%). Win rate 69.2%. That is +3.39 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004833).
* When Saturn formed a square with Sun (52 events since 2000), Nifty Midcap 100 averaged +0.71% over the next 5 trading days (base rate +0.27%). Win rate 46.2%. That is +0.44 pp above the unconditional baseline. Not statistically significant (p=0.1496, q=0.293 after Benjamini-Hochberg correction).
* When Saturn formed a square with Sun (52 events since 2000), Nifty Midcap 150 averaged +0.99% over the next 5 trading days (base rate +0.26%). Win rate 71.2%. That is +0.72 pp above the unconditional baseline. Statistically significant at p=0.01357 and after Benjamini-Hochberg correction (q=0.04865).
* When Saturn formed a square with Sun (52 events since 2000), BSE Sensex averaged +0.57% over the next 5 trading days (base rate +0.25%). Win rate 59.6%. That is +0.32 pp above the unconditional baseline. Not statistically significant (p=0.4288, q=0.6103 after Benjamini-Hochberg correction).

* When Saturn formed a trine with Sun (51 events since 2000), Nifty 50 averaged +3.06% over the next 5 trading days (base rate +0.22%). Win rate 72.5%. That is +2.84 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0007536).
* When Saturn formed a trine with Sun (51 events since 2000), Nifty Bank averaged +3.51% over the next 5 trading days (base rate +0.30%). Win rate 64.7%. That is +3.21 pp above the unconditional baseline. Statistically significant at p=0.0001999 and after Benjamini-Hochberg correction (q=0.001677).
* When Saturn formed a trine with Sun (51 events since 2000), Nifty Midcap 100 averaged -0.08% over the next 5 trading days (base rate +0.27%). Win rate 41.2%. That is -0.34 pp below the unconditional baseline. Not statistically significant (p=0.3201, q=0.4975 after Benjamini-Hochberg correction).
* When Saturn formed a trine with Sun (51 events since 2000), Nifty Midcap 150 averaged +0.92% over the next 5 trading days (base rate +0.26%). Win rate 72.5%. That is +0.66 pp above the unconditional baseline. Nominally significant at p=0.04904, but it does not survive Benjamini-Hochberg correction (q=0.1266).
* When Saturn formed a trine with Sun (51 events since 2000), BSE Sensex averaged +0.89% over the next 5 trading days (base rate +0.25%). Win rate 62.7%. That is +0.64 pp above the unconditional baseline. Not statistically significant (p=0.109, q=0.2312 after Benjamini-Hochberg correction).

* When Saturn opposed Venus (26 events since 2000), Nifty 50 averaged +2.91% over the next 5 trading days (base rate +0.22%). Win rate 65.4%. That is +2.69 pp above the unconditional baseline. Statistically significant at p=0.007921 and after Benjamini-Hochberg correction (q=0.03127).
* When Saturn opposed Venus (26 events since 2000), Nifty Bank averaged +3.14% over the next 5 trading days (base rate +0.30%). Win rate 57.7%. That is +2.84 pp above the unconditional baseline. Nominally significant at p=0.01699, but it does not survive Benjamini-Hochberg correction (q=0.05791).
* When Saturn opposed Venus (26 events since 2000), Nifty Midcap 100 averaged +0.44% over the next 5 trading days (base rate +0.27%). Win rate 42.3%. That is +0.17 pp above the unconditional baseline. Not statistically significant (p=0.7736, q=0.8721 after Benjamini-Hochberg correction).
* When Saturn opposed Venus (26 events since 2000), Nifty Midcap 150 averaged +0.60% over the next 5 trading days (base rate +0.26%). Win rate 61.5%. That is +0.34 pp above the unconditional baseline. Not statistically significant (p=0.4544, q=0.6337 after Benjamini-Hochberg correction).
* When Saturn opposed Venus (26 events since 2000), BSE Sensex averaged +0.68% over the next 5 trading days (base rate +0.25%). Win rate 57.7%. That is +0.43 pp above the unconditional baseline. Not statistically significant (p=0.4655, q=0.6423 after Benjamini-Hochberg correction).

* When Saturn formed a square with Venus (55 events since 2000), Nifty 50 averaged +2.63% over the next 5 trading days (base rate +0.22%). Win rate 65.5%. That is +2.41 pp above the unconditional baseline. Statistically significant at p=0.0004885 and after Benjamini-Hochberg correction (q=0.003396).
* When Saturn formed a square with Venus (55 events since 2000), Nifty Bank averaged +2.89% over the next 5 trading days (base rate +0.30%). Win rate 69.1%. That is +2.59 pp above the unconditional baseline. Statistically significant at p=0.001665 and after Benjamini-Hochberg correction (q=0.008745).
* When Saturn formed a square with Venus (55 events since 2000), Nifty Midcap 100 averaged +0.15% over the next 5 trading days (base rate +0.27%). Win rate 38.2%. That is -0.12 pp below the unconditional baseline. Not statistically significant (p=0.7368, q=0.8481 after Benjamini-Hochberg correction).
* When Saturn formed a square with Venus (55 events since 2000), Nifty Midcap 150 averaged +0.30% over the next 5 trading days (base rate +0.26%). Win rate 60.0%. That is +0.04 pp above the unconditional baseline. Not statistically significant (p=0.9094, q=0.959 after Benjamini-Hochberg correction).
* When Saturn formed a square with Venus (55 events since 2000), BSE Sensex averaged +0.02% over the next 5 trading days (base rate +0.25%). Win rate 52.7%. That is -0.23 pp below the unconditional baseline. Not statistically significant (p=0.5544, q=0.7203 after Benjamini-Hochberg correction).

* When Saturn formed a trine with Venus (53 events since 2000), Nifty 50 averaged +3.36% over the next 5 trading days (base rate +0.22%). Win rate 73.6%. That is +3.14 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.563e-05).
* When Saturn formed a trine with Venus (53 events since 2000), Nifty Bank averaged +3.94% over the next 5 trading days (base rate +0.30%). Win rate 73.6%. That is +3.64 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=6.925e-05).
* When Saturn formed a trine with Venus (53 events since 2000), Nifty Midcap 100 averaged +0.20% over the next 5 trading days (base rate +0.27%). Win rate 41.5%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.8353, q=0.9119 after Benjamini-Hochberg correction).
* When Saturn formed a trine with Venus (53 events since 2000), Nifty Midcap 150 averaged +0.75% over the next 5 trading days (base rate +0.26%). Win rate 69.8%. That is +0.49 pp above the unconditional baseline. Not statistically significant (p=0.105, q=0.2249 after Benjamini-Hochberg correction).
* When Saturn formed a trine with Venus (53 events since 2000), BSE Sensex averaged +0.36% over the next 5 trading days (base rate +0.25%). Win rate 58.5%. That is +0.11 pp above the unconditional baseline. Not statistically significant (p=0.7574, q=0.8604 after Benjamini-Hochberg correction).

**All windows — Major aspects (Trine / Square / Opposition)**

| Event | Index | Window | N | Mean ret | Base rate | Excess | Win % | p-value | q (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jupiter-Ketu Opposition | Nifty 50 | 1 | 4 | 0.1574 | 0.04492 | 0.1125 | 75 | 0.8268 | 0.9052 |
| Jupiter-Ketu Opposition | Nifty 50 | 3 | 4 | 1.194 | 0.1333 | 1.061 | 50 | 0.5974 | 0.7511 |
| Jupiter-Ketu Opposition | Nifty 50 | 5 | 4 | 2.002 | 0.2178 | 1.784 | 50 | 0.607 | 0.7565 |
| Jupiter-Ketu Opposition | Nifty 50 | 10 | 4 | 3.318 | 0.4212 | 2.897 | 75 | 0.4974 | 0.6741 |
| Jupiter-Ketu Opposition | Nifty 50 | 20 | 4 | 6.914 | 0.8264 | 6.088 | 75 | 0.4362 | 0.6173 |
| Jupiter-Ketu Opposition | Nifty Bank | 1 | 4 | 0.5264 | 0.06023 | 0.4662 | 75 | 0.5312 | 0.7014 |
| Jupiter-Ketu Opposition | Nifty Bank | 3 | 4 | 1.245 | 0.1819 | 1.063 | 50 | 0.6758 | 0.8083 |
| Jupiter-Ketu Opposition | Nifty Bank | 5 | 4 | 1.075 | 0.3 | 0.7755 | 50 | 0.8666 | 0.9304 |
| Jupiter-Ketu Opposition | Nifty Bank | 10 | 4 | 1.675 | 0.5834 | 1.091 | 50 | 0.8769 | 0.9372 |
| Jupiter-Ketu Opposition | Nifty Bank | 20 | 4 | 2.919 | 1.172 | 1.746 | 50 | 0.8468 | 0.9172 |
| Jupiter-Ketu Opposition | Nifty Midcap 100 | 1 | 4 | -0.556 | 0.05397 | -0.6099 | 50 | 0.2264 | 0.3915 |
| Jupiter-Ketu Opposition | Nifty Midcap 100 | 3 | 4 | -0.4137 | 0.1609 | -0.5746 | 50 | 0.5941 | 0.7492 |
| Jupiter-Ketu Opposition | Nifty Midcap 100 | 5 | 4 | -1.201 | 0.266 | -1.467 | 25 | 0.4494 | 0.6292 |
| Jupiter-Ketu Opposition | Nifty Midcap 100 | 10 | 4 | -0.3385 | 0.532 | -0.8705 | 50 | 0.6662 | 0.8025 |
| Jupiter-Ketu Opposition | Nifty Midcap 100 | 20 | 4 | 0.6123 | 1.065 | -0.4525 | 50 | 0.8157 | 0.897 |
| Jupiter-Ketu Opposition | Nifty Midcap 150 | 1 | 4 | 0.3091 | 0.05323 | 0.2558 | 75 | 0.6869 | 0.8141 |
| Jupiter-Ketu Opposition | Nifty Midcap 150 | 3 | 4 | 0.0001172 | 0.1594 | -0.1593 | 50 | 0.8907 | 0.9451 |
| Jupiter-Ketu Opposition | Nifty Midcap 150 | 5 | 4 | 0.06911 | 0.2642 | -0.1951 | 75 | 0.9245 | 0.9669 |
| Jupiter-Ketu Opposition | Nifty Midcap 150 | 10 | 4 | 1.635 | 0.5204 | 1.115 | 75 | 0.6948 | 0.8194 |
| Jupiter-Ketu Opposition | Nifty Midcap 150 | 20 | 4 | 1.852 | 1.047 | 0.8043 | 75 | 0.7904 | 0.8811 |
| Jupiter-Ketu Opposition | BSE Sensex | 1 | 4 | -0.03137 | 0.05036 | -0.08173 | 75 | 0.888 | 0.9436 |
| Jupiter-Ketu Opposition | BSE Sensex | 3 | 4 | -0.2566 | 0.1513 | -0.4079 | 50 | 0.7494 | 0.8555 |
| Jupiter-Ketu Opposition | BSE Sensex | 5 | 4 | -0.6045 | 0.2506 | -0.8551 | 50 | 0.7015 | 0.8237 |
| Jupiter-Ketu Opposition | BSE Sensex | 10 | 4 | -0.4586 | 0.4957 | -0.9542 | 25 | 0.7284 | 0.842 |
| Jupiter-Ketu Opposition | BSE Sensex | 20 | 4 | -0.7584 | 1.002 | -1.76 | 50 | 0.5605 | 0.7248 |
| Jupiter-Ketu Square | Nifty 50 | 1 | 8 | 0.4571 | 0.04492 | 0.4122 | 75 | 0.2851 | 0.4606 |
| Jupiter-Ketu Square | Nifty 50 | 3 | 8 | 1.73 | 0.1333 | 1.596 | 62.5 | 0.2392 | 0.4066 |
| Jupiter-Ketu Square | Nifty 50 | 5 | 8 | 4.077 | 0.2178 | 3.859 | 75 | 0.06384 | 0.1552 |
| Jupiter-Ketu Square | Nifty 50 | 10 | 8 | 5.303 | 0.4212 | 4.882 | 75 | 0.09613 | 0.2107 |
| Jupiter-Ketu Square | Nifty 50 | 20 | 8 | 10.01 | 0.8264 | 9.18 | 75 | 0.1005 | 0.2175 |
| Jupiter-Ketu Square | Nifty Bank | 1 | 8 | 1.017 | 0.06023 | 0.9569 | 75 | 0.07522 | 0.1752 |
| Jupiter-Ketu Square | Nifty Bank | 3 | 8 | 2.396 | 0.1819 | 2.214 | 62.5 | 0.1612 | 0.3112 |
| Jupiter-Ketu Square | Nifty Bank | 5 | 8 | 4.799 | 0.3 | 4.499 | 75 | 0.04589 | 0.1204 |
| Jupiter-Ketu Square | Nifty Bank | 10 | 8 | 7.052 | 0.5834 | 6.469 | 87.5 | 0.06383 | 0.1552 |
| Jupiter-Ketu Square | Nifty Bank | 20 | 8 | 9.968 | 1.172 | 8.796 | 87.5 | 0.05782 | 0.144 |
| Jupiter-Ketu Square | Nifty Midcap 100 | 1 | 8 | -0.03012 | 0.05397 | -0.08409 | 75 | 0.7325 | 0.8451 |
| Jupiter-Ketu Square | Nifty Midcap 100 | 3 | 8 | -0.5364 | 0.1609 | -0.6973 | 37.5 | 0.2826 | 0.4582 |
| Jupiter-Ketu Square | Nifty Midcap 100 | 5 | 8 | 0.3051 | 0.266 | 0.03911 | 37.5 | 0.9649 | 0.9862 |
| Jupiter-Ketu Square | Nifty Midcap 100 | 10 | 8 | 1.956 | 0.532 | 1.424 | 75 | 0.3462 | 0.5256 |
| Jupiter-Ketu Square | Nifty Midcap 100 | 20 | 8 | 2.542 | 1.065 | 1.477 | 75 | 0.5721 | 0.7317 |
| Jupiter-Ketu Square | Nifty Midcap 150 | 1 | 8 | 0.3017 | 0.05323 | 0.2485 | 75 | 0.6128 | 0.7615 |
| Jupiter-Ketu Square | Nifty Midcap 150 | 3 | 8 | -0.7118 | 0.1594 | -0.8712 | 62.5 | 0.2218 | 0.386 |
| Jupiter-Ketu Square | Nifty Midcap 150 | 5 | 8 | -0.1319 | 0.2642 | -0.3962 | 62.5 | 0.7675 | 0.8687 |
| Jupiter-Ketu Square | Nifty Midcap 150 | 10 | 8 | 0.5442 | 0.5204 | 0.02375 | 62.5 | 0.992 | 0.9968 |
| Jupiter-Ketu Square | Nifty Midcap 150 | 20 | 8 | 0.4237 | 1.047 | -0.6237 | 62.5 | 0.7399 | 0.8491 |
| Jupiter-Ketu Square | BSE Sensex | 1 | 8 | -0.519 | 0.05036 | -0.5694 | 37.5 | 0.4844 | 0.6622 |
| Jupiter-Ketu Square | BSE Sensex | 3 | 8 | -0.9219 | 0.1513 | -1.073 | 50 | 0.3093 | 0.4871 |
| Jupiter-Ketu Square | BSE Sensex | 5 | 8 | -0.5866 | 0.2506 | -0.8371 | 50 | 0.6045 | 0.7556 |
| Jupiter-Ketu Square | BSE Sensex | 10 | 8 | -0.9576 | 0.4957 | -1.453 | 50 | 0.6131 | 0.7615 |
| Jupiter-Ketu Square | BSE Sensex | 20 | 8 | -0.2368 | 1.002 | -1.238 | 50 | 0.6951 | 0.8194 |
| Jupiter-Ketu Trine | Nifty 50 | 1 | 8 | 0.355 | 0.04492 | 0.3101 | 75 | 0.4174 | 0.599 |
| Jupiter-Ketu Trine | Nifty 50 | 3 | 8 | 2.057 | 0.1333 | 1.924 | 87.5 | 0.06691 | 0.1604 |
| Jupiter-Ketu Trine | Nifty 50 | 5 | 8 | 3.36 | 0.2178 | 3.142 | 87.5 | 0.07245 | 0.1701 |
| Jupiter-Ketu Trine | Nifty 50 | 10 | 8 | 4.766 | 0.4212 | 4.345 | 87.5 | 0.06247 | 0.1531 |
| Jupiter-Ketu Trine | Nifty 50 | 20 | 8 | 3.906 | 0.8264 | 3.079 | 37.5 | 0.5954 | 0.7504 |
| Jupiter-Ketu Trine | Nifty Bank | 1 | 8 | 0.7985 | 0.06023 | 0.7383 | 75 | 0.2061 | 0.3678 |
| Jupiter-Ketu Trine | Nifty Bank | 3 | 8 | 2.598 | 0.1819 | 2.416 | 87.5 | 0.08081 | 0.1841 |
| Jupiter-Ketu Trine | Nifty Bank | 5 | 8 | 3.59 | 0.3 | 3.29 | 87.5 | 0.1089 | 0.231 |
| Jupiter-Ketu Trine | Nifty Bank | 10 | 8 | 5.379 | 0.5834 | 4.795 | 62.5 | 0.1203 | 0.2492 |
| Jupiter-Ketu Trine | Nifty Bank | 20 | 8 | 4.533 | 1.172 | 3.361 | 50 | 0.4909 | 0.6691 |
| Jupiter-Ketu Trine | Nifty Midcap 100 | 1 | 8 | -0.6331 | 0.05397 | -0.6871 | 62.5 | 0.279 | 0.4552 |
| Jupiter-Ketu Trine | Nifty Midcap 100 | 3 | 8 | -0.3859 | 0.1609 | -0.5468 | 50 | 0.5755 | 0.7342 |
| Jupiter-Ketu Trine | Nifty Midcap 100 | 5 | 8 | -0.4667 | 0.266 | -0.7328 | 50 | 0.4448 | 0.6249 |
| Jupiter-Ketu Trine | Nifty Midcap 100 | 10 | 8 | 1.453 | 0.532 | 0.9206 | 75 | 0.6699 | 0.8046 |
| Jupiter-Ketu Trine | Nifty Midcap 100 | 20 | 8 | -2.283 | 1.065 | -3.348 | 75 | 0.4459 | 0.6258 |
| Jupiter-Ketu Trine | Nifty Midcap 150 | 1 | 8 | 0.5866 | 0.05323 | 0.5334 | 75 | 0.2196 | 0.3853 |
| Jupiter-Ketu Trine | Nifty Midcap 150 | 3 | 8 | 0.7964 | 0.1594 | 0.6369 | 87.5 | 0.1887 | 0.3466 |
| Jupiter-Ketu Trine | Nifty Midcap 150 | 5 | 8 | 1.36 | 0.2642 | 1.095 | 75 | 0.09443 | 0.2083 |
| Jupiter-Ketu Trine | Nifty Midcap 150 | 10 | 8 | 3.029 | 0.5204 | 2.509 | 87.5 | 0.05185 | 0.1319 |
| Jupiter-Ketu Trine | Nifty Midcap 150 | 20 | 8 | -1.411 | 1.047 | -2.459 | 50 | 0.456 | 0.6341 |
| Jupiter-Ketu Trine | BSE Sensex | 1 | 8 | -0.09622 | 0.05036 | -0.1466 | 62.5 | 0.7181 | 0.8361 |
| Jupiter-Ketu Trine | BSE Sensex | 3 | 8 | 0.7072 | 0.1513 | 0.5559 | 75 | 0.4388 | 0.6191 |
| Jupiter-Ketu Trine | BSE Sensex | 5 | 8 | 1.529 | 0.2506 | 1.278 | 62.5 | 0.1639 | 0.3154 |
| Jupiter-Ketu Trine | BSE Sensex | 10 | 8 | 1.712 | 0.4957 | 1.216 | 87.5 | 0.2228 | 0.3869 |
| Jupiter-Ketu Trine | BSE Sensex | 20 | 8 | -1.559 | 1.002 | -2.561 | 25 | 0.3034 | 0.4806 |
| Jupiter-Mars Opposition | Nifty 50 | 1 | 20 | 0.5203 | 0.04492 | 0.4754 | 60 | 0.02917 | 0.08691 |
| Jupiter-Mars Opposition | Nifty 50 | 3 | 20 | 2.854 | 0.1333 | 2.72 | 75 | 0.001204 | 0.006859 |
| Jupiter-Mars Opposition | Nifty 50 | 5 | 20 | 5.08 | 0.2178 | 4.862 | 80 | 0.00041 | 0.002945 |
| Jupiter-Mars Opposition | Nifty 50 | 10 | 20 | 7.018 | 0.4212 | 6.597 | 90 | 9.931e-05 | 0.0009724 |
| Jupiter-Mars Opposition | Nifty 50 | 20 | 20 | 13.5 | 0.8264 | 12.67 | 90 | 0.0005102 | 0.003504 |
| Jupiter-Mars Opposition | Nifty Bank | 1 | 20 | 1.209 | 0.06023 | 1.149 | 70 | 0.003616 | 0.01642 |
| Jupiter-Mars Opposition | Nifty Bank | 3 | 20 | 3.716 | 0.1819 | 3.534 | 75 | 0.0005175 | 0.003541 |
| Jupiter-Mars Opposition | Nifty Bank | 5 | 20 | 6.081 | 0.3 | 5.781 | 80 | 0.0001187 | 0.001129 |
| Jupiter-Mars Opposition | Nifty Bank | 10 | 20 | 9.098 | 0.5834 | 8.514 | 95 | 3.124e-05 | 0.0003944 |
| Jupiter-Mars Opposition | Nifty Bank | 20 | 20 | 12.21 | 1.172 | 11.04 | 90 | 0.0002787 | 0.00216 |
| Jupiter-Mars Opposition | Nifty Midcap 100 | 1 | 20 | 0.209 | 0.05397 | 0.155 | 85 | 0.08579 | 0.1925 |
| Jupiter-Mars Opposition | Nifty Midcap 100 | 3 | 20 | 0.3264 | 0.1609 | 0.1656 | 35 | 0.6236 | 0.7706 |
| Jupiter-Mars Opposition | Nifty Midcap 100 | 5 | 20 | 0.1886 | 0.266 | -0.07739 | 30 | 0.8764 | 0.9372 |
| Jupiter-Mars Opposition | Nifty Midcap 100 | 10 | 20 | 2.653 | 0.532 | 2.121 | 80 | 0.006146 | 0.02524 |
| Jupiter-Mars Opposition | Nifty Midcap 100 | 20 | 20 | 3.086 | 1.065 | 2.021 | 80 | 0.2248 | 0.3894 |
| Jupiter-Mars Opposition | Nifty Midcap 150 | 1 | 20 | 0.6922 | 0.05323 | 0.639 | 50 | 0.01683 | 0.05753 |
| Jupiter-Mars Opposition | Nifty Midcap 150 | 3 | 20 | 0.7348 | 0.1594 | 0.5754 | 75 | 0.1464 | 0.2889 |
| Jupiter-Mars Opposition | Nifty Midcap 150 | 5 | 20 | 1.478 | 0.2642 | 1.214 | 80 | 0.03324 | 0.0955 |
| Jupiter-Mars Opposition | Nifty Midcap 150 | 10 | 20 | 3.725 | 0.5204 | 3.205 | 90 | 7.391e-05 | 0.000772 |
| Jupiter-Mars Opposition | Nifty Midcap 150 | 20 | 20 | 3.75 | 1.047 | 2.703 | 90 | 0.04313 | 0.1148 |
| Jupiter-Mars Opposition | BSE Sensex | 1 | 20 | 0.09273 | 0.05036 | 0.04237 | 40 | 0.8447 | 0.9163 |
| Jupiter-Mars Opposition | BSE Sensex | 3 | 20 | 0.2415 | 0.1513 | 0.09014 | 55 | 0.8598 | 0.9252 |
| Jupiter-Mars Opposition | BSE Sensex | 5 | 20 | 0.8479 | 0.2506 | 0.5973 | 65 | 0.4649 | 0.6421 |
| Jupiter-Mars Opposition | BSE Sensex | 10 | 20 | 2.005 | 0.4957 | 1.509 | 80 | 0.1759 | 0.33 |
| Jupiter-Mars Opposition | BSE Sensex | 20 | 20 | 3.224 | 1.002 | 2.223 | 75 | 0.2392 | 0.4066 |
| Jupiter-Mars Square | Nifty 50 | 1 | 28 | 0.2374 | 0.04492 | 0.1924 | 67.86 | 0.2598 | 0.4326 |
| Jupiter-Mars Square | Nifty 50 | 3 | 28 | 1.203 | 0.1333 | 1.07 | 60.71 | 0.0691 | 0.1642 |
| Jupiter-Mars Square | Nifty 50 | 5 | 28 | 2.071 | 0.2178 | 1.854 | 64.29 | 0.0682 | 0.1625 |
| Jupiter-Mars Square | Nifty 50 | 10 | 28 | 4.006 | 0.4212 | 3.584 | 67.86 | 0.003382 | 0.0155 |
| Jupiter-Mars Square | Nifty 50 | 20 | 28 | 8.053 | 0.8264 | 7.226 | 82.14 | 0.003454 | 0.01576 |
| Jupiter-Mars Square | Nifty Bank | 1 | 28 | 0.4331 | 0.06023 | 0.3728 | 67.86 | 0.2308 | 0.3964 |
| Jupiter-Mars Square | Nifty Bank | 3 | 28 | 1.672 | 0.1819 | 1.49 | 60.71 | 0.04049 | 0.1094 |
| Jupiter-Mars Square | Nifty Bank | 5 | 28 | 2.445 | 0.3 | 2.145 | 57.14 | 0.06445 | 0.1561 |
| Jupiter-Mars Square | Nifty Bank | 10 | 28 | 5.356 | 0.5834 | 4.772 | 82.14 | 0.00188 | 0.009683 |
| Jupiter-Mars Square | Nifty Bank | 20 | 28 | 8.153 | 1.172 | 6.981 | 75 | 0.002231 | 0.01085 |
| Jupiter-Mars Square | Nifty Midcap 100 | 1 | 28 | 0.02844 | 0.05397 | -0.02552 | 64.29 | 0.8787 | 0.9377 |
| Jupiter-Mars Square | Nifty Midcap 100 | 3 | 28 | 0.1357 | 0.1609 | -0.0252 | 42.86 | 0.9425 | 0.9769 |
| Jupiter-Mars Square | Nifty Midcap 100 | 5 | 28 | -0.2105 | 0.266 | -0.4765 | 39.29 | 0.3834 | 0.5656 |
| Jupiter-Mars Square | Nifty Midcap 100 | 10 | 28 | 2.259 | 0.532 | 1.727 | 67.86 | 0.07392 | 0.1727 |
| Jupiter-Mars Square | Nifty Midcap 100 | 20 | 28 | 2.442 | 1.065 | 1.377 | 75 | 0.4342 | 0.6164 |
| Jupiter-Mars Square | Nifty Midcap 150 | 1 | 28 | 0.1852 | 0.05323 | 0.132 | 57.14 | 0.5192 | 0.6924 |
| Jupiter-Mars Square | Nifty Midcap 150 | 3 | 28 | -0.0477 | 0.1594 | -0.2071 | 57.14 | 0.5094 | 0.6841 |
| Jupiter-Mars Square | Nifty Midcap 150 | 5 | 28 | -0.1722 | 0.2642 | -0.4365 | 57.14 | 0.3946 | 0.5783 |
| Jupiter-Mars Square | Nifty Midcap 150 | 10 | 28 | 2.085 | 0.5204 | 1.564 | 67.86 | 0.02734 | 0.08302 |
| Jupiter-Mars Square | Nifty Midcap 150 | 20 | 28 | 2.67 | 1.047 | 1.622 | 82.14 | 0.146 | 0.2885 |
| Jupiter-Mars Square | BSE Sensex | 1 | 28 | -0.1715 | 0.05036 | -0.2219 | 46.43 | 0.1821 | 0.3375 |
| Jupiter-Mars Square | BSE Sensex | 3 | 28 | -0.2574 | 0.1513 | -0.4087 | 42.86 | 0.2238 | 0.3881 |
| Jupiter-Mars Square | BSE Sensex | 5 | 28 | -0.6816 | 0.2506 | -0.9322 | 50 | 0.1119 | 0.2361 |
| Jupiter-Mars Square | BSE Sensex | 10 | 28 | 0.7682 | 0.4957 | 0.2725 | 57.14 | 0.7434 | 0.851 |
| Jupiter-Mars Square | BSE Sensex | 20 | 28 | 1.403 | 1.002 | 0.4015 | 67.86 | 0.7416 | 0.8502 |
| Jupiter-Mars Trine | Nifty 50 | 1 | 26 | 0.1492 | 0.04492 | 0.1043 | 57.69 | 0.6505 | 0.7932 |
| Jupiter-Mars Trine | Nifty 50 | 3 | 26 | 0.9217 | 0.1333 | 0.7885 | 50 | 0.212 | 0.3748 |
| Jupiter-Mars Trine | Nifty 50 | 5 | 26 | 2.091 | 0.2178 | 1.873 | 53.85 | 0.06587 | 0.1585 |
| Jupiter-Mars Trine | Nifty 50 | 10 | 26 | 3.938 | 0.4212 | 3.517 | 73.08 | 0.005998 | 0.02477 |
| Jupiter-Mars Trine | Nifty 50 | 20 | 26 | 7.517 | 0.8264 | 6.691 | 69.23 | 0.008298 | 0.03235 |
| Jupiter-Mars Trine | Nifty Bank | 1 | 26 | 0.3228 | 0.06023 | 0.2626 | 57.69 | 0.5713 | 0.7311 |
| Jupiter-Mars Trine | Nifty Bank | 3 | 26 | 1.176 | 0.1819 | 0.9939 | 46.15 | 0.2361 | 0.4036 |
| Jupiter-Mars Trine | Nifty Bank | 5 | 26 | 2.489 | 0.3 | 2.189 | 57.69 | 0.06183 | 0.1521 |
| Jupiter-Mars Trine | Nifty Bank | 10 | 26 | 4.816 | 0.5834 | 4.232 | 65.38 | 0.01325 | 0.04764 |
| Jupiter-Mars Trine | Nifty Bank | 20 | 26 | 6.501 | 1.172 | 5.328 | 57.69 | 0.0209 | 0.06804 |
| Jupiter-Mars Trine | Nifty Midcap 100 | 1 | 26 | -0.007601 | 0.05397 | -0.06157 | 61.54 | 0.6902 | 0.8175 |
| Jupiter-Mars Trine | Nifty Midcap 100 | 3 | 26 | -0.1542 | 0.1609 | -0.3151 | 38.46 | 0.3626 | 0.5446 |
| Jupiter-Mars Trine | Nifty Midcap 100 | 5 | 26 | 0.2693 | 0.266 | 0.003248 | 42.31 | 0.995 | 0.9976 |
| Jupiter-Mars Trine | Nifty Midcap 100 | 10 | 26 | 2.806 | 0.532 | 2.274 | 73.08 | 0.00485 | 0.02074 |
| Jupiter-Mars Trine | Nifty Midcap 100 | 20 | 26 | 3.204 | 1.065 | 2.139 | 76.92 | 0.01829 | 0.06201 |
| Jupiter-Mars Trine | Nifty Midcap 150 | 1 | 26 | 0.2144 | 0.05323 | 0.1612 | 57.69 | 0.5308 | 0.7014 |
| Jupiter-Mars Trine | Nifty Midcap 150 | 3 | 26 | -0.5453 | 0.1594 | -0.7047 | 42.31 | 0.01222 | 0.04475 |
| Jupiter-Mars Trine | Nifty Midcap 150 | 5 | 26 | -0.4878 | 0.2642 | -0.752 | 42.31 | 0.06622 | 0.1591 |
| Jupiter-Mars Trine | Nifty Midcap 150 | 10 | 26 | 0.6877 | 0.5204 | 0.1673 | 61.54 | 0.8639 | 0.9282 |
| Jupiter-Mars Trine | Nifty Midcap 150 | 20 | 26 | 0.9211 | 1.047 | -0.1264 | 69.23 | 0.905 | 0.9565 |
| Jupiter-Mars Trine | BSE Sensex | 1 | 26 | -0.1329 | 0.05036 | -0.1833 | 50 | 0.4614 | 0.6397 |
| Jupiter-Mars Trine | BSE Sensex | 3 | 26 | -0.4915 | 0.1513 | -0.6428 | 34.62 | 0.05874 | 0.146 |
| Jupiter-Mars Trine | BSE Sensex | 5 | 26 | -0.7098 | 0.2506 | -0.9603 | 34.62 | 0.0463 | 0.1213 |
| Jupiter-Mars Trine | BSE Sensex | 10 | 26 | 0.2093 | 0.4957 | -0.2864 | 61.54 | 0.7383 | 0.8485 |
| Jupiter-Mars Trine | BSE Sensex | 20 | 26 | 0.2716 | 1.002 | -0.7301 | 57.69 | 0.4727 | 0.6502 |
| Jupiter-Mercury Opposition | Nifty 50 | 1 | 28 | 0.478 | 0.04492 | 0.4331 | 67.86 | 0.0109 | 0.0409 |
| Jupiter-Mercury Opposition | Nifty 50 | 3 | 28 | 1.987 | 0.1333 | 1.853 | 67.86 | 0.0008601 | 0.005228 |
| Jupiter-Mercury Opposition | Nifty 50 | 5 | 28 | 2.927 | 0.2178 | 2.709 | 71.43 | 0.002592 | 0.0124 |
| Jupiter-Mercury Opposition | Nifty 50 | 10 | 28 | 3.841 | 0.4212 | 3.42 | 71.43 | 0.003699 | 0.01671 |
| Jupiter-Mercury Opposition | Nifty 50 | 20 | 28 | 7.445 | 0.8264 | 6.618 | 64.29 | 0.004999 | 0.02128 |
| Jupiter-Mercury Opposition | Nifty Bank | 1 | 28 | 0.8169 | 0.06023 | 0.7567 | 64.29 | 0.00646 | 0.02619 |
| Jupiter-Mercury Opposition | Nifty Bank | 3 | 28 | 2.509 | 0.1819 | 2.327 | 67.86 | 0.001931 | 0.00985 |
| Jupiter-Mercury Opposition | Nifty Bank | 5 | 28 | 2.932 | 0.3 | 2.632 | 60.71 | 0.01378 | 0.04906 |
| Jupiter-Mercury Opposition | Nifty Bank | 10 | 28 | 4.31 | 0.5834 | 3.727 | 71.43 | 0.01405 | 0.04956 |
| Jupiter-Mercury Opposition | Nifty Bank | 20 | 28 | 6.072 | 1.172 | 4.899 | 67.86 | 0.0234 | 0.07404 |
| Jupiter-Mercury Opposition | Nifty Midcap 100 | 1 | 28 | 0.4919 | 0.05397 | 0.4379 | 75 | 0.08846 | 0.1975 |
| Jupiter-Mercury Opposition | Nifty Midcap 100 | 3 | 28 | 0.4814 | 0.1609 | 0.3205 | 42.86 | 0.2967 | 0.4741 |
| Jupiter-Mercury Opposition | Nifty Midcap 100 | 5 | 28 | 1.129 | 0.266 | 0.8632 | 57.14 | 0.03712 | 0.1037 |
| Jupiter-Mercury Opposition | Nifty Midcap 100 | 10 | 28 | 2.395 | 0.532 | 1.863 | 82.14 | 0.001974 | 0.009988 |
| Jupiter-Mercury Opposition | Nifty Midcap 100 | 20 | 28 | 3.427 | 1.065 | 2.362 | 71.43 | 0.04967 | 0.1277 |
| Jupiter-Mercury Opposition | Nifty Midcap 150 | 1 | 28 | 0.3901 | 0.05323 | 0.3369 | 67.86 | 0.176 | 0.33 |
| Jupiter-Mercury Opposition | Nifty Midcap 150 | 3 | 28 | 0.6808 | 0.1594 | 0.5213 | 71.43 | 0.1069 | 0.2276 |
| Jupiter-Mercury Opposition | Nifty Midcap 150 | 5 | 28 | 0.3178 | 0.2642 | 0.05356 | 64.29 | 0.9237 | 0.9669 |
| Jupiter-Mercury Opposition | Nifty Midcap 150 | 10 | 28 | 1.132 | 0.5204 | 0.6116 | 71.43 | 0.4408 | 0.6217 |
| Jupiter-Mercury Opposition | Nifty Midcap 150 | 20 | 28 | 0.906 | 1.047 | -0.1414 | 57.14 | 0.9031 | 0.9551 |
| Jupiter-Mercury Opposition | BSE Sensex | 1 | 28 | 0.01407 | 0.05036 | -0.03629 | 57.14 | 0.877 | 0.9372 |
| Jupiter-Mercury Opposition | BSE Sensex | 3 | 28 | 0.5548 | 0.1513 | 0.4035 | 46.43 | 0.231 | 0.3966 |
| Jupiter-Mercury Opposition | BSE Sensex | 5 | 28 | 0.1925 | 0.2506 | -0.05809 | 64.29 | 0.9149 | 0.9623 |
| Jupiter-Mercury Opposition | BSE Sensex | 10 | 28 | 0.06953 | 0.4957 | -0.4261 | 57.14 | 0.5538 | 0.7201 |
| Jupiter-Mercury Opposition | BSE Sensex | 20 | 28 | 0.2899 | 1.002 | -0.7117 | 46.43 | 0.4958 | 0.6734 |
| Jupiter-Mercury Square | Nifty 50 | 1 | 65 | 0.4294 | 0.04492 | 0.3845 | 66.15 | 0.01682 | 0.05753 |
| Jupiter-Mercury Square | Nifty 50 | 3 | 65 | 1.824 | 0.1333 | 1.691 | 64.62 | 0.0009235 | 0.00548 |
| Jupiter-Mercury Square | Nifty 50 | 5 | 65 | 2.972 | 0.2178 | 2.754 | 66.15 | 0.0001911 | 0.001633 |
| Jupiter-Mercury Square | Nifty 50 | 10 | 65 | 3.996 | 0.4212 | 3.574 | 64.62 | 7.759e-05 | 0.0008038 |
| Jupiter-Mercury Square | Nifty 50 | 20 | 65 | 8.058 | 0.8264 | 7.232 | 75.38 | 3.507e-05 | 0.000427 |
| Jupiter-Mercury Square | Nifty Bank | 1 | 65 | 0.7883 | 0.06023 | 0.728 | 70.77 | 0.001657 | 0.008716 |
| Jupiter-Mercury Square | Nifty Bank | 3 | 65 | 2.369 | 0.1819 | 2.187 | 61.54 | 0.0002094 | 0.001731 |
| Jupiter-Mercury Square | Nifty Bank | 5 | 65 | 3.683 | 0.3 | 3.383 | 66.15 | 0.0001086 | 0.001049 |
| Jupiter-Mercury Square | Nifty Bank | 10 | 65 | 5.289 | 0.5834 | 4.705 | 69.23 | 1.807e-05 | 0.000262 |
| Jupiter-Mercury Square | Nifty Bank | 20 | 65 | 7.853 | 1.172 | 6.681 | 70.77 | 4.551e-05 | 0.0005236 |
| Jupiter-Mercury Square | Nifty Midcap 100 | 1 | 65 | 0.1251 | 0.05397 | 0.07111 | 70.77 | 0.6967 | 0.82 |
| Jupiter-Mercury Square | Nifty Midcap 100 | 3 | 65 | 0.1897 | 0.1609 | 0.02889 | 44.62 | 0.9342 | 0.9726 |
| Jupiter-Mercury Square | Nifty Midcap 100 | 5 | 65 | 0.01289 | 0.266 | -0.2531 | 40 | 0.5645 | 0.7258 |
| Jupiter-Mercury Square | Nifty Midcap 100 | 10 | 65 | 1.573 | 0.532 | 1.041 | 72.31 | 0.07238 | 0.1701 |
| Jupiter-Mercury Square | Nifty Midcap 100 | 20 | 65 | 2.341 | 1.065 | 1.276 | 69.23 | 0.159 | 0.3078 |
| Jupiter-Mercury Square | Nifty Midcap 150 | 1 | 65 | 0.4974 | 0.05323 | 0.4441 | 64.62 | 0.009695 | 0.03676 |
| Jupiter-Mercury Square | Nifty Midcap 150 | 3 | 65 | 0.4046 | 0.1594 | 0.2451 | 61.54 | 0.5169 | 0.6905 |
| Jupiter-Mercury Square | Nifty Midcap 150 | 5 | 65 | 0.6562 | 0.2642 | 0.3919 | 64.62 | 0.3883 | 0.5706 |
| Jupiter-Mercury Square | Nifty Midcap 150 | 10 | 65 | 1.871 | 0.5204 | 1.351 | 64.62 | 0.01772 | 0.0603 |
| Jupiter-Mercury Square | Nifty Midcap 150 | 20 | 65 | 2.163 | 1.047 | 1.115 | 75.38 | 0.1854 | 0.3423 |
| Jupiter-Mercury Square | BSE Sensex | 1 | 65 | 0.007051 | 0.05036 | -0.04331 | 49.23 | 0.7869 | 0.8798 |
| Jupiter-Mercury Square | BSE Sensex | 3 | 65 | 0.3974 | 0.1513 | 0.2461 | 53.85 | 0.5655 | 0.7267 |
| Jupiter-Mercury Square | BSE Sensex | 5 | 65 | 0.4667 | 0.2506 | 0.2161 | 55.38 | 0.696 | 0.82 |
| Jupiter-Mercury Square | BSE Sensex | 10 | 65 | 0.6375 | 0.4957 | 0.1418 | 53.85 | 0.8167 | 0.8978 |
| Jupiter-Mercury Square | BSE Sensex | 20 | 65 | 1.613 | 1.002 | 0.6113 | 63.08 | 0.5141 | 0.6876 |
| Jupiter-Mercury Trine | Nifty 50 | 1 | 63 | 0.334 | 0.04492 | 0.2891 | 65.08 | 0.01397 | 0.04946 |
| Jupiter-Mercury Trine | Nifty 50 | 3 | 63 | 1.456 | 0.1333 | 1.323 | 60.32 | 0.0006375 | 0.004122 |
| Jupiter-Mercury Trine | Nifty 50 | 5 | 63 | 2.501 | 0.2178 | 2.283 | 73.02 | 0.0002957 | 0.002249 |
| Jupiter-Mercury Trine | Nifty 50 | 10 | 63 | 3.124 | 0.4212 | 2.703 | 63.49 | 0.001129 | 0.006506 |
| Jupiter-Mercury Trine | Nifty 50 | 20 | 63 | 7.028 | 0.8264 | 6.202 | 71.43 | 9.555e-05 | 0.000948 |
| Jupiter-Mercury Trine | Nifty Bank | 1 | 63 | 0.6755 | 0.06023 | 0.6152 | 65.08 | 0.0008831 | 0.005317 |
| Jupiter-Mercury Trine | Nifty Bank | 3 | 63 | 1.91 | 0.1819 | 1.728 | 63.49 | 0.0005951 | 0.003895 |
| Jupiter-Mercury Trine | Nifty Bank | 5 | 63 | 2.88 | 0.3 | 2.58 | 69.84 | 0.0005369 | 0.003628 |
| Jupiter-Mercury Trine | Nifty Bank | 10 | 63 | 3.734 | 0.5834 | 3.15 | 60.32 | 0.002905 | 0.01364 |
| Jupiter-Mercury Trine | Nifty Bank | 20 | 63 | 6.324 | 1.172 | 5.151 | 74.6 | 0.0003496 | 0.002591 |
| Jupiter-Mercury Trine | Nifty Midcap 100 | 1 | 63 | -0.1051 | 0.05397 | -0.1591 | 57.14 | 0.2808 | 0.4572 |
| Jupiter-Mercury Trine | Nifty Midcap 100 | 3 | 63 | -0.03124 | 0.1609 | -0.1921 | 38.1 | 0.4976 | 0.6741 |
| Jupiter-Mercury Trine | Nifty Midcap 100 | 5 | 63 | -0.03839 | 0.266 | -0.3044 | 39.68 | 0.3195 | 0.4967 |
| Jupiter-Mercury Trine | Nifty Midcap 100 | 10 | 63 | 1.549 | 0.532 | 1.017 | 66.67 | 0.02412 | 0.07576 |
| Jupiter-Mercury Trine | Nifty Midcap 100 | 20 | 63 | 2.577 | 1.065 | 1.513 | 73.02 | 0.04837 | 0.1254 |
| Jupiter-Mercury Trine | Nifty Midcap 150 | 1 | 63 | 0.3105 | 0.05323 | 0.2572 | 63.49 | 0.07338 | 0.1719 |
| Jupiter-Mercury Trine | Nifty Midcap 150 | 3 | 63 | 0.08426 | 0.1594 | -0.07519 | 58.73 | 0.7669 | 0.8685 |
| Jupiter-Mercury Trine | Nifty Midcap 150 | 5 | 63 | 0.2169 | 0.2642 | -0.04738 | 68.25 | 0.8763 | 0.9372 |
| Jupiter-Mercury Trine | Nifty Midcap 150 | 10 | 63 | 1.012 | 0.5204 | 0.4917 | 58.73 | 0.2942 | 0.4706 |
| Jupiter-Mercury Trine | Nifty Midcap 150 | 20 | 63 | 1.787 | 1.047 | 0.7395 | 71.43 | 0.1827 | 0.3383 |
| Jupiter-Mercury Trine | BSE Sensex | 1 | 63 | -0.09096 | 0.05036 | -0.1413 | 50.79 | 0.2987 | 0.4752 |
| Jupiter-Mercury Trine | BSE Sensex | 3 | 63 | -0.235 | 0.1513 | -0.3863 | 49.21 | 0.1901 | 0.3481 |
| Jupiter-Mercury Trine | BSE Sensex | 5 | 63 | -0.3471 | 0.2506 | -0.5977 | 55.56 | 0.08847 | 0.1975 |
| Jupiter-Mercury Trine | BSE Sensex | 10 | 63 | 0.03152 | 0.4957 | -0.4641 | 55.56 | 0.3186 | 0.4957 |
| Jupiter-Mercury Trine | BSE Sensex | 20 | 63 | 0.5808 | 1.002 | -0.4209 | 60.32 | 0.5228 | 0.6952 |
| Jupiter-Moon Opposition | Nifty 50 | 1 | 56 | 0.5928 | 0.04492 | 0.5478 | 60.71 | 0.007379 | 0.02928 |
| Jupiter-Moon Opposition | Nifty 50 | 3 | 56 | 2.48 | 0.1333 | 2.347 | 75 | 6.515e-07 | 1.64e-05 |
| Jupiter-Moon Opposition | Nifty 50 | 5 | 56 | 3.634 | 0.2178 | 3.417 | 66.07 | 2.918e-06 | 6.046e-05 |
| Jupiter-Moon Opposition | Nifty 50 | 10 | 56 | 4.469 | 0.4212 | 4.048 | 64.29 | 3.741e-05 | 0.0004468 |
| Jupiter-Moon Opposition | Nifty 50 | 20 | 56 | 9.538 | 0.8264 | 8.711 | 73.21 | 3.491e-06 | 6.855e-05 |
| Jupiter-Moon Opposition | Nifty Bank | 1 | 56 | 1.103 | 0.06023 | 1.043 | 64.29 | 0.0003881 | 0.00282 |
| Jupiter-Moon Opposition | Nifty Bank | 3 | 56 | 3.212 | 0.1819 | 3.03 | 75 | 4.491e-07 | 1.248e-05 |
| Jupiter-Moon Opposition | Nifty Bank | 5 | 56 | 4.153 | 0.3 | 3.853 | 69.64 | 4.728e-06 | 8.662e-05 |
| Jupiter-Moon Opposition | Nifty Bank | 10 | 56 | 5.509 | 0.5834 | 4.925 | 66.07 | 6.683e-05 | 0.0007181 |
| Jupiter-Moon Opposition | Nifty Bank | 20 | 56 | 8.708 | 1.172 | 7.536 | 76.79 | 7.895e-06 | 0.0001293 |
| Jupiter-Moon Opposition | Nifty Midcap 100 | 1 | 56 | 0.3368 | 0.05397 | 0.2828 | 75 | 0.1555 | 0.3023 |
| Jupiter-Moon Opposition | Nifty Midcap 100 | 3 | 56 | 0.6591 | 0.1609 | 0.4983 | 41.07 | 0.05714 | 0.1427 |
| Jupiter-Moon Opposition | Nifty Midcap 100 | 5 | 56 | 0.2699 | 0.266 | 0.003898 | 39.29 | 0.9897 | 0.9958 |
| Jupiter-Moon Opposition | Nifty Midcap 100 | 10 | 56 | 1.861 | 0.532 | 1.329 | 69.64 | 0.005386 | 0.0227 |
| Jupiter-Moon Opposition | Nifty Midcap 100 | 20 | 56 | 3.139 | 1.065 | 2.075 | 73.21 | 0.001512 | 0.008128 |
| Jupiter-Moon Opposition | Nifty Midcap 150 | 1 | 56 | 0.699 | 0.05323 | 0.6458 | 62.5 | 0.002092 | 0.01039 |
| Jupiter-Moon Opposition | Nifty Midcap 150 | 3 | 56 | 0.755 | 0.1594 | 0.5956 | 75 | 0.03888 | 0.1067 |
| Jupiter-Moon Opposition | Nifty Midcap 150 | 5 | 56 | 0.7393 | 0.2642 | 0.4751 | 67.86 | 0.1455 | 0.2877 |
| Jupiter-Moon Opposition | Nifty Midcap 150 | 10 | 56 | 1.436 | 0.5204 | 0.9154 | 62.5 | 0.1334 | 0.27 |
| Jupiter-Moon Opposition | Nifty Midcap 150 | 20 | 56 | 2.272 | 1.047 | 1.225 | 71.43 | 0.05741 | 0.1432 |
| Jupiter-Moon Opposition | BSE Sensex | 1 | 56 | 0.2311 | 0.05036 | 0.1807 | 46.43 | 0.3883 | 0.5706 |
| Jupiter-Moon Opposition | BSE Sensex | 3 | 56 | 0.8683 | 0.1513 | 0.717 | 64.29 | 0.03785 | 0.105 |
| Jupiter-Moon Opposition | BSE Sensex | 5 | 56 | 0.6119 | 0.2506 | 0.3614 | 57.14 | 0.3324 | 0.5119 |
| Jupiter-Moon Opposition | BSE Sensex | 10 | 56 | 0.5283 | 0.4957 | 0.03267 | 55.36 | 0.9545 | 0.982 |
| Jupiter-Moon Opposition | BSE Sensex | 20 | 56 | 1.796 | 1.002 | 0.794 | 64.29 | 0.283 | 0.4587 |
| Jupiter-Moon Square | Nifty 50 | 1 | 122 | 0.4305 | 0.04492 | 0.3855 | 69.67 | 0.0005448 | 0.003661 |
| Jupiter-Moon Square | Nifty 50 | 3 | 122 | 1.832 | 0.1333 | 1.699 | 64.75 | 9.642e-08 | 3.493e-06 |
| Jupiter-Moon Square | Nifty 50 | 5 | 122 | 2.831 | 0.2178 | 2.614 | 68.85 | 1.257e-07 | 4.405e-06 |
| Jupiter-Moon Square | Nifty 50 | 10 | 122 | 3.696 | 0.4212 | 3.275 | 70.49 | 1.069e-07 | 3.782e-06 |
| Jupiter-Moon Square | Nifty 50 | 20 | 121 | 7.417 | 0.8264 | 6.59 | 72.73 | 3.877e-08 | 1.615e-06 |
| Jupiter-Moon Square | Nifty Bank | 1 | 122 | 0.7416 | 0.06023 | 0.6814 | 68.85 | 7.388e-06 | 0.0001226 |
| Jupiter-Moon Square | Nifty Bank | 3 | 122 | 2.281 | 0.1819 | 2.099 | 68.03 | 4.536e-08 | 1.829e-06 |
| Jupiter-Moon Square | Nifty Bank | 5 | 122 | 3.255 | 0.3 | 2.955 | 66.39 | 3.238e-07 | 9.871e-06 |
| Jupiter-Moon Square | Nifty Bank | 10 | 122 | 4.76 | 0.5834 | 4.176 | 74.59 | 4.29e-08 | 1.768e-06 |
| Jupiter-Moon Square | Nifty Bank | 20 | 121 | 6.908 | 1.172 | 5.736 | 70.25 | 1.124e-06 | 2.634e-05 |
| Jupiter-Moon Square | Nifty Midcap 100 | 1 | 122 | 0.1932 | 0.05397 | 0.1393 | 68.85 | 0.2431 | 0.4113 |
| Jupiter-Moon Square | Nifty Midcap 100 | 3 | 122 | 0.3636 | 0.1609 | 0.2027 | 41.8 | 0.4042 | 0.5862 |
| Jupiter-Moon Square | Nifty Midcap 100 | 5 | 122 | 0.2484 | 0.266 | -0.01762 | 45.9 | 0.9537 | 0.982 |
| Jupiter-Moon Square | Nifty Midcap 100 | 10 | 122 | 1.36 | 0.532 | 0.8284 | 68.85 | 0.05995 | 0.1486 |
| Jupiter-Moon Square | Nifty Midcap 100 | 20 | 121 | 1.681 | 1.065 | 0.6167 | 68.6 | 0.3131 | 0.4908 |
| Jupiter-Moon Square | Nifty Midcap 150 | 1 | 122 | 0.5139 | 0.05323 | 0.4607 | 74.59 | 0.0001359 | 0.00125 |
| Jupiter-Moon Square | Nifty Midcap 150 | 3 | 122 | 0.6439 | 0.1594 | 0.4844 | 66.39 | 0.03379 | 0.0965 |
| Jupiter-Moon Square | Nifty Midcap 150 | 5 | 122 | 0.8298 | 0.2642 | 0.5656 | 66.39 | 0.0632 | 0.1544 |
| Jupiter-Moon Square | Nifty Midcap 150 | 10 | 122 | 1.748 | 0.5204 | 1.227 | 70.49 | 0.001657 | 0.008716 |
| Jupiter-Moon Square | Nifty Midcap 150 | 20 | 121 | 1.948 | 1.047 | 0.9004 | 71.9 | 0.1024 | 0.2205 |
| Jupiter-Moon Square | BSE Sensex | 1 | 122 | 0.1304 | 0.05036 | 0.08 | 57.38 | 0.492 | 0.6705 |
| Jupiter-Moon Square | BSE Sensex | 3 | 122 | 0.4538 | 0.1513 | 0.3025 | 56.56 | 0.2763 | 0.4533 |
| Jupiter-Moon Square | BSE Sensex | 5 | 122 | 0.262 | 0.2506 | 0.01139 | 58.2 | 0.9739 | 0.9895 |
| Jupiter-Moon Square | BSE Sensex | 10 | 122 | 0.4645 | 0.4957 | -0.03118 | 58.2 | 0.9413 | 0.9767 |
| Jupiter-Moon Square | BSE Sensex | 20 | 121 | 1.125 | 1.002 | 0.1234 | 64.46 | 0.8392 | 0.9128 |
| Jupiter-Moon Trine | Nifty 50 | 1 | 96 | 0.3059 | 0.04492 | 0.261 | 64.58 | 0.01996 | 0.06609 |
| Jupiter-Moon Trine | Nifty 50 | 3 | 96 | 1.735 | 0.1333 | 1.602 | 73.96 | 1.618e-07 | 5.323e-06 |
| Jupiter-Moon Trine | Nifty 50 | 5 | 96 | 2.854 | 0.2178 | 2.636 | 70.83 | 5.39e-07 | 1.413e-05 |
| Jupiter-Moon Trine | Nifty 50 | 10 | 96 | 3.95 | 0.4212 | 3.529 | 69.79 | 2.131e-07 | 6.831e-06 |
| Jupiter-Moon Trine | Nifty 50 | 20 | 96 | 7.82 | 0.8264 | 6.994 | 71.88 | 2.296e-07 | 7.235e-06 |
| Jupiter-Moon Trine | Nifty Bank | 1 | 96 | 0.6373 | 0.06023 | 0.5771 | 62.5 | 0.0005974 | 0.003903 |
| Jupiter-Moon Trine | Nifty Bank | 3 | 96 | 2.153 | 0.1819 | 1.971 | 67.71 | 5.547e-07 | 1.445e-05 |
| Jupiter-Moon Trine | Nifty Bank | 5 | 96 | 3.121 | 0.3 | 2.821 | 65.62 | 3.455e-06 | 6.82e-05 |
| Jupiter-Moon Trine | Nifty Bank | 10 | 96 | 4.83 | 0.5834 | 4.246 | 70.83 | 5.889e-07 | 1.512e-05 |
| Jupiter-Moon Trine | Nifty Bank | 20 | 96 | 7.019 | 1.172 | 5.847 | 70.83 | 1.558e-06 | 3.458e-05 |
| Jupiter-Moon Trine | Nifty Midcap 100 | 1 | 96 | -0.1136 | 0.05397 | -0.1675 | 56.25 | 0.2201 | 0.3853 |
| Jupiter-Moon Trine | Nifty Midcap 100 | 3 | 96 | 0.1584 | 0.1609 | -0.002414 | 39.58 | 0.9918 | 0.9968 |
| Jupiter-Moon Trine | Nifty Midcap 100 | 5 | 96 | 0.2689 | 0.266 | 0.002927 | 45.83 | 0.9919 | 0.9968 |
| Jupiter-Moon Trine | Nifty Midcap 100 | 10 | 96 | 1.68 | 0.532 | 1.148 | 70.83 | 0.007347 | 0.02921 |
| Jupiter-Moon Trine | Nifty Midcap 100 | 20 | 96 | 2.393 | 1.065 | 1.328 | 68.75 | 0.03639 | 0.1022 |
| Jupiter-Moon Trine | Nifty Midcap 150 | 1 | 96 | 0.3858 | 0.05323 | 0.3325 | 61.46 | 0.00686 | 0.02743 |
| Jupiter-Moon Trine | Nifty Midcap 150 | 3 | 96 | 0.4234 | 0.1594 | 0.264 | 72.92 | 0.07889 | 0.1811 |
| Jupiter-Moon Trine | Nifty Midcap 150 | 5 | 96 | 0.5863 | 0.2642 | 0.3221 | 69.79 | 0.1664 | 0.3183 |
| Jupiter-Moon Trine | Nifty Midcap 150 | 10 | 96 | 1.731 | 0.5204 | 1.21 | 72.92 | 0.001083 | 0.006319 |
| Jupiter-Moon Trine | Nifty Midcap 150 | 20 | 96 | 1.862 | 1.047 | 0.8144 | 70.83 | 0.1363 | 0.274 |
| Jupiter-Moon Trine | BSE Sensex | 1 | 96 | 0.08386 | 0.05036 | 0.0335 | 52.08 | 0.7677 | 0.8687 |
| Jupiter-Moon Trine | BSE Sensex | 3 | 96 | 0.388 | 0.1513 | 0.2367 | 67.71 | 0.2701 | 0.4454 |
| Jupiter-Moon Trine | BSE Sensex | 5 | 96 | 0.3546 | 0.2506 | 0.104 | 59.38 | 0.7213 | 0.8384 |
| Jupiter-Moon Trine | BSE Sensex | 10 | 96 | 1.008 | 0.4957 | 0.5128 | 61.46 | 0.1852 | 0.3421 |
| Jupiter-Moon Trine | BSE Sensex | 20 | 96 | 1.402 | 1.002 | 0.4007 | 62.5 | 0.5331 | 0.7018 |
| Jupiter-Rahu Opposition | Nifty 50 | 1 | 3 | 0.5958 | 0.04492 | 0.5509 | 100 | 0.2017 | 0.363 |
| Jupiter-Rahu Opposition | Nifty 50 | 3 | 3 | 3.381 | 0.1333 | 3.248 | 100 | 0.1051 | 0.2249 |
| Jupiter-Rahu Opposition | Nifty 50 | 5 | 3 | 5.222 | 0.2178 | 5.004 | 100 | 0.157 | 0.3048 |
| Jupiter-Rahu Opposition | Nifty 50 | 10 | 3 | 5.968 | 0.4212 | 5.547 | 100 | 0.2466 | 0.4162 |
| Jupiter-Rahu Opposition | Nifty 50 | 20 | 3 | 7.7 | 0.8264 | 6.874 | 33.33 | 0.5335 | 0.7018 |
| Jupiter-Rahu Opposition | Nifty Bank | 1 | 3 | 0.9123 | 0.06023 | 0.8521 | 66.67 | 0.3721 | 0.5538 |
| Jupiter-Rahu Opposition | Nifty Bank | 3 | 3 | 4.608 | 0.1819 | 4.426 | 100 | 0.07808 | 0.1795 |
| Jupiter-Rahu Opposition | Nifty Bank | 5 | 3 | 6.349 | 0.3 | 6.049 | 100 | 0.1251 | 0.2567 |
| Jupiter-Rahu Opposition | Nifty Bank | 10 | 3 | 7.417 | 0.5834 | 6.834 | 66.67 | 0.2842 | 0.4596 |
| Jupiter-Rahu Opposition | Nifty Bank | 20 | 3 | 7.052 | 1.172 | 5.88 | 66.67 | 0.5372 | 0.7051 |
| Jupiter-Rahu Opposition | Nifty Midcap 100 | 1 | 3 | 0.1287 | 0.05397 | 0.07478 | 100 | 0.2378 | 0.4054 |
| Jupiter-Rahu Opposition | Nifty Midcap 100 | 3 | 3 | 0.4736 | 0.1609 | 0.3127 | 66.67 | 0.5453 | 0.7133 |
| Jupiter-Rahu Opposition | Nifty Midcap 100 | 5 | 3 | 0.808 | 0.266 | 0.542 | 66.67 | 0.5334 | 0.7018 |
| Jupiter-Rahu Opposition | Nifty Midcap 100 | 10 | 3 | 2.135 | 0.532 | 1.603 | 100 | 0.3095 | 0.4871 |
| Jupiter-Rahu Opposition | Nifty Midcap 100 | 20 | 3 | -0.209 | 1.065 | -1.274 | 66.67 | 0.7742 | 0.8721 |
| Jupiter-Rahu Opposition | Nifty Midcap 150 | 1 | 3 | 0.8004 | 0.05323 | 0.7472 | 100 | 0.2524 | 0.424 |
| Jupiter-Rahu Opposition | Nifty Midcap 150 | 3 | 3 | 1.724 | 0.1594 | 1.564 | 100 | 0.13 | 0.2646 |
| Jupiter-Rahu Opposition | Nifty Midcap 150 | 5 | 3 | 2.607 | 0.2642 | 2.342 | 100 | 0.04725 | 0.1231 |
| Jupiter-Rahu Opposition | Nifty Midcap 150 | 10 | 3 | 3.696 | 0.5204 | 3.175 | 100 | 0.09192 | 0.2037 |
| Jupiter-Rahu Opposition | Nifty Midcap 150 | 20 | 3 | 0.8541 | 1.047 | -0.1933 | 33.33 | 0.9386 | 0.9749 |
| Jupiter-Rahu Opposition | BSE Sensex | 1 | 3 | 0.074 | 0.05036 | 0.02364 | 66.67 | 0.9335 | 0.9724 |
| Jupiter-Rahu Opposition | BSE Sensex | 3 | 3 | 0.7598 | 0.1513 | 0.6085 | 66.67 | 0.7201 | 0.8373 |
| Jupiter-Rahu Opposition | BSE Sensex | 5 | 3 | 1.511 | 0.2506 | 1.261 | 66.67 | 0.4634 | 0.6414 |
| Jupiter-Rahu Opposition | BSE Sensex | 10 | 3 | 2.233 | 0.4957 | 1.737 | 100 | 0.05933 | 0.1471 |
| Jupiter-Rahu Opposition | BSE Sensex | 20 | 3 | 1.947 | 1.002 | 0.9451 | 33.33 | 0.8024 | 0.8899 |
| Jupiter-Rahu Square | Nifty 50 | 1 | 8 | 0.4571 | 0.04492 | 0.4122 | 75 | 0.2851 | 0.4606 |
| Jupiter-Rahu Square | Nifty 50 | 3 | 8 | 1.73 | 0.1333 | 1.596 | 62.5 | 0.2392 | 0.4066 |
| Jupiter-Rahu Square | Nifty 50 | 5 | 8 | 4.077 | 0.2178 | 3.859 | 75 | 0.06384 | 0.1552 |
| Jupiter-Rahu Square | Nifty 50 | 10 | 8 | 5.303 | 0.4212 | 4.882 | 75 | 0.09613 | 0.2107 |
| Jupiter-Rahu Square | Nifty 50 | 20 | 8 | 10.01 | 0.8264 | 9.18 | 75 | 0.1005 | 0.2175 |
| Jupiter-Rahu Square | Nifty Bank | 1 | 8 | 1.017 | 0.06023 | 0.9569 | 75 | 0.07522 | 0.1752 |
| Jupiter-Rahu Square | Nifty Bank | 3 | 8 | 2.396 | 0.1819 | 2.214 | 62.5 | 0.1612 | 0.3112 |
| Jupiter-Rahu Square | Nifty Bank | 5 | 8 | 4.799 | 0.3 | 4.499 | 75 | 0.04589 | 0.1204 |
| Jupiter-Rahu Square | Nifty Bank | 10 | 8 | 7.052 | 0.5834 | 6.469 | 87.5 | 0.06383 | 0.1552 |
| Jupiter-Rahu Square | Nifty Bank | 20 | 8 | 9.968 | 1.172 | 8.796 | 87.5 | 0.05782 | 0.144 |
| Jupiter-Rahu Square | Nifty Midcap 100 | 1 | 8 | -0.03012 | 0.05397 | -0.08409 | 75 | 0.7325 | 0.8451 |
| Jupiter-Rahu Square | Nifty Midcap 100 | 3 | 8 | -0.5364 | 0.1609 | -0.6973 | 37.5 | 0.2826 | 0.4582 |
| Jupiter-Rahu Square | Nifty Midcap 100 | 5 | 8 | 0.3051 | 0.266 | 0.03911 | 37.5 | 0.9649 | 0.9862 |
| Jupiter-Rahu Square | Nifty Midcap 100 | 10 | 8 | 1.956 | 0.532 | 1.424 | 75 | 0.3462 | 0.5256 |
| Jupiter-Rahu Square | Nifty Midcap 100 | 20 | 8 | 2.542 | 1.065 | 1.477 | 75 | 0.5721 | 0.7317 |
| Jupiter-Rahu Square | Nifty Midcap 150 | 1 | 8 | 0.3017 | 0.05323 | 0.2485 | 75 | 0.6128 | 0.7615 |
| Jupiter-Rahu Square | Nifty Midcap 150 | 3 | 8 | -0.7118 | 0.1594 | -0.8712 | 62.5 | 0.2218 | 0.386 |
| Jupiter-Rahu Square | Nifty Midcap 150 | 5 | 8 | -0.1319 | 0.2642 | -0.3962 | 62.5 | 0.7675 | 0.8687 |
| Jupiter-Rahu Square | Nifty Midcap 150 | 10 | 8 | 0.5442 | 0.5204 | 0.02375 | 62.5 | 0.992 | 0.9968 |
| Jupiter-Rahu Square | Nifty Midcap 150 | 20 | 8 | 0.4237 | 1.047 | -0.6237 | 62.5 | 0.7399 | 0.8491 |
| Jupiter-Rahu Square | BSE Sensex | 1 | 8 | -0.519 | 0.05036 | -0.5694 | 37.5 | 0.4844 | 0.6622 |
| Jupiter-Rahu Square | BSE Sensex | 3 | 8 | -0.9219 | 0.1513 | -1.073 | 50 | 0.3093 | 0.4871 |
| Jupiter-Rahu Square | BSE Sensex | 5 | 8 | -0.5866 | 0.2506 | -0.8371 | 50 | 0.6045 | 0.7556 |
| Jupiter-Rahu Square | BSE Sensex | 10 | 8 | -0.9576 | 0.4957 | -1.453 | 50 | 0.6131 | 0.7615 |
| Jupiter-Rahu Square | BSE Sensex | 20 | 8 | -0.2368 | 1.002 | -1.238 | 50 | 0.6951 | 0.8194 |
| Jupiter-Rahu Trine | Nifty 50 | 1 | 9 | 0.08193 | 0.04492 | 0.03701 | 66.67 | 0.9471 | 0.979 |
| Jupiter-Rahu Trine | Nifty 50 | 3 | 9 | 2.311 | 0.1333 | 2.177 | 66.67 | 0.0829 | 0.1875 |
| Jupiter-Rahu Trine | Nifty 50 | 5 | 9 | 4.744 | 0.2178 | 4.526 | 77.78 | 0.02299 | 0.07316 |
| Jupiter-Rahu Trine | Nifty 50 | 10 | 9 | 6.297 | 0.4212 | 5.876 | 77.78 | 0.023 | 0.07316 |
| Jupiter-Rahu Trine | Nifty 50 | 20 | 9 | 12.08 | 0.8264 | 11.25 | 77.78 | 0.03871 | 0.1064 |
| Jupiter-Rahu Trine | Nifty Bank | 1 | 9 | 0.6048 | 0.06023 | 0.5446 | 77.78 | 0.5067 | 0.6825 |
| Jupiter-Rahu Trine | Nifty Bank | 3 | 9 | 2.856 | 0.1819 | 2.674 | 77.78 | 0.1135 | 0.2384 |
| Jupiter-Rahu Trine | Nifty Bank | 5 | 9 | 5.002 | 0.3 | 4.702 | 77.78 | 0.04535 | 0.1193 |
| Jupiter-Rahu Trine | Nifty Bank | 10 | 9 | 7.132 | 0.5834 | 6.548 | 66.67 | 0.04986 | 0.128 |
| Jupiter-Rahu Trine | Nifty Bank | 20 | 9 | 10.69 | 1.172 | 9.518 | 77.78 | 0.05237 | 0.1327 |
| Jupiter-Rahu Trine | Nifty Midcap 100 | 1 | 9 | -0.5668 | 0.05397 | -0.6208 | 55.56 | 0.07651 | 0.1768 |
| Jupiter-Rahu Trine | Nifty Midcap 100 | 3 | 9 | -0.1379 | 0.1609 | -0.2988 | 22.22 | 0.3787 | 0.5608 |
| Jupiter-Rahu Trine | Nifty Midcap 100 | 5 | 9 | 0.6893 | 0.266 | 0.4233 | 44.44 | 0.3975 | 0.5805 |
| Jupiter-Rahu Trine | Nifty Midcap 100 | 10 | 9 | 3.208 | 0.532 | 2.676 | 77.78 | 0.04125 | 0.1109 |
| Jupiter-Rahu Trine | Nifty Midcap 100 | 20 | 9 | 2.941 | 1.065 | 1.877 | 77.78 | 0.1367 | 0.2741 |
| Jupiter-Rahu Trine | Nifty Midcap 150 | 1 | 9 | 0.3323 | 0.05323 | 0.279 | 66.67 | 0.6462 | 0.7898 |
| Jupiter-Rahu Trine | Nifty Midcap 150 | 3 | 9 | 0.2164 | 0.1594 | 0.05693 | 66.67 | 0.8918 | 0.9458 |
| Jupiter-Rahu Trine | Nifty Midcap 150 | 5 | 9 | 1.295 | 0.2642 | 1.031 | 88.89 | 0.03857 | 0.1063 |
| Jupiter-Rahu Trine | Nifty Midcap 150 | 10 | 9 | 2.837 | 0.5204 | 2.316 | 77.78 | 0.02555 | 0.07872 |
| Jupiter-Rahu Trine | Nifty Midcap 150 | 20 | 9 | 2.975 | 1.047 | 1.928 | 77.78 | 0.1772 | 0.3312 |
| Jupiter-Rahu Trine | BSE Sensex | 1 | 9 | 0.1044 | 0.05036 | 0.05407 | 55.56 | 0.928 | 0.9699 |
| Jupiter-Rahu Trine | BSE Sensex | 3 | 9 | 0.469 | 0.1513 | 0.3177 | 77.78 | 0.5496 | 0.7161 |
| Jupiter-Rahu Trine | BSE Sensex | 5 | 9 | 1.719 | 0.2506 | 1.468 | 77.78 | 0.05034 | 0.1289 |
| Jupiter-Rahu Trine | BSE Sensex | 10 | 9 | 1.651 | 0.4957 | 1.155 | 55.56 | 0.4507 | 0.6302 |
| Jupiter-Rahu Trine | BSE Sensex | 20 | 9 | 2.188 | 1.002 | 1.187 | 66.67 | 0.5478 | 0.7148 |
| Jupiter-Saturn Opposition | Nifty 50 | 1 | 3 | -0.6628 | 0.04492 | -0.7077 | 33.33 | 0.5829 | 0.7408 |
| Jupiter-Saturn Opposition | Nifty 50 | 3 | 3 | 2.007 | 0.1333 | 1.874 | 100 | 0.04515 | 0.119 |
| Jupiter-Saturn Opposition | Nifty 50 | 5 | 3 | 3.026 | 0.2178 | 2.809 | 100 | 0.02515 | 0.07793 |
| Jupiter-Saturn Opposition | Nifty 50 | 10 | 3 | 1.167 | 0.4212 | 0.7455 | 66.67 | 0.3461 | 0.5256 |
| Jupiter-Saturn Opposition | Nifty 50 | 20 | 3 | 5.656 | 0.8264 | 4.83 | 100 | 0.137 | 0.2745 |
| Jupiter-Saturn Opposition | Nifty Bank | 1 | 3 | -0.4129 | 0.06023 | -0.4732 | 66.67 | 0.7074 | 0.829 |
| Jupiter-Saturn Opposition | Nifty Bank | 3 | 3 | 2.496 | 0.1819 | 2.315 | 100 | 0.09454 | 0.2084 |
| Jupiter-Saturn Opposition | Nifty Bank | 5 | 3 | 3.122 | 0.3 | 2.822 | 100 | 0.01974 | 0.06552 |
| Jupiter-Saturn Opposition | Nifty Bank | 10 | 3 | 1.177 | 0.5834 | 0.5932 | 100 | 0.3877 | 0.5702 |
| Jupiter-Saturn Opposition | Nifty Bank | 20 | 3 | 6.822 | 1.172 | 5.649 | 100 | 0.1984 | 0.3586 |
| Jupiter-Saturn Opposition | Nifty Midcap 100 | 1 | 3 | -0.697 | 0.05397 | -0.751 | 33.33 | 0.5566 | 0.7224 |
| Jupiter-Saturn Opposition | Nifty Midcap 100 | 3 | 3 | 2.112 | 0.1609 | 1.951 | 100 | 0.09572 | 0.2102 |
| Jupiter-Saturn Opposition | Nifty Midcap 100 | 5 | 3 | 2.948 | 0.266 | 2.682 | 100 | 0.1375 | 0.2754 |
| Jupiter-Saturn Opposition | Nifty Midcap 100 | 10 | 3 | 1.422 | 0.532 | 0.8899 | 66.67 | 0.6498 | 0.7929 |
| Jupiter-Saturn Opposition | Nifty Midcap 100 | 20 | 3 | 3.42 | 1.065 | 2.356 | 66.67 | 0.521 | 0.6939 |
| Jupiter-Saturn Opposition | Nifty Midcap 150 | 1 | 3 | -0.6711 | 0.05323 | -0.7244 | 33.33 | 0.5771 | 0.7353 |
| Jupiter-Saturn Opposition | Nifty Midcap 150 | 3 | 3 | 1.902 | 0.1594 | 1.743 | 100 | 0.06937 | 0.1646 |
| Jupiter-Saturn Opposition | Nifty Midcap 150 | 5 | 3 | 3.062 | 0.2642 | 2.798 | 100 | 0.02647 | 0.08069 |
| Jupiter-Saturn Opposition | Nifty Midcap 150 | 10 | 3 | 1.294 | 0.5204 | 0.7733 | 66.67 | 0.3789 | 0.5608 |
| Jupiter-Saturn Opposition | Nifty Midcap 150 | 20 | 3 | 5.616 | 1.047 | 4.568 | 100 | 0.1233 | 0.2544 |
| Jupiter-Saturn Opposition | BSE Sensex | 1 | 3 | -0.5958 | 0.05036 | -0.6461 | 33.33 | 0.6147 | 0.7625 |
| Jupiter-Saturn Opposition | BSE Sensex | 3 | 3 | 2.028 | 0.1513 | 1.877 | 100 | 0.04873 | 0.126 |
| Jupiter-Saturn Opposition | BSE Sensex | 5 | 3 | 2.959 | 0.2506 | 2.708 | 100 | 0.04293 | 0.1143 |
| Jupiter-Saturn Opposition | BSE Sensex | 10 | 3 | 1.158 | 0.4957 | 0.6624 | 66.67 | 0.4056 | 0.5876 |
| Jupiter-Saturn Opposition | BSE Sensex | 20 | 3 | 5.855 | 1.002 | 4.854 | 100 | 0.1407 | 0.2803 |
| Jupiter-Saturn Square | Nifty 50 | 1 | 9 | 0.3672 | 0.04492 | 0.3223 | 66.67 | 0.3043 | 0.4812 |
| Jupiter-Saturn Square | Nifty 50 | 3 | 9 | 2.077 | 0.1333 | 1.944 | 77.78 | 0.06464 | 0.1565 |
| Jupiter-Saturn Square | Nifty 50 | 5 | 9 | 3.837 | 0.2178 | 3.62 | 77.78 | 0.04224 | 0.1128 |
| Jupiter-Saturn Square | Nifty 50 | 10 | 9 | 4.595 | 0.4212 | 4.173 | 66.67 | 0.0839 | 0.1894 |
| Jupiter-Saturn Square | Nifty 50 | 20 | 9 | 8.787 | 0.8264 | 7.96 | 77.78 | 0.1118 | 0.2361 |
| Jupiter-Saturn Square | Nifty Bank | 1 | 9 | 0.8 | 0.06023 | 0.7398 | 77.78 | 0.1547 | 0.3014 |
| Jupiter-Saturn Square | Nifty Bank | 3 | 9 | 2.786 | 0.1819 | 2.604 | 77.78 | 0.04903 | 0.1266 |
| Jupiter-Saturn Square | Nifty Bank | 5 | 9 | 4.243 | 0.3 | 3.943 | 88.89 | 0.04734 | 0.1232 |
| Jupiter-Saturn Square | Nifty Bank | 10 | 9 | 5.476 | 0.5834 | 4.893 | 66.67 | 0.1047 | 0.2244 |
| Jupiter-Saturn Square | Nifty Bank | 20 | 9 | 7.503 | 1.172 | 6.331 | 77.78 | 0.1587 | 0.3074 |
| Jupiter-Saturn Square | Nifty Midcap 100 | 1 | 9 | 0.1828 | 0.05397 | 0.1288 | 77.78 | 0.4586 | 0.6369 |
| Jupiter-Saturn Square | Nifty Midcap 100 | 3 | 9 | 0.04789 | 0.1609 | -0.113 | 44.44 | 0.655 | 0.7938 |
| Jupiter-Saturn Square | Nifty Midcap 100 | 5 | 9 | 0.1949 | 0.266 | -0.07114 | 44.44 | 0.8417 | 0.9146 |
| Jupiter-Saturn Square | Nifty Midcap 100 | 10 | 9 | 1.989 | 0.532 | 1.457 | 55.56 | 0.1553 | 0.3021 |
| Jupiter-Saturn Square | Nifty Midcap 100 | 20 | 9 | 2.399 | 1.065 | 1.335 | 77.78 | 0.2972 | 0.4744 |
| Jupiter-Saturn Square | Nifty Midcap 150 | 1 | 9 | 0.2748 | 0.05323 | 0.2216 | 55.56 | 0.5203 | 0.6937 |
| Jupiter-Saturn Square | Nifty Midcap 150 | 3 | 9 | 0.2937 | 0.1594 | 0.1343 | 55.56 | 0.7084 | 0.8295 |
| Jupiter-Saturn Square | Nifty Midcap 150 | 5 | 9 | 0.4458 | 0.2642 | 0.1816 | 66.67 | 0.7778 | 0.8736 |
| Jupiter-Saturn Square | Nifty Midcap 150 | 10 | 9 | 1.122 | 0.5204 | 0.6012 | 55.56 | 0.4686 | 0.6458 |
| Jupiter-Saturn Square | Nifty Midcap 150 | 20 | 9 | 0.7391 | 1.047 | -0.3084 | 55.56 | 0.8246 | 0.9041 |
| Jupiter-Saturn Square | BSE Sensex | 1 | 9 | 0.2293 | 0.05036 | 0.179 | 55.56 | 0.6027 | 0.7547 |
| Jupiter-Saturn Square | BSE Sensex | 3 | 9 | 0.2214 | 0.1513 | 0.07006 | 55.56 | 0.8387 | 0.9128 |
| Jupiter-Saturn Square | BSE Sensex | 5 | 9 | 0.3912 | 0.2506 | 0.1406 | 55.56 | 0.8323 | 0.9097 |
| Jupiter-Saturn Square | BSE Sensex | 10 | 9 | 1.086 | 0.4957 | 0.5904 | 55.56 | 0.4898 | 0.6681 |
| Jupiter-Saturn Square | BSE Sensex | 20 | 9 | 0.824 | 1.002 | -0.1776 | 66.67 | 0.8988 | 0.9515 |
| Jupiter-Saturn Trine | Nifty 50 | 1 | 10 | -0.5311 | 0.04492 | -0.5761 | 40 | 0.409 | 0.5909 |
| Jupiter-Saturn Trine | Nifty 50 | 3 | 10 | 0.4816 | 0.1333 | 0.3484 | 60 | 0.7613 | 0.8637 |
| Jupiter-Saturn Trine | Nifty 50 | 5 | 10 | 1.161 | 0.2178 | 0.9436 | 60 | 0.5935 | 0.7488 |
| Jupiter-Saturn Trine | Nifty 50 | 10 | 10 | 2.543 | 0.4212 | 2.122 | 70 | 0.3424 | 0.5231 |
| Jupiter-Saturn Trine | Nifty 50 | 20 | 10 | 3.168 | 0.8264 | 2.341 | 70 | 0.6251 | 0.7721 |
| Jupiter-Saturn Trine | Nifty Bank | 1 | 10 | -0.171 | 0.06023 | -0.2312 | 40 | 0.7394 | 0.8491 |
| Jupiter-Saturn Trine | Nifty Bank | 3 | 10 | 1.134 | 0.1819 | 0.9524 | 50 | 0.408 | 0.59 |
| Jupiter-Saturn Trine | Nifty Bank | 5 | 10 | 1.899 | 0.3 | 1.599 | 40 | 0.433 | 0.6156 |
| Jupiter-Saturn Trine | Nifty Bank | 10 | 10 | 2.729 | 0.5834 | 2.146 | 70 | 0.4261 | 0.6078 |
| Jupiter-Saturn Trine | Nifty Bank | 20 | 10 | 2.164 | 1.172 | 0.9912 | 50 | 0.8266 | 0.9052 |
| Jupiter-Saturn Trine | Nifty Midcap 100 | 1 | 10 | -0.3464 | 0.05397 | -0.4004 | 60 | 0.4569 | 0.6349 |
| Jupiter-Saturn Trine | Nifty Midcap 100 | 3 | 10 | -0.1623 | 0.1609 | -0.3232 | 40 | 0.7148 | 0.8343 |
| Jupiter-Saturn Trine | Nifty Midcap 100 | 5 | 10 | -0.09677 | 0.266 | -0.3628 | 50 | 0.8339 | 0.9109 |
| Jupiter-Saturn Trine | Nifty Midcap 100 | 10 | 10 | 1.414 | 0.532 | 0.8825 | 60 | 0.7227 | 0.8394 |
| Jupiter-Saturn Trine | Nifty Midcap 100 | 20 | 10 | -0.4472 | 1.065 | -1.512 | 70 | 0.7326 | 0.8451 |
| Jupiter-Saturn Trine | Nifty Midcap 150 | 1 | 10 | -0.7862 | 0.05323 | -0.8395 | 30 | 0.218 | 0.3835 |
| Jupiter-Saturn Trine | Nifty Midcap 150 | 3 | 10 | -0.2089 | 0.1594 | -0.3683 | 50 | 0.6965 | 0.82 |
| Jupiter-Saturn Trine | Nifty Midcap 150 | 5 | 10 | -0.2381 | 0.2642 | -0.5024 | 60 | 0.6547 | 0.7938 |
| Jupiter-Saturn Trine | Nifty Midcap 150 | 10 | 10 | 0.428 | 0.5204 | -0.09245 | 70 | 0.948 | 0.9796 |
| Jupiter-Saturn Trine | Nifty Midcap 150 | 20 | 10 | -0.7248 | 1.047 | -1.772 | 60 | 0.5703 | 0.7305 |
| Jupiter-Saturn Trine | BSE Sensex | 1 | 10 | -0.7904 | 0.05036 | -0.8408 | 20 | 0.1354 | 0.2728 |
| Jupiter-Saturn Trine | BSE Sensex | 3 | 10 | -0.2459 | 0.1513 | -0.3972 | 50 | 0.6771 | 0.8085 |
| Jupiter-Saturn Trine | BSE Sensex | 5 | 10 | -0.2091 | 0.2506 | -0.4597 | 50 | 0.697 | 0.8201 |
| Jupiter-Saturn Trine | BSE Sensex | 10 | 10 | 0.3521 | 0.4957 | -0.1436 | 60 | 0.9203 | 0.9658 |
| Jupiter-Saturn Trine | BSE Sensex | 20 | 10 | -0.921 | 1.002 | -1.923 | 70 | 0.5398 | 0.7077 |
| Jupiter-Sun Opposition | Nifty 50 | 1 | 24 | 0.09273 | 0.04492 | 0.0478 | 58.33 | 0.8465 | 0.9172 |
| Jupiter-Sun Opposition | Nifty 50 | 3 | 24 | 1.495 | 0.1333 | 1.361 | 62.5 | 0.03664 | 0.1025 |
| Jupiter-Sun Opposition | Nifty 50 | 5 | 24 | 2.671 | 0.2178 | 2.453 | 62.5 | 0.02846 | 0.08543 |
| Jupiter-Sun Opposition | Nifty 50 | 10 | 24 | 4.466 | 0.4212 | 4.044 | 70.83 | 0.004116 | 0.01816 |
| Jupiter-Sun Opposition | Nifty 50 | 20 | 24 | 8.734 | 0.8264 | 7.908 | 79.17 | 0.003688 | 0.01668 |
| Jupiter-Sun Opposition | Nifty Bank | 1 | 24 | 0.5078 | 0.06023 | 0.4476 | 66.67 | 0.1928 | 0.3515 |
| Jupiter-Sun Opposition | Nifty Bank | 3 | 24 | 2.072 | 0.1819 | 1.891 | 70.83 | 0.01949 | 0.065 |
| Jupiter-Sun Opposition | Nifty Bank | 5 | 24 | 3.182 | 0.3 | 2.882 | 70.83 | 0.02536 | 0.07841 |
| Jupiter-Sun Opposition | Nifty Bank | 10 | 24 | 5.679 | 0.5834 | 5.096 | 79.17 | 0.005405 | 0.02275 |
| Jupiter-Sun Opposition | Nifty Bank | 20 | 24 | 8.132 | 1.172 | 6.96 | 83.33 | 0.005964 | 0.02466 |
| Jupiter-Sun Opposition | Nifty Midcap 100 | 1 | 24 | 0.07304 | 0.05397 | 0.01907 | 62.5 | 0.9493 | 0.9798 |
| Jupiter-Sun Opposition | Nifty Midcap 100 | 3 | 24 | -0.4144 | 0.1609 | -0.5753 | 25 | 0.3851 | 0.5677 |
| Jupiter-Sun Opposition | Nifty Midcap 100 | 5 | 24 | -0.4503 | 0.266 | -0.7163 | 29.17 | 0.419 | 0.6006 |
| Jupiter-Sun Opposition | Nifty Midcap 100 | 10 | 24 | 2.237 | 0.532 | 1.705 | 75 | 0.09647 | 0.2111 |
| Jupiter-Sun Opposition | Nifty Midcap 100 | 20 | 24 | 2.32 | 1.065 | 1.256 | 66.67 | 0.2875 | 0.4622 |
| Jupiter-Sun Opposition | Nifty Midcap 150 | 1 | 24 | 0.1059 | 0.05323 | 0.05264 | 58.33 | 0.8437 | 0.916 |
| Jupiter-Sun Opposition | Nifty Midcap 150 | 3 | 24 | -0.005795 | 0.1594 | -0.1652 | 58.33 | 0.5744 | 0.7339 |
| Jupiter-Sun Opposition | Nifty Midcap 150 | 5 | 24 | 0.09332 | 0.2642 | -0.1709 | 58.33 | 0.7342 | 0.8459 |
| Jupiter-Sun Opposition | Nifty Midcap 150 | 10 | 24 | 1.604 | 0.5204 | 1.084 | 70.83 | 0.2056 | 0.3673 |
| Jupiter-Sun Opposition | Nifty Midcap 150 | 20 | 24 | 1.477 | 1.047 | 0.4299 | 75 | 0.7371 | 0.8481 |
| Jupiter-Sun Opposition | BSE Sensex | 1 | 24 | -0.2566 | 0.05036 | -0.307 | 41.67 | 0.1698 | 0.3233 |
| Jupiter-Sun Opposition | BSE Sensex | 3 | 24 | -0.04967 | 0.1513 | -0.201 | 50 | 0.5856 | 0.7432 |
| Jupiter-Sun Opposition | BSE Sensex | 5 | 24 | -0.3506 | 0.2506 | -0.6012 | 50 | 0.3084 | 0.4867 |
| Jupiter-Sun Opposition | BSE Sensex | 10 | 24 | 0.1322 | 0.4957 | -0.3634 | 58.33 | 0.6723 | 0.8068 |
| Jupiter-Sun Opposition | BSE Sensex | 20 | 24 | -0.122 | 1.002 | -1.124 | 50 | 0.353 | 0.533 |
| Jupiter-Sun Square | Nifty 50 | 1 | 49 | 0.4755 | 0.04492 | 0.4306 | 67.35 | 0.0003462 | 0.002575 |
| Jupiter-Sun Square | Nifty 50 | 3 | 49 | 1.829 | 0.1333 | 1.696 | 73.47 | 0.000627 | 0.004061 |
| Jupiter-Sun Square | Nifty 50 | 5 | 49 | 3.407 | 0.2178 | 3.189 | 77.55 | 1.999e-05 | 0.0002829 |
| Jupiter-Sun Square | Nifty 50 | 10 | 49 | 5.001 | 0.4212 | 4.58 | 83.67 | 4.468e-06 | 8.295e-05 |
| Jupiter-Sun Square | Nifty 50 | 20 | 49 | 8.601 | 0.8264 | 7.775 | 73.47 | 7.194e-05 | 0.0007599 |
| Jupiter-Sun Square | Nifty Bank | 1 | 49 | 0.9278 | 0.06023 | 0.8676 | 71.43 | 0.001114 | 0.006448 |
| Jupiter-Sun Square | Nifty Bank | 3 | 49 | 2.297 | 0.1819 | 2.115 | 77.55 | 0.0008981 | 0.005389 |
| Jupiter-Sun Square | Nifty Bank | 5 | 49 | 4.165 | 0.3 | 3.865 | 81.63 | 3.158e-06 | 6.402e-05 |
| Jupiter-Sun Square | Nifty Bank | 10 | 49 | 6.804 | 0.5834 | 6.221 | 83.67 | 2.785e-07 | 8.63e-06 |
| Jupiter-Sun Square | Nifty Bank | 20 | 49 | 8.107 | 1.172 | 6.935 | 73.47 | 6.349e-05 | 0.0006961 |
| Jupiter-Sun Square | Nifty Midcap 100 | 1 | 49 | -0.1788 | 0.05397 | -0.2327 | 65.31 | 0.3711 | 0.5533 |
| Jupiter-Sun Square | Nifty Midcap 100 | 3 | 49 | -0.06193 | 0.1609 | -0.2228 | 36.73 | 0.6406 | 0.7845 |
| Jupiter-Sun Square | Nifty Midcap 100 | 5 | 49 | 0.02408 | 0.266 | -0.2419 | 36.73 | 0.6319 | 0.7778 |
| Jupiter-Sun Square | Nifty Midcap 100 | 10 | 49 | 1.699 | 0.532 | 1.167 | 71.43 | 0.05056 | 0.1293 |
| Jupiter-Sun Square | Nifty Midcap 100 | 20 | 49 | 2.353 | 1.065 | 1.288 | 63.27 | 0.124 | 0.2554 |
| Jupiter-Sun Square | Nifty Midcap 150 | 1 | 49 | 0.5449 | 0.05323 | 0.4917 | 65.31 | 0.0004752 | 0.003325 |
| Jupiter-Sun Square | Nifty Midcap 150 | 3 | 49 | 0.2341 | 0.1594 | 0.07469 | 71.43 | 0.8041 | 0.891 |
| Jupiter-Sun Square | Nifty Midcap 150 | 5 | 49 | 0.8348 | 0.2642 | 0.5706 | 71.43 | 0.06857 | 0.1632 |
| Jupiter-Sun Square | Nifty Midcap 150 | 10 | 49 | 2.708 | 0.5204 | 2.187 | 83.67 | 0.0002168 | 0.00176 |
| Jupiter-Sun Square | Nifty Midcap 150 | 20 | 49 | 2.626 | 1.047 | 1.578 | 77.55 | 0.0416 | 0.1116 |
| Jupiter-Sun Square | BSE Sensex | 1 | 49 | 0.2175 | 0.05036 | 0.1672 | 61.22 | 0.1366 | 0.2741 |
| Jupiter-Sun Square | BSE Sensex | 3 | 49 | 0.2071 | 0.1513 | 0.05575 | 61.22 | 0.8814 | 0.9398 |
| Jupiter-Sun Square | BSE Sensex | 5 | 49 | 0.8184 | 0.2506 | 0.5678 | 71.43 | 0.1287 | 0.2627 |
| Jupiter-Sun Square | BSE Sensex | 10 | 49 | 1.508 | 0.4957 | 1.012 | 73.47 | 0.09009 | 0.2007 |
| Jupiter-Sun Square | BSE Sensex | 20 | 49 | 2.096 | 1.002 | 1.094 | 71.43 | 0.237 | 0.4047 |
| Jupiter-Sun Trine | Nifty 50 | 1 | 48 | 0.3453 | 0.04492 | 0.3003 | 64.58 | 0.03323 | 0.0955 |
| Jupiter-Sun Trine | Nifty 50 | 3 | 48 | 1.946 | 0.1333 | 1.813 | 68.75 | 2.412e-05 | 0.000323 |
| Jupiter-Sun Trine | Nifty 50 | 5 | 48 | 2.903 | 0.2178 | 2.685 | 68.75 | 0.0003138 | 0.002368 |
| Jupiter-Sun Trine | Nifty 50 | 10 | 48 | 3.583 | 0.4212 | 3.162 | 64.58 | 0.002061 | 0.01032 |
| Jupiter-Sun Trine | Nifty 50 | 20 | 48 | 7.276 | 0.8264 | 6.449 | 64.58 | 0.001256 | 0.007102 |
| Jupiter-Sun Trine | Nifty Bank | 1 | 48 | 0.5991 | 0.06023 | 0.5388 | 64.58 | 0.02542 | 0.07842 |
| Jupiter-Sun Trine | Nifty Bank | 3 | 48 | 2.548 | 0.1819 | 2.366 | 66.67 | 2.346e-05 | 0.0003176 |
| Jupiter-Sun Trine | Nifty Bank | 5 | 48 | 3.564 | 0.3 | 3.264 | 72.92 | 0.000198 | 0.001673 |
| Jupiter-Sun Trine | Nifty Bank | 10 | 48 | 4.847 | 0.5834 | 4.263 | 64.58 | 0.0009103 | 0.005427 |
| Jupiter-Sun Trine | Nifty Bank | 20 | 48 | 6.56 | 1.172 | 5.388 | 66.67 | 0.004034 | 0.01786 |
| Jupiter-Sun Trine | Nifty Midcap 100 | 1 | 48 | 0.2536 | 0.05397 | 0.1996 | 72.92 | 0.1682 | 0.3209 |
| Jupiter-Sun Trine | Nifty Midcap 100 | 3 | 48 | 0.6369 | 0.1609 | 0.476 | 45.83 | 0.05109 | 0.1305 |
| Jupiter-Sun Trine | Nifty Midcap 100 | 5 | 48 | 0.2858 | 0.266 | 0.01983 | 39.58 | 0.9556 | 0.982 |
| Jupiter-Sun Trine | Nifty Midcap 100 | 10 | 48 | 1.57 | 0.532 | 1.038 | 72.92 | 0.09974 | 0.2164 |
| Jupiter-Sun Trine | Nifty Midcap 100 | 20 | 48 | 2.171 | 1.065 | 1.106 | 72.92 | 0.2461 | 0.4156 |
| Jupiter-Sun Trine | Nifty Midcap 150 | 1 | 48 | 0.3958 | 0.05323 | 0.3425 | 62.5 | 0.03658 | 0.1025 |
| Jupiter-Sun Trine | Nifty Midcap 150 | 3 | 48 | 0.5066 | 0.1594 | 0.3471 | 72.92 | 0.06422 | 0.1558 |
| Jupiter-Sun Trine | Nifty Midcap 150 | 5 | 48 | 0.5518 | 0.2642 | 0.2876 | 70.83 | 0.3237 | 0.5018 |
| Jupiter-Sun Trine | Nifty Midcap 150 | 10 | 48 | 0.9819 | 0.5204 | 0.4615 | 58.33 | 0.459 | 0.6372 |
| Jupiter-Sun Trine | Nifty Midcap 150 | 20 | 48 | 1.138 | 1.047 | 0.09095 | 62.5 | 0.9078 | 0.9584 |
| Jupiter-Sun Trine | BSE Sensex | 1 | 48 | 0.1664 | 0.05036 | 0.1161 | 54.17 | 0.4385 | 0.6191 |
| Jupiter-Sun Trine | BSE Sensex | 3 | 48 | 0.5248 | 0.1513 | 0.3735 | 60.42 | 0.08012 | 0.1831 |
| Jupiter-Sun Trine | BSE Sensex | 5 | 48 | 0.4261 | 0.2506 | 0.1756 | 62.5 | 0.6273 | 0.7741 |
| Jupiter-Sun Trine | BSE Sensex | 10 | 48 | -0.3195 | 0.4957 | -0.8151 | 52.08 | 0.1957 | 0.3545 |
| Jupiter-Sun Trine | BSE Sensex | 20 | 48 | 0.1275 | 1.002 | -0.8742 | 54.17 | 0.2988 | 0.4752 |
| Jupiter-Venus Opposition | Nifty 50 | 1 | 24 | 0.6444 | 0.04492 | 0.5995 | 75 | 0.00505 | 0.02147 |
| Jupiter-Venus Opposition | Nifty 50 | 3 | 24 | 2.196 | 0.1333 | 2.063 | 75 | 0.0004569 | 0.003215 |
| Jupiter-Venus Opposition | Nifty 50 | 5 | 24 | 3.877 | 0.2178 | 3.66 | 79.17 | 0.0002413 | 0.001913 |
| Jupiter-Venus Opposition | Nifty 50 | 10 | 24 | 4.576 | 0.4212 | 4.155 | 83.33 | 0.001444 | 0.007859 |
| Jupiter-Venus Opposition | Nifty 50 | 20 | 24 | 9.361 | 0.8264 | 8.534 | 87.5 | 0.001279 | 0.007175 |
| Jupiter-Venus Opposition | Nifty Bank | 1 | 24 | 1.236 | 0.06023 | 1.176 | 79.17 | 0.0002303 | 0.001841 |
| Jupiter-Venus Opposition | Nifty Bank | 3 | 24 | 3.356 | 0.1819 | 3.174 | 91.67 | 2.535e-05 | 0.0003346 |
| Jupiter-Venus Opposition | Nifty Bank | 5 | 24 | 5.196 | 0.3 | 4.896 | 91.67 | 1.914e-05 | 0.000275 |
| Jupiter-Venus Opposition | Nifty Bank | 10 | 24 | 6.092 | 0.5834 | 5.508 | 83.33 | 0.0006895 | 0.004383 |
| Jupiter-Venus Opposition | Nifty Bank | 20 | 24 | 8.861 | 1.172 | 7.689 | 79.17 | 0.002153 | 0.01056 |
| Jupiter-Venus Opposition | Nifty Midcap 100 | 1 | 24 | 0.01662 | 0.05397 | -0.03735 | 66.67 | 0.8585 | 0.9246 |
| Jupiter-Venus Opposition | Nifty Midcap 100 | 3 | 24 | 0.5951 | 0.1609 | 0.4343 | 45.83 | 0.2503 | 0.421 |
| Jupiter-Venus Opposition | Nifty Midcap 100 | 5 | 24 | 1.215 | 0.266 | 0.9489 | 50 | 0.05369 | 0.1354 |
| Jupiter-Venus Opposition | Nifty Midcap 100 | 10 | 24 | 2.415 | 0.532 | 1.883 | 87.5 | 0.01306 | 0.04722 |
| Jupiter-Venus Opposition | Nifty Midcap 100 | 20 | 24 | 4.136 | 1.065 | 3.071 | 79.17 | 0.008887 | 0.03427 |
| Jupiter-Venus Opposition | Nifty Midcap 150 | 1 | 24 | 0.5032 | 0.05323 | 0.45 | 66.67 | 0.1874 | 0.3449 |
| Jupiter-Venus Opposition | Nifty Midcap 150 | 3 | 24 | 0.5923 | 0.1594 | 0.4328 | 79.17 | 0.1375 | 0.2754 |
| Jupiter-Venus Opposition | Nifty Midcap 150 | 5 | 24 | 1.007 | 0.2642 | 0.7429 | 70.83 | 0.1775 | 0.3313 |
| Jupiter-Venus Opposition | Nifty Midcap 150 | 10 | 24 | 2.22 | 0.5204 | 1.699 | 83.33 | 0.002568 | 0.01231 |
| Jupiter-Venus Opposition | Nifty Midcap 150 | 20 | 24 | 3.497 | 1.047 | 2.45 | 87.5 | 0.004007 | 0.01778 |
| Jupiter-Venus Opposition | BSE Sensex | 1 | 24 | 0.1648 | 0.05036 | 0.1144 | 58.33 | 0.7277 | 0.8419 |
| Jupiter-Venus Opposition | BSE Sensex | 3 | 24 | 0.5801 | 0.1513 | 0.4288 | 58.33 | 0.1856 | 0.3424 |
| Jupiter-Venus Opposition | BSE Sensex | 5 | 24 | 0.853 | 0.2506 | 0.6024 | 62.5 | 0.3238 | 0.5018 |
| Jupiter-Venus Opposition | BSE Sensex | 10 | 24 | 1.294 | 0.4957 | 0.7979 | 79.17 | 0.1587 | 0.3074 |
| Jupiter-Venus Opposition | BSE Sensex | 20 | 24 | 2.323 | 1.002 | 1.322 | 79.17 | 0.1339 | 0.2706 |
| Jupiter-Venus Square | Nifty 50 | 1 | 55 | 0.3608 | 0.04492 | 0.3159 | 72.73 | 0.02888 | 0.08643 |
| Jupiter-Venus Square | Nifty 50 | 3 | 55 | 1.544 | 0.1333 | 1.411 | 63.64 | 0.002936 | 0.01375 |
| Jupiter-Venus Square | Nifty 50 | 5 | 55 | 3.07 | 0.2178 | 2.852 | 65.45 | 0.0001571 | 0.001396 |
| Jupiter-Venus Square | Nifty 50 | 10 | 55 | 4.236 | 0.4212 | 3.815 | 78.18 | 0.0001167 | 0.001114 |
| Jupiter-Venus Square | Nifty 50 | 20 | 55 | 8.468 | 0.8264 | 7.642 | 74.55 | 0.0001554 | 0.001392 |
| Jupiter-Venus Square | Nifty Bank | 1 | 55 | 0.8487 | 0.06023 | 0.7885 | 65.45 | 0.0004519 | 0.003197 |
| Jupiter-Venus Square | Nifty Bank | 3 | 55 | 2.081 | 0.1819 | 1.9 | 67.27 | 0.001254 | 0.007102 |
| Jupiter-Venus Square | Nifty Bank | 5 | 55 | 3.581 | 0.3 | 3.281 | 67.27 | 0.0001084 | 0.001049 |
| Jupiter-Venus Square | Nifty Bank | 10 | 55 | 5.246 | 0.5834 | 4.663 | 78.18 | 0.0001571 | 0.001396 |
| Jupiter-Venus Square | Nifty Bank | 20 | 55 | 7.024 | 1.172 | 5.852 | 72.73 | 0.00199 | 0.01003 |
| Jupiter-Venus Square | Nifty Midcap 100 | 1 | 55 | -0.1363 | 0.05397 | -0.1903 | 63.64 | 0.2355 | 0.4027 |
| Jupiter-Venus Square | Nifty Midcap 100 | 3 | 55 | -0.3703 | 0.1609 | -0.5311 | 29.09 | 0.05328 | 0.1346 |
| Jupiter-Venus Square | Nifty Midcap 100 | 5 | 55 | -0.4752 | 0.266 | -0.7413 | 32.73 | 0.07454 | 0.1738 |
| Jupiter-Venus Square | Nifty Midcap 100 | 10 | 55 | 1.21 | 0.532 | 0.6778 | 74.55 | 0.2875 | 0.4622 |
| Jupiter-Venus Square | Nifty Midcap 100 | 20 | 55 | 1.255 | 1.065 | 0.1904 | 65.45 | 0.8681 | 0.9317 |
| Jupiter-Venus Square | Nifty Midcap 150 | 1 | 55 | 0.383 | 0.05323 | 0.3298 | 69.09 | 0.06121 | 0.1509 |
| Jupiter-Venus Square | Nifty Midcap 150 | 3 | 55 | -0.1343 | 0.1594 | -0.2938 | 63.64 | 0.2549 | 0.4274 |
| Jupiter-Venus Square | Nifty Midcap 150 | 5 | 55 | 0.4563 | 0.2642 | 0.1921 | 65.45 | 0.5642 | 0.7258 |
| Jupiter-Venus Square | Nifty Midcap 150 | 10 | 55 | 1.588 | 0.5204 | 1.068 | 76.36 | 0.06318 | 0.1544 |
| Jupiter-Venus Square | Nifty Midcap 150 | 20 | 55 | 1.225 | 1.047 | 0.1771 | 69.09 | 0.8519 | 0.9199 |
| Jupiter-Venus Square | BSE Sensex | 1 | 55 | -0.003519 | 0.05036 | -0.05388 | 58.18 | 0.7304 | 0.8436 |
| Jupiter-Venus Square | BSE Sensex | 3 | 55 | -0.1942 | 0.1513 | -0.3455 | 47.27 | 0.2576 | 0.4306 |
| Jupiter-Venus Square | BSE Sensex | 5 | 55 | 0.2104 | 0.2506 | -0.04012 | 54.55 | 0.919 | 0.9648 |
| Jupiter-Venus Square | BSE Sensex | 10 | 55 | 0.415 | 0.4957 | -0.08066 | 67.27 | 0.8832 | 0.9415 |
| Jupiter-Venus Square | BSE Sensex | 20 | 55 | 0.4762 | 1.002 | -0.5255 | 61.82 | 0.6223 | 0.77 |
| Jupiter-Venus Trine | Nifty 50 | 1 | 49 | 0.2437 | 0.04492 | 0.1988 | 59.18 | 0.2128 | 0.3756 |
| Jupiter-Venus Trine | Nifty 50 | 3 | 49 | 1.218 | 0.1333 | 1.085 | 46.94 | 0.02173 | 0.07014 |
| Jupiter-Venus Trine | Nifty 50 | 5 | 49 | 2.837 | 0.2178 | 2.619 | 65.31 | 0.0007121 | 0.0045 |
| Jupiter-Venus Trine | Nifty 50 | 10 | 49 | 3.701 | 0.4212 | 3.28 | 65.31 | 0.001496 | 0.008081 |
| Jupiter-Venus Trine | Nifty 50 | 20 | 49 | 8.354 | 0.8264 | 7.527 | 73.47 | 0.0001277 | 0.0012 |
| Jupiter-Venus Trine | Nifty Bank | 1 | 49 | 0.5575 | 0.06023 | 0.4973 | 65.31 | 0.03037 | 0.08969 |
| Jupiter-Venus Trine | Nifty Bank | 3 | 49 | 1.573 | 0.1819 | 1.391 | 61.22 | 0.0256 | 0.07882 |
| Jupiter-Venus Trine | Nifty Bank | 5 | 49 | 3.089 | 0.3 | 2.789 | 61.22 | 0.001616 | 0.008558 |
| Jupiter-Venus Trine | Nifty Bank | 10 | 49 | 4.565 | 0.5834 | 3.981 | 59.18 | 0.001994 | 0.01004 |
| Jupiter-Venus Trine | Nifty Bank | 20 | 49 | 7.922 | 1.172 | 6.75 | 73.47 | 0.0001296 | 0.001209 |
| Jupiter-Venus Trine | Nifty Midcap 100 | 1 | 49 | -0.1021 | 0.05397 | -0.156 | 65.31 | 0.3477 | 0.5271 |
| Jupiter-Venus Trine | Nifty Midcap 100 | 3 | 49 | -0.6583 | 0.1609 | -0.8192 | 20.41 | 0.003292 | 0.01516 |
| Jupiter-Venus Trine | Nifty Midcap 100 | 5 | 49 | -0.1821 | 0.266 | -0.4481 | 32.65 | 0.1898 | 0.3479 |
| Jupiter-Venus Trine | Nifty Midcap 100 | 10 | 49 | 1.682 | 0.532 | 1.15 | 73.47 | 0.03102 | 0.09078 |
| Jupiter-Venus Trine | Nifty Midcap 100 | 20 | 49 | 2.229 | 1.065 | 1.164 | 69.39 | 0.1105 | 0.234 |
| Jupiter-Venus Trine | Nifty Midcap 150 | 1 | 49 | 0.2695 | 0.05323 | 0.2163 | 53.06 | 0.2207 | 0.3854 |
| Jupiter-Venus Trine | Nifty Midcap 150 | 3 | 49 | -0.3948 | 0.1594 | -0.5543 | 46.94 | 0.00667 | 0.02684 |
| Jupiter-Venus Trine | Nifty Midcap 150 | 5 | 49 | 0.1841 | 0.2642 | -0.08012 | 61.22 | 0.8102 | 0.8947 |
| Jupiter-Venus Trine | Nifty Midcap 150 | 10 | 49 | 1.38 | 0.5204 | 0.8595 | 65.31 | 0.1416 | 0.2816 |
| Jupiter-Venus Trine | Nifty Midcap 150 | 20 | 49 | 1.72 | 1.047 | 0.6726 | 69.39 | 0.3658 | 0.5471 |
| Jupiter-Venus Trine | BSE Sensex | 1 | 49 | -0.1879 | 0.05036 | -0.2383 | 42.86 | 0.1208 | 0.2501 |
| Jupiter-Venus Trine | BSE Sensex | 3 | 49 | -0.7023 | 0.1513 | -0.8536 | 38.78 | 0.0003447 | 0.00257 |
| Jupiter-Venus Trine | BSE Sensex | 5 | 49 | -0.3968 | 0.2506 | -0.6474 | 42.86 | 0.06732 | 0.1609 |
| Jupiter-Venus Trine | BSE Sensex | 10 | 49 | -0.02659 | 0.4957 | -0.5223 | 57.14 | 0.3833 | 0.5656 |
| Jupiter-Venus Trine | BSE Sensex | 20 | 49 | 0.8253 | 1.002 | -0.1764 | 61.22 | 0.832 | 0.9097 |
| Ketu-Mars Opposition | Nifty 50 | 1 | 16 | 0.09786 | 0.04492 | 0.05293 | 62.5 | 0.8615 | 0.9263 |
| Ketu-Mars Opposition | Nifty 50 | 3 | 16 | 1.931 | 0.1333 | 1.798 | 75 | 0.02567 | 0.07891 |
| Ketu-Mars Opposition | Nifty 50 | 5 | 16 | 3.137 | 0.2178 | 2.919 | 68.75 | 0.02918 | 0.08691 |
| Ketu-Mars Opposition | Nifty 50 | 10 | 16 | 3.638 | 0.4212 | 3.217 | 62.5 | 0.08467 | 0.1905 |
| Ketu-Mars Opposition | Nifty 50 | 20 | 16 | 8.276 | 0.8264 | 7.449 | 56.25 | 0.03223 | 0.09348 |
| Ketu-Mars Opposition | Nifty Bank | 1 | 16 | 0.456 | 0.06023 | 0.3958 | 62.5 | 0.4387 | 0.6191 |
| Ketu-Mars Opposition | Nifty Bank | 3 | 16 | 2.101 | 0.1819 | 1.919 | 56.25 | 0.1021 | 0.2199 |
| Ketu-Mars Opposition | Nifty Bank | 5 | 16 | 3.074 | 0.3 | 2.774 | 68.75 | 0.1054 | 0.2251 |
| Ketu-Mars Opposition | Nifty Bank | 10 | 16 | 3.906 | 0.5834 | 3.322 | 62.5 | 0.1903 | 0.3482 |
| Ketu-Mars Opposition | Nifty Bank | 20 | 16 | 6.483 | 1.172 | 5.311 | 56.25 | 0.1004 | 0.2174 |
| Ketu-Mars Opposition | Nifty Midcap 100 | 1 | 16 | -0.429 | 0.05397 | -0.483 | 43.75 | 0.05584 | 0.14 |
| Ketu-Mars Opposition | Nifty Midcap 100 | 3 | 16 | 0.3796 | 0.1609 | 0.2188 | 43.75 | 0.5892 | 0.7459 |
| Ketu-Mars Opposition | Nifty Midcap 100 | 5 | 16 | 0.2327 | 0.266 | -0.03334 | 37.5 | 0.9557 | 0.982 |
| Ketu-Mars Opposition | Nifty Midcap 100 | 10 | 16 | 1.185 | 0.532 | 0.6529 | 50 | 0.5319 | 0.7014 |
| Ketu-Mars Opposition | Nifty Midcap 100 | 20 | 16 | 2.47 | 1.065 | 1.405 | 62.5 | 0.2589 | 0.432 |
| Ketu-Mars Opposition | Nifty Midcap 150 | 1 | 16 | 0.2262 | 0.05323 | 0.173 | 62.5 | 0.6068 | 0.7565 |
| Ketu-Mars Opposition | Nifty Midcap 150 | 3 | 16 | 0.2382 | 0.1594 | 0.07879 | 68.75 | 0.8239 | 0.9036 |
| Ketu-Mars Opposition | Nifty Midcap 150 | 5 | 16 | 0.5239 | 0.2642 | 0.2597 | 75 | 0.5485 | 0.7152 |
| Ketu-Mars Opposition | Nifty Midcap 150 | 10 | 16 | 0.9079 | 0.5204 | 0.3875 | 56.25 | 0.7087 | 0.8295 |
| Ketu-Mars Opposition | Nifty Midcap 150 | 20 | 16 | 1.606 | 1.047 | 0.5589 | 56.25 | 0.5004 | 0.6766 |
| Ketu-Mars Opposition | BSE Sensex | 1 | 16 | 0.03912 | 0.05036 | -0.01124 | 50 | 0.9761 | 0.9901 |
| Ketu-Mars Opposition | BSE Sensex | 3 | 16 | 0.189 | 0.1513 | 0.03773 | 50 | 0.9464 | 0.9787 |
| Ketu-Mars Opposition | BSE Sensex | 5 | 16 | 0.1872 | 0.2506 | -0.06341 | 50 | 0.9246 | 0.9669 |
| Ketu-Mars Opposition | BSE Sensex | 10 | 16 | -0.7123 | 0.4957 | -1.208 | 50 | 0.2024 | 0.3633 |
| Ketu-Mars Opposition | BSE Sensex | 20 | 16 | 0.2786 | 1.002 | -0.7231 | 43.75 | 0.4095 | 0.5909 |
| Ketu-Mars Square | Nifty 50 | 1 | 34 | 0.5677 | 0.04492 | 0.5228 | 73.53 | 0.03571 | 0.1011 |
| Ketu-Mars Square | Nifty 50 | 3 | 34 | 2.592 | 0.1333 | 2.459 | 82.35 | 0.001326 | 0.007332 |
| Ketu-Mars Square | Nifty 50 | 5 | 34 | 3.683 | 0.2178 | 3.465 | 79.41 | 0.000583 | 0.003856 |
| Ketu-Mars Square | Nifty 50 | 10 | 34 | 4.139 | 0.4212 | 3.718 | 67.65 | 0.00195 | 0.009906 |
| Ketu-Mars Square | Nifty 50 | 20 | 34 | 8.322 | 0.8264 | 7.496 | 70.59 | 0.001068 | 0.006238 |
| Ketu-Mars Square | Nifty Bank | 1 | 34 | 0.8389 | 0.06023 | 0.7787 | 70.59 | 0.005867 | 0.02437 |
| Ketu-Mars Square | Nifty Bank | 3 | 34 | 3.145 | 0.1819 | 2.963 | 85.29 | 0.0003659 | 0.00268 |
| Ketu-Mars Square | Nifty Bank | 5 | 34 | 4.121 | 0.3 | 3.821 | 70.59 | 0.00197 | 0.009983 |
| Ketu-Mars Square | Nifty Bank | 10 | 34 | 5.287 | 0.5834 | 4.703 | 67.65 | 0.001259 | 0.007102 |
| Ketu-Mars Square | Nifty Bank | 20 | 34 | 7.315 | 1.172 | 6.142 | 73.53 | 0.00183 | 0.009479 |
| Ketu-Mars Square | Nifty Midcap 100 | 1 | 34 | 0.2577 | 0.05397 | 0.2037 | 70.59 | 0.4557 | 0.6341 |
| Ketu-Mars Square | Nifty Midcap 100 | 3 | 34 | 0.9088 | 0.1609 | 0.7479 | 41.18 | 0.1802 | 0.3345 |
| Ketu-Mars Square | Nifty Midcap 100 | 5 | 34 | 0.7492 | 0.266 | 0.4832 | 44.12 | 0.3938 | 0.5773 |
| Ketu-Mars Square | Nifty Midcap 100 | 10 | 34 | 2.025 | 0.532 | 1.493 | 73.53 | 0.03623 | 0.1019 |
| Ketu-Mars Square | Nifty Midcap 100 | 20 | 34 | 3.379 | 1.065 | 2.314 | 73.53 | 0.04422 | 0.1168 |
| Ketu-Mars Square | Nifty Midcap 150 | 1 | 34 | 0.5066 | 0.05323 | 0.4534 | 67.65 | 0.1026 | 0.2208 |
| Ketu-Mars Square | Nifty Midcap 150 | 3 | 34 | 0.9227 | 0.1594 | 0.7632 | 73.53 | 0.22 | 0.3853 |
| Ketu-Mars Square | Nifty Midcap 150 | 5 | 34 | 1.15 | 0.2642 | 0.8856 | 73.53 | 0.1632 | 0.3146 |
| Ketu-Mars Square | Nifty Midcap 150 | 10 | 34 | 1.944 | 0.5204 | 1.423 | 67.65 | 0.03315 | 0.09549 |
| Ketu-Mars Square | Nifty Midcap 150 | 20 | 34 | 1.698 | 1.047 | 0.6509 | 61.76 | 0.368 | 0.5498 |
| Ketu-Mars Square | BSE Sensex | 1 | 34 | 0.1228 | 0.05036 | 0.07246 | 58.82 | 0.7736 | 0.8721 |
| Ketu-Mars Square | BSE Sensex | 3 | 34 | 0.9623 | 0.1513 | 0.811 | 70.59 | 0.2294 | 0.3955 |
| Ketu-Mars Square | BSE Sensex | 5 | 34 | 0.9129 | 0.2506 | 0.6623 | 58.82 | 0.3331 | 0.512 |
| Ketu-Mars Square | BSE Sensex | 10 | 34 | 0.7965 | 0.4957 | 0.3008 | 64.71 | 0.6402 | 0.7844 |
| Ketu-Mars Square | BSE Sensex | 20 | 34 | 0.7946 | 1.002 | -0.207 | 58.82 | 0.8051 | 0.891 |
| Ketu-Mars Trine | Nifty 50 | 1 | 34 | 0.8019 | 0.04492 | 0.757 | 79.41 | 0.0007154 | 0.004509 |
| Ketu-Mars Trine | Nifty 50 | 3 | 34 | 2.086 | 0.1333 | 1.953 | 67.65 | 0.000774 | 0.004829 |
| Ketu-Mars Trine | Nifty 50 | 5 | 34 | 3.557 | 0.2178 | 3.339 | 79.41 | 0.0002949 | 0.002248 |
| Ketu-Mars Trine | Nifty 50 | 10 | 34 | 4.734 | 0.4212 | 4.313 | 70.59 | 0.0003632 | 0.002671 |
| Ketu-Mars Trine | Nifty 50 | 20 | 34 | 9.823 | 0.8264 | 8.997 | 76.47 | 0.0001488 | 0.001348 |
| Ketu-Mars Trine | Nifty Bank | 1 | 34 | 1.272 | 0.06023 | 1.212 | 79.41 | 0.0001478 | 0.001342 |
| Ketu-Mars Trine | Nifty Bank | 3 | 34 | 3.054 | 0.1819 | 2.872 | 79.41 | 0.0001955 | 0.001658 |
| Ketu-Mars Trine | Nifty Bank | 5 | 34 | 4.35 | 0.3 | 4.05 | 79.41 | 0.0001378 | 0.00126 |
| Ketu-Mars Trine | Nifty Bank | 10 | 34 | 6.611 | 0.5834 | 6.028 | 76.47 | 6.464e-05 | 0.0007006 |
| Ketu-Mars Trine | Nifty Bank | 20 | 34 | 10.09 | 1.172 | 8.918 | 79.41 | 0.0002662 | 0.002075 |
| Ketu-Mars Trine | Nifty Midcap 100 | 1 | 34 | 0.3179 | 0.05397 | 0.2639 | 67.65 | 0.2038 | 0.3653 |
| Ketu-Mars Trine | Nifty Midcap 100 | 3 | 34 | -0.01225 | 0.1609 | -0.1731 | 41.18 | 0.7189 | 0.8364 |
| Ketu-Mars Trine | Nifty Midcap 100 | 5 | 34 | 0.2642 | 0.266 | -0.00185 | 35.29 | 0.9974 | 0.9993 |
| Ketu-Mars Trine | Nifty Midcap 100 | 10 | 34 | 1.391 | 0.532 | 0.8587 | 64.71 | 0.2253 | 0.3899 |
| Ketu-Mars Trine | Nifty Midcap 100 | 20 | 34 | 2.975 | 1.065 | 1.91 | 67.65 | 0.1012 | 0.2185 |
| Ketu-Mars Trine | Nifty Midcap 150 | 1 | 34 | 0.7682 | 0.05323 | 0.715 | 73.53 | 0.006045 | 0.02491 |
| Ketu-Mars Trine | Nifty Midcap 150 | 3 | 34 | 0.5564 | 0.1594 | 0.3969 | 64.71 | 0.2856 | 0.4608 |
| Ketu-Mars Trine | Nifty Midcap 150 | 5 | 34 | 1.045 | 0.2642 | 0.781 | 73.53 | 0.09329 | 0.2062 |
| Ketu-Mars Trine | Nifty Midcap 150 | 10 | 34 | 2.26 | 0.5204 | 1.739 | 67.65 | 0.01974 | 0.06552 |
| Ketu-Mars Trine | Nifty Midcap 150 | 20 | 34 | 3.199 | 1.047 | 2.152 | 70.59 | 0.08197 | 0.1862 |
| Ketu-Mars Trine | BSE Sensex | 1 | 34 | 0.5537 | 0.05036 | 0.5034 | 64.71 | 0.052 | 0.1322 |
| Ketu-Mars Trine | BSE Sensex | 3 | 34 | 0.7501 | 0.1513 | 0.5988 | 55.88 | 0.2114 | 0.3739 |
| Ketu-Mars Trine | BSE Sensex | 5 | 34 | 1.039 | 0.2506 | 0.7885 | 61.76 | 0.1729 | 0.3265 |
| Ketu-Mars Trine | BSE Sensex | 10 | 34 | 1.401 | 0.4957 | 0.9053 | 58.82 | 0.2275 | 0.3931 |
| Ketu-Mars Trine | BSE Sensex | 20 | 34 | 2.649 | 1.002 | 1.647 | 61.76 | 0.1986 | 0.3587 |
| Ketu-Mercury Opposition | Nifty 50 | 1 | 42 | 0.1222 | 0.04492 | 0.07724 | 57.14 | 0.7247 | 0.8398 |
| Ketu-Mercury Opposition | Nifty 50 | 3 | 42 | 1.047 | 0.1333 | 0.9136 | 66.67 | 0.06212 | 0.1525 |
| Ketu-Mercury Opposition | Nifty 50 | 5 | 42 | 1.764 | 0.2178 | 1.546 | 66.67 | 0.03964 | 0.1078 |
| Ketu-Mercury Opposition | Nifty 50 | 10 | 42 | 3.179 | 0.4212 | 2.758 | 73.81 | 0.002954 | 0.01377 |
| Ketu-Mercury Opposition | Nifty 50 | 20 | 42 | 6.156 | 0.8264 | 5.33 | 64.29 | 0.00288 | 0.01357 |
| Ketu-Mercury Opposition | Nifty Bank | 1 | 42 | 0.1976 | 0.06023 | 0.1373 | 66.67 | 0.6531 | 0.7932 |
| Ketu-Mercury Opposition | Nifty Bank | 3 | 42 | 1.233 | 0.1819 | 1.051 | 71.43 | 0.12 | 0.2487 |
| Ketu-Mercury Opposition | Nifty Bank | 5 | 42 | 1.778 | 0.3 | 1.478 | 69.05 | 0.1234 | 0.2544 |
| Ketu-Mercury Opposition | Nifty Bank | 10 | 42 | 3.764 | 0.5834 | 3.181 | 73.81 | 0.008891 | 0.03427 |
| Ketu-Mercury Opposition | Nifty Bank | 20 | 42 | 6.248 | 1.172 | 5.075 | 73.81 | 0.002645 | 0.01262 |
| Ketu-Mercury Opposition | Nifty Midcap 100 | 1 | 42 | 0.05909 | 0.05397 | 0.005129 | 59.52 | 0.9796 | 0.9921 |
| Ketu-Mercury Opposition | Nifty Midcap 100 | 3 | 42 | -0.05087 | 0.1609 | -0.2117 | 45.24 | 0.4657 | 0.6423 |
| Ketu-Mercury Opposition | Nifty Midcap 100 | 5 | 42 | -0.04448 | 0.266 | -0.3105 | 40.48 | 0.4363 | 0.6173 |
| Ketu-Mercury Opposition | Nifty Midcap 100 | 10 | 42 | 1.778 | 0.532 | 1.246 | 64.29 | 0.05216 | 0.1323 |
| Ketu-Mercury Opposition | Nifty Midcap 100 | 20 | 42 | 1.845 | 1.065 | 0.7802 | 64.29 | 0.3993 | 0.5817 |
| Ketu-Mercury Opposition | Nifty Midcap 150 | 1 | 42 | 0.2106 | 0.05323 | 0.1574 | 54.76 | 0.5019 | 0.6773 |
| Ketu-Mercury Opposition | Nifty Midcap 150 | 3 | 42 | 0.1394 | 0.1594 | -0.02006 | 66.67 | 0.9539 | 0.982 |
| Ketu-Mercury Opposition | Nifty Midcap 150 | 5 | 42 | 0.2129 | 0.2642 | -0.05132 | 66.67 | 0.9111 | 0.9595 |
| Ketu-Mercury Opposition | Nifty Midcap 150 | 10 | 42 | 1.848 | 0.5204 | 1.327 | 69.05 | 0.03124 | 0.09108 |
| Ketu-Mercury Opposition | Nifty Midcap 150 | 20 | 42 | 2.165 | 1.047 | 1.117 | 61.9 | 0.1945 | 0.3529 |
| Ketu-Mercury Opposition | BSE Sensex | 1 | 42 | -0.01472 | 0.05036 | -0.06508 | 45.24 | 0.7546 | 0.8588 |
| Ketu-Mercury Opposition | BSE Sensex | 3 | 42 | 0.1385 | 0.1513 | -0.01285 | 64.29 | 0.9718 | 0.9892 |
| Ketu-Mercury Opposition | BSE Sensex | 5 | 42 | -0.0591 | 0.2506 | -0.3097 | 59.52 | 0.5251 | 0.6971 |
| Ketu-Mercury Opposition | BSE Sensex | 10 | 42 | 1.083 | 0.4957 | 0.5869 | 66.67 | 0.3099 | 0.4871 |
| Ketu-Mercury Opposition | BSE Sensex | 20 | 42 | 1.505 | 1.002 | 0.5029 | 54.76 | 0.5841 | 0.7417 |
| Ketu-Mercury Square | Nifty 50 | 1 | 56 | 0.2739 | 0.04492 | 0.229 | 58.93 | 0.1725 | 0.3264 |
| Ketu-Mercury Square | Nifty 50 | 3 | 56 | 1.403 | 0.1333 | 1.27 | 57.14 | 0.005569 | 0.02328 |
| Ketu-Mercury Square | Nifty 50 | 5 | 56 | 2.614 | 0.2178 | 2.397 | 66.07 | 0.0008148 | 0.005034 |
| Ketu-Mercury Square | Nifty 50 | 10 | 56 | 3.43 | 0.4212 | 3.008 | 57.14 | 0.001104 | 0.006408 |
| Ketu-Mercury Square | Nifty 50 | 20 | 56 | 8.79 | 0.8264 | 7.964 | 82.14 | 3.797e-06 | 7.301e-05 |
| Ketu-Mercury Square | Nifty Bank | 1 | 56 | 0.3916 | 0.06023 | 0.3314 | 57.14 | 0.2375 | 0.4052 |
| Ketu-Mercury Square | Nifty Bank | 3 | 56 | 1.695 | 0.1819 | 1.513 | 62.5 | 0.01418 | 0.04989 |
| Ketu-Mercury Square | Nifty Bank | 5 | 56 | 2.715 | 0.3 | 2.415 | 67.86 | 0.004149 | 0.01826 |
| Ketu-Mercury Square | Nifty Bank | 10 | 56 | 3.847 | 0.5834 | 3.263 | 60.71 | 0.006531 | 0.02642 |
| Ketu-Mercury Square | Nifty Bank | 20 | 56 | 7.604 | 1.172 | 6.431 | 78.57 | 4.891e-05 | 0.0005591 |
| Ketu-Mercury Square | Nifty Midcap 100 | 1 | 56 | 0.1925 | 0.05397 | 0.1386 | 66.07 | 0.3825 | 0.5648 |
| Ketu-Mercury Square | Nifty Midcap 100 | 3 | 56 | 0.01197 | 0.1609 | -0.1489 | 41.07 | 0.5969 | 0.7511 |
| Ketu-Mercury Square | Nifty Midcap 100 | 5 | 56 | 0.505 | 0.266 | 0.239 | 42.86 | 0.5283 | 0.6998 |
| Ketu-Mercury Square | Nifty Midcap 100 | 10 | 56 | 2.098 | 0.532 | 1.566 | 76.79 | 0.001651 | 0.008716 |
| Ketu-Mercury Square | Nifty Midcap 100 | 20 | 56 | 3.654 | 1.065 | 2.589 | 75 | 0.0002161 | 0.001759 |
| Ketu-Mercury Square | Nifty Midcap 150 | 1 | 56 | 0.2505 | 0.05323 | 0.1973 | 57.14 | 0.3037 | 0.4806 |
| Ketu-Mercury Square | Nifty Midcap 150 | 3 | 56 | -0.2045 | 0.1594 | -0.3639 | 53.57 | 0.2823 | 0.4582 |
| Ketu-Mercury Square | Nifty Midcap 150 | 5 | 56 | 0.0489 | 0.2642 | -0.2153 | 62.5 | 0.5599 | 0.7248 |
| Ketu-Mercury Square | Nifty Midcap 150 | 10 | 56 | 0.9985 | 0.5204 | 0.4781 | 55.36 | 0.3412 | 0.5216 |
| Ketu-Mercury Square | Nifty Midcap 150 | 20 | 56 | 2.788 | 1.047 | 1.74 | 78.57 | 0.001296 | 0.00723 |
| Ketu-Mercury Square | BSE Sensex | 1 | 56 | -0.149 | 0.05036 | -0.1993 | 44.64 | 0.2981 | 0.4747 |
| Ketu-Mercury Square | BSE Sensex | 3 | 56 | -0.1079 | 0.1513 | -0.2592 | 46.43 | 0.5014 | 0.6771 |
| Ketu-Mercury Square | BSE Sensex | 5 | 56 | -0.171 | 0.2506 | -0.4215 | 46.43 | 0.3436 | 0.5236 |
| Ketu-Mercury Square | BSE Sensex | 10 | 56 | -0.2933 | 0.4957 | -0.7889 | 42.86 | 0.1378 | 0.2755 |
| Ketu-Mercury Square | BSE Sensex | 20 | 56 | 1.493 | 1.002 | 0.4918 | 71.43 | 0.4838 | 0.6622 |
| Ketu-Mercury Trine | Nifty 50 | 1 | 56 | 0.6476 | 0.04492 | 0.6027 | 75 | 1.04e-05 | 0.0001653 |
| Ketu-Mercury Trine | Nifty 50 | 3 | 56 | 2.208 | 0.1333 | 2.075 | 75 | 1.576e-06 | 3.469e-05 |
| Ketu-Mercury Trine | Nifty 50 | 5 | 56 | 3.684 | 0.2178 | 3.466 | 78.57 | 5.384e-07 | 1.413e-05 |
| Ketu-Mercury Trine | Nifty 50 | 10 | 56 | 5.262 | 0.4212 | 4.841 | 82.14 | 9.54e-08 | 3.493e-06 |
| Ketu-Mercury Trine | Nifty 50 | 20 | 56 | 8.531 | 0.8264 | 7.705 | 73.21 | 2.308e-05 | 0.0003149 |
| Ketu-Mercury Trine | Nifty Bank | 1 | 56 | 1.105 | 0.06023 | 1.045 | 76.79 | 7.694e-07 | 1.924e-05 |
| Ketu-Mercury Trine | Nifty Bank | 3 | 56 | 2.843 | 0.1819 | 2.661 | 76.79 | 4.157e-06 | 7.756e-05 |
| Ketu-Mercury Trine | Nifty Bank | 5 | 56 | 4.575 | 0.3 | 4.275 | 82.14 | 9.523e-08 | 3.493e-06 |
| Ketu-Mercury Trine | Nifty Bank | 10 | 56 | 7.348 | 0.5834 | 6.765 | 78.57 | 1.129e-08 | 5.643e-07 |
| Ketu-Mercury Trine | Nifty Bank | 20 | 56 | 8.513 | 1.172 | 7.341 | 75 | 1.18e-05 | 0.0001843 |
| Ketu-Mercury Trine | Nifty Midcap 100 | 1 | 56 | 0.1148 | 0.05397 | 0.06083 | 66.07 | 0.6777 | 0.8088 |
| Ketu-Mercury Trine | Nifty Midcap 100 | 3 | 56 | 0.193 | 0.1609 | 0.03215 | 39.29 | 0.9101 | 0.9595 |
| Ketu-Mercury Trine | Nifty Midcap 100 | 5 | 56 | 0.2188 | 0.266 | -0.04721 | 37.5 | 0.9072 | 0.9583 |
| Ketu-Mercury Trine | Nifty Midcap 100 | 10 | 56 | 1.659 | 0.532 | 1.127 | 67.86 | 0.03674 | 0.1027 |
| Ketu-Mercury Trine | Nifty Midcap 100 | 20 | 56 | 2.269 | 1.065 | 1.204 | 73.21 | 0.262 | 0.4348 |
| Ketu-Mercury Trine | Nifty Midcap 150 | 1 | 56 | 0.736 | 0.05323 | 0.6828 | 71.43 | 3.698e-05 | 0.000443 |
| Ketu-Mercury Trine | Nifty Midcap 150 | 3 | 56 | 0.7871 | 0.1594 | 0.6277 | 73.21 | 0.02007 | 0.06611 |
| Ketu-Mercury Trine | Nifty Midcap 150 | 5 | 56 | 1.391 | 0.2642 | 1.127 | 76.79 | 0.002181 | 0.01068 |
| Ketu-Mercury Trine | Nifty Midcap 150 | 10 | 56 | 2.925 | 0.5204 | 2.404 | 78.57 | 2.808e-05 | 0.000361 |
| Ketu-Mercury Trine | Nifty Midcap 150 | 20 | 56 | 2.404 | 1.047 | 1.356 | 67.86 | 0.09027 | 0.201 |
| Ketu-Mercury Trine | BSE Sensex | 1 | 56 | 0.2867 | 0.05036 | 0.2363 | 55.36 | 0.1516 | 0.2965 |
| Ketu-Mercury Trine | BSE Sensex | 3 | 56 | 0.6286 | 0.1513 | 0.4773 | 57.14 | 0.1014 | 0.2187 |
| Ketu-Mercury Trine | BSE Sensex | 5 | 56 | 0.7018 | 0.2506 | 0.4513 | 58.93 | 0.2797 | 0.4561 |
| Ketu-Mercury Trine | BSE Sensex | 10 | 56 | 1.631 | 0.4957 | 1.136 | 69.64 | 0.04321 | 0.1149 |
| Ketu-Mercury Trine | BSE Sensex | 20 | 56 | 1.544 | 1.002 | 0.5427 | 62.5 | 0.5332 | 0.7018 |
| Ketu-Moon Opposition | Nifty 50 | 1 | 54 | 0.5163 | 0.04492 | 0.4714 | 62.96 | 0.189 | 0.3469 |
| Ketu-Moon Opposition | Nifty 50 | 3 | 54 | 1.823 | 0.1333 | 1.69 | 61.11 | 0.001515 | 0.008128 |
| Ketu-Moon Opposition | Nifty 50 | 5 | 54 | 3.089 | 0.2178 | 2.871 | 68.52 | 0.0002346 | 0.001864 |
| Ketu-Moon Opposition | Nifty 50 | 10 | 54 | 4.534 | 0.4212 | 4.113 | 70.37 | 3.615e-05 | 0.0004359 |
| Ketu-Moon Opposition | Nifty 50 | 20 | 54 | 9.561 | 0.8264 | 8.735 | 79.63 | 1.838e-06 | 3.961e-05 |
| Ketu-Moon Opposition | Nifty Bank | 1 | 54 | 0.6681 | 0.06023 | 0.6079 | 55.56 | 0.1507 | 0.2948 |
| Ketu-Moon Opposition | Nifty Bank | 3 | 54 | 2.217 | 0.1819 | 2.035 | 61.11 | 0.006329 | 0.02577 |
| Ketu-Moon Opposition | Nifty Bank | 5 | 54 | 3.366 | 0.3 | 3.066 | 68.52 | 0.001348 | 0.007413 |
| Ketu-Moon Opposition | Nifty Bank | 10 | 54 | 5.855 | 0.5834 | 5.272 | 77.78 | 2.698e-05 | 0.0003501 |
| Ketu-Moon Opposition | Nifty Bank | 20 | 54 | 9.341 | 1.172 | 8.168 | 79.63 | 4.694e-07 | 1.273e-05 |
| Ketu-Moon Opposition | Nifty Midcap 100 | 1 | 54 | 0.2517 | 0.05397 | 0.1978 | 68.52 | 0.4527 | 0.6318 |
| Ketu-Moon Opposition | Nifty Midcap 100 | 3 | 54 | -0.1034 | 0.1609 | -0.2642 | 37.04 | 0.2778 | 0.4548 |
| Ketu-Moon Opposition | Nifty Midcap 100 | 5 | 54 | -0.1495 | 0.266 | -0.4155 | 40.74 | 0.221 | 0.3854 |
| Ketu-Moon Opposition | Nifty Midcap 100 | 10 | 54 | 1.697 | 0.532 | 1.165 | 68.52 | 0.0446 | 0.1176 |
| Ketu-Moon Opposition | Nifty Midcap 100 | 20 | 54 | 3.087 | 1.065 | 2.022 | 72.22 | 0.02273 | 0.07256 |
| Ketu-Moon Opposition | Nifty Midcap 150 | 1 | 54 | 0.6174 | 0.05323 | 0.5641 | 61.11 | 0.1195 | 0.248 |
| Ketu-Moon Opposition | Nifty Midcap 150 | 3 | 54 | 0.4227 | 0.1594 | 0.2633 | 61.11 | 0.5074 | 0.6827 |
| Ketu-Moon Opposition | Nifty Midcap 150 | 5 | 54 | 0.7504 | 0.2642 | 0.4861 | 66.67 | 0.2911 | 0.466 |
| Ketu-Moon Opposition | Nifty Midcap 150 | 10 | 54 | 2.245 | 0.5204 | 1.725 | 68.52 | 0.008525 | 0.03313 |
| Ketu-Moon Opposition | Nifty Midcap 150 | 20 | 54 | 2.959 | 1.047 | 1.911 | 77.78 | 0.01624 | 0.05605 |
| Ketu-Moon Opposition | BSE Sensex | 1 | 54 | 0.3825 | 0.05036 | 0.3322 | 57.41 | 0.3452 | 0.5249 |
| Ketu-Moon Opposition | BSE Sensex | 3 | 54 | 0.4037 | 0.1513 | 0.2524 | 53.7 | 0.5266 | 0.6983 |
| Ketu-Moon Opposition | BSE Sensex | 5 | 54 | 0.574 | 0.2506 | 0.3234 | 59.26 | 0.4728 | 0.6502 |
| Ketu-Moon Opposition | BSE Sensex | 10 | 54 | 1.365 | 0.4957 | 0.869 | 57.41 | 0.1661 | 0.3178 |
| Ketu-Moon Opposition | BSE Sensex | 20 | 54 | 2.296 | 1.002 | 1.294 | 68.52 | 0.1195 | 0.248 |
| Ketu-Moon Square | Nifty 50 | 1 | 113 | 0.1934 | 0.04492 | 0.1485 | 57.52 | 0.2995 | 0.4757 |
| Ketu-Moon Square | Nifty 50 | 3 | 113 | 1.213 | 0.1333 | 1.08 | 61.06 | 0.0009411 | 0.005549 |
| Ketu-Moon Square | Nifty 50 | 5 | 113 | 2.064 | 0.2178 | 1.846 | 60.18 | 0.0002204 | 0.00177 |
| Ketu-Moon Square | Nifty 50 | 10 | 113 | 2.893 | 0.4212 | 2.472 | 61.95 | 0.0001771 | 0.00153 |
| Ketu-Moon Square | Nifty 50 | 20 | 113 | 6.267 | 0.8264 | 5.441 | 61.95 | 1.078e-05 | 0.0001698 |
| Ketu-Moon Square | Nifty Bank | 1 | 113 | 0.4155 | 0.06023 | 0.3553 | 55.75 | 0.06972 | 0.1653 |
| Ketu-Moon Square | Nifty Bank | 3 | 113 | 1.603 | 0.1819 | 1.421 | 66.37 | 0.0008774 | 0.005307 |
| Ketu-Moon Square | Nifty Bank | 5 | 113 | 2.334 | 0.3 | 2.034 | 61.06 | 0.0005221 | 0.003559 |
| Ketu-Moon Square | Nifty Bank | 10 | 113 | 3.59 | 0.5834 | 3.007 | 61.95 | 0.0002162 | 0.001759 |
| Ketu-Moon Square | Nifty Bank | 20 | 113 | 5.18 | 1.172 | 4.008 | 61.95 | 0.0005855 | 0.003859 |
| Ketu-Moon Square | Nifty Midcap 100 | 1 | 113 | -0.02186 | 0.05397 | -0.07583 | 65.49 | 0.6006 | 0.7527 |
| Ketu-Moon Square | Nifty Midcap 100 | 3 | 113 | 0.01948 | 0.1609 | -0.1414 | 44.25 | 0.6021 | 0.7542 |
| Ketu-Moon Square | Nifty Midcap 100 | 5 | 113 | -0.142 | 0.266 | -0.408 | 38.05 | 0.1726 | 0.3264 |
| Ketu-Moon Square | Nifty Midcap 100 | 10 | 113 | 1.54 | 0.532 | 1.008 | 69.91 | 0.01524 | 0.05296 |
| Ketu-Moon Square | Nifty Midcap 100 | 20 | 113 | 2.136 | 1.065 | 1.071 | 69.91 | 0.07362 | 0.1722 |
| Ketu-Moon Square | Nifty Midcap 150 | 1 | 113 | 0.222 | 0.05323 | 0.1688 | 55.75 | 0.2766 | 0.4534 |
| Ketu-Moon Square | Nifty Midcap 150 | 3 | 113 | -0.04382 | 0.1594 | -0.2033 | 61.95 | 0.3514 | 0.5311 |
| Ketu-Moon Square | Nifty Midcap 150 | 5 | 113 | 0.08407 | 0.2642 | -0.1802 | 59.29 | 0.5178 | 0.691 |
| Ketu-Moon Square | Nifty Midcap 150 | 10 | 113 | 1.06 | 0.5204 | 0.5398 | 59.29 | 0.2086 | 0.3709 |
| Ketu-Moon Square | Nifty Midcap 150 | 20 | 113 | 1.148 | 1.047 | 0.1005 | 62.83 | 0.8564 | 0.9229 |
| Ketu-Moon Square | BSE Sensex | 1 | 113 | -0.0843 | 0.05036 | -0.1347 | 46.02 | 0.379 | 0.5608 |
| Ketu-Moon Square | BSE Sensex | 3 | 113 | -0.132 | 0.1513 | -0.2833 | 49.56 | 0.2441 | 0.4128 |
| Ketu-Moon Square | BSE Sensex | 5 | 113 | -0.183 | 0.2506 | -0.4335 | 50.44 | 0.1365 | 0.2741 |
| Ketu-Moon Square | BSE Sensex | 10 | 113 | 0.114 | 0.4957 | -0.3817 | 54.87 | 0.3598 | 0.5405 |
| Ketu-Moon Square | BSE Sensex | 20 | 113 | 0.6374 | 1.002 | -0.3643 | 55.75 | 0.5345 | 0.7026 |
| Ketu-Moon Trine | Nifty 50 | 1 | 115 | 0.4843 | 0.04492 | 0.4394 | 72.17 | 0.0001556 | 0.001392 |
| Ketu-Moon Trine | Nifty 50 | 3 | 115 | 1.887 | 0.1333 | 1.754 | 71.3 | 6.949e-08 | 2.659e-06 |
| Ketu-Moon Trine | Nifty 50 | 5 | 115 | 3.485 | 0.2178 | 3.267 | 70.43 | 5.94e-10 | 3.713e-08 |
| Ketu-Moon Trine | Nifty 50 | 10 | 115 | 4.564 | 0.4212 | 4.143 | 73.04 | 8.129e-10 | 4.763e-08 |
| Ketu-Moon Trine | Nifty 50 | 20 | 115 | 8.833 | 0.8264 | 8.007 | 80.87 | 2.889e-10 | 1.868e-08 |
| Ketu-Moon Trine | Nifty Bank | 1 | 115 | 0.8999 | 0.06023 | 0.8397 | 66.09 | 4.3e-07 | 1.222e-05 |
| Ketu-Moon Trine | Nifty Bank | 3 | 115 | 2.495 | 0.1819 | 2.313 | 65.22 | 1.472e-08 | 7.262e-07 |
| Ketu-Moon Trine | Nifty Bank | 5 | 115 | 4.137 | 0.3 | 3.837 | 69.57 | 1.963e-09 | 1.078e-07 |
| Ketu-Moon Trine | Nifty Bank | 10 | 115 | 5.841 | 0.5834 | 5.257 | 73.91 | 7.046e-10 | 4.262e-08 |
| Ketu-Moon Trine | Nifty Bank | 20 | 115 | 8.282 | 1.172 | 7.11 | 76.52 | 4.101e-09 | 2.166e-07 |
| Ketu-Moon Trine | Nifty Midcap 100 | 1 | 115 | 0.03295 | 0.05397 | -0.02101 | 72.17 | 0.8775 | 0.9372 |
| Ketu-Moon Trine | Nifty Midcap 100 | 3 | 115 | -0.1257 | 0.1609 | -0.2865 | 35.65 | 0.2036 | 0.3651 |
| Ketu-Moon Trine | Nifty Midcap 100 | 5 | 115 | 0.2643 | 0.266 | -0.00174 | 40.87 | 0.9952 | 0.9976 |
| Ketu-Moon Trine | Nifty Midcap 100 | 10 | 115 | 1.889 | 0.532 | 1.357 | 73.04 | 0.0001273 | 0.001199 |
| Ketu-Moon Trine | Nifty Midcap 100 | 20 | 115 | 2.281 | 1.065 | 1.216 | 70.43 | 0.04652 | 0.1216 |
| Ketu-Moon Trine | Nifty Midcap 150 | 1 | 115 | 0.505 | 0.05323 | 0.4518 | 66.96 | 0.0005733 | 0.003805 |
| Ketu-Moon Trine | Nifty Midcap 150 | 3 | 115 | 0.2981 | 0.1594 | 0.1387 | 67.83 | 0.5038 | 0.6793 |
| Ketu-Moon Trine | Nifty Midcap 150 | 5 | 115 | 0.9546 | 0.2642 | 0.6903 | 68.7 | 0.02795 | 0.08413 |
| Ketu-Moon Trine | Nifty Midcap 150 | 10 | 115 | 2.186 | 0.5204 | 1.665 | 72.17 | 0.0001866 | 0.0016 |
| Ketu-Moon Trine | Nifty Midcap 150 | 20 | 115 | 2.305 | 1.047 | 1.258 | 76.52 | 0.02641 | 0.08058 |
| Ketu-Moon Trine | BSE Sensex | 1 | 115 | 0.05625 | 0.05036 | 0.005893 | 53.04 | 0.9629 | 0.9852 |
| Ketu-Moon Trine | BSE Sensex | 3 | 115 | 0.124 | 0.1513 | -0.02727 | 52.17 | 0.9081 | 0.9584 |
| Ketu-Moon Trine | BSE Sensex | 5 | 115 | 0.6865 | 0.2506 | 0.436 | 58.26 | 0.2087 | 0.371 |
| Ketu-Moon Trine | BSE Sensex | 10 | 115 | 1.04 | 0.4957 | 0.544 | 65.22 | 0.2077 | 0.3696 |
| Ketu-Moon Trine | BSE Sensex | 20 | 115 | 1.386 | 1.002 | 0.3842 | 68.7 | 0.5317 | 0.7014 |
| Ketu-Rahu Opposition | Nifty 50 | 1 | 1 | 1.147 | 0.04492 | 1.102 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty 50 | 3 | 1 | 5.627 | 0.1333 | 5.493 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty 50 | 5 | 1 | 9.735 | 0.2178 | 9.517 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty 50 | 10 | 1 | 12.78 | 0.4212 | 12.36 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty 50 | 20 | 1 | 26.11 | 0.8264 | 25.28 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Bank | 1 | 1 | 2.357 | 0.06023 | 2.297 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Bank | 3 | 1 | 7.149 | 0.1819 | 6.967 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Bank | 5 | 1 | 10.93 | 0.3 | 10.63 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Bank | 10 | 1 | 15.81 | 0.5834 | 15.23 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Bank | 20 | 1 | 22.55 | 1.172 | 21.37 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 100 | 1 | 1 | 0.06997 | 0.05397 | 0.01601 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 100 | 3 | 1 | -0.164 | 0.1609 | -0.3248 | 0 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 100 | 5 | 1 | -0.2908 | 0.266 | -0.5568 | 0 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 100 | 10 | 1 | 4.229 | 0.532 | 3.697 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 100 | 20 | 1 | 5.748 | 1.065 | 4.683 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 150 | 1 | 1 | 1.714 | 0.05323 | 1.661 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 150 | 3 | 1 | 0.5604 | 0.1594 | 0.401 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 150 | 5 | 1 | 1.583 | 0.2642 | 1.319 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 150 | 10 | 1 | 5.639 | 0.5204 | 5.119 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | Nifty Midcap 150 | 20 | 1 | 5.159 | 1.047 | 4.112 | 100 | n/a | n/a |
| Ketu-Rahu Opposition | BSE Sensex | 1 | 1 | -2.441 | 0.05036 | -2.491 | 0 | n/a | n/a |
| Ketu-Rahu Opposition | BSE Sensex | 3 | 1 | -1.394 | 0.1513 | -1.545 | 0 | n/a | n/a |
| Ketu-Rahu Opposition | BSE Sensex | 5 | 1 | -3.546 | 0.2506 | -3.797 | 0 | n/a | n/a |
| Ketu-Rahu Opposition | BSE Sensex | 10 | 1 | -0.4826 | 0.4957 | -0.9783 | 0 | n/a | n/a |
| Ketu-Rahu Opposition | BSE Sensex | 20 | 1 | -5.017 | 1.002 | -6.018 | 0 | n/a | n/a |
| Ketu-Saturn Opposition | Nifty 50 | 1 | 3 | 0.5852 | 0.04492 | 0.5403 | 100 | 0.209 | 0.3711 |
| Ketu-Saturn Opposition | Nifty 50 | 3 | 3 | 2.228 | 0.1333 | 2.095 | 66.67 | 0.4717 | 0.6494 |
| Ketu-Saturn Opposition | Nifty 50 | 5 | 3 | 4.878 | 0.2178 | 4.66 | 100 | 0.2208 | 0.3854 |
| Ketu-Saturn Opposition | Nifty 50 | 10 | 3 | 6.531 | 0.4212 | 6.11 | 100 | 0.1934 | 0.3521 |
| Ketu-Saturn Opposition | Nifty 50 | 20 | 3 | 12.72 | 0.8264 | 11.89 | 100 | 0.2199 | 0.3853 |
| Ketu-Saturn Opposition | Nifty Bank | 1 | 3 | 1.31 | 0.06023 | 1.25 | 100 | 0.1877 | 0.345 |
| Ketu-Saturn Opposition | Nifty Bank | 3 | 3 | 2.71 | 0.1819 | 2.529 | 66.67 | 0.5634 | 0.7258 |
| Ketu-Saturn Opposition | Nifty Bank | 5 | 3 | 6.013 | 0.3 | 5.713 | 100 | 0.1737 | 0.3269 |
| Ketu-Saturn Opposition | Nifty Bank | 10 | 3 | 7.678 | 0.5834 | 7.095 | 100 | 0.2305 | 0.3963 |
| Ketu-Saturn Opposition | Nifty Bank | 20 | 3 | 12.1 | 1.172 | 10.93 | 100 | 0.1736 | 0.3269 |
| Ketu-Saturn Opposition | Nifty Midcap 100 | 1 | 3 | -0.07756 | 0.05397 | -0.1315 | 66.67 | 0.4553 | 0.6341 |
| Ketu-Saturn Opposition | Nifty Midcap 100 | 3 | 3 | 0.7262 | 0.1609 | 0.5653 | 33.33 | 0.6049 | 0.7556 |
| Ketu-Saturn Opposition | Nifty Midcap 100 | 5 | 3 | 2.752 | 0.266 | 2.486 | 66.67 | 0.3334 | 0.512 |
| Ketu-Saturn Opposition | Nifty Midcap 100 | 10 | 3 | 5.628 | 0.532 | 5.096 | 100 | 0.03604 | 0.1015 |
| Ketu-Saturn Opposition | Nifty Midcap 100 | 20 | 3 | 9.488 | 1.065 | 8.423 | 100 | 0.09772 | 0.2129 |
| Ketu-Saturn Opposition | Nifty Midcap 150 | 1 | 3 | 0.7813 | 0.05323 | 0.728 | 100 | 0.2675 | 0.4421 |
| Ketu-Saturn Opposition | Nifty Midcap 150 | 3 | 3 | 0.5901 | 0.1594 | 0.4307 | 66.67 | 0.8133 | 0.8962 |
| Ketu-Saturn Opposition | Nifty Midcap 150 | 5 | 3 | 2.19 | 0.2642 | 1.926 | 100 | 0.2122 | 0.3749 |
| Ketu-Saturn Opposition | Nifty Midcap 150 | 10 | 3 | 4.09 | 0.5204 | 3.57 | 100 | 0.05034 | 0.1289 |
| Ketu-Saturn Opposition | Nifty Midcap 150 | 20 | 3 | 5.61 | 1.047 | 4.562 | 100 | 0.01931 | 0.06459 |
| Ketu-Saturn Opposition | BSE Sensex | 1 | 3 | -0.2274 | 0.05036 | -0.2778 | 66.67 | 0.651 | 0.7932 |
| Ketu-Saturn Opposition | BSE Sensex | 3 | 3 | 1.416 | 0.1513 | 1.265 | 66.67 | 0.576 | 0.7342 |
| Ketu-Saturn Opposition | BSE Sensex | 5 | 3 | 2.076 | 0.2506 | 1.826 | 100 | 0.2759 | 0.453 |
| Ketu-Saturn Opposition | BSE Sensex | 10 | 3 | 2.271 | 0.4957 | 1.776 | 100 | 0.2999 | 0.4757 |
| Ketu-Saturn Opposition | BSE Sensex | 20 | 3 | 4.494 | 1.002 | 3.492 | 100 | 0.1728 | 0.3265 |
| Ketu-Saturn Square | Nifty 50 | 1 | 4 | -0.1036 | 0.04492 | -0.1485 | 25 | 0.7834 | 0.8768 |
| Ketu-Saturn Square | Nifty 50 | 3 | 4 | 0.7296 | 0.1333 | 0.5964 | 25 | 0.7431 | 0.851 |
| Ketu-Saturn Square | Nifty 50 | 5 | 4 | 2.778 | 0.2178 | 2.56 | 75 | 0.3636 | 0.545 |
| Ketu-Saturn Square | Nifty 50 | 10 | 4 | 2.158 | 0.4212 | 1.737 | 50 | 0.6837 | 0.8124 |
| Ketu-Saturn Square | Nifty 50 | 20 | 4 | 4.889 | 0.8264 | 4.063 | 50 | 0.6144 | 0.7624 |
| Ketu-Saturn Square | Nifty Bank | 1 | 4 | 0.01137 | 0.06023 | -0.04886 | 50 | 0.9609 | 0.984 |
| Ketu-Saturn Square | Nifty Bank | 3 | 4 | 1.218 | 0.1819 | 1.036 | 50 | 0.6518 | 0.7932 |
| Ketu-Saturn Square | Nifty Bank | 5 | 4 | 3.274 | 0.3 | 2.974 | 50 | 0.3531 | 0.533 |
| Ketu-Saturn Square | Nifty Bank | 10 | 4 | 2.7 | 0.5834 | 2.116 | 50 | 0.682 | 0.8118 |
| Ketu-Saturn Square | Nifty Bank | 20 | 4 | 4.124 | 1.172 | 2.952 | 50 | 0.6757 | 0.8083 |
| Ketu-Saturn Square | Nifty Midcap 100 | 1 | 4 | -0.1145 | 0.05397 | -0.1685 | 50 | 0.612 | 0.7611 |
| Ketu-Saturn Square | Nifty Midcap 100 | 3 | 4 | -0.7593 | 0.1609 | -0.9201 | 25 | 0.2024 | 0.3633 |
| Ketu-Saturn Square | Nifty Midcap 100 | 5 | 4 | -0.1538 | 0.266 | -0.4198 | 25 | 0.655 | 0.7938 |
| Ketu-Saturn Square | Nifty Midcap 100 | 10 | 4 | -0.09881 | 0.532 | -0.6308 | 50 | 0.7874 | 0.8798 |
| Ketu-Saturn Square | Nifty Midcap 100 | 20 | 4 | -1.339 | 1.065 | -2.404 | 50 | 0.5699 | 0.7302 |
| Ketu-Saturn Square | Nifty Midcap 150 | 1 | 4 | 0.07458 | 0.05323 | 0.02135 | 25 | 0.9739 | 0.9895 |
| Ketu-Saturn Square | Nifty Midcap 150 | 3 | 4 | -0.6049 | 0.1594 | -0.7644 | 25 | 0.2186 | 0.3842 |
| Ketu-Saturn Square | Nifty Midcap 150 | 5 | 4 | 0.8223 | 0.2642 | 0.558 | 75 | 0.4426 | 0.6228 |
| Ketu-Saturn Square | Nifty Midcap 150 | 10 | 4 | 0.5176 | 0.5204 | -0.002799 | 75 | 0.9991 | 0.9997 |
| Ketu-Saturn Square | Nifty Midcap 150 | 20 | 4 | -0.3236 | 1.047 | -1.371 | 50 | 0.6338 | 0.7784 |
| Ketu-Saturn Square | BSE Sensex | 1 | 4 | -0.2991 | 0.05036 | -0.3495 | 25 | 0.3745 | 0.5558 |
| Ketu-Saturn Square | BSE Sensex | 3 | 4 | -0.04818 | 0.1513 | -0.1995 | 25 | 0.8465 | 0.9172 |
| Ketu-Saturn Square | BSE Sensex | 5 | 4 | 1.387 | 0.2506 | 1.136 | 50 | 0.4141 | 0.5961 |
| Ketu-Saturn Square | BSE Sensex | 10 | 4 | 0.1046 | 0.4957 | -0.391 | 50 | 0.8711 | 0.9336 |
| Ketu-Saturn Square | BSE Sensex | 20 | 4 | 0.1688 | 1.002 | -0.8329 | 50 | 0.7906 | 0.8811 |
| Ketu-Saturn Trine | Nifty 50 | 1 | 5 | 1.149 | 0.04492 | 1.104 | 100 | 0.07566 | 0.1757 |
| Ketu-Saturn Trine | Nifty 50 | 3 | 5 | 3.535 | 0.1333 | 3.402 | 100 | 0.02542 | 0.07842 |
| Ketu-Saturn Trine | Nifty 50 | 5 | 5 | 5.09 | 0.2178 | 4.872 | 100 | 0.07421 | 0.1732 |
| Ketu-Saturn Trine | Nifty 50 | 10 | 5 | 7.271 | 0.4212 | 6.85 | 100 | 0.03869 | 0.1064 |
| Ketu-Saturn Trine | Nifty 50 | 20 | 5 | 13.46 | 0.8264 | 12.63 | 100 | 0.07243 | 0.1701 |
| Ketu-Saturn Trine | Nifty Bank | 1 | 5 | 1.711 | 0.06023 | 1.651 | 100 | 0.02056 | 0.06728 |
| Ketu-Saturn Trine | Nifty Bank | 3 | 5 | 3.719 | 0.1819 | 3.538 | 100 | 0.07251 | 0.1702 |
| Ketu-Saturn Trine | Nifty Bank | 5 | 5 | 4.86 | 0.3 | 4.56 | 80 | 0.156 | 0.303 |
| Ketu-Saturn Trine | Nifty Bank | 10 | 5 | 7.143 | 0.5834 | 6.56 | 80 | 0.1487 | 0.292 |
| Ketu-Saturn Trine | Nifty Bank | 20 | 5 | 10.37 | 1.172 | 9.195 | 100 | 0.1392 | 0.2781 |
| Ketu-Saturn Trine | Nifty Midcap 100 | 1 | 5 | 0.7419 | 0.05397 | 0.6879 | 80 | 0.3866 | 0.5691 |
| Ketu-Saturn Trine | Nifty Midcap 100 | 3 | 5 | 1.555 | 0.1609 | 1.394 | 60 | 0.3439 | 0.5239 |
| Ketu-Saturn Trine | Nifty Midcap 100 | 5 | 5 | 0.9932 | 0.266 | 0.7272 | 60 | 0.3876 | 0.5702 |
| Ketu-Saturn Trine | Nifty Midcap 100 | 10 | 5 | 2.979 | 0.532 | 2.447 | 80 | 0.1598 | 0.309 |
| Ketu-Saturn Trine | Nifty Midcap 100 | 20 | 5 | 5.948 | 1.065 | 4.883 | 80 | 0.1486 | 0.292 |
| Ketu-Saturn Trine | Nifty Midcap 150 | 1 | 5 | 1.33 | 0.05323 | 1.277 | 100 | 0.05277 | 0.1334 |
| Ketu-Saturn Trine | Nifty Midcap 150 | 3 | 5 | 1.452 | 0.1594 | 1.293 | 100 | 0.08552 | 0.192 |
| Ketu-Saturn Trine | Nifty Midcap 150 | 5 | 5 | 1.789 | 0.2642 | 1.524 | 100 | 0.1213 | 0.2507 |
| Ketu-Saturn Trine | Nifty Midcap 150 | 10 | 5 | 4.296 | 0.5204 | 3.775 | 100 | 0.003735 | 0.01675 |
| Ketu-Saturn Trine | Nifty Midcap 150 | 20 | 5 | 4.8 | 1.047 | 3.753 | 100 | 0.001408 | 0.007732 |
| Ketu-Saturn Trine | BSE Sensex | 1 | 5 | 2.17 | 0.05036 | 2.119 | 80 | 0.27 | 0.4454 |
| Ketu-Saturn Trine | BSE Sensex | 3 | 5 | 3.002 | 0.1513 | 2.851 | 80 | 0.2024 | 0.3633 |
| Ketu-Saturn Trine | BSE Sensex | 5 | 5 | 4.257 | 0.2506 | 4.006 | 100 | 0.186 | 0.3428 |
| Ketu-Saturn Trine | BSE Sensex | 10 | 5 | 4.207 | 0.4957 | 3.712 | 100 | 0.001166 | 0.006666 |
| Ketu-Saturn Trine | BSE Sensex | 20 | 5 | 3.213 | 1.002 | 2.211 | 80 | 0.3867 | 0.5691 |
| Ketu-Sun Opposition | Nifty 50 | 1 | 28 | 0.3973 | 0.04492 | 0.3524 | 75 | 0.0611 | 0.1507 |
| Ketu-Sun Opposition | Nifty 50 | 3 | 28 | 1.514 | 0.1333 | 1.38 | 67.86 | 0.02618 | 0.08 |
| Ketu-Sun Opposition | Nifty 50 | 5 | 28 | 2.879 | 0.2178 | 2.661 | 71.43 | 0.008166 | 0.03186 |
| Ketu-Sun Opposition | Nifty 50 | 10 | 28 | 3.547 | 0.4212 | 3.126 | 67.86 | 0.02223 | 0.07144 |
| Ketu-Sun Opposition | Nifty 50 | 20 | 28 | 6.976 | 0.8264 | 6.15 | 64.29 | 0.02145 | 0.0694 |
| Ketu-Sun Opposition | Nifty Bank | 1 | 28 | 0.8199 | 0.06023 | 0.7596 | 71.43 | 0.0136 | 0.04866 |
| Ketu-Sun Opposition | Nifty Bank | 3 | 28 | 1.683 | 0.1819 | 1.501 | 60.71 | 0.0671 | 0.1606 |
| Ketu-Sun Opposition | Nifty Bank | 5 | 28 | 2.757 | 0.3 | 2.457 | 60.71 | 0.04552 | 0.1196 |
| Ketu-Sun Opposition | Nifty Bank | 10 | 28 | 3.715 | 0.5834 | 3.132 | 57.14 | 0.08671 | 0.1941 |
| Ketu-Sun Opposition | Nifty Bank | 20 | 28 | 4.898 | 1.172 | 3.725 | 60.71 | 0.1771 | 0.3312 |
| Ketu-Sun Opposition | Nifty Midcap 100 | 1 | 28 | 0.2018 | 0.05397 | 0.1478 | 64.29 | 0.4425 | 0.6228 |
| Ketu-Sun Opposition | Nifty Midcap 100 | 3 | 28 | 0.2713 | 0.1609 | 0.1105 | 39.29 | 0.8151 | 0.897 |
| Ketu-Sun Opposition | Nifty Midcap 100 | 5 | 28 | 0.4431 | 0.266 | 0.1771 | 42.86 | 0.7556 | 0.8594 |
| Ketu-Sun Opposition | Nifty Midcap 100 | 10 | 28 | 1.258 | 0.532 | 0.7264 | 57.14 | 0.2593 | 0.4321 |
| Ketu-Sun Opposition | Nifty Midcap 100 | 20 | 28 | 1.675 | 1.065 | 0.6107 | 53.57 | 0.6033 | 0.7549 |
| Ketu-Sun Opposition | Nifty Midcap 150 | 1 | 28 | 0.6013 | 0.05323 | 0.5481 | 67.86 | 0.0268 | 0.08158 |
| Ketu-Sun Opposition | Nifty Midcap 150 | 3 | 28 | 0.2696 | 0.1594 | 0.1102 | 67.86 | 0.7518 | 0.8574 |
| Ketu-Sun Opposition | Nifty Midcap 150 | 5 | 28 | 0.6559 | 0.2642 | 0.3916 | 71.43 | 0.4065 | 0.5885 |
| Ketu-Sun Opposition | Nifty Midcap 150 | 10 | 28 | 1.319 | 0.5204 | 0.799 | 67.86 | 0.325 | 0.503 |
| Ketu-Sun Opposition | Nifty Midcap 150 | 20 | 28 | 0.9875 | 1.047 | -0.05999 | 64.29 | 0.9576 | 0.9826 |
| Ketu-Sun Opposition | BSE Sensex | 1 | 28 | 0.3079 | 0.05036 | 0.2575 | 57.14 | 0.2614 | 0.4342 |
| Ketu-Sun Opposition | BSE Sensex | 3 | 28 | -0.02223 | 0.1513 | -0.1735 | 57.14 | 0.677 | 0.8085 |
| Ketu-Sun Opposition | BSE Sensex | 5 | 28 | -0.3074 | 0.2506 | -0.558 | 53.57 | 0.3967 | 0.5802 |
| Ketu-Sun Opposition | BSE Sensex | 10 | 28 | -0.9883 | 0.4957 | -1.484 | 46.43 | 0.164 | 0.3154 |
| Ketu-Sun Opposition | BSE Sensex | 20 | 28 | -0.8461 | 1.002 | -1.848 | 50 | 0.1802 | 0.3345 |
| Ketu-Sun Square | Nifty 50 | 1 | 56 | 0.4479 | 0.04492 | 0.403 | 69.64 | 0.03719 | 0.1038 |
| Ketu-Sun Square | Nifty 50 | 3 | 56 | 1.935 | 0.1333 | 1.802 | 64.29 | 9.344e-05 | 0.0009319 |
| Ketu-Sun Square | Nifty 50 | 5 | 56 | 3.147 | 0.2178 | 2.93 | 71.43 | 3.353e-05 | 0.0004136 |
| Ketu-Sun Square | Nifty 50 | 10 | 56 | 3.99 | 0.4212 | 3.568 | 66.07 | 0.0001996 | 0.001677 |
| Ketu-Sun Square | Nifty 50 | 20 | 56 | 8.313 | 0.8264 | 7.487 | 66.07 | 3.295e-05 | 0.0004091 |
| Ketu-Sun Square | Nifty Bank | 1 | 56 | 0.6984 | 0.06023 | 0.6381 | 62.5 | 0.02232 | 0.07152 |
| Ketu-Sun Square | Nifty Bank | 3 | 56 | 2.384 | 0.1819 | 2.202 | 69.64 | 0.0003022 | 0.002289 |
| Ketu-Sun Square | Nifty Bank | 5 | 56 | 3.206 | 0.3 | 2.906 | 67.86 | 0.0005297 | 0.003592 |
| Ketu-Sun Square | Nifty Bank | 10 | 56 | 4.325 | 0.5834 | 3.741 | 66.07 | 0.002268 | 0.011 |
| Ketu-Sun Square | Nifty Bank | 20 | 56 | 6.707 | 1.172 | 5.535 | 60.71 | 0.001926 | 0.009839 |
| Ketu-Sun Square | Nifty Midcap 100 | 1 | 56 | 0.2766 | 0.05397 | 0.2227 | 66.07 | 0.1998 | 0.3603 |
| Ketu-Sun Square | Nifty Midcap 100 | 3 | 56 | 0.6689 | 0.1609 | 0.5081 | 46.43 | 0.1283 | 0.2622 |
| Ketu-Sun Square | Nifty Midcap 100 | 5 | 56 | 1.187 | 0.266 | 0.9208 | 50 | 0.01438 | 0.05035 |
| Ketu-Sun Square | Nifty Midcap 100 | 10 | 56 | 2.401 | 0.532 | 1.869 | 75 | 0.0002011 | 0.00168 |
| Ketu-Sun Square | Nifty Midcap 100 | 20 | 56 | 3.44 | 1.065 | 2.376 | 71.43 | 0.0006696 | 0.004278 |
| Ketu-Sun Square | Nifty Midcap 150 | 1 | 56 | 0.5587 | 0.05323 | 0.5054 | 67.86 | 0.01369 | 0.04882 |
| Ketu-Sun Square | Nifty Midcap 150 | 3 | 56 | 0.5531 | 0.1594 | 0.3937 | 64.29 | 0.1938 | 0.3523 |
| Ketu-Sun Square | Nifty Midcap 150 | 5 | 56 | 0.811 | 0.2642 | 0.5467 | 66.07 | 0.118 | 0.2457 |
| Ketu-Sun Square | Nifty Midcap 150 | 10 | 56 | 1.771 | 0.5204 | 1.25 | 64.29 | 0.04372 | 0.1158 |
| Ketu-Sun Square | Nifty Midcap 150 | 20 | 56 | 2.204 | 1.047 | 1.156 | 66.07 | 0.1278 | 0.2617 |
| Ketu-Sun Square | BSE Sensex | 1 | 56 | 0.181 | 0.05036 | 0.1306 | 53.57 | 0.5104 | 0.6841 |
| Ketu-Sun Square | BSE Sensex | 3 | 56 | 0.5045 | 0.1513 | 0.3532 | 58.93 | 0.3152 | 0.4926 |
| Ketu-Sun Square | BSE Sensex | 5 | 56 | 0.5313 | 0.2506 | 0.2808 | 58.93 | 0.4501 | 0.6298 |
| Ketu-Sun Square | BSE Sensex | 10 | 56 | 0.5958 | 0.4957 | 0.1002 | 53.57 | 0.8687 | 0.9318 |
| Ketu-Sun Square | BSE Sensex | 20 | 56 | 1.151 | 1.002 | 0.1496 | 51.79 | 0.8545 | 0.9213 |
| Ketu-Sun Trine | Nifty 50 | 1 | 56 | 0.2727 | 0.04492 | 0.2277 | 66.07 | 0.234 | 0.4003 |
| Ketu-Sun Trine | Nifty 50 | 3 | 56 | 1.982 | 0.1333 | 1.849 | 69.64 | 8.862e-06 | 0.0001433 |
| Ketu-Sun Trine | Nifty 50 | 5 | 56 | 3.532 | 0.2178 | 3.314 | 75 | 1.437e-06 | 3.267e-05 |
| Ketu-Sun Trine | Nifty 50 | 10 | 56 | 4.821 | 0.4212 | 4.4 | 76.79 | 9.535e-07 | 2.322e-05 |
| Ketu-Sun Trine | Nifty 50 | 20 | 56 | 8.264 | 0.8264 | 7.438 | 67.86 | 3.796e-05 | 0.0004519 |
| Ketu-Sun Trine | Nifty Bank | 1 | 56 | 0.6759 | 0.06023 | 0.6157 | 69.64 | 0.04108 | 0.1108 |
| Ketu-Sun Trine | Nifty Bank | 3 | 56 | 2.616 | 0.1819 | 2.435 | 67.86 | 3.575e-05 | 0.0004338 |
| Ketu-Sun Trine | Nifty Bank | 5 | 56 | 4.227 | 0.3 | 3.927 | 69.64 | 2.964e-06 | 6.106e-05 |
| Ketu-Sun Trine | Nifty Bank | 10 | 56 | 6.545 | 0.5834 | 5.962 | 75 | 2.035e-07 | 6.578e-06 |
| Ketu-Sun Trine | Nifty Bank | 20 | 56 | 8.001 | 1.172 | 6.829 | 71.43 | 2.286e-05 | 0.000314 |
| Ketu-Sun Trine | Nifty Midcap 100 | 1 | 56 | 0.03512 | 0.05397 | -0.01884 | 57.14 | 0.9298 | 0.9709 |
| Ketu-Sun Trine | Nifty Midcap 100 | 3 | 56 | 0.4401 | 0.1609 | 0.2793 | 41.07 | 0.2902 | 0.465 |
| Ketu-Sun Trine | Nifty Midcap 100 | 5 | 56 | 0.275 | 0.266 | 0.008948 | 41.07 | 0.9763 | 0.9901 |
| Ketu-Sun Trine | Nifty Midcap 100 | 10 | 56 | 1.669 | 0.532 | 1.137 | 67.86 | 0.02471 | 0.07709 |
| Ketu-Sun Trine | Nifty Midcap 100 | 20 | 56 | 2.802 | 1.065 | 1.738 | 76.79 | 0.07555 | 0.1756 |
| Ketu-Sun Trine | Nifty Midcap 150 | 1 | 56 | 0.3428 | 0.05323 | 0.2895 | 62.5 | 0.1895 | 0.3477 |
| Ketu-Sun Trine | Nifty Midcap 150 | 3 | 56 | 0.5596 | 0.1594 | 0.4002 | 60.71 | 0.08272 | 0.1872 |
| Ketu-Sun Trine | Nifty Midcap 150 | 5 | 56 | 1.18 | 0.2642 | 0.9155 | 69.64 | 0.007978 | 0.03143 |
| Ketu-Sun Trine | Nifty Midcap 150 | 10 | 56 | 2.487 | 0.5204 | 1.967 | 71.43 | 0.0001741 | 0.001515 |
| Ketu-Sun Trine | Nifty Midcap 150 | 20 | 56 | 2.128 | 1.047 | 1.081 | 67.86 | 0.1485 | 0.292 |
| Ketu-Sun Trine | BSE Sensex | 1 | 56 | -0.1673 | 0.05036 | -0.2177 | 46.43 | 0.2978 | 0.4747 |
| Ketu-Sun Trine | BSE Sensex | 3 | 56 | 0.1672 | 0.1513 | 0.01586 | 50 | 0.9592 | 0.9833 |
| Ketu-Sun Trine | BSE Sensex | 5 | 56 | 0.5594 | 0.2506 | 0.3088 | 60.71 | 0.4524 | 0.6318 |
| Ketu-Sun Trine | BSE Sensex | 10 | 56 | 1.206 | 0.4957 | 0.7106 | 67.86 | 0.2077 | 0.3696 |
| Ketu-Sun Trine | BSE Sensex | 20 | 56 | 1.233 | 1.002 | 0.2309 | 60.71 | 0.8042 | 0.891 |
| Ketu-Venus Opposition | Nifty 50 | 1 | 30 | -0.005244 | 0.04492 | -0.05017 | 53.33 | 0.7956 | 0.8851 |
| Ketu-Venus Opposition | Nifty 50 | 3 | 30 | 0.7642 | 0.1333 | 0.631 | 53.33 | 0.3165 | 0.4937 |
| Ketu-Venus Opposition | Nifty 50 | 5 | 30 | 1.567 | 0.2178 | 1.349 | 50 | 0.1939 | 0.3523 |
| Ketu-Venus Opposition | Nifty 50 | 10 | 30 | 3.353 | 0.4212 | 2.932 | 70 | 0.01931 | 0.06459 |
| Ketu-Venus Opposition | Nifty 50 | 20 | 30 | 6.568 | 0.8264 | 5.741 | 73.33 | 0.01999 | 0.06609 |
| Ketu-Venus Opposition | Nifty Bank | 1 | 30 | 0.3211 | 0.06023 | 0.2609 | 56.67 | 0.4142 | 0.5961 |
| Ketu-Venus Opposition | Nifty Bank | 3 | 30 | 1.118 | 0.1819 | 0.9359 | 60 | 0.2736 | 0.4502 |
| Ketu-Venus Opposition | Nifty Bank | 5 | 30 | 1.924 | 0.3 | 1.624 | 53.33 | 0.1861 | 0.3428 |
| Ketu-Venus Opposition | Nifty Bank | 10 | 30 | 4.431 | 0.5834 | 3.848 | 63.33 | 0.01423 | 0.04996 |
| Ketu-Venus Opposition | Nifty Bank | 20 | 30 | 5.844 | 1.172 | 4.671 | 63.33 | 0.04002 | 0.1085 |
| Ketu-Venus Opposition | Nifty Midcap 100 | 1 | 30 | -0.3858 | 0.05397 | -0.4397 | 56.67 | 0.09092 | 0.202 |
| Ketu-Venus Opposition | Nifty Midcap 100 | 3 | 30 | -0.6843 | 0.1609 | -0.8452 | 33.33 | 0.09698 | 0.2118 |
| Ketu-Venus Opposition | Nifty Midcap 100 | 5 | 30 | -1.225 | 0.266 | -1.492 | 26.67 | 0.02972 | 0.08817 |
| Ketu-Venus Opposition | Nifty Midcap 100 | 10 | 30 | 1.197 | 0.532 | 0.665 | 66.67 | 0.2895 | 0.4643 |
| Ketu-Venus Opposition | Nifty Midcap 100 | 20 | 30 | 1.451 | 1.065 | 0.3859 | 60 | 0.7176 | 0.8361 |
| Ketu-Venus Opposition | Nifty Midcap 150 | 1 | 30 | 0.06029 | 0.05323 | 0.007059 | 46.67 | 0.9747 | 0.9897 |
| Ketu-Venus Opposition | Nifty Midcap 150 | 3 | 30 | -0.4789 | 0.1594 | -0.6383 | 53.33 | 0.07894 | 0.1811 |
| Ketu-Venus Opposition | Nifty Midcap 150 | 5 | 30 | -0.7016 | 0.2642 | -0.9658 | 50 | 0.06261 | 0.1533 |
| Ketu-Venus Opposition | Nifty Midcap 150 | 10 | 30 | 0.5682 | 0.5204 | 0.0478 | 63.33 | 0.9542 | 0.982 |
| Ketu-Venus Opposition | Nifty Midcap 150 | 20 | 30 | -0.06972 | 1.047 | -1.117 | 66.67 | 0.3136 | 0.4908 |
| Ketu-Venus Opposition | BSE Sensex | 1 | 30 | -0.3033 | 0.05036 | -0.3537 | 40 | 0.03536 | 0.1002 |
| Ketu-Venus Opposition | BSE Sensex | 3 | 30 | -0.799 | 0.1513 | -0.9503 | 36.67 | 0.006836 | 0.02736 |
| Ketu-Venus Opposition | BSE Sensex | 5 | 30 | -1.479 | 0.2506 | -1.73 | 26.67 | 0.001279 | 0.007175 |
| Ketu-Venus Opposition | BSE Sensex | 10 | 30 | -0.9126 | 0.4957 | -1.408 | 53.33 | 0.113 | 0.2375 |
| Ketu-Venus Opposition | BSE Sensex | 20 | 30 | -1.362 | 1.002 | -2.363 | 56.67 | 0.05136 | 0.1309 |
| Ketu-Venus Square | Nifty 50 | 1 | 60 | 0.5276 | 0.04492 | 0.4827 | 73.33 | 0.0001539 | 0.001387 |
| Ketu-Venus Square | Nifty 50 | 3 | 60 | 1.723 | 0.1333 | 1.59 | 65 | 0.0002816 | 0.002168 |
| Ketu-Venus Square | Nifty 50 | 5 | 60 | 3.025 | 0.2178 | 2.807 | 70 | 3.384e-05 | 0.0004147 |
| Ketu-Venus Square | Nifty 50 | 10 | 60 | 3.789 | 0.4212 | 3.368 | 68.33 | 0.0002837 | 0.002176 |
| Ketu-Venus Square | Nifty 50 | 20 | 60 | 7.322 | 0.8264 | 6.495 | 63.33 | 0.0005584 | 0.003726 |
| Ketu-Venus Square | Nifty Bank | 1 | 60 | 0.9036 | 0.06023 | 0.8433 | 68.33 | 6.307e-05 | 0.0006955 |
| Ketu-Venus Square | Nifty Bank | 3 | 60 | 2.152 | 0.1819 | 1.97 | 63.33 | 0.0005877 | 0.00386 |
| Ketu-Venus Square | Nifty Bank | 5 | 60 | 3.455 | 0.3 | 3.155 | 70 | 0.000105 | 0.001021 |
| Ketu-Venus Square | Nifty Bank | 10 | 60 | 4.925 | 0.5834 | 4.341 | 65 | 0.0001694 | 0.001484 |
| Ketu-Venus Square | Nifty Bank | 20 | 60 | 6.737 | 1.172 | 5.565 | 68.33 | 0.001126 | 0.006495 |
| Ketu-Venus Square | Nifty Midcap 100 | 1 | 60 | 0.1777 | 0.05397 | 0.1237 | 73.33 | 0.4229 | 0.6044 |
| Ketu-Venus Square | Nifty Midcap 100 | 3 | 60 | 0.0261 | 0.1609 | -0.1348 | 36.67 | 0.723 | 0.8394 |
| Ketu-Venus Square | Nifty Midcap 100 | 5 | 60 | 0.07563 | 0.266 | -0.1904 | 35 | 0.6228 | 0.77 |
| Ketu-Venus Square | Nifty Midcap 100 | 10 | 60 | 1.38 | 0.532 | 0.8485 | 65 | 0.2094 | 0.3711 |
| Ketu-Venus Square | Nifty Midcap 100 | 20 | 60 | 1.87 | 1.065 | 0.8048 | 60 | 0.4276 | 0.609 |
| Ketu-Venus Square | Nifty Midcap 150 | 1 | 60 | 0.6315 | 0.05323 | 0.5783 | 70 | 7.371e-05 | 0.000772 |
| Ketu-Venus Square | Nifty Midcap 150 | 3 | 60 | 0.2125 | 0.1594 | 0.05303 | 66.67 | 0.8369 | 0.9123 |
| Ketu-Venus Square | Nifty Midcap 150 | 5 | 60 | 0.4229 | 0.2642 | 0.1586 | 65 | 0.5809 | 0.7388 |
| Ketu-Venus Square | Nifty Midcap 150 | 10 | 60 | 1.425 | 0.5204 | 0.9041 | 66.67 | 0.09793 | 0.2131 |
| Ketu-Venus Square | Nifty Midcap 150 | 20 | 60 | 1.084 | 1.047 | 0.03621 | 65 | 0.9667 | 0.9869 |
| Ketu-Venus Square | BSE Sensex | 1 | 60 | 0.199 | 0.05036 | 0.1486 | 60 | 0.2809 | 0.4572 |
| Ketu-Venus Square | BSE Sensex | 3 | 60 | 0.1723 | 0.1513 | 0.02097 | 58.33 | 0.9495 | 0.9798 |
| Ketu-Venus Square | BSE Sensex | 5 | 60 | 0.06512 | 0.2506 | -0.1854 | 55 | 0.5919 | 0.7474 |
| Ketu-Venus Square | BSE Sensex | 10 | 60 | -0.1408 | 0.4957 | -0.6364 | 51.67 | 0.218 | 0.3835 |
| Ketu-Venus Square | BSE Sensex | 20 | 60 | -0.4662 | 1.002 | -1.468 | 50 | 0.101 | 0.2181 |
| Ketu-Venus Trine | Nifty 50 | 1 | 60 | 0.1672 | 0.04492 | 0.1223 | 56.67 | 0.5256 | 0.6974 |
| Ketu-Venus Trine | Nifty 50 | 3 | 60 | 1.748 | 0.1333 | 1.614 | 68.33 | 0.0001096 | 0.001057 |
| Ketu-Venus Trine | Nifty 50 | 5 | 60 | 2.942 | 0.2178 | 2.724 | 66.67 | 0.0001148 | 0.001101 |
| Ketu-Venus Trine | Nifty 50 | 10 | 60 | 3.474 | 0.4212 | 3.053 | 66.67 | 0.003354 | 0.01542 |
| Ketu-Venus Trine | Nifty 50 | 20 | 60 | 7.79 | 0.8264 | 6.964 | 66.67 | 5.96e-05 | 0.0006651 |
| Ketu-Venus Trine | Nifty Bank | 1 | 60 | 0.554 | 0.06023 | 0.4938 | 66.67 | 0.09562 | 0.2101 |
| Ketu-Venus Trine | Nifty Bank | 3 | 60 | 2.452 | 0.1819 | 2.27 | 68.33 | 0.0001704 | 0.001486 |
| Ketu-Venus Trine | Nifty Bank | 5 | 60 | 3.363 | 0.3 | 3.063 | 68.33 | 0.0003037 | 0.002296 |
| Ketu-Venus Trine | Nifty Bank | 10 | 60 | 4.562 | 0.5834 | 3.978 | 66.67 | 0.004888 | 0.02085 |
| Ketu-Venus Trine | Nifty Bank | 20 | 60 | 7.017 | 1.172 | 5.845 | 63.33 | 0.001165 | 0.006666 |
| Ketu-Venus Trine | Nifty Midcap 100 | 1 | 60 | 0.0517 | 0.05397 | -0.002267 | 65 | 0.9874 | 0.9953 |
| Ketu-Venus Trine | Nifty Midcap 100 | 3 | 60 | 0.2982 | 0.1609 | 0.1374 | 43.33 | 0.6547 | 0.7938 |
| Ketu-Venus Trine | Nifty Midcap 100 | 5 | 60 | 0.2248 | 0.266 | -0.04123 | 48.33 | 0.9327 | 0.9724 |
| Ketu-Venus Trine | Nifty Midcap 100 | 10 | 60 | 1.585 | 0.532 | 1.053 | 78.33 | 0.1153 | 0.241 |
| Ketu-Venus Trine | Nifty Midcap 100 | 20 | 60 | 2.498 | 1.065 | 1.434 | 65 | 0.1195 | 0.248 |
| Ketu-Venus Trine | Nifty Midcap 150 | 1 | 60 | 0.102 | 0.05323 | 0.04878 | 55 | 0.8362 | 0.9121 |
| Ketu-Venus Trine | Nifty Midcap 150 | 3 | 60 | 0.3927 | 0.1594 | 0.2332 | 66.67 | 0.3809 | 0.5633 |
| Ketu-Venus Trine | Nifty Midcap 150 | 5 | 60 | 0.8065 | 0.2642 | 0.5422 | 70 | 0.1746 | 0.3283 |
| Ketu-Venus Trine | Nifty Midcap 150 | 10 | 60 | 1.402 | 0.5204 | 0.8815 | 61.67 | 0.2471 | 0.4167 |
| Ketu-Venus Trine | Nifty Midcap 150 | 20 | 60 | 2.146 | 1.047 | 1.098 | 65 | 0.1818 | 0.3372 |
| Ketu-Venus Trine | BSE Sensex | 1 | 60 | -0.3664 | 0.05036 | -0.4168 | 33.33 | 0.04159 | 0.1116 |
| Ketu-Venus Trine | BSE Sensex | 3 | 60 | 0.1667 | 0.1513 | 0.01542 | 56.67 | 0.9584 | 0.983 |
| Ketu-Venus Trine | BSE Sensex | 5 | 60 | 0.6763 | 0.2506 | 0.4258 | 63.33 | 0.3397 | 0.5205 |
| Ketu-Venus Trine | BSE Sensex | 10 | 60 | 0.745 | 0.4957 | 0.2494 | 58.33 | 0.7482 | 0.8546 |
| Ketu-Venus Trine | BSE Sensex | 20 | 60 | 1.603 | 1.002 | 0.6011 | 56.67 | 0.524 | 0.6961 |
| Mars-Mercury Opposition | Nifty 50 | 1 | 12 | 0.7418 | 0.04492 | 0.6969 | 75 | 0.02924 | 0.08702 |
| Mars-Mercury Opposition | Nifty 50 | 3 | 12 | 2.022 | 0.1333 | 1.889 | 75 | 0.03435 | 0.09768 |
| Mars-Mercury Opposition | Nifty 50 | 5 | 12 | 3.312 | 0.2178 | 3.095 | 83.33 | 0.03193 | 0.09283 |
| Mars-Mercury Opposition | Nifty 50 | 10 | 12 | 5.047 | 0.4212 | 4.626 | 83.33 | 0.01625 | 0.05605 |
| Mars-Mercury Opposition | Nifty 50 | 20 | 12 | 7.182 | 0.8264 | 6.356 | 66.67 | 0.1355 | 0.2728 |
| Mars-Mercury Opposition | Nifty Bank | 1 | 12 | 1.009 | 0.06023 | 0.9493 | 66.67 | 0.04601 | 0.1206 |
| Mars-Mercury Opposition | Nifty Bank | 3 | 12 | 2.851 | 0.1819 | 2.67 | 83.33 | 0.01554 | 0.05391 |
| Mars-Mercury Opposition | Nifty Bank | 5 | 12 | 4.127 | 0.3 | 3.827 | 83.33 | 0.02461 | 0.07685 |
| Mars-Mercury Opposition | Nifty Bank | 10 | 12 | 7.256 | 0.5834 | 6.673 | 91.67 | 0.007256 | 0.02892 |
| Mars-Mercury Opposition | Nifty Bank | 20 | 12 | 9.156 | 1.172 | 7.983 | 75 | 0.04034 | 0.1091 |
| Mars-Mercury Opposition | Nifty Midcap 100 | 1 | 12 | 0.6378 | 0.05397 | 0.5839 | 91.67 | 0.07289 | 0.171 |
| Mars-Mercury Opposition | Nifty Midcap 100 | 3 | 12 | 0.1846 | 0.1609 | 0.02377 | 41.67 | 0.9695 | 0.9882 |
| Mars-Mercury Opposition | Nifty Midcap 100 | 5 | 12 | 0.3133 | 0.266 | 0.04729 | 41.67 | 0.949 | 0.9798 |
| Mars-Mercury Opposition | Nifty Midcap 100 | 10 | 12 | 1.875 | 0.532 | 1.343 | 58.33 | 0.4206 | 0.6024 |
| Mars-Mercury Opposition | Nifty Midcap 100 | 20 | 12 | -0.5197 | 1.065 | -1.584 | 50 | 0.5987 | 0.7519 |
| Mars-Mercury Opposition | Nifty Midcap 150 | 1 | 12 | 0.8955 | 0.05323 | 0.8423 | 75 | 0.02162 | 0.0699 |
| Mars-Mercury Opposition | Nifty Midcap 150 | 3 | 12 | 0.788 | 0.1594 | 0.6286 | 75 | 0.2215 | 0.386 |
| Mars-Mercury Opposition | Nifty Midcap 150 | 5 | 12 | 1.314 | 0.2642 | 1.05 | 75 | 0.09969 | 0.2164 |
| Mars-Mercury Opposition | Nifty Midcap 150 | 10 | 12 | 3.171 | 0.5204 | 2.651 | 91.67 | 0.02064 | 0.06737 |
| Mars-Mercury Opposition | Nifty Midcap 150 | 20 | 12 | 1.949 | 1.047 | 0.9017 | 66.67 | 0.6987 | 0.8219 |
| Mars-Mercury Opposition | BSE Sensex | 1 | 12 | 0.7586 | 0.05036 | 0.7083 | 75 | 0.03163 | 0.09208 |
| Mars-Mercury Opposition | BSE Sensex | 3 | 12 | 0.6523 | 0.1513 | 0.501 | 58.33 | 0.4557 | 0.6341 |
| Mars-Mercury Opposition | BSE Sensex | 5 | 12 | 0.8308 | 0.2506 | 0.5803 | 58.33 | 0.5494 | 0.7161 |
| Mars-Mercury Opposition | BSE Sensex | 10 | 12 | 2.635 | 0.4957 | 2.14 | 75 | 0.1461 | 0.2886 |
| Mars-Mercury Opposition | BSE Sensex | 20 | 12 | 2.658 | 1.002 | 1.656 | 58.33 | 0.5307 | 0.7014 |
| Mars-Mercury Square | Nifty 50 | 1 | 54 | 0.5675 | 0.04492 | 0.5226 | 72.22 | 0.0001668 | 0.001472 |
| Mars-Mercury Square | Nifty 50 | 3 | 54 | 2.117 | 0.1333 | 1.984 | 64.81 | 1.666e-05 | 0.000245 |
| Mars-Mercury Square | Nifty 50 | 5 | 53 | 3.563 | 0.2178 | 3.346 | 66.04 | 1.831e-05 | 0.0002641 |
| Mars-Mercury Square | Nifty 50 | 10 | 53 | 5.08 | 0.4212 | 4.659 | 73.58 | 3.855e-06 | 7.375e-05 |
| Mars-Mercury Square | Nifty 50 | 20 | 53 | 10.34 | 0.8264 | 9.514 | 79.25 | 1.099e-06 | 2.598e-05 |
| Mars-Mercury Square | Nifty Bank | 1 | 54 | 1.079 | 0.06023 | 1.019 | 74.07 | 1.101e-06 | 2.598e-05 |
| Mars-Mercury Square | Nifty Bank | 3 | 54 | 2.811 | 0.1819 | 2.629 | 70.37 | 3.788e-06 | 7.301e-05 |
| Mars-Mercury Square | Nifty Bank | 5 | 53 | 4.089 | 0.3 | 3.789 | 66.04 | 3.455e-05 | 0.000422 |
| Mars-Mercury Square | Nifty Bank | 10 | 53 | 6.071 | 0.5834 | 5.488 | 73.58 | 2.281e-05 | 0.000314 |
| Mars-Mercury Square | Nifty Bank | 20 | 53 | 9.513 | 1.172 | 8.34 | 77.36 | 2.804e-06 | 5.841e-05 |
| Mars-Mercury Square | Nifty Midcap 100 | 1 | 54 | 0.2957 | 0.05397 | 0.2418 | 74.07 | 0.1062 | 0.2262 |
| Mars-Mercury Square | Nifty Midcap 100 | 3 | 54 | 0.2882 | 0.1609 | 0.1273 | 33.33 | 0.6524 | 0.7932 |
| Mars-Mercury Square | Nifty Midcap 100 | 5 | 53 | 0.4646 | 0.266 | 0.1986 | 41.51 | 0.5921 | 0.7474 |
| Mars-Mercury Square | Nifty Midcap 100 | 10 | 53 | 2.695 | 0.532 | 2.163 | 71.7 | 8.654e-05 | 0.0008771 |
| Mars-Mercury Square | Nifty Midcap 100 | 20 | 53 | 3.553 | 1.065 | 2.488 | 79.25 | 0.001215 | 0.006914 |
| Mars-Mercury Square | Nifty Midcap 150 | 1 | 54 | 0.7471 | 0.05323 | 0.6939 | 75.93 | 1.429e-05 | 0.0002169 |
| Mars-Mercury Square | Nifty Midcap 150 | 3 | 54 | 0.4524 | 0.1594 | 0.2929 | 64.81 | 0.2112 | 0.3739 |
| Mars-Mercury Square | Nifty Midcap 150 | 5 | 53 | 0.6617 | 0.2642 | 0.3975 | 64.15 | 0.2414 | 0.4096 |
| Mars-Mercury Square | Nifty Midcap 150 | 10 | 53 | 2.396 | 0.5204 | 1.876 | 73.58 | 0.0009874 | 0.005813 |
| Mars-Mercury Square | Nifty Midcap 150 | 20 | 53 | 3.072 | 1.047 | 2.025 | 77.36 | 0.004033 | 0.01786 |
| Mars-Mercury Square | BSE Sensex | 1 | 54 | 0.335 | 0.05036 | 0.2847 | 64.81 | 0.03312 | 0.09549 |
| Mars-Mercury Square | BSE Sensex | 3 | 54 | 0.5359 | 0.1513 | 0.3846 | 61.11 | 0.1548 | 0.3015 |
| Mars-Mercury Square | BSE Sensex | 5 | 53 | 0.6515 | 0.2506 | 0.4009 | 56.6 | 0.3273 | 0.5054 |
| Mars-Mercury Square | BSE Sensex | 10 | 53 | 1.128 | 0.4957 | 0.6322 | 60.38 | 0.2629 | 0.436 |
| Mars-Mercury Square | BSE Sensex | 20 | 53 | 1.942 | 1.002 | 0.9401 | 60.38 | 0.3329 | 0.512 |
| Mars-Mercury Trine | Nifty 50 | 1 | 32 | 0.1021 | 0.04492 | 0.05719 | 65.62 | 0.8197 | 0.8998 |
| Mars-Mercury Trine | Nifty 50 | 3 | 32 | 1.404 | 0.1333 | 1.271 | 68.75 | 0.02984 | 0.08846 |
| Mars-Mercury Trine | Nifty 50 | 5 | 32 | 2.704 | 0.2178 | 2.486 | 75 | 0.001686 | 0.008831 |
| Mars-Mercury Trine | Nifty 50 | 10 | 32 | 3.644 | 0.4212 | 3.223 | 78.12 | 0.003653 | 0.01657 |
| Mars-Mercury Trine | Nifty 50 | 20 | 32 | 7.245 | 0.8264 | 6.419 | 75 | 0.00128 | 0.007175 |
| Mars-Mercury Trine | Nifty Bank | 1 | 32 | 0.2877 | 0.06023 | 0.2275 | 65.62 | 0.5646 | 0.7258 |
| Mars-Mercury Trine | Nifty Bank | 3 | 32 | 1.728 | 0.1819 | 1.546 | 65.62 | 0.03771 | 0.1048 |
| Mars-Mercury Trine | Nifty Bank | 5 | 32 | 3.372 | 0.3 | 3.072 | 75 | 0.001138 | 0.006534 |
| Mars-Mercury Trine | Nifty Bank | 10 | 32 | 4.883 | 0.5834 | 4.3 | 78.12 | 0.001506 | 0.008119 |
| Mars-Mercury Trine | Nifty Bank | 20 | 32 | 7.468 | 1.172 | 6.296 | 78.12 | 0.0009016 | 0.0054 |
| Mars-Mercury Trine | Nifty Midcap 100 | 1 | 32 | 0.09245 | 0.05397 | 0.03848 | 62.5 | 0.8302 | 0.9085 |
| Mars-Mercury Trine | Nifty Midcap 100 | 3 | 32 | 0.696 | 0.1609 | 0.5351 | 46.88 | 0.2886 | 0.4633 |
| Mars-Mercury Trine | Nifty Midcap 100 | 5 | 32 | 0.8942 | 0.266 | 0.6282 | 46.88 | 0.3172 | 0.4943 |
| Mars-Mercury Trine | Nifty Midcap 100 | 10 | 32 | 1.719 | 0.532 | 1.187 | 62.5 | 0.1346 | 0.2718 |
| Mars-Mercury Trine | Nifty Midcap 100 | 20 | 32 | 3.061 | 1.065 | 1.996 | 68.75 | 0.1783 | 0.3324 |
| Mars-Mercury Trine | Nifty Midcap 150 | 1 | 32 | 0.1256 | 0.05323 | 0.07237 | 65.62 | 0.7894 | 0.881 |
| Mars-Mercury Trine | Nifty Midcap 150 | 3 | 32 | 0.3551 | 0.1594 | 0.1956 | 65.62 | 0.6558 | 0.7944 |
| Mars-Mercury Trine | Nifty Midcap 150 | 5 | 32 | 1.229 | 0.2642 | 0.9646 | 75 | 0.02241 | 0.07178 |
| Mars-Mercury Trine | Nifty Midcap 150 | 10 | 32 | 2.304 | 0.5204 | 1.783 | 81.25 | 0.01962 | 0.06521 |
| Mars-Mercury Trine | Nifty Midcap 150 | 20 | 32 | 3.361 | 1.047 | 2.313 | 75 | 0.01029 | 0.03874 |
| Mars-Mercury Trine | BSE Sensex | 1 | 32 | -0.02248 | 0.05036 | -0.07284 | 62.5 | 0.7588 | 0.8617 |
| Mars-Mercury Trine | BSE Sensex | 3 | 32 | 0.5787 | 0.1513 | 0.4274 | 62.5 | 0.3536 | 0.5336 |
| Mars-Mercury Trine | BSE Sensex | 5 | 32 | 1.066 | 0.2506 | 0.8149 | 68.75 | 0.1148 | 0.2402 |
| Mars-Mercury Trine | BSE Sensex | 10 | 32 | 1.753 | 0.4957 | 1.257 | 71.88 | 0.07792 | 0.1794 |
| Mars-Mercury Trine | BSE Sensex | 20 | 32 | 2.53 | 1.002 | 1.529 | 68.75 | 0.0825 | 0.187 |
| Mars-Moon Opposition | Nifty 50 | 1 | 50 | 0.2696 | 0.04492 | 0.2247 | 60 | 0.1057 | 0.2255 |
| Mars-Moon Opposition | Nifty 50 | 3 | 50 | 1.487 | 0.1333 | 1.353 | 64 | 0.001682 | 0.008823 |
| Mars-Moon Opposition | Nifty 50 | 5 | 50 | 2.296 | 0.2178 | 2.078 | 68 | 0.003902 | 0.01736 |
| Mars-Moon Opposition | Nifty 50 | 10 | 50 | 2.919 | 0.4212 | 2.498 | 58 | 0.006653 | 0.0268 |
| Mars-Moon Opposition | Nifty 50 | 20 | 50 | 6.749 | 0.8264 | 5.923 | 66 | 0.0008511 | 0.00519 |
| Mars-Moon Opposition | Nifty Bank | 1 | 50 | 0.5437 | 0.06023 | 0.4835 | 60 | 0.01316 | 0.04745 |
| Mars-Moon Opposition | Nifty Bank | 3 | 50 | 1.917 | 0.1819 | 1.735 | 66 | 0.001712 | 0.008955 |
| Mars-Moon Opposition | Nifty Bank | 5 | 50 | 2.443 | 0.3 | 2.143 | 66 | 0.01148 | 0.04268 |
| Mars-Moon Opposition | Nifty Bank | 10 | 50 | 3.268 | 0.5834 | 2.684 | 62 | 0.02988 | 0.08852 |
| Mars-Moon Opposition | Nifty Bank | 20 | 50 | 5.211 | 1.172 | 4.038 | 70 | 0.01912 | 0.06436 |
| Mars-Moon Opposition | Nifty Midcap 100 | 1 | 50 | 0.2077 | 0.05397 | 0.1537 | 64 | 0.4479 | 0.6282 |
| Mars-Moon Opposition | Nifty Midcap 100 | 3 | 50 | 0.1356 | 0.1609 | -0.02524 | 40 | 0.9493 | 0.9798 |
| Mars-Moon Opposition | Nifty Midcap 100 | 5 | 50 | -0.1026 | 0.266 | -0.3686 | 40 | 0.4438 | 0.6243 |
| Mars-Moon Opposition | Nifty Midcap 100 | 10 | 50 | 1.149 | 0.532 | 0.6166 | 56 | 0.2791 | 0.4552 |
| Mars-Moon Opposition | Nifty Midcap 100 | 20 | 50 | 2.757 | 1.065 | 1.692 | 68 | 0.07928 | 0.1816 |
| Mars-Moon Opposition | Nifty Midcap 150 | 1 | 50 | 0.4101 | 0.05323 | 0.3569 | 60 | 0.02683 | 0.08159 |
| Mars-Moon Opposition | Nifty Midcap 150 | 3 | 50 | 0.2769 | 0.1594 | 0.1175 | 64 | 0.6164 | 0.7643 |
| Mars-Moon Opposition | Nifty Midcap 150 | 5 | 50 | 0.3403 | 0.2642 | 0.07608 | 66 | 0.8275 | 0.9058 |
| Mars-Moon Opposition | Nifty Midcap 150 | 10 | 50 | 1.215 | 0.5204 | 0.6947 | 62 | 0.19 | 0.348 |
| Mars-Moon Opposition | Nifty Midcap 150 | 20 | 50 | 1.671 | 1.047 | 0.6239 | 68 | 0.3651 | 0.5465 |
| Mars-Moon Opposition | BSE Sensex | 1 | 50 | -0.2115 | 0.05036 | -0.2619 | 42 | 0.1425 | 0.2831 |
| Mars-Moon Opposition | BSE Sensex | 3 | 50 | -0.01963 | 0.1513 | -0.1709 | 52 | 0.5843 | 0.7417 |
| Mars-Moon Opposition | BSE Sensex | 5 | 50 | 0.04234 | 0.2506 | -0.2082 | 60 | 0.6299 | 0.7766 |
| Mars-Moon Opposition | BSE Sensex | 10 | 50 | -0.116 | 0.4957 | -0.6117 | 46 | 0.2669 | 0.4417 |
| Mars-Moon Opposition | BSE Sensex | 20 | 50 | -0.08223 | 1.002 | -1.084 | 50 | 0.2291 | 0.3953 |
| Mars-Moon Square | Nifty 50 | 1 | 110 | 0.332 | 0.04492 | 0.2871 | 65.45 | 0.002308 | 0.01118 |
| Mars-Moon Square | Nifty 50 | 3 | 110 | 1.606 | 0.1333 | 1.472 | 68.18 | 3.373e-07 | 1.012e-05 |
| Mars-Moon Square | Nifty 50 | 5 | 110 | 2.769 | 0.2178 | 2.551 | 70 | 1.937e-08 | 9.08e-07 |
| Mars-Moon Square | Nifty 50 | 10 | 110 | 3.481 | 0.4212 | 3.06 | 70.91 | 1.319e-06 | 3.046e-05 |
| Mars-Moon Square | Nifty 50 | 20 | 110 | 6.951 | 0.8264 | 6.125 | 68.18 | 4.321e-07 | 1.222e-05 |
| Mars-Moon Square | Nifty Bank | 1 | 110 | 0.5391 | 0.06023 | 0.4789 | 66.36 | 0.002544 | 0.01223 |
| Mars-Moon Square | Nifty Bank | 3 | 110 | 1.992 | 0.1819 | 1.81 | 65.45 | 9.041e-07 | 2.216e-05 |
| Mars-Moon Square | Nifty Bank | 5 | 110 | 3.067 | 0.3 | 2.767 | 70 | 1.015e-07 | 3.626e-06 |
| Mars-Moon Square | Nifty Bank | 10 | 110 | 4.579 | 0.5834 | 3.996 | 74.55 | 7.985e-07 | 1.983e-05 |
| Mars-Moon Square | Nifty Bank | 20 | 110 | 6.722 | 1.172 | 5.55 | 66.36 | 3.937e-06 | 7.456e-05 |
| Mars-Moon Square | Nifty Midcap 100 | 1 | 110 | 0.2188 | 0.05397 | 0.1649 | 65.45 | 0.1585 | 0.3074 |
| Mars-Moon Square | Nifty Midcap 100 | 3 | 110 | 0.08174 | 0.1609 | -0.07912 | 42.73 | 0.7512 | 0.8573 |
| Mars-Moon Square | Nifty Midcap 100 | 5 | 110 | 0.446 | 0.266 | 0.18 | 47.27 | 0.5463 | 0.7143 |
| Mars-Moon Square | Nifty Midcap 100 | 10 | 110 | 0.9134 | 0.532 | 0.3815 | 65.45 | 0.4454 | 0.6253 |
| Mars-Moon Square | Nifty Midcap 100 | 20 | 110 | 1.883 | 1.065 | 0.818 | 60 | 0.2327 | 0.3986 |
| Mars-Moon Square | Nifty Midcap 150 | 1 | 110 | 0.2983 | 0.05323 | 0.2451 | 58.18 | 0.02407 | 0.07574 |
| Mars-Moon Square | Nifty Midcap 150 | 3 | 110 | 0.2939 | 0.1594 | 0.1344 | 61.82 | 0.4447 | 0.6249 |
| Mars-Moon Square | Nifty Midcap 150 | 5 | 110 | 0.659 | 0.2642 | 0.3947 | 65.45 | 0.06758 | 0.1613 |
| Mars-Moon Square | Nifty Midcap 150 | 10 | 110 | 1.295 | 0.5204 | 0.7746 | 67.27 | 0.04961 | 0.1277 |
| Mars-Moon Square | Nifty Midcap 150 | 20 | 110 | 1.681 | 1.047 | 0.6337 | 65.45 | 0.2568 | 0.4297 |
| Mars-Moon Square | BSE Sensex | 1 | 110 | 0.04398 | 0.05036 | -0.006377 | 53.64 | 0.9562 | 0.9821 |
| Mars-Moon Square | BSE Sensex | 3 | 110 | 0.1888 | 0.1513 | 0.03754 | 55.45 | 0.8594 | 0.925 |
| Mars-Moon Square | BSE Sensex | 5 | 110 | 0.3451 | 0.2506 | 0.09448 | 56.36 | 0.7132 | 0.8334 |
| Mars-Moon Square | BSE Sensex | 10 | 110 | 0.05905 | 0.4957 | -0.4366 | 57.27 | 0.3462 | 0.5256 |
| Mars-Moon Square | BSE Sensex | 20 | 110 | 0.4382 | 1.002 | -0.5635 | 51.82 | 0.3717 | 0.5538 |
| Mars-Moon Trine | Nifty 50 | 1 | 100 | 0.06767 | 0.04492 | 0.02275 | 59 | 0.8634 | 0.928 |
| Mars-Moon Trine | Nifty 50 | 3 | 100 | 1.124 | 0.1333 | 0.9906 | 63 | 0.003379 | 0.0155 |
| Mars-Moon Trine | Nifty 50 | 5 | 100 | 2.133 | 0.2178 | 1.916 | 64 | 0.0006546 | 0.00421 |
| Mars-Moon Trine | Nifty 50 | 10 | 100 | 3.115 | 0.4212 | 2.694 | 71 | 0.0005941 | 0.003895 |
| Mars-Moon Trine | Nifty 50 | 20 | 100 | 7.422 | 0.8264 | 6.596 | 72 | 2.912e-07 | 8.951e-06 |
| Mars-Moon Trine | Nifty Bank | 1 | 100 | 0.3707 | 0.06023 | 0.3105 | 55 | 0.1057 | 0.2255 |
| Mars-Moon Trine | Nifty Bank | 3 | 100 | 1.622 | 0.1819 | 1.44 | 68 | 0.0004109 | 0.002946 |
| Mars-Moon Trine | Nifty Bank | 5 | 100 | 2.71 | 0.3 | 2.41 | 66 | 0.000136 | 0.00125 |
| Mars-Moon Trine | Nifty Bank | 10 | 100 | 4.106 | 0.5834 | 3.522 | 75 | 0.0002894 | 0.002211 |
| Mars-Moon Trine | Nifty Bank | 20 | 100 | 7.015 | 1.172 | 5.842 | 71 | 4.365e-07 | 1.222e-05 |
| Mars-Moon Trine | Nifty Midcap 100 | 1 | 100 | -0.1238 | 0.05397 | -0.1778 | 57 | 0.2113 | 0.3739 |
| Mars-Moon Trine | Nifty Midcap 100 | 3 | 100 | -0.3665 | 0.1609 | -0.5274 | 36 | 0.03092 | 0.09059 |
| Mars-Moon Trine | Nifty Midcap 100 | 5 | 100 | -0.5802 | 0.266 | -0.8462 | 39 | 0.01826 | 0.06196 |
| Mars-Moon Trine | Nifty Midcap 100 | 10 | 100 | 1.119 | 0.532 | 0.5865 | 68 | 0.2594 | 0.4321 |
| Mars-Moon Trine | Nifty Midcap 100 | 20 | 100 | 2.337 | 1.065 | 1.272 | 70 | 0.05114 | 0.1306 |
| Mars-Moon Trine | Nifty Midcap 150 | 1 | 100 | 0.1651 | 0.05323 | 0.1119 | 57 | 0.4367 | 0.6173 |
| Mars-Moon Trine | Nifty Midcap 150 | 3 | 100 | -0.1201 | 0.1594 | -0.2795 | 63 | 0.1761 | 0.33 |
| Mars-Moon Trine | Nifty Midcap 150 | 5 | 100 | 0.04442 | 0.2642 | -0.2198 | 61 | 0.496 | 0.6734 |
| Mars-Moon Trine | Nifty Midcap 150 | 10 | 100 | 1.281 | 0.5204 | 0.761 | 73 | 0.18 | 0.3345 |
| Mars-Moon Trine | Nifty Midcap 150 | 20 | 100 | 2.194 | 1.047 | 1.146 | 72 | 0.02916 | 0.08691 |
| Mars-Moon Trine | BSE Sensex | 1 | 100 | -0.2436 | 0.05036 | -0.294 | 46 | 0.0648 | 0.1568 |
| Mars-Moon Trine | BSE Sensex | 3 | 100 | -0.456 | 0.1513 | -0.6073 | 54 | 0.03242 | 0.09387 |
| Mars-Moon Trine | BSE Sensex | 5 | 100 | -0.2938 | 0.2506 | -0.5444 | 54 | 0.1212 | 0.2507 |
| Mars-Moon Trine | BSE Sensex | 10 | 100 | 0.1906 | 0.4957 | -0.3051 | 63 | 0.587 | 0.7447 |
| Mars-Moon Trine | BSE Sensex | 20 | 100 | 1.235 | 1.002 | 0.2337 | 62 | 0.6691 | 0.8046 |
| Mars-Rahu Opposition | Nifty 50 | 1 | 17 | 0.385 | 0.04492 | 0.34 | 64.71 | 0.1496 | 0.293 |
| Mars-Rahu Opposition | Nifty 50 | 3 | 17 | 1.06 | 0.1333 | 0.9263 | 64.71 | 0.2853 | 0.4606 |
| Mars-Rahu Opposition | Nifty 50 | 5 | 17 | 1.476 | 0.2178 | 1.258 | 58.82 | 0.379 | 0.5608 |
| Mars-Rahu Opposition | Nifty 50 | 10 | 17 | 0.584 | 0.4212 | 0.1628 | 47.06 | 0.939 | 0.9749 |
| Mars-Rahu Opposition | Nifty 50 | 20 | 17 | 2.784 | 0.8264 | 1.958 | 52.94 | 0.6312 | 0.7776 |
| Mars-Rahu Opposition | Nifty Bank | 1 | 17 | 0.628 | 0.06023 | 0.5678 | 58.82 | 0.1673 | 0.3195 |
| Mars-Rahu Opposition | Nifty Bank | 3 | 17 | 1.296 | 0.1819 | 1.114 | 58.82 | 0.3631 | 0.5447 |
| Mars-Rahu Opposition | Nifty Bank | 5 | 17 | 1.615 | 0.3 | 1.315 | 58.82 | 0.4647 | 0.6421 |
| Mars-Rahu Opposition | Nifty Bank | 10 | 17 | 0.6765 | 0.5834 | 0.0931 | 47.06 | 0.9732 | 0.9895 |
| Mars-Rahu Opposition | Nifty Bank | 20 | 17 | 1.112 | 1.172 | -0.06029 | 58.82 | 0.989 | 0.9956 |
| Mars-Rahu Opposition | Nifty Midcap 100 | 1 | 17 | 0.086 | 0.05397 | 0.03203 | 64.71 | 0.921 | 0.9658 |
| Mars-Rahu Opposition | Nifty Midcap 100 | 3 | 17 | -0.3672 | 0.1609 | -0.5281 | 41.18 | 0.31 | 0.4871 |
| Mars-Rahu Opposition | Nifty Midcap 100 | 5 | 17 | -0.6499 | 0.266 | -0.9159 | 29.41 | 0.2189 | 0.3844 |
| Mars-Rahu Opposition | Nifty Midcap 100 | 10 | 17 | -0.6829 | 0.532 | -1.215 | 58.82 | 0.4014 | 0.5838 |
| Mars-Rahu Opposition | Nifty Midcap 100 | 20 | 17 | -2.284 | 1.065 | -3.349 | 52.94 | 0.2416 | 0.4097 |
| Mars-Rahu Opposition | Nifty Midcap 150 | 1 | 17 | 0.4115 | 0.05323 | 0.3582 | 58.82 | 0.1695 | 0.3229 |
| Mars-Rahu Opposition | Nifty Midcap 150 | 3 | 17 | -0.1777 | 0.1594 | -0.3372 | 58.82 | 0.5691 | 0.7296 |
| Mars-Rahu Opposition | Nifty Midcap 150 | 5 | 17 | -0.7194 | 0.2642 | -0.9837 | 52.94 | 0.2784 | 0.4549 |
| Mars-Rahu Opposition | Nifty Midcap 150 | 10 | 17 | -1.403 | 0.5204 | -1.924 | 47.06 | 0.2328 | 0.3986 |
| Mars-Rahu Opposition | Nifty Midcap 150 | 20 | 17 | -2.201 | 1.047 | -3.248 | 52.94 | 0.223 | 0.3869 |
| Mars-Rahu Opposition | BSE Sensex | 1 | 17 | -0.1446 | 0.05036 | -0.195 | 52.94 | 0.6171 | 0.7645 |
| Mars-Rahu Opposition | BSE Sensex | 3 | 17 | -0.7562 | 0.1513 | -0.9075 | 47.06 | 0.204 | 0.3653 |
| Mars-Rahu Opposition | BSE Sensex | 5 | 17 | -1.389 | 0.2506 | -1.64 | 41.18 | 0.08399 | 0.1894 |
| Mars-Rahu Opposition | BSE Sensex | 10 | 17 | -2.669 | 0.4957 | -3.165 | 35.29 | 0.04181 | 0.1119 |
| Mars-Rahu Opposition | BSE Sensex | 20 | 17 | -2.897 | 1.002 | -3.899 | 47.06 | 0.1397 | 0.2786 |
| Mars-Rahu Square | Nifty 50 | 1 | 34 | 0.5677 | 0.04492 | 0.5228 | 73.53 | 0.03571 | 0.1011 |
| Mars-Rahu Square | Nifty 50 | 3 | 34 | 2.592 | 0.1333 | 2.459 | 82.35 | 0.001326 | 0.007332 |
| Mars-Rahu Square | Nifty 50 | 5 | 34 | 3.683 | 0.2178 | 3.465 | 79.41 | 0.000583 | 0.003856 |
| Mars-Rahu Square | Nifty 50 | 10 | 34 | 4.139 | 0.4212 | 3.718 | 67.65 | 0.00195 | 0.009906 |
| Mars-Rahu Square | Nifty 50 | 20 | 34 | 8.322 | 0.8264 | 7.496 | 70.59 | 0.001068 | 0.006238 |
| Mars-Rahu Square | Nifty Bank | 1 | 34 | 0.8389 | 0.06023 | 0.7787 | 70.59 | 0.005867 | 0.02437 |
| Mars-Rahu Square | Nifty Bank | 3 | 34 | 3.145 | 0.1819 | 2.963 | 85.29 | 0.0003659 | 0.00268 |
| Mars-Rahu Square | Nifty Bank | 5 | 34 | 4.121 | 0.3 | 3.821 | 70.59 | 0.00197 | 0.009983 |
| Mars-Rahu Square | Nifty Bank | 10 | 34 | 5.287 | 0.5834 | 4.703 | 67.65 | 0.001259 | 0.007102 |
| Mars-Rahu Square | Nifty Bank | 20 | 34 | 7.315 | 1.172 | 6.142 | 73.53 | 0.00183 | 0.009479 |
| Mars-Rahu Square | Nifty Midcap 100 | 1 | 34 | 0.2577 | 0.05397 | 0.2037 | 70.59 | 0.4557 | 0.6341 |
| Mars-Rahu Square | Nifty Midcap 100 | 3 | 34 | 0.9088 | 0.1609 | 0.7479 | 41.18 | 0.1802 | 0.3345 |
| Mars-Rahu Square | Nifty Midcap 100 | 5 | 34 | 0.7492 | 0.266 | 0.4832 | 44.12 | 0.3938 | 0.5773 |
| Mars-Rahu Square | Nifty Midcap 100 | 10 | 34 | 2.025 | 0.532 | 1.493 | 73.53 | 0.03623 | 0.1019 |
| Mars-Rahu Square | Nifty Midcap 100 | 20 | 34 | 3.379 | 1.065 | 2.314 | 73.53 | 0.04422 | 0.1168 |
| Mars-Rahu Square | Nifty Midcap 150 | 1 | 34 | 0.5066 | 0.05323 | 0.4534 | 67.65 | 0.1026 | 0.2208 |
| Mars-Rahu Square | Nifty Midcap 150 | 3 | 34 | 0.9227 | 0.1594 | 0.7632 | 73.53 | 0.22 | 0.3853 |
| Mars-Rahu Square | Nifty Midcap 150 | 5 | 34 | 1.15 | 0.2642 | 0.8856 | 73.53 | 0.1632 | 0.3146 |
| Mars-Rahu Square | Nifty Midcap 150 | 10 | 34 | 1.944 | 0.5204 | 1.423 | 67.65 | 0.03315 | 0.09549 |
| Mars-Rahu Square | Nifty Midcap 150 | 20 | 34 | 1.698 | 1.047 | 0.6509 | 61.76 | 0.368 | 0.5498 |
| Mars-Rahu Square | BSE Sensex | 1 | 34 | 0.1228 | 0.05036 | 0.07246 | 58.82 | 0.7736 | 0.8721 |
| Mars-Rahu Square | BSE Sensex | 3 | 34 | 0.9623 | 0.1513 | 0.811 | 70.59 | 0.2294 | 0.3955 |
| Mars-Rahu Square | BSE Sensex | 5 | 34 | 0.9129 | 0.2506 | 0.6623 | 58.82 | 0.3331 | 0.512 |
| Mars-Rahu Square | BSE Sensex | 10 | 34 | 0.7965 | 0.4957 | 0.3008 | 64.71 | 0.6402 | 0.7844 |
| Mars-Rahu Square | BSE Sensex | 20 | 34 | 0.7946 | 1.002 | -0.207 | 58.82 | 0.8051 | 0.891 |
| Mars-Rahu Trine | Nifty 50 | 1 | 36 | 0.503 | 0.04492 | 0.4581 | 69.44 | 0.007855 | 0.03104 |
| Mars-Rahu Trine | Nifty 50 | 3 | 36 | 1.689 | 0.1333 | 1.556 | 69.44 | 0.004247 | 0.01858 |
| Mars-Rahu Trine | Nifty 50 | 5 | 36 | 3.253 | 0.2178 | 3.035 | 72.22 | 0.0005087 | 0.003504 |
| Mars-Rahu Trine | Nifty 50 | 10 | 36 | 3.82 | 0.4212 | 3.399 | 75 | 0.00307 | 0.01429 |
| Mars-Rahu Trine | Nifty 50 | 20 | 36 | 6.665 | 0.8264 | 5.839 | 69.44 | 0.009531 | 0.03632 |
| Mars-Rahu Trine | Nifty Bank | 1 | 36 | 0.879 | 0.06023 | 0.8188 | 72.22 | 0.002185 | 0.01069 |
| Mars-Rahu Trine | Nifty Bank | 3 | 36 | 1.992 | 0.1819 | 1.81 | 75 | 0.01106 | 0.04142 |
| Mars-Rahu Trine | Nifty Bank | 5 | 36 | 3.534 | 0.3 | 3.235 | 75 | 0.002086 | 0.01039 |
| Mars-Rahu Trine | Nifty Bank | 10 | 36 | 4.359 | 0.5834 | 3.775 | 77.78 | 0.01015 | 0.03833 |
| Mars-Rahu Trine | Nifty Bank | 20 | 36 | 6.135 | 1.172 | 4.963 | 66.67 | 0.01402 | 0.0495 |
| Mars-Rahu Trine | Nifty Midcap 100 | 1 | 36 | -0.1697 | 0.05397 | -0.2237 | 63.89 | 0.3628 | 0.5446 |
| Mars-Rahu Trine | Nifty Midcap 100 | 3 | 36 | -0.07566 | 0.1609 | -0.2365 | 41.67 | 0.5131 | 0.687 |
| Mars-Rahu Trine | Nifty Midcap 100 | 5 | 36 | 0.4552 | 0.266 | 0.1892 | 41.67 | 0.7953 | 0.8851 |
| Mars-Rahu Trine | Nifty Midcap 100 | 10 | 36 | 0.8952 | 0.532 | 0.3633 | 66.67 | 0.7167 | 0.836 |
| Mars-Rahu Trine | Nifty Midcap 100 | 20 | 36 | 1.866 | 1.065 | 0.8011 | 69.44 | 0.6165 | 0.7643 |
| Mars-Rahu Trine | Nifty Midcap 150 | 1 | 36 | 0.5198 | 0.05323 | 0.4666 | 69.44 | 0.02422 | 0.07595 |
| Mars-Rahu Trine | Nifty Midcap 150 | 3 | 36 | 0.09306 | 0.1594 | -0.06638 | 61.11 | 0.8854 | 0.9423 |
| Mars-Rahu Trine | Nifty Midcap 150 | 5 | 36 | 0.8312 | 0.2642 | 0.567 | 69.44 | 0.3131 | 0.4908 |
| Mars-Rahu Trine | Nifty Midcap 150 | 10 | 36 | 1.591 | 0.5204 | 1.071 | 72.22 | 0.1487 | 0.292 |
| Mars-Rahu Trine | Nifty Midcap 150 | 20 | 36 | 1.057 | 1.047 | 0.01001 | 63.89 | 0.9925 | 0.997 |
| Mars-Rahu Trine | BSE Sensex | 1 | 36 | 0.1749 | 0.05036 | 0.1245 | 52.78 | 0.5085 | 0.6836 |
| Mars-Rahu Trine | BSE Sensex | 3 | 36 | 0.1235 | 0.1513 | -0.02783 | 55.56 | 0.9503 | 0.9801 |
| Mars-Rahu Trine | BSE Sensex | 5 | 36 | 0.7058 | 0.2506 | 0.4552 | 66.67 | 0.417 | 0.5988 |
| Mars-Rahu Trine | BSE Sensex | 10 | 36 | 0.4329 | 0.4957 | -0.06275 | 58.33 | 0.9297 | 0.9709 |
| Mars-Rahu Trine | BSE Sensex | 20 | 36 | 0.665 | 1.002 | -0.3366 | 58.33 | 0.7614 | 0.8637 |
| Mars-Saturn Opposition | Nifty 50 | 1 | 13 | 0.4226 | 0.04492 | 0.3776 | 69.23 | 0.2612 | 0.4342 |
| Mars-Saturn Opposition | Nifty 50 | 3 | 13 | 2.335 | 0.1333 | 2.202 | 84.62 | 0.01211 | 0.04441 |
| Mars-Saturn Opposition | Nifty 50 | 5 | 13 | 3.713 | 0.2178 | 3.496 | 84.62 | 0.01398 | 0.04946 |
| Mars-Saturn Opposition | Nifty 50 | 10 | 13 | 4.401 | 0.4212 | 3.979 | 76.92 | 0.03898 | 0.1068 |
| Mars-Saturn Opposition | Nifty 50 | 20 | 13 | 7.9 | 0.8264 | 7.074 | 61.54 | 0.07542 | 0.1756 |
| Mars-Saturn Opposition | Nifty Bank | 1 | 13 | 0.5534 | 0.06023 | 0.4932 | 61.54 | 0.274 | 0.4503 |
| Mars-Saturn Opposition | Nifty Bank | 3 | 13 | 3.21 | 0.1819 | 3.029 | 69.23 | 0.008892 | 0.03427 |
| Mars-Saturn Opposition | Nifty Bank | 5 | 13 | 4.544 | 0.3 | 4.244 | 84.62 | 0.01159 | 0.04282 |
| Mars-Saturn Opposition | Nifty Bank | 10 | 13 | 5.875 | 0.5834 | 5.291 | 76.92 | 0.0334 | 0.0957 |
| Mars-Saturn Opposition | Nifty Bank | 20 | 13 | 7.066 | 1.172 | 5.894 | 53.85 | 0.1127 | 0.2374 |
| Mars-Saturn Opposition | Nifty Midcap 100 | 1 | 13 | 0.07013 | 0.05397 | 0.01617 | 84.62 | 0.9687 | 0.9877 |
| Mars-Saturn Opposition | Nifty Midcap 100 | 3 | 13 | 0.3429 | 0.1609 | 0.1821 | 53.85 | 0.7461 | 0.8532 |
| Mars-Saturn Opposition | Nifty Midcap 100 | 5 | 13 | 0.3991 | 0.266 | 0.1331 | 38.46 | 0.8407 | 0.914 |
| Mars-Saturn Opposition | Nifty Midcap 100 | 10 | 13 | 2.112 | 0.532 | 1.58 | 69.23 | 0.07693 | 0.1776 |
| Mars-Saturn Opposition | Nifty Midcap 100 | 20 | 13 | 2.537 | 1.065 | 1.472 | 61.54 | 0.3328 | 0.512 |
| Mars-Saturn Opposition | Nifty Midcap 150 | 1 | 13 | 0.458 | 0.05323 | 0.4048 | 61.54 | 0.257 | 0.4298 |
| Mars-Saturn Opposition | Nifty Midcap 150 | 3 | 13 | 0.5519 | 0.1594 | 0.3925 | 76.92 | 0.4267 | 0.6084 |
| Mars-Saturn Opposition | Nifty Midcap 150 | 5 | 13 | 1.053 | 0.2642 | 0.7889 | 76.92 | 0.07637 | 0.1767 |
| Mars-Saturn Opposition | Nifty Midcap 150 | 10 | 13 | 1.848 | 0.5204 | 1.328 | 69.23 | 0.1536 | 0.2996 |
| Mars-Saturn Opposition | Nifty Midcap 150 | 20 | 13 | 1.644 | 1.047 | 0.5967 | 61.54 | 0.6336 | 0.7784 |
| Mars-Saturn Opposition | BSE Sensex | 1 | 13 | 0.05387 | 0.05036 | 0.003511 | 61.54 | 0.9893 | 0.9957 |
| Mars-Saturn Opposition | BSE Sensex | 3 | 13 | 0.3638 | 0.1513 | 0.2125 | 61.54 | 0.6908 | 0.8179 |
| Mars-Saturn Opposition | BSE Sensex | 5 | 13 | 0.5179 | 0.2506 | 0.2674 | 61.54 | 0.5883 | 0.7459 |
| Mars-Saturn Opposition | BSE Sensex | 10 | 13 | -0.2052 | 0.4957 | -0.7009 | 38.46 | 0.3711 | 0.5533 |
| Mars-Saturn Opposition | BSE Sensex | 20 | 13 | -1.013 | 1.002 | -2.015 | 38.46 | 0.1778 | 0.3316 |
| Mars-Saturn Square | Nifty 50 | 1 | 31 | 0.3463 | 0.04492 | 0.3013 | 77.42 | 0.0962 | 0.2107 |
| Mars-Saturn Square | Nifty 50 | 3 | 31 | 2.481 | 0.1333 | 2.347 | 83.87 | 1.031e-05 | 0.0001645 |
| Mars-Saturn Square | Nifty 50 | 5 | 31 | 3.866 | 0.2178 | 3.648 | 77.42 | 9.61e-05 | 0.0009508 |
| Mars-Saturn Square | Nifty 50 | 10 | 31 | 4.742 | 0.4212 | 4.321 | 74.19 | 0.0006017 | 0.003924 |
| Mars-Saturn Square | Nifty 50 | 20 | 31 | 9.201 | 0.8264 | 8.374 | 74.19 | 0.0007412 | 0.00464 |
| Mars-Saturn Square | Nifty Bank | 1 | 31 | 0.8041 | 0.06023 | 0.7439 | 67.74 | 0.004378 | 0.01905 |
| Mars-Saturn Square | Nifty Bank | 3 | 31 | 3.316 | 0.1819 | 3.134 | 80.65 | 6.479e-06 | 0.0001109 |
| Mars-Saturn Square | Nifty Bank | 5 | 31 | 4.552 | 0.3 | 4.252 | 77.42 | 5.453e-05 | 0.0006159 |
| Mars-Saturn Square | Nifty Bank | 10 | 31 | 6.013 | 0.5834 | 5.43 | 77.42 | 0.0004742 | 0.003325 |
| Mars-Saturn Square | Nifty Bank | 20 | 31 | 8.622 | 1.172 | 7.45 | 77.42 | 0.0006409 | 0.004136 |
| Mars-Saturn Square | Nifty Midcap 100 | 1 | 31 | 0.003633 | 0.05397 | -0.05033 | 58.06 | 0.7562 | 0.8596 |
| Mars-Saturn Square | Nifty Midcap 100 | 3 | 31 | 0.4126 | 0.1609 | 0.2517 | 45.16 | 0.51 | 0.6841 |
| Mars-Saturn Square | Nifty Midcap 100 | 5 | 31 | 0.4781 | 0.266 | 0.2121 | 41.94 | 0.6624 | 0.7996 |
| Mars-Saturn Square | Nifty Midcap 100 | 10 | 31 | 1.838 | 0.532 | 1.306 | 70.97 | 0.105 | 0.2249 |
| Mars-Saturn Square | Nifty Midcap 100 | 20 | 31 | 3.264 | 1.065 | 2.2 | 77.42 | 0.02246 | 0.07184 |
| Mars-Saturn Square | Nifty Midcap 150 | 1 | 31 | 0.4243 | 0.05323 | 0.3711 | 77.42 | 0.06792 | 0.1619 |
| Mars-Saturn Square | Nifty Midcap 150 | 3 | 31 | 0.9185 | 0.1594 | 0.7591 | 83.87 | 0.0008221 | 0.005058 |
| Mars-Saturn Square | Nifty Midcap 150 | 5 | 31 | 1.375 | 0.2642 | 1.111 | 77.42 | 0.003658 | 0.01657 |
| Mars-Saturn Square | Nifty Midcap 150 | 10 | 31 | 1.704 | 0.5204 | 1.184 | 70.97 | 0.08393 | 0.1894 |
| Mars-Saturn Square | Nifty Midcap 150 | 20 | 31 | 2.209 | 1.047 | 1.161 | 74.19 | 0.1284 | 0.2622 |
| Mars-Saturn Square | BSE Sensex | 1 | 31 | -0.1 | 0.05036 | -0.1504 | 54.84 | 0.4004 | 0.5832 |
| Mars-Saturn Square | BSE Sensex | 3 | 31 | 0.6414 | 0.1513 | 0.4901 | 67.74 | 0.07556 | 0.1756 |
| Mars-Saturn Square | BSE Sensex | 5 | 31 | 1.011 | 0.2506 | 0.7607 | 67.74 | 0.08125 | 0.185 |
| Mars-Saturn Square | BSE Sensex | 10 | 31 | 0.4772 | 0.4957 | -0.01847 | 61.29 | 0.977 | 0.9905 |
| Mars-Saturn Square | BSE Sensex | 20 | 31 | 0.888 | 1.002 | -0.1136 | 67.74 | 0.9069 | 0.9583 |
| Mars-Saturn Trine | Nifty 50 | 1 | 33 | 0.5538 | 0.04492 | 0.5089 | 69.7 | 0.005133 | 0.02175 |
| Mars-Saturn Trine | Nifty 50 | 3 | 33 | 1.614 | 0.1333 | 1.481 | 60.61 | 0.01133 | 0.04238 |
| Mars-Saturn Trine | Nifty 50 | 5 | 33 | 3.074 | 0.2178 | 2.856 | 66.67 | 0.001945 | 0.009906 |
| Mars-Saturn Trine | Nifty 50 | 10 | 33 | 4.116 | 0.4212 | 3.695 | 66.67 | 0.002497 | 0.01205 |
| Mars-Saturn Trine | Nifty 50 | 20 | 32 | 8.008 | 0.8264 | 7.182 | 65.62 | 0.004069 | 0.01797 |
| Mars-Saturn Trine | Nifty Bank | 1 | 33 | 0.9696 | 0.06023 | 0.9093 | 66.67 | 0.001342 | 0.007403 |
| Mars-Saturn Trine | Nifty Bank | 3 | 33 | 2.167 | 0.1819 | 1.985 | 60.61 | 0.009056 | 0.0348 |
| Mars-Saturn Trine | Nifty Bank | 5 | 33 | 3.525 | 0.3 | 3.225 | 66.67 | 0.00275 | 0.01306 |
| Mars-Saturn Trine | Nifty Bank | 10 | 33 | 5.295 | 0.5834 | 4.711 | 66.67 | 0.002198 | 0.01073 |
| Mars-Saturn Trine | Nifty Bank | 20 | 32 | 6.913 | 1.172 | 5.741 | 65.62 | 0.0115 | 0.04268 |
| Mars-Saturn Trine | Nifty Midcap 100 | 1 | 33 | 0.1225 | 0.05397 | 0.06857 | 66.67 | 0.6924 | 0.8183 |
| Mars-Saturn Trine | Nifty Midcap 100 | 3 | 33 | -0.01042 | 0.1609 | -0.1713 | 36.36 | 0.5419 | 0.7095 |
| Mars-Saturn Trine | Nifty Midcap 100 | 5 | 33 | 0.2558 | 0.266 | -0.01023 | 48.48 | 0.975 | 0.9897 |
| Mars-Saturn Trine | Nifty Midcap 100 | 10 | 33 | 1.428 | 0.532 | 0.896 | 72.73 | 0.1898 | 0.3479 |
| Mars-Saturn Trine | Nifty Midcap 100 | 20 | 32 | 1.855 | 1.065 | 0.7902 | 65.62 | 0.4657 | 0.6423 |
| Mars-Saturn Trine | Nifty Midcap 150 | 1 | 33 | 0.5706 | 0.05323 | 0.5174 | 63.64 | 0.01398 | 0.04946 |
| Mars-Saturn Trine | Nifty Midcap 150 | 3 | 33 | 0.07338 | 0.1594 | -0.08606 | 57.58 | 0.7784 | 0.8736 |
| Mars-Saturn Trine | Nifty Midcap 150 | 5 | 33 | 0.6562 | 0.2642 | 0.3919 | 66.67 | 0.3097 | 0.4871 |
| Mars-Saturn Trine | Nifty Midcap 150 | 10 | 33 | 1.898 | 0.5204 | 1.378 | 69.7 | 0.04118 | 0.1109 |
| Mars-Saturn Trine | Nifty Midcap 150 | 20 | 32 | 1.572 | 1.047 | 0.5247 | 65.62 | 0.5542 | 0.7203 |
| Mars-Saturn Trine | BSE Sensex | 1 | 33 | 0.3838 | 0.05036 | 0.3334 | 54.55 | 0.09585 | 0.2103 |
| Mars-Saturn Trine | BSE Sensex | 3 | 33 | 0.2863 | 0.1513 | 0.135 | 54.55 | 0.6914 | 0.8183 |
| Mars-Saturn Trine | BSE Sensex | 5 | 33 | 0.7866 | 0.2506 | 0.536 | 63.64 | 0.1824 | 0.3379 |
| Mars-Saturn Trine | BSE Sensex | 10 | 33 | 1.42 | 0.4957 | 0.924 | 63.64 | 0.1367 | 0.2741 |
| Mars-Saturn Trine | BSE Sensex | 20 | 32 | 1.619 | 1.002 | 0.6176 | 62.5 | 0.5335 | 0.7018 |
| Mars-Sun Opposition | Nifty 50 | 1 | 12 | 0.1029 | 0.04492 | 0.05793 | 66.67 | 0.8616 | 0.9263 |
| Mars-Sun Opposition | Nifty 50 | 3 | 12 | 1.874 | 0.1333 | 1.74 | 66.67 | 0.04715 | 0.1231 |
| Mars-Sun Opposition | Nifty 50 | 5 | 12 | 2.986 | 0.2178 | 2.768 | 58.33 | 0.06423 | 0.1558 |
| Mars-Sun Opposition | Nifty 50 | 10 | 12 | 3.64 | 0.4212 | 3.219 | 50 | 0.09479 | 0.2087 |
| Mars-Sun Opposition | Nifty 50 | 20 | 12 | 6.809 | 0.8264 | 5.982 | 75 | 0.1491 | 0.2925 |
| Mars-Sun Opposition | Nifty Bank | 1 | 12 | 0.3528 | 0.06023 | 0.2925 | 66.67 | 0.5807 | 0.7388 |
| Mars-Sun Opposition | Nifty Bank | 3 | 12 | 2.592 | 0.1819 | 2.41 | 66.67 | 0.03773 | 0.1048 |
| Mars-Sun Opposition | Nifty Bank | 5 | 12 | 3.65 | 0.3 | 3.35 | 66.67 | 0.05464 | 0.1374 |
| Mars-Sun Opposition | Nifty Bank | 10 | 12 | 5.186 | 0.5834 | 4.603 | 83.33 | 0.05143 | 0.131 |
| Mars-Sun Opposition | Nifty Bank | 20 | 12 | 8.546 | 1.172 | 7.373 | 83.33 | 0.04152 | 0.1115 |
| Mars-Sun Opposition | Nifty Midcap 100 | 1 | 12 | -0.7237 | 0.05397 | -0.7777 | 50 | 0.08209 | 0.1863 |
| Mars-Sun Opposition | Nifty Midcap 100 | 3 | 12 | -0.06295 | 0.1609 | -0.2238 | 41.67 | 0.7411 | 0.8501 |
| Mars-Sun Opposition | Nifty Midcap 100 | 5 | 12 | -0.2508 | 0.266 | -0.5168 | 41.67 | 0.4838 | 0.6622 |
| Mars-Sun Opposition | Nifty Midcap 100 | 10 | 12 | -0.1399 | 0.532 | -0.6719 | 50 | 0.5904 | 0.747 |
| Mars-Sun Opposition | Nifty Midcap 100 | 20 | 12 | -0.2185 | 1.065 | -1.283 | 66.67 | 0.6363 | 0.7808 |
| Mars-Sun Opposition | Nifty Midcap 150 | 1 | 12 | 0.3245 | 0.05323 | 0.2713 | 66.67 | 0.4749 | 0.6521 |
| Mars-Sun Opposition | Nifty Midcap 150 | 3 | 12 | 0.6325 | 0.1594 | 0.4731 | 66.67 | 0.276 | 0.453 |
| Mars-Sun Opposition | Nifty Midcap 150 | 5 | 12 | 0.9936 | 0.2642 | 0.7293 | 58.33 | 0.2885 | 0.4633 |
| Mars-Sun Opposition | Nifty Midcap 150 | 10 | 12 | 1.858 | 0.5204 | 1.337 | 50 | 0.2069 | 0.369 |
| Mars-Sun Opposition | Nifty Midcap 150 | 20 | 12 | 1.405 | 1.047 | 0.358 | 75 | 0.8645 | 0.9286 |
| Mars-Sun Opposition | BSE Sensex | 1 | 12 | -0.1376 | 0.05036 | -0.188 | 50 | 0.5998 | 0.7527 |
| Mars-Sun Opposition | BSE Sensex | 3 | 12 | 0.4145 | 0.1513 | 0.2632 | 58.33 | 0.6936 | 0.8189 |
| Mars-Sun Opposition | BSE Sensex | 5 | 12 | 0.7815 | 0.2506 | 0.5309 | 50 | 0.519 | 0.6924 |
| Mars-Sun Opposition | BSE Sensex | 10 | 12 | 0.8806 | 0.4957 | 0.385 | 41.67 | 0.6871 | 0.8141 |
| Mars-Sun Opposition | BSE Sensex | 20 | 12 | 1.359 | 1.002 | 0.3575 | 66.67 | 0.8267 | 0.9052 |
| Mars-Sun Square | Nifty 50 | 1 | 24 | 0.4596 | 0.04492 | 0.4146 | 62.5 | 0.05681 | 0.142 |
| Mars-Sun Square | Nifty 50 | 3 | 24 | 1.39 | 0.1333 | 1.256 | 66.67 | 0.0814 | 0.185 |
| Mars-Sun Square | Nifty 50 | 5 | 24 | 2.65 | 0.2178 | 2.432 | 66.67 | 0.02969 | 0.08817 |
| Mars-Sun Square | Nifty 50 | 10 | 24 | 4.367 | 0.4212 | 3.945 | 83.33 | 0.005294 | 0.02236 |
| Mars-Sun Square | Nifty 50 | 20 | 24 | 8.528 | 0.8264 | 7.702 | 70.83 | 0.004566 | 0.01968 |
| Mars-Sun Square | Nifty Bank | 1 | 24 | 0.822 | 0.06023 | 0.7618 | 66.67 | 0.02744 | 0.08326 |
| Mars-Sun Square | Nifty Bank | 3 | 24 | 1.904 | 0.1819 | 1.722 | 62.5 | 0.06085 | 0.1504 |
| Mars-Sun Square | Nifty Bank | 5 | 24 | 3.023 | 0.3 | 2.723 | 66.67 | 0.03861 | 0.1063 |
| Mars-Sun Square | Nifty Bank | 10 | 24 | 5.29 | 0.5834 | 4.707 | 66.67 | 0.01179 | 0.04337 |
| Mars-Sun Square | Nifty Bank | 20 | 24 | 7.444 | 1.172 | 6.272 | 79.17 | 0.01243 | 0.04544 |
| Mars-Sun Square | Nifty Midcap 100 | 1 | 24 | 0.1588 | 0.05397 | 0.1049 | 62.5 | 0.6822 | 0.8118 |
| Mars-Sun Square | Nifty Midcap 100 | 3 | 24 | 0.2155 | 0.1609 | 0.05463 | 37.5 | 0.9107 | 0.9595 |
| Mars-Sun Square | Nifty Midcap 100 | 5 | 24 | 0.2732 | 0.266 | 0.007232 | 41.67 | 0.9888 | 0.9956 |
| Mars-Sun Square | Nifty Midcap 100 | 10 | 24 | 2.548 | 0.532 | 2.016 | 79.17 | 0.003726 | 0.01675 |
| Mars-Sun Square | Nifty Midcap 100 | 20 | 24 | 3.27 | 1.065 | 2.205 | 66.67 | 0.05103 | 0.1304 |
| Mars-Sun Square | Nifty Midcap 150 | 1 | 24 | 0.5722 | 0.05323 | 0.519 | 58.33 | 0.02913 | 0.08691 |
| Mars-Sun Square | Nifty Midcap 150 | 3 | 24 | 0.1374 | 0.1594 | -0.02203 | 66.67 | 0.9627 | 0.9852 |
| Mars-Sun Square | Nifty Midcap 150 | 5 | 24 | 0.5913 | 0.2642 | 0.3271 | 70.83 | 0.5989 | 0.7519 |
| Mars-Sun Square | Nifty Midcap 150 | 10 | 24 | 2.541 | 0.5204 | 2.021 | 83.33 | 0.03272 | 0.0946 |
| Mars-Sun Square | Nifty Midcap 150 | 20 | 24 | 3.33 | 1.047 | 2.282 | 75 | 0.08631 | 0.1936 |
| Mars-Sun Square | BSE Sensex | 1 | 24 | 0.06125 | 0.05036 | 0.01089 | 45.83 | 0.9654 | 0.9864 |
| Mars-Sun Square | BSE Sensex | 3 | 24 | 0.06777 | 0.1513 | -0.08353 | 58.33 | 0.878 | 0.9372 |
| Mars-Sun Square | BSE Sensex | 5 | 24 | 0.427 | 0.2506 | 0.1765 | 66.67 | 0.7717 | 0.8717 |
| Mars-Sun Square | BSE Sensex | 10 | 24 | 1.541 | 0.4957 | 1.045 | 66.67 | 0.2817 | 0.4581 |
| Mars-Sun Square | BSE Sensex | 20 | 24 | 2.215 | 1.002 | 1.214 | 66.67 | 0.3913 | 0.5745 |
| Mars-Sun Trine | Nifty 50 | 1 | 24 | 0.4535 | 0.04492 | 0.4086 | 79.17 | 0.01825 | 0.06196 |
| Mars-Sun Trine | Nifty 50 | 3 | 24 | 1.564 | 0.1333 | 1.431 | 75 | 0.01581 | 0.05474 |
| Mars-Sun Trine | Nifty 50 | 5 | 24 | 2.976 | 0.2178 | 2.759 | 83.33 | 0.005742 | 0.02392 |
| Mars-Sun Trine | Nifty 50 | 10 | 24 | 4.288 | 0.4212 | 3.867 | 87.5 | 0.002135 | 0.0105 |
| Mars-Sun Trine | Nifty 50 | 20 | 24 | 7.315 | 0.8264 | 6.488 | 75 | 0.01333 | 0.04785 |
| Mars-Sun Trine | Nifty Bank | 1 | 24 | 0.8233 | 0.06023 | 0.7631 | 66.67 | 0.01365 | 0.04876 |
| Mars-Sun Trine | Nifty Bank | 3 | 24 | 1.848 | 0.1819 | 1.666 | 66.67 | 0.03898 | 0.1068 |
| Mars-Sun Trine | Nifty Bank | 5 | 24 | 3.738 | 0.3 | 3.438 | 83.33 | 0.002525 | 0.01215 |
| Mars-Sun Trine | Nifty Bank | 10 | 24 | 5.074 | 0.5834 | 4.49 | 75 | 0.0066 | 0.02664 |
| Mars-Sun Trine | Nifty Bank | 20 | 24 | 6.748 | 1.172 | 5.576 | 66.67 | 0.0324 | 0.09387 |
| Mars-Sun Trine | Nifty Midcap 100 | 1 | 24 | 0.002497 | 0.05397 | -0.05147 | 62.5 | 0.7994 | 0.8879 |
| Mars-Sun Trine | Nifty Midcap 100 | 3 | 24 | -0.2585 | 0.1609 | -0.4194 | 50 | 0.2134 | 0.3765 |
| Mars-Sun Trine | Nifty Midcap 100 | 5 | 24 | 0.01345 | 0.266 | -0.2526 | 45.83 | 0.653 | 0.7932 |
| Mars-Sun Trine | Nifty Midcap 100 | 10 | 24 | 1.842 | 0.532 | 1.31 | 75 | 0.1079 | 0.2294 |
| Mars-Sun Trine | Nifty Midcap 100 | 20 | 24 | 2.138 | 1.065 | 1.073 | 58.33 | 0.4904 | 0.6688 |
| Mars-Sun Trine | Nifty Midcap 150 | 1 | 24 | 0.6369 | 0.05323 | 0.5837 | 79.17 | 0.00436 | 0.019 |
| Mars-Sun Trine | Nifty Midcap 150 | 3 | 24 | 0.42 | 0.1594 | 0.2606 | 75 | 0.3465 | 0.5257 |
| Mars-Sun Trine | Nifty Midcap 150 | 5 | 24 | 1.073 | 0.2642 | 0.8092 | 83.33 | 0.0655 | 0.1578 |
| Mars-Sun Trine | Nifty Midcap 150 | 10 | 24 | 2.343 | 0.5204 | 1.823 | 87.5 | 0.004523 | 0.01956 |
| Mars-Sun Trine | Nifty Midcap 150 | 20 | 24 | 2.169 | 1.047 | 1.121 | 79.17 | 0.2772 | 0.4542 |
| Mars-Sun Trine | BSE Sensex | 1 | 24 | 0.4412 | 0.05036 | 0.3908 | 66.67 | 0.06079 | 0.1504 |
| Mars-Sun Trine | BSE Sensex | 3 | 24 | 1.194 | 0.1513 | 1.043 | 75 | 0.06515 | 0.1572 |
| Mars-Sun Trine | BSE Sensex | 5 | 24 | 1.551 | 0.2506 | 1.3 | 79.17 | 0.03955 | 0.1077 |
| Mars-Sun Trine | BSE Sensex | 10 | 24 | 1.791 | 0.4957 | 1.295 | 79.17 | 0.03046 | 0.08979 |
| Mars-Sun Trine | BSE Sensex | 20 | 24 | 1.477 | 1.002 | 0.4758 | 66.67 | 0.6592 | 0.7968 |
| Mars-Venus Opposition | Nifty 50 | 1 | 12 | 0.3575 | 0.04492 | 0.3126 | 83.33 | 0.6118 | 0.7611 |
| Mars-Venus Opposition | Nifty 50 | 3 | 12 | 1.723 | 0.1333 | 1.589 | 75 | 0.08067 | 0.1839 |
| Mars-Venus Opposition | Nifty 50 | 5 | 12 | 3.318 | 0.2178 | 3.1 | 75 | 0.0305 | 0.08979 |
| Mars-Venus Opposition | Nifty 50 | 10 | 12 | 4.579 | 0.4212 | 4.158 | 75 | 0.02996 | 0.08867 |
| Mars-Venus Opposition | Nifty 50 | 20 | 12 | 8.059 | 0.8264 | 7.232 | 83.33 | 0.05333 | 0.1346 |
| Mars-Venus Opposition | Nifty Bank | 1 | 12 | 1.134 | 0.06023 | 1.074 | 83.33 | 0.08262 | 0.1871 |
| Mars-Venus Opposition | Nifty Bank | 3 | 12 | 2.993 | 0.1819 | 2.811 | 83.33 | 0.006173 | 0.02533 |
| Mars-Venus Opposition | Nifty Bank | 5 | 12 | 5.394 | 0.3 | 5.094 | 83.33 | 0.00386 | 0.01725 |
| Mars-Venus Opposition | Nifty Bank | 10 | 12 | 6.697 | 0.5834 | 6.113 | 83.33 | 0.009409 | 0.03589 |
| Mars-Venus Opposition | Nifty Bank | 20 | 12 | 8.085 | 1.172 | 6.913 | 83.33 | 0.03648 | 0.1023 |
| Mars-Venus Opposition | Nifty Midcap 100 | 1 | 12 | -0.1605 | 0.05397 | -0.2145 | 75 | 0.7118 | 0.8321 |
| Mars-Venus Opposition | Nifty Midcap 100 | 3 | 12 | 0.03842 | 0.1609 | -0.1224 | 41.67 | 0.7931 | 0.8836 |
| Mars-Venus Opposition | Nifty Midcap 100 | 5 | 12 | -0.2907 | 0.266 | -0.5567 | 41.67 | 0.432 | 0.6145 |
| Mars-Venus Opposition | Nifty Midcap 100 | 10 | 12 | 1.893 | 0.532 | 1.361 | 66.67 | 0.3567 | 0.5367 |
| Mars-Venus Opposition | Nifty Midcap 100 | 20 | 12 | 2.362 | 1.065 | 1.297 | 75 | 0.3049 | 0.482 |
| Mars-Venus Opposition | Nifty Midcap 150 | 1 | 12 | 0.4588 | 0.05323 | 0.4056 | 83.33 | 0.5286 | 0.7 |
| Mars-Venus Opposition | Nifty Midcap 150 | 3 | 12 | 0.5135 | 0.1594 | 0.3541 | 75 | 0.4613 | 0.6397 |
| Mars-Venus Opposition | Nifty Midcap 150 | 5 | 12 | 1.439 | 0.2642 | 1.174 | 75 | 0.08138 | 0.185 |
| Mars-Venus Opposition | Nifty Midcap 150 | 10 | 12 | 2.906 | 0.5204 | 2.386 | 66.67 | 0.04123 | 0.1109 |
| Mars-Venus Opposition | Nifty Midcap 150 | 20 | 12 | 2.596 | 1.047 | 1.549 | 83.33 | 0.3093 | 0.4871 |
| Mars-Venus Opposition | BSE Sensex | 1 | 12 | 0.2088 | 0.05036 | 0.1584 | 75 | 0.7716 | 0.8717 |
| Mars-Venus Opposition | BSE Sensex | 3 | 12 | 0.34 | 0.1513 | 0.1887 | 58.33 | 0.723 | 0.8394 |
| Mars-Venus Opposition | BSE Sensex | 5 | 12 | 0.5991 | 0.2506 | 0.3485 | 58.33 | 0.6471 | 0.7906 |
| Mars-Venus Opposition | BSE Sensex | 10 | 12 | 1.108 | 0.4957 | 0.6128 | 58.33 | 0.63 | 0.7766 |
| Mars-Venus Opposition | BSE Sensex | 20 | 12 | 1.027 | 1.002 | 0.02503 | 58.33 | 0.9861 | 0.9949 |
| Mars-Venus Square | Nifty 50 | 1 | 36 | 0.3055 | 0.04492 | 0.2606 | 61.11 | 0.1968 | 0.3558 |
| Mars-Venus Square | Nifty 50 | 3 | 36 | 1.829 | 0.1333 | 1.696 | 69.44 | 0.0004351 | 0.003102 |
| Mars-Venus Square | Nifty 50 | 5 | 36 | 2.677 | 0.2178 | 2.459 | 72.22 | 0.001423 | 0.007773 |
| Mars-Venus Square | Nifty 50 | 10 | 36 | 3.015 | 0.4212 | 2.594 | 66.67 | 0.01136 | 0.04243 |
| Mars-Venus Square | Nifty 50 | 20 | 35 | 6.037 | 0.8264 | 5.21 | 57.14 | 0.01363 | 0.04873 |
| Mars-Venus Square | Nifty Bank | 1 | 36 | 0.6185 | 0.06023 | 0.5583 | 66.67 | 0.06138 | 0.1512 |
| Mars-Venus Square | Nifty Bank | 3 | 36 | 2.357 | 0.1819 | 2.175 | 72.22 | 0.000609 | 0.003958 |
| Mars-Venus Square | Nifty Bank | 5 | 36 | 3.171 | 0.3 | 2.871 | 72.22 | 0.002552 | 0.01225 |
| Mars-Venus Square | Nifty Bank | 10 | 36 | 3.357 | 0.5834 | 2.773 | 61.11 | 0.04378 | 0.1159 |
| Mars-Venus Square | Nifty Bank | 20 | 35 | 5.412 | 1.172 | 4.24 | 54.29 | 0.03466 | 0.09848 |
| Mars-Venus Square | Nifty Midcap 100 | 1 | 36 | 0.0451 | 0.05397 | -0.008865 | 66.67 | 0.9675 | 0.9874 |
| Mars-Venus Square | Nifty Midcap 100 | 3 | 36 | 0.5397 | 0.1609 | 0.3788 | 52.78 | 0.2577 | 0.4306 |
| Mars-Venus Square | Nifty Midcap 100 | 5 | 36 | 0.3108 | 0.266 | 0.04484 | 36.11 | 0.9374 | 0.9749 |
| Mars-Venus Square | Nifty Midcap 100 | 10 | 36 | 1.647 | 0.532 | 1.115 | 72.22 | 0.2065 | 0.3683 |
| Mars-Venus Square | Nifty Midcap 100 | 20 | 35 | 1.803 | 1.065 | 0.7386 | 62.86 | 0.4354 | 0.6172 |
| Mars-Venus Square | Nifty Midcap 150 | 1 | 36 | 0.201 | 0.05323 | 0.1478 | 55.56 | 0.5224 | 0.695 |
| Mars-Venus Square | Nifty Midcap 150 | 3 | 36 | 0.6479 | 0.1594 | 0.4885 | 66.67 | 0.09301 | 0.2058 |
| Mars-Venus Square | Nifty Midcap 150 | 5 | 36 | 0.5521 | 0.2642 | 0.2879 | 63.89 | 0.4484 | 0.6286 |
| Mars-Venus Square | Nifty Midcap 150 | 10 | 36 | 0.4925 | 0.5204 | -0.02797 | 61.11 | 0.9645 | 0.9862 |
| Mars-Venus Square | Nifty Midcap 150 | 20 | 35 | 0.633 | 1.047 | -0.4145 | 57.14 | 0.6321 | 0.7778 |
| Mars-Venus Square | BSE Sensex | 1 | 36 | 0.06563 | 0.05036 | 0.01527 | 55.56 | 0.9426 | 0.9769 |
| Mars-Venus Square | BSE Sensex | 3 | 36 | 0.7116 | 0.1513 | 0.5603 | 61.11 | 0.06184 | 0.1521 |
| Mars-Venus Square | BSE Sensex | 5 | 36 | 0.4493 | 0.2506 | 0.1987 | 58.33 | 0.6177 | 0.765 |
| Mars-Venus Square | BSE Sensex | 10 | 36 | 0.2865 | 0.4957 | -0.2092 | 55.56 | 0.7254 | 0.8404 |
| Mars-Venus Square | BSE Sensex | 20 | 35 | 0.6668 | 1.002 | -0.3348 | 51.43 | 0.6963 | 0.82 |
| Mars-Venus Trine | Nifty 50 | 1 | 32 | 0.4392 | 0.04492 | 0.3943 | 75 | 0.02026 | 0.06654 |
| Mars-Venus Trine | Nifty 50 | 3 | 32 | 1.885 | 0.1333 | 1.752 | 71.88 | 0.004233 | 0.01854 |
| Mars-Venus Trine | Nifty 50 | 5 | 32 | 3.614 | 0.2178 | 3.396 | 75 | 0.0004917 | 0.003408 |
| Mars-Venus Trine | Nifty 50 | 10 | 32 | 4.777 | 0.4212 | 4.356 | 78.12 | 0.0005528 | 0.003701 |
| Mars-Venus Trine | Nifty 50 | 20 | 32 | 9.225 | 0.8264 | 8.399 | 75 | 0.0004138 | 0.002955 |
| Mars-Venus Trine | Nifty Bank | 1 | 32 | 0.7645 | 0.06023 | 0.7043 | 65.62 | 0.01577 | 0.05465 |
| Mars-Venus Trine | Nifty Bank | 3 | 32 | 2.493 | 0.1819 | 2.311 | 78.12 | 0.002884 | 0.01357 |
| Mars-Venus Trine | Nifty Bank | 5 | 32 | 4.24 | 0.3 | 3.94 | 71.88 | 0.0005294 | 0.003592 |
| Mars-Venus Trine | Nifty Bank | 10 | 32 | 5.683 | 0.5834 | 5.1 | 75 | 0.001657 | 0.008716 |
| Mars-Venus Trine | Nifty Bank | 20 | 32 | 9.069 | 1.172 | 7.896 | 84.38 | 0.0001334 | 0.001232 |
| Mars-Venus Trine | Nifty Midcap 100 | 1 | 32 | 0.3741 | 0.05397 | 0.3202 | 78.12 | 0.04651 | 0.1216 |
| Mars-Venus Trine | Nifty Midcap 100 | 3 | 32 | 0.4883 | 0.1609 | 0.3275 | 43.75 | 0.2951 | 0.4717 |
| Mars-Venus Trine | Nifty Midcap 100 | 5 | 32 | 1.034 | 0.266 | 0.7679 | 56.25 | 0.1333 | 0.2699 |
| Mars-Venus Trine | Nifty Midcap 100 | 10 | 32 | 3.184 | 0.532 | 2.652 | 75 | 0.0004825 | 0.003363 |
| Mars-Venus Trine | Nifty Midcap 100 | 20 | 32 | 3.668 | 1.065 | 2.604 | 75 | 0.03049 | 0.08979 |
| Mars-Venus Trine | Nifty Midcap 150 | 1 | 32 | 0.5538 | 0.05323 | 0.5005 | 75 | 0.01021 | 0.03851 |
| Mars-Venus Trine | Nifty Midcap 150 | 3 | 32 | 0.4036 | 0.1594 | 0.2442 | 68.75 | 0.489 | 0.6674 |
| Mars-Venus Trine | Nifty Midcap 150 | 5 | 32 | 1.145 | 0.2642 | 0.8812 | 71.88 | 0.07168 | 0.1691 |
| Mars-Venus Trine | Nifty Midcap 150 | 10 | 32 | 2.298 | 0.5204 | 1.778 | 78.12 | 0.01517 | 0.05287 |
| Mars-Venus Trine | Nifty Midcap 150 | 20 | 32 | 2.498 | 1.047 | 1.45 | 78.12 | 0.04075 | 0.11 |
| Mars-Venus Trine | BSE Sensex | 1 | 32 | 0.1153 | 0.05036 | 0.06496 | 62.5 | 0.6967 | 0.82 |
| Mars-Venus Trine | BSE Sensex | 3 | 32 | 0.5211 | 0.1513 | 0.3698 | 59.38 | 0.3543 | 0.5345 |
| Mars-Venus Trine | BSE Sensex | 5 | 32 | 1.214 | 0.2506 | 0.963 | 65.62 | 0.08685 | 0.1943 |
| Mars-Venus Trine | BSE Sensex | 10 | 32 | 1.58 | 0.4957 | 1.085 | 71.88 | 0.1338 | 0.2706 |
| Mars-Venus Trine | BSE Sensex | 20 | 32 | 2.579 | 1.002 | 1.577 | 71.88 | 0.05691 | 0.1422 |
| Mercury-Moon Opposition | Nifty 50 | 1 | 62 | 0.2712 | 0.04492 | 0.2262 | 61.29 | 0.1326 | 0.269 |
| Mercury-Moon Opposition | Nifty 50 | 3 | 62 | 1.693 | 0.1333 | 1.56 | 70.97 | 0.0002183 | 0.001768 |
| Mercury-Moon Opposition | Nifty 50 | 5 | 62 | 3.147 | 0.2178 | 2.93 | 72.58 | 1.098e-05 | 0.0001723 |
| Mercury-Moon Opposition | Nifty 50 | 10 | 61 | 3.773 | 0.4212 | 3.351 | 67.21 | 0.0002461 | 0.001934 |
| Mercury-Moon Opposition | Nifty 50 | 20 | 61 | 6.96 | 0.8264 | 6.134 | 67.21 | 0.0007978 | 0.004945 |
| Mercury-Moon Opposition | Nifty Bank | 1 | 62 | 0.5217 | 0.06023 | 0.4614 | 56.45 | 0.04948 | 0.1275 |
| Mercury-Moon Opposition | Nifty Bank | 3 | 62 | 1.984 | 0.1819 | 1.802 | 69.35 | 0.001841 | 0.009524 |
| Mercury-Moon Opposition | Nifty Bank | 5 | 62 | 3.424 | 0.3 | 3.124 | 74.19 | 7.124e-05 | 0.0007568 |
| Mercury-Moon Opposition | Nifty Bank | 10 | 61 | 4.601 | 0.5834 | 4.018 | 68.85 | 0.0008417 | 0.005141 |
| Mercury-Moon Opposition | Nifty Bank | 20 | 61 | 5.806 | 1.172 | 4.634 | 60.66 | 0.006362 | 0.02588 |
| Mercury-Moon Opposition | Nifty Midcap 100 | 1 | 62 | 0.05514 | 0.05397 | 0.001173 | 62.9 | 0.9942 | 0.9976 |
| Mercury-Moon Opposition | Nifty Midcap 100 | 3 | 62 | 0.3116 | 0.1609 | 0.1508 | 43.55 | 0.5885 | 0.7459 |
| Mercury-Moon Opposition | Nifty Midcap 100 | 5 | 62 | 0.1827 | 0.266 | -0.08331 | 41.94 | 0.7824 | 0.8763 |
| Mercury-Moon Opposition | Nifty Midcap 100 | 10 | 61 | 1.565 | 0.532 | 1.033 | 70.49 | 0.05243 | 0.1327 |
| Mercury-Moon Opposition | Nifty Midcap 100 | 20 | 61 | 1.563 | 1.065 | 0.4984 | 65.57 | 0.6139 | 0.7623 |
| Mercury-Moon Opposition | Nifty Midcap 150 | 1 | 62 | 0.3002 | 0.05323 | 0.247 | 56.45 | 0.1303 | 0.2649 |
| Mercury-Moon Opposition | Nifty Midcap 150 | 3 | 62 | 0.186 | 0.1594 | 0.02658 | 66.13 | 0.9166 | 0.9629 |
| Mercury-Moon Opposition | Nifty Midcap 150 | 5 | 62 | 0.6997 | 0.2642 | 0.4355 | 70.97 | 0.1907 | 0.3485 |
| Mercury-Moon Opposition | Nifty Midcap 150 | 10 | 61 | 1.429 | 0.5204 | 0.909 | 67.21 | 0.09689 | 0.2118 |
| Mercury-Moon Opposition | Nifty Midcap 150 | 20 | 61 | 0.9419 | 1.047 | -0.1055 | 68.85 | 0.8989 | 0.9515 |
| Mercury-Moon Opposition | BSE Sensex | 1 | 62 | -0.1573 | 0.05036 | -0.2076 | 48.39 | 0.2392 | 0.4066 |
| Mercury-Moon Opposition | BSE Sensex | 3 | 62 | 0.03746 | 0.1513 | -0.1139 | 54.84 | 0.7062 | 0.8283 |
| Mercury-Moon Opposition | BSE Sensex | 5 | 62 | 0.2538 | 0.2506 | 0.003195 | 61.29 | 0.9943 | 0.9976 |
| Mercury-Moon Opposition | BSE Sensex | 10 | 61 | 0.4595 | 0.4957 | -0.03616 | 60.66 | 0.9514 | 0.9807 |
| Mercury-Moon Opposition | BSE Sensex | 20 | 61 | 0.4485 | 1.002 | -0.5531 | 63.93 | 0.5794 | 0.738 |
| Mercury-Moon Square | Nifty 50 | 1 | 126 | 0.3921 | 0.04492 | 0.3472 | 67.46 | 0.004518 | 0.01956 |
| Mercury-Moon Square | Nifty 50 | 3 | 126 | 1.819 | 0.1333 | 1.686 | 73.02 | 4.369e-08 | 1.781e-06 |
| Mercury-Moon Square | Nifty 50 | 5 | 126 | 2.895 | 0.2178 | 2.677 | 68.25 | 8.016e-08 | 3.036e-06 |
| Mercury-Moon Square | Nifty 50 | 10 | 126 | 4.161 | 0.4212 | 3.74 | 72.22 | 1.113e-09 | 6.419e-08 |
| Mercury-Moon Square | Nifty 50 | 20 | 126 | 8.523 | 0.8264 | 7.697 | 74.6 | 5.287e-11 | 3.741e-09 |
| Mercury-Moon Square | Nifty Bank | 1 | 126 | 0.6471 | 0.06023 | 0.5868 | 67.46 | 0.001883 | 0.009686 |
| Mercury-Moon Square | Nifty Bank | 3 | 126 | 2.191 | 0.1819 | 2.009 | 72.22 | 5.127e-07 | 1.371e-05 |
| Mercury-Moon Square | Nifty Bank | 5 | 126 | 3.051 | 0.3 | 2.751 | 66.67 | 5.61e-06 | 9.877e-05 |
| Mercury-Moon Square | Nifty Bank | 10 | 126 | 5.059 | 0.5834 | 4.476 | 67.46 | 3.207e-08 | 1.382e-06 |
| Mercury-Moon Square | Nifty Bank | 20 | 126 | 7.604 | 1.172 | 6.432 | 69.84 | 3.524e-09 | 1.888e-07 |
| Mercury-Moon Square | Nifty Midcap 100 | 1 | 126 | 0.06424 | 0.05397 | 0.01028 | 65.08 | 0.946 | 0.9787 |
| Mercury-Moon Square | Nifty Midcap 100 | 3 | 126 | 0.001694 | 0.1609 | -0.1592 | 39.68 | 0.5477 | 0.7148 |
| Mercury-Moon Square | Nifty Midcap 100 | 5 | 126 | 0.05205 | 0.266 | -0.214 | 42.06 | 0.4592 | 0.6373 |
| Mercury-Moon Square | Nifty Midcap 100 | 10 | 126 | 1.802 | 0.532 | 1.27 | 70.63 | 0.0005728 | 0.003805 |
| Mercury-Moon Square | Nifty Midcap 100 | 20 | 126 | 2.855 | 1.065 | 1.791 | 71.43 | 0.0008862 | 0.005326 |
| Mercury-Moon Square | Nifty Midcap 150 | 1 | 126 | 0.4971 | 0.05323 | 0.4438 | 67.46 | 0.0005676 | 0.003781 |
| Mercury-Moon Square | Nifty Midcap 150 | 3 | 126 | 0.3885 | 0.1594 | 0.2291 | 74.6 | 0.2208 | 0.3854 |
| Mercury-Moon Square | Nifty Midcap 150 | 5 | 126 | 0.4723 | 0.2642 | 0.2081 | 66.67 | 0.4374 | 0.618 |
| Mercury-Moon Square | Nifty Midcap 150 | 10 | 126 | 1.965 | 0.5204 | 1.445 | 69.84 | 7.328e-05 | 0.0007719 |
| Mercury-Moon Square | Nifty Midcap 150 | 20 | 126 | 2.509 | 1.047 | 1.462 | 73.81 | 0.0005151 | 0.003531 |
| Mercury-Moon Square | BSE Sensex | 1 | 126 | 0.0756 | 0.05036 | 0.02524 | 54.76 | 0.8445 | 0.9163 |
| Mercury-Moon Square | BSE Sensex | 3 | 126 | 0.3274 | 0.1513 | 0.1761 | 59.52 | 0.4024 | 0.5847 |
| Mercury-Moon Square | BSE Sensex | 5 | 126 | 0.09819 | 0.2506 | -0.1524 | 51.59 | 0.5965 | 0.7511 |
| Mercury-Moon Square | BSE Sensex | 10 | 126 | 0.6231 | 0.4957 | 0.1274 | 56.35 | 0.7087 | 0.8295 |
| Mercury-Moon Square | BSE Sensex | 20 | 126 | 1.15 | 1.002 | 0.1485 | 59.52 | 0.7807 | 0.8755 |
| Mercury-Moon Trine | Nifty 50 | 1 | 94 | 0.271 | 0.04492 | 0.2261 | 61.7 | 0.04957 | 0.1277 |
| Mercury-Moon Trine | Nifty 50 | 3 | 94 | 1.826 | 0.1333 | 1.692 | 68.09 | 1.045e-06 | 2.5e-05 |
| Mercury-Moon Trine | Nifty 50 | 5 | 94 | 3.358 | 0.2178 | 3.14 | 70.21 | 2.996e-08 | 1.306e-06 |
| Mercury-Moon Trine | Nifty 50 | 10 | 94 | 4.694 | 0.4212 | 4.273 | 70.21 | 5.245e-09 | 2.732e-07 |
| Mercury-Moon Trine | Nifty 50 | 20 | 94 | 9.676 | 0.8264 | 8.849 | 72.34 | 5.273e-10 | 3.351e-08 |
| Mercury-Moon Trine | Nifty Bank | 1 | 94 | 0.7357 | 0.06023 | 0.6754 | 69.15 | 2.181e-05 | 0.0003029 |
| Mercury-Moon Trine | Nifty Bank | 3 | 94 | 2.323 | 0.1819 | 2.141 | 65.96 | 1.514e-06 | 3.38e-05 |
| Mercury-Moon Trine | Nifty Bank | 5 | 94 | 3.731 | 0.3 | 3.431 | 71.28 | 3.324e-07 | 1.005e-05 |
| Mercury-Moon Trine | Nifty Bank | 10 | 94 | 5.736 | 0.5834 | 5.153 | 70.21 | 2.257e-08 | 1.032e-06 |
| Mercury-Moon Trine | Nifty Bank | 20 | 94 | 8.839 | 1.172 | 7.667 | 71.28 | 1.625e-09 | 9.092e-08 |
| Mercury-Moon Trine | Nifty Midcap 100 | 1 | 94 | -0.251 | 0.05397 | -0.305 | 58.51 | 0.01436 | 0.05035 |
| Mercury-Moon Trine | Nifty Midcap 100 | 3 | 94 | -0.1767 | 0.1609 | -0.3375 | 34.04 | 0.1357 | 0.2729 |
| Mercury-Moon Trine | Nifty Midcap 100 | 5 | 94 | -0.3519 | 0.266 | -0.6179 | 31.91 | 0.03858 | 0.1063 |
| Mercury-Moon Trine | Nifty Midcap 100 | 10 | 94 | 2 | 0.532 | 1.468 | 70.21 | 0.0008231 | 0.005058 |
| Mercury-Moon Trine | Nifty Midcap 100 | 20 | 94 | 2.928 | 1.065 | 1.863 | 71.28 | 0.001912 | 0.009797 |
| Mercury-Moon Trine | Nifty Midcap 150 | 1 | 94 | 0.4125 | 0.05323 | 0.3592 | 59.57 | 0.007669 | 0.03034 |
| Mercury-Moon Trine | Nifty Midcap 150 | 3 | 94 | 0.2145 | 0.1594 | 0.05507 | 68.09 | 0.7416 | 0.8502 |
| Mercury-Moon Trine | Nifty Midcap 150 | 5 | 94 | 0.6802 | 0.2642 | 0.416 | 70.21 | 0.07959 | 0.1822 |
| Mercury-Moon Trine | Nifty Midcap 150 | 10 | 94 | 2.151 | 0.5204 | 1.631 | 71.28 | 3.915e-05 | 0.0004617 |
| Mercury-Moon Trine | Nifty Midcap 150 | 20 | 94 | 2.603 | 1.047 | 1.556 | 71.28 | 0.0009337 | 0.005523 |
| Mercury-Moon Trine | BSE Sensex | 1 | 94 | -0.07368 | 0.05036 | -0.124 | 48.94 | 0.3132 | 0.4908 |
| Mercury-Moon Trine | BSE Sensex | 3 | 94 | -0.1233 | 0.1513 | -0.2746 | 55.32 | 0.2728 | 0.4493 |
| Mercury-Moon Trine | BSE Sensex | 5 | 94 | -0.292 | 0.2506 | -0.5425 | 53.19 | 0.1648 | 0.3163 |
| Mercury-Moon Trine | BSE Sensex | 10 | 94 | 0.4604 | 0.4957 | -0.03528 | 56.38 | 0.9432 | 0.977 |
| Mercury-Moon Trine | BSE Sensex | 20 | 94 | 1.152 | 1.002 | 0.1506 | 55.32 | 0.8153 | 0.897 |
| Mercury-Rahu Opposition | Nifty 50 | 1 | 28 | 0.2786 | 0.04492 | 0.2336 | 60.71 | 0.2714 | 0.4472 |
| Mercury-Rahu Opposition | Nifty 50 | 3 | 28 | 1.693 | 0.1333 | 1.56 | 67.86 | 0.01323 | 0.04761 |
| Mercury-Rahu Opposition | Nifty 50 | 5 | 28 | 3.075 | 0.2178 | 2.857 | 67.86 | 0.005301 | 0.02236 |
| Mercury-Rahu Opposition | Nifty 50 | 10 | 28 | 4.198 | 0.4212 | 3.776 | 67.86 | 0.00375 | 0.01678 |
| Mercury-Rahu Opposition | Nifty 50 | 20 | 28 | 8.598 | 0.8264 | 7.772 | 67.86 | 0.003147 | 0.01459 |
| Mercury-Rahu Opposition | Nifty Bank | 1 | 28 | 0.8459 | 0.06023 | 0.7856 | 67.86 | 0.0386 | 0.1063 |
| Mercury-Rahu Opposition | Nifty Bank | 3 | 28 | 2.279 | 0.1819 | 2.097 | 60.71 | 0.009096 | 0.03484 |
| Mercury-Rahu Opposition | Nifty Bank | 5 | 28 | 3.554 | 0.3 | 3.254 | 64.29 | 0.008123 | 0.03179 |
| Mercury-Rahu Opposition | Nifty Bank | 10 | 28 | 5.523 | 0.5834 | 4.94 | 67.86 | 0.001614 | 0.008558 |
| Mercury-Rahu Opposition | Nifty Bank | 20 | 28 | 8.288 | 1.172 | 7.116 | 64.29 | 0.002097 | 0.01039 |
| Mercury-Rahu Opposition | Nifty Midcap 100 | 1 | 28 | -0.05284 | 0.05397 | -0.1068 | 53.57 | 0.5473 | 0.7148 |
| Mercury-Rahu Opposition | Nifty Midcap 100 | 3 | 28 | 0.3366 | 0.1609 | 0.1757 | 42.86 | 0.5384 | 0.7061 |
| Mercury-Rahu Opposition | Nifty Midcap 100 | 5 | 28 | 0.5095 | 0.266 | 0.2435 | 46.43 | 0.4366 | 0.6173 |
| Mercury-Rahu Opposition | Nifty Midcap 100 | 10 | 28 | 2.082 | 0.532 | 1.55 | 78.57 | 0.02007 | 0.06611 |
| Mercury-Rahu Opposition | Nifty Midcap 100 | 20 | 28 | 3.218 | 1.065 | 2.153 | 82.14 | 0.03436 | 0.09768 |
| Mercury-Rahu Opposition | Nifty Midcap 150 | 1 | 28 | 0.4509 | 0.05323 | 0.3977 | 60.71 | 0.1042 | 0.2237 |
| Mercury-Rahu Opposition | Nifty Midcap 150 | 3 | 28 | 0.3099 | 0.1594 | 0.1505 | 64.29 | 0.6752 | 0.8083 |
| Mercury-Rahu Opposition | Nifty Midcap 150 | 5 | 28 | 0.7172 | 0.2642 | 0.453 | 67.86 | 0.3317 | 0.511 |
| Mercury-Rahu Opposition | Nifty Midcap 150 | 10 | 28 | 1.967 | 0.5204 | 1.447 | 60.71 | 0.03921 | 0.107 |
| Mercury-Rahu Opposition | Nifty Midcap 150 | 20 | 28 | 2.336 | 1.047 | 1.288 | 67.86 | 0.1651 | 0.3165 |
| Mercury-Rahu Opposition | BSE Sensex | 1 | 28 | 0.08291 | 0.05036 | 0.03255 | 53.57 | 0.8779 | 0.9372 |
| Mercury-Rahu Opposition | BSE Sensex | 3 | 28 | 0.3363 | 0.1513 | 0.185 | 53.57 | 0.6531 | 0.7932 |
| Mercury-Rahu Opposition | BSE Sensex | 5 | 28 | 0.3807 | 0.2506 | 0.1301 | 53.57 | 0.7969 | 0.8854 |
| Mercury-Rahu Opposition | BSE Sensex | 10 | 28 | 0.4614 | 0.4957 | -0.03422 | 57.14 | 0.9558 | 0.982 |
| Mercury-Rahu Opposition | BSE Sensex | 20 | 28 | 1.622 | 1.002 | 0.62 | 60.71 | 0.5294 | 0.7006 |
| Mercury-Rahu Square | Nifty 50 | 1 | 56 | 0.2739 | 0.04492 | 0.229 | 58.93 | 0.1725 | 0.3264 |
| Mercury-Rahu Square | Nifty 50 | 3 | 56 | 1.403 | 0.1333 | 1.27 | 57.14 | 0.005569 | 0.02328 |
| Mercury-Rahu Square | Nifty 50 | 5 | 56 | 2.614 | 0.2178 | 2.397 | 66.07 | 0.0008148 | 0.005034 |
| Mercury-Rahu Square | Nifty 50 | 10 | 56 | 3.43 | 0.4212 | 3.008 | 57.14 | 0.001104 | 0.006408 |
| Mercury-Rahu Square | Nifty 50 | 20 | 56 | 8.79 | 0.8264 | 7.964 | 82.14 | 3.797e-06 | 7.301e-05 |
| Mercury-Rahu Square | Nifty Bank | 1 | 56 | 0.3916 | 0.06023 | 0.3314 | 57.14 | 0.2375 | 0.4052 |
| Mercury-Rahu Square | Nifty Bank | 3 | 56 | 1.695 | 0.1819 | 1.513 | 62.5 | 0.01418 | 0.04989 |
| Mercury-Rahu Square | Nifty Bank | 5 | 56 | 2.715 | 0.3 | 2.415 | 67.86 | 0.004149 | 0.01826 |
| Mercury-Rahu Square | Nifty Bank | 10 | 56 | 3.847 | 0.5834 | 3.263 | 60.71 | 0.006531 | 0.02642 |
| Mercury-Rahu Square | Nifty Bank | 20 | 56 | 7.604 | 1.172 | 6.431 | 78.57 | 4.891e-05 | 0.0005591 |
| Mercury-Rahu Square | Nifty Midcap 100 | 1 | 56 | 0.1925 | 0.05397 | 0.1386 | 66.07 | 0.3825 | 0.5648 |
| Mercury-Rahu Square | Nifty Midcap 100 | 3 | 56 | 0.01197 | 0.1609 | -0.1489 | 41.07 | 0.5969 | 0.7511 |
| Mercury-Rahu Square | Nifty Midcap 100 | 5 | 56 | 0.505 | 0.266 | 0.239 | 42.86 | 0.5283 | 0.6998 |
| Mercury-Rahu Square | Nifty Midcap 100 | 10 | 56 | 2.098 | 0.532 | 1.566 | 76.79 | 0.001651 | 0.008716 |
| Mercury-Rahu Square | Nifty Midcap 100 | 20 | 56 | 3.654 | 1.065 | 2.589 | 75 | 0.0002161 | 0.001759 |
| Mercury-Rahu Square | Nifty Midcap 150 | 1 | 56 | 0.2505 | 0.05323 | 0.1973 | 57.14 | 0.3037 | 0.4806 |
| Mercury-Rahu Square | Nifty Midcap 150 | 3 | 56 | -0.2045 | 0.1594 | -0.3639 | 53.57 | 0.2823 | 0.4582 |
| Mercury-Rahu Square | Nifty Midcap 150 | 5 | 56 | 0.0489 | 0.2642 | -0.2153 | 62.5 | 0.5599 | 0.7248 |
| Mercury-Rahu Square | Nifty Midcap 150 | 10 | 56 | 0.9985 | 0.5204 | 0.4781 | 55.36 | 0.3412 | 0.5216 |
| Mercury-Rahu Square | Nifty Midcap 150 | 20 | 56 | 2.788 | 1.047 | 1.74 | 78.57 | 0.001296 | 0.00723 |
| Mercury-Rahu Square | BSE Sensex | 1 | 56 | -0.149 | 0.05036 | -0.1993 | 44.64 | 0.2981 | 0.4747 |
| Mercury-Rahu Square | BSE Sensex | 3 | 56 | -0.1079 | 0.1513 | -0.2592 | 46.43 | 0.5014 | 0.6771 |
| Mercury-Rahu Square | BSE Sensex | 5 | 56 | -0.171 | 0.2506 | -0.4215 | 46.43 | 0.3436 | 0.5236 |
| Mercury-Rahu Square | BSE Sensex | 10 | 56 | -0.2933 | 0.4957 | -0.7889 | 42.86 | 0.1378 | 0.2755 |
| Mercury-Rahu Square | BSE Sensex | 20 | 56 | 1.493 | 1.002 | 0.4918 | 71.43 | 0.4838 | 0.6622 |
| Mercury-Rahu Trine | Nifty 50 | 1 | 114 | 0.406 | 0.04492 | 0.3611 | 67.54 | 0.006809 | 0.02734 |
| Mercury-Rahu Trine | Nifty 50 | 3 | 114 | 1.569 | 0.1333 | 1.436 | 62.28 | 0.0001025 | 0.001001 |
| Mercury-Rahu Trine | Nifty 50 | 5 | 114 | 3.013 | 0.2178 | 2.796 | 71.05 | 1.903e-08 | 9.034e-07 |
| Mercury-Rahu Trine | Nifty 50 | 10 | 114 | 3.748 | 0.4212 | 3.326 | 66.67 | 2.657e-07 | 8.302e-06 |
| Mercury-Rahu Trine | Nifty 50 | 20 | 114 | 7.189 | 0.8264 | 6.362 | 70.18 | 3.806e-07 | 1.115e-05 |
| Mercury-Rahu Trine | Nifty Bank | 1 | 114 | 0.7275 | 0.06023 | 0.6673 | 63.16 | 0.0001225 | 0.001157 |
| Mercury-Rahu Trine | Nifty Bank | 3 | 114 | 1.946 | 0.1819 | 1.764 | 61.4 | 9.046e-05 | 0.000907 |
| Mercury-Rahu Trine | Nifty Bank | 5 | 114 | 3.605 | 0.3 | 3.305 | 71.05 | 2.859e-08 | 1.262e-06 |
| Mercury-Rahu Trine | Nifty Bank | 10 | 114 | 5.014 | 0.5834 | 4.431 | 71.93 | 3.696e-08 | 1.568e-06 |
| Mercury-Rahu Trine | Nifty Bank | 20 | 114 | 6.956 | 1.172 | 5.783 | 70.18 | 9.808e-07 | 2.373e-05 |
| Mercury-Rahu Trine | Nifty Midcap 100 | 1 | 114 | 0.06816 | 0.05397 | 0.01419 | 64.91 | 0.9294 | 0.9709 |
| Mercury-Rahu Trine | Nifty Midcap 100 | 3 | 114 | 0.02217 | 0.1609 | -0.1387 | 39.47 | 0.6042 | 0.7556 |
| Mercury-Rahu Trine | Nifty Midcap 100 | 5 | 114 | 0.0908 | 0.266 | -0.1752 | 40.35 | 0.4761 | 0.6536 |
| Mercury-Rahu Trine | Nifty Midcap 100 | 10 | 114 | 1.134 | 0.532 | 0.6019 | 64.04 | 0.16 | 0.3091 |
| Mercury-Rahu Trine | Nifty Midcap 100 | 20 | 114 | 1.848 | 1.065 | 0.7836 | 69.3 | 0.2097 | 0.3714 |
| Mercury-Rahu Trine | Nifty Midcap 150 | 1 | 114 | 0.4043 | 0.05323 | 0.3511 | 65.79 | 0.01197 | 0.04396 |
| Mercury-Rahu Trine | Nifty Midcap 150 | 3 | 114 | 0.2505 | 0.1594 | 0.09109 | 58.77 | 0.754 | 0.8587 |
| Mercury-Rahu Trine | Nifty Midcap 150 | 5 | 114 | 0.8227 | 0.2642 | 0.5584 | 65.79 | 0.06744 | 0.1611 |
| Mercury-Rahu Trine | Nifty Midcap 150 | 10 | 114 | 1.576 | 0.5204 | 1.055 | 65.79 | 0.01146 | 0.04268 |
| Mercury-Rahu Trine | Nifty Midcap 150 | 20 | 114 | 1.619 | 1.047 | 0.5713 | 68.42 | 0.3492 | 0.5289 |
| Mercury-Rahu Trine | BSE Sensex | 1 | 114 | 0.09663 | 0.05036 | 0.04627 | 57.02 | 0.7387 | 0.8487 |
| Mercury-Rahu Trine | BSE Sensex | 3 | 114 | 0.169 | 0.1513 | 0.01765 | 56.14 | 0.9577 | 0.9826 |
| Mercury-Rahu Trine | BSE Sensex | 5 | 114 | 0.5518 | 0.2506 | 0.3013 | 62.28 | 0.3697 | 0.5519 |
| Mercury-Rahu Trine | BSE Sensex | 10 | 114 | 0.7766 | 0.4957 | 0.2809 | 57.02 | 0.4939 | 0.6724 |
| Mercury-Rahu Trine | BSE Sensex | 20 | 114 | 1.039 | 1.002 | 0.03712 | 63.16 | 0.9538 | 0.982 |
| Mercury-Saturn Opposition | Nifty 50 | 1 | 28 | 0.4003 | 0.04492 | 0.3553 | 67.86 | 0.03658 | 0.1025 |
| Mercury-Saturn Opposition | Nifty 50 | 3 | 28 | 2.1 | 0.1333 | 1.967 | 71.43 | 0.001467 | 0.007962 |
| Mercury-Saturn Opposition | Nifty 50 | 5 | 28 | 3.949 | 0.2178 | 3.731 | 71.43 | 0.0004764 | 0.003327 |
| Mercury-Saturn Opposition | Nifty 50 | 10 | 28 | 5.316 | 0.4212 | 4.895 | 71.43 | 0.0005394 | 0.003631 |
| Mercury-Saturn Opposition | Nifty 50 | 20 | 28 | 9.798 | 0.8264 | 8.971 | 71.43 | 0.0007291 | 0.00458 |
| Mercury-Saturn Opposition | Nifty Bank | 1 | 28 | 0.6806 | 0.06023 | 0.6204 | 67.86 | 0.03879 | 0.1066 |
| Mercury-Saturn Opposition | Nifty Bank | 3 | 28 | 2.566 | 0.1819 | 2.384 | 71.43 | 0.003179 | 0.01472 |
| Mercury-Saturn Opposition | Nifty Bank | 5 | 28 | 4.655 | 0.3 | 4.356 | 71.43 | 0.0006759 | 0.004311 |
| Mercury-Saturn Opposition | Nifty Bank | 10 | 28 | 6.837 | 0.5834 | 6.253 | 67.86 | 0.000457 | 0.003215 |
| Mercury-Saturn Opposition | Nifty Bank | 20 | 28 | 9.806 | 1.172 | 8.634 | 82.14 | 0.0005048 | 0.003493 |
| Mercury-Saturn Opposition | Nifty Midcap 100 | 1 | 28 | -0.1685 | 0.05397 | -0.2225 | 50 | 0.1423 | 0.2828 |
| Mercury-Saturn Opposition | Nifty Midcap 100 | 3 | 28 | -0.07371 | 0.1609 | -0.2346 | 32.14 | 0.4629 | 0.6412 |
| Mercury-Saturn Opposition | Nifty Midcap 100 | 5 | 28 | 0.3224 | 0.266 | 0.05641 | 25 | 0.9308 | 0.9709 |
| Mercury-Saturn Opposition | Nifty Midcap 100 | 10 | 28 | 1.68 | 0.532 | 1.148 | 67.86 | 0.1947 | 0.3531 |
| Mercury-Saturn Opposition | Nifty Midcap 100 | 20 | 28 | 3.183 | 1.065 | 2.118 | 67.86 | 0.09336 | 0.2062 |
| Mercury-Saturn Opposition | Nifty Midcap 150 | 1 | 28 | 0.3967 | 0.05323 | 0.3435 | 64.29 | 0.08719 | 0.195 |
| Mercury-Saturn Opposition | Nifty Midcap 150 | 3 | 28 | 0.4096 | 0.1594 | 0.2502 | 67.86 | 0.4034 | 0.5857 |
| Mercury-Saturn Opposition | Nifty Midcap 150 | 5 | 28 | 1.183 | 0.2642 | 0.9187 | 67.86 | 0.09953 | 0.2162 |
| Mercury-Saturn Opposition | Nifty Midcap 150 | 10 | 28 | 2.69 | 0.5204 | 2.17 | 67.86 | 0.01554 | 0.05391 |
| Mercury-Saturn Opposition | Nifty Midcap 150 | 20 | 28 | 2.572 | 1.047 | 1.525 | 71.43 | 0.1773 | 0.3312 |
| Mercury-Saturn Opposition | BSE Sensex | 1 | 28 | 0.2525 | 0.05036 | 0.2022 | 53.57 | 0.3784 | 0.5608 |
| Mercury-Saturn Opposition | BSE Sensex | 3 | 28 | 1.15 | 0.1513 | 0.9986 | 64.29 | 0.02627 | 0.08022 |
| Mercury-Saturn Opposition | BSE Sensex | 5 | 28 | 1.777 | 0.2506 | 1.526 | 71.43 | 0.0235 | 0.07425 |
| Mercury-Saturn Opposition | BSE Sensex | 10 | 28 | 2.453 | 0.4957 | 1.957 | 64.29 | 0.03033 | 0.08964 |
| Mercury-Saturn Opposition | BSE Sensex | 20 | 28 | 2.446 | 1.002 | 1.445 | 64.29 | 0.2306 | 0.3963 |
| Mercury-Saturn Square | Nifty 50 | 1 | 66 | 0.449 | 0.04492 | 0.4041 | 68.18 | 0.005912 | 0.02453 |
| Mercury-Saturn Square | Nifty 50 | 3 | 66 | 1.897 | 0.1333 | 1.763 | 63.64 | 4.936e-06 | 8.898e-05 |
| Mercury-Saturn Square | Nifty 50 | 5 | 66 | 3.069 | 0.2178 | 2.851 | 69.7 | 1.298e-05 | 0.0001994 |
| Mercury-Saturn Square | Nifty 50 | 10 | 66 | 3.643 | 0.4212 | 3.222 | 63.64 | 0.0003241 | 0.00244 |
| Mercury-Saturn Square | Nifty 50 | 20 | 66 | 8.677 | 0.8264 | 7.85 | 75.76 | 1.899e-06 | 4.069e-05 |
| Mercury-Saturn Square | Nifty Bank | 1 | 66 | 0.8928 | 0.06023 | 0.8325 | 74.24 | 4.507e-05 | 0.0005216 |
| Mercury-Saturn Square | Nifty Bank | 3 | 66 | 2.458 | 0.1819 | 2.276 | 71.21 | 6.418e-06 | 0.0001104 |
| Mercury-Saturn Square | Nifty Bank | 5 | 66 | 3.412 | 0.3 | 3.112 | 66.67 | 4.1e-05 | 0.0004806 |
| Mercury-Saturn Square | Nifty Bank | 10 | 66 | 4.833 | 0.5834 | 4.25 | 65.15 | 0.000141 | 0.001283 |
| Mercury-Saturn Square | Nifty Bank | 20 | 66 | 8.257 | 1.172 | 7.085 | 77.27 | 2.508e-06 | 5.255e-05 |
| Mercury-Saturn Square | Nifty Midcap 100 | 1 | 66 | 0.1205 | 0.05397 | 0.06649 | 65.15 | 0.6733 | 0.8074 |
| Mercury-Saturn Square | Nifty Midcap 100 | 3 | 66 | 0.03745 | 0.1609 | -0.1234 | 36.36 | 0.5514 | 0.7172 |
| Mercury-Saturn Square | Nifty Midcap 100 | 5 | 66 | 0.01046 | 0.266 | -0.2556 | 31.82 | 0.34 | 0.5208 |
| Mercury-Saturn Square | Nifty Midcap 100 | 10 | 66 | 1.453 | 0.532 | 0.9212 | 72.73 | 0.06341 | 0.1548 |
| Mercury-Saturn Square | Nifty Midcap 100 | 20 | 66 | 2.204 | 1.065 | 1.139 | 69.7 | 0.09394 | 0.2073 |
| Mercury-Saturn Square | Nifty Midcap 150 | 1 | 66 | 0.516 | 0.05323 | 0.4628 | 69.7 | 0.003458 | 0.01576 |
| Mercury-Saturn Square | Nifty Midcap 150 | 3 | 66 | 0.4054 | 0.1594 | 0.2459 | 63.64 | 0.1943 | 0.3528 |
| Mercury-Saturn Square | Nifty Midcap 150 | 5 | 66 | 0.382 | 0.2642 | 0.1177 | 66.67 | 0.694 | 0.8191 |
| Mercury-Saturn Square | Nifty Midcap 150 | 10 | 66 | 0.8669 | 0.5204 | 0.3465 | 60.61 | 0.5601 | 0.7248 |
| Mercury-Saturn Square | Nifty Midcap 150 | 20 | 66 | 1.919 | 1.047 | 0.872 | 77.27 | 0.1711 | 0.3249 |
| Mercury-Saturn Square | BSE Sensex | 1 | 66 | 0.1329 | 0.05036 | 0.08249 | 51.52 | 0.581 | 0.7388 |
| Mercury-Saturn Square | BSE Sensex | 3 | 66 | 0.2462 | 0.1513 | 0.09488 | 45.45 | 0.6729 | 0.8072 |
| Mercury-Saturn Square | BSE Sensex | 5 | 66 | -0.06946 | 0.2506 | -0.32 | 54.55 | 0.2983 | 0.4749 |
| Mercury-Saturn Square | BSE Sensex | 10 | 66 | -0.491 | 0.4957 | -0.9867 | 43.94 | 0.05296 | 0.1338 |
| Mercury-Saturn Square | BSE Sensex | 20 | 66 | 0.4049 | 1.002 | -0.5967 | 65.15 | 0.4254 | 0.6073 |
| Mercury-Saturn Trine | Nifty 50 | 1 | 63 | 0.4931 | 0.04492 | 0.4482 | 68.25 | 0.0002424 | 0.001918 |
| Mercury-Saturn Trine | Nifty 50 | 3 | 63 | 2.076 | 0.1333 | 1.943 | 71.43 | 3.588e-07 | 1.06e-05 |
| Mercury-Saturn Trine | Nifty 50 | 5 | 63 | 3.566 | 0.2178 | 3.348 | 77.78 | 1.973e-07 | 6.433e-06 |
| Mercury-Saturn Trine | Nifty 50 | 10 | 63 | 4.306 | 0.4212 | 3.884 | 73.02 | 4.094e-06 | 7.677e-05 |
| Mercury-Saturn Trine | Nifty 50 | 20 | 63 | 8.753 | 0.8264 | 7.927 | 74.6 | 4.959e-06 | 8.898e-05 |
| Mercury-Saturn Trine | Nifty Bank | 1 | 63 | 0.9201 | 0.06023 | 0.8599 | 66.67 | 2.488e-05 | 0.0003321 |
| Mercury-Saturn Trine | Nifty Bank | 3 | 63 | 2.665 | 0.1819 | 2.483 | 65.08 | 4.184e-07 | 1.207e-05 |
| Mercury-Saturn Trine | Nifty Bank | 5 | 63 | 4.124 | 0.3 | 3.824 | 76.19 | 3.56e-07 | 1.06e-05 |
| Mercury-Saturn Trine | Nifty Bank | 10 | 63 | 5.477 | 0.5834 | 4.894 | 76.19 | 3.309e-06 | 6.601e-05 |
| Mercury-Saturn Trine | Nifty Bank | 20 | 63 | 8.09 | 1.172 | 6.917 | 74.6 | 1.996e-05 | 0.0002829 |
| Mercury-Saturn Trine | Nifty Midcap 100 | 1 | 63 | -0.07187 | 0.05397 | -0.1258 | 63.49 | 0.3413 | 0.5216 |
| Mercury-Saturn Trine | Nifty Midcap 100 | 3 | 63 | 0.1128 | 0.1609 | -0.04807 | 34.92 | 0.818 | 0.8988 |
| Mercury-Saturn Trine | Nifty Midcap 100 | 5 | 63 | 0.3727 | 0.266 | 0.1067 | 38.1 | 0.7074 | 0.829 |
| Mercury-Saturn Trine | Nifty Midcap 100 | 10 | 63 | 1.828 | 0.532 | 1.296 | 74.6 | 0.01461 | 0.05106 |
| Mercury-Saturn Trine | Nifty Midcap 100 | 20 | 63 | 2.373 | 1.065 | 1.309 | 74.6 | 0.1217 | 0.2515 |
| Mercury-Saturn Trine | Nifty Midcap 150 | 1 | 63 | 0.6132 | 0.05323 | 0.56 | 66.67 | 5.546e-05 | 0.0006246 |
| Mercury-Saturn Trine | Nifty Midcap 150 | 3 | 63 | 0.5362 | 0.1594 | 0.3767 | 73.02 | 0.03722 | 0.1038 |
| Mercury-Saturn Trine | Nifty Midcap 150 | 5 | 63 | 1.093 | 0.2642 | 0.8283 | 74.6 | 0.002136 | 0.0105 |
| Mercury-Saturn Trine | Nifty Midcap 150 | 10 | 63 | 1.888 | 0.5204 | 1.368 | 68.25 | 0.001441 | 0.007857 |
| Mercury-Saturn Trine | Nifty Midcap 150 | 20 | 63 | 2.218 | 1.047 | 1.171 | 73.02 | 0.1007 | 0.2177 |
| Mercury-Saturn Trine | BSE Sensex | 1 | 63 | 0.3046 | 0.05036 | 0.2542 | 60.32 | 0.04728 | 0.1231 |
| Mercury-Saturn Trine | BSE Sensex | 3 | 63 | 0.2024 | 0.1513 | 0.05105 | 58.73 | 0.8545 | 0.9213 |
| Mercury-Saturn Trine | BSE Sensex | 5 | 63 | 0.5154 | 0.2506 | 0.2649 | 63.49 | 0.4109 | 0.5926 |
| Mercury-Saturn Trine | BSE Sensex | 10 | 63 | 0.2733 | 0.4957 | -0.2223 | 55.56 | 0.6518 | 0.7932 |
| Mercury-Saturn Trine | BSE Sensex | 20 | 63 | 1.199 | 1.002 | 0.1973 | 60.32 | 0.806 | 0.8911 |
| Moon-Rahu Opposition | Nifty 50 | 1 | 57 | 0.2306 | 0.04492 | 0.1857 | 63.16 | 0.1749 | 0.3286 |
| Moon-Rahu Opposition | Nifty 50 | 3 | 57 | 1.841 | 0.1333 | 1.708 | 66.67 | 6.501e-05 | 0.0007006 |
| Moon-Rahu Opposition | Nifty 50 | 5 | 57 | 3.297 | 0.2178 | 3.079 | 68.42 | 1.705e-05 | 0.0002488 |
| Moon-Rahu Opposition | Nifty 50 | 10 | 57 | 4.659 | 0.4212 | 4.237 | 64.91 | 2.124e-05 | 0.0002972 |
| Moon-Rahu Opposition | Nifty 50 | 20 | 57 | 9.414 | 0.8264 | 8.588 | 71.93 | 7.423e-06 | 0.0001226 |
| Moon-Rahu Opposition | Nifty Bank | 1 | 57 | 0.6182 | 0.06023 | 0.558 | 61.4 | 0.01917 | 0.06436 |
| Moon-Rahu Opposition | Nifty Bank | 3 | 57 | 2.332 | 0.1819 | 2.15 | 66.67 | 0.0001313 | 0.001219 |
| Moon-Rahu Opposition | Nifty Bank | 5 | 57 | 3.726 | 0.3 | 3.426 | 57.89 | 4.114e-05 | 0.0004806 |
| Moon-Rahu Opposition | Nifty Bank | 10 | 57 | 5.815 | 0.5834 | 5.231 | 61.4 | 2.811e-05 | 0.000361 |
| Moon-Rahu Opposition | Nifty Bank | 20 | 57 | 8.23 | 1.172 | 7.058 | 66.67 | 9.754e-05 | 0.0009601 |
| Moon-Rahu Opposition | Nifty Midcap 100 | 1 | 57 | 0.1095 | 0.05397 | 0.05554 | 73.68 | 0.6993 | 0.8221 |
| Moon-Rahu Opposition | Nifty Midcap 100 | 3 | 57 | 0.1357 | 0.1609 | -0.02515 | 36.84 | 0.9224 | 0.9665 |
| Moon-Rahu Opposition | Nifty Midcap 100 | 5 | 57 | 0.1268 | 0.266 | -0.1392 | 43.86 | 0.6922 | 0.8183 |
| Moon-Rahu Opposition | Nifty Midcap 100 | 10 | 57 | 1.839 | 0.532 | 1.307 | 75.44 | 0.02755 | 0.0833 |
| Moon-Rahu Opposition | Nifty Midcap 100 | 20 | 57 | 1.797 | 1.065 | 0.7323 | 71.93 | 0.4519 | 0.6313 |
| Moon-Rahu Opposition | Nifty Midcap 150 | 1 | 57 | 0.1975 | 0.05323 | 0.1443 | 56.14 | 0.4413 | 0.6219 |
| Moon-Rahu Opposition | Nifty Midcap 150 | 3 | 57 | -0.13 | 0.1594 | -0.2894 | 61.4 | 0.2996 | 0.4757 |
| Moon-Rahu Opposition | Nifty Midcap 150 | 5 | 57 | 0.4116 | 0.2642 | 0.1474 | 66.67 | 0.6627 | 0.7996 |
| Moon-Rahu Opposition | Nifty Midcap 150 | 10 | 57 | 1.946 | 0.5204 | 1.426 | 59.65 | 0.02434 | 0.0762 |
| Moon-Rahu Opposition | Nifty Midcap 150 | 20 | 57 | 2.433 | 1.047 | 1.386 | 70.18 | 0.1046 | 0.2244 |
| Moon-Rahu Opposition | BSE Sensex | 1 | 57 | -0.2083 | 0.05036 | -0.2586 | 45.61 | 0.1764 | 0.3303 |
| Moon-Rahu Opposition | BSE Sensex | 3 | 57 | 0.1269 | 0.1513 | -0.02446 | 50.88 | 0.9424 | 0.9769 |
| Moon-Rahu Opposition | BSE Sensex | 5 | 57 | 0.5057 | 0.2506 | 0.2551 | 54.39 | 0.5676 | 0.7282 |
| Moon-Rahu Opposition | BSE Sensex | 10 | 57 | 0.9584 | 0.4957 | 0.4628 | 47.37 | 0.4219 | 0.6034 |
| Moon-Rahu Opposition | BSE Sensex | 20 | 57 | 1.69 | 1.002 | 0.6881 | 52.63 | 0.4146 | 0.5961 |
| Moon-Rahu Square | Nifty 50 | 1 | 113 | 0.1934 | 0.04492 | 0.1485 | 57.52 | 0.2995 | 0.4757 |
| Moon-Rahu Square | Nifty 50 | 3 | 113 | 1.213 | 0.1333 | 1.08 | 61.06 | 0.0009411 | 0.005549 |
| Moon-Rahu Square | Nifty 50 | 5 | 113 | 2.064 | 0.2178 | 1.846 | 60.18 | 0.0002204 | 0.00177 |
| Moon-Rahu Square | Nifty 50 | 10 | 113 | 2.893 | 0.4212 | 2.472 | 61.95 | 0.0001771 | 0.00153 |
| Moon-Rahu Square | Nifty 50 | 20 | 113 | 6.267 | 0.8264 | 5.441 | 61.95 | 1.078e-05 | 0.0001698 |
| Moon-Rahu Square | Nifty Bank | 1 | 113 | 0.4155 | 0.06023 | 0.3553 | 55.75 | 0.06972 | 0.1653 |
| Moon-Rahu Square | Nifty Bank | 3 | 113 | 1.603 | 0.1819 | 1.421 | 66.37 | 0.0008774 | 0.005307 |
| Moon-Rahu Square | Nifty Bank | 5 | 113 | 2.334 | 0.3 | 2.034 | 61.06 | 0.0005221 | 0.003559 |
| Moon-Rahu Square | Nifty Bank | 10 | 113 | 3.59 | 0.5834 | 3.007 | 61.95 | 0.0002162 | 0.001759 |
| Moon-Rahu Square | Nifty Bank | 20 | 113 | 5.18 | 1.172 | 4.008 | 61.95 | 0.0005855 | 0.003859 |
| Moon-Rahu Square | Nifty Midcap 100 | 1 | 113 | -0.02186 | 0.05397 | -0.07583 | 65.49 | 0.6006 | 0.7527 |
| Moon-Rahu Square | Nifty Midcap 100 | 3 | 113 | 0.01948 | 0.1609 | -0.1414 | 44.25 | 0.6021 | 0.7542 |
| Moon-Rahu Square | Nifty Midcap 100 | 5 | 113 | -0.142 | 0.266 | -0.408 | 38.05 | 0.1726 | 0.3264 |
| Moon-Rahu Square | Nifty Midcap 100 | 10 | 113 | 1.54 | 0.532 | 1.008 | 69.91 | 0.01524 | 0.05296 |
| Moon-Rahu Square | Nifty Midcap 100 | 20 | 113 | 2.136 | 1.065 | 1.071 | 69.91 | 0.07362 | 0.1722 |
| Moon-Rahu Square | Nifty Midcap 150 | 1 | 113 | 0.222 | 0.05323 | 0.1688 | 55.75 | 0.2766 | 0.4534 |
| Moon-Rahu Square | Nifty Midcap 150 | 3 | 113 | -0.04382 | 0.1594 | -0.2033 | 61.95 | 0.3514 | 0.5311 |
| Moon-Rahu Square | Nifty Midcap 150 | 5 | 113 | 0.08407 | 0.2642 | -0.1802 | 59.29 | 0.5178 | 0.691 |
| Moon-Rahu Square | Nifty Midcap 150 | 10 | 113 | 1.06 | 0.5204 | 0.5398 | 59.29 | 0.2086 | 0.3709 |
| Moon-Rahu Square | Nifty Midcap 150 | 20 | 113 | 1.148 | 1.047 | 0.1005 | 62.83 | 0.8564 | 0.9229 |
| Moon-Rahu Square | BSE Sensex | 1 | 113 | -0.0843 | 0.05036 | -0.1347 | 46.02 | 0.379 | 0.5608 |
| Moon-Rahu Square | BSE Sensex | 3 | 113 | -0.132 | 0.1513 | -0.2833 | 49.56 | 0.2441 | 0.4128 |
| Moon-Rahu Square | BSE Sensex | 5 | 113 | -0.183 | 0.2506 | -0.4335 | 50.44 | 0.1365 | 0.2741 |
| Moon-Rahu Square | BSE Sensex | 10 | 113 | 0.114 | 0.4957 | -0.3817 | 54.87 | 0.3598 | 0.5405 |
| Moon-Rahu Square | BSE Sensex | 20 | 113 | 0.6374 | 1.002 | -0.3643 | 55.75 | 0.5345 | 0.7026 |
| Moon-Rahu Trine | Nifty 50 | 1 | 119 | 0.2467 | 0.04492 | 0.2018 | 63.03 | 0.06505 | 0.1571 |
| Moon-Rahu Trine | Nifty 50 | 3 | 119 | 1.383 | 0.1333 | 1.25 | 59.66 | 2.318e-05 | 0.0003149 |
| Moon-Rahu Trine | Nifty 50 | 5 | 119 | 2.578 | 0.2178 | 2.36 | 67.23 | 1.818e-06 | 3.961e-05 |
| Moon-Rahu Trine | Nifty 50 | 10 | 119 | 3.758 | 0.4212 | 3.337 | 70.59 | 6.273e-08 | 2.425e-06 |
| Moon-Rahu Trine | Nifty 50 | 20 | 118 | 7.576 | 0.8264 | 6.749 | 72.88 | 5.924e-08 | 2.314e-06 |
| Moon-Rahu Trine | Nifty Bank | 1 | 119 | 0.596 | 0.06023 | 0.5357 | 63.87 | 0.0005466 | 0.003667 |
| Moon-Rahu Trine | Nifty Bank | 3 | 119 | 1.794 | 0.1819 | 1.612 | 58.82 | 2.854e-05 | 0.0003652 |
| Moon-Rahu Trine | Nifty Bank | 5 | 119 | 2.942 | 0.3 | 2.642 | 64.71 | 5.57e-06 | 9.852e-05 |
| Moon-Rahu Trine | Nifty Bank | 10 | 119 | 4.671 | 0.5834 | 4.088 | 64.71 | 3.903e-07 | 1.135e-05 |
| Moon-Rahu Trine | Nifty Bank | 20 | 118 | 6.725 | 1.172 | 5.553 | 71.19 | 5.115e-06 | 9.134e-05 |
| Moon-Rahu Trine | Nifty Midcap 100 | 1 | 119 | 0.1054 | 0.05397 | 0.0514 | 64.71 | 0.7374 | 0.8481 |
| Moon-Rahu Trine | Nifty Midcap 100 | 3 | 119 | 0.05658 | 0.1609 | -0.1043 | 39.5 | 0.6403 | 0.7844 |
| Moon-Rahu Trine | Nifty Midcap 100 | 5 | 119 | -0.1513 | 0.266 | -0.4174 | 36.13 | 0.09636 | 0.2109 |
| Moon-Rahu Trine | Nifty Midcap 100 | 10 | 119 | 1.671 | 0.532 | 1.139 | 70.59 | 0.003579 | 0.01627 |
| Moon-Rahu Trine | Nifty Midcap 100 | 20 | 118 | 1.79 | 1.065 | 0.7255 | 64.41 | 0.2425 | 0.411 |
| Moon-Rahu Trine | Nifty Midcap 150 | 1 | 119 | 0.3323 | 0.05323 | 0.279 | 60.5 | 0.03318 | 0.09549 |
| Moon-Rahu Trine | Nifty Midcap 150 | 3 | 119 | 0.05288 | 0.1594 | -0.1066 | 58.82 | 0.5217 | 0.6943 |
| Moon-Rahu Trine | Nifty Midcap 150 | 5 | 119 | 0.1995 | 0.2642 | -0.06474 | 63.03 | 0.8155 | 0.897 |
| Moon-Rahu Trine | Nifty Midcap 150 | 10 | 119 | 1.536 | 0.5204 | 1.015 | 65.55 | 0.009564 | 0.03638 |
| Moon-Rahu Trine | Nifty Midcap 150 | 20 | 118 | 1.682 | 1.047 | 0.6341 | 71.19 | 0.2578 | 0.4306 |
| Moon-Rahu Trine | BSE Sensex | 1 | 119 | 0.03557 | 0.05036 | -0.01479 | 52.1 | 0.9075 | 0.9584 |
| Moon-Rahu Trine | BSE Sensex | 3 | 119 | 0.1436 | 0.1513 | -0.007725 | 51.26 | 0.9688 | 0.9877 |
| Moon-Rahu Trine | BSE Sensex | 5 | 119 | 0.1934 | 0.2506 | -0.05719 | 57.14 | 0.8387 | 0.9128 |
| Moon-Rahu Trine | BSE Sensex | 10 | 119 | 0.7486 | 0.4957 | 0.2529 | 61.34 | 0.5137 | 0.6873 |
| Moon-Rahu Trine | BSE Sensex | 20 | 118 | 0.8351 | 1.002 | -0.1666 | 65.25 | 0.7819 | 0.8761 |
| Moon-Saturn Opposition | Nifty 50 | 1 | 57 | 0.4476 | 0.04492 | 0.4027 | 66.67 | 0.03978 | 0.1081 |
| Moon-Saturn Opposition | Nifty 50 | 3 | 57 | 2.226 | 0.1333 | 2.092 | 73.68 | 2.415e-06 | 5.088e-05 |
| Moon-Saturn Opposition | Nifty 50 | 5 | 57 | 3.553 | 0.2178 | 3.336 | 75.44 | 1.6e-05 | 0.0002391 |
| Moon-Saturn Opposition | Nifty 50 | 10 | 57 | 5.079 | 0.4212 | 4.658 | 80.7 | 4.719e-07 | 1.273e-05 |
| Moon-Saturn Opposition | Nifty 50 | 20 | 57 | 9.384 | 0.8264 | 8.558 | 82.46 | 1.339e-06 | 3.063e-05 |
| Moon-Saturn Opposition | Nifty Bank | 1 | 57 | 0.7961 | 0.06023 | 0.7359 | 66.67 | 0.004401 | 0.0191 |
| Moon-Saturn Opposition | Nifty Bank | 3 | 57 | 2.863 | 0.1819 | 2.681 | 71.93 | 7.195e-06 | 0.0001205 |
| Moon-Saturn Opposition | Nifty Bank | 5 | 57 | 4.269 | 0.3 | 3.969 | 75.44 | 1.62e-05 | 0.000241 |
| Moon-Saturn Opposition | Nifty Bank | 10 | 57 | 6.874 | 0.5834 | 6.291 | 80.7 | 1.318e-07 | 4.534e-06 |
| Moon-Saturn Opposition | Nifty Bank | 20 | 57 | 9.282 | 1.172 | 8.109 | 77.19 | 4.777e-06 | 8.696e-05 |
| Moon-Saturn Opposition | Nifty Midcap 100 | 1 | 57 | 0.05068 | 0.05397 | -0.003286 | 64.91 | 0.9847 | 0.9948 |
| Moon-Saturn Opposition | Nifty Midcap 100 | 3 | 57 | 0.4055 | 0.1609 | 0.2446 | 52.63 | 0.3658 | 0.5471 |
| Moon-Saturn Opposition | Nifty Midcap 100 | 5 | 57 | 0.7224 | 0.266 | 0.4564 | 59.65 | 0.2032 | 0.3645 |
| Moon-Saturn Opposition | Nifty Midcap 100 | 10 | 57 | 2.649 | 0.532 | 2.117 | 80.7 | 0.0001745 | 0.001515 |
| Moon-Saturn Opposition | Nifty Midcap 100 | 20 | 57 | 3.79 | 1.065 | 2.725 | 75.44 | 0.0004067 | 0.002927 |
| Moon-Saturn Opposition | Nifty Midcap 150 | 1 | 57 | 0.3619 | 0.05323 | 0.3087 | 61.4 | 0.1657 | 0.3173 |
| Moon-Saturn Opposition | Nifty Midcap 150 | 3 | 57 | 0.7198 | 0.1594 | 0.5603 | 66.67 | 0.06552 | 0.1578 |
| Moon-Saturn Opposition | Nifty Midcap 150 | 5 | 57 | 1.142 | 0.2642 | 0.8776 | 70.18 | 0.09457 | 0.2084 |
| Moon-Saturn Opposition | Nifty Midcap 150 | 10 | 57 | 2.519 | 0.5204 | 1.998 | 77.19 | 0.0007819 | 0.004855 |
| Moon-Saturn Opposition | Nifty Midcap 150 | 20 | 57 | 2.986 | 1.047 | 1.939 | 75.44 | 0.03002 | 0.08877 |
| Moon-Saturn Opposition | BSE Sensex | 1 | 57 | 0.2204 | 0.05036 | 0.1701 | 54.39 | 0.4347 | 0.6168 |
| Moon-Saturn Opposition | BSE Sensex | 3 | 57 | 0.7345 | 0.1513 | 0.5832 | 61.4 | 0.07633 | 0.1767 |
| Moon-Saturn Opposition | BSE Sensex | 5 | 57 | 0.9701 | 0.2506 | 0.7195 | 66.67 | 0.1648 | 0.3163 |
| Moon-Saturn Opposition | BSE Sensex | 10 | 57 | 1.789 | 0.4957 | 1.293 | 75.44 | 0.02012 | 0.06619 |
| Moon-Saturn Opposition | BSE Sensex | 20 | 57 | 2.176 | 1.002 | 1.174 | 68.42 | 0.192 | 0.3503 |
| Moon-Saturn Square | Nifty 50 | 1 | 109 | 0.3015 | 0.04492 | 0.2566 | 64.22 | 0.00327 | 0.01508 |
| Moon-Saturn Square | Nifty 50 | 3 | 109 | 1.67 | 0.1333 | 1.536 | 64.22 | 1.596e-07 | 5.323e-06 |
| Moon-Saturn Square | Nifty 50 | 5 | 109 | 2.808 | 0.2178 | 2.59 | 65.14 | 1.469e-07 | 4.961e-06 |
| Moon-Saturn Square | Nifty 50 | 10 | 109 | 3.774 | 0.4212 | 3.353 | 68.81 | 2.19e-07 | 6.96e-06 |
| Moon-Saturn Square | Nifty 50 | 20 | 108 | 7.804 | 0.8264 | 6.977 | 72.22 | 4.89e-08 | 1.951e-06 |
| Moon-Saturn Square | Nifty Bank | 1 | 109 | 0.702 | 0.06023 | 0.6418 | 63.3 | 2.687e-05 | 0.0003501 |
| Moon-Saturn Square | Nifty Bank | 3 | 109 | 2.327 | 0.1819 | 2.145 | 68.81 | 1.757e-08 | 8.558e-07 |
| Moon-Saturn Square | Nifty Bank | 5 | 109 | 3.277 | 0.3 | 2.977 | 65.14 | 1.607e-07 | 5.323e-06 |
| Moon-Saturn Square | Nifty Bank | 10 | 109 | 4.743 | 0.5834 | 4.16 | 68.81 | 4.351e-07 | 1.222e-05 |
| Moon-Saturn Square | Nifty Bank | 20 | 108 | 7.27 | 1.172 | 6.098 | 72.22 | 1.292e-07 | 4.485e-06 |
| Moon-Saturn Square | Nifty Midcap 100 | 1 | 109 | -0.04592 | 0.05397 | -0.09988 | 66.06 | 0.2692 | 0.4445 |
| Moon-Saturn Square | Nifty Midcap 100 | 3 | 109 | -0.1259 | 0.1609 | -0.2868 | 32.11 | 0.06778 | 0.1617 |
| Moon-Saturn Square | Nifty Midcap 100 | 5 | 109 | -0.0793 | 0.266 | -0.3453 | 33.94 | 0.1432 | 0.2838 |
| Moon-Saturn Square | Nifty Midcap 100 | 10 | 109 | 1.438 | 0.532 | 0.9063 | 66.97 | 0.01666 | 0.05712 |
| Moon-Saturn Square | Nifty Midcap 100 | 20 | 108 | 2.29 | 1.065 | 1.225 | 68.52 | 0.04328 | 0.115 |
| Moon-Saturn Square | Nifty Midcap 150 | 1 | 109 | 0.393 | 0.05323 | 0.3398 | 57.8 | 0.002695 | 0.01282 |
| Moon-Saturn Square | Nifty Midcap 150 | 3 | 109 | 0.21 | 0.1594 | 0.05056 | 64.22 | 0.7247 | 0.8398 |
| Moon-Saturn Square | Nifty Midcap 150 | 5 | 109 | 0.469 | 0.2642 | 0.2047 | 64.22 | 0.318 | 0.4952 |
| Moon-Saturn Square | Nifty Midcap 150 | 10 | 109 | 1.457 | 0.5204 | 0.9368 | 66.97 | 0.01115 | 0.04174 |
| Moon-Saturn Square | Nifty Midcap 150 | 20 | 108 | 1.561 | 1.047 | 0.5135 | 68.52 | 0.2873 | 0.4622 |
| Moon-Saturn Square | BSE Sensex | 1 | 109 | -0.01303 | 0.05036 | -0.06339 | 49.54 | 0.6096 | 0.7591 |
| Moon-Saturn Square | BSE Sensex | 3 | 109 | -0.07477 | 0.1513 | -0.2261 | 52.29 | 0.3237 | 0.5018 |
| Moon-Saturn Square | BSE Sensex | 5 | 109 | -0.01587 | 0.2506 | -0.2664 | 55.05 | 0.3649 | 0.5465 |
| Moon-Saturn Square | BSE Sensex | 10 | 109 | 0.04046 | 0.4957 | -0.4552 | 55.96 | 0.3401 | 0.5208 |
| Moon-Saturn Square | BSE Sensex | 20 | 108 | 0.5864 | 1.002 | -0.4153 | 57.41 | 0.5086 | 0.6836 |
| Moon-Saturn Trine | Nifty 50 | 1 | 104 | 0.3437 | 0.04492 | 0.2988 | 64.42 | 0.0241 | 0.07576 |
| Moon-Saturn Trine | Nifty 50 | 3 | 104 | 1.611 | 0.1333 | 1.477 | 72.12 | 5.672e-06 | 9.94e-05 |
| Moon-Saturn Trine | Nifty 50 | 5 | 104 | 2.697 | 0.2178 | 2.479 | 69.23 | 3.45e-06 | 6.82e-05 |
| Moon-Saturn Trine | Nifty 50 | 10 | 104 | 3.721 | 0.4212 | 3.299 | 73.08 | 6.075e-07 | 1.55e-05 |
| Moon-Saturn Trine | Nifty 50 | 20 | 104 | 7.494 | 0.8264 | 6.667 | 69.23 | 8.965e-08 | 3.362e-06 |
| Moon-Saturn Trine | Nifty Bank | 1 | 104 | 0.5644 | 0.06023 | 0.5042 | 58.65 | 0.007129 | 0.02844 |
| Moon-Saturn Trine | Nifty Bank | 3 | 104 | 1.844 | 0.1819 | 1.662 | 64.42 | 7.486e-05 | 0.0007798 |
| Moon-Saturn Trine | Nifty Bank | 5 | 104 | 2.875 | 0.3 | 2.575 | 64.42 | 6.324e-05 | 0.0006955 |
| Moon-Saturn Trine | Nifty Bank | 10 | 104 | 4.143 | 0.5834 | 3.559 | 66.35 | 5.299e-05 | 0.0006021 |
| Moon-Saturn Trine | Nifty Bank | 20 | 104 | 6.283 | 1.172 | 5.111 | 66.35 | 2.543e-05 | 0.0003346 |
| Moon-Saturn Trine | Nifty Midcap 100 | 1 | 104 | 0.09187 | 0.05397 | 0.0379 | 73.08 | 0.7776 | 0.8736 |
| Moon-Saturn Trine | Nifty Midcap 100 | 3 | 104 | 0.2712 | 0.1609 | 0.1103 | 50 | 0.6453 | 0.7892 |
| Moon-Saturn Trine | Nifty Midcap 100 | 5 | 104 | 0.4149 | 0.266 | 0.1489 | 48.08 | 0.6408 | 0.7845 |
| Moon-Saturn Trine | Nifty Midcap 100 | 10 | 104 | 1.994 | 0.532 | 1.462 | 74.04 | 0.0003574 | 0.002638 |
| Moon-Saturn Trine | Nifty Midcap 100 | 20 | 104 | 2.856 | 1.065 | 1.791 | 75.96 | 0.001341 | 0.007403 |
| Moon-Saturn Trine | Nifty Midcap 150 | 1 | 104 | 0.3749 | 0.05323 | 0.3217 | 60.58 | 0.02376 | 0.07488 |
| Moon-Saturn Trine | Nifty Midcap 150 | 3 | 104 | 0.3742 | 0.1594 | 0.2148 | 72.12 | 0.2937 | 0.4701 |
| Moon-Saturn Trine | Nifty Midcap 150 | 5 | 104 | 0.5717 | 0.2642 | 0.3075 | 71.15 | 0.3104 | 0.4872 |
| Moon-Saturn Trine | Nifty Midcap 150 | 10 | 104 | 1.688 | 0.5204 | 1.167 | 73.08 | 0.003713 | 0.01671 |
| Moon-Saturn Trine | Nifty Midcap 150 | 20 | 104 | 1.974 | 1.047 | 0.9265 | 69.23 | 0.04169 | 0.1118 |
| Moon-Saturn Trine | BSE Sensex | 1 | 104 | 0.04655 | 0.05036 | -0.003808 | 54.81 | 0.9774 | 0.9906 |
| Moon-Saturn Trine | BSE Sensex | 3 | 104 | 0.2456 | 0.1513 | 0.09427 | 60.58 | 0.6811 | 0.8116 |
| Moon-Saturn Trine | BSE Sensex | 5 | 104 | 0.2497 | 0.2506 | -0.0008682 | 59.62 | 0.9979 | 0.9993 |
| Moon-Saturn Trine | BSE Sensex | 10 | 104 | 0.3764 | 0.4957 | -0.1192 | 61.54 | 0.7744 | 0.8721 |
| Moon-Saturn Trine | BSE Sensex | 20 | 104 | 0.7785 | 1.002 | -0.2231 | 54.81 | 0.6802 | 0.8108 |
| Moon-Sun Opposition | Nifty 50 | 1 | 63 | 0.4048 | 0.04492 | 0.3599 | 73.02 | 0.002005 | 0.01008 |
| Moon-Sun Opposition | Nifty 50 | 3 | 63 | 1.961 | 0.1333 | 1.828 | 71.43 | 7.09e-06 | 0.0001192 |
| Moon-Sun Opposition | Nifty 50 | 5 | 63 | 2.945 | 0.2178 | 2.727 | 63.49 | 2.51e-05 | 0.0003325 |
| Moon-Sun Opposition | Nifty 50 | 10 | 63 | 3.869 | 0.4212 | 3.448 | 69.84 | 5.079e-05 | 0.0005789 |
| Moon-Sun Opposition | Nifty 50 | 20 | 63 | 7.937 | 0.8264 | 7.11 | 73.02 | 2.972e-05 | 0.0003778 |
| Moon-Sun Opposition | Nifty Bank | 1 | 63 | 0.7839 | 0.06023 | 0.7236 | 74.6 | 0.0007637 | 0.004773 |
| Moon-Sun Opposition | Nifty Bank | 3 | 63 | 2.444 | 0.1819 | 2.262 | 69.84 | 0.0001151 | 0.001101 |
| Moon-Sun Opposition | Nifty Bank | 5 | 63 | 3.349 | 0.3 | 3.049 | 66.67 | 6.491e-05 | 0.0007006 |
| Moon-Sun Opposition | Nifty Bank | 10 | 63 | 4.749 | 0.5834 | 4.166 | 68.25 | 0.0001118 | 0.001075 |
| Moon-Sun Opposition | Nifty Bank | 20 | 63 | 6.849 | 1.172 | 5.677 | 65.08 | 0.0002139 | 0.001759 |
| Moon-Sun Opposition | Nifty Midcap 100 | 1 | 63 | 0.0478 | 0.05397 | -0.006169 | 65.08 | 0.9679 | 0.9874 |
| Moon-Sun Opposition | Nifty Midcap 100 | 3 | 63 | 0.3815 | 0.1609 | 0.2207 | 44.44 | 0.4239 | 0.6054 |
| Moon-Sun Opposition | Nifty Midcap 100 | 5 | 63 | 0.01965 | 0.266 | -0.2464 | 41.27 | 0.392 | 0.5753 |
| Moon-Sun Opposition | Nifty Midcap 100 | 10 | 63 | 1.567 | 0.532 | 1.035 | 65.08 | 0.1036 | 0.2228 |
| Moon-Sun Opposition | Nifty Midcap 100 | 20 | 63 | 2.806 | 1.065 | 1.742 | 71.43 | 0.07579 | 0.1758 |
| Moon-Sun Opposition | Nifty Midcap 150 | 1 | 63 | 0.4806 | 0.05323 | 0.4274 | 71.43 | 0.001324 | 0.007332 |
| Moon-Sun Opposition | Nifty Midcap 150 | 3 | 63 | 0.5732 | 0.1594 | 0.4137 | 76.19 | 0.09154 | 0.2033 |
| Moon-Sun Opposition | Nifty Midcap 150 | 5 | 63 | 0.6779 | 0.2642 | 0.4137 | 63.49 | 0.1333 | 0.2699 |
| Moon-Sun Opposition | Nifty Midcap 150 | 10 | 63 | 1.744 | 0.5204 | 1.224 | 69.84 | 0.00814 | 0.03183 |
| Moon-Sun Opposition | Nifty Midcap 150 | 20 | 63 | 2.135 | 1.047 | 1.088 | 73.02 | 0.1253 | 0.2569 |
| Moon-Sun Opposition | BSE Sensex | 1 | 63 | 0.1373 | 0.05036 | 0.08699 | 57.14 | 0.5305 | 0.7014 |
| Moon-Sun Opposition | BSE Sensex | 3 | 63 | 0.6051 | 0.1513 | 0.4538 | 61.9 | 0.1219 | 0.2517 |
| Moon-Sun Opposition | BSE Sensex | 5 | 63 | 0.4255 | 0.2506 | 0.1749 | 52.38 | 0.5894 | 0.7459 |
| Moon-Sun Opposition | BSE Sensex | 10 | 63 | 0.5874 | 0.4957 | 0.09177 | 60.32 | 0.8428 | 0.9153 |
| Moon-Sun Opposition | BSE Sensex | 20 | 63 | 1.298 | 1.002 | 0.2965 | 63.49 | 0.683 | 0.8123 |
| Moon-Sun Square | Nifty 50 | 1 | 114 | 0.1101 | 0.04492 | 0.06516 | 57.02 | 0.5989 | 0.7519 |
| Moon-Sun Square | Nifty 50 | 3 | 114 | 1.372 | 0.1333 | 1.238 | 64.04 | 0.0001632 | 0.001443 |
| Moon-Sun Square | Nifty 50 | 5 | 114 | 2.451 | 0.2178 | 2.234 | 64.04 | 2.373e-05 | 0.000319 |
| Moon-Sun Square | Nifty 50 | 10 | 114 | 3.389 | 0.4212 | 2.968 | 62.28 | 9.582e-06 | 0.0001542 |
| Moon-Sun Square | Nifty 50 | 20 | 114 | 7.479 | 0.8264 | 6.653 | 72.81 | 3.722e-08 | 1.568e-06 |
| Moon-Sun Square | Nifty Bank | 1 | 114 | 0.3417 | 0.06023 | 0.2814 | 61.4 | 0.148 | 0.2916 |
| Moon-Sun Square | Nifty Bank | 3 | 114 | 1.776 | 0.1819 | 1.594 | 64.04 | 0.0001555 | 0.001392 |
| Moon-Sun Square | Nifty Bank | 5 | 114 | 2.702 | 0.3 | 2.402 | 63.16 | 0.000137 | 0.001257 |
| Moon-Sun Square | Nifty Bank | 10 | 114 | 4.264 | 0.5834 | 3.681 | 64.91 | 2.28e-05 | 0.000314 |
| Moon-Sun Square | Nifty Bank | 20 | 114 | 7.042 | 1.172 | 5.869 | 72.81 | 1.361e-07 | 4.64e-06 |
| Moon-Sun Square | Nifty Midcap 100 | 1 | 114 | -0.2811 | 0.05397 | -0.3351 | 53.51 | 0.008682 | 0.03363 |
| Moon-Sun Square | Nifty Midcap 100 | 3 | 114 | -0.03094 | 0.1609 | -0.1918 | 38.6 | 0.4165 | 0.5986 |
| Moon-Sun Square | Nifty Midcap 100 | 5 | 114 | 0.2145 | 0.266 | -0.05147 | 38.6 | 0.8717 | 0.9339 |
| Moon-Sun Square | Nifty Midcap 100 | 10 | 114 | 1.147 | 0.532 | 0.6153 | 64.04 | 0.1156 | 0.2413 |
| Moon-Sun Square | Nifty Midcap 100 | 20 | 114 | 2.486 | 1.065 | 1.421 | 64.91 | 0.02166 | 0.06996 |
| Moon-Sun Square | Nifty Midcap 150 | 1 | 114 | 0.1699 | 0.05323 | 0.1167 | 55.26 | 0.3971 | 0.5805 |
| Moon-Sun Square | Nifty Midcap 150 | 3 | 114 | 0.06923 | 0.1594 | -0.09021 | 61.4 | 0.6919 | 0.8183 |
| Moon-Sun Square | Nifty Midcap 150 | 5 | 114 | 0.3634 | 0.2642 | 0.09916 | 64.91 | 0.7591 | 0.8618 |
| Moon-Sun Square | Nifty Midcap 150 | 10 | 114 | 1.347 | 0.5204 | 0.8269 | 61.4 | 0.05924 | 0.1471 |
| Moon-Sun Square | Nifty Midcap 150 | 20 | 114 | 2.033 | 1.047 | 0.986 | 72.81 | 0.0582 | 0.1448 |
| Moon-Sun Square | BSE Sensex | 1 | 114 | -0.08326 | 0.05036 | -0.1336 | 50.88 | 0.3113 | 0.4884 |
| Moon-Sun Square | BSE Sensex | 3 | 114 | 0.1197 | 0.1513 | -0.03163 | 56.14 | 0.8989 | 0.9515 |
| Moon-Sun Square | BSE Sensex | 5 | 114 | 0.2878 | 0.2506 | 0.03721 | 57.02 | 0.9157 | 0.9627 |
| Moon-Sun Square | BSE Sensex | 10 | 114 | 0.7078 | 0.4957 | 0.2122 | 59.65 | 0.6318 | 0.7778 |
| Moon-Sun Square | BSE Sensex | 20 | 114 | 1.802 | 1.002 | 0.7999 | 67.54 | 0.1398 | 0.2786 |
| Moon-Sun Trine | Nifty 50 | 1 | 108 | 0.381 | 0.04492 | 0.3361 | 67.59 | 0.0001975 | 0.001672 |
| Moon-Sun Trine | Nifty 50 | 3 | 108 | 1.804 | 0.1333 | 1.671 | 68.52 | 2.52e-08 | 1.139e-06 |
| Moon-Sun Trine | Nifty 50 | 5 | 108 | 3.044 | 0.2178 | 2.826 | 64.81 | 2.155e-08 | 9.977e-07 |
| Moon-Sun Trine | Nifty 50 | 10 | 108 | 4.054 | 0.4212 | 3.632 | 71.3 | 9.687e-08 | 3.493e-06 |
| Moon-Sun Trine | Nifty 50 | 20 | 107 | 8.441 | 0.8264 | 7.614 | 73.83 | 7.125e-09 | 3.611e-07 |
| Moon-Sun Trine | Nifty Bank | 1 | 108 | 0.6475 | 0.06023 | 0.5873 | 62.96 | 0.0003353 | 0.002515 |
| Moon-Sun Trine | Nifty Bank | 3 | 108 | 2.214 | 0.1819 | 2.032 | 62.96 | 4.562e-07 | 1.258e-05 |
| Moon-Sun Trine | Nifty Bank | 5 | 108 | 3.218 | 0.3 | 2.918 | 64.81 | 1.324e-06 | 3.046e-05 |
| Moon-Sun Trine | Nifty Bank | 10 | 108 | 4.81 | 0.5834 | 4.227 | 72.22 | 1.582e-06 | 3.469e-05 |
| Moon-Sun Trine | Nifty Bank | 20 | 107 | 7.072 | 1.172 | 5.9 | 72.9 | 3.305e-06 | 6.601e-05 |
| Moon-Sun Trine | Nifty Midcap 100 | 1 | 108 | 0.06571 | 0.05397 | 0.01175 | 67.59 | 0.9035 | 0.9553 |
| Moon-Sun Trine | Nifty Midcap 100 | 3 | 108 | 0.1966 | 0.1609 | 0.03576 | 41.67 | 0.8488 | 0.9183 |
| Moon-Sun Trine | Nifty Midcap 100 | 5 | 108 | 0.1954 | 0.266 | -0.07063 | 34.26 | 0.7899 | 0.8811 |
| Moon-Sun Trine | Nifty Midcap 100 | 10 | 108 | 1.734 | 0.532 | 1.202 | 75.93 | 0.004362 | 0.019 |
| Moon-Sun Trine | Nifty Midcap 100 | 20 | 107 | 2.477 | 1.065 | 1.413 | 72.9 | 0.0163 | 0.05613 |
| Moon-Sun Trine | Nifty Midcap 150 | 1 | 108 | 0.4818 | 0.05323 | 0.4286 | 65.74 | 8.151e-05 | 0.0008329 |
| Moon-Sun Trine | Nifty Midcap 150 | 3 | 108 | 0.2526 | 0.1594 | 0.09319 | 65.74 | 0.4999 | 0.6765 |
| Moon-Sun Trine | Nifty Midcap 150 | 5 | 108 | 0.5075 | 0.2642 | 0.2432 | 62.96 | 0.2368 | 0.4046 |
| Moon-Sun Trine | Nifty Midcap 150 | 10 | 108 | 1.696 | 0.5204 | 1.175 | 71.3 | 0.003406 | 0.01557 |
| Moon-Sun Trine | Nifty Midcap 150 | 20 | 107 | 1.881 | 1.047 | 0.8333 | 73.83 | 0.07576 | 0.1758 |
| Moon-Sun Trine | BSE Sensex | 1 | 108 | 0.06284 | 0.05036 | 0.01248 | 54.63 | 0.8966 | 0.95 |
| Moon-Sun Trine | BSE Sensex | 3 | 108 | 0.07435 | 0.1513 | -0.07696 | 54.63 | 0.6644 | 0.8011 |
| Moon-Sun Trine | BSE Sensex | 5 | 108 | -0.1337 | 0.2506 | -0.3843 | 47.22 | 0.1253 | 0.2569 |
| Moon-Sun Trine | BSE Sensex | 10 | 108 | 0.1895 | 0.4957 | -0.3062 | 61.11 | 0.4337 | 0.616 |
| Moon-Sun Trine | BSE Sensex | 20 | 107 | 0.5568 | 1.002 | -0.4448 | 60.75 | 0.434 | 0.6162 |
| Moon-Venus Opposition | Nifty 50 | 1 | 61 | 0.1801 | 0.04492 | 0.1352 | 59.02 | 0.4036 | 0.5858 |
| Moon-Venus Opposition | Nifty 50 | 3 | 61 | 1.437 | 0.1333 | 1.304 | 59.02 | 0.002204 | 0.01075 |
| Moon-Venus Opposition | Nifty 50 | 5 | 61 | 2.462 | 0.2178 | 2.244 | 67.21 | 0.0007116 | 0.0045 |
| Moon-Venus Opposition | Nifty 50 | 10 | 61 | 3.878 | 0.4212 | 3.457 | 70.49 | 2.369e-05 | 0.000319 |
| Moon-Venus Opposition | Nifty 50 | 20 | 61 | 7.306 | 0.8264 | 6.48 | 73.77 | 7.153e-05 | 0.0007577 |
| Moon-Venus Opposition | Nifty Bank | 1 | 61 | 0.475 | 0.06023 | 0.4148 | 60.66 | 0.08734 | 0.1952 |
| Moon-Venus Opposition | Nifty Bank | 3 | 61 | 1.734 | 0.1819 | 1.552 | 62.3 | 0.0057 | 0.0238 |
| Moon-Venus Opposition | Nifty Bank | 5 | 61 | 2.902 | 0.3 | 2.602 | 65.57 | 0.001061 | 0.006216 |
| Moon-Venus Opposition | Nifty Bank | 10 | 61 | 5.022 | 0.5834 | 4.439 | 73.77 | 1.951e-05 | 0.0002793 |
| Moon-Venus Opposition | Nifty Bank | 20 | 61 | 7.147 | 1.172 | 5.974 | 75.41 | 4.307e-05 | 0.0005 |
| Moon-Venus Opposition | Nifty Midcap 100 | 1 | 61 | 0.05115 | 0.05397 | -0.002815 | 62.3 | 0.9852 | 0.9948 |
| Moon-Venus Opposition | Nifty Midcap 100 | 3 | 61 | 0.1501 | 0.1609 | -0.01075 | 42.62 | 0.9677 | 0.9874 |
| Moon-Venus Opposition | Nifty Midcap 100 | 5 | 61 | -0.07769 | 0.266 | -0.3437 | 36.07 | 0.3261 | 0.5038 |
| Moon-Venus Opposition | Nifty Midcap 100 | 10 | 61 | 1.557 | 0.532 | 1.025 | 72.13 | 0.109 | 0.2312 |
| Moon-Venus Opposition | Nifty Midcap 100 | 20 | 61 | 1.99 | 1.065 | 0.9254 | 68.85 | 0.373 | 0.5544 |
| Moon-Venus Opposition | Nifty Midcap 150 | 1 | 61 | 0.2359 | 0.05323 | 0.1827 | 59.02 | 0.2979 | 0.4747 |
| Moon-Venus Opposition | Nifty Midcap 150 | 3 | 61 | 0.2416 | 0.1594 | 0.08213 | 60.66 | 0.763 | 0.8652 |
| Moon-Venus Opposition | Nifty Midcap 150 | 5 | 61 | 0.4496 | 0.2642 | 0.1853 | 65.57 | 0.6061 | 0.7563 |
| Moon-Venus Opposition | Nifty Midcap 150 | 10 | 61 | 2.04 | 0.5204 | 1.52 | 67.21 | 0.001324 | 0.007332 |
| Moon-Venus Opposition | Nifty Midcap 150 | 20 | 61 | 2.091 | 1.047 | 1.044 | 70.49 | 0.1694 | 0.3229 |
| Moon-Venus Opposition | BSE Sensex | 1 | 61 | -0.1086 | 0.05036 | -0.159 | 45.9 | 0.3165 | 0.4937 |
| Moon-Venus Opposition | BSE Sensex | 3 | 61 | 0.1058 | 0.1513 | -0.04551 | 55.74 | 0.877 | 0.9372 |
| Moon-Venus Opposition | BSE Sensex | 5 | 61 | -0.02295 | 0.2506 | -0.2735 | 55.74 | 0.5014 | 0.6771 |
| Moon-Venus Opposition | BSE Sensex | 10 | 61 | 0.476 | 0.4957 | -0.01968 | 57.38 | 0.9699 | 0.9884 |
| Moon-Venus Opposition | BSE Sensex | 20 | 61 | 0.6372 | 1.002 | -0.3644 | 59.02 | 0.683 | 0.8123 |
| Moon-Venus Square | Nifty 50 | 1 | 117 | 0.0141 | 0.04492 | -0.03082 | 55.56 | 0.8503 | 0.9192 |
| Moon-Venus Square | Nifty 50 | 3 | 117 | 1.409 | 0.1333 | 1.276 | 64.1 | 0.0002684 | 0.002088 |
| Moon-Venus Square | Nifty 50 | 5 | 117 | 2.626 | 0.2178 | 2.408 | 66.67 | 1.314e-06 | 3.046e-05 |
| Moon-Venus Square | Nifty 50 | 10 | 117 | 3.403 | 0.4212 | 2.982 | 70.94 | 6.762e-06 | 0.0001152 |
| Moon-Venus Square | Nifty 50 | 20 | 116 | 6.601 | 0.8264 | 5.775 | 62.93 | 4.878e-06 | 8.837e-05 |
| Moon-Venus Square | Nifty Bank | 1 | 117 | 0.2723 | 0.06023 | 0.2121 | 61.54 | 0.3466 | 0.5257 |
| Moon-Venus Square | Nifty Bank | 3 | 117 | 1.741 | 0.1819 | 1.56 | 59.83 | 0.0004527 | 0.003197 |
| Moon-Venus Square | Nifty Bank | 5 | 117 | 3.006 | 0.3 | 2.706 | 67.52 | 1.005e-05 | 0.0001611 |
| Moon-Venus Square | Nifty Bank | 10 | 117 | 4.048 | 0.5834 | 3.465 | 69.23 | 6.027e-05 | 0.0006706 |
| Moon-Venus Square | Nifty Bank | 20 | 116 | 5.664 | 1.172 | 4.491 | 61.21 | 0.0002049 | 0.0017 |
| Moon-Venus Square | Nifty Midcap 100 | 1 | 117 | -0.2462 | 0.05397 | -0.3001 | 57.26 | 0.04665 | 0.1219 |
| Moon-Venus Square | Nifty Midcap 100 | 3 | 117 | -0.04598 | 0.1609 | -0.2068 | 38.46 | 0.4442 | 0.6245 |
| Moon-Venus Square | Nifty Midcap 100 | 5 | 117 | 0.1116 | 0.266 | -0.1544 | 42.74 | 0.5987 | 0.7519 |
| Moon-Venus Square | Nifty Midcap 100 | 10 | 117 | 1.437 | 0.532 | 0.9055 | 70.94 | 0.05648 | 0.1414 |
| Moon-Venus Square | Nifty Midcap 100 | 20 | 116 | 2.248 | 1.065 | 1.184 | 65.52 | 0.06907 | 0.1642 |
| Moon-Venus Square | Nifty Midcap 150 | 1 | 117 | 0.1245 | 0.05323 | 0.0713 | 56.41 | 0.6724 | 0.8068 |
| Moon-Venus Square | Nifty Midcap 150 | 3 | 117 | 0.2183 | 0.1594 | 0.05889 | 62.39 | 0.8209 | 0.9008 |
| Moon-Venus Square | Nifty Midcap 150 | 5 | 117 | 0.7304 | 0.2642 | 0.4661 | 68.38 | 0.1284 | 0.2622 |
| Moon-Venus Square | Nifty Midcap 150 | 10 | 117 | 1.473 | 0.5204 | 0.9528 | 69.23 | 0.04115 | 0.1109 |
| Moon-Venus Square | Nifty Midcap 150 | 20 | 116 | 1.473 | 1.047 | 0.4259 | 63.79 | 0.5319 | 0.7014 |
| Moon-Venus Square | BSE Sensex | 1 | 117 | -0.2959 | 0.05036 | -0.3463 | 41.03 | 0.03625 | 0.1019 |
| Moon-Venus Square | BSE Sensex | 3 | 117 | 0.0004271 | 0.1513 | -0.1509 | 46.15 | 0.5887 | 0.7459 |
| Moon-Venus Square | BSE Sensex | 5 | 117 | 0.2499 | 0.2506 | -0.0006955 | 51.28 | 0.9982 | 0.9993 |
| Moon-Venus Square | BSE Sensex | 10 | 117 | 0.2843 | 0.4957 | -0.2114 | 59.83 | 0.6418 | 0.7855 |
| Moon-Venus Square | BSE Sensex | 20 | 116 | 0.3244 | 1.002 | -0.6773 | 50.86 | 0.3257 | 0.5037 |
| Moon-Venus Trine | Nifty 50 | 1 | 93 | 0.3777 | 0.04492 | 0.3328 | 69.89 | 0.001481 | 0.008015 |
| Moon-Venus Trine | Nifty 50 | 3 | 93 | 1.511 | 0.1333 | 1.378 | 73.12 | 1.548e-05 | 0.0002322 |
| Moon-Venus Trine | Nifty 50 | 5 | 93 | 2.486 | 0.2178 | 2.268 | 68.82 | 6.398e-05 | 0.0006995 |
| Moon-Venus Trine | Nifty 50 | 10 | 93 | 3.887 | 0.4212 | 3.465 | 73.12 | 1.047e-06 | 2.5e-05 |
| Moon-Venus Trine | Nifty 50 | 20 | 93 | 7.34 | 0.8264 | 6.514 | 68.82 | 1.496e-06 | 3.36e-05 |
| Moon-Venus Trine | Nifty Bank | 1 | 93 | 0.7716 | 0.06023 | 0.7114 | 65.59 | 3.119e-05 | 0.0003944 |
| Moon-Venus Trine | Nifty Bank | 3 | 93 | 1.824 | 0.1819 | 1.642 | 69.89 | 0.0001937 | 0.001647 |
| Moon-Venus Trine | Nifty Bank | 5 | 93 | 2.671 | 0.3 | 2.371 | 65.59 | 0.0003546 | 0.002623 |
| Moon-Venus Trine | Nifty Bank | 10 | 93 | 4.78 | 0.5834 | 4.196 | 70.97 | 3.054e-06 | 6.259e-05 |
| Moon-Venus Trine | Nifty Bank | 20 | 93 | 6.719 | 1.172 | 5.547 | 69.89 | 1.658e-05 | 0.0002448 |
| Moon-Venus Trine | Nifty Midcap 100 | 1 | 93 | -0.02222 | 0.05397 | -0.07619 | 61.29 | 0.4172 | 0.599 |
| Moon-Venus Trine | Nifty Midcap 100 | 3 | 93 | 0.05736 | 0.1609 | -0.1035 | 38.71 | 0.6324 | 0.7778 |
| Moon-Venus Trine | Nifty Midcap 100 | 5 | 93 | -0.01701 | 0.266 | -0.283 | 40.86 | 0.3735 | 0.5549 |
| Moon-Venus Trine | Nifty Midcap 100 | 10 | 93 | 1.678 | 0.532 | 1.146 | 67.74 | 0.01626 | 0.05606 |
| Moon-Venus Trine | Nifty Midcap 100 | 20 | 93 | 1.828 | 1.065 | 0.7636 | 63.44 | 0.2124 | 0.3749 |
| Moon-Venus Trine | Nifty Midcap 150 | 1 | 93 | 0.4754 | 0.05323 | 0.4222 | 68.82 | 0.0003427 | 0.002562 |
| Moon-Venus Trine | Nifty Midcap 150 | 3 | 93 | 0.3224 | 0.1594 | 0.1629 | 70.97 | 0.3838 | 0.5659 |
| Moon-Venus Trine | Nifty Midcap 150 | 5 | 93 | 0.4781 | 0.2642 | 0.2138 | 66.67 | 0.524 | 0.6961 |
| Moon-Venus Trine | Nifty Midcap 150 | 10 | 93 | 1.966 | 0.5204 | 1.445 | 73.12 | 0.001726 | 0.009016 |
| Moon-Venus Trine | Nifty Midcap 150 | 20 | 93 | 2.115 | 1.047 | 1.067 | 68.82 | 0.07779 | 0.1792 |
| Moon-Venus Trine | BSE Sensex | 1 | 93 | 0.1157 | 0.05036 | 0.06533 | 53.76 | 0.5601 | 0.7248 |
| Moon-Venus Trine | BSE Sensex | 3 | 93 | 0.1044 | 0.1513 | -0.04692 | 60.22 | 0.8186 | 0.8992 |
| Moon-Venus Trine | BSE Sensex | 5 | 93 | 0.1203 | 0.2506 | -0.1303 | 55.91 | 0.7108 | 0.8312 |
| Moon-Venus Trine | BSE Sensex | 10 | 93 | 0.8728 | 0.4957 | 0.3772 | 65.59 | 0.4186 | 0.6003 |
| Moon-Venus Trine | BSE Sensex | 20 | 93 | 0.9902 | 1.002 | -0.01144 | 56.99 | 0.9869 | 0.9953 |
| Rahu-Saturn Opposition | Nifty 50 | 1 | 2 | 1.727 | 0.04492 | 1.682 | 50 | 0.6489 | 0.7921 |
| Rahu-Saturn Opposition | Nifty 50 | 3 | 2 | 0.4834 | 0.1333 | 0.3501 | 50 | 0.8858 | 0.9423 |
| Rahu-Saturn Opposition | Nifty 50 | 5 | 2 | -1.554 | 0.2178 | -1.771 | 50 | 0.5913 | 0.7471 |
| Rahu-Saturn Opposition | Nifty 50 | 10 | 2 | 3.625 | 0.4212 | 3.203 | 100 | 0.2658 | 0.4401 |
| Rahu-Saturn Opposition | Nifty 50 | 20 | 2 | 1.161 | 0.8264 | 0.335 | 50 | 0.9086 | 0.9585 |
| Rahu-Saturn Opposition | Nifty Bank | 1 | 2 | 1.487 | 0.06023 | 1.426 | 50 | 0.7136 | 0.8334 |
| Rahu-Saturn Opposition | Nifty Bank | 3 | 2 | 0.4756 | 0.1819 | 0.2937 | 50 | 0.8855 | 0.9423 |
| Rahu-Saturn Opposition | Nifty Bank | 5 | 2 | -1.772 | 0.3 | -2.072 | 50 | 0.7336 | 0.8454 |
| Rahu-Saturn Opposition | Nifty Bank | 10 | 2 | 6.595 | 0.5834 | 6.011 | 100 | 0.3503 | 0.5301 |
| Rahu-Saturn Opposition | Nifty Bank | 20 | 2 | 4.53 | 1.172 | 3.357 | 50 | 0.6687 | 0.8045 |
| Rahu-Saturn Opposition | Nifty Midcap 100 | 1 | 2 | -0.2745 | 0.05397 | -0.3284 | 50 | 0.7953 | 0.8851 |
| Rahu-Saturn Opposition | Nifty Midcap 100 | 3 | 2 | -1.293 | 0.1609 | -1.453 | 50 | 0.4871 | 0.665 |
| Rahu-Saturn Opposition | Nifty Midcap 100 | 5 | 2 | -1.123 | 0.266 | -1.389 | 50 | 0.5147 | 0.6878 |
| Rahu-Saturn Opposition | Nifty Midcap 100 | 10 | 2 | 0.6832 | 0.532 | 0.1512 | 50 | 0.9459 | 0.9787 |
| Rahu-Saturn Opposition | Nifty Midcap 100 | 20 | 2 | -4.492 | 1.065 | -5.557 | 50 | 0.5597 | 0.7248 |
| Rahu-Saturn Opposition | Nifty Midcap 150 | 1 | 2 | 1.595 | 0.05323 | 1.542 | 50 | 0.6574 | 0.7955 |
| Rahu-Saturn Opposition | Nifty Midcap 150 | 3 | 2 | 0.3205 | 0.1594 | 0.161 | 50 | 0.9381 | 0.9749 |
| Rahu-Saturn Opposition | Nifty Midcap 150 | 5 | 2 | -1.792 | 0.2642 | -2.056 | 50 | 0.5966 | 0.7511 |
| Rahu-Saturn Opposition | Nifty Midcap 150 | 10 | 2 | 3.561 | 0.5204 | 3.041 | 100 | 0.2296 | 0.3956 |
| Rahu-Saturn Opposition | Nifty Midcap 150 | 20 | 2 | 1.1 | 1.047 | 0.05207 | 50 | 0.9856 | 0.9948 |
| Rahu-Saturn Opposition | BSE Sensex | 1 | 2 | 1.25 | 0.05036 | 1.2 | 50 | 0.685 | 0.8129 |
| Rahu-Saturn Opposition | BSE Sensex | 3 | 2 | 0.1179 | 0.1513 | -0.0334 | 50 | 0.9858 | 0.9948 |
| Rahu-Saturn Opposition | BSE Sensex | 5 | 2 | -1.912 | 0.2506 | -2.162 | 50 | 0.576 | 0.7342 |
| Rahu-Saturn Opposition | BSE Sensex | 10 | 2 | 3.4 | 0.4957 | 2.904 | 100 | 0.2249 | 0.3894 |
| Rahu-Saturn Opposition | BSE Sensex | 20 | 2 | 0.4746 | 1.002 | -0.527 | 50 | 0.7466 | 0.8533 |
| Rahu-Saturn Square | Nifty 50 | 1 | 4 | -0.1036 | 0.04492 | -0.1485 | 25 | 0.7834 | 0.8768 |
| Rahu-Saturn Square | Nifty 50 | 3 | 4 | 0.7296 | 0.1333 | 0.5964 | 25 | 0.7431 | 0.851 |
| Rahu-Saturn Square | Nifty 50 | 5 | 4 | 2.778 | 0.2178 | 2.56 | 75 | 0.3636 | 0.545 |
| Rahu-Saturn Square | Nifty 50 | 10 | 4 | 2.158 | 0.4212 | 1.737 | 50 | 0.6837 | 0.8124 |
| Rahu-Saturn Square | Nifty 50 | 20 | 4 | 4.889 | 0.8264 | 4.063 | 50 | 0.6144 | 0.7624 |
| Rahu-Saturn Square | Nifty Bank | 1 | 4 | 0.01137 | 0.06023 | -0.04886 | 50 | 0.9609 | 0.984 |
| Rahu-Saturn Square | Nifty Bank | 3 | 4 | 1.218 | 0.1819 | 1.036 | 50 | 0.6518 | 0.7932 |
| Rahu-Saturn Square | Nifty Bank | 5 | 4 | 3.274 | 0.3 | 2.974 | 50 | 0.3531 | 0.533 |
| Rahu-Saturn Square | Nifty Bank | 10 | 4 | 2.7 | 0.5834 | 2.116 | 50 | 0.682 | 0.8118 |
| Rahu-Saturn Square | Nifty Bank | 20 | 4 | 4.124 | 1.172 | 2.952 | 50 | 0.6757 | 0.8083 |
| Rahu-Saturn Square | Nifty Midcap 100 | 1 | 4 | -0.1145 | 0.05397 | -0.1685 | 50 | 0.612 | 0.7611 |
| Rahu-Saturn Square | Nifty Midcap 100 | 3 | 4 | -0.7593 | 0.1609 | -0.9201 | 25 | 0.2024 | 0.3633 |
| Rahu-Saturn Square | Nifty Midcap 100 | 5 | 4 | -0.1538 | 0.266 | -0.4198 | 25 | 0.655 | 0.7938 |
| Rahu-Saturn Square | Nifty Midcap 100 | 10 | 4 | -0.09881 | 0.532 | -0.6308 | 50 | 0.7874 | 0.8798 |
| Rahu-Saturn Square | Nifty Midcap 100 | 20 | 4 | -1.339 | 1.065 | -2.404 | 50 | 0.5699 | 0.7302 |
| Rahu-Saturn Square | Nifty Midcap 150 | 1 | 4 | 0.07458 | 0.05323 | 0.02135 | 25 | 0.9739 | 0.9895 |
| Rahu-Saturn Square | Nifty Midcap 150 | 3 | 4 | -0.6049 | 0.1594 | -0.7644 | 25 | 0.2186 | 0.3842 |
| Rahu-Saturn Square | Nifty Midcap 150 | 5 | 4 | 0.8223 | 0.2642 | 0.558 | 75 | 0.4426 | 0.6228 |
| Rahu-Saturn Square | Nifty Midcap 150 | 10 | 4 | 0.5176 | 0.5204 | -0.002799 | 75 | 0.9991 | 0.9997 |
| Rahu-Saturn Square | Nifty Midcap 150 | 20 | 4 | -0.3236 | 1.047 | -1.371 | 50 | 0.6338 | 0.7784 |
| Rahu-Saturn Square | BSE Sensex | 1 | 4 | -0.2991 | 0.05036 | -0.3495 | 25 | 0.3745 | 0.5558 |
| Rahu-Saturn Square | BSE Sensex | 3 | 4 | -0.04818 | 0.1513 | -0.1995 | 25 | 0.8465 | 0.9172 |
| Rahu-Saturn Square | BSE Sensex | 5 | 4 | 1.387 | 0.2506 | 1.136 | 50 | 0.4141 | 0.5961 |
| Rahu-Saturn Square | BSE Sensex | 10 | 4 | 0.1046 | 0.4957 | -0.391 | 50 | 0.8711 | 0.9336 |
| Rahu-Saturn Square | BSE Sensex | 20 | 4 | 0.1688 | 1.002 | -0.8329 | 50 | 0.7906 | 0.8811 |
| Rahu-Saturn Trine | Nifty 50 | 1 | 4 | 0.2303 | 0.04492 | 0.1854 | 50 | 0.7782 | 0.8736 |
| Rahu-Saturn Trine | Nifty 50 | 3 | 4 | 1.626 | 0.1333 | 1.493 | 50 | 0.4218 | 0.6034 |
| Rahu-Saturn Trine | Nifty 50 | 5 | 4 | 2.399 | 0.2178 | 2.182 | 75 | 0.4487 | 0.6288 |
| Rahu-Saturn Trine | Nifty 50 | 10 | 4 | 4.557 | 0.4212 | 4.136 | 100 | 0.2337 | 0.4 |
| Rahu-Saturn Trine | Nifty 50 | 20 | 4 | 6.414 | 0.8264 | 5.588 | 75 | 0.5087 | 0.6836 |
| Rahu-Saturn Trine | Nifty Bank | 1 | 4 | 0.6848 | 0.06023 | 0.6246 | 75 | 0.5134 | 0.687 |
| Rahu-Saturn Trine | Nifty Bank | 3 | 4 | 2.74 | 0.1819 | 2.558 | 50 | 0.2619 | 0.4348 |
| Rahu-Saturn Trine | Nifty Bank | 5 | 4 | 2.854 | 0.3 | 2.554 | 75 | 0.4137 | 0.5961 |
| Rahu-Saturn Trine | Nifty Bank | 10 | 4 | 6.556 | 0.5834 | 5.973 | 75 | 0.1909 | 0.3487 |
| Rahu-Saturn Trine | Nifty Bank | 20 | 4 | 6.756 | 1.172 | 5.584 | 75 | 0.4207 | 0.6024 |
| Rahu-Saturn Trine | Nifty Midcap 100 | 1 | 4 | 0.3927 | 0.05397 | 0.3388 | 75 | 0.2545 | 0.4271 |
| Rahu-Saturn Trine | Nifty Midcap 100 | 3 | 4 | -0.2398 | 0.1609 | -0.4006 | 25 | 0.3513 | 0.5311 |
| Rahu-Saturn Trine | Nifty Midcap 100 | 5 | 4 | -1.487 | 0.266 | -1.753 | 0 | 0.2874 | 0.4622 |
| Rahu-Saturn Trine | Nifty Midcap 100 | 10 | 4 | 1.294 | 0.532 | 0.762 | 75 | 0.684 | 0.8125 |
| Rahu-Saturn Trine | Nifty Midcap 100 | 20 | 4 | 1.596 | 1.065 | 0.5311 | 75 | 0.8389 | 0.9128 |
| Rahu-Saturn Trine | Nifty Midcap 150 | 1 | 4 | -0.1493 | 0.05323 | -0.2025 | 50 | 0.7263 | 0.8408 |
| Rahu-Saturn Trine | Nifty Midcap 150 | 3 | 4 | 0.4221 | 0.1594 | 0.2626 | 50 | 0.7795 | 0.8744 |
| Rahu-Saturn Trine | Nifty Midcap 150 | 5 | 4 | 0.1603 | 0.2642 | -0.1039 | 75 | 0.8481 | 0.9178 |
| Rahu-Saturn Trine | Nifty Midcap 150 | 10 | 4 | 1.833 | 0.5204 | 1.312 | 100 | 0.113 | 0.2375 |
| Rahu-Saturn Trine | Nifty Midcap 150 | 20 | 4 | 1.036 | 1.047 | -0.01122 | 75 | 0.9977 | 0.9993 |
| Rahu-Saturn Trine | BSE Sensex | 1 | 4 | -0.1416 | 0.05036 | -0.1919 | 50 | 0.7397 | 0.8491 |
| Rahu-Saturn Trine | BSE Sensex | 3 | 4 | 0.4426 | 0.1513 | 0.2913 | 50 | 0.772 | 0.8717 |
| Rahu-Saturn Trine | BSE Sensex | 5 | 4 | -0.1085 | 0.2506 | -0.359 | 75 | 0.5436 | 0.7115 |
| Rahu-Saturn Trine | BSE Sensex | 10 | 4 | 1.224 | 0.4957 | 0.7285 | 100 | 0.02499 | 0.07752 |
| Rahu-Saturn Trine | BSE Sensex | 20 | 4 | 1.128 | 1.002 | 0.1262 | 75 | 0.9752 | 0.9897 |
| Rahu-Sun Opposition | Nifty 50 | 1 | 29 | 0.2842 | 0.04492 | 0.2393 | 65.52 | 0.1486 | 0.292 |
| Rahu-Sun Opposition | Nifty 50 | 3 | 29 | 1.344 | 0.1333 | 1.211 | 62.07 | 0.05443 | 0.1371 |
| Rahu-Sun Opposition | Nifty 50 | 5 | 29 | 2.513 | 0.2178 | 2.295 | 55.17 | 0.02786 | 0.08406 |
| Rahu-Sun Opposition | Nifty 50 | 10 | 29 | 3.761 | 0.4212 | 3.34 | 68.97 | 0.009596 | 0.03642 |
| Rahu-Sun Opposition | Nifty 50 | 20 | 29 | 8.143 | 0.8264 | 7.316 | 65.52 | 0.004223 | 0.01852 |
| Rahu-Sun Opposition | Nifty Bank | 1 | 29 | 0.6848 | 0.06023 | 0.6246 | 68.97 | 0.03055 | 0.08979 |
| Rahu-Sun Opposition | Nifty Bank | 3 | 29 | 1.592 | 0.1819 | 1.41 | 62.07 | 0.09532 | 0.2095 |
| Rahu-Sun Opposition | Nifty Bank | 5 | 29 | 2.732 | 0.3 | 2.432 | 55.17 | 0.04765 | 0.1238 |
| Rahu-Sun Opposition | Nifty Bank | 10 | 29 | 5.016 | 0.5834 | 4.433 | 62.07 | 0.006216 | 0.0254 |
| Rahu-Sun Opposition | Nifty Bank | 20 | 29 | 7.607 | 1.172 | 6.434 | 65.52 | 0.004681 | 0.02006 |
| Rahu-Sun Opposition | Nifty Midcap 100 | 1 | 29 | -0.1269 | 0.05397 | -0.1809 | 62.07 | 0.3974 | 0.5805 |
| Rahu-Sun Opposition | Nifty Midcap 100 | 3 | 29 | -0.1632 | 0.1609 | -0.3241 | 31.03 | 0.3558 | 0.5357 |
| Rahu-Sun Opposition | Nifty Midcap 100 | 5 | 29 | 0.3909 | 0.266 | 0.1248 | 41.38 | 0.7999 | 0.888 |
| Rahu-Sun Opposition | Nifty Midcap 100 | 10 | 29 | 1.861 | 0.532 | 1.329 | 68.97 | 0.03797 | 0.1051 |
| Rahu-Sun Opposition | Nifty Midcap 100 | 20 | 29 | 3.179 | 1.065 | 2.114 | 79.31 | 0.03331 | 0.09557 |
| Rahu-Sun Opposition | Nifty Midcap 150 | 1 | 29 | 0.3426 | 0.05323 | 0.2894 | 58.62 | 0.1534 | 0.2994 |
| Rahu-Sun Opposition | Nifty Midcap 150 | 3 | 29 | -0.1327 | 0.1594 | -0.2922 | 62.07 | 0.3427 | 0.5231 |
| Rahu-Sun Opposition | Nifty Midcap 150 | 5 | 29 | -0.02152 | 0.2642 | -0.2858 | 55.17 | 0.5211 | 0.6939 |
| Rahu-Sun Opposition | Nifty Midcap 150 | 10 | 29 | 1.379 | 0.5204 | 0.8582 | 65.52 | 0.1677 | 0.32 |
| Rahu-Sun Opposition | Nifty Midcap 150 | 20 | 29 | 1.989 | 1.047 | 0.9417 | 65.52 | 0.2782 | 0.4549 |
| Rahu-Sun Opposition | BSE Sensex | 1 | 29 | -0.3317 | 0.05036 | -0.3821 | 41.38 | 0.04857 | 0.1257 |
| Rahu-Sun Opposition | BSE Sensex | 3 | 29 | -0.5714 | 0.1513 | -0.7228 | 41.38 | 0.04972 | 0.1277 |
| Rahu-Sun Opposition | BSE Sensex | 5 | 29 | -0.9889 | 0.2506 | -1.239 | 34.48 | 0.01914 | 0.06436 |
| Rahu-Sun Opposition | BSE Sensex | 10 | 29 | 0.2758 | 0.4957 | -0.2198 | 65.52 | 0.6699 | 0.8046 |
| Rahu-Sun Opposition | BSE Sensex | 20 | 29 | 1.742 | 1.002 | 0.7403 | 58.62 | 0.402 | 0.5842 |
| Rahu-Sun Square | Nifty 50 | 1 | 56 | 0.4479 | 0.04492 | 0.403 | 69.64 | 0.03719 | 0.1038 |
| Rahu-Sun Square | Nifty 50 | 3 | 56 | 1.935 | 0.1333 | 1.802 | 64.29 | 9.344e-05 | 0.0009319 |
| Rahu-Sun Square | Nifty 50 | 5 | 56 | 3.147 | 0.2178 | 2.93 | 71.43 | 3.353e-05 | 0.0004136 |
| Rahu-Sun Square | Nifty 50 | 10 | 56 | 3.99 | 0.4212 | 3.568 | 66.07 | 0.0001996 | 0.001677 |
| Rahu-Sun Square | Nifty 50 | 20 | 56 | 8.313 | 0.8264 | 7.487 | 66.07 | 3.295e-05 | 0.0004091 |
| Rahu-Sun Square | Nifty Bank | 1 | 56 | 0.6984 | 0.06023 | 0.6381 | 62.5 | 0.02232 | 0.07152 |
| Rahu-Sun Square | Nifty Bank | 3 | 56 | 2.384 | 0.1819 | 2.202 | 69.64 | 0.0003022 | 0.002289 |
| Rahu-Sun Square | Nifty Bank | 5 | 56 | 3.206 | 0.3 | 2.906 | 67.86 | 0.0005297 | 0.003592 |
| Rahu-Sun Square | Nifty Bank | 10 | 56 | 4.325 | 0.5834 | 3.741 | 66.07 | 0.002268 | 0.011 |
| Rahu-Sun Square | Nifty Bank | 20 | 56 | 6.707 | 1.172 | 5.535 | 60.71 | 0.001926 | 0.009839 |
| Rahu-Sun Square | Nifty Midcap 100 | 1 | 56 | 0.2766 | 0.05397 | 0.2227 | 66.07 | 0.1998 | 0.3603 |
| Rahu-Sun Square | Nifty Midcap 100 | 3 | 56 | 0.6689 | 0.1609 | 0.5081 | 46.43 | 0.1283 | 0.2622 |
| Rahu-Sun Square | Nifty Midcap 100 | 5 | 56 | 1.187 | 0.266 | 0.9208 | 50 | 0.01438 | 0.05035 |
| Rahu-Sun Square | Nifty Midcap 100 | 10 | 56 | 2.401 | 0.532 | 1.869 | 75 | 0.0002011 | 0.00168 |
| Rahu-Sun Square | Nifty Midcap 100 | 20 | 56 | 3.44 | 1.065 | 2.376 | 71.43 | 0.0006696 | 0.004278 |
| Rahu-Sun Square | Nifty Midcap 150 | 1 | 56 | 0.5587 | 0.05323 | 0.5054 | 67.86 | 0.01369 | 0.04882 |
| Rahu-Sun Square | Nifty Midcap 150 | 3 | 56 | 0.5531 | 0.1594 | 0.3937 | 64.29 | 0.1938 | 0.3523 |
| Rahu-Sun Square | Nifty Midcap 150 | 5 | 56 | 0.811 | 0.2642 | 0.5467 | 66.07 | 0.118 | 0.2457 |
| Rahu-Sun Square | Nifty Midcap 150 | 10 | 56 | 1.771 | 0.5204 | 1.25 | 64.29 | 0.04372 | 0.1158 |
| Rahu-Sun Square | Nifty Midcap 150 | 20 | 56 | 2.204 | 1.047 | 1.156 | 66.07 | 0.1278 | 0.2617 |
| Rahu-Sun Square | BSE Sensex | 1 | 56 | 0.181 | 0.05036 | 0.1306 | 53.57 | 0.5104 | 0.6841 |
| Rahu-Sun Square | BSE Sensex | 3 | 56 | 0.5045 | 0.1513 | 0.3532 | 58.93 | 0.3152 | 0.4926 |
| Rahu-Sun Square | BSE Sensex | 5 | 56 | 0.5313 | 0.2506 | 0.2808 | 58.93 | 0.4501 | 0.6298 |
| Rahu-Sun Square | BSE Sensex | 10 | 56 | 0.5958 | 0.4957 | 0.1002 | 53.57 | 0.8687 | 0.9318 |
| Rahu-Sun Square | BSE Sensex | 20 | 56 | 1.151 | 1.002 | 0.1496 | 51.79 | 0.8545 | 0.9213 |
| Rahu-Sun Trine | Nifty 50 | 1 | 57 | 0.1651 | 0.04492 | 0.1202 | 63.16 | 0.484 | 0.6622 |
| Rahu-Sun Trine | Nifty 50 | 3 | 57 | 1.693 | 0.1333 | 1.56 | 66.67 | 0.0001292 | 0.001208 |
| Rahu-Sun Trine | Nifty 50 | 5 | 57 | 2.802 | 0.2178 | 2.585 | 66.67 | 0.000192 | 0.001636 |
| Rahu-Sun Trine | Nifty 50 | 10 | 57 | 3.41 | 0.4212 | 2.989 | 66.67 | 0.001982 | 0.01001 |
| Rahu-Sun Trine | Nifty 50 | 20 | 56 | 7.145 | 0.8264 | 6.318 | 66.07 | 0.000906 | 0.00541 |
| Rahu-Sun Trine | Nifty Bank | 1 | 57 | 0.5921 | 0.06023 | 0.5318 | 61.4 | 0.01515 | 0.05286 |
| Rahu-Sun Trine | Nifty Bank | 3 | 57 | 2.453 | 0.1819 | 2.272 | 71.93 | 2.955e-05 | 0.0003769 |
| Rahu-Sun Trine | Nifty Bank | 5 | 57 | 3.614 | 0.3 | 3.314 | 77.19 | 1.511e-05 | 0.0002276 |
| Rahu-Sun Trine | Nifty Bank | 10 | 57 | 4.46 | 0.5834 | 3.876 | 70.18 | 0.0008746 | 0.005307 |
| Rahu-Sun Trine | Nifty Bank | 20 | 56 | 6.512 | 1.172 | 5.34 | 67.86 | 0.00387 | 0.01725 |
| Rahu-Sun Trine | Nifty Midcap 100 | 1 | 57 | 0.01806 | 0.05397 | -0.0359 | 64.91 | 0.8428 | 0.9153 |
| Rahu-Sun Trine | Nifty Midcap 100 | 3 | 57 | 0.04029 | 0.1609 | -0.1206 | 36.84 | 0.7074 | 0.829 |
| Rahu-Sun Trine | Nifty Midcap 100 | 5 | 57 | -0.09503 | 0.266 | -0.361 | 31.58 | 0.399 | 0.5817 |
| Rahu-Sun Trine | Nifty Midcap 100 | 10 | 57 | 1.261 | 0.532 | 0.7288 | 64.91 | 0.2641 | 0.4379 |
| Rahu-Sun Trine | Nifty Midcap 100 | 20 | 56 | 2.273 | 1.065 | 1.208 | 69.64 | 0.2054 | 0.3672 |
| Rahu-Sun Trine | Nifty Midcap 150 | 1 | 57 | 0.2292 | 0.05323 | 0.176 | 61.4 | 0.3547 | 0.5349 |
| Rahu-Sun Trine | Nifty Midcap 150 | 3 | 57 | 0.3219 | 0.1594 | 0.1625 | 64.91 | 0.453 | 0.632 |
| Rahu-Sun Trine | Nifty Midcap 150 | 5 | 57 | 0.6177 | 0.2642 | 0.3535 | 66.67 | 0.274 | 0.4503 |
| Rahu-Sun Trine | Nifty Midcap 150 | 10 | 57 | 1.338 | 0.5204 | 0.8175 | 68.42 | 0.172 | 0.3259 |
| Rahu-Sun Trine | Nifty Midcap 150 | 20 | 56 | 1.134 | 1.047 | 0.08644 | 66.07 | 0.9231 | 0.9669 |
| Rahu-Sun Trine | BSE Sensex | 1 | 57 | -0.08876 | 0.05036 | -0.1391 | 54.39 | 0.4351 | 0.6172 |
| Rahu-Sun Trine | BSE Sensex | 3 | 57 | 0.2499 | 0.1513 | 0.09863 | 59.65 | 0.6772 | 0.8085 |
| Rahu-Sun Trine | BSE Sensex | 5 | 57 | 0.1298 | 0.2506 | -0.1207 | 57.89 | 0.7527 | 0.858 |
| Rahu-Sun Trine | BSE Sensex | 10 | 57 | -0.02798 | 0.4957 | -0.5236 | 59.65 | 0.3744 | 0.5558 |
| Rahu-Sun Trine | BSE Sensex | 20 | 56 | 0.461 | 1.002 | -0.5407 | 58.93 | 0.5625 | 0.7258 |
| Rahu-Venus Opposition | Nifty 50 | 1 | 29 | 0.2693 | 0.04492 | 0.2243 | 65.52 | 0.2871 | 0.4622 |
| Rahu-Venus Opposition | Nifty 50 | 3 | 29 | 1.596 | 0.1333 | 1.462 | 72.41 | 0.01292 | 0.04686 |
| Rahu-Venus Opposition | Nifty 50 | 5 | 29 | 2.733 | 0.2178 | 2.515 | 75.86 | 0.01173 | 0.04321 |
| Rahu-Venus Opposition | Nifty 50 | 10 | 29 | 4.778 | 0.4212 | 4.357 | 82.76 | 0.0002204 | 0.00177 |
| Rahu-Venus Opposition | Nifty 50 | 20 | 29 | 8.377 | 0.8264 | 7.55 | 86.21 | 0.0016 | 0.008509 |
| Rahu-Venus Opposition | Nifty Bank | 1 | 29 | 0.5123 | 0.06023 | 0.4521 | 62.07 | 0.281 | 0.4572 |
| Rahu-Venus Opposition | Nifty Bank | 3 | 29 | 1.797 | 0.1819 | 1.615 | 62.07 | 0.03913 | 0.107 |
| Rahu-Venus Opposition | Nifty Bank | 5 | 29 | 3.227 | 0.3 | 2.927 | 72.41 | 0.009377 | 0.03581 |
| Rahu-Venus Opposition | Nifty Bank | 10 | 29 | 6.186 | 0.5834 | 5.603 | 79.31 | 0.000254 | 0.001984 |
| Rahu-Venus Opposition | Nifty Bank | 20 | 29 | 7.926 | 1.172 | 6.754 | 79.31 | 0.002067 | 0.01032 |
| Rahu-Venus Opposition | Nifty Midcap 100 | 1 | 29 | -0.05309 | 0.05397 | -0.1071 | 65.52 | 0.7737 | 0.8721 |
| Rahu-Venus Opposition | Nifty Midcap 100 | 3 | 29 | 0.3662 | 0.1609 | 0.2053 | 44.83 | 0.6391 | 0.7837 |
| Rahu-Venus Opposition | Nifty Midcap 100 | 5 | 29 | 0.5009 | 0.266 | 0.2349 | 48.28 | 0.6676 | 0.8036 |
| Rahu-Venus Opposition | Nifty Midcap 100 | 10 | 29 | 2.044 | 0.532 | 1.512 | 68.97 | 0.04369 | 0.1158 |
| Rahu-Venus Opposition | Nifty Midcap 100 | 20 | 29 | 2.927 | 1.065 | 1.862 | 72.41 | 0.08054 | 0.1837 |
| Rahu-Venus Opposition | Nifty Midcap 150 | 1 | 29 | 0.3781 | 0.05323 | 0.3248 | 72.41 | 0.1731 | 0.3265 |
| Rahu-Venus Opposition | Nifty Midcap 150 | 3 | 29 | 0.243 | 0.1594 | 0.08356 | 68.97 | 0.785 | 0.878 |
| Rahu-Venus Opposition | Nifty Midcap 150 | 5 | 29 | 0.4392 | 0.2642 | 0.175 | 72.41 | 0.7183 | 0.8361 |
| Rahu-Venus Opposition | Nifty Midcap 150 | 10 | 29 | 2.67 | 0.5204 | 2.15 | 82.76 | 0.0004495 | 0.003192 |
| Rahu-Venus Opposition | Nifty Midcap 150 | 20 | 29 | 2.631 | 1.047 | 1.583 | 86.21 | 0.03361 | 0.09615 |
| Rahu-Venus Opposition | BSE Sensex | 1 | 29 | -0.001283 | 0.05036 | -0.05164 | 65.52 | 0.812 | 0.8953 |
| Rahu-Venus Opposition | BSE Sensex | 3 | 29 | 0.2109 | 0.1513 | 0.05962 | 65.52 | 0.8508 | 0.9192 |
| Rahu-Venus Opposition | BSE Sensex | 5 | 29 | 0.5649 | 0.2506 | 0.3143 | 62.07 | 0.5643 | 0.7258 |
| Rahu-Venus Opposition | BSE Sensex | 10 | 29 | 2.018 | 0.4957 | 1.522 | 75.86 | 0.02443 | 0.07635 |
| Rahu-Venus Opposition | BSE Sensex | 20 | 29 | 1.632 | 1.002 | 0.6299 | 72.41 | 0.4946 | 0.6727 |
| Rahu-Venus Square | Nifty 50 | 1 | 60 | 0.5276 | 0.04492 | 0.4827 | 73.33 | 0.0001539 | 0.001387 |
| Rahu-Venus Square | Nifty 50 | 3 | 60 | 1.723 | 0.1333 | 1.59 | 65 | 0.0002816 | 0.002168 |
| Rahu-Venus Square | Nifty 50 | 5 | 60 | 3.025 | 0.2178 | 2.807 | 70 | 3.384e-05 | 0.0004147 |
| Rahu-Venus Square | Nifty 50 | 10 | 60 | 3.789 | 0.4212 | 3.368 | 68.33 | 0.0002837 | 0.002176 |
| Rahu-Venus Square | Nifty 50 | 20 | 60 | 7.322 | 0.8264 | 6.495 | 63.33 | 0.0005584 | 0.003726 |
| Rahu-Venus Square | Nifty Bank | 1 | 60 | 0.9036 | 0.06023 | 0.8433 | 68.33 | 6.307e-05 | 0.0006955 |
| Rahu-Venus Square | Nifty Bank | 3 | 60 | 2.152 | 0.1819 | 1.97 | 63.33 | 0.0005877 | 0.00386 |
| Rahu-Venus Square | Nifty Bank | 5 | 60 | 3.455 | 0.3 | 3.155 | 70 | 0.000105 | 0.001021 |
| Rahu-Venus Square | Nifty Bank | 10 | 60 | 4.925 | 0.5834 | 4.341 | 65 | 0.0001694 | 0.001484 |
| Rahu-Venus Square | Nifty Bank | 20 | 60 | 6.737 | 1.172 | 5.565 | 68.33 | 0.001126 | 0.006495 |
| Rahu-Venus Square | Nifty Midcap 100 | 1 | 60 | 0.1777 | 0.05397 | 0.1237 | 73.33 | 0.4229 | 0.6044 |
| Rahu-Venus Square | Nifty Midcap 100 | 3 | 60 | 0.0261 | 0.1609 | -0.1348 | 36.67 | 0.723 | 0.8394 |
| Rahu-Venus Square | Nifty Midcap 100 | 5 | 60 | 0.07563 | 0.266 | -0.1904 | 35 | 0.6228 | 0.77 |
| Rahu-Venus Square | Nifty Midcap 100 | 10 | 60 | 1.38 | 0.532 | 0.8485 | 65 | 0.2094 | 0.3711 |
| Rahu-Venus Square | Nifty Midcap 100 | 20 | 60 | 1.87 | 1.065 | 0.8048 | 60 | 0.4276 | 0.609 |
| Rahu-Venus Square | Nifty Midcap 150 | 1 | 60 | 0.6315 | 0.05323 | 0.5783 | 70 | 7.371e-05 | 0.000772 |
| Rahu-Venus Square | Nifty Midcap 150 | 3 | 60 | 0.2125 | 0.1594 | 0.05303 | 66.67 | 0.8369 | 0.9123 |
| Rahu-Venus Square | Nifty Midcap 150 | 5 | 60 | 0.4229 | 0.2642 | 0.1586 | 65 | 0.5809 | 0.7388 |
| Rahu-Venus Square | Nifty Midcap 150 | 10 | 60 | 1.425 | 0.5204 | 0.9041 | 66.67 | 0.09793 | 0.2131 |
| Rahu-Venus Square | Nifty Midcap 150 | 20 | 60 | 1.084 | 1.047 | 0.03621 | 65 | 0.9667 | 0.9869 |
| Rahu-Venus Square | BSE Sensex | 1 | 60 | 0.199 | 0.05036 | 0.1486 | 60 | 0.2809 | 0.4572 |
| Rahu-Venus Square | BSE Sensex | 3 | 60 | 0.1723 | 0.1513 | 0.02097 | 58.33 | 0.9495 | 0.9798 |
| Rahu-Venus Square | BSE Sensex | 5 | 60 | 0.06512 | 0.2506 | -0.1854 | 55 | 0.5919 | 0.7474 |
| Rahu-Venus Square | BSE Sensex | 10 | 60 | -0.1408 | 0.4957 | -0.6364 | 51.67 | 0.218 | 0.3835 |
| Rahu-Venus Square | BSE Sensex | 20 | 60 | -0.4662 | 1.002 | -1.468 | 50 | 0.101 | 0.2181 |
| Rahu-Venus Trine | Nifty 50 | 1 | 60 | 0.5006 | 0.04492 | 0.4557 | 71.67 | 1.236e-05 | 0.000191 |
| Rahu-Venus Trine | Nifty 50 | 3 | 60 | 1.46 | 0.1333 | 1.327 | 60 | 0.00156 | 0.008348 |
| Rahu-Venus Trine | Nifty 50 | 5 | 59 | 2.564 | 0.2178 | 2.346 | 64.41 | 0.0007129 | 0.0045 |
| Rahu-Venus Trine | Nifty 50 | 10 | 59 | 3.641 | 0.4212 | 3.22 | 62.71 | 0.0003429 | 0.002562 |
| Rahu-Venus Trine | Nifty 50 | 20 | 59 | 7.829 | 0.8264 | 7.002 | 64.41 | 6.768e-05 | 0.0007252 |
| Rahu-Venus Trine | Nifty Bank | 1 | 60 | 0.9187 | 0.06023 | 0.8585 | 66.67 | 7.941e-06 | 0.0001295 |
| Rahu-Venus Trine | Nifty Bank | 3 | 60 | 1.76 | 0.1819 | 1.578 | 58.33 | 0.005252 | 0.02223 |
| Rahu-Venus Trine | Nifty Bank | 5 | 59 | 2.601 | 0.3 | 2.301 | 59.32 | 0.005509 | 0.02316 |
| Rahu-Venus Trine | Nifty Bank | 10 | 59 | 4.228 | 0.5834 | 3.644 | 59.32 | 0.001507 | 0.008119 |
| Rahu-Venus Trine | Nifty Bank | 20 | 59 | 6.986 | 1.172 | 5.813 | 62.71 | 0.0001599 | 0.001418 |
| Rahu-Venus Trine | Nifty Midcap 100 | 1 | 60 | 0.1349 | 0.05397 | 0.0809 | 71.67 | 0.5907 | 0.7471 |
| Rahu-Venus Trine | Nifty Midcap 100 | 3 | 60 | -0.1072 | 0.1609 | -0.2681 | 41.67 | 0.2155 | 0.3795 |
| Rahu-Venus Trine | Nifty Midcap 100 | 5 | 59 | 0.4259 | 0.266 | 0.1599 | 44.07 | 0.6097 | 0.7591 |
| Rahu-Venus Trine | Nifty Midcap 100 | 10 | 59 | 1.655 | 0.532 | 1.123 | 69.49 | 0.06178 | 0.1521 |
| Rahu-Venus Trine | Nifty Midcap 100 | 20 | 59 | 2.864 | 1.065 | 1.799 | 74.58 | 0.05205 | 0.1322 |
| Rahu-Venus Trine | Nifty Midcap 150 | 1 | 60 | 0.6061 | 0.05323 | 0.5528 | 73.33 | 5.782e-06 | 0.0001008 |
| Rahu-Venus Trine | Nifty Midcap 150 | 3 | 60 | 0.05906 | 0.1594 | -0.1004 | 61.67 | 0.6483 | 0.7919 |
| Rahu-Venus Trine | Nifty Midcap 150 | 5 | 59 | 0.1914 | 0.2642 | -0.07284 | 61.02 | 0.8063 | 0.8912 |
| Rahu-Venus Trine | Nifty Midcap 150 | 10 | 59 | 1.432 | 0.5204 | 0.9114 | 61.02 | 0.06611 | 0.159 |
| Rahu-Venus Trine | Nifty Midcap 150 | 20 | 59 | 1.67 | 1.047 | 0.6229 | 62.71 | 0.3449 | 0.5249 |
| Rahu-Venus Trine | BSE Sensex | 1 | 60 | 0.2736 | 0.05036 | 0.2233 | 56.67 | 0.171 | 0.3249 |
| Rahu-Venus Trine | BSE Sensex | 3 | 60 | 0.04375 | 0.1513 | -0.1076 | 46.67 | 0.7615 | 0.8637 |
| Rahu-Venus Trine | BSE Sensex | 5 | 59 | -0.09936 | 0.2506 | -0.3499 | 52.54 | 0.3429 | 0.5231 |
| Rahu-Venus Trine | BSE Sensex | 10 | 59 | 0.3287 | 0.4957 | -0.167 | 52.54 | 0.7262 | 0.8408 |
| Rahu-Venus Trine | BSE Sensex | 20 | 59 | 1.453 | 1.002 | 0.4518 | 59.32 | 0.5511 | 0.717 |
| Saturn-Sun Opposition | Nifty 50 | 1 | 26 | 0.6206 | 0.04492 | 0.5757 | 76.92 | 0.0003807 | 0.002772 |
| Saturn-Sun Opposition | Nifty 50 | 3 | 26 | 2.165 | 0.1333 | 2.032 | 69.23 | 0.0009215 | 0.005477 |
| Saturn-Sun Opposition | Nifty 50 | 5 | 26 | 3.116 | 0.2178 | 2.898 | 73.08 | 0.004337 | 0.01893 |
| Saturn-Sun Opposition | Nifty 50 | 10 | 26 | 4.45 | 0.4212 | 4.029 | 65.38 | 0.003866 | 0.01725 |
| Saturn-Sun Opposition | Nifty 50 | 20 | 26 | 8.944 | 0.8264 | 8.117 | 80.77 | 0.003385 | 0.0155 |
| Saturn-Sun Opposition | Nifty Bank | 1 | 26 | 0.9865 | 0.06023 | 0.9263 | 80.77 | 0.0001858 | 0.001598 |
| Saturn-Sun Opposition | Nifty Bank | 3 | 26 | 2.638 | 0.1819 | 2.456 | 65.38 | 0.002693 | 0.01282 |
| Saturn-Sun Opposition | Nifty Bank | 5 | 26 | 3.586 | 0.3 | 3.286 | 76.92 | 0.006831 | 0.02736 |
| Saturn-Sun Opposition | Nifty Bank | 10 | 26 | 5.083 | 0.5834 | 4.499 | 69.23 | 0.01916 | 0.06436 |
| Saturn-Sun Opposition | Nifty Bank | 20 | 26 | 7.427 | 1.172 | 6.255 | 76.92 | 0.03286 | 0.09492 |
| Saturn-Sun Opposition | Nifty Midcap 100 | 1 | 26 | 0.2881 | 0.05397 | 0.2341 | 69.23 | 0.2316 | 0.3975 |
| Saturn-Sun Opposition | Nifty Midcap 100 | 3 | 26 | 0.5551 | 0.1609 | 0.3943 | 46.15 | 0.3807 | 0.5632 |
| Saturn-Sun Opposition | Nifty Midcap 100 | 5 | 26 | 0.02903 | 0.266 | -0.237 | 34.62 | 0.7288 | 0.8422 |
| Saturn-Sun Opposition | Nifty Midcap 100 | 10 | 26 | 2.011 | 0.532 | 1.479 | 65.38 | 0.1648 | 0.3163 |
| Saturn-Sun Opposition | Nifty Midcap 100 | 20 | 26 | 3.417 | 1.065 | 2.353 | 69.23 | 0.1148 | 0.2402 |
| Saturn-Sun Opposition | Nifty Midcap 150 | 1 | 26 | 0.6625 | 0.05323 | 0.6093 | 73.08 | 0.001168 | 0.006666 |
| Saturn-Sun Opposition | Nifty Midcap 150 | 3 | 26 | 0.8206 | 0.1594 | 0.6612 | 65.38 | 0.07243 | 0.1701 |
| Saturn-Sun Opposition | Nifty Midcap 150 | 5 | 26 | 0.8944 | 0.2642 | 0.6302 | 73.08 | 0.201 | 0.362 |
| Saturn-Sun Opposition | Nifty Midcap 150 | 10 | 26 | 2.02 | 0.5204 | 1.499 | 61.54 | 0.09986 | 0.2166 |
| Saturn-Sun Opposition | Nifty Midcap 150 | 20 | 26 | 2.792 | 1.047 | 1.745 | 76.92 | 0.2602 | 0.4329 |
| Saturn-Sun Opposition | BSE Sensex | 1 | 26 | 0.5372 | 0.05036 | 0.4868 | 61.54 | 0.01198 | 0.04396 |
| Saturn-Sun Opposition | BSE Sensex | 3 | 26 | 0.9906 | 0.1513 | 0.8393 | 65.38 | 0.06698 | 0.1605 |
| Saturn-Sun Opposition | BSE Sensex | 5 | 26 | 1.056 | 0.2506 | 0.8056 | 69.23 | 0.1641 | 0.3154 |
| Saturn-Sun Opposition | BSE Sensex | 10 | 26 | 1.609 | 0.4957 | 1.114 | 61.54 | 0.2477 | 0.4174 |
| Saturn-Sun Opposition | BSE Sensex | 20 | 26 | 2.463 | 1.002 | 1.461 | 76.92 | 0.3721 | 0.5538 |
| Saturn-Sun Square | Nifty 50 | 1 | 52 | 0.4206 | 0.04492 | 0.3757 | 65.38 | 0.02006 | 0.06611 |
| Saturn-Sun Square | Nifty 50 | 3 | 52 | 1.984 | 0.1333 | 1.851 | 75 | 5.424e-06 | 9.64e-05 |
| Saturn-Sun Square | Nifty 50 | 5 | 52 | 3.217 | 0.2178 | 2.999 | 69.23 | 1.809e-05 | 0.000262 |
| Saturn-Sun Square | Nifty 50 | 10 | 52 | 3.928 | 0.4212 | 3.506 | 69.23 | 0.0002211 | 0.001772 |
| Saturn-Sun Square | Nifty 50 | 20 | 52 | 7.595 | 0.8264 | 6.768 | 67.31 | 0.0003685 | 0.002693 |
| Saturn-Sun Square | Nifty Bank | 1 | 52 | 0.8537 | 0.06023 | 0.7935 | 67.31 | 0.001477 | 0.008002 |
| Saturn-Sun Square | Nifty Bank | 3 | 52 | 2.451 | 0.1819 | 2.269 | 75 | 5.59e-05 | 0.0006277 |
| Saturn-Sun Square | Nifty Bank | 5 | 52 | 3.688 | 0.3 | 3.388 | 69.23 | 4.15e-05 | 0.0004833 |
| Saturn-Sun Square | Nifty Bank | 10 | 52 | 5.223 | 0.5834 | 4.639 | 67.31 | 8.446e-05 | 0.0008598 |
| Saturn-Sun Square | Nifty Bank | 20 | 52 | 7.124 | 1.172 | 5.951 | 63.46 | 0.0008833 | 0.005317 |
| Saturn-Sun Square | Nifty Midcap 100 | 1 | 52 | 0.2561 | 0.05397 | 0.2021 | 75 | 0.1489 | 0.2923 |
| Saturn-Sun Square | Nifty Midcap 100 | 3 | 52 | 0.6719 | 0.1609 | 0.511 | 51.92 | 0.04807 | 0.1247 |
| Saturn-Sun Square | Nifty Midcap 100 | 5 | 52 | 0.7097 | 0.266 | 0.4437 | 46.15 | 0.1496 | 0.293 |
| Saturn-Sun Square | Nifty Midcap 100 | 10 | 52 | 2.187 | 0.532 | 1.655 | 75 | 0.0004747 | 0.003325 |
| Saturn-Sun Square | Nifty Midcap 100 | 20 | 52 | 2.969 | 1.065 | 1.904 | 73.08 | 0.01642 | 0.05649 |
| Saturn-Sun Square | Nifty Midcap 150 | 1 | 52 | 0.5228 | 0.05323 | 0.4696 | 59.62 | 0.01104 | 0.0414 |
| Saturn-Sun Square | Nifty Midcap 150 | 3 | 52 | 0.5899 | 0.1594 | 0.4304 | 76.92 | 0.02088 | 0.06804 |
| Saturn-Sun Square | Nifty Midcap 150 | 5 | 52 | 0.9883 | 0.2642 | 0.7241 | 71.15 | 0.01357 | 0.04865 |
| Saturn-Sun Square | Nifty Midcap 150 | 10 | 52 | 1.9 | 0.5204 | 1.379 | 69.23 | 0.01147 | 0.04268 |
| Saturn-Sun Square | Nifty Midcap 150 | 20 | 52 | 1.222 | 1.047 | 0.1747 | 67.31 | 0.8191 | 0.8994 |
| Saturn-Sun Square | BSE Sensex | 1 | 52 | 0.06474 | 0.05036 | 0.01438 | 55.77 | 0.9318 | 0.9717 |
| Saturn-Sun Square | BSE Sensex | 3 | 52 | 0.4375 | 0.1513 | 0.2861 | 63.46 | 0.2301 | 0.396 |
| Saturn-Sun Square | BSE Sensex | 5 | 52 | 0.572 | 0.2506 | 0.3214 | 59.62 | 0.4288 | 0.6103 |
| Saturn-Sun Square | BSE Sensex | 10 | 52 | 0.5176 | 0.4957 | 0.02196 | 53.85 | 0.9735 | 0.9895 |
| Saturn-Sun Square | BSE Sensex | 20 | 52 | -0.2231 | 1.002 | -1.225 | 51.92 | 0.1547 | 0.3014 |
| Saturn-Sun Trine | Nifty 50 | 1 | 51 | 0.1292 | 0.04492 | 0.08427 | 56.86 | 0.5709 | 0.7309 |
| Saturn-Sun Trine | Nifty 50 | 3 | 51 | 1.543 | 0.1333 | 1.41 | 62.75 | 0.001414 | 0.007739 |
| Saturn-Sun Trine | Nifty 50 | 5 | 51 | 3.061 | 0.2178 | 2.843 | 72.55 | 7.074e-05 | 0.0007536 |
| Saturn-Sun Trine | Nifty 50 | 10 | 51 | 4.855 | 0.4212 | 4.434 | 78.43 | 4.015e-06 | 7.565e-05 |
| Saturn-Sun Trine | Nifty 50 | 20 | 51 | 8.684 | 0.8264 | 7.858 | 80.39 | 1.978e-05 | 0.000282 |
| Saturn-Sun Trine | Nifty Bank | 1 | 51 | 0.3249 | 0.06023 | 0.2647 | 60.78 | 0.2974 | 0.4744 |
| Saturn-Sun Trine | Nifty Bank | 3 | 51 | 1.889 | 0.1819 | 1.707 | 62.75 | 0.004972 | 0.02119 |
| Saturn-Sun Trine | Nifty Bank | 5 | 51 | 3.505 | 0.3 | 3.205 | 64.71 | 0.0001999 | 0.001677 |
| Saturn-Sun Trine | Nifty Bank | 10 | 51 | 6.385 | 0.5834 | 5.801 | 78.43 | 1.405e-05 | 0.0002142 |
| Saturn-Sun Trine | Nifty Bank | 20 | 51 | 8.287 | 1.172 | 7.115 | 76.47 | 2.508e-05 | 0.0003325 |
| Saturn-Sun Trine | Nifty Midcap 100 | 1 | 51 | -0.2949 | 0.05397 | -0.3489 | 50.98 | 0.09943 | 0.2162 |
| Saturn-Sun Trine | Nifty Midcap 100 | 3 | 51 | -0.1388 | 0.1609 | -0.2997 | 39.22 | 0.2687 | 0.4439 |
| Saturn-Sun Trine | Nifty Midcap 100 | 5 | 51 | -0.07582 | 0.266 | -0.3418 | 41.18 | 0.3201 | 0.4975 |
| Saturn-Sun Trine | Nifty Midcap 100 | 10 | 51 | 1.731 | 0.532 | 1.199 | 74.51 | 0.02588 | 0.07943 |
| Saturn-Sun Trine | Nifty Midcap 100 | 20 | 51 | 2.823 | 1.065 | 1.758 | 70.59 | 0.04212 | 0.1126 |
| Saturn-Sun Trine | Nifty Midcap 150 | 1 | 51 | 0.07839 | 0.05323 | 0.02516 | 50.98 | 0.8837 | 0.9417 |
| Saturn-Sun Trine | Nifty Midcap 150 | 3 | 51 | 0.1124 | 0.1594 | -0.04707 | 60.78 | 0.8413 | 0.9145 |
| Saturn-Sun Trine | Nifty Midcap 150 | 5 | 51 | 0.9224 | 0.2642 | 0.6582 | 72.55 | 0.04904 | 0.1266 |
| Saturn-Sun Trine | Nifty Midcap 150 | 10 | 51 | 2.802 | 0.5204 | 2.281 | 78.43 | 0.0001803 | 0.001554 |
| Saturn-Sun Trine | Nifty Midcap 150 | 20 | 51 | 2.944 | 1.047 | 1.897 | 76.47 | 0.01414 | 0.04983 |
| Saturn-Sun Trine | BSE Sensex | 1 | 51 | -0.2891 | 0.05036 | -0.3395 | 41.18 | 0.01756 | 0.05981 |
| Saturn-Sun Trine | BSE Sensex | 3 | 51 | 0.1456 | 0.1513 | -0.005707 | 50.98 | 0.9843 | 0.9948 |
| Saturn-Sun Trine | BSE Sensex | 5 | 51 | 0.888 | 0.2506 | 0.6374 | 62.75 | 0.109 | 0.2312 |
| Saturn-Sun Trine | BSE Sensex | 10 | 51 | 1.916 | 0.4957 | 1.421 | 70.59 | 0.02521 | 0.07805 |
| Saturn-Sun Trine | BSE Sensex | 20 | 51 | 2.25 | 1.002 | 1.248 | 72.55 | 0.1351 | 0.2724 |
| Saturn-Venus Opposition | Nifty 50 | 1 | 26 | 0.3386 | 0.04492 | 0.2937 | 57.69 | 0.2043 | 0.3657 |
| Saturn-Venus Opposition | Nifty 50 | 3 | 26 | 1.508 | 0.1333 | 1.375 | 76.92 | 0.03073 | 0.09017 |
| Saturn-Venus Opposition | Nifty 50 | 5 | 26 | 2.908 | 0.2178 | 2.69 | 65.38 | 0.007921 | 0.03127 |
| Saturn-Venus Opposition | Nifty 50 | 10 | 26 | 3.87 | 0.4212 | 3.449 | 69.23 | 0.009006 | 0.03464 |
| Saturn-Venus Opposition | Nifty 50 | 20 | 26 | 7.194 | 0.8264 | 6.368 | 61.54 | 0.01315 | 0.04745 |
| Saturn-Venus Opposition | Nifty Bank | 1 | 26 | 0.5226 | 0.06023 | 0.4624 | 50 | 0.1932 | 0.352 |
| Saturn-Venus Opposition | Nifty Bank | 3 | 26 | 2.054 | 0.1819 | 1.872 | 73.08 | 0.02328 | 0.07375 |
| Saturn-Venus Opposition | Nifty Bank | 5 | 26 | 3.141 | 0.3 | 2.841 | 57.69 | 0.01699 | 0.05791 |
| Saturn-Venus Opposition | Nifty Bank | 10 | 26 | 4.336 | 0.5834 | 3.753 | 65.38 | 0.02062 | 0.06736 |
| Saturn-Venus Opposition | Nifty Bank | 20 | 26 | 5.536 | 1.172 | 4.364 | 61.54 | 0.06011 | 0.1488 |
| Saturn-Venus Opposition | Nifty Midcap 100 | 1 | 26 | 0.3275 | 0.05397 | 0.2735 | 73.08 | 0.1402 | 0.2794 |
| Saturn-Venus Opposition | Nifty Midcap 100 | 3 | 26 | -0.2149 | 0.1609 | -0.3758 | 38.46 | 0.329 | 0.5075 |
| Saturn-Venus Opposition | Nifty Midcap 100 | 5 | 26 | 0.4395 | 0.266 | 0.1735 | 42.31 | 0.7736 | 0.8721 |
| Saturn-Venus Opposition | Nifty Midcap 100 | 10 | 26 | 2.451 | 0.532 | 1.919 | 76.92 | 0.02477 | 0.07715 |
| Saturn-Venus Opposition | Nifty Midcap 100 | 20 | 26 | 2.894 | 1.065 | 1.829 | 65.38 | 0.1855 | 0.3423 |
| Saturn-Venus Opposition | Nifty Midcap 150 | 1 | 26 | 0.3288 | 0.05323 | 0.2755 | 53.85 | 0.2605 | 0.4332 |
| Saturn-Venus Opposition | Nifty Midcap 150 | 3 | 26 | 0.1648 | 0.1594 | 0.00538 | 76.92 | 0.987 | 0.9953 |
| Saturn-Venus Opposition | Nifty Midcap 150 | 5 | 26 | 0.5994 | 0.2642 | 0.3351 | 61.54 | 0.4544 | 0.6337 |
| Saturn-Venus Opposition | Nifty Midcap 150 | 10 | 26 | 1.769 | 0.5204 | 1.249 | 69.23 | 0.07733 | 0.1784 |
| Saturn-Venus Opposition | Nifty Midcap 150 | 20 | 26 | 1.294 | 1.047 | 0.2469 | 57.69 | 0.7537 | 0.8587 |
| Saturn-Venus Opposition | BSE Sensex | 1 | 26 | 0.1195 | 0.05036 | 0.06917 | 38.46 | 0.7818 | 0.8761 |
| Saturn-Venus Opposition | BSE Sensex | 3 | 26 | 0.3351 | 0.1513 | 0.1837 | 65.38 | 0.674 | 0.8079 |
| Saturn-Venus Opposition | BSE Sensex | 5 | 26 | 0.6775 | 0.2506 | 0.427 | 57.69 | 0.4655 | 0.6423 |
| Saturn-Venus Opposition | BSE Sensex | 10 | 26 | 1.192 | 0.4957 | 0.6962 | 65.38 | 0.395 | 0.5785 |
| Saturn-Venus Opposition | BSE Sensex | 20 | 26 | 1.276 | 1.002 | 0.2739 | 53.85 | 0.7779 | 0.8736 |
| Saturn-Venus Square | Nifty 50 | 1 | 55 | 0.3325 | 0.04492 | 0.2876 | 61.82 | 0.03759 | 0.1046 |
| Saturn-Venus Square | Nifty 50 | 3 | 55 | 1.561 | 0.1333 | 1.427 | 63.64 | 0.0005334 | 0.003611 |
| Saturn-Venus Square | Nifty 50 | 5 | 55 | 2.631 | 0.2178 | 2.413 | 65.45 | 0.0004885 | 0.003396 |
| Saturn-Venus Square | Nifty 50 | 10 | 55 | 3.093 | 0.4212 | 2.672 | 72.73 | 0.01326 | 0.04764 |
| Saturn-Venus Square | Nifty 50 | 20 | 55 | 6.748 | 0.8264 | 5.921 | 70.91 | 0.00176 | 0.009164 |
| Saturn-Venus Square | Nifty Bank | 1 | 55 | 0.6748 | 0.06023 | 0.6146 | 69.09 | 0.01269 | 0.04626 |
| Saturn-Venus Square | Nifty Bank | 3 | 55 | 2 | 0.1819 | 1.818 | 61.82 | 0.0006419 | 0.004136 |
| Saturn-Venus Square | Nifty Bank | 5 | 55 | 2.889 | 0.3 | 2.589 | 69.09 | 0.001665 | 0.008745 |
| Saturn-Venus Square | Nifty Bank | 10 | 55 | 3.808 | 0.5834 | 3.224 | 67.27 | 0.01259 | 0.04599 |
| Saturn-Venus Square | Nifty Bank | 20 | 55 | 5.699 | 1.172 | 4.527 | 69.09 | 0.01296 | 0.04694 |
| Saturn-Venus Square | Nifty Midcap 100 | 1 | 55 | 0.08752 | 0.05397 | 0.03355 | 65.45 | 0.836 | 0.9121 |
| Saturn-Venus Square | Nifty Midcap 100 | 3 | 55 | 0.02893 | 0.1609 | -0.1319 | 41.82 | 0.6526 | 0.7932 |
| Saturn-Venus Square | Nifty Midcap 100 | 5 | 55 | 0.1489 | 0.266 | -0.1171 | 38.18 | 0.7368 | 0.8481 |
| Saturn-Venus Square | Nifty Midcap 100 | 10 | 55 | 1.367 | 0.532 | 0.8354 | 69.09 | 0.2871 | 0.4622 |
| Saturn-Venus Square | Nifty Midcap 100 | 20 | 55 | 2.262 | 1.065 | 1.197 | 70.91 | 0.1869 | 0.3441 |
| Saturn-Venus Square | Nifty Midcap 150 | 1 | 55 | 0.3824 | 0.05323 | 0.3292 | 61.82 | 0.04941 | 0.1274 |
| Saturn-Venus Square | Nifty Midcap 150 | 3 | 55 | 0.02433 | 0.1594 | -0.1351 | 61.82 | 0.627 | 0.7741 |
| Saturn-Venus Square | Nifty Midcap 150 | 5 | 55 | 0.304 | 0.2642 | 0.03972 | 60 | 0.9094 | 0.959 |
| Saturn-Venus Square | Nifty Midcap 150 | 10 | 55 | 0.9647 | 0.5204 | 0.4443 | 67.27 | 0.5665 | 0.7275 |
| Saturn-Venus Square | Nifty Midcap 150 | 20 | 55 | 1.104 | 1.047 | 0.05657 | 74.55 | 0.9498 | 0.9798 |
| Saturn-Venus Square | BSE Sensex | 1 | 55 | 0.04614 | 0.05036 | -0.004218 | 52.73 | 0.9807 | 0.9923 |
| Saturn-Venus Square | BSE Sensex | 3 | 55 | -0.07245 | 0.1513 | -0.2238 | 50.91 | 0.4598 | 0.6379 |
| Saturn-Venus Square | BSE Sensex | 5 | 55 | 0.01891 | 0.2506 | -0.2317 | 52.73 | 0.5544 | 0.7203 |
| Saturn-Venus Square | BSE Sensex | 10 | 55 | 0.2086 | 0.4957 | -0.2871 | 61.82 | 0.7172 | 0.8361 |
| Saturn-Venus Square | BSE Sensex | 20 | 55 | 0.5739 | 1.002 | -0.4277 | 65.45 | 0.6599 | 0.7975 |
| Saturn-Venus Trine | Nifty 50 | 1 | 53 | 0.4125 | 0.04492 | 0.3676 | 67.92 | 0.0008319 | 0.005097 |
| Saturn-Venus Trine | Nifty 50 | 3 | 53 | 1.809 | 0.1333 | 1.676 | 67.92 | 6.434e-05 | 0.0007006 |
| Saturn-Venus Trine | Nifty 50 | 5 | 53 | 3.361 | 0.2178 | 3.143 | 73.58 | 3.255e-06 | 6.563e-05 |
| Saturn-Venus Trine | Nifty 50 | 10 | 53 | 4.627 | 0.4212 | 4.206 | 69.81 | 6.939e-06 | 0.0001172 |
| Saturn-Venus Trine | Nifty 50 | 20 | 53 | 9.362 | 0.8264 | 8.535 | 77.36 | 1.482e-06 | 3.348e-05 |
| Saturn-Venus Trine | Nifty Bank | 1 | 53 | 0.7961 | 0.06023 | 0.7359 | 67.92 | 0.0007396 | 0.004638 |
| Saturn-Venus Trine | Nifty Bank | 3 | 53 | 2.255 | 0.1819 | 2.073 | 67.92 | 9.022e-05 | 0.000907 |
| Saturn-Venus Trine | Nifty Bank | 5 | 53 | 3.938 | 0.3 | 3.638 | 73.58 | 3.546e-06 | 6.925e-05 |
| Saturn-Venus Trine | Nifty Bank | 10 | 53 | 5.739 | 0.5834 | 5.156 | 73.58 | 1.469e-05 | 0.0002221 |
| Saturn-Venus Trine | Nifty Bank | 20 | 53 | 8.447 | 1.172 | 7.274 | 71.7 | 2.311e-05 | 0.0003149 |
| Saturn-Venus Trine | Nifty Midcap 100 | 1 | 53 | -0.03161 | 0.05397 | -0.08558 | 60.38 | 0.4695 | 0.6469 |
| Saturn-Venus Trine | Nifty Midcap 100 | 3 | 53 | 0.1385 | 0.1609 | -0.0224 | 39.62 | 0.9428 | 0.9769 |
| Saturn-Venus Trine | Nifty Midcap 100 | 5 | 53 | 0.2026 | 0.266 | -0.06344 | 41.51 | 0.8353 | 0.9119 |
| Saturn-Venus Trine | Nifty Midcap 100 | 10 | 53 | 2.218 | 0.532 | 1.686 | 79.25 | 0.001156 | 0.006631 |
| Saturn-Venus Trine | Nifty Midcap 100 | 20 | 53 | 3.511 | 1.065 | 2.446 | 75.47 | 0.001424 | 0.007773 |
| Saturn-Venus Trine | Nifty Midcap 150 | 1 | 53 | 0.476 | 0.05323 | 0.4228 | 67.92 | 0.001462 | 0.007948 |
| Saturn-Venus Trine | Nifty Midcap 150 | 3 | 53 | 0.1936 | 0.1594 | 0.03418 | 66.04 | 0.8922 | 0.946 |
| Saturn-Venus Trine | Nifty Midcap 150 | 5 | 53 | 0.751 | 0.2642 | 0.4868 | 69.81 | 0.105 | 0.2249 |
| Saturn-Venus Trine | Nifty Midcap 150 | 10 | 53 | 1.974 | 0.5204 | 1.454 | 69.81 | 0.03103 | 0.09078 |
| Saturn-Venus Trine | Nifty Midcap 150 | 20 | 53 | 2.836 | 1.047 | 1.789 | 73.58 | 0.02035 | 0.06677 |
| Saturn-Venus Trine | BSE Sensex | 1 | 53 | -0.04072 | 0.05036 | -0.09108 | 50.94 | 0.5107 | 0.6842 |
| Saturn-Venus Trine | BSE Sensex | 3 | 53 | 0.08784 | 0.1513 | -0.06347 | 50.94 | 0.831 | 0.9091 |
| Saturn-Venus Trine | BSE Sensex | 5 | 53 | 0.3597 | 0.2506 | 0.1092 | 58.49 | 0.7574 | 0.8604 |
| Saturn-Venus Trine | BSE Sensex | 10 | 53 | 0.954 | 0.4957 | 0.4583 | 60.38 | 0.4642 | 0.6421 |
| Saturn-Venus Trine | BSE Sensex | 20 | 53 | 1.699 | 1.002 | 0.6973 | 66.04 | 0.3861 | 0.5686 |

### Conjunctions (Yuti)

* When Jupiter conjoined Ketu (3 events since 2005), Nifty 50 averaged +5.22% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +5.00 pp above the unconditional baseline. Not statistically significant (p=0.157, q=0.3048 after Benjamini-Hochberg correction).
* When Jupiter conjoined Ketu (3 events since 2005), Nifty Bank averaged +6.35% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +6.05 pp above the unconditional baseline. Not statistically significant (p=0.1251, q=0.2567 after Benjamini-Hochberg correction).
* When Jupiter conjoined Ketu (3 events since 2005), Nifty Midcap 100 averaged +0.81% over the next 5 trading days (base rate +0.27%). Win rate 66.7%. That is +0.54 pp above the unconditional baseline. Not statistically significant (p=0.5334, q=0.7018 after Benjamini-Hochberg correction).
* When Jupiter conjoined Ketu (3 events since 2005), Nifty Midcap 150 averaged +2.61% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +2.34 pp above the unconditional baseline. Nominally significant at p=0.04725, but it does not survive Benjamini-Hochberg correction (q=0.1231).
* When Jupiter conjoined Ketu (3 events since 2005), BSE Sensex averaged +1.51% over the next 5 trading days (base rate +0.25%). Win rate 66.7%. That is +1.26 pp above the unconditional baseline. Not statistically significant (p=0.4634, q=0.6414 after Benjamini-Hochberg correction).

* When Jupiter conjoined Mars (12 events since 2000), Nifty 50 averaged +2.88% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is +2.66 pp above the unconditional baseline. Not statistically significant (p=0.1095, q=0.2321 after Benjamini-Hochberg correction).
* When Jupiter conjoined Mars (12 events since 2000), Nifty Bank averaged +2.50% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is +2.20 pp above the unconditional baseline. Not statistically significant (p=0.284, q=0.4596 after Benjamini-Hochberg correction).
* When Jupiter conjoined Mars (12 events since 2000), Nifty Midcap 100 averaged +0.82% over the next 5 trading days (base rate +0.27%). Win rate 58.3%. That is +0.55 pp above the unconditional baseline. Not statistically significant (p=0.2457, q=0.4153 after Benjamini-Hochberg correction).
* When Jupiter conjoined Mars (12 events since 2000), Nifty Midcap 150 averaged +0.12% over the next 5 trading days (base rate +0.26%). Win rate 50.0%. That is -0.15 pp below the unconditional baseline. Not statistically significant (p=0.8002, q=0.8881 after Benjamini-Hochberg correction).
* When Jupiter conjoined Mars (12 events since 2000), BSE Sensex averaged +0.83% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is +0.58 pp above the unconditional baseline. Not statistically significant (p=0.4802, q=0.6584 after Benjamini-Hochberg correction).

* When Jupiter conjoined Mercury (39 events since 2000), Nifty 50 averaged +2.79% over the next 5 trading days (base rate +0.22%). Win rate 56.4%. That is +2.57 pp above the unconditional baseline. Statistically significant at p=0.002394 and after Benjamini-Hochberg correction (q=0.01157).
* When Jupiter conjoined Mercury (39 events since 2000), Nifty Bank averaged +2.92% over the next 5 trading days (base rate +0.30%). Win rate 59.0%. That is +2.62 pp above the unconditional baseline. Statistically significant at p=0.008422 and after Benjamini-Hochberg correction (q=0.0328).
* When Jupiter conjoined Mercury (39 events since 2000), Nifty Midcap 100 averaged +0.41% over the next 5 trading days (base rate +0.27%). Win rate 43.6%. That is +0.14 pp above the unconditional baseline. Not statistically significant (p=0.7429, q=0.851 after Benjamini-Hochberg correction).
* When Jupiter conjoined Mercury (39 events since 2000), Nifty Midcap 150 averaged +0.52% over the next 5 trading days (base rate +0.26%). Win rate 53.8%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.5071, q=0.6827 after Benjamini-Hochberg correction).
* When Jupiter conjoined Mercury (39 events since 2000), BSE Sensex averaged -0.06% over the next 5 trading days (base rate +0.25%). Win rate 43.6%. That is -0.31 pp below the unconditional baseline. Not statistically significant (p=0.4957, q=0.6734 after Benjamini-Hochberg correction).

* When Jupiter conjoined Moon (55 events since 2000), Nifty 50 averaged +3.30% over the next 5 trading days (base rate +0.22%). Win rate 63.6%. That is +3.08 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004043).
* When Jupiter conjoined Moon (55 events since 2000), Nifty Bank averaged +3.64% over the next 5 trading days (base rate +0.30%). Win rate 67.3%. That is +3.34 pp above the unconditional baseline. Statistically significant at p=0.000216 and after Benjamini-Hochberg correction (q=0.001759).
* When Jupiter conjoined Moon (55 events since 2000), Nifty Midcap 100 averaged +0.12% over the next 5 trading days (base rate +0.27%). Win rate 36.4%. That is -0.15 pp below the unconditional baseline. Not statistically significant (p=0.6698, q=0.8046 after Benjamini-Hochberg correction).
* When Jupiter conjoined Moon (55 events since 2000), Nifty Midcap 150 averaged +0.47% over the next 5 trading days (base rate +0.26%). Win rate 61.8%. That is +0.20 pp above the unconditional baseline. Not statistically significant (p=0.5401, q=0.7079 after Benjamini-Hochberg correction).
* When Jupiter conjoined Moon (55 events since 2000), BSE Sensex averaged +0.17% over the next 5 trading days (base rate +0.25%). Win rate 50.9%. That is -0.08 pp below the unconditional baseline. Not statistically significant (p=0.8442, q=0.9163 after Benjamini-Hochberg correction).

* When Jupiter conjoined Rahu (4 events since 2001), Nifty 50 averaged +2.00% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is +1.78 pp above the unconditional baseline. Not statistically significant (p=0.607, q=0.7565 after Benjamini-Hochberg correction).
* When Jupiter conjoined Rahu (4 events since 2001), Nifty Bank averaged +1.08% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is +0.78 pp above the unconditional baseline. Not statistically significant (p=0.8666, q=0.9304 after Benjamini-Hochberg correction).
* When Jupiter conjoined Rahu (4 events since 2001), Nifty Midcap 100 averaged -1.20% over the next 5 trading days (base rate +0.27%). Win rate 25.0%. That is -1.47 pp below the unconditional baseline. Not statistically significant (p=0.4494, q=0.6292 after Benjamini-Hochberg correction).
* When Jupiter conjoined Rahu (4 events since 2001), Nifty Midcap 150 averaged +0.07% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is -0.20 pp below the unconditional baseline. Not statistically significant (p=0.9245, q=0.9669 after Benjamini-Hochberg correction).
* When Jupiter conjoined Rahu (4 events since 2001), BSE Sensex averaged -0.60% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.86 pp below the unconditional baseline. Not statistically significant (p=0.7015, q=0.8237 after Benjamini-Hochberg correction).

* When Jupiter conjoined Saturn (2 events since 2000), Nifty 50 averaged +7.13% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +6.92 pp above the unconditional baseline. Not statistically significant (p=0.2289, q=0.3952 after Benjamini-Hochberg correction).
* When Jupiter conjoined Saturn (2 events since 2000), Nifty Bank averaged +8.63% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +8.33 pp above the unconditional baseline. Not statistically significant (p=0.1711, q=0.3249 after Benjamini-Hochberg correction).
* When Jupiter conjoined Saturn (2 events since 2000), Nifty Midcap 100 averaged +2.98% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +2.72 pp above the unconditional baseline. Not statistically significant (p=0.559, q=0.7248 after Benjamini-Hochberg correction).
* When Jupiter conjoined Saturn (2 events since 2000), Nifty Midcap 150 averaged +3.05% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +2.78 pp above the unconditional baseline. Not statistically significant (p=0.3082, q=0.4866 after Benjamini-Hochberg correction).
* When Jupiter conjoined Saturn (2 events since 2000), BSE Sensex averaged +6.34% over the next 5 trading days (base rate +0.25%). Win rate 100.0%. That is +6.09 pp above the unconditional baseline. Not statistically significant (p=0.1846, q=0.3415 after Benjamini-Hochberg correction).

* When Jupiter conjoined Sun (25 events since 2000), Nifty 50 averaged +3.42% over the next 5 trading days (base rate +0.22%). Win rate 72.0%. That is +3.20 pp above the unconditional baseline. Statistically significant at p=0.002891 and after Benjamini-Hochberg correction (q=0.01358).
* When Jupiter conjoined Sun (25 events since 2000), Nifty Bank averaged +4.22% over the next 5 trading days (base rate +0.30%). Win rate 80.0%. That is +3.92 pp above the unconditional baseline. Statistically significant at p=0.002774 and after Benjamini-Hochberg correction (q=0.01315).
* When Jupiter conjoined Sun (25 events since 2000), Nifty Midcap 100 averaged -0.01% over the next 5 trading days (base rate +0.27%). Win rate 40.0%. That is -0.28 pp below the unconditional baseline. Not statistically significant (p=0.6295, q=0.7765 after Benjamini-Hochberg correction).
* When Jupiter conjoined Sun (25 events since 2000), Nifty Midcap 150 averaged +1.10% over the next 5 trading days (base rate +0.26%). Win rate 68.0%. That is +0.84 pp above the unconditional baseline. Not statistically significant (p=0.1242, q=0.2557 after Benjamini-Hochberg correction).
* When Jupiter conjoined Sun (25 events since 2000), BSE Sensex averaged +0.30% over the next 5 trading days (base rate +0.25%). Win rate 44.0%. That is +0.05 pp above the unconditional baseline. Not statistically significant (p=0.94, q=0.9756 after Benjamini-Hochberg correction).

* When Jupiter conjoined Venus (27 events since 2000), Nifty 50 averaged +2.09% over the next 5 trading days (base rate +0.22%). Win rate 51.9%. That is +1.87 pp above the unconditional baseline. Not statistically significant (p=0.06663, q=0.1599 after Benjamini-Hochberg correction).
* When Jupiter conjoined Venus (27 events since 2000), Nifty Bank averaged +2.59% over the next 5 trading days (base rate +0.30%). Win rate 59.3%. That is +2.29 pp above the unconditional baseline. Not statistically significant (p=0.05498, q=0.1382 after Benjamini-Hochberg correction).
* When Jupiter conjoined Venus (27 events since 2000), Nifty Midcap 100 averaged -0.38% over the next 5 trading days (base rate +0.27%). Win rate 33.3%. That is -0.65 pp below the unconditional baseline. Not statistically significant (p=0.07635, q=0.1767 after Benjamini-Hochberg correction).
* When Jupiter conjoined Venus (27 events since 2000), Nifty Midcap 150 averaged +0.02% over the next 5 trading days (base rate +0.26%). Win rate 51.9%. That is -0.24 pp below the unconditional baseline. Not statistically significant (p=0.597, q=0.7511 after Benjamini-Hochberg correction).
* When Jupiter conjoined Venus (27 events since 2000), BSE Sensex averaged -0.24% over the next 5 trading days (base rate +0.25%). Win rate 44.4%. That is -0.49 pp below the unconditional baseline. Not statistically significant (p=0.4026, q=0.5848 after Benjamini-Hochberg correction).

* When Ketu conjoined Mars (17 events since 2001), Nifty 50 averaged +1.48% over the next 5 trading days (base rate +0.22%). Win rate 58.8%. That is +1.26 pp above the unconditional baseline. Not statistically significant (p=0.379, q=0.5608 after Benjamini-Hochberg correction).
* When Ketu conjoined Mars (17 events since 2001), Nifty Bank averaged +1.61% over the next 5 trading days (base rate +0.30%). Win rate 58.8%. That is +1.31 pp above the unconditional baseline. Not statistically significant (p=0.4647, q=0.6421 after Benjamini-Hochberg correction).
* When Ketu conjoined Mars (17 events since 2001), Nifty Midcap 100 averaged -0.65% over the next 5 trading days (base rate +0.27%). Win rate 29.4%. That is -0.92 pp below the unconditional baseline. Not statistically significant (p=0.2189, q=0.3844 after Benjamini-Hochberg correction).
* When Ketu conjoined Mars (17 events since 2001), Nifty Midcap 150 averaged -0.72% over the next 5 trading days (base rate +0.26%). Win rate 52.9%. That is -0.98 pp below the unconditional baseline. Not statistically significant (p=0.2784, q=0.4549 after Benjamini-Hochberg correction).
* When Ketu conjoined Mars (17 events since 2001), BSE Sensex averaged -1.39% over the next 5 trading days (base rate +0.25%). Win rate 41.2%. That is -1.64 pp below the unconditional baseline. Not statistically significant (p=0.08399, q=0.1894 after Benjamini-Hochberg correction).

* When Ketu conjoined Mercury (28 events since 2000), Nifty 50 averaged +3.08% over the next 5 trading days (base rate +0.22%). Win rate 67.9%. That is +2.86 pp above the unconditional baseline. Statistically significant at p=0.005301 and after Benjamini-Hochberg correction (q=0.02236).
* When Ketu conjoined Mercury (28 events since 2000), Nifty Bank averaged +3.55% over the next 5 trading days (base rate +0.30%). Win rate 64.3%. That is +3.25 pp above the unconditional baseline. Statistically significant at p=0.008123 and after Benjamini-Hochberg correction (q=0.03179).
* When Ketu conjoined Mercury (28 events since 2000), Nifty Midcap 100 averaged +0.51% over the next 5 trading days (base rate +0.27%). Win rate 46.4%. That is +0.24 pp above the unconditional baseline. Not statistically significant (p=0.4366, q=0.6173 after Benjamini-Hochberg correction).
* When Ketu conjoined Mercury (28 events since 2000), Nifty Midcap 150 averaged +0.72% over the next 5 trading days (base rate +0.26%). Win rate 67.9%. That is +0.45 pp above the unconditional baseline. Not statistically significant (p=0.3317, q=0.511 after Benjamini-Hochberg correction).
* When Ketu conjoined Mercury (28 events since 2000), BSE Sensex averaged +0.38% over the next 5 trading days (base rate +0.25%). Win rate 53.6%. That is +0.13 pp above the unconditional baseline. Not statistically significant (p=0.7969, q=0.8854 after Benjamini-Hochberg correction).

* When Ketu conjoined Moon (57 events since 2000), Nifty 50 averaged +3.30% over the next 5 trading days (base rate +0.22%). Win rate 68.4%. That is +3.08 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0002488).
* When Ketu conjoined Moon (57 events since 2000), Nifty Bank averaged +3.73% over the next 5 trading days (base rate +0.30%). Win rate 57.9%. That is +3.43 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0004806).
* When Ketu conjoined Moon (57 events since 2000), Nifty Midcap 100 averaged +0.13% over the next 5 trading days (base rate +0.27%). Win rate 43.9%. That is -0.14 pp below the unconditional baseline. Not statistically significant (p=0.6922, q=0.8183 after Benjamini-Hochberg correction).
* When Ketu conjoined Moon (57 events since 2000), Nifty Midcap 150 averaged +0.41% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.15 pp above the unconditional baseline. Not statistically significant (p=0.6627, q=0.7996 after Benjamini-Hochberg correction).
* When Ketu conjoined Moon (57 events since 2000), BSE Sensex averaged +0.51% over the next 5 trading days (base rate +0.25%). Win rate 54.4%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.5676, q=0.7282 after Benjamini-Hochberg correction).

* When Ketu conjoined Saturn (2 events since 2007), Nifty 50 averaged -1.55% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is -1.77 pp below the unconditional baseline. Not statistically significant (p=0.5913, q=0.7471 after Benjamini-Hochberg correction).
* When Ketu conjoined Saturn (2 events since 2007), Nifty Bank averaged -1.77% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is -2.07 pp below the unconditional baseline. Not statistically significant (p=0.7336, q=0.8454 after Benjamini-Hochberg correction).
* When Ketu conjoined Saturn (2 events since 2007), Nifty Midcap 100 averaged -1.12% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is -1.39 pp below the unconditional baseline. Not statistically significant (p=0.5147, q=0.6878 after Benjamini-Hochberg correction).
* When Ketu conjoined Saturn (2 events since 2007), Nifty Midcap 150 averaged -1.79% over the next 5 trading days (base rate +0.26%). Win rate 50.0%. That is -2.06 pp below the unconditional baseline. Not statistically significant (p=0.5966, q=0.7511 after Benjamini-Hochberg correction).
* When Ketu conjoined Saturn (2 events since 2007), BSE Sensex averaged -1.91% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -2.16 pp below the unconditional baseline. Not statistically significant (p=0.576, q=0.7342 after Benjamini-Hochberg correction).

* When Ketu conjoined Sun (29 events since 2000), Nifty 50 averaged +2.51% over the next 5 trading days (base rate +0.22%). Win rate 55.2%. That is +2.30 pp above the unconditional baseline. Nominally significant at p=0.02786, but it does not survive Benjamini-Hochberg correction (q=0.08406).
* When Ketu conjoined Sun (29 events since 2000), Nifty Bank averaged +2.73% over the next 5 trading days (base rate +0.30%). Win rate 55.2%. That is +2.43 pp above the unconditional baseline. Nominally significant at p=0.04765, but it does not survive Benjamini-Hochberg correction (q=0.1238).
* When Ketu conjoined Sun (29 events since 2000), Nifty Midcap 100 averaged +0.39% over the next 5 trading days (base rate +0.27%). Win rate 41.4%. That is +0.12 pp above the unconditional baseline. Not statistically significant (p=0.7999, q=0.888 after Benjamini-Hochberg correction).
* When Ketu conjoined Sun (29 events since 2000), Nifty Midcap 150 averaged -0.02% over the next 5 trading days (base rate +0.26%). Win rate 55.2%. That is -0.29 pp below the unconditional baseline. Not statistically significant (p=0.5211, q=0.6939 after Benjamini-Hochberg correction).
* When Ketu conjoined Sun (29 events since 2000), BSE Sensex averaged -0.99% over the next 5 trading days (base rate +0.25%). Win rate 34.5%. That is -1.24 pp below the unconditional baseline. Nominally significant at p=0.01914, but it does not survive Benjamini-Hochberg correction (q=0.06436).

* When Ketu conjoined Venus (29 events since 2000), Nifty 50 averaged +2.73% over the next 5 trading days (base rate +0.22%). Win rate 75.9%. That is +2.52 pp above the unconditional baseline. Statistically significant at p=0.01173 and after Benjamini-Hochberg correction (q=0.04321).
* When Ketu conjoined Venus (29 events since 2000), Nifty Bank averaged +3.23% over the next 5 trading days (base rate +0.30%). Win rate 72.4%. That is +2.93 pp above the unconditional baseline. Statistically significant at p=0.009377 and after Benjamini-Hochberg correction (q=0.03581).
* When Ketu conjoined Venus (29 events since 2000), Nifty Midcap 100 averaged +0.50% over the next 5 trading days (base rate +0.27%). Win rate 48.3%. That is +0.23 pp above the unconditional baseline. Not statistically significant (p=0.6676, q=0.8036 after Benjamini-Hochberg correction).
* When Ketu conjoined Venus (29 events since 2000), Nifty Midcap 150 averaged +0.44% over the next 5 trading days (base rate +0.26%). Win rate 72.4%. That is +0.17 pp above the unconditional baseline. Not statistically significant (p=0.7183, q=0.8361 after Benjamini-Hochberg correction).
* When Ketu conjoined Venus (29 events since 2000), BSE Sensex averaged +0.56% over the next 5 trading days (base rate +0.25%). Win rate 62.1%. That is +0.31 pp above the unconditional baseline. Not statistically significant (p=0.5643, q=0.7258 after Benjamini-Hochberg correction).

* When Mars conjoined Mercury (43 events since 2000), Nifty 50 averaged +1.88% over the next 5 trading days (base rate +0.22%). Win rate 65.1%. That is +1.66 pp above the unconditional baseline. Nominally significant at p=0.03318, but it does not survive Benjamini-Hochberg correction (q=0.09549).
* When Mars conjoined Mercury (43 events since 2000), Nifty Bank averaged +2.12% over the next 5 trading days (base rate +0.30%). Win rate 65.1%. That is +1.82 pp above the unconditional baseline. Nominally significant at p=0.04804, but it does not survive Benjamini-Hochberg correction (q=0.1247).
* When Mars conjoined Mercury (43 events since 2000), Nifty Midcap 100 averaged -0.51% over the next 5 trading days (base rate +0.27%). Win rate 41.9%. That is -0.77 pp below the unconditional baseline. Not statistically significant (p=0.1268, q=0.2598 after Benjamini-Hochberg correction).
* When Mars conjoined Mercury (43 events since 2000), Nifty Midcap 150 averaged -0.05% over the next 5 trading days (base rate +0.26%). Win rate 65.1%. That is -0.31 pp below the unconditional baseline. Not statistically significant (p=0.4261, q=0.6078 after Benjamini-Hochberg correction).
* When Mars conjoined Mercury (43 events since 2000), BSE Sensex averaged -0.25% over the next 5 trading days (base rate +0.25%). Win rate 58.1%. That is -0.50 pp below the unconditional baseline. Not statistically significant (p=0.2146, q=0.3781 after Benjamini-Hochberg correction).

* When Mars conjoined Moon (54 events since 2000), Nifty 50 averaged +2.28% over the next 5 trading days (base rate +0.22%). Win rate 63.0%. That is +2.06 pp above the unconditional baseline. Statistically significant at p=0.003425 and after Benjamini-Hochberg correction (q=0.01565).
* When Mars conjoined Moon (54 events since 2000), Nifty Bank averaged +2.61% over the next 5 trading days (base rate +0.30%). Win rate 63.0%. That is +2.31 pp above the unconditional baseline. Statistically significant at p=0.007003 and after Benjamini-Hochberg correction (q=0.02797).
* When Mars conjoined Moon (54 events since 2000), Nifty Midcap 100 averaged -0.39% over the next 5 trading days (base rate +0.27%). Win rate 37.0%. That is -0.65 pp below the unconditional baseline. Not statistically significant (p=0.07767, q=0.179 after Benjamini-Hochberg correction).
* When Mars conjoined Moon (54 events since 2000), Nifty Midcap 150 averaged +0.22% over the next 5 trading days (base rate +0.26%). Win rate 63.0%. That is -0.04 pp below the unconditional baseline. Not statistically significant (p=0.8931, q=0.9466 after Benjamini-Hochberg correction).
* When Mars conjoined Moon (54 events since 2000), BSE Sensex averaged -0.20% over the next 5 trading days (base rate +0.25%). Win rate 53.7%. That is -0.45 pp below the unconditional baseline. Not statistically significant (p=0.176, q=0.33 after Benjamini-Hochberg correction).

* When Mars conjoined Rahu (16 events since 2000), Nifty 50 averaged +3.14% over the next 5 trading days (base rate +0.22%). Win rate 68.8%. That is +2.92 pp above the unconditional baseline. Nominally significant at p=0.02918, but it does not survive Benjamini-Hochberg correction (q=0.08691).
* When Mars conjoined Rahu (16 events since 2000), Nifty Bank averaged +3.07% over the next 5 trading days (base rate +0.30%). Win rate 68.8%. That is +2.77 pp above the unconditional baseline. Not statistically significant (p=0.1054, q=0.2251 after Benjamini-Hochberg correction).
* When Mars conjoined Rahu (16 events since 2000), Nifty Midcap 100 averaged +0.23% over the next 5 trading days (base rate +0.27%). Win rate 37.5%. That is -0.03 pp below the unconditional baseline. Not statistically significant (p=0.9557, q=0.982 after Benjamini-Hochberg correction).
* When Mars conjoined Rahu (16 events since 2000), Nifty Midcap 150 averaged +0.52% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.5485, q=0.7152 after Benjamini-Hochberg correction).
* When Mars conjoined Rahu (16 events since 2000), BSE Sensex averaged +0.19% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.9246, q=0.9669 after Benjamini-Hochberg correction).

* When Mars conjoined Saturn (14 events since 2000), Nifty 50 averaged +2.89% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +2.67 pp above the unconditional baseline. Not statistically significant (p=0.07596, q=0.176 after Benjamini-Hochberg correction).
* When Mars conjoined Saturn (14 events since 2000), Nifty Bank averaged +3.30% over the next 5 trading days (base rate +0.30%). Win rate 64.3%. That is +3.00 pp above the unconditional baseline. Not statistically significant (p=0.06634, q=0.1593 after Benjamini-Hochberg correction).
* When Mars conjoined Saturn (14 events since 2000), Nifty Midcap 100 averaged -1.91% over the next 5 trading days (base rate +0.27%). Win rate 21.4%. That is -2.17 pp below the unconditional baseline. Not statistically significant (p=0.07965, q=0.1822 after Benjamini-Hochberg correction).
* When Mars conjoined Saturn (14 events since 2000), Nifty Midcap 150 averaged +0.56% over the next 5 trading days (base rate +0.26%). Win rate 71.4%. That is +0.30 pp above the unconditional baseline. Not statistically significant (p=0.6865, q=0.8141 after Benjamini-Hochberg correction).
* When Mars conjoined Saturn (14 events since 2000), BSE Sensex averaged -0.72% over the next 5 trading days (base rate +0.25%). Win rate 57.1%. That is -0.97 pp below the unconditional baseline. Not statistically significant (p=0.3332, q=0.512 after Benjamini-Hochberg correction).

* When Mars conjoined Sun (13 events since 2000), Nifty 50 averaged +4.53% over the next 5 trading days (base rate +0.22%). Win rate 76.9%. That is +4.32 pp above the unconditional baseline. Statistically significant at p=0.004496 and after Benjamini-Hochberg correction (q=0.01949).
* When Mars conjoined Sun (13 events since 2000), Nifty Bank averaged +5.36% over the next 5 trading days (base rate +0.30%). Win rate 92.3%. That is +5.06 pp above the unconditional baseline. Statistically significant at p=0.001902 and after Benjamini-Hochberg correction (q=0.009772).
* When Mars conjoined Sun (13 events since 2000), Nifty Midcap 100 averaged -0.39% over the next 5 trading days (base rate +0.27%). Win rate 23.1%. That is -0.66 pp below the unconditional baseline. Not statistically significant (p=0.1965, q=0.3556 after Benjamini-Hochberg correction).
* When Mars conjoined Sun (13 events since 2000), Nifty Midcap 150 averaged +2.18% over the next 5 trading days (base rate +0.26%). Win rate 84.6%. That is +1.91 pp above the unconditional baseline. Nominally significant at p=0.02605, but it does not survive Benjamini-Hochberg correction (q=0.07975).
* When Mars conjoined Sun (13 events since 2000), BSE Sensex averaged +2.18% over the next 5 trading days (base rate +0.25%). Win rate 76.9%. That is +1.93 pp above the unconditional baseline. Nominally significant at p=0.02317, but it does not survive Benjamini-Hochberg correction (q=0.07348).

* When Mars conjoined Venus (21 events since 2000), Nifty 50 averaged +2.73% over the next 5 trading days (base rate +0.22%). Win rate 61.9%. That is +2.51 pp above the unconditional baseline. Nominally significant at p=0.02194, but it does not survive Benjamini-Hochberg correction (q=0.07068).
* When Mars conjoined Venus (21 events since 2000), Nifty Bank averaged +3.51% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +3.21 pp above the unconditional baseline. Statistically significant at p=0.01272 and after Benjamini-Hochberg correction (q=0.0463).
* When Mars conjoined Venus (21 events since 2000), Nifty Midcap 100 averaged +0.36% over the next 5 trading days (base rate +0.27%). Win rate 38.1%. That is +0.09 pp above the unconditional baseline. Not statistically significant (p=0.9149, q=0.9623 after Benjamini-Hochberg correction).
* When Mars conjoined Venus (21 events since 2000), Nifty Midcap 150 averaged +0.88% over the next 5 trading days (base rate +0.26%). Win rate 57.1%. That is +0.61 pp above the unconditional baseline. Not statistically significant (p=0.2541, q=0.4265 after Benjamini-Hochberg correction).
* When Mars conjoined Venus (21 events since 2000), BSE Sensex averaged +0.25% over the next 5 trading days (base rate +0.25%). Win rate 42.9%. Not statistically significant (p=0.9951, q=0.9976 after Benjamini-Hochberg correction).

* When Mercury conjoined Moon (57 events since 2001), Nifty 50 averaged +2.89% over the next 5 trading days (base rate +0.22%). Win rate 68.4%. That is +2.68 pp above the unconditional baseline. Statistically significant at p=0.0006101 and after Benjamini-Hochberg correction (q=0.003958).
* When Mercury conjoined Moon (57 events since 2001), Nifty Bank averaged +3.43% over the next 5 trading days (base rate +0.30%). Win rate 68.4%. That is +3.13 pp above the unconditional baseline. Statistically significant at p=0.0008795 and after Benjamini-Hochberg correction (q=0.005311).
* When Mercury conjoined Moon (57 events since 2001), Nifty Midcap 100 averaged -0.36% over the next 5 trading days (base rate +0.27%). Win rate 36.8%. That is -0.63 pp below the unconditional baseline. Not statistically significant (p=0.1965, q=0.3556 after Benjamini-Hochberg correction).
* When Mercury conjoined Moon (57 events since 2001), Nifty Midcap 150 averaged +0.79% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.52 pp above the unconditional baseline. Not statistically significant (p=0.3254, q=0.5035 after Benjamini-Hochberg correction).
* When Mercury conjoined Moon (57 events since 2001), BSE Sensex averaged +0.46% over the next 5 trading days (base rate +0.25%). Win rate 61.4%. That is +0.21 pp above the unconditional baseline. Not statistically significant (p=0.7107, q=0.8312 after Benjamini-Hochberg correction).

* When Mercury conjoined Rahu (42 events since 2000), Nifty 50 averaged +1.76% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +1.55 pp above the unconditional baseline. Nominally significant at p=0.03964, but it does not survive Benjamini-Hochberg correction (q=0.1078).
* When Mercury conjoined Rahu (42 events since 2000), Nifty Bank averaged +1.78% over the next 5 trading days (base rate +0.30%). Win rate 69.0%. That is +1.48 pp above the unconditional baseline. Not statistically significant (p=0.1234, q=0.2544 after Benjamini-Hochberg correction).
* When Mercury conjoined Rahu (42 events since 2000), Nifty Midcap 100 averaged -0.04% over the next 5 trading days (base rate +0.27%). Win rate 40.5%. That is -0.31 pp below the unconditional baseline. Not statistically significant (p=0.4363, q=0.6173 after Benjamini-Hochberg correction).
* When Mercury conjoined Rahu (42 events since 2000), Nifty Midcap 150 averaged +0.21% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is -0.05 pp below the unconditional baseline. Not statistically significant (p=0.9111, q=0.9595 after Benjamini-Hochberg correction).
* When Mercury conjoined Rahu (42 events since 2000), BSE Sensex averaged -0.06% over the next 5 trading days (base rate +0.25%). Win rate 59.5%. That is -0.31 pp below the unconditional baseline. Not statistically significant (p=0.5251, q=0.6971 after Benjamini-Hochberg correction).

* When Mercury conjoined Saturn (32 events since 2000), Nifty 50 averaged +3.05% over the next 5 trading days (base rate +0.22%). Win rate 65.6%. That is +2.83 pp above the unconditional baseline. Statistically significant at p=0.0008392 and after Benjamini-Hochberg correction (q=0.005134).
* When Mercury conjoined Saturn (32 events since 2000), Nifty Bank averaged +3.62% over the next 5 trading days (base rate +0.30%). Win rate 71.9%. That is +3.32 pp above the unconditional baseline. Statistically significant at p=0.0009029 and after Benjamini-Hochberg correction (q=0.0054).
* When Mercury conjoined Saturn (32 events since 2000), Nifty Midcap 100 averaged +0.80% over the next 5 trading days (base rate +0.27%). Win rate 46.9%. That is +0.54 pp above the unconditional baseline. Not statistically significant (p=0.4053, q=0.5875 after Benjamini-Hochberg correction).
* When Mercury conjoined Saturn (32 events since 2000), Nifty Midcap 150 averaged +1.02% over the next 5 trading days (base rate +0.26%). Win rate 68.8%. That is +0.76 pp above the unconditional baseline. Nominally significant at p=0.02536, but it does not survive Benjamini-Hochberg correction (q=0.07841).
* When Mercury conjoined Saturn (32 events since 2000), BSE Sensex averaged +0.65% over the next 5 trading days (base rate +0.25%). Win rate 62.5%. That is +0.40 pp above the unconditional baseline. Not statistically significant (p=0.3712, q=0.5533 after Benjamini-Hochberg correction).

* When Mercury conjoined Sun (168 events since 2000), Nifty 50 averaged +3.16% over the next 5 trading days (base rate +0.22%). Win rate 72.0%. That is +2.94 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=2.211e-11).
* When Mercury conjoined Sun (168 events since 2000), Nifty Bank averaged +3.80% over the next 5 trading days (base rate +0.30%). Win rate 69.6%. That is +3.50 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.25e-11).
* When Mercury conjoined Sun (168 events since 2000), Nifty Midcap 100 averaged +0.32% over the next 5 trading days (base rate +0.27%). Win rate 41.1%. That is +0.06 pp above the unconditional baseline. Not statistically significant (p=0.8054, q=0.891 after Benjamini-Hochberg correction).
* When Mercury conjoined Sun (168 events since 2000), Nifty Midcap 150 averaged +0.71% over the next 5 trading days (base rate +0.26%). Win rate 69.0%. That is +0.45 pp above the unconditional baseline. Nominally significant at p=0.02543, but it does not survive Benjamini-Hochberg correction (q=0.07842).
* When Mercury conjoined Sun (168 events since 2000), BSE Sensex averaged +0.40% over the next 5 trading days (base rate +0.25%). Win rate 55.4%. That is +0.15 pp above the unconditional baseline. Not statistically significant (p=0.5011, q=0.6771 after Benjamini-Hochberg correction).

* When Mercury conjoined Venus (61 events since 2000), Nifty 50 averaged +2.93% over the next 5 trading days (base rate +0.22%). Win rate 72.1%. That is +2.72 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0008076).
* When Mercury conjoined Venus (61 events since 2000), Nifty Bank averaged +3.18% over the next 5 trading days (base rate +0.30%). Win rate 70.5%. That is +2.88 pp above the unconditional baseline. Statistically significant at p=0.0005386 and after Benjamini-Hochberg correction (q=0.003631).
* When Mercury conjoined Venus (61 events since 2000), Nifty Midcap 100 averaged +0.27% over the next 5 trading days (base rate +0.27%). Win rate 42.6%. Not statistically significant (p=0.9952, q=0.9976 after Benjamini-Hochberg correction).
* When Mercury conjoined Venus (61 events since 2000), Nifty Midcap 150 averaged +0.83% over the next 5 trading days (base rate +0.26%). Win rate 70.5%. That is +0.56 pp above the unconditional baseline. Not statistically significant (p=0.1395, q=0.2786 after Benjamini-Hochberg correction).
* When Mercury conjoined Venus (61 events since 2000), BSE Sensex averaged +0.36% over the next 5 trading days (base rate +0.25%). Win rate 60.7%. That is +0.11 pp above the unconditional baseline. Not statistically significant (p=0.7964, q=0.8854 after Benjamini-Hochberg correction).

* When Moon conjoined Rahu (54 events since 2000), Nifty 50 averaged +3.09% over the next 5 trading days (base rate +0.22%). Win rate 68.5%. That is +2.87 pp above the unconditional baseline. Statistically significant at p=0.0002346 and after Benjamini-Hochberg correction (q=0.001864).
* When Moon conjoined Rahu (54 events since 2000), Nifty Bank averaged +3.37% over the next 5 trading days (base rate +0.30%). Win rate 68.5%. That is +3.07 pp above the unconditional baseline. Statistically significant at p=0.001348 and after Benjamini-Hochberg correction (q=0.007413).
* When Moon conjoined Rahu (54 events since 2000), Nifty Midcap 100 averaged -0.15% over the next 5 trading days (base rate +0.27%). Win rate 40.7%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.221, q=0.3854 after Benjamini-Hochberg correction).
* When Moon conjoined Rahu (54 events since 2000), Nifty Midcap 150 averaged +0.75% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.49 pp above the unconditional baseline. Not statistically significant (p=0.2911, q=0.466 after Benjamini-Hochberg correction).
* When Moon conjoined Rahu (54 events since 2000), BSE Sensex averaged +0.57% over the next 5 trading days (base rate +0.25%). Win rate 59.3%. That is +0.32 pp above the unconditional baseline. Not statistically significant (p=0.4728, q=0.6502 after Benjamini-Hochberg correction).

* When Moon conjoined Saturn (55 events since 2000), Nifty 50 averaged +2.86% over the next 5 trading days (base rate +0.22%). Win rate 63.6%. That is +2.64 pp above the unconditional baseline. Statistically significant at p=0.000169 and after Benjamini-Hochberg correction (q=0.001484).
* When Moon conjoined Saturn (55 events since 2000), Nifty Bank averaged +3.46% over the next 5 trading days (base rate +0.30%). Win rate 63.6%. That is +3.16 pp above the unconditional baseline. Statistically significant at p=0.0002047 and after Benjamini-Hochberg correction (q=0.0017).
* When Moon conjoined Saturn (55 events since 2000), Nifty Midcap 100 averaged -0.41% over the next 5 trading days (base rate +0.27%). Win rate 29.1%. That is -0.67 pp below the unconditional baseline. Not statistically significant (p=0.114, q=0.239 after Benjamini-Hochberg correction).
* When Moon conjoined Saturn (55 events since 2000), Nifty Midcap 150 averaged +0.34% over the next 5 trading days (base rate +0.26%). Win rate 60.0%. That is +0.08 pp above the unconditional baseline. Not statistically significant (p=0.7964, q=0.8854 after Benjamini-Hochberg correction).
* When Moon conjoined Saturn (55 events since 2000), BSE Sensex averaged +0.25% over the next 5 trading days (base rate +0.25%). Win rate 54.5%. Not statistically significant (p=0.9948, q=0.9976 after Benjamini-Hochberg correction).

* When Moon conjoined Sun (60 events since 2000), Nifty 50 averaged +3.24% over the next 5 trading days (base rate +0.22%). Win rate 73.3%. That is +3.02 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000191).
* When Moon conjoined Sun (60 events since 2000), Nifty Bank averaged +3.84% over the next 5 trading days (base rate +0.30%). Win rate 76.7%. That is +3.54 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0001267).
* When Moon conjoined Sun (60 events since 2000), Nifty Midcap 100 averaged -0.03% over the next 5 trading days (base rate +0.27%). Win rate 43.3%. That is -0.29 pp below the unconditional baseline. Not statistically significant (p=0.4967, q=0.6739 after Benjamini-Hochberg correction).
* When Moon conjoined Sun (60 events since 2000), Nifty Midcap 150 averaged +1.02% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +0.76 pp above the unconditional baseline. Nominally significant at p=0.04266, but it does not survive Benjamini-Hochberg correction (q=0.1137).
* When Moon conjoined Sun (60 events since 2000), BSE Sensex averaged +0.56% over the next 5 trading days (base rate +0.25%). Win rate 60.0%. That is +0.31 pp above the unconditional baseline. Not statistically significant (p=0.4506, q=0.6302 after Benjamini-Hochberg correction).

* When Moon conjoined Venus (44 events since 2000), Nifty 50 averaged +1.76% over the next 5 trading days (base rate +0.22%). Win rate 61.4%. That is +1.54 pp above the unconditional baseline. Nominally significant at p=0.03053, but it does not survive Benjamini-Hochberg correction (q=0.08979).
* When Moon conjoined Venus (44 events since 2000), Nifty Bank averaged +1.91% over the next 5 trading days (base rate +0.30%). Win rate 56.8%. That is +1.61 pp above the unconditional baseline. Not statistically significant (p=0.05582, q=0.14 after Benjamini-Hochberg correction).
* When Moon conjoined Venus (44 events since 2000), Nifty Midcap 100 averaged -0.27% over the next 5 trading days (base rate +0.27%). Win rate 36.4%. That is -0.54 pp below the unconditional baseline. Not statistically significant (p=0.3173, q=0.4943 after Benjamini-Hochberg correction).
* When Moon conjoined Venus (44 events since 2000), Nifty Midcap 150 averaged +0.04% over the next 5 trading days (base rate +0.26%). Win rate 61.4%. That is -0.23 pp below the unconditional baseline. Not statistically significant (p=0.494, q=0.6724 after Benjamini-Hochberg correction).
* When Moon conjoined Venus (44 events since 2000), BSE Sensex averaged -0.14% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.39 pp below the unconditional baseline. Not statistically significant (p=0.322, q=0.4997 after Benjamini-Hochberg correction).

* When Rahu conjoined Saturn (3 events since 2002), Nifty 50 averaged +4.88% over the next 5 trading days (base rate +0.22%). Win rate 100.0%. That is +4.66 pp above the unconditional baseline. Not statistically significant (p=0.2208, q=0.3854 after Benjamini-Hochberg correction).
* When Rahu conjoined Saturn (3 events since 2002), Nifty Bank averaged +6.01% over the next 5 trading days (base rate +0.30%). Win rate 100.0%. That is +5.71 pp above the unconditional baseline. Not statistically significant (p=0.1737, q=0.3269 after Benjamini-Hochberg correction).
* When Rahu conjoined Saturn (3 events since 2002), Nifty Midcap 100 averaged +2.75% over the next 5 trading days (base rate +0.27%). Win rate 66.7%. That is +2.49 pp above the unconditional baseline. Not statistically significant (p=0.3334, q=0.512 after Benjamini-Hochberg correction).
* When Rahu conjoined Saturn (3 events since 2002), Nifty Midcap 150 averaged +2.19% over the next 5 trading days (base rate +0.26%). Win rate 100.0%. That is +1.93 pp above the unconditional baseline. Not statistically significant (p=0.2122, q=0.3749 after Benjamini-Hochberg correction).
* When Rahu conjoined Saturn (3 events since 2002), BSE Sensex averaged +2.08% over the next 5 trading days (base rate +0.25%). Win rate 100.0%. That is +1.83 pp above the unconditional baseline. Not statistically significant (p=0.2759, q=0.453 after Benjamini-Hochberg correction).

* When Rahu conjoined Sun (28 events since 2000), Nifty 50 averaged +2.88% over the next 5 trading days (base rate +0.22%). Win rate 71.4%. That is +2.66 pp above the unconditional baseline. Statistically significant at p=0.008166 and after Benjamini-Hochberg correction (q=0.03186).
* When Rahu conjoined Sun (28 events since 2000), Nifty Bank averaged +2.76% over the next 5 trading days (base rate +0.30%). Win rate 60.7%. That is +2.46 pp above the unconditional baseline. Nominally significant at p=0.04552, but it does not survive Benjamini-Hochberg correction (q=0.1196).
* When Rahu conjoined Sun (28 events since 2000), Nifty Midcap 100 averaged +0.44% over the next 5 trading days (base rate +0.27%). Win rate 42.9%. That is +0.18 pp above the unconditional baseline. Not statistically significant (p=0.7556, q=0.8594 after Benjamini-Hochberg correction).
* When Rahu conjoined Sun (28 events since 2000), Nifty Midcap 150 averaged +0.66% over the next 5 trading days (base rate +0.26%). Win rate 71.4%. That is +0.39 pp above the unconditional baseline. Not statistically significant (p=0.4065, q=0.5885 after Benjamini-Hochberg correction).
* When Rahu conjoined Sun (28 events since 2000), BSE Sensex averaged -0.31% over the next 5 trading days (base rate +0.25%). Win rate 53.6%. That is -0.56 pp below the unconditional baseline. Not statistically significant (p=0.3967, q=0.5802 after Benjamini-Hochberg correction).

* When Rahu conjoined Venus (30 events since 2000), Nifty 50 averaged +1.57% over the next 5 trading days (base rate +0.22%). Win rate 50.0%. That is +1.35 pp above the unconditional baseline. Not statistically significant (p=0.1939, q=0.3523 after Benjamini-Hochberg correction).
* When Rahu conjoined Venus (30 events since 2000), Nifty Bank averaged +1.92% over the next 5 trading days (base rate +0.30%). Win rate 53.3%. That is +1.62 pp above the unconditional baseline. Not statistically significant (p=0.1861, q=0.3428 after Benjamini-Hochberg correction).
* When Rahu conjoined Venus (30 events since 2000), Nifty Midcap 100 averaged -1.23% over the next 5 trading days (base rate +0.27%). Win rate 26.7%. That is -1.49 pp below the unconditional baseline. Nominally significant at p=0.02972, but it does not survive Benjamini-Hochberg correction (q=0.08817).
* When Rahu conjoined Venus (30 events since 2000), Nifty Midcap 150 averaged -0.70% over the next 5 trading days (base rate +0.26%). Win rate 50.0%. That is -0.97 pp below the unconditional baseline. Not statistically significant (p=0.06261, q=0.1533 after Benjamini-Hochberg correction).
* When Rahu conjoined Venus (30 events since 2000), BSE Sensex averaged -1.48% over the next 5 trading days (base rate +0.25%). Win rate 26.7%. That is -1.73 pp below the unconditional baseline. Statistically significant at p=0.001279 and after Benjamini-Hochberg correction (q=0.007175).

* When Saturn conjoined Sun (26 events since 2000), Nifty 50 averaged +2.75% over the next 5 trading days (base rate +0.22%). Win rate 57.7%. That is +2.53 pp above the unconditional baseline. Nominally significant at p=0.01664, but it does not survive Benjamini-Hochberg correction (q=0.05708).
* When Saturn conjoined Sun (26 events since 2000), Nifty Bank averaged +3.33% over the next 5 trading days (base rate +0.30%). Win rate 57.7%. That is +3.03 pp above the unconditional baseline. Nominally significant at p=0.0166, but it does not survive Benjamini-Hochberg correction (q=0.05701).
* When Saturn conjoined Sun (26 events since 2000), Nifty Midcap 100 averaged -0.18% over the next 5 trading days (base rate +0.27%). Win rate 26.9%. That is -0.44 pp below the unconditional baseline. Not statistically significant (p=0.1832, q=0.339 after Benjamini-Hochberg correction).
* When Saturn conjoined Sun (26 events since 2000), Nifty Midcap 150 averaged +0.53% over the next 5 trading days (base rate +0.26%). Win rate 61.5%. That is +0.26 pp above the unconditional baseline. Not statistically significant (p=0.5672, q=0.7282 after Benjamini-Hochberg correction).
* When Saturn conjoined Sun (26 events since 2000), BSE Sensex averaged +0.24% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. Not statistically significant (p=0.9905, q=0.9964 after Benjamini-Hochberg correction).

* When Saturn conjoined Venus (30 events since 2000), Nifty 50 averaged +2.73% over the next 5 trading days (base rate +0.22%). Win rate 63.3%. That is +2.51 pp above the unconditional baseline. Nominally significant at p=0.01688, but it does not survive Benjamini-Hochberg correction (q=0.05765).
* When Saturn conjoined Venus (30 events since 2000), Nifty Bank averaged +2.92% over the next 5 trading days (base rate +0.30%). Win rate 66.7%. That is +2.62 pp above the unconditional baseline. Nominally significant at p=0.03937, but it does not survive Benjamini-Hochberg correction (q=0.1074).
* When Saturn conjoined Venus (30 events since 2000), Nifty Midcap 100 averaged +0.02% over the next 5 trading days (base rate +0.27%). Win rate 43.3%. That is -0.24 pp below the unconditional baseline. Not statistically significant (p=0.42, q=0.6018 after Benjamini-Hochberg correction).
* When Saturn conjoined Venus (30 events since 2000), Nifty Midcap 150 averaged -0.02% over the next 5 trading days (base rate +0.26%). Win rate 60.0%. That is -0.28 pp below the unconditional baseline. Not statistically significant (p=0.6515, q=0.7932 after Benjamini-Hochberg correction).
* When Saturn conjoined Venus (30 events since 2000), BSE Sensex averaged -0.31% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is -0.56 pp below the unconditional baseline. Not statistically significant (p=0.3552, q=0.5353 after Benjamini-Hochberg correction).

* When Sun conjoined Venus (34 events since 2000), Nifty 50 averaged +3.50% over the next 5 trading days (base rate +0.22%). Win rate 76.5%. That is +3.28 pp above the unconditional baseline. Statistically significant at p=0.0003889 and after Benjamini-Hochberg correction (q=0.002821).
* When Sun conjoined Venus (34 events since 2000), Nifty Bank averaged +3.38% over the next 5 trading days (base rate +0.30%). Win rate 61.8%. That is +3.08 pp above the unconditional baseline. Statistically significant at p=0.004266 and after Benjamini-Hochberg correction (q=0.01865).
* When Sun conjoined Venus (34 events since 2000), Nifty Midcap 100 averaged +1.05% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.78 pp above the unconditional baseline. Not statistically significant (p=0.1437, q=0.2846 after Benjamini-Hochberg correction).
* When Sun conjoined Venus (34 events since 2000), Nifty Midcap 150 averaged +1.15% over the next 5 trading days (base rate +0.26%). Win rate 76.5%. That is +0.88 pp above the unconditional baseline. Not statistically significant (p=0.06733, q=0.1609 after Benjamini-Hochberg correction).
* When Sun conjoined Venus (34 events since 2000), BSE Sensex averaged +0.83% over the next 5 trading days (base rate +0.25%). Win rate 67.6%. That is +0.58 pp above the unconditional baseline. Not statistically significant (p=0.2387, q=0.4066 after Benjamini-Hochberg correction).

**All windows — Conjunctions (Yuti)**

| Event | Index | Window | N | Mean ret | Base rate | Excess | Win % | p-value | q (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jupiter-Ketu Conjunction | Nifty 50 | 1 | 3 | 0.5958 | 0.04492 | 0.5509 | 100 | 0.2017 | 0.363 |
| Jupiter-Ketu Conjunction | Nifty 50 | 3 | 3 | 3.381 | 0.1333 | 3.248 | 100 | 0.1051 | 0.2249 |
| Jupiter-Ketu Conjunction | Nifty 50 | 5 | 3 | 5.222 | 0.2178 | 5.004 | 100 | 0.157 | 0.3048 |
| Jupiter-Ketu Conjunction | Nifty 50 | 10 | 3 | 5.968 | 0.4212 | 5.547 | 100 | 0.2466 | 0.4162 |
| Jupiter-Ketu Conjunction | Nifty 50 | 20 | 3 | 7.7 | 0.8264 | 6.874 | 33.33 | 0.5335 | 0.7018 |
| Jupiter-Ketu Conjunction | Nifty Bank | 1 | 3 | 0.9123 | 0.06023 | 0.8521 | 66.67 | 0.3721 | 0.5538 |
| Jupiter-Ketu Conjunction | Nifty Bank | 3 | 3 | 4.608 | 0.1819 | 4.426 | 100 | 0.07808 | 0.1795 |
| Jupiter-Ketu Conjunction | Nifty Bank | 5 | 3 | 6.349 | 0.3 | 6.049 | 100 | 0.1251 | 0.2567 |
| Jupiter-Ketu Conjunction | Nifty Bank | 10 | 3 | 7.417 | 0.5834 | 6.834 | 66.67 | 0.2842 | 0.4596 |
| Jupiter-Ketu Conjunction | Nifty Bank | 20 | 3 | 7.052 | 1.172 | 5.88 | 66.67 | 0.5372 | 0.7051 |
| Jupiter-Ketu Conjunction | Nifty Midcap 100 | 1 | 3 | 0.1287 | 0.05397 | 0.07478 | 100 | 0.2378 | 0.4054 |
| Jupiter-Ketu Conjunction | Nifty Midcap 100 | 3 | 3 | 0.4736 | 0.1609 | 0.3127 | 66.67 | 0.5453 | 0.7133 |
| Jupiter-Ketu Conjunction | Nifty Midcap 100 | 5 | 3 | 0.808 | 0.266 | 0.542 | 66.67 | 0.5334 | 0.7018 |
| Jupiter-Ketu Conjunction | Nifty Midcap 100 | 10 | 3 | 2.135 | 0.532 | 1.603 | 100 | 0.3095 | 0.4871 |
| Jupiter-Ketu Conjunction | Nifty Midcap 100 | 20 | 3 | -0.209 | 1.065 | -1.274 | 66.67 | 0.7742 | 0.8721 |
| Jupiter-Ketu Conjunction | Nifty Midcap 150 | 1 | 3 | 0.8004 | 0.05323 | 0.7472 | 100 | 0.2524 | 0.424 |
| Jupiter-Ketu Conjunction | Nifty Midcap 150 | 3 | 3 | 1.724 | 0.1594 | 1.564 | 100 | 0.13 | 0.2646 |
| Jupiter-Ketu Conjunction | Nifty Midcap 150 | 5 | 3 | 2.607 | 0.2642 | 2.342 | 100 | 0.04725 | 0.1231 |
| Jupiter-Ketu Conjunction | Nifty Midcap 150 | 10 | 3 | 3.696 | 0.5204 | 3.175 | 100 | 0.09192 | 0.2037 |
| Jupiter-Ketu Conjunction | Nifty Midcap 150 | 20 | 3 | 0.8541 | 1.047 | -0.1933 | 33.33 | 0.9386 | 0.9749 |
| Jupiter-Ketu Conjunction | BSE Sensex | 1 | 3 | 0.074 | 0.05036 | 0.02364 | 66.67 | 0.9335 | 0.9724 |
| Jupiter-Ketu Conjunction | BSE Sensex | 3 | 3 | 0.7598 | 0.1513 | 0.6085 | 66.67 | 0.7201 | 0.8373 |
| Jupiter-Ketu Conjunction | BSE Sensex | 5 | 3 | 1.511 | 0.2506 | 1.261 | 66.67 | 0.4634 | 0.6414 |
| Jupiter-Ketu Conjunction | BSE Sensex | 10 | 3 | 2.233 | 0.4957 | 1.737 | 100 | 0.05933 | 0.1471 |
| Jupiter-Ketu Conjunction | BSE Sensex | 20 | 3 | 1.947 | 1.002 | 0.9451 | 33.33 | 0.8024 | 0.8899 |
| Jupiter-Mars Conjunction | Nifty 50 | 1 | 12 | -0.722 | 0.04492 | -0.7669 | 66.67 | 0.5212 | 0.6939 |
| Jupiter-Mars Conjunction | Nifty 50 | 3 | 12 | 1.058 | 0.1333 | 0.9249 | 58.33 | 0.4276 | 0.609 |
| Jupiter-Mars Conjunction | Nifty 50 | 5 | 12 | 2.878 | 0.2178 | 2.661 | 50 | 0.1095 | 0.2321 |
| Jupiter-Mars Conjunction | Nifty 50 | 10 | 12 | 3.11 | 0.4212 | 2.689 | 58.33 | 0.2567 | 0.4297 |
| Jupiter-Mars Conjunction | Nifty 50 | 20 | 12 | 7.494 | 0.8264 | 6.668 | 58.33 | 0.1415 | 0.2816 |
| Jupiter-Mars Conjunction | Nifty Bank | 1 | 12 | -0.8735 | 0.06023 | -0.9337 | 58.33 | 0.5562 | 0.7222 |
| Jupiter-Mars Conjunction | Nifty Bank | 3 | 12 | 0.596 | 0.1819 | 0.414 | 50 | 0.8058 | 0.8911 |
| Jupiter-Mars Conjunction | Nifty Bank | 5 | 12 | 2.498 | 0.3 | 2.198 | 50 | 0.284 | 0.4596 |
| Jupiter-Mars Conjunction | Nifty Bank | 10 | 12 | 2.48 | 0.5834 | 1.897 | 50 | 0.5633 | 0.7258 |
| Jupiter-Mars Conjunction | Nifty Bank | 20 | 12 | 4.389 | 1.172 | 3.217 | 50 | 0.456 | 0.6341 |
| Jupiter-Mars Conjunction | Nifty Midcap 100 | 1 | 12 | -0.5116 | 0.05397 | -0.5656 | 66.67 | 0.5277 | 0.6995 |
| Jupiter-Mars Conjunction | Nifty Midcap 100 | 3 | 12 | 0.4007 | 0.1609 | 0.2398 | 41.67 | 0.6801 | 0.8108 |
| Jupiter-Mars Conjunction | Nifty Midcap 100 | 5 | 12 | 0.8169 | 0.266 | 0.5508 | 58.33 | 0.2457 | 0.4153 |
| Jupiter-Mars Conjunction | Nifty Midcap 100 | 10 | 12 | 2.599 | 0.532 | 2.067 | 75 | 0.1292 | 0.2636 |
| Jupiter-Mars Conjunction | Nifty Midcap 100 | 20 | 12 | 3.435 | 1.065 | 2.37 | 75 | 0.1115 | 0.2358 |
| Jupiter-Mars Conjunction | Nifty Midcap 150 | 1 | 12 | -0.9706 | 0.05323 | -1.024 | 58.33 | 0.404 | 0.586 |
| Jupiter-Mars Conjunction | Nifty Midcap 150 | 3 | 12 | -0.739 | 0.1594 | -0.8985 | 50 | 0.1793 | 0.334 |
| Jupiter-Mars Conjunction | Nifty Midcap 150 | 5 | 12 | 0.1188 | 0.2642 | -0.1455 | 50 | 0.8002 | 0.8881 |
| Jupiter-Mars Conjunction | Nifty Midcap 150 | 10 | 12 | 0.4111 | 0.5204 | -0.1093 | 58.33 | 0.935 | 0.9731 |
| Jupiter-Mars Conjunction | Nifty Midcap 150 | 20 | 12 | 0.07476 | 1.047 | -0.9727 | 58.33 | 0.5759 | 0.7342 |
| Jupiter-Mars Conjunction | BSE Sensex | 1 | 12 | -0.8733 | 0.05036 | -0.9237 | 41.67 | 0.5041 | 0.6795 |
| Jupiter-Mars Conjunction | BSE Sensex | 3 | 12 | 0.6164 | 0.1513 | 0.4651 | 58.33 | 0.7382 | 0.8485 |
| Jupiter-Mars Conjunction | BSE Sensex | 5 | 12 | 0.8329 | 0.2506 | 0.5824 | 50 | 0.4802 | 0.6584 |
| Jupiter-Mars Conjunction | BSE Sensex | 10 | 12 | -1.559 | 0.4957 | -2.054 | 41.67 | 0.1237 | 0.2549 |
| Jupiter-Mars Conjunction | BSE Sensex | 20 | 12 | -2.396 | 1.002 | -3.397 | 25 | 0.05559 | 0.1396 |
| Jupiter-Mercury Conjunction | Nifty 50 | 1 | 39 | 0.5212 | 0.04492 | 0.4763 | 66.67 | 0.02086 | 0.06803 |
| Jupiter-Mercury Conjunction | Nifty 50 | 3 | 39 | 1.91 | 0.1333 | 1.777 | 69.23 | 0.001137 | 0.006534 |
| Jupiter-Mercury Conjunction | Nifty 50 | 5 | 39 | 2.787 | 0.2178 | 2.569 | 56.41 | 0.002394 | 0.01157 |
| Jupiter-Mercury Conjunction | Nifty 50 | 10 | 39 | 3.961 | 0.4212 | 3.539 | 66.67 | 0.001308 | 0.00729 |
| Jupiter-Mercury Conjunction | Nifty 50 | 20 | 39 | 7.563 | 0.8264 | 6.736 | 66.67 | 0.002105 | 0.01041 |
| Jupiter-Mercury Conjunction | Nifty Bank | 1 | 39 | 0.8867 | 0.06023 | 0.8265 | 61.54 | 0.004529 | 0.01957 |
| Jupiter-Mercury Conjunction | Nifty Bank | 3 | 39 | 2.303 | 0.1819 | 2.121 | 64.1 | 0.002153 | 0.01056 |
| Jupiter-Mercury Conjunction | Nifty Bank | 5 | 39 | 2.917 | 0.3 | 2.617 | 58.97 | 0.008422 | 0.0328 |
| Jupiter-Mercury Conjunction | Nifty Bank | 10 | 39 | 4.588 | 0.5834 | 4.005 | 66.67 | 0.006217 | 0.0254 |
| Jupiter-Mercury Conjunction | Nifty Bank | 20 | 39 | 6.523 | 1.172 | 5.351 | 69.23 | 0.009086 | 0.03484 |
| Jupiter-Mercury Conjunction | Nifty Midcap 100 | 1 | 39 | 0.2986 | 0.05397 | 0.2446 | 71.79 | 0.4082 | 0.5901 |
| Jupiter-Mercury Conjunction | Nifty Midcap 100 | 3 | 39 | 0.6365 | 0.1609 | 0.4757 | 43.59 | 0.3091 | 0.4871 |
| Jupiter-Mercury Conjunction | Nifty Midcap 100 | 5 | 39 | 0.4081 | 0.266 | 0.1421 | 43.59 | 0.7429 | 0.851 |
| Jupiter-Mercury Conjunction | Nifty Midcap 100 | 10 | 39 | 1.585 | 0.532 | 1.053 | 71.79 | 0.05743 | 0.1432 |
| Jupiter-Mercury Conjunction | Nifty Midcap 100 | 20 | 39 | 1.805 | 1.065 | 0.7402 | 66.67 | 0.4745 | 0.652 |
| Jupiter-Mercury Conjunction | Nifty Midcap 150 | 1 | 39 | 0.4989 | 0.05323 | 0.4457 | 64.1 | 0.0635 | 0.1549 |
| Jupiter-Mercury Conjunction | Nifty Midcap 150 | 3 | 39 | 0.5687 | 0.1594 | 0.4092 | 64.1 | 0.2426 | 0.411 |
| Jupiter-Mercury Conjunction | Nifty Midcap 150 | 5 | 39 | 0.5206 | 0.2642 | 0.2564 | 53.85 | 0.5071 | 0.6827 |
| Jupiter-Mercury Conjunction | Nifty Midcap 150 | 10 | 39 | 1.731 | 0.5204 | 1.211 | 61.54 | 0.05259 | 0.1331 |
| Jupiter-Mercury Conjunction | Nifty Midcap 150 | 20 | 39 | 1.571 | 1.047 | 0.5235 | 69.23 | 0.55 | 0.7161 |
| Jupiter-Mercury Conjunction | BSE Sensex | 1 | 39 | 0.2833 | 0.05036 | 0.233 | 56.41 | 0.3345 | 0.5134 |
| Jupiter-Mercury Conjunction | BSE Sensex | 3 | 39 | 0.3973 | 0.1513 | 0.246 | 61.54 | 0.5727 | 0.7323 |
| Jupiter-Mercury Conjunction | BSE Sensex | 5 | 39 | -0.06 | 0.2506 | -0.3106 | 43.59 | 0.4957 | 0.6734 |
| Jupiter-Mercury Conjunction | BSE Sensex | 10 | 39 | 0.1159 | 0.4957 | -0.3798 | 53.85 | 0.5892 | 0.7459 |
| Jupiter-Mercury Conjunction | BSE Sensex | 20 | 39 | 0.597 | 1.002 | -0.4046 | 51.28 | 0.662 | 0.7996 |
| Jupiter-Moon Conjunction | Nifty 50 | 1 | 55 | 0.6544 | 0.04492 | 0.6095 | 80 | 3.098e-06 | 6.314e-05 |
| Jupiter-Moon Conjunction | Nifty 50 | 3 | 55 | 1.765 | 0.1333 | 1.632 | 65.45 | 0.0007193 | 0.004526 |
| Jupiter-Moon Conjunction | Nifty 50 | 5 | 55 | 3.297 | 0.2178 | 3.08 | 63.64 | 3.224e-05 | 0.0004043 |
| Jupiter-Moon Conjunction | Nifty 50 | 10 | 55 | 4.07 | 0.4212 | 3.649 | 70.91 | 0.0003765 | 0.002747 |
| Jupiter-Moon Conjunction | Nifty 50 | 20 | 55 | 9.271 | 0.8264 | 8.444 | 78.18 | 6.074e-06 | 0.000105 |
| Jupiter-Moon Conjunction | Nifty Bank | 1 | 55 | 1.082 | 0.06023 | 1.022 | 74.55 | 2.403e-06 | 5.088e-05 |
| Jupiter-Moon Conjunction | Nifty Bank | 3 | 55 | 2.08 | 0.1819 | 1.898 | 69.09 | 0.004195 | 0.01844 |
| Jupiter-Moon Conjunction | Nifty Bank | 5 | 55 | 3.643 | 0.3 | 3.343 | 67.27 | 0.000216 | 0.001759 |
| Jupiter-Moon Conjunction | Nifty Bank | 10 | 55 | 5.274 | 0.5834 | 4.691 | 67.27 | 0.0002111 | 0.00174 |
| Jupiter-Moon Conjunction | Nifty Bank | 20 | 55 | 8.153 | 1.172 | 6.98 | 74.55 | 3.162e-05 | 0.0003979 |
| Jupiter-Moon Conjunction | Nifty Midcap 100 | 1 | 55 | 0.2793 | 0.05397 | 0.2254 | 76.36 | 0.13 | 0.2646 |
| Jupiter-Moon Conjunction | Nifty Midcap 100 | 3 | 55 | 0.07336 | 0.1609 | -0.0875 | 34.55 | 0.7438 | 0.851 |
| Jupiter-Moon Conjunction | Nifty Midcap 100 | 5 | 55 | 0.1157 | 0.266 | -0.1503 | 36.36 | 0.6698 | 0.8046 |
| Jupiter-Moon Conjunction | Nifty Midcap 100 | 10 | 55 | 1.815 | 0.532 | 1.283 | 70.91 | 0.04125 | 0.1109 |
| Jupiter-Moon Conjunction | Nifty Midcap 100 | 20 | 55 | 2.916 | 1.065 | 1.851 | 76.36 | 0.02128 | 0.06916 |
| Jupiter-Moon Conjunction | Nifty Midcap 150 | 1 | 55 | 0.6221 | 0.05323 | 0.5689 | 70.91 | 0.0001391 | 0.001269 |
| Jupiter-Moon Conjunction | Nifty Midcap 150 | 3 | 55 | -0.009015 | 0.1594 | -0.1685 | 60 | 0.5604 | 0.7248 |
| Jupiter-Moon Conjunction | Nifty Midcap 150 | 5 | 55 | 0.4662 | 0.2642 | 0.2019 | 61.82 | 0.5401 | 0.7079 |
| Jupiter-Moon Conjunction | Nifty Midcap 150 | 10 | 55 | 1.332 | 0.5204 | 0.8113 | 67.27 | 0.2071 | 0.3692 |
| Jupiter-Moon Conjunction | Nifty Midcap 150 | 20 | 55 | 2.151 | 1.047 | 1.103 | 78.18 | 0.09518 | 0.2095 |
| Jupiter-Moon Conjunction | BSE Sensex | 1 | 55 | 0.2776 | 0.05036 | 0.2272 | 58.18 | 0.1082 | 0.2298 |
| Jupiter-Moon Conjunction | BSE Sensex | 3 | 55 | 0.07639 | 0.1513 | -0.07492 | 49.09 | 0.8053 | 0.891 |
| Jupiter-Moon Conjunction | BSE Sensex | 5 | 55 | 0.1722 | 0.2506 | -0.07834 | 50.91 | 0.8442 | 0.9163 |
| Jupiter-Moon Conjunction | BSE Sensex | 10 | 55 | 0.3042 | 0.4957 | -0.1915 | 58.18 | 0.7476 | 0.8543 |
| Jupiter-Moon Conjunction | BSE Sensex | 20 | 55 | 1.242 | 1.002 | 0.2402 | 65.45 | 0.7319 | 0.845 |
| Jupiter-Rahu Conjunction | Nifty 50 | 1 | 4 | 0.1574 | 0.04492 | 0.1125 | 75 | 0.8268 | 0.9052 |
| Jupiter-Rahu Conjunction | Nifty 50 | 3 | 4 | 1.194 | 0.1333 | 1.061 | 50 | 0.5974 | 0.7511 |
| Jupiter-Rahu Conjunction | Nifty 50 | 5 | 4 | 2.002 | 0.2178 | 1.784 | 50 | 0.607 | 0.7565 |
| Jupiter-Rahu Conjunction | Nifty 50 | 10 | 4 | 3.318 | 0.4212 | 2.897 | 75 | 0.4974 | 0.6741 |
| Jupiter-Rahu Conjunction | Nifty 50 | 20 | 4 | 6.914 | 0.8264 | 6.088 | 75 | 0.4362 | 0.6173 |
| Jupiter-Rahu Conjunction | Nifty Bank | 1 | 4 | 0.5264 | 0.06023 | 0.4662 | 75 | 0.5312 | 0.7014 |
| Jupiter-Rahu Conjunction | Nifty Bank | 3 | 4 | 1.245 | 0.1819 | 1.063 | 50 | 0.6758 | 0.8083 |
| Jupiter-Rahu Conjunction | Nifty Bank | 5 | 4 | 1.075 | 0.3 | 0.7755 | 50 | 0.8666 | 0.9304 |
| Jupiter-Rahu Conjunction | Nifty Bank | 10 | 4 | 1.675 | 0.5834 | 1.091 | 50 | 0.8769 | 0.9372 |
| Jupiter-Rahu Conjunction | Nifty Bank | 20 | 4 | 2.919 | 1.172 | 1.746 | 50 | 0.8468 | 0.9172 |
| Jupiter-Rahu Conjunction | Nifty Midcap 100 | 1 | 4 | -0.556 | 0.05397 | -0.6099 | 50 | 0.2264 | 0.3915 |
| Jupiter-Rahu Conjunction | Nifty Midcap 100 | 3 | 4 | -0.4137 | 0.1609 | -0.5746 | 50 | 0.5941 | 0.7492 |
| Jupiter-Rahu Conjunction | Nifty Midcap 100 | 5 | 4 | -1.201 | 0.266 | -1.467 | 25 | 0.4494 | 0.6292 |
| Jupiter-Rahu Conjunction | Nifty Midcap 100 | 10 | 4 | -0.3385 | 0.532 | -0.8705 | 50 | 0.6662 | 0.8025 |
| Jupiter-Rahu Conjunction | Nifty Midcap 100 | 20 | 4 | 0.6123 | 1.065 | -0.4525 | 50 | 0.8157 | 0.897 |
| Jupiter-Rahu Conjunction | Nifty Midcap 150 | 1 | 4 | 0.3091 | 0.05323 | 0.2558 | 75 | 0.6869 | 0.8141 |
| Jupiter-Rahu Conjunction | Nifty Midcap 150 | 3 | 4 | 0.0001172 | 0.1594 | -0.1593 | 50 | 0.8907 | 0.9451 |
| Jupiter-Rahu Conjunction | Nifty Midcap 150 | 5 | 4 | 0.06911 | 0.2642 | -0.1951 | 75 | 0.9245 | 0.9669 |
| Jupiter-Rahu Conjunction | Nifty Midcap 150 | 10 | 4 | 1.635 | 0.5204 | 1.115 | 75 | 0.6948 | 0.8194 |
| Jupiter-Rahu Conjunction | Nifty Midcap 150 | 20 | 4 | 1.852 | 1.047 | 0.8043 | 75 | 0.7904 | 0.8811 |
| Jupiter-Rahu Conjunction | BSE Sensex | 1 | 4 | -0.03137 | 0.05036 | -0.08173 | 75 | 0.888 | 0.9436 |
| Jupiter-Rahu Conjunction | BSE Sensex | 3 | 4 | -0.2566 | 0.1513 | -0.4079 | 50 | 0.7494 | 0.8555 |
| Jupiter-Rahu Conjunction | BSE Sensex | 5 | 4 | -0.6045 | 0.2506 | -0.8551 | 50 | 0.7015 | 0.8237 |
| Jupiter-Rahu Conjunction | BSE Sensex | 10 | 4 | -0.4586 | 0.4957 | -0.9542 | 25 | 0.7284 | 0.842 |
| Jupiter-Rahu Conjunction | BSE Sensex | 20 | 4 | -0.7584 | 1.002 | -1.76 | 50 | 0.5605 | 0.7248 |
| Jupiter-Saturn Conjunction | Nifty 50 | 1 | 2 | 1.091 | 0.04492 | 1.046 | 100 | 0.01937 | 0.06468 |
| Jupiter-Saturn Conjunction | Nifty 50 | 3 | 2 | 4.392 | 0.1333 | 4.259 | 100 | 0.1794 | 0.334 |
| Jupiter-Saturn Conjunction | Nifty 50 | 5 | 2 | 7.134 | 0.2178 | 6.916 | 100 | 0.2289 | 0.3952 |
| Jupiter-Saturn Conjunction | Nifty 50 | 10 | 2 | 9.657 | 0.4212 | 9.235 | 100 | 0.2074 | 0.3694 |
| Jupiter-Saturn Conjunction | Nifty 50 | 20 | 2 | 17.53 | 0.8264 | 16.7 | 100 | 0.3021 | 0.479 |
| Jupiter-Saturn Conjunction | Nifty Bank | 1 | 2 | 1.466 | 0.06023 | 1.406 | 100 | 0.3593 | 0.5403 |
| Jupiter-Saturn Conjunction | Nifty Bank | 3 | 2 | 5.18 | 0.1819 | 4.998 | 100 | 0.2388 | 0.4066 |
| Jupiter-Saturn Conjunction | Nifty Bank | 5 | 2 | 8.632 | 0.3 | 8.332 | 100 | 0.1711 | 0.3249 |
| Jupiter-Saturn Conjunction | Nifty Bank | 10 | 2 | 11.75 | 0.5834 | 11.17 | 100 | 0.2218 | 0.386 |
| Jupiter-Saturn Conjunction | Nifty Bank | 20 | 2 | 16.31 | 1.172 | 15.14 | 100 | 0.2486 | 0.4188 |
| Jupiter-Saturn Conjunction | Nifty Midcap 100 | 1 | 2 | 1.714 | 0.05397 | 1.66 | 100 | 0.4969 | 0.6739 |
| Jupiter-Saturn Conjunction | Nifty Midcap 100 | 3 | 2 | 2.467 | 0.1609 | 2.306 | 50 | 0.5418 | 0.7095 |
| Jupiter-Saturn Conjunction | Nifty Midcap 100 | 5 | 2 | 2.983 | 0.266 | 2.717 | 50 | 0.559 | 0.7248 |
| Jupiter-Saturn Conjunction | Nifty Midcap 100 | 10 | 2 | 8.515 | 0.532 | 7.983 | 100 | 0.3136 | 0.4908 |
| Jupiter-Saturn Conjunction | Nifty Midcap 100 | 20 | 2 | 9.876 | 1.065 | 8.811 | 100 | 0.2787 | 0.4552 |
| Jupiter-Saturn Conjunction | Nifty Midcap 150 | 1 | 2 | 1.401 | 0.05323 | 1.347 | 100 | 0.1444 | 0.2856 |
| Jupiter-Saturn Conjunction | Nifty Midcap 150 | 3 | 2 | 1.884 | 0.1594 | 1.724 | 100 | 0.4166 | 0.5986 |
| Jupiter-Saturn Conjunction | Nifty Midcap 150 | 5 | 2 | 3.049 | 0.2642 | 2.785 | 100 | 0.3082 | 0.4866 |
| Jupiter-Saturn Conjunction | Nifty Midcap 150 | 10 | 2 | 6.074 | 0.5204 | 5.554 | 100 | 0.04621 | 0.1211 |
| Jupiter-Saturn Conjunction | Nifty Midcap 150 | 20 | 2 | 7.493 | 1.047 | 6.446 | 100 | 0.2208 | 0.3854 |
| Jupiter-Saturn Conjunction | BSE Sensex | 1 | 2 | 1.952 | 0.05036 | 1.902 | 100 | 0.297 | 0.4744 |
| Jupiter-Saturn Conjunction | BSE Sensex | 3 | 2 | 3.177 | 0.1513 | 3.025 | 100 | 0.002123 | 0.01048 |
| Jupiter-Saturn Conjunction | BSE Sensex | 5 | 2 | 6.338 | 0.2506 | 6.087 | 100 | 0.1846 | 0.3415 |
| Jupiter-Saturn Conjunction | BSE Sensex | 10 | 2 | 8.531 | 0.4957 | 8.035 | 100 | 0.17 | 0.3234 |
| Jupiter-Saturn Conjunction | BSE Sensex | 20 | 2 | 9.951 | 1.002 | 8.949 | 100 | 0.1058 | 0.2255 |
| Jupiter-Sun Conjunction | Nifty 50 | 1 | 25 | 0.7596 | 0.04492 | 0.7147 | 80 | 0.01148 | 0.04268 |
| Jupiter-Sun Conjunction | Nifty 50 | 3 | 25 | 2.23 | 0.1333 | 2.096 | 64 | 0.003713 | 0.01671 |
| Jupiter-Sun Conjunction | Nifty 50 | 5 | 25 | 3.416 | 0.2178 | 3.198 | 72 | 0.002891 | 0.01358 |
| Jupiter-Sun Conjunction | Nifty 50 | 10 | 25 | 4.726 | 0.4212 | 4.305 | 68 | 0.001791 | 0.0093 |
| Jupiter-Sun Conjunction | Nifty 50 | 20 | 25 | 7.801 | 0.8264 | 6.974 | 76 | 0.01164 | 0.04296 |
| Jupiter-Sun Conjunction | Nifty Bank | 1 | 25 | 1.111 | 0.06023 | 1.051 | 68 | 0.0249 | 0.07737 |
| Jupiter-Sun Conjunction | Nifty Bank | 3 | 25 | 2.908 | 0.1819 | 2.726 | 68 | 0.005521 | 0.02319 |
| Jupiter-Sun Conjunction | Nifty Bank | 5 | 25 | 4.224 | 0.3 | 3.924 | 80 | 0.002774 | 0.01315 |
| Jupiter-Sun Conjunction | Nifty Bank | 10 | 25 | 6.092 | 0.5834 | 5.509 | 72 | 0.001907 | 0.009784 |
| Jupiter-Sun Conjunction | Nifty Bank | 20 | 25 | 7.45 | 1.172 | 6.277 | 72 | 0.01015 | 0.03833 |
| Jupiter-Sun Conjunction | Nifty Midcap 100 | 1 | 25 | 0.391 | 0.05397 | 0.337 | 76 | 0.1708 | 0.3249 |
| Jupiter-Sun Conjunction | Nifty Midcap 100 | 3 | 25 | 0.2414 | 0.1609 | 0.08051 | 36 | 0.8513 | 0.9194 |
| Jupiter-Sun Conjunction | Nifty Midcap 100 | 5 | 25 | -0.01282 | 0.266 | -0.2788 | 40 | 0.6295 | 0.7765 |
| Jupiter-Sun Conjunction | Nifty Midcap 100 | 10 | 25 | 1.463 | 0.532 | 0.9314 | 76 | 0.2248 | 0.3894 |
| Jupiter-Sun Conjunction | Nifty Midcap 100 | 20 | 25 | 1.3 | 1.065 | 0.2347 | 68 | 0.873 | 0.9351 |
| Jupiter-Sun Conjunction | Nifty Midcap 150 | 1 | 25 | 0.8381 | 0.05323 | 0.7849 | 80 | 0.008012 | 0.03152 |
| Jupiter-Sun Conjunction | Nifty Midcap 150 | 3 | 25 | 0.8023 | 0.1594 | 0.6428 | 68 | 0.1998 | 0.3603 |
| Jupiter-Sun Conjunction | Nifty Midcap 150 | 5 | 25 | 1.102 | 0.2642 | 0.8377 | 68 | 0.1242 | 0.2557 |
| Jupiter-Sun Conjunction | Nifty Midcap 150 | 10 | 25 | 2.52 | 0.5204 | 2 | 76 | 0.01446 | 0.05059 |
| Jupiter-Sun Conjunction | Nifty Midcap 150 | 20 | 25 | 1.557 | 1.047 | 0.5098 | 76 | 0.6586 | 0.7965 |
| Jupiter-Sun Conjunction | BSE Sensex | 1 | 25 | 0.3642 | 0.05036 | 0.3139 | 64 | 0.3659 | 0.5471 |
| Jupiter-Sun Conjunction | BSE Sensex | 3 | 25 | 0.3586 | 0.1513 | 0.2073 | 52 | 0.7243 | 0.8398 |
| Jupiter-Sun Conjunction | BSE Sensex | 5 | 25 | 0.3009 | 0.2506 | 0.05032 | 44 | 0.94 | 0.9756 |
| Jupiter-Sun Conjunction | BSE Sensex | 10 | 25 | 1.1 | 0.4957 | 0.6044 | 60 | 0.5354 | 0.7036 |
| Jupiter-Sun Conjunction | BSE Sensex | 20 | 25 | 1.145 | 1.002 | 0.1436 | 60 | 0.887 | 0.9431 |
| Jupiter-Venus Conjunction | Nifty 50 | 1 | 27 | 0.2365 | 0.04492 | 0.1916 | 48.15 | 0.3855 | 0.5681 |
| Jupiter-Venus Conjunction | Nifty 50 | 3 | 27 | 1.431 | 0.1333 | 1.297 | 66.67 | 0.03579 | 0.1012 |
| Jupiter-Venus Conjunction | Nifty 50 | 5 | 27 | 2.088 | 0.2178 | 1.87 | 51.85 | 0.06663 | 0.1599 |
| Jupiter-Venus Conjunction | Nifty 50 | 10 | 27 | 3.26 | 0.4212 | 2.839 | 59.26 | 0.03756 | 0.1046 |
| Jupiter-Venus Conjunction | Nifty 50 | 20 | 27 | 6.565 | 0.8264 | 5.739 | 62.96 | 0.02342 | 0.07406 |
| Jupiter-Venus Conjunction | Nifty Bank | 1 | 27 | 0.5967 | 0.06023 | 0.5365 | 62.96 | 0.08445 | 0.1902 |
| Jupiter-Venus Conjunction | Nifty Bank | 3 | 27 | 2.011 | 0.1819 | 1.829 | 66.67 | 0.03114 | 0.091 |
| Jupiter-Venus Conjunction | Nifty Bank | 5 | 27 | 2.586 | 0.3 | 2.286 | 59.26 | 0.05498 | 0.1382 |
| Jupiter-Venus Conjunction | Nifty Bank | 10 | 27 | 4.142 | 0.5834 | 3.559 | 62.96 | 0.04041 | 0.1093 |
| Jupiter-Venus Conjunction | Nifty Bank | 20 | 27 | 5.65 | 1.172 | 4.477 | 59.26 | 0.06366 | 0.1552 |
| Jupiter-Venus Conjunction | Nifty Midcap 100 | 1 | 27 | -0.02978 | 0.05397 | -0.08374 | 55.56 | 0.7304 | 0.8436 |
| Jupiter-Venus Conjunction | Nifty Midcap 100 | 3 | 27 | -0.3332 | 0.1609 | -0.494 | 29.63 | 0.02754 | 0.0833 |
| Jupiter-Venus Conjunction | Nifty Midcap 100 | 5 | 27 | -0.3817 | 0.266 | -0.6477 | 33.33 | 0.07635 | 0.1767 |
| Jupiter-Venus Conjunction | Nifty Midcap 100 | 10 | 27 | 0.7277 | 0.532 | 0.1957 | 55.56 | 0.7784 | 0.8736 |
| Jupiter-Venus Conjunction | Nifty Midcap 100 | 20 | 27 | 1.085 | 1.065 | 0.02014 | 62.96 | 0.9835 | 0.9946 |
| Jupiter-Venus Conjunction | Nifty Midcap 150 | 1 | 27 | 0.3303 | 0.05323 | 0.2771 | 51.85 | 0.2553 | 0.4278 |
| Jupiter-Venus Conjunction | Nifty Midcap 150 | 3 | 27 | 0.08629 | 0.1594 | -0.07316 | 62.96 | 0.8318 | 0.9097 |
| Jupiter-Venus Conjunction | Nifty Midcap 150 | 5 | 27 | 0.01968 | 0.2642 | -0.2446 | 51.85 | 0.597 | 0.7511 |
| Jupiter-Venus Conjunction | Nifty Midcap 150 | 10 | 27 | 1.277 | 0.5204 | 0.7565 | 51.85 | 0.3724 | 0.5538 |
| Jupiter-Venus Conjunction | Nifty Midcap 150 | 20 | 27 | 0.8594 | 1.047 | -0.188 | 59.26 | 0.8338 | 0.9109 |
| Jupiter-Venus Conjunction | BSE Sensex | 1 | 27 | 0.01389 | 0.05036 | -0.03647 | 48.15 | 0.8583 | 0.9246 |
| Jupiter-Venus Conjunction | BSE Sensex | 3 | 27 | -0.1106 | 0.1513 | -0.2619 | 51.85 | 0.564 | 0.7258 |
| Jupiter-Venus Conjunction | BSE Sensex | 5 | 27 | -0.2375 | 0.2506 | -0.4881 | 44.44 | 0.4026 | 0.5848 |
| Jupiter-Venus Conjunction | BSE Sensex | 10 | 27 | 0.7136 | 0.4957 | 0.2179 | 51.85 | 0.7768 | 0.8736 |
| Jupiter-Venus Conjunction | BSE Sensex | 20 | 27 | 0.5877 | 1.002 | -0.414 | 55.56 | 0.6627 | 0.7996 |
| Ketu-Mars Conjunction | Nifty 50 | 1 | 17 | 0.385 | 0.04492 | 0.34 | 64.71 | 0.1496 | 0.293 |
| Ketu-Mars Conjunction | Nifty 50 | 3 | 17 | 1.06 | 0.1333 | 0.9263 | 64.71 | 0.2853 | 0.4606 |
| Ketu-Mars Conjunction | Nifty 50 | 5 | 17 | 1.476 | 0.2178 | 1.258 | 58.82 | 0.379 | 0.5608 |
| Ketu-Mars Conjunction | Nifty 50 | 10 | 17 | 0.584 | 0.4212 | 0.1628 | 47.06 | 0.939 | 0.9749 |
| Ketu-Mars Conjunction | Nifty 50 | 20 | 17 | 2.784 | 0.8264 | 1.958 | 52.94 | 0.6312 | 0.7776 |
| Ketu-Mars Conjunction | Nifty Bank | 1 | 17 | 0.628 | 0.06023 | 0.5678 | 58.82 | 0.1673 | 0.3195 |
| Ketu-Mars Conjunction | Nifty Bank | 3 | 17 | 1.296 | 0.1819 | 1.114 | 58.82 | 0.3631 | 0.5447 |
| Ketu-Mars Conjunction | Nifty Bank | 5 | 17 | 1.615 | 0.3 | 1.315 | 58.82 | 0.4647 | 0.6421 |
| Ketu-Mars Conjunction | Nifty Bank | 10 | 17 | 0.6765 | 0.5834 | 0.0931 | 47.06 | 0.9732 | 0.9895 |
| Ketu-Mars Conjunction | Nifty Bank | 20 | 17 | 1.112 | 1.172 | -0.06029 | 58.82 | 0.989 | 0.9956 |
| Ketu-Mars Conjunction | Nifty Midcap 100 | 1 | 17 | 0.086 | 0.05397 | 0.03203 | 64.71 | 0.921 | 0.9658 |
| Ketu-Mars Conjunction | Nifty Midcap 100 | 3 | 17 | -0.3672 | 0.1609 | -0.5281 | 41.18 | 0.31 | 0.4871 |
| Ketu-Mars Conjunction | Nifty Midcap 100 | 5 | 17 | -0.6499 | 0.266 | -0.9159 | 29.41 | 0.2189 | 0.3844 |
| Ketu-Mars Conjunction | Nifty Midcap 100 | 10 | 17 | -0.6829 | 0.532 | -1.215 | 58.82 | 0.4014 | 0.5838 |
| Ketu-Mars Conjunction | Nifty Midcap 100 | 20 | 17 | -2.284 | 1.065 | -3.349 | 52.94 | 0.2416 | 0.4097 |
| Ketu-Mars Conjunction | Nifty Midcap 150 | 1 | 17 | 0.4115 | 0.05323 | 0.3582 | 58.82 | 0.1695 | 0.3229 |
| Ketu-Mars Conjunction | Nifty Midcap 150 | 3 | 17 | -0.1777 | 0.1594 | -0.3372 | 58.82 | 0.5691 | 0.7296 |
| Ketu-Mars Conjunction | Nifty Midcap 150 | 5 | 17 | -0.7194 | 0.2642 | -0.9837 | 52.94 | 0.2784 | 0.4549 |
| Ketu-Mars Conjunction | Nifty Midcap 150 | 10 | 17 | -1.403 | 0.5204 | -1.924 | 47.06 | 0.2328 | 0.3986 |
| Ketu-Mars Conjunction | Nifty Midcap 150 | 20 | 17 | -2.201 | 1.047 | -3.248 | 52.94 | 0.223 | 0.3869 |
| Ketu-Mars Conjunction | BSE Sensex | 1 | 17 | -0.1446 | 0.05036 | -0.195 | 52.94 | 0.6171 | 0.7645 |
| Ketu-Mars Conjunction | BSE Sensex | 3 | 17 | -0.7562 | 0.1513 | -0.9075 | 47.06 | 0.204 | 0.3653 |
| Ketu-Mars Conjunction | BSE Sensex | 5 | 17 | -1.389 | 0.2506 | -1.64 | 41.18 | 0.08399 | 0.1894 |
| Ketu-Mars Conjunction | BSE Sensex | 10 | 17 | -2.669 | 0.4957 | -3.165 | 35.29 | 0.04181 | 0.1119 |
| Ketu-Mars Conjunction | BSE Sensex | 20 | 17 | -2.897 | 1.002 | -3.899 | 47.06 | 0.1397 | 0.2786 |
| Ketu-Mercury Conjunction | Nifty 50 | 1 | 28 | 0.2786 | 0.04492 | 0.2336 | 60.71 | 0.2714 | 0.4472 |
| Ketu-Mercury Conjunction | Nifty 50 | 3 | 28 | 1.693 | 0.1333 | 1.56 | 67.86 | 0.01323 | 0.04761 |
| Ketu-Mercury Conjunction | Nifty 50 | 5 | 28 | 3.075 | 0.2178 | 2.857 | 67.86 | 0.005301 | 0.02236 |
| Ketu-Mercury Conjunction | Nifty 50 | 10 | 28 | 4.198 | 0.4212 | 3.776 | 67.86 | 0.00375 | 0.01678 |
| Ketu-Mercury Conjunction | Nifty 50 | 20 | 28 | 8.598 | 0.8264 | 7.772 | 67.86 | 0.003147 | 0.01459 |
| Ketu-Mercury Conjunction | Nifty Bank | 1 | 28 | 0.8459 | 0.06023 | 0.7856 | 67.86 | 0.0386 | 0.1063 |
| Ketu-Mercury Conjunction | Nifty Bank | 3 | 28 | 2.279 | 0.1819 | 2.097 | 60.71 | 0.009096 | 0.03484 |
| Ketu-Mercury Conjunction | Nifty Bank | 5 | 28 | 3.554 | 0.3 | 3.254 | 64.29 | 0.008123 | 0.03179 |
| Ketu-Mercury Conjunction | Nifty Bank | 10 | 28 | 5.523 | 0.5834 | 4.94 | 67.86 | 0.001614 | 0.008558 |
| Ketu-Mercury Conjunction | Nifty Bank | 20 | 28 | 8.288 | 1.172 | 7.116 | 64.29 | 0.002097 | 0.01039 |
| Ketu-Mercury Conjunction | Nifty Midcap 100 | 1 | 28 | -0.05284 | 0.05397 | -0.1068 | 53.57 | 0.5473 | 0.7148 |
| Ketu-Mercury Conjunction | Nifty Midcap 100 | 3 | 28 | 0.3366 | 0.1609 | 0.1757 | 42.86 | 0.5384 | 0.7061 |
| Ketu-Mercury Conjunction | Nifty Midcap 100 | 5 | 28 | 0.5095 | 0.266 | 0.2435 | 46.43 | 0.4366 | 0.6173 |
| Ketu-Mercury Conjunction | Nifty Midcap 100 | 10 | 28 | 2.082 | 0.532 | 1.55 | 78.57 | 0.02007 | 0.06611 |
| Ketu-Mercury Conjunction | Nifty Midcap 100 | 20 | 28 | 3.218 | 1.065 | 2.153 | 82.14 | 0.03436 | 0.09768 |
| Ketu-Mercury Conjunction | Nifty Midcap 150 | 1 | 28 | 0.4509 | 0.05323 | 0.3977 | 60.71 | 0.1042 | 0.2237 |
| Ketu-Mercury Conjunction | Nifty Midcap 150 | 3 | 28 | 0.3099 | 0.1594 | 0.1505 | 64.29 | 0.6752 | 0.8083 |
| Ketu-Mercury Conjunction | Nifty Midcap 150 | 5 | 28 | 0.7172 | 0.2642 | 0.453 | 67.86 | 0.3317 | 0.511 |
| Ketu-Mercury Conjunction | Nifty Midcap 150 | 10 | 28 | 1.967 | 0.5204 | 1.447 | 60.71 | 0.03921 | 0.107 |
| Ketu-Mercury Conjunction | Nifty Midcap 150 | 20 | 28 | 2.336 | 1.047 | 1.288 | 67.86 | 0.1651 | 0.3165 |
| Ketu-Mercury Conjunction | BSE Sensex | 1 | 28 | 0.08291 | 0.05036 | 0.03255 | 53.57 | 0.8779 | 0.9372 |
| Ketu-Mercury Conjunction | BSE Sensex | 3 | 28 | 0.3363 | 0.1513 | 0.185 | 53.57 | 0.6531 | 0.7932 |
| Ketu-Mercury Conjunction | BSE Sensex | 5 | 28 | 0.3807 | 0.2506 | 0.1301 | 53.57 | 0.7969 | 0.8854 |
| Ketu-Mercury Conjunction | BSE Sensex | 10 | 28 | 0.4614 | 0.4957 | -0.03422 | 57.14 | 0.9558 | 0.982 |
| Ketu-Mercury Conjunction | BSE Sensex | 20 | 28 | 1.622 | 1.002 | 0.62 | 60.71 | 0.5294 | 0.7006 |
| Ketu-Moon Conjunction | Nifty 50 | 1 | 57 | 0.2306 | 0.04492 | 0.1857 | 63.16 | 0.1749 | 0.3286 |
| Ketu-Moon Conjunction | Nifty 50 | 3 | 57 | 1.841 | 0.1333 | 1.708 | 66.67 | 6.501e-05 | 0.0007006 |
| Ketu-Moon Conjunction | Nifty 50 | 5 | 57 | 3.297 | 0.2178 | 3.079 | 68.42 | 1.705e-05 | 0.0002488 |
| Ketu-Moon Conjunction | Nifty 50 | 10 | 57 | 4.659 | 0.4212 | 4.237 | 64.91 | 2.124e-05 | 0.0002972 |
| Ketu-Moon Conjunction | Nifty 50 | 20 | 57 | 9.414 | 0.8264 | 8.588 | 71.93 | 7.423e-06 | 0.0001226 |
| Ketu-Moon Conjunction | Nifty Bank | 1 | 57 | 0.6182 | 0.06023 | 0.558 | 61.4 | 0.01917 | 0.06436 |
| Ketu-Moon Conjunction | Nifty Bank | 3 | 57 | 2.332 | 0.1819 | 2.15 | 66.67 | 0.0001313 | 0.001219 |
| Ketu-Moon Conjunction | Nifty Bank | 5 | 57 | 3.726 | 0.3 | 3.426 | 57.89 | 4.114e-05 | 0.0004806 |
| Ketu-Moon Conjunction | Nifty Bank | 10 | 57 | 5.815 | 0.5834 | 5.231 | 61.4 | 2.811e-05 | 0.000361 |
| Ketu-Moon Conjunction | Nifty Bank | 20 | 57 | 8.23 | 1.172 | 7.058 | 66.67 | 9.754e-05 | 0.0009601 |
| Ketu-Moon Conjunction | Nifty Midcap 100 | 1 | 57 | 0.1095 | 0.05397 | 0.05554 | 73.68 | 0.6993 | 0.8221 |
| Ketu-Moon Conjunction | Nifty Midcap 100 | 3 | 57 | 0.1357 | 0.1609 | -0.02515 | 36.84 | 0.9224 | 0.9665 |
| Ketu-Moon Conjunction | Nifty Midcap 100 | 5 | 57 | 0.1268 | 0.266 | -0.1392 | 43.86 | 0.6922 | 0.8183 |
| Ketu-Moon Conjunction | Nifty Midcap 100 | 10 | 57 | 1.839 | 0.532 | 1.307 | 75.44 | 0.02755 | 0.0833 |
| Ketu-Moon Conjunction | Nifty Midcap 100 | 20 | 57 | 1.797 | 1.065 | 0.7323 | 71.93 | 0.4519 | 0.6313 |
| Ketu-Moon Conjunction | Nifty Midcap 150 | 1 | 57 | 0.1975 | 0.05323 | 0.1443 | 56.14 | 0.4413 | 0.6219 |
| Ketu-Moon Conjunction | Nifty Midcap 150 | 3 | 57 | -0.13 | 0.1594 | -0.2894 | 61.4 | 0.2996 | 0.4757 |
| Ketu-Moon Conjunction | Nifty Midcap 150 | 5 | 57 | 0.4116 | 0.2642 | 0.1474 | 66.67 | 0.6627 | 0.7996 |
| Ketu-Moon Conjunction | Nifty Midcap 150 | 10 | 57 | 1.946 | 0.5204 | 1.426 | 59.65 | 0.02434 | 0.0762 |
| Ketu-Moon Conjunction | Nifty Midcap 150 | 20 | 57 | 2.433 | 1.047 | 1.386 | 70.18 | 0.1046 | 0.2244 |
| Ketu-Moon Conjunction | BSE Sensex | 1 | 57 | -0.2083 | 0.05036 | -0.2586 | 45.61 | 0.1764 | 0.3303 |
| Ketu-Moon Conjunction | BSE Sensex | 3 | 57 | 0.1269 | 0.1513 | -0.02446 | 50.88 | 0.9424 | 0.9769 |
| Ketu-Moon Conjunction | BSE Sensex | 5 | 57 | 0.5057 | 0.2506 | 0.2551 | 54.39 | 0.5676 | 0.7282 |
| Ketu-Moon Conjunction | BSE Sensex | 10 | 57 | 0.9584 | 0.4957 | 0.4628 | 47.37 | 0.4219 | 0.6034 |
| Ketu-Moon Conjunction | BSE Sensex | 20 | 57 | 1.69 | 1.002 | 0.6881 | 52.63 | 0.4146 | 0.5961 |
| Ketu-Saturn Conjunction | Nifty 50 | 1 | 2 | 1.727 | 0.04492 | 1.682 | 50 | 0.6489 | 0.7921 |
| Ketu-Saturn Conjunction | Nifty 50 | 3 | 2 | 0.4834 | 0.1333 | 0.3501 | 50 | 0.8858 | 0.9423 |
| Ketu-Saturn Conjunction | Nifty 50 | 5 | 2 | -1.554 | 0.2178 | -1.771 | 50 | 0.5913 | 0.7471 |
| Ketu-Saturn Conjunction | Nifty 50 | 10 | 2 | 3.625 | 0.4212 | 3.203 | 100 | 0.2658 | 0.4401 |
| Ketu-Saturn Conjunction | Nifty 50 | 20 | 2 | 1.161 | 0.8264 | 0.335 | 50 | 0.9086 | 0.9585 |
| Ketu-Saturn Conjunction | Nifty Bank | 1 | 2 | 1.487 | 0.06023 | 1.426 | 50 | 0.7136 | 0.8334 |
| Ketu-Saturn Conjunction | Nifty Bank | 3 | 2 | 0.4756 | 0.1819 | 0.2937 | 50 | 0.8855 | 0.9423 |
| Ketu-Saturn Conjunction | Nifty Bank | 5 | 2 | -1.772 | 0.3 | -2.072 | 50 | 0.7336 | 0.8454 |
| Ketu-Saturn Conjunction | Nifty Bank | 10 | 2 | 6.595 | 0.5834 | 6.011 | 100 | 0.3503 | 0.5301 |
| Ketu-Saturn Conjunction | Nifty Bank | 20 | 2 | 4.53 | 1.172 | 3.357 | 50 | 0.6687 | 0.8045 |
| Ketu-Saturn Conjunction | Nifty Midcap 100 | 1 | 2 | -0.2745 | 0.05397 | -0.3284 | 50 | 0.7953 | 0.8851 |
| Ketu-Saturn Conjunction | Nifty Midcap 100 | 3 | 2 | -1.293 | 0.1609 | -1.453 | 50 | 0.4871 | 0.665 |
| Ketu-Saturn Conjunction | Nifty Midcap 100 | 5 | 2 | -1.123 | 0.266 | -1.389 | 50 | 0.5147 | 0.6878 |
| Ketu-Saturn Conjunction | Nifty Midcap 100 | 10 | 2 | 0.6832 | 0.532 | 0.1512 | 50 | 0.9459 | 0.9787 |
| Ketu-Saturn Conjunction | Nifty Midcap 100 | 20 | 2 | -4.492 | 1.065 | -5.557 | 50 | 0.5597 | 0.7248 |
| Ketu-Saturn Conjunction | Nifty Midcap 150 | 1 | 2 | 1.595 | 0.05323 | 1.542 | 50 | 0.6574 | 0.7955 |
| Ketu-Saturn Conjunction | Nifty Midcap 150 | 3 | 2 | 0.3205 | 0.1594 | 0.161 | 50 | 0.9381 | 0.9749 |
| Ketu-Saturn Conjunction | Nifty Midcap 150 | 5 | 2 | -1.792 | 0.2642 | -2.056 | 50 | 0.5966 | 0.7511 |
| Ketu-Saturn Conjunction | Nifty Midcap 150 | 10 | 2 | 3.561 | 0.5204 | 3.041 | 100 | 0.2296 | 0.3956 |
| Ketu-Saturn Conjunction | Nifty Midcap 150 | 20 | 2 | 1.1 | 1.047 | 0.05207 | 50 | 0.9856 | 0.9948 |
| Ketu-Saturn Conjunction | BSE Sensex | 1 | 2 | 1.25 | 0.05036 | 1.2 | 50 | 0.685 | 0.8129 |
| Ketu-Saturn Conjunction | BSE Sensex | 3 | 2 | 0.1179 | 0.1513 | -0.0334 | 50 | 0.9858 | 0.9948 |
| Ketu-Saturn Conjunction | BSE Sensex | 5 | 2 | -1.912 | 0.2506 | -2.162 | 50 | 0.576 | 0.7342 |
| Ketu-Saturn Conjunction | BSE Sensex | 10 | 2 | 3.4 | 0.4957 | 2.904 | 100 | 0.2249 | 0.3894 |
| Ketu-Saturn Conjunction | BSE Sensex | 20 | 2 | 0.4746 | 1.002 | -0.527 | 50 | 0.7466 | 0.8533 |
| Ketu-Sun Conjunction | Nifty 50 | 1 | 29 | 0.2842 | 0.04492 | 0.2393 | 65.52 | 0.1486 | 0.292 |
| Ketu-Sun Conjunction | Nifty 50 | 3 | 29 | 1.344 | 0.1333 | 1.211 | 62.07 | 0.05443 | 0.1371 |
| Ketu-Sun Conjunction | Nifty 50 | 5 | 29 | 2.513 | 0.2178 | 2.295 | 55.17 | 0.02786 | 0.08406 |
| Ketu-Sun Conjunction | Nifty 50 | 10 | 29 | 3.761 | 0.4212 | 3.34 | 68.97 | 0.009596 | 0.03642 |
| Ketu-Sun Conjunction | Nifty 50 | 20 | 29 | 8.143 | 0.8264 | 7.316 | 65.52 | 0.004223 | 0.01852 |
| Ketu-Sun Conjunction | Nifty Bank | 1 | 29 | 0.6848 | 0.06023 | 0.6246 | 68.97 | 0.03055 | 0.08979 |
| Ketu-Sun Conjunction | Nifty Bank | 3 | 29 | 1.592 | 0.1819 | 1.41 | 62.07 | 0.09532 | 0.2095 |
| Ketu-Sun Conjunction | Nifty Bank | 5 | 29 | 2.732 | 0.3 | 2.432 | 55.17 | 0.04765 | 0.1238 |
| Ketu-Sun Conjunction | Nifty Bank | 10 | 29 | 5.016 | 0.5834 | 4.433 | 62.07 | 0.006216 | 0.0254 |
| Ketu-Sun Conjunction | Nifty Bank | 20 | 29 | 7.607 | 1.172 | 6.434 | 65.52 | 0.004681 | 0.02006 |
| Ketu-Sun Conjunction | Nifty Midcap 100 | 1 | 29 | -0.1269 | 0.05397 | -0.1809 | 62.07 | 0.3974 | 0.5805 |
| Ketu-Sun Conjunction | Nifty Midcap 100 | 3 | 29 | -0.1632 | 0.1609 | -0.3241 | 31.03 | 0.3558 | 0.5357 |
| Ketu-Sun Conjunction | Nifty Midcap 100 | 5 | 29 | 0.3909 | 0.266 | 0.1248 | 41.38 | 0.7999 | 0.888 |
| Ketu-Sun Conjunction | Nifty Midcap 100 | 10 | 29 | 1.861 | 0.532 | 1.329 | 68.97 | 0.03797 | 0.1051 |
| Ketu-Sun Conjunction | Nifty Midcap 100 | 20 | 29 | 3.179 | 1.065 | 2.114 | 79.31 | 0.03331 | 0.09557 |
| Ketu-Sun Conjunction | Nifty Midcap 150 | 1 | 29 | 0.3426 | 0.05323 | 0.2894 | 58.62 | 0.1534 | 0.2994 |
| Ketu-Sun Conjunction | Nifty Midcap 150 | 3 | 29 | -0.1327 | 0.1594 | -0.2922 | 62.07 | 0.3427 | 0.5231 |
| Ketu-Sun Conjunction | Nifty Midcap 150 | 5 | 29 | -0.02152 | 0.2642 | -0.2858 | 55.17 | 0.5211 | 0.6939 |
| Ketu-Sun Conjunction | Nifty Midcap 150 | 10 | 29 | 1.379 | 0.5204 | 0.8582 | 65.52 | 0.1677 | 0.32 |
| Ketu-Sun Conjunction | Nifty Midcap 150 | 20 | 29 | 1.989 | 1.047 | 0.9417 | 65.52 | 0.2782 | 0.4549 |
| Ketu-Sun Conjunction | BSE Sensex | 1 | 29 | -0.3317 | 0.05036 | -0.3821 | 41.38 | 0.04857 | 0.1257 |
| Ketu-Sun Conjunction | BSE Sensex | 3 | 29 | -0.5714 | 0.1513 | -0.7228 | 41.38 | 0.04972 | 0.1277 |
| Ketu-Sun Conjunction | BSE Sensex | 5 | 29 | -0.9889 | 0.2506 | -1.239 | 34.48 | 0.01914 | 0.06436 |
| Ketu-Sun Conjunction | BSE Sensex | 10 | 29 | 0.2758 | 0.4957 | -0.2198 | 65.52 | 0.6699 | 0.8046 |
| Ketu-Sun Conjunction | BSE Sensex | 20 | 29 | 1.742 | 1.002 | 0.7403 | 58.62 | 0.402 | 0.5842 |
| Ketu-Venus Conjunction | Nifty 50 | 1 | 29 | 0.2693 | 0.04492 | 0.2243 | 65.52 | 0.2871 | 0.4622 |
| Ketu-Venus Conjunction | Nifty 50 | 3 | 29 | 1.596 | 0.1333 | 1.462 | 72.41 | 0.01292 | 0.04686 |
| Ketu-Venus Conjunction | Nifty 50 | 5 | 29 | 2.733 | 0.2178 | 2.515 | 75.86 | 0.01173 | 0.04321 |
| Ketu-Venus Conjunction | Nifty 50 | 10 | 29 | 4.778 | 0.4212 | 4.357 | 82.76 | 0.0002204 | 0.00177 |
| Ketu-Venus Conjunction | Nifty 50 | 20 | 29 | 8.377 | 0.8264 | 7.55 | 86.21 | 0.0016 | 0.008509 |
| Ketu-Venus Conjunction | Nifty Bank | 1 | 29 | 0.5123 | 0.06023 | 0.4521 | 62.07 | 0.281 | 0.4572 |
| Ketu-Venus Conjunction | Nifty Bank | 3 | 29 | 1.797 | 0.1819 | 1.615 | 62.07 | 0.03913 | 0.107 |
| Ketu-Venus Conjunction | Nifty Bank | 5 | 29 | 3.227 | 0.3 | 2.927 | 72.41 | 0.009377 | 0.03581 |
| Ketu-Venus Conjunction | Nifty Bank | 10 | 29 | 6.186 | 0.5834 | 5.603 | 79.31 | 0.000254 | 0.001984 |
| Ketu-Venus Conjunction | Nifty Bank | 20 | 29 | 7.926 | 1.172 | 6.754 | 79.31 | 0.002067 | 0.01032 |
| Ketu-Venus Conjunction | Nifty Midcap 100 | 1 | 29 | -0.05309 | 0.05397 | -0.1071 | 65.52 | 0.7737 | 0.8721 |
| Ketu-Venus Conjunction | Nifty Midcap 100 | 3 | 29 | 0.3662 | 0.1609 | 0.2053 | 44.83 | 0.6391 | 0.7837 |
| Ketu-Venus Conjunction | Nifty Midcap 100 | 5 | 29 | 0.5009 | 0.266 | 0.2349 | 48.28 | 0.6676 | 0.8036 |
| Ketu-Venus Conjunction | Nifty Midcap 100 | 10 | 29 | 2.044 | 0.532 | 1.512 | 68.97 | 0.04369 | 0.1158 |
| Ketu-Venus Conjunction | Nifty Midcap 100 | 20 | 29 | 2.927 | 1.065 | 1.862 | 72.41 | 0.08054 | 0.1837 |
| Ketu-Venus Conjunction | Nifty Midcap 150 | 1 | 29 | 0.3781 | 0.05323 | 0.3248 | 72.41 | 0.1731 | 0.3265 |
| Ketu-Venus Conjunction | Nifty Midcap 150 | 3 | 29 | 0.243 | 0.1594 | 0.08356 | 68.97 | 0.785 | 0.878 |
| Ketu-Venus Conjunction | Nifty Midcap 150 | 5 | 29 | 0.4392 | 0.2642 | 0.175 | 72.41 | 0.7183 | 0.8361 |
| Ketu-Venus Conjunction | Nifty Midcap 150 | 10 | 29 | 2.67 | 0.5204 | 2.15 | 82.76 | 0.0004495 | 0.003192 |
| Ketu-Venus Conjunction | Nifty Midcap 150 | 20 | 29 | 2.631 | 1.047 | 1.583 | 86.21 | 0.03361 | 0.09615 |
| Ketu-Venus Conjunction | BSE Sensex | 1 | 29 | -0.001283 | 0.05036 | -0.05164 | 65.52 | 0.812 | 0.8953 |
| Ketu-Venus Conjunction | BSE Sensex | 3 | 29 | 0.2109 | 0.1513 | 0.05962 | 65.52 | 0.8508 | 0.9192 |
| Ketu-Venus Conjunction | BSE Sensex | 5 | 29 | 0.5649 | 0.2506 | 0.3143 | 62.07 | 0.5643 | 0.7258 |
| Ketu-Venus Conjunction | BSE Sensex | 10 | 29 | 2.018 | 0.4957 | 1.522 | 75.86 | 0.02443 | 0.07635 |
| Ketu-Venus Conjunction | BSE Sensex | 20 | 29 | 1.632 | 1.002 | 0.6299 | 72.41 | 0.4946 | 0.6727 |
| Mars-Mercury Conjunction | Nifty 50 | 1 | 43 | 0.2093 | 0.04492 | 0.1644 | 58.14 | 0.2738 | 0.4503 |
| Mars-Mercury Conjunction | Nifty 50 | 3 | 43 | 1.084 | 0.1333 | 0.9511 | 58.14 | 0.05034 | 0.1289 |
| Mars-Mercury Conjunction | Nifty 50 | 5 | 43 | 1.878 | 0.2178 | 1.66 | 65.12 | 0.03318 | 0.09549 |
| Mars-Mercury Conjunction | Nifty 50 | 10 | 43 | 3.064 | 0.4212 | 2.643 | 62.79 | 0.01274 | 0.04635 |
| Mars-Mercury Conjunction | Nifty 50 | 20 | 43 | 5.535 | 0.8264 | 4.709 | 60.47 | 0.02369 | 0.07472 |
| Mars-Mercury Conjunction | Nifty Bank | 1 | 43 | 0.4605 | 0.06023 | 0.4003 | 55.81 | 0.09163 | 0.2033 |
| Mars-Mercury Conjunction | Nifty Bank | 3 | 43 | 1.331 | 0.1819 | 1.149 | 60.47 | 0.08329 | 0.1883 |
| Mars-Mercury Conjunction | Nifty Bank | 5 | 43 | 2.121 | 0.3 | 1.821 | 65.12 | 0.04804 | 0.1247 |
| Mars-Mercury Conjunction | Nifty Bank | 10 | 43 | 3.599 | 0.5834 | 3.015 | 60.47 | 0.02048 | 0.06713 |
| Mars-Mercury Conjunction | Nifty Bank | 20 | 43 | 4.476 | 1.172 | 3.304 | 58.14 | 0.07862 | 0.1807 |
| Mars-Mercury Conjunction | Nifty Midcap 100 | 1 | 43 | -0.1625 | 0.05397 | -0.2165 | 53.49 | 0.1952 | 0.3538 |
| Mars-Mercury Conjunction | Nifty Midcap 100 | 3 | 43 | -0.2589 | 0.1609 | -0.4198 | 34.88 | 0.2319 | 0.3978 |
| Mars-Mercury Conjunction | Nifty Midcap 100 | 5 | 43 | -0.5072 | 0.266 | -0.7732 | 41.86 | 0.1268 | 0.2598 |
| Mars-Mercury Conjunction | Nifty Midcap 100 | 10 | 43 | 0.6641 | 0.532 | 0.1322 | 62.79 | 0.8689 | 0.9318 |
| Mars-Mercury Conjunction | Nifty Midcap 100 | 20 | 43 | 1.058 | 1.065 | -0.007097 | 69.77 | 0.9957 | 0.9978 |
| Mars-Mercury Conjunction | Nifty Midcap 150 | 1 | 43 | 0.15 | 0.05323 | 0.09681 | 55.81 | 0.6003 | 0.7527 |
| Mars-Mercury Conjunction | Nifty Midcap 150 | 3 | 43 | -0.1005 | 0.1594 | -0.26 | 55.81 | 0.3644 | 0.5459 |
| Mars-Mercury Conjunction | Nifty Midcap 150 | 5 | 43 | -0.04662 | 0.2642 | -0.3109 | 65.12 | 0.4261 | 0.6078 |
| Mars-Mercury Conjunction | Nifty Midcap 150 | 10 | 43 | 1.216 | 0.5204 | 0.696 | 65.12 | 0.3187 | 0.4957 |
| Mars-Mercury Conjunction | Nifty Midcap 150 | 20 | 43 | 0.5119 | 1.047 | -0.5355 | 58.14 | 0.6196 | 0.767 |
| Mars-Mercury Conjunction | BSE Sensex | 1 | 43 | -0.255 | 0.05036 | -0.3053 | 46.51 | 0.1054 | 0.2251 |
| Mars-Mercury Conjunction | BSE Sensex | 3 | 43 | -0.1915 | 0.1513 | -0.3428 | 48.84 | 0.3081 | 0.4866 |
| Mars-Mercury Conjunction | BSE Sensex | 5 | 43 | -0.2538 | 0.2506 | -0.5043 | 58.14 | 0.2146 | 0.3781 |
| Mars-Mercury Conjunction | BSE Sensex | 10 | 43 | 0.4595 | 0.4957 | -0.03621 | 62.79 | 0.9605 | 0.984 |
| Mars-Mercury Conjunction | BSE Sensex | 20 | 43 | 0.1862 | 1.002 | -0.8155 | 60.47 | 0.4985 | 0.6749 |
| Mars-Moon Conjunction | Nifty 50 | 1 | 54 | 0.07319 | 0.04492 | 0.02827 | 55.56 | 0.8494 | 0.9187 |
| Mars-Moon Conjunction | Nifty 50 | 3 | 54 | 1.269 | 0.1333 | 1.136 | 62.96 | 0.01698 | 0.05791 |
| Mars-Moon Conjunction | Nifty 50 | 5 | 54 | 2.278 | 0.2178 | 2.06 | 62.96 | 0.003425 | 0.01565 |
| Mars-Moon Conjunction | Nifty 50 | 10 | 54 | 3.635 | 0.4212 | 3.213 | 62.96 | 0.000489 | 0.003396 |
| Mars-Moon Conjunction | Nifty 50 | 20 | 54 | 7.328 | 0.8264 | 6.501 | 70.37 | 0.0002034 | 0.001695 |
| Mars-Moon Conjunction | Nifty Bank | 1 | 54 | 0.353 | 0.06023 | 0.2928 | 53.7 | 0.26 | 0.4328 |
| Mars-Moon Conjunction | Nifty Bank | 3 | 54 | 1.651 | 0.1819 | 1.47 | 61.11 | 0.02884 | 0.08639 |
| Mars-Moon Conjunction | Nifty Bank | 5 | 54 | 2.611 | 0.3 | 2.311 | 62.96 | 0.007003 | 0.02797 |
| Mars-Moon Conjunction | Nifty Bank | 10 | 54 | 4.435 | 0.5834 | 3.852 | 68.52 | 0.00111 | 0.006435 |
| Mars-Moon Conjunction | Nifty Bank | 20 | 54 | 6.57 | 1.172 | 5.397 | 66.67 | 0.001027 | 0.006034 |
| Mars-Moon Conjunction | Nifty Midcap 100 | 1 | 54 | -0.2323 | 0.05397 | -0.2862 | 50 | 0.03218 | 0.09346 |
| Mars-Moon Conjunction | Nifty Midcap 100 | 3 | 54 | -0.2067 | 0.1609 | -0.3676 | 33.33 | 0.2499 | 0.4208 |
| Mars-Moon Conjunction | Nifty Midcap 100 | 5 | 54 | -0.3853 | 0.266 | -0.6513 | 37.04 | 0.07767 | 0.179 |
| Mars-Moon Conjunction | Nifty Midcap 100 | 10 | 54 | 1.495 | 0.532 | 0.9631 | 64.81 | 0.08244 | 0.187 |
| Mars-Moon Conjunction | Nifty Midcap 100 | 20 | 54 | 2.625 | 1.065 | 1.56 | 72.22 | 0.03786 | 0.105 |
| Mars-Moon Conjunction | Nifty Midcap 150 | 1 | 54 | 0.1645 | 0.05323 | 0.1113 | 55.56 | 0.5087 | 0.6836 |
| Mars-Moon Conjunction | Nifty Midcap 150 | 3 | 54 | -0.005616 | 0.1594 | -0.1651 | 62.96 | 0.591 | 0.7471 |
| Mars-Moon Conjunction | Nifty Midcap 150 | 5 | 54 | 0.2199 | 0.2642 | -0.04438 | 62.96 | 0.8931 | 0.9466 |
| Mars-Moon Conjunction | Nifty Midcap 150 | 10 | 54 | 1.549 | 0.5204 | 1.029 | 61.11 | 0.06537 | 0.1577 |
| Mars-Moon Conjunction | Nifty Midcap 150 | 20 | 54 | 1.477 | 1.047 | 0.4296 | 64.81 | 0.5418 | 0.7095 |
| Mars-Moon Conjunction | BSE Sensex | 1 | 54 | -0.2581 | 0.05036 | -0.3085 | 38.89 | 0.02855 | 0.08557 |
| Mars-Moon Conjunction | BSE Sensex | 3 | 54 | -0.2466 | 0.1513 | -0.3979 | 50 | 0.2429 | 0.4112 |
| Mars-Moon Conjunction | BSE Sensex | 5 | 54 | -0.2034 | 0.2506 | -0.454 | 53.7 | 0.176 | 0.33 |
| Mars-Moon Conjunction | BSE Sensex | 10 | 54 | 0.6688 | 0.4957 | 0.1731 | 57.41 | 0.7247 | 0.8398 |
| Mars-Moon Conjunction | BSE Sensex | 20 | 54 | 0.795 | 1.002 | -0.2067 | 64.81 | 0.7789 | 0.874 |
| Mars-Rahu Conjunction | Nifty 50 | 1 | 16 | 0.09786 | 0.04492 | 0.05293 | 62.5 | 0.8615 | 0.9263 |
| Mars-Rahu Conjunction | Nifty 50 | 3 | 16 | 1.931 | 0.1333 | 1.798 | 75 | 0.02567 | 0.07891 |
| Mars-Rahu Conjunction | Nifty 50 | 5 | 16 | 3.137 | 0.2178 | 2.919 | 68.75 | 0.02918 | 0.08691 |
| Mars-Rahu Conjunction | Nifty 50 | 10 | 16 | 3.638 | 0.4212 | 3.217 | 62.5 | 0.08467 | 0.1905 |
| Mars-Rahu Conjunction | Nifty 50 | 20 | 16 | 8.276 | 0.8264 | 7.449 | 56.25 | 0.03223 | 0.09348 |
| Mars-Rahu Conjunction | Nifty Bank | 1 | 16 | 0.456 | 0.06023 | 0.3958 | 62.5 | 0.4387 | 0.6191 |
| Mars-Rahu Conjunction | Nifty Bank | 3 | 16 | 2.101 | 0.1819 | 1.919 | 56.25 | 0.1021 | 0.2199 |
| Mars-Rahu Conjunction | Nifty Bank | 5 | 16 | 3.074 | 0.3 | 2.774 | 68.75 | 0.1054 | 0.2251 |
| Mars-Rahu Conjunction | Nifty Bank | 10 | 16 | 3.906 | 0.5834 | 3.322 | 62.5 | 0.1903 | 0.3482 |
| Mars-Rahu Conjunction | Nifty Bank | 20 | 16 | 6.483 | 1.172 | 5.311 | 56.25 | 0.1004 | 0.2174 |
| Mars-Rahu Conjunction | Nifty Midcap 100 | 1 | 16 | -0.429 | 0.05397 | -0.483 | 43.75 | 0.05584 | 0.14 |
| Mars-Rahu Conjunction | Nifty Midcap 100 | 3 | 16 | 0.3796 | 0.1609 | 0.2188 | 43.75 | 0.5892 | 0.7459 |
| Mars-Rahu Conjunction | Nifty Midcap 100 | 5 | 16 | 0.2327 | 0.266 | -0.03334 | 37.5 | 0.9557 | 0.982 |
| Mars-Rahu Conjunction | Nifty Midcap 100 | 10 | 16 | 1.185 | 0.532 | 0.6529 | 50 | 0.5319 | 0.7014 |
| Mars-Rahu Conjunction | Nifty Midcap 100 | 20 | 16 | 2.47 | 1.065 | 1.405 | 62.5 | 0.2589 | 0.432 |
| Mars-Rahu Conjunction | Nifty Midcap 150 | 1 | 16 | 0.2262 | 0.05323 | 0.173 | 62.5 | 0.6068 | 0.7565 |
| Mars-Rahu Conjunction | Nifty Midcap 150 | 3 | 16 | 0.2382 | 0.1594 | 0.07879 | 68.75 | 0.8239 | 0.9036 |
| Mars-Rahu Conjunction | Nifty Midcap 150 | 5 | 16 | 0.5239 | 0.2642 | 0.2597 | 75 | 0.5485 | 0.7152 |
| Mars-Rahu Conjunction | Nifty Midcap 150 | 10 | 16 | 0.9079 | 0.5204 | 0.3875 | 56.25 | 0.7087 | 0.8295 |
| Mars-Rahu Conjunction | Nifty Midcap 150 | 20 | 16 | 1.606 | 1.047 | 0.5589 | 56.25 | 0.5004 | 0.6766 |
| Mars-Rahu Conjunction | BSE Sensex | 1 | 16 | 0.03912 | 0.05036 | -0.01124 | 50 | 0.9761 | 0.9901 |
| Mars-Rahu Conjunction | BSE Sensex | 3 | 16 | 0.189 | 0.1513 | 0.03773 | 50 | 0.9464 | 0.9787 |
| Mars-Rahu Conjunction | BSE Sensex | 5 | 16 | 0.1872 | 0.2506 | -0.06341 | 50 | 0.9246 | 0.9669 |
| Mars-Rahu Conjunction | BSE Sensex | 10 | 16 | -0.7123 | 0.4957 | -1.208 | 50 | 0.2024 | 0.3633 |
| Mars-Rahu Conjunction | BSE Sensex | 20 | 16 | 0.2786 | 1.002 | -0.7231 | 43.75 | 0.4095 | 0.5909 |
| Mars-Saturn Conjunction | Nifty 50 | 1 | 14 | -0.2347 | 0.04492 | -0.2796 | 57.14 | 0.5102 | 0.6841 |
| Mars-Saturn Conjunction | Nifty 50 | 3 | 14 | 1.111 | 0.1333 | 0.978 | 64.29 | 0.3413 | 0.5216 |
| Mars-Saturn Conjunction | Nifty 50 | 5 | 14 | 2.892 | 0.2178 | 2.674 | 71.43 | 0.07596 | 0.176 |
| Mars-Saturn Conjunction | Nifty 50 | 10 | 14 | 4.772 | 0.4212 | 4.351 | 64.29 | 0.01957 | 0.06513 |
| Mars-Saturn Conjunction | Nifty 50 | 20 | 14 | 8.474 | 0.8264 | 7.647 | 71.43 | 0.03789 | 0.105 |
| Mars-Saturn Conjunction | Nifty Bank | 1 | 14 | 0.2197 | 0.06023 | 0.1595 | 50 | 0.7751 | 0.8726 |
| Mars-Saturn Conjunction | Nifty Bank | 3 | 14 | 1.199 | 0.1819 | 1.017 | 57.14 | 0.4327 | 0.6154 |
| Mars-Saturn Conjunction | Nifty Bank | 5 | 14 | 3.304 | 0.3 | 3.004 | 64.29 | 0.06634 | 0.1593 |
| Mars-Saturn Conjunction | Nifty Bank | 10 | 14 | 6.386 | 0.5834 | 5.803 | 71.43 | 0.01908 | 0.06436 |
| Mars-Saturn Conjunction | Nifty Bank | 20 | 14 | 7.667 | 1.172 | 6.495 | 78.57 | 0.05644 | 0.1414 |
| Mars-Saturn Conjunction | Nifty Midcap 100 | 1 | 14 | -1.051 | 0.05397 | -1.104 | 50 | 0.08646 | 0.1938 |
| Mars-Saturn Conjunction | Nifty Midcap 100 | 3 | 14 | -1.812 | 0.1609 | -1.973 | 21.43 | 0.09811 | 0.2134 |
| Mars-Saturn Conjunction | Nifty Midcap 100 | 5 | 14 | -1.908 | 0.266 | -2.174 | 21.43 | 0.07965 | 0.1822 |
| Mars-Saturn Conjunction | Nifty Midcap 100 | 10 | 14 | -0.7527 | 0.532 | -1.285 | 57.14 | 0.4176 | 0.5991 |
| Mars-Saturn Conjunction | Nifty Midcap 100 | 20 | 14 | 1.102 | 1.065 | 0.03746 | 57.14 | 0.9857 | 0.9948 |
| Mars-Saturn Conjunction | Nifty Midcap 150 | 1 | 14 | -0.2822 | 0.05323 | -0.3354 | 50 | 0.4616 | 0.6397 |
| Mars-Saturn Conjunction | Nifty Midcap 150 | 3 | 14 | -0.1505 | 0.1594 | -0.3099 | 64.29 | 0.646 | 0.7898 |
| Mars-Saturn Conjunction | Nifty Midcap 150 | 5 | 14 | 0.5639 | 0.2642 | 0.2996 | 71.43 | 0.6865 | 0.8141 |
| Mars-Saturn Conjunction | Nifty Midcap 150 | 10 | 14 | 3.016 | 0.5204 | 2.495 | 71.43 | 0.02477 | 0.07715 |
| Mars-Saturn Conjunction | Nifty Midcap 150 | 20 | 14 | 2.358 | 1.047 | 1.311 | 71.43 | 0.2973 | 0.4744 |
| Mars-Saturn Conjunction | BSE Sensex | 1 | 14 | -0.872 | 0.05036 | -0.9224 | 42.86 | 0.04891 | 0.1264 |
| Mars-Saturn Conjunction | BSE Sensex | 3 | 14 | -0.9971 | 0.1513 | -1.148 | 50 | 0.2222 | 0.3864 |
| Mars-Saturn Conjunction | BSE Sensex | 5 | 14 | -0.7169 | 0.2506 | -0.9674 | 57.14 | 0.3332 | 0.512 |
| Mars-Saturn Conjunction | BSE Sensex | 10 | 14 | 0.3013 | 0.4957 | -0.1944 | 42.86 | 0.8885 | 0.9439 |
| Mars-Saturn Conjunction | BSE Sensex | 20 | 14 | -0.8158 | 1.002 | -1.817 | 50 | 0.3171 | 0.4943 |
| Mars-Sun Conjunction | Nifty 50 | 1 | 13 | 0.9695 | 0.04492 | 0.9246 | 92.31 | 0.02848 | 0.08543 |
| Mars-Sun Conjunction | Nifty 50 | 3 | 13 | 2.569 | 0.1333 | 2.436 | 84.62 | 0.006762 | 0.02718 |
| Mars-Sun Conjunction | Nifty 50 | 5 | 13 | 4.533 | 0.2178 | 4.315 | 76.92 | 0.004496 | 0.01949 |
| Mars-Sun Conjunction | Nifty 50 | 10 | 13 | 5.448 | 0.4212 | 5.026 | 84.62 | 0.008054 | 0.03162 |
| Mars-Sun Conjunction | Nifty 50 | 20 | 13 | 10.35 | 0.8264 | 9.528 | 92.31 | 0.009921 | 0.03754 |
| Mars-Sun Conjunction | Nifty Bank | 1 | 13 | 1.343 | 0.06023 | 1.283 | 84.62 | 0.001778 | 0.009247 |
| Mars-Sun Conjunction | Nifty Bank | 3 | 13 | 3.153 | 0.1819 | 2.971 | 84.62 | 0.007599 | 0.03012 |
| Mars-Sun Conjunction | Nifty Bank | 5 | 13 | 5.359 | 0.3 | 5.059 | 92.31 | 0.001902 | 0.009772 |
| Mars-Sun Conjunction | Nifty Bank | 10 | 13 | 7.726 | 0.5834 | 7.142 | 84.62 | 0.002109 | 0.01042 |
| Mars-Sun Conjunction | Nifty Bank | 20 | 13 | 10.69 | 1.172 | 9.516 | 92.31 | 0.002222 | 0.01082 |
| Mars-Sun Conjunction | Nifty Midcap 100 | 1 | 13 | 0.00712 | 0.05397 | -0.04685 | 69.23 | 0.9166 | 0.9629 |
| Mars-Sun Conjunction | Nifty Midcap 100 | 3 | 13 | -0.6308 | 0.1609 | -0.7917 | 23.08 | 0.1113 | 0.2354 |
| Mars-Sun Conjunction | Nifty Midcap 100 | 5 | 13 | -0.3909 | 0.266 | -0.6569 | 23.08 | 0.1965 | 0.3556 |
| Mars-Sun Conjunction | Nifty Midcap 100 | 10 | 13 | 1.069 | 0.532 | 0.5371 | 69.23 | 0.4846 | 0.6622 |
| Mars-Sun Conjunction | Nifty Midcap 100 | 20 | 13 | 1.263 | 1.065 | 0.1983 | 46.15 | 0.8857 | 0.9423 |
| Mars-Sun Conjunction | Nifty Midcap 150 | 1 | 13 | 1.047 | 0.05323 | 0.9941 | 92.31 | 0.01932 | 0.06459 |
| Mars-Sun Conjunction | Nifty Midcap 150 | 3 | 13 | 1.197 | 0.1594 | 1.038 | 92.31 | 0.07027 | 0.1661 |
| Mars-Sun Conjunction | Nifty Midcap 150 | 5 | 13 | 2.177 | 0.2642 | 1.913 | 84.62 | 0.02605 | 0.07975 |
| Mars-Sun Conjunction | Nifty Midcap 150 | 10 | 13 | 3.093 | 0.5204 | 2.572 | 84.62 | 0.01158 | 0.04282 |
| Mars-Sun Conjunction | Nifty Midcap 150 | 20 | 13 | 4.309 | 1.047 | 3.261 | 92.31 | 0.001983 | 0.01001 |
| Mars-Sun Conjunction | BSE Sensex | 1 | 13 | 0.8705 | 0.05036 | 0.8201 | 92.31 | 0.05652 | 0.1414 |
| Mars-Sun Conjunction | BSE Sensex | 3 | 13 | 1.457 | 0.1513 | 1.306 | 84.62 | 0.02747 | 0.08329 |
| Mars-Sun Conjunction | BSE Sensex | 5 | 13 | 2.182 | 0.2506 | 1.932 | 76.92 | 0.02317 | 0.07348 |
| Mars-Sun Conjunction | BSE Sensex | 10 | 13 | 1.87 | 0.4957 | 1.374 | 76.92 | 0.111 | 0.2349 |
| Mars-Sun Conjunction | BSE Sensex | 20 | 13 | 2.581 | 1.002 | 1.58 | 84.62 | 0.3037 | 0.4806 |
| Mars-Venus Conjunction | Nifty 50 | 1 | 21 | 0.2464 | 0.04492 | 0.2014 | 66.67 | 0.4684 | 0.6458 |
| Mars-Venus Conjunction | Nifty 50 | 3 | 21 | 1.332 | 0.1333 | 1.199 | 57.14 | 0.09709 | 0.2119 |
| Mars-Venus Conjunction | Nifty 50 | 5 | 21 | 2.731 | 0.2178 | 2.513 | 61.9 | 0.02194 | 0.07068 |
| Mars-Venus Conjunction | Nifty 50 | 10 | 21 | 3.7 | 0.4212 | 3.279 | 57.14 | 0.02704 | 0.08216 |
| Mars-Venus Conjunction | Nifty 50 | 20 | 21 | 8.708 | 0.8264 | 7.881 | 66.67 | 0.01065 | 0.04004 |
| Mars-Venus Conjunction | Nifty Bank | 1 | 21 | 0.4036 | 0.06023 | 0.3434 | 52.38 | 0.3553 | 0.5353 |
| Mars-Venus Conjunction | Nifty Bank | 3 | 21 | 1.741 | 0.1819 | 1.559 | 52.38 | 0.09237 | 0.2046 |
| Mars-Venus Conjunction | Nifty Bank | 5 | 21 | 3.513 | 0.3 | 3.213 | 66.67 | 0.01272 | 0.0463 |
| Mars-Venus Conjunction | Nifty Bank | 10 | 21 | 4.968 | 0.5834 | 4.384 | 57.14 | 0.02132 | 0.06923 |
| Mars-Venus Conjunction | Nifty Bank | 20 | 21 | 9.939 | 1.172 | 8.766 | 80.95 | 0.005957 | 0.02466 |
| Mars-Venus Conjunction | Nifty Midcap 100 | 1 | 21 | 0.3224 | 0.05397 | 0.2684 | 61.9 | 0.5548 | 0.7206 |
| Mars-Venus Conjunction | Nifty Midcap 100 | 3 | 21 | 0.3482 | 0.1609 | 0.1873 | 33.33 | 0.766 | 0.8679 |
| Mars-Venus Conjunction | Nifty Midcap 100 | 5 | 21 | 0.3583 | 0.266 | 0.0923 | 38.1 | 0.9149 | 0.9623 |
| Mars-Venus Conjunction | Nifty Midcap 100 | 10 | 21 | 0.7233 | 0.532 | 0.1914 | 66.67 | 0.8896 | 0.9445 |
| Mars-Venus Conjunction | Nifty Midcap 100 | 20 | 21 | 1.629 | 1.065 | 0.5645 | 57.14 | 0.8032 | 0.8906 |
| Mars-Venus Conjunction | Nifty Midcap 150 | 1 | 21 | 0.3847 | 0.05323 | 0.3315 | 71.43 | 0.2863 | 0.4615 |
| Mars-Venus Conjunction | Nifty Midcap 150 | 3 | 21 | 0.2109 | 0.1594 | 0.05148 | 57.14 | 0.9106 | 0.9595 |
| Mars-Venus Conjunction | Nifty Midcap 150 | 5 | 21 | 0.8765 | 0.2642 | 0.6123 | 57.14 | 0.2541 | 0.4265 |
| Mars-Venus Conjunction | Nifty Midcap 150 | 10 | 21 | 1.858 | 0.5204 | 1.337 | 61.9 | 0.1439 | 0.2848 |
| Mars-Venus Conjunction | Nifty Midcap 150 | 20 | 21 | 3.866 | 1.047 | 2.818 | 71.43 | 0.1434 | 0.284 |
| Mars-Venus Conjunction | BSE Sensex | 1 | 21 | 0.1288 | 0.05036 | 0.07846 | 57.14 | 0.7695 | 0.8702 |
| Mars-Venus Conjunction | BSE Sensex | 3 | 21 | -0.05746 | 0.1513 | -0.2088 | 38.1 | 0.6701 | 0.8046 |
| Mars-Venus Conjunction | BSE Sensex | 5 | 21 | 0.2542 | 0.2506 | 0.003632 | 42.86 | 0.9951 | 0.9976 |
| Mars-Venus Conjunction | BSE Sensex | 10 | 21 | 0.8132 | 0.4957 | 0.3176 | 52.38 | 0.7277 | 0.8419 |
| Mars-Venus Conjunction | BSE Sensex | 20 | 21 | 2.671 | 1.002 | 1.669 | 57.14 | 0.3991 | 0.5817 |
| Mercury-Moon Conjunction | Nifty 50 | 1 | 57 | 0.601 | 0.04492 | 0.5561 | 70.18 | 0.002507 | 0.01209 |
| Mercury-Moon Conjunction | Nifty 50 | 3 | 57 | 2.006 | 0.1333 | 1.873 | 68.42 | 0.0007775 | 0.004835 |
| Mercury-Moon Conjunction | Nifty 50 | 5 | 57 | 2.894 | 0.2178 | 2.676 | 68.42 | 0.0006101 | 0.003958 |
| Mercury-Moon Conjunction | Nifty 50 | 10 | 57 | 3.804 | 0.4212 | 3.383 | 71.93 | 0.0004524 | 0.003197 |
| Mercury-Moon Conjunction | Nifty 50 | 20 | 57 | 7.447 | 0.8264 | 6.621 | 70.18 | 0.0001703 | 0.001486 |
| Mercury-Moon Conjunction | Nifty Bank | 1 | 57 | 1.057 | 0.06023 | 0.9969 | 73.68 | 5.35e-05 | 0.0006061 |
| Mercury-Moon Conjunction | Nifty Bank | 3 | 57 | 2.636 | 0.1819 | 2.454 | 64.91 | 8.808e-05 | 0.0008903 |
| Mercury-Moon Conjunction | Nifty Bank | 5 | 57 | 3.425 | 0.3 | 3.125 | 68.42 | 0.0008795 | 0.005311 |
| Mercury-Moon Conjunction | Nifty Bank | 10 | 57 | 4.971 | 0.5834 | 4.387 | 66.67 | 0.000132 | 0.001222 |
| Mercury-Moon Conjunction | Nifty Bank | 20 | 57 | 6.489 | 1.172 | 5.317 | 66.67 | 0.001248 | 0.007082 |
| Mercury-Moon Conjunction | Nifty Midcap 100 | 1 | 57 | 0.1679 | 0.05397 | 0.1139 | 64.91 | 0.5661 | 0.7273 |
| Mercury-Moon Conjunction | Nifty Midcap 100 | 3 | 57 | 0.02765 | 0.1609 | -0.1332 | 33.33 | 0.7183 | 0.8361 |
| Mercury-Moon Conjunction | Nifty Midcap 100 | 5 | 57 | -0.3649 | 0.266 | -0.6309 | 36.84 | 0.1965 | 0.3556 |
| Mercury-Moon Conjunction | Nifty Midcap 100 | 10 | 57 | 1.126 | 0.532 | 0.5936 | 59.65 | 0.4091 | 0.5909 |
| Mercury-Moon Conjunction | Nifty Midcap 100 | 20 | 57 | 2.507 | 1.065 | 1.443 | 63.16 | 0.1118 | 0.2361 |
| Mercury-Moon Conjunction | Nifty Midcap 150 | 1 | 57 | 0.648 | 0.05323 | 0.5948 | 68.42 | 0.002081 | 0.01038 |
| Mercury-Moon Conjunction | Nifty Midcap 150 | 3 | 57 | 0.753 | 0.1594 | 0.5936 | 66.67 | 0.1915 | 0.3496 |
| Mercury-Moon Conjunction | Nifty Midcap 150 | 5 | 57 | 0.7866 | 0.2642 | 0.5224 | 66.67 | 0.3254 | 0.5035 |
| Mercury-Moon Conjunction | Nifty Midcap 150 | 10 | 57 | 1.633 | 0.5204 | 1.113 | 68.42 | 0.1179 | 0.2457 |
| Mercury-Moon Conjunction | Nifty Midcap 150 | 20 | 57 | 2.008 | 1.047 | 0.9605 | 70.18 | 0.2672 | 0.4421 |
| Mercury-Moon Conjunction | BSE Sensex | 1 | 57 | 0.3761 | 0.05036 | 0.3257 | 56.14 | 0.08859 | 0.1976 |
| Mercury-Moon Conjunction | BSE Sensex | 3 | 57 | 0.6327 | 0.1513 | 0.4813 | 56.14 | 0.3261 | 0.5038 |
| Mercury-Moon Conjunction | BSE Sensex | 5 | 57 | 0.4598 | 0.2506 | 0.2093 | 61.4 | 0.7107 | 0.8312 |
| Mercury-Moon Conjunction | BSE Sensex | 10 | 57 | 0.5865 | 0.4957 | 0.09086 | 57.89 | 0.899 | 0.9515 |
| Mercury-Moon Conjunction | BSE Sensex | 20 | 57 | 1.493 | 1.002 | 0.491 | 64.91 | 0.5735 | 0.733 |
| Mercury-Rahu Conjunction | Nifty 50 | 1 | 42 | 0.1222 | 0.04492 | 0.07724 | 57.14 | 0.7247 | 0.8398 |
| Mercury-Rahu Conjunction | Nifty 50 | 3 | 42 | 1.047 | 0.1333 | 0.9136 | 66.67 | 0.06212 | 0.1525 |
| Mercury-Rahu Conjunction | Nifty 50 | 5 | 42 | 1.764 | 0.2178 | 1.546 | 66.67 | 0.03964 | 0.1078 |
| Mercury-Rahu Conjunction | Nifty 50 | 10 | 42 | 3.179 | 0.4212 | 2.758 | 73.81 | 0.002954 | 0.01377 |
| Mercury-Rahu Conjunction | Nifty 50 | 20 | 42 | 6.156 | 0.8264 | 5.33 | 64.29 | 0.00288 | 0.01357 |
| Mercury-Rahu Conjunction | Nifty Bank | 1 | 42 | 0.1976 | 0.06023 | 0.1373 | 66.67 | 0.6531 | 0.7932 |
| Mercury-Rahu Conjunction | Nifty Bank | 3 | 42 | 1.233 | 0.1819 | 1.051 | 71.43 | 0.12 | 0.2487 |
| Mercury-Rahu Conjunction | Nifty Bank | 5 | 42 | 1.778 | 0.3 | 1.478 | 69.05 | 0.1234 | 0.2544 |
| Mercury-Rahu Conjunction | Nifty Bank | 10 | 42 | 3.764 | 0.5834 | 3.181 | 73.81 | 0.008891 | 0.03427 |
| Mercury-Rahu Conjunction | Nifty Bank | 20 | 42 | 6.248 | 1.172 | 5.075 | 73.81 | 0.002645 | 0.01262 |
| Mercury-Rahu Conjunction | Nifty Midcap 100 | 1 | 42 | 0.05909 | 0.05397 | 0.005129 | 59.52 | 0.9796 | 0.9921 |
| Mercury-Rahu Conjunction | Nifty Midcap 100 | 3 | 42 | -0.05087 | 0.1609 | -0.2117 | 45.24 | 0.4657 | 0.6423 |
| Mercury-Rahu Conjunction | Nifty Midcap 100 | 5 | 42 | -0.04448 | 0.266 | -0.3105 | 40.48 | 0.4363 | 0.6173 |
| Mercury-Rahu Conjunction | Nifty Midcap 100 | 10 | 42 | 1.778 | 0.532 | 1.246 | 64.29 | 0.05216 | 0.1323 |
| Mercury-Rahu Conjunction | Nifty Midcap 100 | 20 | 42 | 1.845 | 1.065 | 0.7802 | 64.29 | 0.3993 | 0.5817 |
| Mercury-Rahu Conjunction | Nifty Midcap 150 | 1 | 42 | 0.2106 | 0.05323 | 0.1574 | 54.76 | 0.5019 | 0.6773 |
| Mercury-Rahu Conjunction | Nifty Midcap 150 | 3 | 42 | 0.1394 | 0.1594 | -0.02006 | 66.67 | 0.9539 | 0.982 |
| Mercury-Rahu Conjunction | Nifty Midcap 150 | 5 | 42 | 0.2129 | 0.2642 | -0.05132 | 66.67 | 0.9111 | 0.9595 |
| Mercury-Rahu Conjunction | Nifty Midcap 150 | 10 | 42 | 1.848 | 0.5204 | 1.327 | 69.05 | 0.03124 | 0.09108 |
| Mercury-Rahu Conjunction | Nifty Midcap 150 | 20 | 42 | 2.165 | 1.047 | 1.117 | 61.9 | 0.1945 | 0.3529 |
| Mercury-Rahu Conjunction | BSE Sensex | 1 | 42 | -0.01472 | 0.05036 | -0.06508 | 45.24 | 0.7546 | 0.8588 |
| Mercury-Rahu Conjunction | BSE Sensex | 3 | 42 | 0.1385 | 0.1513 | -0.01285 | 64.29 | 0.9718 | 0.9892 |
| Mercury-Rahu Conjunction | BSE Sensex | 5 | 42 | -0.0591 | 0.2506 | -0.3097 | 59.52 | 0.5251 | 0.6971 |
| Mercury-Rahu Conjunction | BSE Sensex | 10 | 42 | 1.083 | 0.4957 | 0.5869 | 66.67 | 0.3099 | 0.4871 |
| Mercury-Rahu Conjunction | BSE Sensex | 20 | 42 | 1.505 | 1.002 | 0.5029 | 54.76 | 0.5841 | 0.7417 |
| Mercury-Saturn Conjunction | Nifty 50 | 1 | 32 | 0.5015 | 0.04492 | 0.4566 | 68.75 | 0.006451 | 0.02618 |
| Mercury-Saturn Conjunction | Nifty 50 | 3 | 32 | 1.879 | 0.1333 | 1.745 | 78.12 | 0.001547 | 0.00829 |
| Mercury-Saturn Conjunction | Nifty 50 | 5 | 32 | 3.051 | 0.2178 | 2.833 | 65.62 | 0.0008392 | 0.005134 |
| Mercury-Saturn Conjunction | Nifty 50 | 10 | 32 | 3.488 | 0.4212 | 3.067 | 53.12 | 0.006064 | 0.02493 |
| Mercury-Saturn Conjunction | Nifty 50 | 20 | 32 | 7.378 | 0.8264 | 6.552 | 68.75 | 0.002955 | 0.01377 |
| Mercury-Saturn Conjunction | Nifty Bank | 1 | 32 | 0.7988 | 0.06023 | 0.7386 | 68.75 | 0.003346 | 0.0154 |
| Mercury-Saturn Conjunction | Nifty Bank | 3 | 32 | 2.444 | 0.1819 | 2.262 | 75 | 0.001874 | 0.009664 |
| Mercury-Saturn Conjunction | Nifty Bank | 5 | 32 | 3.615 | 0.3 | 3.315 | 71.88 | 0.0009029 | 0.0054 |
| Mercury-Saturn Conjunction | Nifty Bank | 10 | 32 | 4.589 | 0.5834 | 4.006 | 62.5 | 0.004579 | 0.01969 |
| Mercury-Saturn Conjunction | Nifty Bank | 20 | 32 | 7.547 | 1.172 | 6.374 | 75 | 0.0008241 | 0.005058 |
| Mercury-Saturn Conjunction | Nifty Midcap 100 | 1 | 32 | 0.3866 | 0.05397 | 0.3326 | 71.88 | 0.1193 | 0.248 |
| Mercury-Saturn Conjunction | Nifty Midcap 100 | 3 | 32 | 0.6305 | 0.1609 | 0.4696 | 46.88 | 0.3235 | 0.5018 |
| Mercury-Saturn Conjunction | Nifty Midcap 100 | 5 | 32 | 0.8028 | 0.266 | 0.5368 | 46.88 | 0.4053 | 0.5875 |
| Mercury-Saturn Conjunction | Nifty Midcap 100 | 10 | 32 | 1.73 | 0.532 | 1.198 | 75 | 0.1355 | 0.2728 |
| Mercury-Saturn Conjunction | Nifty Midcap 100 | 20 | 32 | 2.584 | 1.065 | 1.519 | 71.88 | 0.1531 | 0.2992 |
| Mercury-Saturn Conjunction | Nifty Midcap 150 | 1 | 32 | 0.4319 | 0.05323 | 0.3787 | 62.5 | 0.07918 | 0.1815 |
| Mercury-Saturn Conjunction | Nifty Midcap 150 | 3 | 32 | 0.4905 | 0.1594 | 0.3311 | 71.88 | 0.3283 | 0.5066 |
| Mercury-Saturn Conjunction | Nifty Midcap 150 | 5 | 32 | 1.025 | 0.2642 | 0.7604 | 68.75 | 0.02536 | 0.07841 |
| Mercury-Saturn Conjunction | Nifty Midcap 150 | 10 | 32 | 1.68 | 0.5204 | 1.16 | 56.25 | 0.04193 | 0.1122 |
| Mercury-Saturn Conjunction | Nifty Midcap 150 | 20 | 32 | 2.22 | 1.047 | 1.173 | 68.75 | 0.08532 | 0.1917 |
| Mercury-Saturn Conjunction | BSE Sensex | 1 | 32 | 0.04715 | 0.05036 | -0.00321 | 56.25 | 0.9876 | 0.9953 |
| Mercury-Saturn Conjunction | BSE Sensex | 3 | 32 | 0.181 | 0.1513 | 0.02972 | 71.88 | 0.9507 | 0.9803 |
| Mercury-Saturn Conjunction | BSE Sensex | 5 | 32 | 0.6481 | 0.2506 | 0.3976 | 62.5 | 0.3712 | 0.5533 |
| Mercury-Saturn Conjunction | BSE Sensex | 10 | 32 | 0.3584 | 0.4957 | -0.1372 | 46.88 | 0.836 | 0.9121 |
| Mercury-Saturn Conjunction | BSE Sensex | 20 | 32 | 1.305 | 1.002 | 0.3031 | 62.5 | 0.6927 | 0.8184 |
| Mercury-Sun Conjunction | Nifty 50 | 1 | 169 | 0.3529 | 0.04492 | 0.308 | 68.64 | 0.0005093 | 0.003504 |
| Mercury-Sun Conjunction | Nifty 50 | 3 | 168 | 1.723 | 0.1333 | 1.59 | 67.26 | 1.984e-09 | 1.078e-07 |
| Mercury-Sun Conjunction | Nifty 50 | 5 | 168 | 3.162 | 0.2178 | 2.944 | 72.02 | 2.654e-13 | 2.211e-11 |
| Mercury-Sun Conjunction | Nifty 50 | 10 | 168 | 4.294 | 0.4212 | 3.872 | 74.4 | 8.137e-13 | 6.357e-11 |
| Mercury-Sun Conjunction | Nifty 50 | 20 | 168 | 8.01 | 0.8264 | 7.184 | 69.64 | 4.69e-12 | 3.589e-10 |
| Mercury-Sun Conjunction | Nifty Bank | 1 | 169 | 0.7376 | 0.06023 | 0.6773 | 66.27 | 3.901e-06 | 7.427e-05 |
| Mercury-Sun Conjunction | Nifty Bank | 3 | 168 | 2.246 | 0.1819 | 2.064 | 66.67 | 1.467e-09 | 8.338e-08 |
| Mercury-Sun Conjunction | Nifty Bank | 5 | 168 | 3.805 | 0.3 | 3.505 | 69.64 | 1.434e-13 | 1.25e-11 |
| Mercury-Sun Conjunction | Nifty Bank | 10 | 168 | 5.715 | 0.5834 | 5.131 | 72.02 | 5.741e-14 | 5.52e-12 |
| Mercury-Sun Conjunction | Nifty Bank | 20 | 168 | 7.371 | 1.172 | 6.199 | 69.05 | 2.106e-10 | 1.41e-08 |
| Mercury-Sun Conjunction | Nifty Midcap 100 | 1 | 169 | 0.02622 | 0.05397 | -0.02775 | 65.68 | 0.8067 | 0.8913 |
| Mercury-Sun Conjunction | Nifty Midcap 100 | 3 | 168 | 0.05694 | 0.1609 | -0.1039 | 38.69 | 0.6273 | 0.7741 |
| Mercury-Sun Conjunction | Nifty Midcap 100 | 5 | 168 | 0.3226 | 0.266 | 0.05657 | 41.07 | 0.8054 | 0.891 |
| Mercury-Sun Conjunction | Nifty Midcap 100 | 10 | 168 | 1.846 | 0.532 | 1.314 | 70.83 | 0.0002096 | 0.001731 |
| Mercury-Sun Conjunction | Nifty Midcap 100 | 20 | 168 | 2.561 | 1.065 | 1.496 | 72.02 | 0.004565 | 0.01968 |
| Mercury-Sun Conjunction | Nifty Midcap 150 | 1 | 169 | 0.3726 | 0.05323 | 0.3193 | 63.91 | 0.00187 | 0.009659 |
| Mercury-Sun Conjunction | Nifty Midcap 150 | 3 | 168 | 0.1835 | 0.1594 | 0.02403 | 63.1 | 0.8896 | 0.9445 |
| Mercury-Sun Conjunction | Nifty Midcap 150 | 5 | 168 | 0.7144 | 0.2642 | 0.4502 | 69.05 | 0.02543 | 0.07842 |
| Mercury-Sun Conjunction | Nifty Midcap 150 | 10 | 168 | 1.998 | 0.5204 | 1.478 | 75 | 2.048e-05 | 0.0002888 |
| Mercury-Sun Conjunction | Nifty Midcap 150 | 20 | 168 | 1.952 | 1.047 | 0.9042 | 69.05 | 0.04252 | 0.1134 |
| Mercury-Sun Conjunction | BSE Sensex | 1 | 169 | -0.005425 | 0.05036 | -0.05579 | 55.03 | 0.5571 | 0.7228 |
| Mercury-Sun Conjunction | BSE Sensex | 3 | 168 | 0.09099 | 0.1513 | -0.06032 | 52.98 | 0.7684 | 0.8692 |
| Mercury-Sun Conjunction | BSE Sensex | 5 | 168 | 0.4046 | 0.2506 | 0.154 | 55.36 | 0.5011 | 0.6771 |
| Mercury-Sun Conjunction | BSE Sensex | 10 | 168 | 0.7279 | 0.4957 | 0.2323 | 63.1 | 0.4959 | 0.6734 |
| Mercury-Sun Conjunction | BSE Sensex | 20 | 168 | 1.048 | 1.002 | 0.04646 | 60.12 | 0.9233 | 0.9669 |
| Mercury-Venus Conjunction | Nifty 50 | 1 | 61 | 0.3941 | 0.04492 | 0.3492 | 60.66 | 0.02183 | 0.07038 |
| Mercury-Venus Conjunction | Nifty 50 | 3 | 61 | 1.736 | 0.1333 | 1.603 | 67.21 | 8.46e-05 | 0.0008598 |
| Mercury-Venus Conjunction | Nifty 50 | 5 | 61 | 2.933 | 0.2178 | 2.715 | 72.13 | 7.818e-05 | 0.0008076 |
| Mercury-Venus Conjunction | Nifty 50 | 10 | 61 | 3.915 | 0.4212 | 3.494 | 68.85 | 0.0001189 | 0.001129 |
| Mercury-Venus Conjunction | Nifty 50 | 20 | 61 | 7.205 | 0.8264 | 6.379 | 70.49 | 0.0002455 | 0.001934 |
| Mercury-Venus Conjunction | Nifty Bank | 1 | 61 | 0.7231 | 0.06023 | 0.6629 | 63.93 | 0.005546 | 0.02326 |
| Mercury-Venus Conjunction | Nifty Bank | 3 | 61 | 2.16 | 0.1819 | 1.978 | 63.93 | 0.0003933 | 0.002842 |
| Mercury-Venus Conjunction | Nifty Bank | 5 | 61 | 3.185 | 0.3 | 2.885 | 70.49 | 0.0005386 | 0.003631 |
| Mercury-Venus Conjunction | Nifty Bank | 10 | 61 | 4.85 | 0.5834 | 4.266 | 65.57 | 0.0006567 | 0.004217 |
| Mercury-Venus Conjunction | Nifty Bank | 20 | 61 | 6.384 | 1.172 | 5.211 | 67.21 | 0.002791 | 0.01321 |
| Mercury-Venus Conjunction | Nifty Midcap 100 | 1 | 61 | -0.003227 | 0.05397 | -0.05719 | 62.3 | 0.7539 | 0.8587 |
| Mercury-Venus Conjunction | Nifty Midcap 100 | 3 | 61 | 0.09828 | 0.1609 | -0.06257 | 45.9 | 0.8349 | 0.9117 |
| Mercury-Venus Conjunction | Nifty Midcap 100 | 5 | 61 | 0.2685 | 0.266 | 0.002452 | 42.62 | 0.9952 | 0.9976 |
| Mercury-Venus Conjunction | Nifty Midcap 100 | 10 | 61 | 1.728 | 0.532 | 1.196 | 72.13 | 0.08484 | 0.1907 |
| Mercury-Venus Conjunction | Nifty Midcap 100 | 20 | 61 | 2.389 | 1.065 | 1.324 | 67.21 | 0.2228 | 0.3869 |
| Mercury-Venus Conjunction | Nifty Midcap 150 | 1 | 61 | 0.4777 | 0.05323 | 0.4244 | 62.3 | 0.01519 | 0.05288 |
| Mercury-Venus Conjunction | Nifty Midcap 150 | 3 | 61 | 0.4405 | 0.1594 | 0.2811 | 65.57 | 0.2403 | 0.4079 |
| Mercury-Venus Conjunction | Nifty Midcap 150 | 5 | 61 | 0.8287 | 0.2642 | 0.5645 | 70.49 | 0.1395 | 0.2786 |
| Mercury-Venus Conjunction | Nifty Midcap 150 | 10 | 61 | 2.029 | 0.5204 | 1.509 | 65.57 | 0.01266 | 0.04619 |
| Mercury-Venus Conjunction | Nifty Midcap 150 | 20 | 61 | 1.834 | 1.047 | 0.7864 | 70.49 | 0.3443 | 0.5242 |
| Mercury-Venus Conjunction | BSE Sensex | 1 | 61 | -0.02721 | 0.05036 | -0.07757 | 45.9 | 0.6849 | 0.8129 |
| Mercury-Venus Conjunction | BSE Sensex | 3 | 61 | 0.2294 | 0.1513 | 0.07806 | 52.46 | 0.8043 | 0.891 |
| Mercury-Venus Conjunction | BSE Sensex | 5 | 61 | 0.3596 | 0.2506 | 0.1091 | 60.66 | 0.7964 | 0.8854 |
| Mercury-Venus Conjunction | BSE Sensex | 10 | 61 | 1.061 | 0.4957 | 0.5655 | 65.57 | 0.3685 | 0.5504 |
| Mercury-Venus Conjunction | BSE Sensex | 20 | 61 | 1.301 | 1.002 | 0.2994 | 60.66 | 0.7526 | 0.858 |
| Moon-Rahu Conjunction | Nifty 50 | 1 | 54 | 0.5163 | 0.04492 | 0.4714 | 62.96 | 0.189 | 0.3469 |
| Moon-Rahu Conjunction | Nifty 50 | 3 | 54 | 1.823 | 0.1333 | 1.69 | 61.11 | 0.001515 | 0.008128 |
| Moon-Rahu Conjunction | Nifty 50 | 5 | 54 | 3.089 | 0.2178 | 2.871 | 68.52 | 0.0002346 | 0.001864 |
| Moon-Rahu Conjunction | Nifty 50 | 10 | 54 | 4.534 | 0.4212 | 4.113 | 70.37 | 3.615e-05 | 0.0004359 |
| Moon-Rahu Conjunction | Nifty 50 | 20 | 54 | 9.561 | 0.8264 | 8.735 | 79.63 | 1.838e-06 | 3.961e-05 |
| Moon-Rahu Conjunction | Nifty Bank | 1 | 54 | 0.6681 | 0.06023 | 0.6079 | 55.56 | 0.1507 | 0.2948 |
| Moon-Rahu Conjunction | Nifty Bank | 3 | 54 | 2.217 | 0.1819 | 2.035 | 61.11 | 0.006329 | 0.02577 |
| Moon-Rahu Conjunction | Nifty Bank | 5 | 54 | 3.366 | 0.3 | 3.066 | 68.52 | 0.001348 | 0.007413 |
| Moon-Rahu Conjunction | Nifty Bank | 10 | 54 | 5.855 | 0.5834 | 5.272 | 77.78 | 2.698e-05 | 0.0003501 |
| Moon-Rahu Conjunction | Nifty Bank | 20 | 54 | 9.341 | 1.172 | 8.168 | 79.63 | 4.694e-07 | 1.273e-05 |
| Moon-Rahu Conjunction | Nifty Midcap 100 | 1 | 54 | 0.2517 | 0.05397 | 0.1978 | 68.52 | 0.4527 | 0.6318 |
| Moon-Rahu Conjunction | Nifty Midcap 100 | 3 | 54 | -0.1034 | 0.1609 | -0.2642 | 37.04 | 0.2778 | 0.4548 |
| Moon-Rahu Conjunction | Nifty Midcap 100 | 5 | 54 | -0.1495 | 0.266 | -0.4155 | 40.74 | 0.221 | 0.3854 |
| Moon-Rahu Conjunction | Nifty Midcap 100 | 10 | 54 | 1.697 | 0.532 | 1.165 | 68.52 | 0.0446 | 0.1176 |
| Moon-Rahu Conjunction | Nifty Midcap 100 | 20 | 54 | 3.087 | 1.065 | 2.022 | 72.22 | 0.02273 | 0.07256 |
| Moon-Rahu Conjunction | Nifty Midcap 150 | 1 | 54 | 0.6174 | 0.05323 | 0.5641 | 61.11 | 0.1195 | 0.248 |
| Moon-Rahu Conjunction | Nifty Midcap 150 | 3 | 54 | 0.4227 | 0.1594 | 0.2633 | 61.11 | 0.5074 | 0.6827 |
| Moon-Rahu Conjunction | Nifty Midcap 150 | 5 | 54 | 0.7504 | 0.2642 | 0.4861 | 66.67 | 0.2911 | 0.466 |
| Moon-Rahu Conjunction | Nifty Midcap 150 | 10 | 54 | 2.245 | 0.5204 | 1.725 | 68.52 | 0.008525 | 0.03313 |
| Moon-Rahu Conjunction | Nifty Midcap 150 | 20 | 54 | 2.959 | 1.047 | 1.911 | 77.78 | 0.01624 | 0.05605 |
| Moon-Rahu Conjunction | BSE Sensex | 1 | 54 | 0.3825 | 0.05036 | 0.3322 | 57.41 | 0.3452 | 0.5249 |
| Moon-Rahu Conjunction | BSE Sensex | 3 | 54 | 0.4037 | 0.1513 | 0.2524 | 53.7 | 0.5266 | 0.6983 |
| Moon-Rahu Conjunction | BSE Sensex | 5 | 54 | 0.574 | 0.2506 | 0.3234 | 59.26 | 0.4728 | 0.6502 |
| Moon-Rahu Conjunction | BSE Sensex | 10 | 54 | 1.365 | 0.4957 | 0.869 | 57.41 | 0.1661 | 0.3178 |
| Moon-Rahu Conjunction | BSE Sensex | 20 | 54 | 2.296 | 1.002 | 1.294 | 68.52 | 0.1195 | 0.248 |
| Moon-Saturn Conjunction | Nifty 50 | 1 | 55 | 0.4719 | 0.04492 | 0.4269 | 60 | 0.002732 | 0.01299 |
| Moon-Saturn Conjunction | Nifty 50 | 3 | 55 | 1.745 | 0.1333 | 1.612 | 63.64 | 7.963e-05 | 0.0008204 |
| Moon-Saturn Conjunction | Nifty 50 | 5 | 55 | 2.861 | 0.2178 | 2.643 | 63.64 | 0.000169 | 0.001484 |
| Moon-Saturn Conjunction | Nifty 50 | 10 | 55 | 3.744 | 0.4212 | 3.323 | 60 | 0.0002499 | 0.00196 |
| Moon-Saturn Conjunction | Nifty 50 | 20 | 55 | 7.964 | 0.8264 | 7.138 | 70.91 | 5.685e-05 | 0.0006363 |
| Moon-Saturn Conjunction | Nifty Bank | 1 | 55 | 0.9894 | 0.06023 | 0.9292 | 65.45 | 0.0002847 | 0.002179 |
| Moon-Saturn Conjunction | Nifty Bank | 3 | 55 | 2.391 | 0.1819 | 2.209 | 65.45 | 9.48e-05 | 0.0009429 |
| Moon-Saturn Conjunction | Nifty Bank | 5 | 55 | 3.458 | 0.3 | 3.158 | 63.64 | 0.0002047 | 0.0017 |
| Moon-Saturn Conjunction | Nifty Bank | 10 | 55 | 4.714 | 0.5834 | 4.131 | 67.27 | 0.0004118 | 0.002947 |
| Moon-Saturn Conjunction | Nifty Bank | 20 | 55 | 6.738 | 1.172 | 5.566 | 70.91 | 0.0006682 | 0.004278 |
| Moon-Saturn Conjunction | Nifty Midcap 100 | 1 | 55 | 0.06375 | 0.05397 | 0.00978 | 69.09 | 0.9466 | 0.9787 |
| Moon-Saturn Conjunction | Nifty Midcap 100 | 3 | 55 | 0.1366 | 0.1609 | -0.02421 | 36.36 | 0.9151 | 0.9623 |
| Moon-Saturn Conjunction | Nifty Midcap 100 | 5 | 55 | -0.407 | 0.266 | -0.6731 | 29.09 | 0.114 | 0.239 |
| Moon-Saturn Conjunction | Nifty Midcap 100 | 10 | 55 | 1.216 | 0.532 | 0.6837 | 65.45 | 0.2821 | 0.4582 |
| Moon-Saturn Conjunction | Nifty Midcap 100 | 20 | 55 | 2.566 | 1.065 | 1.501 | 74.55 | 0.0662 | 0.1591 |
| Moon-Saturn Conjunction | Nifty Midcap 150 | 1 | 55 | 0.4573 | 0.05323 | 0.404 | 60 | 0.02021 | 0.06641 |
| Moon-Saturn Conjunction | Nifty Midcap 150 | 3 | 55 | 0.2098 | 0.1594 | 0.05037 | 60 | 0.7817 | 0.8761 |
| Moon-Saturn Conjunction | Nifty Midcap 150 | 5 | 55 | 0.3401 | 0.2642 | 0.07588 | 60 | 0.7964 | 0.8854 |
| Moon-Saturn Conjunction | Nifty Midcap 150 | 10 | 55 | 1.111 | 0.5204 | 0.5909 | 54.55 | 0.2326 | 0.3986 |
| Moon-Saturn Conjunction | Nifty Midcap 150 | 20 | 55 | 1.221 | 1.047 | 0.174 | 67.27 | 0.7835 | 0.8768 |
| Moon-Saturn Conjunction | BSE Sensex | 1 | 55 | 0.1297 | 0.05036 | 0.07934 | 50.91 | 0.6586 | 0.7965 |
| Moon-Saturn Conjunction | BSE Sensex | 3 | 55 | 0.2093 | 0.1513 | 0.05802 | 50.91 | 0.8072 | 0.8916 |
| Moon-Saturn Conjunction | BSE Sensex | 5 | 55 | 0.2483 | 0.2506 | -0.002271 | 54.55 | 0.9948 | 0.9976 |
| Moon-Saturn Conjunction | BSE Sensex | 10 | 55 | 0.1149 | 0.4957 | -0.3807 | 47.27 | 0.3825 | 0.5648 |
| Moon-Saturn Conjunction | BSE Sensex | 20 | 55 | 0.6552 | 1.002 | -0.3465 | 54.55 | 0.6226 | 0.77 |
| Moon-Sun Conjunction | Nifty 50 | 1 | 60 | 0.6829 | 0.04492 | 0.638 | 71.67 | 7.707e-05 | 0.0008006 |
| Moon-Sun Conjunction | Nifty 50 | 3 | 60 | 2.138 | 0.1333 | 2.005 | 70 | 4.735e-06 | 8.662e-05 |
| Moon-Sun Conjunction | Nifty 50 | 5 | 60 | 3.242 | 0.2178 | 3.025 | 73.33 | 1.237e-05 | 0.000191 |
| Moon-Sun Conjunction | Nifty 50 | 10 | 60 | 4.162 | 0.4212 | 3.741 | 73.33 | 0.0001869 | 0.0016 |
| Moon-Sun Conjunction | Nifty 50 | 20 | 60 | 8.173 | 0.8264 | 7.347 | 70 | 3.64e-05 | 0.0004375 |
| Moon-Sun Conjunction | Nifty Bank | 1 | 60 | 1.117 | 0.06023 | 1.057 | 71.67 | 2.181e-05 | 0.0003029 |
| Moon-Sun Conjunction | Nifty Bank | 3 | 60 | 2.97 | 0.1819 | 2.788 | 75 | 1.951e-06 | 4.156e-05 |
| Moon-Sun Conjunction | Nifty Bank | 5 | 60 | 3.836 | 0.3 | 3.536 | 76.67 | 7.706e-06 | 0.0001267 |
| Moon-Sun Conjunction | Nifty Bank | 10 | 60 | 5.392 | 0.5834 | 4.809 | 70 | 2.668e-05 | 0.0003499 |
| Moon-Sun Conjunction | Nifty Bank | 20 | 60 | 7.353 | 1.172 | 6.181 | 71.67 | 8.017e-05 | 0.0008237 |
| Moon-Sun Conjunction | Nifty Midcap 100 | 1 | 60 | 0.4241 | 0.05397 | 0.3702 | 75 | 0.003094 | 0.01438 |
| Moon-Sun Conjunction | Nifty Midcap 100 | 3 | 60 | 0.2554 | 0.1609 | 0.09458 | 48.33 | 0.7661 | 0.8679 |
| Moon-Sun Conjunction | Nifty Midcap 100 | 5 | 60 | -0.0258 | 0.266 | -0.2918 | 43.33 | 0.4967 | 0.6739 |
| Moon-Sun Conjunction | Nifty Midcap 100 | 10 | 60 | 1.274 | 0.532 | 0.7423 | 66.67 | 0.2896 | 0.4644 |
| Moon-Sun Conjunction | Nifty Midcap 100 | 20 | 60 | 2.851 | 1.065 | 1.787 | 68.33 | 0.02364 | 0.07462 |
| Moon-Sun Conjunction | Nifty Midcap 150 | 1 | 60 | 0.7801 | 0.05323 | 0.7269 | 71.67 | 3.244e-05 | 0.0004055 |
| Moon-Sun Conjunction | Nifty Midcap 150 | 3 | 60 | 0.7845 | 0.1594 | 0.6251 | 71.67 | 0.03171 | 0.09226 |
| Moon-Sun Conjunction | Nifty Midcap 150 | 5 | 60 | 1.023 | 0.2642 | 0.7587 | 75 | 0.04266 | 0.1137 |
| Moon-Sun Conjunction | Nifty Midcap 150 | 10 | 60 | 1.98 | 0.5204 | 1.459 | 70 | 0.03861 | 0.1063 |
| Moon-Sun Conjunction | Nifty Midcap 150 | 20 | 60 | 2.271 | 1.047 | 1.223 | 73.33 | 0.1304 | 0.2649 |
| Moon-Sun Conjunction | BSE Sensex | 1 | 60 | 0.3441 | 0.05036 | 0.2938 | 53.33 | 0.1138 | 0.2388 |
| Moon-Sun Conjunction | BSE Sensex | 3 | 60 | 0.7824 | 0.1513 | 0.631 | 58.33 | 0.06382 | 0.1552 |
| Moon-Sun Conjunction | BSE Sensex | 5 | 60 | 0.5628 | 0.2506 | 0.3123 | 60 | 0.4506 | 0.6302 |
| Moon-Sun Conjunction | BSE Sensex | 10 | 60 | 0.5725 | 0.4957 | 0.07681 | 65 | 0.9129 | 0.9608 |
| Moon-Sun Conjunction | BSE Sensex | 20 | 60 | 0.6197 | 1.002 | -0.3819 | 58.33 | 0.6545 | 0.7938 |
| Moon-Venus Conjunction | Nifty 50 | 1 | 44 | 0.1146 | 0.04492 | 0.06964 | 63.64 | 0.6769 | 0.8085 |
| Moon-Venus Conjunction | Nifty 50 | 3 | 44 | 1.066 | 0.1333 | 0.933 | 61.36 | 0.02795 | 0.08413 |
| Moon-Venus Conjunction | Nifty 50 | 5 | 44 | 1.757 | 0.2178 | 1.539 | 61.36 | 0.03053 | 0.08979 |
| Moon-Venus Conjunction | Nifty 50 | 10 | 44 | 2.614 | 0.4212 | 2.193 | 68.18 | 0.01806 | 0.06139 |
| Moon-Venus Conjunction | Nifty 50 | 20 | 44 | 5.147 | 0.8264 | 4.321 | 59.09 | 0.01675 | 0.05735 |
| Moon-Venus Conjunction | Nifty Bank | 1 | 44 | 0.3308 | 0.06023 | 0.2705 | 63.64 | 0.3158 | 0.4932 |
| Moon-Venus Conjunction | Nifty Bank | 3 | 44 | 1.406 | 0.1819 | 1.224 | 70.45 | 0.02906 | 0.0869 |
| Moon-Venus Conjunction | Nifty Bank | 5 | 44 | 1.912 | 0.3 | 1.612 | 56.82 | 0.05582 | 0.14 |
| Moon-Venus Conjunction | Nifty Bank | 10 | 44 | 3.244 | 0.5834 | 2.66 | 56.82 | 0.02143 | 0.0694 |
| Moon-Venus Conjunction | Nifty Bank | 20 | 44 | 3.804 | 1.172 | 2.632 | 56.82 | 0.1246 | 0.2563 |
| Moon-Venus Conjunction | Nifty Midcap 100 | 1 | 44 | 0.06064 | 0.05397 | 0.006677 | 50 | 0.9805 | 0.9923 |
| Moon-Venus Conjunction | Nifty Midcap 100 | 3 | 44 | -0.1054 | 0.1609 | -0.2663 | 34.09 | 0.4981 | 0.6746 |
| Moon-Venus Conjunction | Nifty Midcap 100 | 5 | 44 | -0.2711 | 0.266 | -0.5371 | 36.36 | 0.3173 | 0.4943 |
| Moon-Venus Conjunction | Nifty Midcap 100 | 10 | 44 | 0.7912 | 0.532 | 0.2592 | 59.09 | 0.7331 | 0.8454 |
| Moon-Venus Conjunction | Nifty Midcap 100 | 20 | 44 | 1.667 | 1.065 | 0.602 | 65.91 | 0.55 | 0.7161 |
| Moon-Venus Conjunction | Nifty Midcap 150 | 1 | 44 | 0.1607 | 0.05323 | 0.1074 | 61.36 | 0.551 | 0.717 |
| Moon-Venus Conjunction | Nifty Midcap 150 | 3 | 44 | 0.02396 | 0.1594 | -0.1355 | 61.36 | 0.5467 | 0.7146 |
| Moon-Venus Conjunction | Nifty Midcap 150 | 5 | 44 | 0.03826 | 0.2642 | -0.226 | 61.36 | 0.494 | 0.6724 |
| Moon-Venus Conjunction | Nifty Midcap 150 | 10 | 44 | 0.8751 | 0.5204 | 0.3547 | 68.18 | 0.5051 | 0.6806 |
| Moon-Venus Conjunction | Nifty Midcap 150 | 20 | 44 | 0.4841 | 1.047 | -0.5633 | 54.55 | 0.4288 | 0.6103 |
| Moon-Venus Conjunction | BSE Sensex | 1 | 44 | 0.02795 | 0.05036 | -0.02241 | 61.36 | 0.9207 | 0.9658 |
| Moon-Venus Conjunction | BSE Sensex | 3 | 44 | 0.1218 | 0.1513 | -0.0295 | 56.82 | 0.9171 | 0.963 |
| Moon-Venus Conjunction | BSE Sensex | 5 | 44 | -0.1416 | 0.2506 | -0.3922 | 50 | 0.322 | 0.4997 |
| Moon-Venus Conjunction | BSE Sensex | 10 | 44 | 0.1364 | 0.4957 | -0.3592 | 61.36 | 0.4568 | 0.6348 |
| Moon-Venus Conjunction | BSE Sensex | 20 | 44 | 0.03092 | 1.002 | -0.9707 | 50 | 0.24 | 0.4079 |
| Rahu-Saturn Conjunction | Nifty 50 | 1 | 3 | 0.5852 | 0.04492 | 0.5403 | 100 | 0.209 | 0.3711 |
| Rahu-Saturn Conjunction | Nifty 50 | 3 | 3 | 2.228 | 0.1333 | 2.095 | 66.67 | 0.4717 | 0.6494 |
| Rahu-Saturn Conjunction | Nifty 50 | 5 | 3 | 4.878 | 0.2178 | 4.66 | 100 | 0.2208 | 0.3854 |
| Rahu-Saturn Conjunction | Nifty 50 | 10 | 3 | 6.531 | 0.4212 | 6.11 | 100 | 0.1934 | 0.3521 |
| Rahu-Saturn Conjunction | Nifty 50 | 20 | 3 | 12.72 | 0.8264 | 11.89 | 100 | 0.2199 | 0.3853 |
| Rahu-Saturn Conjunction | Nifty Bank | 1 | 3 | 1.31 | 0.06023 | 1.25 | 100 | 0.1877 | 0.345 |
| Rahu-Saturn Conjunction | Nifty Bank | 3 | 3 | 2.71 | 0.1819 | 2.529 | 66.67 | 0.5634 | 0.7258 |
| Rahu-Saturn Conjunction | Nifty Bank | 5 | 3 | 6.013 | 0.3 | 5.713 | 100 | 0.1737 | 0.3269 |
| Rahu-Saturn Conjunction | Nifty Bank | 10 | 3 | 7.678 | 0.5834 | 7.095 | 100 | 0.2305 | 0.3963 |
| Rahu-Saturn Conjunction | Nifty Bank | 20 | 3 | 12.1 | 1.172 | 10.93 | 100 | 0.1736 | 0.3269 |
| Rahu-Saturn Conjunction | Nifty Midcap 100 | 1 | 3 | -0.07756 | 0.05397 | -0.1315 | 66.67 | 0.4553 | 0.6341 |
| Rahu-Saturn Conjunction | Nifty Midcap 100 | 3 | 3 | 0.7262 | 0.1609 | 0.5653 | 33.33 | 0.6049 | 0.7556 |
| Rahu-Saturn Conjunction | Nifty Midcap 100 | 5 | 3 | 2.752 | 0.266 | 2.486 | 66.67 | 0.3334 | 0.512 |
| Rahu-Saturn Conjunction | Nifty Midcap 100 | 10 | 3 | 5.628 | 0.532 | 5.096 | 100 | 0.03604 | 0.1015 |
| Rahu-Saturn Conjunction | Nifty Midcap 100 | 20 | 3 | 9.488 | 1.065 | 8.423 | 100 | 0.09772 | 0.2129 |
| Rahu-Saturn Conjunction | Nifty Midcap 150 | 1 | 3 | 0.7813 | 0.05323 | 0.728 | 100 | 0.2675 | 0.4421 |
| Rahu-Saturn Conjunction | Nifty Midcap 150 | 3 | 3 | 0.5901 | 0.1594 | 0.4307 | 66.67 | 0.8133 | 0.8962 |
| Rahu-Saturn Conjunction | Nifty Midcap 150 | 5 | 3 | 2.19 | 0.2642 | 1.926 | 100 | 0.2122 | 0.3749 |
| Rahu-Saturn Conjunction | Nifty Midcap 150 | 10 | 3 | 4.09 | 0.5204 | 3.57 | 100 | 0.05034 | 0.1289 |
| Rahu-Saturn Conjunction | Nifty Midcap 150 | 20 | 3 | 5.61 | 1.047 | 4.562 | 100 | 0.01931 | 0.06459 |
| Rahu-Saturn Conjunction | BSE Sensex | 1 | 3 | -0.2274 | 0.05036 | -0.2778 | 66.67 | 0.651 | 0.7932 |
| Rahu-Saturn Conjunction | BSE Sensex | 3 | 3 | 1.416 | 0.1513 | 1.265 | 66.67 | 0.576 | 0.7342 |
| Rahu-Saturn Conjunction | BSE Sensex | 5 | 3 | 2.076 | 0.2506 | 1.826 | 100 | 0.2759 | 0.453 |
| Rahu-Saturn Conjunction | BSE Sensex | 10 | 3 | 2.271 | 0.4957 | 1.776 | 100 | 0.2999 | 0.4757 |
| Rahu-Saturn Conjunction | BSE Sensex | 20 | 3 | 4.494 | 1.002 | 3.492 | 100 | 0.1728 | 0.3265 |
| Rahu-Sun Conjunction | Nifty 50 | 1 | 28 | 0.3973 | 0.04492 | 0.3524 | 75 | 0.0611 | 0.1507 |
| Rahu-Sun Conjunction | Nifty 50 | 3 | 28 | 1.514 | 0.1333 | 1.38 | 67.86 | 0.02618 | 0.08 |
| Rahu-Sun Conjunction | Nifty 50 | 5 | 28 | 2.879 | 0.2178 | 2.661 | 71.43 | 0.008166 | 0.03186 |
| Rahu-Sun Conjunction | Nifty 50 | 10 | 28 | 3.547 | 0.4212 | 3.126 | 67.86 | 0.02223 | 0.07144 |
| Rahu-Sun Conjunction | Nifty 50 | 20 | 28 | 6.976 | 0.8264 | 6.15 | 64.29 | 0.02145 | 0.0694 |
| Rahu-Sun Conjunction | Nifty Bank | 1 | 28 | 0.8199 | 0.06023 | 0.7596 | 71.43 | 0.0136 | 0.04866 |
| Rahu-Sun Conjunction | Nifty Bank | 3 | 28 | 1.683 | 0.1819 | 1.501 | 60.71 | 0.0671 | 0.1606 |
| Rahu-Sun Conjunction | Nifty Bank | 5 | 28 | 2.757 | 0.3 | 2.457 | 60.71 | 0.04552 | 0.1196 |
| Rahu-Sun Conjunction | Nifty Bank | 10 | 28 | 3.715 | 0.5834 | 3.132 | 57.14 | 0.08671 | 0.1941 |
| Rahu-Sun Conjunction | Nifty Bank | 20 | 28 | 4.898 | 1.172 | 3.725 | 60.71 | 0.1771 | 0.3312 |
| Rahu-Sun Conjunction | Nifty Midcap 100 | 1 | 28 | 0.2018 | 0.05397 | 0.1478 | 64.29 | 0.4425 | 0.6228 |
| Rahu-Sun Conjunction | Nifty Midcap 100 | 3 | 28 | 0.2713 | 0.1609 | 0.1105 | 39.29 | 0.8151 | 0.897 |
| Rahu-Sun Conjunction | Nifty Midcap 100 | 5 | 28 | 0.4431 | 0.266 | 0.1771 | 42.86 | 0.7556 | 0.8594 |
| Rahu-Sun Conjunction | Nifty Midcap 100 | 10 | 28 | 1.258 | 0.532 | 0.7264 | 57.14 | 0.2593 | 0.4321 |
| Rahu-Sun Conjunction | Nifty Midcap 100 | 20 | 28 | 1.675 | 1.065 | 0.6107 | 53.57 | 0.6033 | 0.7549 |
| Rahu-Sun Conjunction | Nifty Midcap 150 | 1 | 28 | 0.6013 | 0.05323 | 0.5481 | 67.86 | 0.0268 | 0.08158 |
| Rahu-Sun Conjunction | Nifty Midcap 150 | 3 | 28 | 0.2696 | 0.1594 | 0.1102 | 67.86 | 0.7518 | 0.8574 |
| Rahu-Sun Conjunction | Nifty Midcap 150 | 5 | 28 | 0.6559 | 0.2642 | 0.3916 | 71.43 | 0.4065 | 0.5885 |
| Rahu-Sun Conjunction | Nifty Midcap 150 | 10 | 28 | 1.319 | 0.5204 | 0.799 | 67.86 | 0.325 | 0.503 |
| Rahu-Sun Conjunction | Nifty Midcap 150 | 20 | 28 | 0.9875 | 1.047 | -0.05999 | 64.29 | 0.9576 | 0.9826 |
| Rahu-Sun Conjunction | BSE Sensex | 1 | 28 | 0.3079 | 0.05036 | 0.2575 | 57.14 | 0.2614 | 0.4342 |
| Rahu-Sun Conjunction | BSE Sensex | 3 | 28 | -0.02223 | 0.1513 | -0.1735 | 57.14 | 0.677 | 0.8085 |
| Rahu-Sun Conjunction | BSE Sensex | 5 | 28 | -0.3074 | 0.2506 | -0.558 | 53.57 | 0.3967 | 0.5802 |
| Rahu-Sun Conjunction | BSE Sensex | 10 | 28 | -0.9883 | 0.4957 | -1.484 | 46.43 | 0.164 | 0.3154 |
| Rahu-Sun Conjunction | BSE Sensex | 20 | 28 | -0.8461 | 1.002 | -1.848 | 50 | 0.1802 | 0.3345 |
| Rahu-Venus Conjunction | Nifty 50 | 1 | 30 | -0.005244 | 0.04492 | -0.05017 | 53.33 | 0.7956 | 0.8851 |
| Rahu-Venus Conjunction | Nifty 50 | 3 | 30 | 0.7642 | 0.1333 | 0.631 | 53.33 | 0.3165 | 0.4937 |
| Rahu-Venus Conjunction | Nifty 50 | 5 | 30 | 1.567 | 0.2178 | 1.349 | 50 | 0.1939 | 0.3523 |
| Rahu-Venus Conjunction | Nifty 50 | 10 | 30 | 3.353 | 0.4212 | 2.932 | 70 | 0.01931 | 0.06459 |
| Rahu-Venus Conjunction | Nifty 50 | 20 | 30 | 6.568 | 0.8264 | 5.741 | 73.33 | 0.01999 | 0.06609 |
| Rahu-Venus Conjunction | Nifty Bank | 1 | 30 | 0.3211 | 0.06023 | 0.2609 | 56.67 | 0.4142 | 0.5961 |
| Rahu-Venus Conjunction | Nifty Bank | 3 | 30 | 1.118 | 0.1819 | 0.9359 | 60 | 0.2736 | 0.4502 |
| Rahu-Venus Conjunction | Nifty Bank | 5 | 30 | 1.924 | 0.3 | 1.624 | 53.33 | 0.1861 | 0.3428 |
| Rahu-Venus Conjunction | Nifty Bank | 10 | 30 | 4.431 | 0.5834 | 3.848 | 63.33 | 0.01423 | 0.04996 |
| Rahu-Venus Conjunction | Nifty Bank | 20 | 30 | 5.844 | 1.172 | 4.671 | 63.33 | 0.04002 | 0.1085 |
| Rahu-Venus Conjunction | Nifty Midcap 100 | 1 | 30 | -0.3858 | 0.05397 | -0.4397 | 56.67 | 0.09092 | 0.202 |
| Rahu-Venus Conjunction | Nifty Midcap 100 | 3 | 30 | -0.6843 | 0.1609 | -0.8452 | 33.33 | 0.09698 | 0.2118 |
| Rahu-Venus Conjunction | Nifty Midcap 100 | 5 | 30 | -1.225 | 0.266 | -1.492 | 26.67 | 0.02972 | 0.08817 |
| Rahu-Venus Conjunction | Nifty Midcap 100 | 10 | 30 | 1.197 | 0.532 | 0.665 | 66.67 | 0.2895 | 0.4643 |
| Rahu-Venus Conjunction | Nifty Midcap 100 | 20 | 30 | 1.451 | 1.065 | 0.3859 | 60 | 0.7176 | 0.8361 |
| Rahu-Venus Conjunction | Nifty Midcap 150 | 1 | 30 | 0.06029 | 0.05323 | 0.007059 | 46.67 | 0.9747 | 0.9897 |
| Rahu-Venus Conjunction | Nifty Midcap 150 | 3 | 30 | -0.4789 | 0.1594 | -0.6383 | 53.33 | 0.07894 | 0.1811 |
| Rahu-Venus Conjunction | Nifty Midcap 150 | 5 | 30 | -0.7016 | 0.2642 | -0.9658 | 50 | 0.06261 | 0.1533 |
| Rahu-Venus Conjunction | Nifty Midcap 150 | 10 | 30 | 0.5682 | 0.5204 | 0.0478 | 63.33 | 0.9542 | 0.982 |
| Rahu-Venus Conjunction | Nifty Midcap 150 | 20 | 30 | -0.06972 | 1.047 | -1.117 | 66.67 | 0.3136 | 0.4908 |
| Rahu-Venus Conjunction | BSE Sensex | 1 | 30 | -0.3033 | 0.05036 | -0.3537 | 40 | 0.03536 | 0.1002 |
| Rahu-Venus Conjunction | BSE Sensex | 3 | 30 | -0.799 | 0.1513 | -0.9503 | 36.67 | 0.006836 | 0.02736 |
| Rahu-Venus Conjunction | BSE Sensex | 5 | 30 | -1.479 | 0.2506 | -1.73 | 26.67 | 0.001279 | 0.007175 |
| Rahu-Venus Conjunction | BSE Sensex | 10 | 30 | -0.9126 | 0.4957 | -1.408 | 53.33 | 0.113 | 0.2375 |
| Rahu-Venus Conjunction | BSE Sensex | 20 | 30 | -1.362 | 1.002 | -2.363 | 56.67 | 0.05136 | 0.1309 |
| Saturn-Sun Conjunction | Nifty 50 | 1 | 26 | 0.0395 | 0.04492 | -0.005425 | 61.54 | 0.9804 | 0.9923 |
| Saturn-Sun Conjunction | Nifty 50 | 3 | 26 | 1.426 | 0.1333 | 1.293 | 61.54 | 0.04518 | 0.119 |
| Saturn-Sun Conjunction | Nifty 50 | 5 | 26 | 2.748 | 0.2178 | 2.53 | 57.69 | 0.01664 | 0.05708 |
| Saturn-Sun Conjunction | Nifty 50 | 10 | 26 | 3.781 | 0.4212 | 3.36 | 65.38 | 0.0195 | 0.065 |
| Saturn-Sun Conjunction | Nifty 50 | 20 | 26 | 7.252 | 0.8264 | 6.425 | 65.38 | 0.02204 | 0.07096 |
| Saturn-Sun Conjunction | Nifty Bank | 1 | 26 | 0.1344 | 0.06023 | 0.07413 | 53.85 | 0.8391 | 0.9128 |
| Saturn-Sun Conjunction | Nifty Bank | 3 | 26 | 1.745 | 0.1819 | 1.563 | 53.85 | 0.06215 | 0.1525 |
| Saturn-Sun Conjunction | Nifty Bank | 5 | 26 | 3.333 | 0.3 | 3.033 | 57.69 | 0.0166 | 0.05701 |
| Saturn-Sun Conjunction | Nifty Bank | 10 | 26 | 5.175 | 0.5834 | 4.591 | 65.38 | 0.01151 | 0.04268 |
| Saturn-Sun Conjunction | Nifty Bank | 20 | 26 | 6.921 | 1.172 | 5.749 | 65.38 | 0.02226 | 0.07146 |
| Saturn-Sun Conjunction | Nifty Midcap 100 | 1 | 26 | -0.03673 | 0.05397 | -0.0907 | 61.54 | 0.6517 | 0.7932 |
| Saturn-Sun Conjunction | Nifty Midcap 100 | 3 | 26 | -0.21 | 0.1609 | -0.3709 | 34.62 | 0.1904 | 0.3482 |
| Saturn-Sun Conjunction | Nifty Midcap 100 | 5 | 26 | -0.1789 | 0.266 | -0.4449 | 26.92 | 0.1832 | 0.339 |
| Saturn-Sun Conjunction | Nifty Midcap 100 | 10 | 26 | 1.219 | 0.532 | 0.6868 | 69.23 | 0.4095 | 0.5909 |
| Saturn-Sun Conjunction | Nifty Midcap 100 | 20 | 26 | 0.3475 | 1.065 | -0.7173 | 61.54 | 0.6096 | 0.7591 |
| Saturn-Sun Conjunction | Nifty Midcap 150 | 1 | 26 | 0.1146 | 0.05323 | 0.06133 | 57.69 | 0.8118 | 0.8953 |
| Saturn-Sun Conjunction | Nifty Midcap 150 | 3 | 26 | 0.1086 | 0.1594 | -0.05081 | 61.54 | 0.881 | 0.9396 |
| Saturn-Sun Conjunction | Nifty Midcap 150 | 5 | 26 | 0.5266 | 0.2642 | 0.2623 | 61.54 | 0.5672 | 0.7282 |
| Saturn-Sun Conjunction | Nifty Midcap 150 | 10 | 26 | 1.713 | 0.5204 | 1.193 | 65.38 | 0.1805 | 0.3349 |
| Saturn-Sun Conjunction | Nifty Midcap 150 | 20 | 26 | 1.483 | 1.047 | 0.4357 | 69.23 | 0.7104 | 0.8312 |
| Saturn-Sun Conjunction | BSE Sensex | 1 | 26 | -0.1205 | 0.05036 | -0.1709 | 53.85 | 0.6003 | 0.7527 |
| Saturn-Sun Conjunction | BSE Sensex | 3 | 26 | 0.06223 | 0.1513 | -0.08908 | 61.54 | 0.8386 | 0.9128 |
| Saturn-Sun Conjunction | BSE Sensex | 5 | 26 | 0.2441 | 0.2506 | -0.006433 | 50 | 0.9905 | 0.9964 |
| Saturn-Sun Conjunction | BSE Sensex | 10 | 26 | 0.0981 | 0.4957 | -0.3976 | 53.85 | 0.679 | 0.8099 |
| Saturn-Sun Conjunction | BSE Sensex | 20 | 26 | 0.4597 | 1.002 | -0.5419 | 61.54 | 0.6568 | 0.7953 |
| Saturn-Venus Conjunction | Nifty 50 | 1 | 30 | 0.3908 | 0.04492 | 0.3459 | 56.67 | 0.1304 | 0.2649 |
| Saturn-Venus Conjunction | Nifty 50 | 3 | 30 | 1.38 | 0.1333 | 1.247 | 60 | 0.05215 | 0.1323 |
| Saturn-Venus Conjunction | Nifty 50 | 5 | 30 | 2.731 | 0.2178 | 2.513 | 63.33 | 0.01688 | 0.05765 |
| Saturn-Venus Conjunction | Nifty 50 | 10 | 30 | 3.998 | 0.4212 | 3.577 | 76.67 | 0.007654 | 0.03031 |
| Saturn-Venus Conjunction | Nifty 50 | 20 | 30 | 8.568 | 0.8264 | 7.742 | 66.67 | 0.001592 | 0.008505 |
| Saturn-Venus Conjunction | Nifty Bank | 1 | 30 | 0.9045 | 0.06023 | 0.8443 | 70 | 0.04406 | 0.1165 |
| Saturn-Venus Conjunction | Nifty Bank | 3 | 30 | 1.46 | 0.1819 | 1.278 | 63.33 | 0.1553 | 0.3021 |
| Saturn-Venus Conjunction | Nifty Bank | 5 | 30 | 2.917 | 0.3 | 2.617 | 66.67 | 0.03937 | 0.1074 |
| Saturn-Venus Conjunction | Nifty Bank | 10 | 30 | 5.214 | 0.5834 | 4.63 | 70 | 0.005108 | 0.02167 |
| Saturn-Venus Conjunction | Nifty Bank | 20 | 30 | 8.283 | 1.172 | 7.111 | 76.67 | 0.0007761 | 0.004835 |
| Saturn-Venus Conjunction | Nifty Midcap 100 | 1 | 30 | -0.2881 | 0.05397 | -0.342 | 50 | 0.0374 | 0.1042 |
| Saturn-Venus Conjunction | Nifty Midcap 100 | 3 | 30 | -0.03122 | 0.1609 | -0.1921 | 40 | 0.3959 | 0.5794 |
| Saturn-Venus Conjunction | Nifty Midcap 100 | 5 | 30 | 0.02448 | 0.266 | -0.2415 | 43.33 | 0.42 | 0.6018 |
| Saturn-Venus Conjunction | Nifty Midcap 100 | 10 | 30 | 1.803 | 0.532 | 1.271 | 70 | 0.06313 | 0.1544 |
| Saturn-Venus Conjunction | Nifty Midcap 100 | 20 | 30 | 2.389 | 1.065 | 1.324 | 63.33 | 0.2594 | 0.4321 |
| Saturn-Venus Conjunction | Nifty Midcap 150 | 1 | 30 | 0.4462 | 0.05323 | 0.393 | 60 | 0.1138 | 0.2388 |
| Saturn-Venus Conjunction | Nifty Midcap 150 | 3 | 30 | -0.3902 | 0.1594 | -0.5496 | 66.67 | 0.1962 | 0.3552 |
| Saturn-Venus Conjunction | Nifty Midcap 150 | 5 | 30 | -0.01546 | 0.2642 | -0.2797 | 60 | 0.6515 | 0.7932 |
| Saturn-Venus Conjunction | Nifty Midcap 150 | 10 | 30 | 1.32 | 0.5204 | 0.7994 | 66.67 | 0.3273 | 0.5054 |
| Saturn-Venus Conjunction | Nifty Midcap 150 | 20 | 30 | 2.042 | 1.047 | 0.9945 | 66.67 | 0.1758 | 0.33 |
| Saturn-Venus Conjunction | BSE Sensex | 1 | 30 | -0.0581 | 0.05036 | -0.1085 | 43.33 | 0.645 | 0.7892 |
| Saturn-Venus Conjunction | BSE Sensex | 3 | 30 | -0.6127 | 0.1513 | -0.764 | 53.33 | 0.09259 | 0.205 |
| Saturn-Venus Conjunction | BSE Sensex | 5 | 30 | -0.3058 | 0.2506 | -0.5563 | 50 | 0.3552 | 0.5353 |
| Saturn-Venus Conjunction | BSE Sensex | 10 | 30 | 0.1888 | 0.4957 | -0.3069 | 56.67 | 0.6817 | 0.8118 |
| Saturn-Venus Conjunction | BSE Sensex | 20 | 30 | 1.604 | 1.002 | 0.6027 | 56.67 | 0.4741 | 0.6518 |
| Sun-Venus Conjunction | Nifty 50 | 1 | 34 | 0.5219 | 0.04492 | 0.477 | 70.59 | 0.03269 | 0.0946 |
| Sun-Venus Conjunction | Nifty 50 | 3 | 34 | 2.119 | 0.1333 | 1.986 | 76.47 | 0.0002701 | 0.002097 |
| Sun-Venus Conjunction | Nifty 50 | 5 | 34 | 3.501 | 0.2178 | 3.284 | 76.47 | 0.0003889 | 0.002821 |
| Sun-Venus Conjunction | Nifty 50 | 10 | 33 | 3.898 | 0.4212 | 3.477 | 60.61 | 0.006443 | 0.02618 |
| Sun-Venus Conjunction | Nifty 50 | 20 | 33 | 8.863 | 0.8264 | 8.037 | 72.73 | 0.0009321 | 0.005522 |
| Sun-Venus Conjunction | Nifty Bank | 1 | 34 | 0.6598 | 0.06023 | 0.5996 | 61.76 | 0.1428 | 0.2834 |
| Sun-Venus Conjunction | Nifty Bank | 3 | 34 | 2.308 | 0.1819 | 2.126 | 70.59 | 0.003203 | 0.01481 |
| Sun-Venus Conjunction | Nifty Bank | 5 | 34 | 3.384 | 0.3 | 3.084 | 61.76 | 0.004266 | 0.01865 |
| Sun-Venus Conjunction | Nifty Bank | 10 | 33 | 4.801 | 0.5834 | 4.217 | 66.67 | 0.00802 | 0.03152 |
| Sun-Venus Conjunction | Nifty Bank | 20 | 33 | 8.371 | 1.172 | 7.198 | 69.7 | 0.001414 | 0.007739 |
| Sun-Venus Conjunction | Nifty Midcap 100 | 1 | 34 | 0.5396 | 0.05397 | 0.4856 | 85.29 | 0.07727 | 0.1783 |
| Sun-Venus Conjunction | Nifty Midcap 100 | 3 | 34 | 0.8625 | 0.1609 | 0.7017 | 44.12 | 0.1736 | 0.3269 |
| Sun-Venus Conjunction | Nifty Midcap 100 | 5 | 34 | 1.051 | 0.266 | 0.7846 | 50 | 0.1437 | 0.2846 |
| Sun-Venus Conjunction | Nifty Midcap 100 | 10 | 33 | 1.428 | 0.532 | 0.8958 | 72.73 | 0.3078 | 0.4863 |
| Sun-Venus Conjunction | Nifty Midcap 100 | 20 | 33 | 2.353 | 1.065 | 1.289 | 69.7 | 0.3249 | 0.503 |
| Sun-Venus Conjunction | Nifty Midcap 150 | 1 | 34 | 0.4588 | 0.05323 | 0.4056 | 64.71 | 0.1174 | 0.2448 |
| Sun-Venus Conjunction | Nifty Midcap 150 | 3 | 34 | 0.5883 | 0.1594 | 0.4288 | 76.47 | 0.1717 | 0.3255 |
| Sun-Venus Conjunction | Nifty Midcap 150 | 5 | 34 | 1.147 | 0.2642 | 0.8824 | 76.47 | 0.06733 | 0.1609 |
| Sun-Venus Conjunction | Nifty Midcap 150 | 10 | 33 | 1.666 | 0.5204 | 1.145 | 63.64 | 0.1382 | 0.2762 |
| Sun-Venus Conjunction | Nifty Midcap 150 | 20 | 33 | 2.668 | 1.047 | 1.62 | 75.76 | 0.1139 | 0.2389 |
| Sun-Venus Conjunction | BSE Sensex | 1 | 34 | 0.08605 | 0.05036 | 0.03569 | 58.82 | 0.8865 | 0.9428 |
| Sun-Venus Conjunction | BSE Sensex | 3 | 34 | 0.515 | 0.1513 | 0.3637 | 64.71 | 0.2564 | 0.4294 |
| Sun-Venus Conjunction | BSE Sensex | 5 | 34 | 0.8256 | 0.2506 | 0.575 | 67.65 | 0.2387 | 0.4066 |
| Sun-Venus Conjunction | BSE Sensex | 10 | 33 | 0.3111 | 0.4957 | -0.1845 | 48.48 | 0.8173 | 0.8983 |
| Sun-Venus Conjunction | BSE Sensex | 20 | 33 | 2.154 | 1.002 | 1.152 | 63.64 | 0.295 | 0.4717 |

### Direct stations (Anuvakra)

* When Jupiter turned direct (24 events since 2001), Nifty 50 averaged +1.80% over the next 5 trading days (base rate +0.22%). Win rate 45.8%. That is +1.58 pp above the unconditional baseline. Not statistically significant (p=0.1799, q=0.3345 after Benjamini-Hochberg correction).
* When Jupiter turned direct (24 events since 2001), Nifty Bank averaged +2.24% over the next 5 trading days (base rate +0.30%). Win rate 50.0%. That is +1.94 pp above the unconditional baseline. Not statistically significant (p=0.1347, q=0.2718 after Benjamini-Hochberg correction).
* When Jupiter turned direct (24 events since 2001), Nifty Midcap 100 averaged -0.99% over the next 5 trading days (base rate +0.27%). Win rate 37.5%. That is -1.26 pp below the unconditional baseline. Nominally significant at p=0.04012, but it does not survive Benjamini-Hochberg correction (q=0.1087).
* When Jupiter turned direct (24 events since 2001), Nifty Midcap 150 averaged -0.79% over the next 5 trading days (base rate +0.26%). Win rate 41.7%. That is -1.06 pp below the unconditional baseline. Nominally significant at p=0.04366, but it does not survive Benjamini-Hochberg correction (q=0.1158).
* When Jupiter turned direct (24 events since 2001), BSE Sensex averaged -1.31% over the next 5 trading days (base rate +0.25%). Win rate 37.5%. That is -1.56 pp below the unconditional baseline. Statistically significant at p=0.006207 and after Benjamini-Hochberg correction (q=0.0254).

* When Mars turned direct (12 events since 2001), Nifty 50 averaged +2.47% over the next 5 trading days (base rate +0.22%). Win rate 66.7%. That is +2.26 pp above the unconditional baseline. Not statistically significant (p=0.1129, q=0.2375 after Benjamini-Hochberg correction).
* When Mars turned direct (12 events since 2001), Nifty Bank averaged +2.29% over the next 5 trading days (base rate +0.30%). Win rate 58.3%. That is +1.99 pp above the unconditional baseline. Not statistically significant (p=0.2281, q=0.394 after Benjamini-Hochberg correction).
* When Mars turned direct (12 events since 2001), Nifty Midcap 100 averaged +0.41% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.14 pp above the unconditional baseline. Not statistically significant (p=0.8525, q=0.9199 after Benjamini-Hochberg correction).
* When Mars turned direct (12 events since 2001), Nifty Midcap 150 averaged +0.45% over the next 5 trading days (base rate +0.26%). Win rate 66.7%. That is +0.19 pp above the unconditional baseline. Not statistically significant (p=0.6741, q=0.8079 after Benjamini-Hochberg correction).
* When Mars turned direct (12 events since 2001), BSE Sensex averaged +0.47% over the next 5 trading days (base rate +0.25%). Win rate 58.3%. That is +0.22 pp above the unconditional baseline. Not statistically significant (p=0.7375, q=0.8481 after Benjamini-Hochberg correction).

* When Mercury turned direct (84 events since 2000), Nifty 50 averaged +2.59% over the next 5 trading days (base rate +0.22%). Win rate 64.3%. That is +2.37 pp above the unconditional baseline. Statistically significant at p=0.0002308 and after Benjamini-Hochberg correction (q=0.001842).
* When Mercury turned direct (84 events since 2000), Nifty Bank averaged +2.65% over the next 5 trading days (base rate +0.30%). Win rate 63.1%. That is +2.35 pp above the unconditional baseline. Statistically significant at p=0.002853 and after Benjamini-Hochberg correction (q=0.01347).
* When Mercury turned direct (84 events since 2000), Nifty Midcap 100 averaged -0.13% over the next 5 trading days (base rate +0.27%). Win rate 42.9%. That is -0.40 pp below the unconditional baseline. Not statistically significant (p=0.3351, q=0.5142 after Benjamini-Hochberg correction).
* When Mercury turned direct (84 events since 2000), Nifty Midcap 150 averaged +0.25% over the next 5 trading days (base rate +0.26%). Win rate 64.3%. That is -0.01 pp below the unconditional baseline. Not statistically significant (p=0.9721, q=0.9892 after Benjamini-Hochberg correction).
* When Mercury turned direct (84 events since 2000), BSE Sensex averaged -0.17% over the next 5 trading days (base rate +0.25%). Win rate 52.4%. That is -0.42 pp below the unconditional baseline. Not statistically significant (p=0.3137, q=0.4908 after Benjamini-Hochberg correction).

* When Saturn turned direct (26 events since 2000), Nifty 50 averaged +3.51% over the next 5 trading days (base rate +0.22%). Win rate 69.2%. That is +3.30 pp above the unconditional baseline. Statistically significant at p=0.001739 and after Benjamini-Hochberg correction (q=0.009071).
* When Saturn turned direct (26 events since 2000), Nifty Bank averaged +4.33% over the next 5 trading days (base rate +0.30%). Win rate 69.2%. That is +4.03 pp above the unconditional baseline. Statistically significant at p=0.0009173 and after Benjamini-Hochberg correction (q=0.00546).
* When Saturn turned direct (26 events since 2000), Nifty Midcap 100 averaged +0.58% over the next 5 trading days (base rate +0.27%). Win rate 42.3%. That is +0.32 pp above the unconditional baseline. Not statistically significant (p=0.6867, q=0.8141 after Benjamini-Hochberg correction).
* When Saturn turned direct (26 events since 2000), Nifty Midcap 150 averaged +0.97% over the next 5 trading days (base rate +0.26%). Win rate 73.1%. That is +0.71 pp above the unconditional baseline. Not statistically significant (p=0.1198, q=0.2484 after Benjamini-Hochberg correction).
* When Saturn turned direct (26 events since 2000), BSE Sensex averaged +0.28% over the next 5 trading days (base rate +0.25%). Win rate 50.0%. That is +0.03 pp above the unconditional baseline. Not statistically significant (p=0.9641, q=0.9862 after Benjamini-Hochberg correction).

* When Venus turned direct (16 events since 2001), Nifty 50 averaged +4.14% over the next 5 trading days (base rate +0.22%). Win rate 81.2%. That is +3.92 pp above the unconditional baseline. Statistically significant at p=0.002333 and after Benjamini-Hochberg correction (q=0.01129).
* When Venus turned direct (16 events since 2001), Nifty Bank averaged +5.06% over the next 5 trading days (base rate +0.30%). Win rate 93.8%. That is +4.76 pp above the unconditional baseline. Statistically significant at p=0.00123 and after Benjamini-Hochberg correction (q=0.006989).
* When Venus turned direct (16 events since 2001), Nifty Midcap 100 averaged +1.06% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.79 pp above the unconditional baseline. Not statistically significant (p=0.2471, q=0.4167 after Benjamini-Hochberg correction).
* When Venus turned direct (16 events since 2001), Nifty Midcap 150 averaged +1.58% over the next 5 trading days (base rate +0.26%). Win rate 75.0%. That is +1.32 pp above the unconditional baseline. Nominally significant at p=0.0186, but it does not survive Benjamini-Hochberg correction (q=0.063).
* When Venus turned direct (16 events since 2001), BSE Sensex averaged +1.53% over the next 5 trading days (base rate +0.25%). Win rate 68.8%. That is +1.28 pp above the unconditional baseline. Not statistically significant (p=0.07394, q=0.1727 after Benjamini-Hochberg correction).

**All windows — Direct stations (Anuvakra)**

| Event | Index | Window | N | Mean ret | Base rate | Excess | Win % | p-value | q (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jupiter Direct Station | Nifty 50 | 1 | 24 | 0.3472 | 0.04492 | 0.3023 | 58.33 | 0.08259 | 0.1871 |
| Jupiter Direct Station | Nifty 50 | 3 | 24 | 1.09 | 0.1333 | 0.9567 | 41.67 | 0.1535 | 0.2996 |
| Jupiter Direct Station | Nifty 50 | 5 | 24 | 1.795 | 0.2178 | 1.578 | 45.83 | 0.1799 | 0.3345 |
| Jupiter Direct Station | Nifty 50 | 10 | 24 | 2.684 | 0.4212 | 2.263 | 58.33 | 0.131 | 0.266 |
| Jupiter Direct Station | Nifty 50 | 20 | 24 | 6.924 | 0.8264 | 6.097 | 62.5 | 0.0392 | 0.107 |
| Jupiter Direct Station | Nifty Bank | 1 | 24 | 0.8258 | 0.06023 | 0.7656 | 62.5 | 0.01582 | 0.05474 |
| Jupiter Direct Station | Nifty Bank | 3 | 24 | 1.778 | 0.1819 | 1.596 | 54.17 | 0.05446 | 0.1371 |
| Jupiter Direct Station | Nifty Bank | 5 | 24 | 2.244 | 0.3 | 1.944 | 50 | 0.1347 | 0.2718 |
| Jupiter Direct Station | Nifty Bank | 10 | 24 | 3.788 | 0.5834 | 3.205 | 58.33 | 0.07018 | 0.1661 |
| Jupiter Direct Station | Nifty Bank | 20 | 24 | 6.123 | 1.172 | 4.951 | 62.5 | 0.06011 | 0.1488 |
| Jupiter Direct Station | Nifty Midcap 100 | 1 | 24 | -0.0391 | 0.05397 | -0.09306 | 62.5 | 0.6551 | 0.7938 |
| Jupiter Direct Station | Nifty Midcap 100 | 3 | 24 | -0.5034 | 0.1609 | -0.6643 | 25 | 0.008619 | 0.03342 |
| Jupiter Direct Station | Nifty Midcap 100 | 5 | 24 | -0.994 | 0.266 | -1.26 | 37.5 | 0.04012 | 0.1087 |
| Jupiter Direct Station | Nifty Midcap 100 | 10 | 24 | 0.5388 | 0.532 | 0.006804 | 66.67 | 0.994 | 0.9976 |
| Jupiter Direct Station | Nifty Midcap 100 | 20 | 24 | 1.19 | 1.065 | 0.1256 | 70.83 | 0.9466 | 0.9787 |
| Jupiter Direct Station | Nifty Midcap 150 | 1 | 24 | 0.3923 | 0.05323 | 0.3391 | 58.33 | 0.1657 | 0.3173 |
| Jupiter Direct Station | Nifty Midcap 150 | 3 | 24 | -0.46 | 0.1594 | -0.6194 | 41.67 | 0.02595 | 0.07958 |
| Jupiter Direct Station | Nifty Midcap 150 | 5 | 24 | -0.7936 | 0.2642 | -1.058 | 41.67 | 0.04366 | 0.1158 |
| Jupiter Direct Station | Nifty Midcap 150 | 10 | 24 | -0.4197 | 0.5204 | -0.9401 | 45.83 | 0.2695 | 0.4448 |
| Jupiter Direct Station | Nifty Midcap 150 | 20 | 24 | 0.5301 | 1.047 | -0.5174 | 66.67 | 0.6652 | 0.8019 |
| Jupiter Direct Station | BSE Sensex | 1 | 24 | 0.03229 | 0.05036 | -0.01807 | 45.83 | 0.9387 | 0.9749 |
| Jupiter Direct Station | BSE Sensex | 3 | 24 | -0.599 | 0.1513 | -0.7503 | 29.17 | 0.009254 | 0.03541 |
| Jupiter Direct Station | BSE Sensex | 5 | 24 | -1.312 | 0.2506 | -1.563 | 37.5 | 0.006207 | 0.0254 |
| Jupiter Direct Station | BSE Sensex | 10 | 24 | -1.9 | 0.4957 | -2.395 | 37.5 | 0.003529 | 0.01606 |
| Jupiter Direct Station | BSE Sensex | 20 | 24 | -1.432 | 1.002 | -2.434 | 45.83 | 0.08141 | 0.185 |
| Mars Direct Station | Nifty 50 | 1 | 12 | 0.678 | 0.04492 | 0.6331 | 66.67 | 0.06917 | 0.1643 |
| Mars Direct Station | Nifty 50 | 3 | 12 | 2.284 | 0.1333 | 2.151 | 75 | 0.02499 | 0.07752 |
| Mars Direct Station | Nifty 50 | 5 | 12 | 2.474 | 0.2178 | 2.257 | 66.67 | 0.1129 | 0.2375 |
| Mars Direct Station | Nifty 50 | 10 | 12 | 3.663 | 0.4212 | 3.242 | 75 | 0.08019 | 0.1831 |
| Mars Direct Station | Nifty 50 | 20 | 12 | 7.652 | 0.8264 | 6.825 | 75 | 0.07086 | 0.1673 |
| Mars Direct Station | Nifty Bank | 1 | 12 | 0.774 | 0.06023 | 0.7137 | 58.33 | 0.06986 | 0.1655 |
| Mars Direct Station | Nifty Bank | 3 | 12 | 2.021 | 0.1819 | 1.839 | 75 | 0.07225 | 0.1701 |
| Mars Direct Station | Nifty Bank | 5 | 12 | 2.291 | 0.3 | 1.991 | 58.33 | 0.2281 | 0.394 |
| Mars Direct Station | Nifty Bank | 10 | 12 | 3.657 | 0.5834 | 3.074 | 58.33 | 0.2051 | 0.3668 |
| Mars Direct Station | Nifty Bank | 20 | 12 | 4.865 | 1.172 | 3.693 | 66.67 | 0.3181 | 0.4952 |
| Mars Direct Station | Nifty Midcap 100 | 1 | 12 | 0.5874 | 0.05397 | 0.5335 | 66.67 | 0.3414 | 0.5216 |
| Mars Direct Station | Nifty Midcap 100 | 3 | 12 | 1.001 | 0.1609 | 0.8404 | 58.33 | 0.3977 | 0.5806 |
| Mars Direct Station | Nifty Midcap 100 | 5 | 12 | 0.407 | 0.266 | 0.141 | 50 | 0.8525 | 0.9199 |
| Mars Direct Station | Nifty Midcap 100 | 10 | 12 | 2.223 | 0.532 | 1.691 | 83.33 | 0.1074 | 0.2284 |
| Mars Direct Station | Nifty Midcap 100 | 20 | 12 | 3.494 | 1.065 | 2.429 | 83.33 | 0.05875 | 0.146 |
| Mars Direct Station | Nifty Midcap 150 | 1 | 12 | 0.7655 | 0.05323 | 0.7123 | 66.67 | 0.03983 | 0.1081 |
| Mars Direct Station | Nifty Midcap 150 | 3 | 12 | 0.9402 | 0.1594 | 0.7808 | 83.33 | 0.2092 | 0.3711 |
| Mars Direct Station | Nifty Midcap 150 | 5 | 12 | 0.4524 | 0.2642 | 0.1882 | 66.67 | 0.6741 | 0.8079 |
| Mars Direct Station | Nifty Midcap 150 | 10 | 12 | 1.141 | 0.5204 | 0.6202 | 58.33 | 0.4954 | 0.6734 |
| Mars Direct Station | Nifty Midcap 150 | 20 | 12 | 2.181 | 1.047 | 1.133 | 75 | 0.4237 | 0.6054 |
| Mars Direct Station | BSE Sensex | 1 | 12 | 0.5887 | 0.05036 | 0.5383 | 58.33 | 0.1154 | 0.2411 |
| Mars Direct Station | BSE Sensex | 3 | 12 | 1.038 | 0.1513 | 0.8863 | 66.67 | 0.1627 | 0.3138 |
| Mars Direct Station | BSE Sensex | 5 | 12 | 0.473 | 0.2506 | 0.2225 | 58.33 | 0.7375 | 0.8481 |
| Mars Direct Station | BSE Sensex | 10 | 12 | 1.093 | 0.4957 | 0.5971 | 58.33 | 0.5116 | 0.6852 |
| Mars Direct Station | BSE Sensex | 20 | 12 | 1.871 | 1.002 | 0.8692 | 75 | 0.5032 | 0.6788 |
| Mercury Direct Station | Nifty 50 | 1 | 84 | 0.1091 | 0.04492 | 0.06413 | 60.71 | 0.7026 | 0.8247 |
| Mercury Direct Station | Nifty 50 | 3 | 84 | 1.567 | 0.1333 | 1.434 | 69.05 | 0.0001559 | 0.001392 |
| Mercury Direct Station | Nifty 50 | 5 | 84 | 2.592 | 0.2178 | 2.375 | 64.29 | 0.0002308 | 0.001842 |
| Mercury Direct Station | Nifty 50 | 10 | 84 | 3.347 | 0.4212 | 2.926 | 67.86 | 0.0003298 | 0.002479 |
| Mercury Direct Station | Nifty 50 | 20 | 84 | 6.893 | 0.8264 | 6.067 | 64.29 | 6.906e-05 | 0.0007378 |
| Mercury Direct Station | Nifty Bank | 1 | 84 | 0.4622 | 0.06023 | 0.402 | 60.71 | 0.07554 | 0.1756 |
| Mercury Direct Station | Nifty Bank | 3 | 84 | 1.844 | 0.1819 | 1.662 | 60.71 | 0.0008168 | 0.005038 |
| Mercury Direct Station | Nifty Bank | 5 | 84 | 2.652 | 0.3 | 2.352 | 63.1 | 0.002853 | 0.01347 |
| Mercury Direct Station | Nifty Bank | 10 | 84 | 3.806 | 0.5834 | 3.223 | 63.1 | 0.002819 | 0.01333 |
| Mercury Direct Station | Nifty Bank | 20 | 84 | 5.335 | 1.172 | 4.163 | 58.33 | 0.005784 | 0.02407 |
| Mercury Direct Station | Nifty Midcap 100 | 1 | 84 | -0.1312 | 0.05397 | -0.1852 | 60.71 | 0.2541 | 0.4265 |
| Mercury Direct Station | Nifty Midcap 100 | 3 | 84 | 0.1765 | 0.1609 | 0.01563 | 40.48 | 0.9599 | 0.9838 |
| Mercury Direct Station | Nifty Midcap 100 | 5 | 84 | -0.1337 | 0.266 | -0.3997 | 42.86 | 0.3351 | 0.5142 |
| Mercury Direct Station | Nifty Midcap 100 | 10 | 84 | 1.332 | 0.532 | 0.7999 | 70.24 | 0.1487 | 0.292 |
| Mercury Direct Station | Nifty Midcap 100 | 20 | 84 | 1.713 | 1.065 | 0.648 | 66.67 | 0.3468 | 0.5258 |
| Mercury Direct Station | Nifty Midcap 150 | 1 | 84 | 0.1507 | 0.05323 | 0.09751 | 57.14 | 0.5803 | 0.7388 |
| Mercury Direct Station | Nifty Midcap 150 | 3 | 84 | 0.203 | 0.1594 | 0.04352 | 70.24 | 0.8523 | 0.9199 |
| Mercury Direct Station | Nifty Midcap 150 | 5 | 84 | 0.2508 | 0.2642 | -0.0134 | 64.29 | 0.9721 | 0.9892 |
| Mercury Direct Station | Nifty Midcap 150 | 10 | 84 | 1.203 | 0.5204 | 0.6821 | 69.05 | 0.1925 | 0.3512 |
| Mercury Direct Station | Nifty Midcap 150 | 20 | 84 | 0.8372 | 1.047 | -0.2103 | 61.9 | 0.7437 | 0.851 |
| Mercury Direct Station | BSE Sensex | 1 | 84 | -0.1692 | 0.05036 | -0.2196 | 50 | 0.2049 | 0.3666 |
| Mercury Direct Station | BSE Sensex | 3 | 84 | -0.02707 | 0.1513 | -0.1784 | 58.33 | 0.5171 | 0.6906 |
| Mercury Direct Station | BSE Sensex | 5 | 84 | -0.1652 | 0.2506 | -0.4157 | 52.38 | 0.3137 | 0.4908 |
| Mercury Direct Station | BSE Sensex | 10 | 84 | -0.3114 | 0.4957 | -0.807 | 55.95 | 0.1636 | 0.3151 |
| Mercury Direct Station | BSE Sensex | 20 | 84 | -0.2876 | 1.002 | -1.289 | 53.57 | 0.07007 | 0.1659 |
| Saturn Direct Station | Nifty 50 | 1 | 26 | 0.1603 | 0.04492 | 0.1154 | 57.69 | 0.5475 | 0.7148 |
| Saturn Direct Station | Nifty 50 | 3 | 26 | 2.15 | 0.1333 | 2.017 | 76.92 | 0.002097 | 0.01039 |
| Saturn Direct Station | Nifty 50 | 5 | 26 | 3.513 | 0.2178 | 3.296 | 69.23 | 0.001739 | 0.009071 |
| Saturn Direct Station | Nifty 50 | 10 | 26 | 5.144 | 0.4212 | 4.722 | 84.62 | 0.0002437 | 0.001924 |
| Saturn Direct Station | Nifty 50 | 20 | 26 | 8.52 | 0.8264 | 7.694 | 76.92 | 0.004776 | 0.02044 |
| Saturn Direct Station | Nifty Bank | 1 | 26 | 0.9263 | 0.06023 | 0.866 | 73.08 | 0.03063 | 0.08995 |
| Saturn Direct Station | Nifty Bank | 3 | 26 | 3.039 | 0.1819 | 2.857 | 76.92 | 0.001287 | 0.007201 |
| Saturn Direct Station | Nifty Bank | 5 | 26 | 4.329 | 0.3 | 4.029 | 69.23 | 0.0009173 | 0.00546 |
| Saturn Direct Station | Nifty Bank | 10 | 26 | 6.321 | 0.5834 | 5.738 | 76.92 | 0.0007051 | 0.004474 |
| Saturn Direct Station | Nifty Bank | 20 | 26 | 7.216 | 1.172 | 6.043 | 76.92 | 0.01885 | 0.0638 |
| Saturn Direct Station | Nifty Midcap 100 | 1 | 26 | -0.3521 | 0.05397 | -0.4061 | 69.23 | 0.3218 | 0.4997 |
| Saturn Direct Station | Nifty Midcap 100 | 3 | 26 | 0.0394 | 0.1609 | -0.1215 | 38.46 | 0.8388 | 0.9128 |
| Saturn Direct Station | Nifty Midcap 100 | 5 | 26 | 0.5849 | 0.266 | 0.3188 | 42.31 | 0.6867 | 0.8141 |
| Saturn Direct Station | Nifty Midcap 100 | 10 | 26 | 3.035 | 0.532 | 2.503 | 76.92 | 0.004051 | 0.01791 |
| Saturn Direct Station | Nifty Midcap 100 | 20 | 26 | 3.428 | 1.065 | 2.364 | 76.92 | 0.03388 | 0.09669 |
| Saturn Direct Station | Nifty Midcap 150 | 1 | 26 | 0.2773 | 0.05323 | 0.224 | 61.54 | 0.3023 | 0.4792 |
| Saturn Direct Station | Nifty Midcap 150 | 3 | 26 | 0.5305 | 0.1594 | 0.3711 | 76.92 | 0.3433 | 0.5235 |
| Saturn Direct Station | Nifty Midcap 150 | 5 | 26 | 0.9703 | 0.2642 | 0.7061 | 73.08 | 0.1198 | 0.2484 |
| Saturn Direct Station | Nifty Midcap 150 | 10 | 26 | 2.51 | 0.5204 | 1.99 | 80.77 | 0.002126 | 0.01048 |
| Saturn Direct Station | Nifty Midcap 150 | 20 | 26 | 2.24 | 1.047 | 1.193 | 76.92 | 0.2402 | 0.4079 |
| Saturn Direct Station | BSE Sensex | 1 | 26 | -0.3873 | 0.05036 | -0.4377 | 42.31 | 0.01953 | 0.06505 |
| Saturn Direct Station | BSE Sensex | 3 | 26 | 0.03499 | 0.1513 | -0.1163 | 50 | 0.8055 | 0.891 |
| Saturn Direct Station | BSE Sensex | 5 | 26 | 0.2767 | 0.2506 | 0.02614 | 50 | 0.9641 | 0.9862 |
| Saturn Direct Station | BSE Sensex | 10 | 26 | 0.699 | 0.4957 | 0.2033 | 69.23 | 0.7725 | 0.872 |
| Saturn Direct Station | BSE Sensex | 20 | 26 | 0.7724 | 1.002 | -0.2292 | 57.69 | 0.8147 | 0.897 |
| Venus Direct Station | Nifty 50 | 1 | 16 | 0.828 | 0.04492 | 0.7831 | 75 | 0.004575 | 0.01969 |
| Venus Direct Station | Nifty 50 | 3 | 16 | 2.438 | 0.1333 | 2.304 | 81.25 | 0.002933 | 0.01375 |
| Venus Direct Station | Nifty 50 | 5 | 16 | 4.137 | 0.2178 | 3.919 | 81.25 | 0.002333 | 0.01129 |
| Venus Direct Station | Nifty 50 | 10 | 16 | 5.788 | 0.4212 | 5.367 | 93.75 | 0.001059 | 0.006215 |
| Venus Direct Station | Nifty 50 | 20 | 16 | 11.7 | 0.8264 | 10.87 | 81.25 | 0.002575 | 0.01233 |
| Venus Direct Station | Nifty Bank | 1 | 16 | 1.356 | 0.06023 | 1.296 | 81.25 | 0.008944 | 0.03443 |
| Venus Direct Station | Nifty Bank | 3 | 16 | 3.156 | 0.1819 | 2.974 | 68.75 | 0.004586 | 0.0197 |
| Venus Direct Station | Nifty Bank | 5 | 16 | 5.063 | 0.3 | 4.763 | 93.75 | 0.00123 | 0.006989 |
| Venus Direct Station | Nifty Bank | 10 | 16 | 7.692 | 0.5834 | 7.109 | 93.75 | 0.0003909 | 0.00283 |
| Venus Direct Station | Nifty Bank | 20 | 16 | 11.52 | 1.172 | 10.35 | 81.25 | 0.006613 | 0.02667 |
| Venus Direct Station | Nifty Midcap 100 | 1 | 16 | 0.3628 | 0.05397 | 0.3088 | 75 | 0.4365 | 0.6173 |
| Venus Direct Station | Nifty Midcap 100 | 3 | 16 | 0.3725 | 0.1609 | 0.2116 | 56.25 | 0.6779 | 0.8088 |
| Venus Direct Station | Nifty Midcap 100 | 5 | 16 | 1.056 | 0.266 | 0.7903 | 50 | 0.2471 | 0.4167 |
| Venus Direct Station | Nifty Midcap 100 | 10 | 16 | 3.642 | 0.532 | 3.11 | 87.5 | 0.01314 | 0.04745 |
| Venus Direct Station | Nifty Midcap 100 | 20 | 16 | 5.983 | 1.065 | 4.919 | 81.25 | 0.02399 | 0.07552 |
| Venus Direct Station | Nifty Midcap 150 | 1 | 16 | 0.8576 | 0.05323 | 0.8044 | 75 | 0.008724 | 0.03376 |
| Venus Direct Station | Nifty Midcap 150 | 3 | 16 | 0.9872 | 0.1594 | 0.8278 | 81.25 | 0.03391 | 0.09669 |
| Venus Direct Station | Nifty Midcap 150 | 5 | 16 | 1.582 | 0.2642 | 1.318 | 75 | 0.0186 | 0.063 |
| Venus Direct Station | Nifty Midcap 150 | 10 | 16 | 3.363 | 0.5204 | 2.843 | 93.75 | 0.001313 | 0.007304 |
| Venus Direct Station | Nifty Midcap 150 | 20 | 16 | 5.965 | 1.047 | 4.918 | 75 | 0.01997 | 0.06609 |
| Venus Direct Station | BSE Sensex | 1 | 16 | 0.7802 | 0.05036 | 0.7299 | 75 | 0.01913 | 0.06436 |
| Venus Direct Station | BSE Sensex | 3 | 16 | 1.13 | 0.1513 | 0.9787 | 87.5 | 0.02318 | 0.07348 |
| Venus Direct Station | BSE Sensex | 5 | 16 | 1.533 | 0.2506 | 1.282 | 68.75 | 0.07394 | 0.1727 |
| Venus Direct Station | BSE Sensex | 10 | 16 | 2.822 | 0.4957 | 2.326 | 87.5 | 0.007269 | 0.02894 |
| Venus Direct Station | BSE Sensex | 20 | 16 | 6.343 | 1.002 | 5.341 | 81.25 | 0.01479 | 0.05163 |

### Retrograde stations (Vakra)

* When Jupiter went retrograde (24 events since 2000), Nifty 50 averaged +2.59% over the next 5 trading days (base rate +0.22%). Win rate 62.5%. That is +2.37 pp above the unconditional baseline. Nominally significant at p=0.02935, but it does not survive Benjamini-Hochberg correction (q=0.08728).
* When Jupiter went retrograde (24 events since 2000), Nifty Bank averaged +3.18% over the next 5 trading days (base rate +0.30%). Win rate 70.8%. That is +2.88 pp above the unconditional baseline. Nominally significant at p=0.02247, but it does not survive Benjamini-Hochberg correction (q=0.07184).
* When Jupiter went retrograde (24 events since 2000), Nifty Midcap 100 averaged +0.42% over the next 5 trading days (base rate +0.27%). Win rate 41.7%. That is +0.16 pp above the unconditional baseline. Not statistically significant (p=0.6999, q=0.8225 after Benjamini-Hochberg correction).
* When Jupiter went retrograde (24 events since 2000), Nifty Midcap 150 averaged +0.30% over the next 5 trading days (base rate +0.26%). Win rate 62.5%. That is +0.04 pp above the unconditional baseline. Not statistically significant (p=0.9303, q=0.9709 after Benjamini-Hochberg correction).
* When Jupiter went retrograde (24 events since 2000), BSE Sensex averaged +0.08% over the next 5 trading days (base rate +0.25%). Win rate 62.5%. That is -0.17 pp below the unconditional baseline. Not statistically significant (p=0.7016, q=0.8237 after Benjamini-Hochberg correction).

* When Mars went retrograde (12 events since 2001), Nifty 50 averaged +3.13% over the next 5 trading days (base rate +0.22%). Win rate 91.7%. That is +2.91 pp above the unconditional baseline. Not statistically significant (p=0.06412, q=0.1557 after Benjamini-Hochberg correction).
* When Mars went retrograde (12 events since 2001), Nifty Bank averaged +4.39% over the next 5 trading days (base rate +0.30%). Win rate 83.3%. That is +4.09 pp above the unconditional baseline. Nominally significant at p=0.03503, but it does not survive Benjamini-Hochberg correction (q=0.09944).
* When Mars went retrograde (12 events since 2001), Nifty Midcap 100 averaged +0.42% over the next 5 trading days (base rate +0.27%). Win rate 50.0%. That is +0.15 pp above the unconditional baseline. Not statistically significant (p=0.8795, q=0.9383 after Benjamini-Hochberg correction).
* When Mars went retrograde (12 events since 2001), Nifty Midcap 150 averaged +1.14% over the next 5 trading days (base rate +0.26%). Win rate 91.7%. That is +0.87 pp above the unconditional baseline. Not statistically significant (p=0.2821, q=0.4582 after Benjamini-Hochberg correction).
* When Mars went retrograde (12 events since 2001), BSE Sensex averaged +0.63% over the next 5 trading days (base rate +0.25%). Win rate 83.3%. That is +0.38 pp above the unconditional baseline. Not statistically significant (p=0.6643, q=0.8011 after Benjamini-Hochberg correction).

* When Mercury went retrograde (85 events since 2000), Nifty 50 averaged +2.79% over the next 5 trading days (base rate +0.22%). Win rate 65.9%. That is +2.57 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0001016).
* When Mercury went retrograde (85 events since 2000), Nifty Bank averaged +3.19% over the next 5 trading days (base rate +0.30%). Win rate 63.5%. That is +2.89 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0001152).
* When Mercury went retrograde (85 events since 2000), Nifty Midcap 100 averaged -0.20% over the next 5 trading days (base rate +0.27%). Win rate 37.6%. That is -0.47 pp below the unconditional baseline. Not statistically significant (p=0.1431, q=0.2838 after Benjamini-Hochberg correction).
* When Mercury went retrograde (85 events since 2000), Nifty Midcap 150 averaged +0.42% over the next 5 trading days (base rate +0.26%). Win rate 62.4%. That is +0.16 pp above the unconditional baseline. Not statistically significant (p=0.5103, q=0.6841 after Benjamini-Hochberg correction).
* When Mercury went retrograde (85 events since 2000), BSE Sensex averaged +0.06% over the next 5 trading days (base rate +0.25%). Win rate 58.8%. That is -0.19 pp below the unconditional baseline. Not statistically significant (p=0.5101, q=0.6841 after Benjamini-Hochberg correction).

* When Saturn went retrograde (26 events since 2000), Nifty 50 averaged +2.31% over the next 5 trading days (base rate +0.22%). Win rate 61.5%. That is +2.09 pp above the unconditional baseline. Not statistically significant (p=0.06853, q=0.1632 after Benjamini-Hochberg correction).
* When Saturn went retrograde (26 events since 2000), Nifty Bank averaged +3.00% over the next 5 trading days (base rate +0.30%). Win rate 65.4%. That is +2.70 pp above the unconditional baseline. Nominally significant at p=0.04815, but it does not survive Benjamini-Hochberg correction (q=0.1249).
* When Saturn went retrograde (26 events since 2000), Nifty Midcap 100 averaged -0.17% over the next 5 trading days (base rate +0.27%). Win rate 30.8%. That is -0.44 pp below the unconditional baseline. Not statistically significant (p=0.5308, q=0.7014 after Benjamini-Hochberg correction).
* When Saturn went retrograde (26 events since 2000), Nifty Midcap 150 averaged -0.17% over the next 5 trading days (base rate +0.26%). Win rate 57.7%. That is -0.43 pp below the unconditional baseline. Not statistically significant (p=0.5356, q=0.7036 after Benjamini-Hochberg correction).
* When Saturn went retrograde (26 events since 2000), BSE Sensex averaged -0.32% over the next 5 trading days (base rate +0.25%). Win rate 46.2%. That is -0.58 pp below the unconditional baseline. Not statistically significant (p=0.4841, q=0.6622 after Benjamini-Hochberg correction).

* When Venus went retrograde (17 events since 2001), Nifty 50 averaged +3.76% over the next 5 trading days (base rate +0.22%). Win rate 82.4%. That is +3.54 pp above the unconditional baseline. Statistically significant at p=0.00606 and after Benjamini-Hochberg correction (q=0.02493).
* When Venus went retrograde (17 events since 2001), Nifty Bank averaged +3.97% over the next 5 trading days (base rate +0.30%). Win rate 82.4%. That is +3.67 pp above the unconditional baseline. Nominally significant at p=0.02313, but it does not survive Benjamini-Hochberg correction (q=0.07346).
* When Venus went retrograde (17 events since 2001), Nifty Midcap 100 averaged +0.66% over the next 5 trading days (base rate +0.27%). Win rate 52.9%. That is +0.40 pp above the unconditional baseline. Not statistically significant (p=0.5616, q=0.7257 after Benjamini-Hochberg correction).
* When Venus went retrograde (17 events since 2001), Nifty Midcap 150 averaged +1.21% over the next 5 trading days (base rate +0.26%). Win rate 70.6%. That is +0.94 pp above the unconditional baseline. Not statistically significant (p=0.1592, q=0.3081 after Benjamini-Hochberg correction).
* When Venus went retrograde (17 events since 2001), BSE Sensex averaged +0.96% over the next 5 trading days (base rate +0.25%). Win rate 64.7%. That is +0.71 pp above the unconditional baseline. Not statistically significant (p=0.3822, q=0.5648 after Benjamini-Hochberg correction).

**All windows — Retrograde stations (Vakra)**

| Event | Index | Window | N | Mean ret | Base rate | Excess | Win % | p-value | q (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jupiter Retrograde Station | Nifty 50 | 1 | 24 | 0.2658 | 0.04492 | 0.2209 | 75 | 0.3481 | 0.5275 |
| Jupiter Retrograde Station | Nifty 50 | 3 | 24 | 1.56 | 0.1333 | 1.427 | 66.67 | 0.0334 | 0.0957 |
| Jupiter Retrograde Station | Nifty 50 | 5 | 24 | 2.592 | 0.2178 | 2.374 | 62.5 | 0.02935 | 0.08728 |
| Jupiter Retrograde Station | Nifty 50 | 10 | 24 | 3.847 | 0.4212 | 3.426 | 66.67 | 0.01384 | 0.04916 |
| Jupiter Retrograde Station | Nifty 50 | 20 | 24 | 6.973 | 0.8264 | 6.147 | 62.5 | 0.03138 | 0.09144 |
| Jupiter Retrograde Station | Nifty Bank | 1 | 24 | 0.6207 | 0.06023 | 0.5605 | 70.83 | 0.1849 | 0.3418 |
| Jupiter Retrograde Station | Nifty Bank | 3 | 24 | 2.138 | 0.1819 | 1.956 | 70.83 | 0.01898 | 0.06417 |
| Jupiter Retrograde Station | Nifty Bank | 5 | 24 | 3.176 | 0.3 | 2.876 | 70.83 | 0.02247 | 0.07184 |
| Jupiter Retrograde Station | Nifty Bank | 10 | 24 | 5.087 | 0.5834 | 4.504 | 75 | 0.009567 | 0.03638 |
| Jupiter Retrograde Station | Nifty Bank | 20 | 24 | 6.535 | 1.172 | 5.363 | 79.17 | 0.03944 | 0.1075 |
| Jupiter Retrograde Station | Nifty Midcap 100 | 1 | 24 | -0.09302 | 0.05397 | -0.147 | 62.5 | 0.3356 | 0.5147 |
| Jupiter Retrograde Station | Nifty Midcap 100 | 3 | 24 | 0.1318 | 0.1609 | -0.0291 | 41.67 | 0.9251 | 0.9671 |
| Jupiter Retrograde Station | Nifty Midcap 100 | 5 | 24 | 0.4221 | 0.266 | 0.1561 | 41.67 | 0.6999 | 0.8225 |
| Jupiter Retrograde Station | Nifty Midcap 100 | 10 | 24 | 2.393 | 0.532 | 1.861 | 79.17 | 0.003735 | 0.01675 |
| Jupiter Retrograde Station | Nifty Midcap 100 | 20 | 24 | 2.209 | 1.065 | 1.144 | 58.33 | 0.1582 | 0.307 |
| Jupiter Retrograde Station | Nifty Midcap 150 | 1 | 24 | 0.3263 | 0.05323 | 0.2731 | 70.83 | 0.279 | 0.4552 |
| Jupiter Retrograde Station | Nifty Midcap 150 | 3 | 24 | -0.02194 | 0.1594 | -0.1814 | 58.33 | 0.5824 | 0.7403 |
| Jupiter Retrograde Station | Nifty Midcap 150 | 5 | 24 | 0.3023 | 0.2642 | 0.03803 | 62.5 | 0.9303 | 0.9709 |
| Jupiter Retrograde Station | Nifty Midcap 150 | 10 | 24 | 1.58 | 0.5204 | 1.06 | 66.67 | 0.1416 | 0.2816 |
| Jupiter Retrograde Station | Nifty Midcap 150 | 20 | 24 | 0.9611 | 1.047 | -0.08634 | 62.5 | 0.9366 | 0.9745 |
| Jupiter Retrograde Station | BSE Sensex | 1 | 24 | 0.1001 | 0.05036 | 0.04976 | 66.67 | 0.8372 | 0.9124 |
| Jupiter Retrograde Station | BSE Sensex | 3 | 24 | 0.02114 | 0.1513 | -0.1302 | 54.17 | 0.6935 | 0.8189 |
| Jupiter Retrograde Station | BSE Sensex | 5 | 24 | 0.07662 | 0.2506 | -0.174 | 62.5 | 0.7016 | 0.8237 |
| Jupiter Retrograde Station | BSE Sensex | 10 | 24 | 0.4587 | 0.4957 | -0.03695 | 62.5 | 0.962 | 0.9849 |
| Jupiter Retrograde Station | BSE Sensex | 20 | 24 | 0.1572 | 1.002 | -0.8445 | 50 | 0.4557 | 0.6341 |
| Mars Retrograde Station | Nifty 50 | 1 | 12 | 0.4935 | 0.04492 | 0.4486 | 75 | 0.03409 | 0.09714 |
| Mars Retrograde Station | Nifty 50 | 3 | 12 | 1.798 | 0.1333 | 1.665 | 58.33 | 0.07094 | 0.1674 |
| Mars Retrograde Station | Nifty 50 | 5 | 12 | 3.125 | 0.2178 | 2.907 | 91.67 | 0.06412 | 0.1557 |
| Mars Retrograde Station | Nifty 50 | 10 | 12 | 3.572 | 0.4212 | 3.15 | 66.67 | 0.1348 | 0.2719 |
| Mars Retrograde Station | Nifty 50 | 20 | 12 | 8.863 | 0.8264 | 8.037 | 83.33 | 0.02599 | 0.07963 |
| Mars Retrograde Station | Nifty Bank | 1 | 12 | 1.004 | 0.06023 | 0.9437 | 83.33 | 0.01382 | 0.04913 |
| Mars Retrograde Station | Nifty Bank | 3 | 12 | 2.371 | 0.1819 | 2.189 | 50 | 0.07225 | 0.1701 |
| Mars Retrograde Station | Nifty Bank | 5 | 12 | 4.393 | 0.3 | 4.093 | 83.33 | 0.03503 | 0.09944 |
| Mars Retrograde Station | Nifty Bank | 10 | 12 | 5.135 | 0.5834 | 4.551 | 75 | 0.09336 | 0.2062 |
| Mars Retrograde Station | Nifty Bank | 20 | 12 | 9.44 | 1.172 | 8.268 | 91.67 | 0.01238 | 0.04529 |
| Mars Retrograde Station | Nifty Midcap 100 | 1 | 12 | 0.2727 | 0.05397 | 0.2188 | 58.33 | 0.395 | 0.5785 |
| Mars Retrograde Station | Nifty Midcap 100 | 3 | 12 | 0.7727 | 0.1609 | 0.6118 | 58.33 | 0.4079 | 0.59 |
| Mars Retrograde Station | Nifty Midcap 100 | 5 | 12 | 0.4152 | 0.266 | 0.1492 | 50 | 0.8795 | 0.9383 |
| Mars Retrograde Station | Nifty Midcap 100 | 10 | 12 | 1.07 | 0.532 | 0.5379 | 66.67 | 0.7029 | 0.8248 |
| Mars Retrograde Station | Nifty Midcap 100 | 20 | 12 | 4.363 | 1.065 | 3.298 | 75 | 0.1345 | 0.2717 |
| Mars Retrograde Station | Nifty Midcap 150 | 1 | 12 | 0.6713 | 0.05323 | 0.6181 | 91.67 | 0.02308 | 0.07333 |
| Mars Retrograde Station | Nifty Midcap 150 | 3 | 12 | 0.6134 | 0.1594 | 0.454 | 58.33 | 0.338 | 0.5183 |
| Mars Retrograde Station | Nifty Midcap 150 | 5 | 12 | 1.136 | 0.2642 | 0.8716 | 91.67 | 0.2821 | 0.4582 |
| Mars Retrograde Station | Nifty Midcap 150 | 10 | 12 | 1.85 | 0.5204 | 1.329 | 66.67 | 0.3216 | 0.4996 |
| Mars Retrograde Station | Nifty Midcap 150 | 20 | 12 | 3.619 | 1.047 | 2.572 | 83.33 | 0.02288 | 0.07291 |
| Mars Retrograde Station | BSE Sensex | 1 | 12 | 0.327 | 0.05036 | 0.2766 | 83.33 | 0.1083 | 0.2299 |
| Mars Retrograde Station | BSE Sensex | 3 | 12 | 0.5677 | 0.1513 | 0.4164 | 66.67 | 0.4932 | 0.6718 |
| Mars Retrograde Station | BSE Sensex | 5 | 12 | 0.6273 | 0.2506 | 0.3767 | 83.33 | 0.6643 | 0.8011 |
| Mars Retrograde Station | BSE Sensex | 10 | 12 | 0.3791 | 0.4957 | -0.1166 | 58.33 | 0.9305 | 0.9709 |
| Mars Retrograde Station | BSE Sensex | 20 | 12 | 2.386 | 1.002 | 1.385 | 66.67 | 0.3724 | 0.5538 |
| Mercury Retrograde Station | Nifty 50 | 1 | 85 | 0.3853 | 0.04492 | 0.3404 | 60 | 0.009853 | 0.03732 |
| Mercury Retrograde Station | Nifty 50 | 3 | 85 | 1.645 | 0.1333 | 1.512 | 72.94 | 1.637e-05 | 0.0002426 |
| Mercury Retrograde Station | Nifty 50 | 5 | 85 | 2.791 | 0.2178 | 2.573 | 65.88 | 5.85e-06 | 0.0001016 |
| Mercury Retrograde Station | Nifty 50 | 10 | 84 | 3.561 | 0.4212 | 3.14 | 70.24 | 0.0001279 | 0.0012 |
| Mercury Retrograde Station | Nifty 50 | 20 | 84 | 7.404 | 0.8264 | 6.578 | 72.62 | 3.892e-05 | 0.0004604 |
| Mercury Retrograde Station | Nifty Bank | 1 | 85 | 0.7829 | 0.06023 | 0.7227 | 68.24 | 8.844e-05 | 0.0008916 |
| Mercury Retrograde Station | Nifty Bank | 3 | 85 | 2.207 | 0.1819 | 2.025 | 71.76 | 4.532e-06 | 8.371e-05 |
| Mercury Retrograde Station | Nifty Bank | 5 | 85 | 3.186 | 0.3 | 2.886 | 63.53 | 6.789e-06 | 0.0001152 |
| Mercury Retrograde Station | Nifty Bank | 10 | 84 | 4.665 | 0.5834 | 4.082 | 67.86 | 8.113e-05 | 0.0008313 |
| Mercury Retrograde Station | Nifty Bank | 20 | 84 | 6.615 | 1.172 | 5.442 | 65.48 | 0.0003622 | 0.002668 |
| Mercury Retrograde Station | Nifty Midcap 100 | 1 | 85 | -0.08778 | 0.05397 | -0.1417 | 57.65 | 0.2857 | 0.4608 |
| Mercury Retrograde Station | Nifty Midcap 100 | 3 | 85 | -0.1851 | 0.1609 | -0.3459 | 32.94 | 0.2301 | 0.396 |
| Mercury Retrograde Station | Nifty Midcap 100 | 5 | 85 | -0.2045 | 0.266 | -0.4705 | 37.65 | 0.1431 | 0.2838 |
| Mercury Retrograde Station | Nifty Midcap 100 | 10 | 84 | 0.9769 | 0.532 | 0.4449 | 66.67 | 0.4479 | 0.6282 |
| Mercury Retrograde Station | Nifty Midcap 100 | 20 | 84 | 1.835 | 1.065 | 0.7701 | 65.48 | 0.37 | 0.5522 |
| Mercury Retrograde Station | Nifty Midcap 150 | 1 | 85 | 0.4489 | 0.05323 | 0.3957 | 56.47 | 0.005948 | 0.02465 |
| Mercury Retrograde Station | Nifty Midcap 150 | 3 | 85 | 0.2139 | 0.1594 | 0.0545 | 71.76 | 0.778 | 0.8736 |
| Mercury Retrograde Station | Nifty Midcap 150 | 5 | 85 | 0.4242 | 0.2642 | 0.16 | 62.35 | 0.5103 | 0.6841 |
| Mercury Retrograde Station | Nifty Midcap 150 | 10 | 84 | 1.162 | 0.5204 | 0.6412 | 66.67 | 0.2514 | 0.4228 |
| Mercury Retrograde Station | Nifty Midcap 150 | 20 | 84 | 1.276 | 1.047 | 0.2287 | 70.24 | 0.7879 | 0.8799 |
| Mercury Retrograde Station | BSE Sensex | 1 | 85 | 0.04751 | 0.05036 | -0.002854 | 48.24 | 0.9834 | 0.9946 |
| Mercury Retrograde Station | BSE Sensex | 3 | 85 | -0.04068 | 0.1513 | -0.192 | 61.18 | 0.3902 | 0.5731 |
| Mercury Retrograde Station | BSE Sensex | 5 | 85 | 0.06236 | 0.2506 | -0.1882 | 58.82 | 0.5101 | 0.6841 |
| Mercury Retrograde Station | BSE Sensex | 10 | 84 | 0.07129 | 0.4957 | -0.4244 | 59.52 | 0.4336 | 0.616 |
| Mercury Retrograde Station | BSE Sensex | 20 | 84 | 0.269 | 1.002 | -0.7327 | 57.14 | 0.3992 | 0.5817 |
| Saturn Retrograde Station | Nifty 50 | 1 | 26 | 0.5472 | 0.04492 | 0.5022 | 65.38 | 0.02791 | 0.08413 |
| Saturn Retrograde Station | Nifty 50 | 3 | 26 | 1.565 | 0.1333 | 1.431 | 69.23 | 0.02579 | 0.0792 |
| Saturn Retrograde Station | Nifty 50 | 5 | 26 | 2.306 | 0.2178 | 2.088 | 61.54 | 0.06853 | 0.1632 |
| Saturn Retrograde Station | Nifty 50 | 10 | 26 | 2.929 | 0.4212 | 2.508 | 61.54 | 0.08882 | 0.198 |
| Saturn Retrograde Station | Nifty 50 | 20 | 26 | 6.717 | 0.8264 | 5.891 | 65.38 | 0.02761 | 0.08342 |
| Saturn Retrograde Station | Nifty Bank | 1 | 26 | 0.9233 | 0.06023 | 0.863 | 65.38 | 0.006585 | 0.02661 |
| Saturn Retrograde Station | Nifty Bank | 3 | 26 | 2.374 | 0.1819 | 2.192 | 73.08 | 0.005095 | 0.02164 |
| Saturn Retrograde Station | Nifty Bank | 5 | 26 | 3.001 | 0.3 | 2.701 | 65.38 | 0.04815 | 0.1249 |
| Saturn Retrograde Station | Nifty Bank | 10 | 26 | 3.87 | 0.5834 | 3.286 | 57.69 | 0.08006 | 0.1831 |
| Saturn Retrograde Station | Nifty Bank | 20 | 26 | 6.359 | 1.172 | 5.186 | 61.54 | 0.03576 | 0.1011 |
| Saturn Retrograde Station | Nifty Midcap 100 | 1 | 26 | 0.5184 | 0.05397 | 0.4645 | 73.08 | 0.1427 | 0.2832 |
| Saturn Retrograde Station | Nifty Midcap 100 | 3 | 26 | 0.42 | 0.1609 | 0.2591 | 38.46 | 0.6324 | 0.7778 |
| Saturn Retrograde Station | Nifty Midcap 100 | 5 | 26 | -0.1748 | 0.266 | -0.4408 | 30.77 | 0.5308 | 0.7014 |
| Saturn Retrograde Station | Nifty Midcap 100 | 10 | 26 | 0.1972 | 0.532 | -0.3348 | 57.69 | 0.7439 | 0.851 |
| Saturn Retrograde Station | Nifty Midcap 100 | 20 | 26 | 0.8937 | 1.065 | -0.1711 | 61.54 | 0.9011 | 0.9534 |
| Saturn Retrograde Station | Nifty Midcap 150 | 1 | 26 | 0.6266 | 0.05323 | 0.5734 | 65.38 | 0.02139 | 0.0694 |
| Saturn Retrograde Station | Nifty Midcap 150 | 3 | 26 | 0.02461 | 0.1594 | -0.1348 | 61.54 | 0.7279 | 0.8419 |
| Saturn Retrograde Station | Nifty Midcap 150 | 5 | 26 | -0.1689 | 0.2642 | -0.4332 | 57.69 | 0.5356 | 0.7036 |
| Saturn Retrograde Station | Nifty Midcap 150 | 10 | 26 | 0.6009 | 0.5204 | 0.08046 | 57.69 | 0.9342 | 0.9726 |
| Saturn Retrograde Station | Nifty Midcap 150 | 20 | 26 | 0.847 | 1.047 | -0.2005 | 65.38 | 0.8473 | 0.9174 |
| Saturn Retrograde Station | BSE Sensex | 1 | 26 | 0.3958 | 0.05036 | 0.3455 | 50 | 0.185 | 0.3419 |
| Saturn Retrograde Station | BSE Sensex | 3 | 26 | -0.1106 | 0.1513 | -0.2619 | 61.54 | 0.6053 | 0.7559 |
| Saturn Retrograde Station | BSE Sensex | 5 | 26 | -0.3246 | 0.2506 | -0.5752 | 46.15 | 0.4841 | 0.6622 |
| Saturn Retrograde Station | BSE Sensex | 10 | 26 | -0.5417 | 0.4957 | -1.037 | 50 | 0.3151 | 0.4926 |
| Saturn Retrograde Station | BSE Sensex | 20 | 26 | -0.1256 | 1.002 | -1.127 | 53.85 | 0.4007 | 0.5833 |
| Venus Retrograde Station | Nifty 50 | 1 | 17 | 0.3695 | 0.04492 | 0.3245 | 64.71 | 0.206 | 0.3678 |
| Venus Retrograde Station | Nifty 50 | 3 | 17 | 2.068 | 0.1333 | 1.934 | 70.59 | 0.04032 | 0.1091 |
| Venus Retrograde Station | Nifty 50 | 5 | 17 | 3.761 | 0.2178 | 3.543 | 82.35 | 0.00606 | 0.02493 |
| Venus Retrograde Station | Nifty 50 | 10 | 17 | 5.424 | 0.4212 | 5.003 | 76.47 | 0.00488 | 0.02084 |
| Venus Retrograde Station | Nifty 50 | 20 | 17 | 11.39 | 0.8264 | 10.56 | 88.24 | 0.002955 | 0.01377 |
| Venus Retrograde Station | Nifty Bank | 1 | 17 | 0.7619 | 0.06023 | 0.7017 | 64.71 | 0.07651 | 0.1768 |
| Venus Retrograde Station | Nifty Bank | 3 | 17 | 2.781 | 0.1819 | 2.599 | 82.35 | 0.04705 | 0.1229 |
| Venus Retrograde Station | Nifty Bank | 5 | 17 | 3.974 | 0.3 | 3.674 | 82.35 | 0.02313 | 0.07346 |
| Venus Retrograde Station | Nifty Bank | 10 | 17 | 6.744 | 0.5834 | 6.161 | 76.47 | 0.008063 | 0.03163 |
| Venus Retrograde Station | Nifty Bank | 20 | 17 | 11.26 | 1.172 | 10.08 | 82.35 | 0.006228 | 0.02541 |
| Venus Retrograde Station | Nifty Midcap 100 | 1 | 17 | -0.02594 | 0.05397 | -0.0799 | 64.71 | 0.7876 | 0.8798 |
| Venus Retrograde Station | Nifty Midcap 100 | 3 | 17 | 0.4693 | 0.1609 | 0.3084 | 35.29 | 0.6837 | 0.8124 |
| Venus Retrograde Station | Nifty Midcap 100 | 5 | 17 | 0.6628 | 0.266 | 0.3968 | 52.94 | 0.5616 | 0.7257 |
| Venus Retrograde Station | Nifty Midcap 100 | 10 | 17 | 3.285 | 0.532 | 2.753 | 88.24 | 0.03893 | 0.1068 |
| Venus Retrograde Station | Nifty Midcap 100 | 20 | 17 | 5.167 | 1.065 | 4.102 | 82.35 | 0.03119 | 0.09108 |
| Venus Retrograde Station | Nifty Midcap 150 | 1 | 17 | 0.6155 | 0.05323 | 0.5623 | 64.71 | 0.0643 | 0.1559 |
| Venus Retrograde Station | Nifty Midcap 150 | 3 | 17 | 0.6686 | 0.1594 | 0.5091 | 70.59 | 0.4648 | 0.6421 |
| Venus Retrograde Station | Nifty Midcap 150 | 5 | 17 | 1.208 | 0.2642 | 0.9435 | 70.59 | 0.1592 | 0.3081 |
| Venus Retrograde Station | Nifty Midcap 150 | 10 | 17 | 3.046 | 0.5204 | 2.526 | 70.59 | 0.03092 | 0.09059 |
| Venus Retrograde Station | Nifty Midcap 150 | 20 | 17 | 4.999 | 1.047 | 3.951 | 82.35 | 0.0624 | 0.153 |
| Venus Retrograde Station | BSE Sensex | 1 | 17 | 0.2648 | 0.05036 | 0.2144 | 52.94 | 0.5747 | 0.734 |
| Venus Retrograde Station | BSE Sensex | 3 | 17 | 0.4516 | 0.1513 | 0.3002 | 58.82 | 0.7139 | 0.8335 |
| Venus Retrograde Station | BSE Sensex | 5 | 17 | 0.9581 | 0.2506 | 0.7075 | 64.71 | 0.3822 | 0.5648 |
| Venus Retrograde Station | BSE Sensex | 10 | 17 | 1.285 | 0.4957 | 0.7893 | 52.94 | 0.5621 | 0.7258 |
| Venus Retrograde Station | BSE Sensex | 20 | 17 | 3.362 | 1.002 | 2.361 | 64.71 | 0.3103 | 0.4872 |

### Sign ingress (Rashi Sankranti)

* When Jupiter changed sign (39 events since 2000), Nifty 50 averaged +1.85% over the next 5 trading days (base rate +0.22%). Win rate 56.4%. That is +1.63 pp above the unconditional baseline. Nominally significant at p=0.02104, but it does not survive Benjamini-Hochberg correction (q=0.06844).
* When Jupiter changed sign (39 events since 2000), Nifty Bank averaged +2.12% over the next 5 trading days (base rate +0.30%). Win rate 61.5%. That is +1.82 pp above the unconditional baseline. Nominally significant at p=0.02277, but it does not survive Benjamini-Hochberg correction (q=0.07259).
* When Jupiter changed sign (39 events since 2000), Nifty Midcap 100 averaged -0.29% over the next 5 trading days (base rate +0.27%). Win rate 41.0%. That is -0.56 pp below the unconditional baseline. Not statistically significant (p=0.255, q=0.4274 after Benjamini-Hochberg correction).
* When Jupiter changed sign (39 events since 2000), Nifty Midcap 150 averaged +0.39% over the next 5 trading days (base rate +0.26%). Win rate 56.4%. That is +0.12 pp above the unconditional baseline. Not statistically significant (p=0.7167, q=0.836 after Benjamini-Hochberg correction).
* When Jupiter changed sign (39 events since 2000), BSE Sensex averaged +0.18% over the next 5 trading days (base rate +0.25%). Win rate 48.7%. That is -0.07 pp below the unconditional baseline. Not statistically significant (p=0.8258, q=0.9052 after Benjamini-Hochberg correction).

* When Ketu changed sign (17 events since 2000), Nifty 50 averaged +3.26% over the next 5 trading days (base rate +0.22%). Win rate 76.5%. That is +3.04 pp above the unconditional baseline. Statistically significant at p=0.01399 and after Benjamini-Hochberg correction (q=0.04946).
* When Ketu changed sign (17 events since 2000), Nifty Bank averaged +3.87% over the next 5 trading days (base rate +0.30%). Win rate 70.6%. That is +3.57 pp above the unconditional baseline. Statistically significant at p=0.01152 and after Benjamini-Hochberg correction (q=0.04268).
* When Ketu changed sign (17 events since 2000), Nifty Midcap 100 averaged -0.37% over the next 5 trading days (base rate +0.27%). Win rate 41.2%. That is -0.63 pp below the unconditional baseline. Not statistically significant (p=0.1295, q=0.2638 after Benjamini-Hochberg correction).
* When Ketu changed sign (17 events since 2000), Nifty Midcap 150 averaged +0.84% over the next 5 trading days (base rate +0.26%). Win rate 76.5%. That is +0.58 pp above the unconditional baseline. Not statistically significant (p=0.1251, q=0.2567 after Benjamini-Hochberg correction).
* When Ketu changed sign (17 events since 2000), BSE Sensex averaged +0.10% over the next 5 trading days (base rate +0.25%). Win rate 58.8%. That is -0.15 pp below the unconditional baseline. Not statistically significant (p=0.7718, q=0.8717 after Benjamini-Hochberg correction).

* When Mars changed sign (185 events since 2000), Nifty 50 averaged +2.85% over the next 5 trading days (base rate +0.22%). Win rate 65.4%. That is +2.63 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=2.557e-09).
* When Mars changed sign (185 events since 2000), Nifty Bank averaged +3.32% over the next 5 trading days (base rate +0.30%). Win rate 67.0%. That is +3.02 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=2.703e-09).
* When Mars changed sign (185 events since 2000), Nifty Midcap 100 averaged -0.03% over the next 5 trading days (base rate +0.27%). Win rate 34.1%. That is -0.30 pp below the unconditional baseline. Not statistically significant (p=0.1994, q=0.3599 after Benjamini-Hochberg correction).
* When Mars changed sign (185 events since 2000), Nifty Midcap 150 averaged +0.39% over the next 5 trading days (base rate +0.26%). Win rate 63.8%. That is +0.12 pp above the unconditional baseline. Not statistically significant (p=0.5612, q=0.7254 after Benjamini-Hochberg correction).
* When Mars changed sign (185 events since 2000), BSE Sensex averaged +0.09% over the next 5 trading days (base rate +0.25%). Win rate 50.8%. That is -0.16 pp below the unconditional baseline. Not statistically significant (p=0.485, q=0.6626 after Benjamini-Hochberg correction).

* When Mercury changed sign (394 events since 2000), Nifty 50 averaged +3.06% over the next 5 trading days (base rate +0.22%). Win rate 69.5%. That is +2.84 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.89e-25).
* When Mercury changed sign (394 events since 2000), Nifty Bank averaged +3.49% over the next 5 trading days (base rate +0.30%). Win rate 68.5%. That is +3.19 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.276e-22).
* When Mercury changed sign (394 events since 2000), Nifty Midcap 100 averaged +0.20% over the next 5 trading days (base rate +0.27%). Win rate 40.4%. That is -0.06 pp below the unconditional baseline. Not statistically significant (p=0.6917, q=0.8183 after Benjamini-Hochberg correction).
* When Mercury changed sign (394 events since 2000), Nifty Midcap 150 averaged +0.73% over the next 5 trading days (base rate +0.26%). Win rate 69.0%. That is +0.47 pp above the unconditional baseline. Statistically significant at p=0.0002803 and after Benjamini-Hochberg correction (q=0.002167).
* When Mercury changed sign (394 events since 2000), BSE Sensex averaged +0.40% over the next 5 trading days (base rate +0.25%). Win rate 58.4%. That is +0.15 pp above the unconditional baseline. Not statistically significant (p=0.3308, q=0.51 after Benjamini-Hochberg correction).

* When Moon changed sign (4302 events since 2000), Nifty 50 averaged +2.95% over the next 5 trading days (base rate +0.22%). Win rate 68.6%. That is +2.74 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.133e-199).
* When Moon changed sign (4302 events since 2000), Nifty Bank averaged +3.36% over the next 5 trading days (base rate +0.30%). Win rate 67.8%. That is +3.06 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.292e-166).
* When Moon changed sign (4302 events since 2000), Nifty Midcap 100 averaged +0.10% over the next 5 trading days (base rate +0.27%). Win rate 39.6%. That is -0.17 pp below the unconditional baseline. Statistically significant at p=0.01304 and after Benjamini-Hochberg correction (q=0.04719).
* When Moon changed sign (4302 events since 2000), Nifty Midcap 150 averaged +0.56% over the next 5 trading days (base rate +0.26%). Win rate 67.0%. That is +0.29 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.512e-05).
* When Moon changed sign (4302 events since 2000), BSE Sensex averaged +0.25% over the next 5 trading days (base rate +0.25%). Win rate 56.2%. Not statistically significant (p=0.9665, q=0.9869 after Benjamini-Hochberg correction).

* When Rahu changed sign (17 events since 2000), Nifty 50 averaged +3.26% over the next 5 trading days (base rate +0.22%). Win rate 76.5%. That is +3.04 pp above the unconditional baseline. Statistically significant at p=0.01399 and after Benjamini-Hochberg correction (q=0.04946).
* When Rahu changed sign (17 events since 2000), Nifty Bank averaged +3.87% over the next 5 trading days (base rate +0.30%). Win rate 70.6%. That is +3.57 pp above the unconditional baseline. Statistically significant at p=0.01152 and after Benjamini-Hochberg correction (q=0.04268).
* When Rahu changed sign (17 events since 2000), Nifty Midcap 100 averaged -0.37% over the next 5 trading days (base rate +0.27%). Win rate 41.2%. That is -0.63 pp below the unconditional baseline. Not statistically significant (p=0.1295, q=0.2638 after Benjamini-Hochberg correction).
* When Rahu changed sign (17 events since 2000), Nifty Midcap 150 averaged +0.84% over the next 5 trading days (base rate +0.26%). Win rate 76.5%. That is +0.58 pp above the unconditional baseline. Not statistically significant (p=0.1251, q=0.2567 after Benjamini-Hochberg correction).
* When Rahu changed sign (17 events since 2000), BSE Sensex averaged +0.10% over the next 5 trading days (base rate +0.25%). Win rate 58.8%. That is -0.15 pp below the unconditional baseline. Not statistically significant (p=0.7718, q=0.8717 after Benjamini-Hochberg correction).

* When Saturn changed sign (23 events since 2000), Nifty 50 averaged +3.90% over the next 5 trading days (base rate +0.22%). Win rate 73.9%. That is +3.68 pp above the unconditional baseline. Statistically significant at p=0.0044 and after Benjamini-Hochberg correction (q=0.0191).
* When Saturn changed sign (23 events since 2000), Nifty Bank averaged +4.75% over the next 5 trading days (base rate +0.30%). Win rate 69.6%. That is +4.45 pp above the unconditional baseline. Statistically significant at p=0.002022 and after Benjamini-Hochberg correction (q=0.01014).
* When Saturn changed sign (23 events since 2000), Nifty Midcap 100 averaged -0.45% over the next 5 trading days (base rate +0.27%). Win rate 21.7%. That is -0.71 pp below the unconditional baseline. Not statistically significant (p=0.1594, q=0.3083 after Benjamini-Hochberg correction).
* When Saturn changed sign (23 events since 2000), Nifty Midcap 150 averaged +0.36% over the next 5 trading days (base rate +0.26%). Win rate 69.6%. That is +0.09 pp above the unconditional baseline. Not statistically significant (p=0.8508, q=0.9192 after Benjamini-Hochberg correction).
* When Saturn changed sign (23 events since 2000), BSE Sensex averaged -0.37% over the next 5 trading days (base rate +0.25%). Win rate 47.8%. That is -0.62 pp below the unconditional baseline. Not statistically significant (p=0.2826, q=0.4582 after Benjamini-Hochberg correction).

* When Sun changed sign (322 events since 2000), Nifty 50 averaged +2.79% over the next 5 trading days (base rate +0.22%). Win rate 67.1%. That is +2.58 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.927e-14).
* When Sun changed sign (322 events since 2000), Nifty Bank averaged +3.23% over the next 5 trading days (base rate +0.30%). Win rate 66.1%. That is +2.93 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.566e-12).
* When Sun changed sign (322 events since 2000), Nifty Midcap 100 averaged -0.02% over the next 5 trading days (base rate +0.27%). Win rate 35.7%. That is -0.29 pp below the unconditional baseline. Not statistically significant (p=0.06101, q=0.1507 after Benjamini-Hochberg correction).
* When Sun changed sign (322 events since 2000), Nifty Midcap 150 averaged +0.41% over the next 5 trading days (base rate +0.26%). Win rate 66.8%. That is +0.14 pp above the unconditional baseline. Not statistically significant (p=0.4451, q=0.6251 after Benjamini-Hochberg correction).
* When Sun changed sign (322 events since 2000), BSE Sensex averaged -0.05% over the next 5 trading days (base rate +0.25%). Win rate 54.0%. That is -0.30 pp below the unconditional baseline. Not statistically significant (p=0.1324, q=0.2687 after Benjamini-Hochberg correction).

* When Venus changed sign (337 events since 2000), Nifty 50 averaged +3.06% over the next 5 trading days (base rate +0.22%). Win rate 69.7%. That is +2.84 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=1.456e-20).
* When Venus changed sign (337 events since 2000), Nifty Bank averaged +3.46% over the next 5 trading days (base rate +0.30%). Win rate 68.2%. That is +3.16 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=2.925e-18).
* When Venus changed sign (337 events since 2000), Nifty Midcap 100 averaged +0.25% over the next 5 trading days (base rate +0.27%). Win rate 41.2%. That is -0.02 pp below the unconditional baseline. Not statistically significant (p=0.922, q=0.9665 after Benjamini-Hochberg correction).
* When Venus changed sign (337 events since 2000), Nifty Midcap 150 averaged +0.63% over the next 5 trading days (base rate +0.26%). Win rate 67.1%. That is +0.37 pp above the unconditional baseline. Statistically significant at p=0.01282 and after Benjamini-Hochberg correction (q=0.04658).
* When Venus changed sign (337 events since 2000), BSE Sensex averaged +0.37% over the next 5 trading days (base rate +0.25%). Win rate 57.6%. That is +0.12 pp above the unconditional baseline. Not statistically significant (p=0.4969, q=0.6739 after Benjamini-Hochberg correction).

**All windows — Sign ingress (Rashi Sankranti)**

| Event | Index | Window | N | Mean ret | Base rate | Excess | Win % | p-value | q (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jupiter Sign Ingress | Nifty 50 | 1 | 40 | 0.4726 | 0.04492 | 0.4277 | 67.5 | 0.007356 | 0.02922 |
| Jupiter Sign Ingress | Nifty 50 | 3 | 40 | 1.355 | 0.1333 | 1.222 | 60 | 0.005555 | 0.02327 |
| Jupiter Sign Ingress | Nifty 50 | 5 | 39 | 1.852 | 0.2178 | 1.634 | 56.41 | 0.02104 | 0.06844 |
| Jupiter Sign Ingress | Nifty 50 | 10 | 39 | 3.165 | 0.4212 | 2.744 | 56.41 | 0.008544 | 0.03317 |
| Jupiter Sign Ingress | Nifty 50 | 20 | 39 | 6.195 | 0.8264 | 5.369 | 76.92 | 0.003216 | 0.01485 |
| Jupiter Sign Ingress | Nifty Bank | 1 | 40 | 0.685 | 0.06023 | 0.6248 | 67.5 | 0.003993 | 0.01774 |
| Jupiter Sign Ingress | Nifty Bank | 3 | 40 | 1.531 | 0.1819 | 1.35 | 67.5 | 0.02421 | 0.07595 |
| Jupiter Sign Ingress | Nifty Bank | 5 | 39 | 2.125 | 0.3 | 1.825 | 61.54 | 0.02277 | 0.07259 |
| Jupiter Sign Ingress | Nifty Bank | 10 | 39 | 3.877 | 0.5834 | 3.293 | 58.97 | 0.01029 | 0.03874 |
| Jupiter Sign Ingress | Nifty Bank | 20 | 39 | 5.555 | 1.172 | 4.383 | 69.23 | 0.01153 | 0.04268 |
| Jupiter Sign Ingress | Nifty Midcap 100 | 1 | 40 | 0.003999 | 0.05397 | -0.04997 | 65 | 0.8474 | 0.9174 |
| Jupiter Sign Ingress | Nifty Midcap 100 | 3 | 40 | -0.1261 | 0.1609 | -0.2869 | 42.5 | 0.4816 | 0.6601 |
| Jupiter Sign Ingress | Nifty Midcap 100 | 5 | 39 | -0.2945 | 0.266 | -0.5605 | 41.03 | 0.255 | 0.4274 |
| Jupiter Sign Ingress | Nifty Midcap 100 | 10 | 39 | 1.106 | 0.532 | 0.5745 | 58.97 | 0.4119 | 0.5939 |
| Jupiter Sign Ingress | Nifty Midcap 100 | 20 | 39 | 2.426 | 1.065 | 1.361 | 69.23 | 0.2229 | 0.3869 |
| Jupiter Sign Ingress | Nifty Midcap 150 | 1 | 40 | 0.5295 | 0.05323 | 0.4763 | 70 | 0.005734 | 0.02392 |
| Jupiter Sign Ingress | Nifty Midcap 150 | 3 | 40 | 0.4998 | 0.1594 | 0.3404 | 60 | 0.2092 | 0.3711 |
| Jupiter Sign Ingress | Nifty Midcap 150 | 5 | 39 | 0.3856 | 0.2642 | 0.1214 | 56.41 | 0.7167 | 0.836 |
| Jupiter Sign Ingress | Nifty Midcap 150 | 10 | 39 | 1.86 | 0.5204 | 1.339 | 56.41 | 0.07411 | 0.1731 |
| Jupiter Sign Ingress | Nifty Midcap 150 | 20 | 39 | 2.428 | 1.047 | 1.381 | 74.36 | 0.1156 | 0.2413 |
| Jupiter Sign Ingress | BSE Sensex | 1 | 40 | 0.3781 | 0.05036 | 0.3277 | 62.5 | 0.03639 | 0.1022 |
| Jupiter Sign Ingress | BSE Sensex | 3 | 40 | 0.6032 | 0.1513 | 0.4518 | 62.5 | 0.1329 | 0.2693 |
| Jupiter Sign Ingress | BSE Sensex | 5 | 39 | 0.1765 | 0.2506 | -0.07409 | 48.72 | 0.8258 | 0.9052 |
| Jupiter Sign Ingress | BSE Sensex | 10 | 39 | 1.136 | 0.4957 | 0.6407 | 51.28 | 0.3589 | 0.5398 |
| Jupiter Sign Ingress | BSE Sensex | 20 | 39 | 1.672 | 1.002 | 0.6707 | 61.54 | 0.4749 | 0.6521 |
| Ketu Sign Ingress | Nifty 50 | 1 | 17 | 0.05549 | 0.04492 | 0.01057 | 47.06 | 0.9712 | 0.9891 |
| Ketu Sign Ingress | Nifty 50 | 3 | 17 | 1.591 | 0.1333 | 1.458 | 64.71 | 0.06489 | 0.1568 |
| Ketu Sign Ingress | Nifty 50 | 5 | 17 | 3.255 | 0.2178 | 3.037 | 76.47 | 0.01399 | 0.04946 |
| Ketu Sign Ingress | Nifty 50 | 10 | 17 | 4.178 | 0.4212 | 3.757 | 70.59 | 0.02835 | 0.0852 |
| Ketu Sign Ingress | Nifty 50 | 20 | 17 | 7.982 | 0.8264 | 7.155 | 76.47 | 0.03591 | 0.1013 |
| Ketu Sign Ingress | Nifty Bank | 1 | 17 | 0.5775 | 0.06023 | 0.5172 | 47.06 | 0.284 | 0.4596 |
| Ketu Sign Ingress | Nifty Bank | 3 | 17 | 2.454 | 0.1819 | 2.272 | 70.59 | 0.02484 | 0.07724 |
| Ketu Sign Ingress | Nifty Bank | 5 | 17 | 3.869 | 0.3 | 3.569 | 70.59 | 0.01152 | 0.04268 |
| Ketu Sign Ingress | Nifty Bank | 10 | 17 | 5.471 | 0.5834 | 4.887 | 70.59 | 0.02058 | 0.06728 |
| Ketu Sign Ingress | Nifty Bank | 20 | 17 | 6.74 | 1.172 | 5.567 | 76.47 | 0.09074 | 0.2018 |
| Ketu Sign Ingress | Nifty Midcap 100 | 1 | 17 | -0.3733 | 0.05397 | -0.4273 | 41.18 | 0.1776 | 0.3313 |
| Ketu Sign Ingress | Nifty Midcap 100 | 3 | 17 | -0.617 | 0.1609 | -0.7778 | 23.53 | 0.1142 | 0.2391 |
| Ketu Sign Ingress | Nifty Midcap 100 | 5 | 17 | -0.3651 | 0.266 | -0.6311 | 41.18 | 0.1295 | 0.2638 |
| Ketu Sign Ingress | Nifty Midcap 100 | 10 | 17 | 1.23 | 0.532 | 0.6981 | 58.82 | 0.5635 | 0.7258 |
| Ketu Sign Ingress | Nifty Midcap 100 | 20 | 17 | 3.242 | 1.065 | 2.177 | 88.24 | 0.1717 | 0.3255 |
| Ketu Sign Ingress | Nifty Midcap 150 | 1 | 17 | 0.213 | 0.05323 | 0.1598 | 47.06 | 0.6353 | 0.7799 |
| Ketu Sign Ingress | Nifty Midcap 150 | 3 | 17 | 0.2518 | 0.1594 | 0.0924 | 64.71 | 0.8108 | 0.8947 |
| Ketu Sign Ingress | Nifty Midcap 150 | 5 | 17 | 0.8419 | 0.2642 | 0.5777 | 76.47 | 0.1251 | 0.2567 |
| Ketu Sign Ingress | Nifty Midcap 150 | 10 | 17 | 2.011 | 0.5204 | 1.491 | 70.59 | 0.112 | 0.2361 |
| Ketu Sign Ingress | Nifty Midcap 150 | 20 | 17 | 1.799 | 1.047 | 0.7519 | 76.47 | 0.5626 | 0.7258 |
| Ketu Sign Ingress | BSE Sensex | 1 | 17 | -0.3973 | 0.05036 | -0.4477 | 23.53 | 0.148 | 0.2916 |
| Ketu Sign Ingress | BSE Sensex | 3 | 17 | -0.1502 | 0.1513 | -0.3015 | 47.06 | 0.4777 | 0.6552 |
| Ketu Sign Ingress | BSE Sensex | 5 | 17 | 0.09859 | 0.2506 | -0.152 | 58.82 | 0.7718 | 0.8717 |
| Ketu Sign Ingress | BSE Sensex | 10 | 17 | 0.1991 | 0.4957 | -0.2965 | 58.82 | 0.737 | 0.8481 |
| Ketu Sign Ingress | BSE Sensex | 20 | 17 | 1.002 | 1.002 | 0.0003801 | 58.82 | 0.9998 | 0.9998 |
| Mars Sign Ingress | Nifty 50 | 1 | 185 | 0.2895 | 0.04492 | 0.2446 | 69.19 | 0.007932 | 0.03128 |
| Mars Sign Ingress | Nifty 50 | 3 | 185 | 1.739 | 0.1333 | 1.605 | 65.95 | 2.257e-10 | 1.485e-08 |
| Mars Sign Ingress | Nifty 50 | 5 | 185 | 2.851 | 0.2178 | 2.633 | 65.41 | 3.478e-11 | 2.557e-09 |
| Mars Sign Ingress | Nifty 50 | 10 | 185 | 4.172 | 0.4212 | 3.75 | 72.97 | 3.211e-13 | 2.618e-11 |
| Mars Sign Ingress | Nifty 50 | 20 | 185 | 8.178 | 0.8264 | 7.352 | 71.89 | 4.66e-13 | 3.718e-11 |
| Mars Sign Ingress | Nifty Bank | 1 | 185 | 0.7141 | 0.06023 | 0.6538 | 66.49 | 8.351e-07 | 2.06e-05 |
| Mars Sign Ingress | Nifty Bank | 3 | 185 | 2.339 | 0.1819 | 2.157 | 68.65 | 1.284e-11 | 9.631e-10 |
| Mars Sign Ingress | Nifty Bank | 5 | 185 | 3.315 | 0.3 | 3.015 | 67.03 | 3.748e-11 | 2.703e-09 |
| Mars Sign Ingress | Nifty Bank | 10 | 185 | 5.289 | 0.5834 | 4.706 | 71.35 | 1.984e-13 | 1.691e-11 |
| Mars Sign Ingress | Nifty Bank | 20 | 185 | 7.289 | 1.172 | 6.116 | 72.97 | 6.783e-11 | 4.624e-09 |
| Mars Sign Ingress | Nifty Midcap 100 | 1 | 185 | -0.1046 | 0.05397 | -0.1586 | 63.24 | 0.08439 | 0.1902 |
| Mars Sign Ingress | Nifty Midcap 100 | 3 | 185 | -0.05815 | 0.1609 | -0.219 | 35.68 | 0.2143 | 0.3778 |
| Mars Sign Ingress | Nifty Midcap 100 | 5 | 185 | -0.03209 | 0.266 | -0.2981 | 34.05 | 0.1994 | 0.3599 |
| Mars Sign Ingress | Nifty Midcap 100 | 10 | 185 | 1.701 | 0.532 | 1.169 | 67.57 | 0.000855 | 0.005205 |
| Mars Sign Ingress | Nifty Midcap 100 | 20 | 185 | 2.608 | 1.065 | 1.543 | 66.49 | 0.003874 | 0.01726 |
| Mars Sign Ingress | Nifty Midcap 150 | 1 | 185 | 0.3193 | 0.05323 | 0.2661 | 66.49 | 0.0118 | 0.0434 |
| Mars Sign Ingress | Nifty Midcap 150 | 3 | 185 | 0.2433 | 0.1594 | 0.08391 | 63.78 | 0.6056 | 0.756 |
| Mars Sign Ingress | Nifty Midcap 150 | 5 | 185 | 0.3853 | 0.2642 | 0.121 | 63.78 | 0.5612 | 0.7254 |
| Mars Sign Ingress | Nifty Midcap 150 | 10 | 185 | 1.711 | 0.5204 | 1.191 | 71.89 | 0.0004057 | 0.002925 |
| Mars Sign Ingress | Nifty Midcap 150 | 20 | 185 | 2.009 | 1.047 | 0.9616 | 71.89 | 0.04239 | 0.1131 |
| Mars Sign Ingress | BSE Sensex | 1 | 185 | -0.01587 | 0.05036 | -0.06623 | 53.51 | 0.5235 | 0.6959 |
| Mars Sign Ingress | BSE Sensex | 3 | 185 | 0.202 | 0.1513 | 0.0507 | 55.68 | 0.7893 | 0.881 |
| Mars Sign Ingress | BSE Sensex | 5 | 185 | 0.0872 | 0.2506 | -0.1634 | 50.81 | 0.485 | 0.6626 |
| Mars Sign Ingress | BSE Sensex | 10 | 185 | 0.548 | 0.4957 | 0.05229 | 60.54 | 0.875 | 0.9367 |
| Mars Sign Ingress | BSE Sensex | 20 | 185 | 0.8457 | 1.002 | -0.156 | 61.08 | 0.7634 | 0.8654 |
| Mercury Sign Ingress | Nifty 50 | 1 | 394 | 0.3647 | 0.04492 | 0.3198 | 65.23 | 6.026e-09 | 3.096e-07 |
| Mercury Sign Ingress | Nifty 50 | 3 | 394 | 1.803 | 0.1333 | 1.67 | 68.27 | 1.994e-25 | 3.936e-23 |
| Mercury Sign Ingress | Nifty 50 | 5 | 394 | 3.058 | 0.2178 | 2.84 | 69.54 | 7.562e-28 | 1.89e-25 |
| Mercury Sign Ingress | Nifty 50 | 10 | 394 | 4.19 | 0.4212 | 3.768 | 71.57 | 2.218e-28 | 5.941e-26 |
| Mercury Sign Ingress | Nifty 50 | 20 | 394 | 8.284 | 0.8264 | 7.458 | 70.81 | 6.599e-29 | 1.904e-26 |
| Mercury Sign Ingress | Nifty Bank | 1 | 394 | 0.7545 | 0.06023 | 0.6943 | 65.74 | 2.909e-15 | 3.03e-13 |
| Mercury Sign Ingress | Nifty Bank | 3 | 394 | 2.315 | 0.1819 | 2.133 | 68.27 | 1.183e-23 | 2.112e-21 |
| Mercury Sign Ingress | Nifty Bank | 5 | 394 | 3.487 | 0.3 | 3.187 | 68.53 | 6.807e-25 | 1.276e-22 |
| Mercury Sign Ingress | Nifty Bank | 10 | 394 | 5.238 | 0.5834 | 4.655 | 70.3 | 4.994e-27 | 1.171e-24 |
| Mercury Sign Ingress | Nifty Bank | 20 | 394 | 7.729 | 1.172 | 6.557 | 70.56 | 9.817e-26 | 2.045e-23 |
| Mercury Sign Ingress | Nifty Midcap 100 | 1 | 394 | 0.05568 | 0.05397 | 0.001713 | 64.97 | 0.9781 | 0.9911 |
| Mercury Sign Ingress | Nifty Midcap 100 | 3 | 394 | 0.1503 | 0.1609 | -0.01054 | 40.86 | 0.9305 | 0.9709 |
| Mercury Sign Ingress | Nifty Midcap 100 | 5 | 394 | 0.204 | 0.266 | -0.06203 | 40.36 | 0.6917 | 0.8183 |
| Mercury Sign Ingress | Nifty Midcap 100 | 10 | 394 | 1.695 | 0.532 | 1.163 | 70.81 | 6.291e-07 | 1.594e-05 |
| Mercury Sign Ingress | Nifty Midcap 100 | 20 | 394 | 2.489 | 1.065 | 1.424 | 69.8 | 1.237e-05 | 0.000191 |
| Mercury Sign Ingress | Nifty Midcap 150 | 1 | 394 | 0.4502 | 0.05323 | 0.3969 | 65.23 | 6.592e-10 | 4.052e-08 |
| Mercury Sign Ingress | Nifty Midcap 150 | 3 | 394 | 0.3909 | 0.1594 | 0.2315 | 68.27 | 0.02008 | 0.06611 |
| Mercury Sign Ingress | Nifty Midcap 150 | 5 | 394 | 0.7312 | 0.2642 | 0.467 | 69.04 | 0.0002803 | 0.002167 |
| Mercury Sign Ingress | Nifty Midcap 150 | 10 | 394 | 1.868 | 0.5204 | 1.347 | 68.78 | 6.736e-11 | 4.624e-09 |
| Mercury Sign Ingress | Nifty Midcap 150 | 20 | 394 | 2.182 | 1.047 | 1.134 | 70.3 | 6.131e-05 | 0.0006802 |
| Mercury Sign Ingress | BSE Sensex | 1 | 394 | 0.1237 | 0.05036 | 0.07338 | 55.84 | 0.2502 | 0.421 |
| Mercury Sign Ingress | BSE Sensex | 3 | 394 | 0.291 | 0.1513 | 0.1397 | 57.61 | 0.2205 | 0.3854 |
| Mercury Sign Ingress | BSE Sensex | 5 | 394 | 0.4025 | 0.2506 | 0.1519 | 58.38 | 0.3308 | 0.51 |
| Mercury Sign Ingress | BSE Sensex | 10 | 394 | 0.7637 | 0.4957 | 0.268 | 60.91 | 0.2001 | 0.3606 |
| Mercury Sign Ingress | BSE Sensex | 20 | 394 | 1.158 | 1.002 | 0.1563 | 58.88 | 0.6231 | 0.7701 |
| Moon Sign Ingress | Nifty 50 | 1 | 4305 | 0.3734 | 0.04492 | 0.3285 | 66.41 | 1.032e-35 | 3.226e-33 |
| Moon Sign Ingress | Nifty 50 | 3 | 4304 | 1.711 | 0.1333 | 1.578 | 67.57 | 8.809e-155 | 4.719e-152 |
| Moon Sign Ingress | Nifty 50 | 5 | 4302 | 2.953 | 0.2178 | 2.735 | 68.64 | 6.041e-203 | 1.133e-199 |
| Moon Sign Ingress | Nifty 50 | 10 | 4299 | 3.982 | 0.4212 | 3.561 | 69.57 | 1.481e-194 | 1.852e-191 |
| Moon Sign Ingress | Nifty 50 | 20 | 4293 | 8.114 | 0.8264 | 7.288 | 71.28 | 1.839e-243 | 6.897e-240 |
| Moon Sign Ingress | Nifty Bank | 1 | 4305 | 0.7226 | 0.06023 | 0.6623 | 65.97 | 2.282e-71 | 9.507e-69 |
| Moon Sign Ingress | Nifty Bank | 3 | 4304 | 2.19 | 0.1819 | 2.008 | 66.89 | 1.037e-143 | 4.862e-141 |
| Moon Sign Ingress | Nifty Bank | 5 | 4302 | 3.363 | 0.3 | 3.063 | 67.76 | 5.267e-169 | 3.292e-166 |
| Moon Sign Ingress | Nifty Bank | 10 | 4299 | 4.971 | 0.5834 | 4.388 | 68.9 | 2.206e-175 | 2.068e-172 |
| Moon Sign Ingress | Nifty Bank | 20 | 4293 | 7.352 | 1.172 | 6.18 | 70.09 | 4.784e-170 | 3.588e-167 |
| Moon Sign Ingress | Nifty Midcap 100 | 1 | 4305 | 0.06843 | 0.05397 | 0.01447 | 65.64 | 0.6331 | 0.7784 |
| Moon Sign Ingress | Nifty Midcap 100 | 3 | 4304 | 0.0595 | 0.1609 | -0.1014 | 39.27 | 0.05152 | 0.1312 |
| Moon Sign Ingress | Nifty Midcap 100 | 5 | 4302 | 0.1006 | 0.266 | -0.1654 | 39.61 | 0.01304 | 0.04719 |
| Moon Sign Ingress | Nifty Midcap 100 | 10 | 4299 | 1.577 | 0.532 | 1.045 | 69.16 | 1.226e-26 | 2.704e-24 |
| Moon Sign Ingress | Nifty Midcap 100 | 20 | 4293 | 2.411 | 1.065 | 1.346 | 69.79 | 5.657e-21 | 7.577e-19 |
| Moon Sign Ingress | Nifty Midcap 150 | 1 | 4305 | 0.4288 | 0.05323 | 0.3756 | 64.65 | 2.614e-42 | 9.801e-40 |
| Moon Sign Ingress | Nifty Midcap 150 | 3 | 4304 | 0.2523 | 0.1594 | 0.09289 | 65.57 | 0.0381 | 0.1054 |
| Moon Sign Ingress | Nifty Midcap 150 | 5 | 4302 | 0.5583 | 0.2642 | 0.2941 | 66.97 | 5.888e-07 | 1.512e-05 |
| Moon Sign Ingress | Nifty Midcap 150 | 10 | 4299 | 1.656 | 0.5204 | 1.135 | 67.88 | 1.537e-38 | 5.238e-36 |
| Moon Sign Ingress | Nifty Midcap 150 | 20 | 4293 | 1.962 | 1.047 | 0.915 | 70.11 | 7.04e-14 | 6.6e-12 |
| Moon Sign Ingress | BSE Sensex | 1 | 4305 | 0.05787 | 0.05036 | 0.007514 | 53.47 | 0.7781 | 0.8736 |
| Moon Sign Ingress | BSE Sensex | 3 | 4304 | 0.1577 | 0.1513 | 0.006426 | 55.46 | 0.8913 | 0.9455 |
| Moon Sign Ingress | BSE Sensex | 5 | 4302 | 0.248 | 0.2506 | -0.002585 | 56.23 | 0.9665 | 0.9869 |
| Moon Sign Ingress | BSE Sensex | 10 | 4299 | 0.4969 | 0.4957 | 0.001266 | 58.13 | 0.9882 | 0.9956 |
| Moon Sign Ingress | BSE Sensex | 20 | 4293 | 1.008 | 1.002 | 0.006655 | 60.03 | 0.9573 | 0.9826 |
| Rahu Sign Ingress | Nifty 50 | 1 | 17 | 0.05549 | 0.04492 | 0.01057 | 47.06 | 0.9712 | 0.9891 |
| Rahu Sign Ingress | Nifty 50 | 3 | 17 | 1.591 | 0.1333 | 1.458 | 64.71 | 0.06489 | 0.1568 |
| Rahu Sign Ingress | Nifty 50 | 5 | 17 | 3.255 | 0.2178 | 3.037 | 76.47 | 0.01399 | 0.04946 |
| Rahu Sign Ingress | Nifty 50 | 10 | 17 | 4.178 | 0.4212 | 3.757 | 70.59 | 0.02835 | 0.0852 |
| Rahu Sign Ingress | Nifty 50 | 20 | 17 | 7.982 | 0.8264 | 7.155 | 76.47 | 0.03591 | 0.1013 |
| Rahu Sign Ingress | Nifty Bank | 1 | 17 | 0.5775 | 0.06023 | 0.5172 | 47.06 | 0.284 | 0.4596 |
| Rahu Sign Ingress | Nifty Bank | 3 | 17 | 2.454 | 0.1819 | 2.272 | 70.59 | 0.02484 | 0.07724 |
| Rahu Sign Ingress | Nifty Bank | 5 | 17 | 3.869 | 0.3 | 3.569 | 70.59 | 0.01152 | 0.04268 |
| Rahu Sign Ingress | Nifty Bank | 10 | 17 | 5.471 | 0.5834 | 4.887 | 70.59 | 0.02058 | 0.06728 |
| Rahu Sign Ingress | Nifty Bank | 20 | 17 | 6.74 | 1.172 | 5.567 | 76.47 | 0.09074 | 0.2018 |
| Rahu Sign Ingress | Nifty Midcap 100 | 1 | 17 | -0.3733 | 0.05397 | -0.4273 | 41.18 | 0.1776 | 0.3313 |
| Rahu Sign Ingress | Nifty Midcap 100 | 3 | 17 | -0.617 | 0.1609 | -0.7778 | 23.53 | 0.1142 | 0.2391 |
| Rahu Sign Ingress | Nifty Midcap 100 | 5 | 17 | -0.3651 | 0.266 | -0.6311 | 41.18 | 0.1295 | 0.2638 |
| Rahu Sign Ingress | Nifty Midcap 100 | 10 | 17 | 1.23 | 0.532 | 0.6981 | 58.82 | 0.5635 | 0.7258 |
| Rahu Sign Ingress | Nifty Midcap 100 | 20 | 17 | 3.242 | 1.065 | 2.177 | 88.24 | 0.1717 | 0.3255 |
| Rahu Sign Ingress | Nifty Midcap 150 | 1 | 17 | 0.213 | 0.05323 | 0.1598 | 47.06 | 0.6353 | 0.7799 |
| Rahu Sign Ingress | Nifty Midcap 150 | 3 | 17 | 0.2518 | 0.1594 | 0.0924 | 64.71 | 0.8108 | 0.8947 |
| Rahu Sign Ingress | Nifty Midcap 150 | 5 | 17 | 0.8419 | 0.2642 | 0.5777 | 76.47 | 0.1251 | 0.2567 |
| Rahu Sign Ingress | Nifty Midcap 150 | 10 | 17 | 2.011 | 0.5204 | 1.491 | 70.59 | 0.112 | 0.2361 |
| Rahu Sign Ingress | Nifty Midcap 150 | 20 | 17 | 1.799 | 1.047 | 0.7519 | 76.47 | 0.5626 | 0.7258 |
| Rahu Sign Ingress | BSE Sensex | 1 | 17 | -0.3973 | 0.05036 | -0.4477 | 23.53 | 0.148 | 0.2916 |
| Rahu Sign Ingress | BSE Sensex | 3 | 17 | -0.1502 | 0.1513 | -0.3015 | 47.06 | 0.4777 | 0.6552 |
| Rahu Sign Ingress | BSE Sensex | 5 | 17 | 0.09859 | 0.2506 | -0.152 | 58.82 | 0.7718 | 0.8717 |
| Rahu Sign Ingress | BSE Sensex | 10 | 17 | 0.1991 | 0.4957 | -0.2965 | 58.82 | 0.737 | 0.8481 |
| Rahu Sign Ingress | BSE Sensex | 20 | 17 | 1.002 | 1.002 | 0.0003801 | 58.82 | 0.9998 | 0.9998 |
| Saturn Sign Ingress | Nifty 50 | 1 | 23 | 0.4615 | 0.04492 | 0.4166 | 65.22 | 0.01382 | 0.04913 |
| Saturn Sign Ingress | Nifty 50 | 3 | 23 | 2.186 | 0.1333 | 2.052 | 65.22 | 0.006039 | 0.02491 |
| Saturn Sign Ingress | Nifty 50 | 5 | 23 | 3.899 | 0.2178 | 3.681 | 73.91 | 0.0044 | 0.0191 |
| Saturn Sign Ingress | Nifty 50 | 10 | 23 | 5.493 | 0.4212 | 5.072 | 78.26 | 0.002022 | 0.01014 |
| Saturn Sign Ingress | Nifty 50 | 20 | 23 | 12.18 | 0.8264 | 11.36 | 78.26 | 0.0003467 | 0.002575 |
| Saturn Sign Ingress | Nifty Bank | 1 | 23 | 1.058 | 0.06023 | 0.9982 | 69.57 | 0.001598 | 0.008509 |
| Saturn Sign Ingress | Nifty Bank | 3 | 23 | 3.215 | 0.1819 | 3.033 | 69.57 | 0.001096 | 0.006383 |
| Saturn Sign Ingress | Nifty Bank | 5 | 23 | 4.75 | 0.3 | 4.45 | 69.57 | 0.002022 | 0.01014 |
| Saturn Sign Ingress | Nifty Bank | 10 | 23 | 7.375 | 0.5834 | 6.791 | 78.26 | 0.0006836 | 0.004352 |
| Saturn Sign Ingress | Nifty Bank | 20 | 23 | 11.78 | 1.172 | 10.61 | 78.26 | 0.0001224 | 0.001157 |
| Saturn Sign Ingress | Nifty Midcap 100 | 1 | 23 | 0.0396 | 0.05397 | -0.01437 | 65.22 | 0.9164 | 0.9629 |
| Saturn Sign Ingress | Nifty Midcap 100 | 3 | 23 | -0.618 | 0.1609 | -0.7788 | 21.74 | 0.0718 | 0.1692 |
| Saturn Sign Ingress | Nifty Midcap 100 | 5 | 23 | -0.446 | 0.266 | -0.712 | 21.74 | 0.1594 | 0.3083 |
| Saturn Sign Ingress | Nifty Midcap 100 | 10 | 23 | 2.011 | 0.532 | 1.479 | 78.26 | 0.07339 | 0.1719 |
| Saturn Sign Ingress | Nifty Midcap 100 | 20 | 23 | 4.228 | 1.065 | 3.163 | 91.3 | 9.818e-05 | 0.0009638 |
| Saturn Sign Ingress | Nifty Midcap 150 | 1 | 23 | 0.6137 | 0.05323 | 0.5604 | 65.22 | 0.01652 | 0.05677 |
| Saturn Sign Ingress | Nifty Midcap 150 | 3 | 23 | 0.1949 | 0.1594 | 0.03549 | 69.57 | 0.9028 | 0.9551 |
| Saturn Sign Ingress | Nifty Midcap 150 | 5 | 23 | 0.3587 | 0.2642 | 0.0945 | 69.57 | 0.8508 | 0.9192 |
| Saturn Sign Ingress | Nifty Midcap 150 | 10 | 23 | 1.876 | 0.5204 | 1.355 | 78.26 | 0.107 | 0.2276 |
| Saturn Sign Ingress | Nifty Midcap 150 | 20 | 23 | 2.513 | 1.047 | 1.466 | 73.91 | 0.09715 | 0.2119 |
| Saturn Sign Ingress | BSE Sensex | 1 | 23 | 0.1509 | 0.05036 | 0.1005 | 56.52 | 0.6763 | 0.8085 |
| Saturn Sign Ingress | BSE Sensex | 3 | 23 | -0.3183 | 0.1513 | -0.4696 | 52.17 | 0.288 | 0.4628 |
| Saturn Sign Ingress | BSE Sensex | 5 | 23 | -0.3734 | 0.2506 | -0.6239 | 47.83 | 0.2826 | 0.4582 |
| Saturn Sign Ingress | BSE Sensex | 10 | 23 | 0.5362 | 0.4957 | 0.04055 | 65.22 | 0.9588 | 0.9832 |
| Saturn Sign Ingress | BSE Sensex | 20 | 23 | 2.157 | 1.002 | 1.156 | 65.22 | 0.2645 | 0.4383 |
| Sun Sign Ingress | Nifty 50 | 1 | 322 | 0.4018 | 0.04492 | 0.3569 | 65.22 | 4.552e-05 | 0.0005236 |
| Sun Sign Ingress | Nifty 50 | 3 | 322 | 1.626 | 0.1333 | 1.493 | 66.15 | 2.184e-14 | 2.214e-12 |
| Sun Sign Ingress | Nifty 50 | 5 | 322 | 2.795 | 0.2178 | 2.577 | 67.08 | 3.665e-16 | 3.927e-14 |
| Sun Sign Ingress | Nifty 50 | 10 | 322 | 4.104 | 0.4212 | 3.683 | 69.88 | 1.435e-21 | 1.993e-19 |
| Sun Sign Ingress | Nifty 50 | 20 | 321 | 8.159 | 0.8264 | 7.332 | 71.34 | 2.658e-22 | 3.987e-20 |
| Sun Sign Ingress | Nifty Bank | 1 | 322 | 0.7955 | 0.06023 | 0.7352 | 67.7 | 7.564e-10 | 4.502e-08 |
| Sun Sign Ingress | Nifty Bank | 3 | 322 | 2.136 | 0.1819 | 1.954 | 62.73 | 1.179e-13 | 1.053e-11 |
| Sun Sign Ingress | Nifty Bank | 5 | 322 | 3.226 | 0.3 | 2.926 | 66.15 | 3.614e-14 | 3.566e-12 |
| Sun Sign Ingress | Nifty Bank | 10 | 322 | 5.056 | 0.5834 | 4.473 | 69.88 | 1.541e-19 | 1.926e-17 |
| Sun Sign Ingress | Nifty Bank | 20 | 321 | 7.471 | 1.172 | 6.299 | 71.96 | 4.234e-19 | 4.811e-17 |
| Sun Sign Ingress | Nifty Midcap 100 | 1 | 322 | 0.06323 | 0.05397 | 0.009269 | 66.46 | 0.9125 | 0.9606 |
| Sun Sign Ingress | Nifty Midcap 100 | 3 | 322 | -0.0638 | 0.1609 | -0.2247 | 39.13 | 0.0708 | 0.1673 |
| Sun Sign Ingress | Nifty Midcap 100 | 5 | 322 | -0.02377 | 0.266 | -0.2898 | 35.71 | 0.06101 | 0.1507 |
| Sun Sign Ingress | Nifty Midcap 100 | 10 | 322 | 1.689 | 0.532 | 1.157 | 70.19 | 5.154e-07 | 1.371e-05 |
| Sun Sign Ingress | Nifty Midcap 100 | 20 | 321 | 2.364 | 1.065 | 1.299 | 70.4 | 0.0005073 | 0.003504 |
| Sun Sign Ingress | Nifty Midcap 150 | 1 | 322 | 0.4663 | 0.05323 | 0.4131 | 63.35 | 8.532e-06 | 0.0001385 |
| Sun Sign Ingress | Nifty Midcap 150 | 3 | 322 | 0.1821 | 0.1594 | 0.02266 | 64.6 | 0.8588 | 0.9246 |
| Sun Sign Ingress | Nifty Midcap 150 | 5 | 322 | 0.4073 | 0.2642 | 0.143 | 66.77 | 0.4451 | 0.6251 |
| Sun Sign Ingress | Nifty Midcap 150 | 10 | 322 | 1.835 | 0.5204 | 1.315 | 68.32 | 2.712e-08 | 1.211e-06 |
| Sun Sign Ingress | Nifty Midcap 150 | 20 | 321 | 2.018 | 1.047 | 0.9702 | 69.16 | 0.003711 | 0.01671 |
| Sun Sign Ingress | BSE Sensex | 1 | 322 | 0.03507 | 0.05036 | -0.01529 | 50.31 | 0.8746 | 0.9366 |
| Sun Sign Ingress | BSE Sensex | 3 | 322 | 0.03599 | 0.1513 | -0.1153 | 50.31 | 0.4072 | 0.5894 |
| Sun Sign Ingress | BSE Sensex | 5 | 322 | -0.04855 | 0.2506 | -0.2991 | 54.04 | 0.1324 | 0.2687 |
| Sun Sign Ingress | BSE Sensex | 10 | 322 | 0.6914 | 0.4957 | 0.1958 | 58.7 | 0.3931 | 0.5768 |
| Sun Sign Ingress | BSE Sensex | 20 | 321 | 1.116 | 1.002 | 0.1145 | 60.75 | 0.7566 | 0.8597 |
| Venus Sign Ingress | Nifty 50 | 1 | 337 | 0.4346 | 0.04492 | 0.3897 | 66.47 | 1.788e-08 | 8.597e-07 |
| Venus Sign Ingress | Nifty 50 | 3 | 337 | 1.884 | 0.1333 | 1.751 | 72.4 | 1.155e-22 | 1.805e-20 |
| Venus Sign Ingress | Nifty 50 | 5 | 337 | 3.061 | 0.2178 | 2.843 | 69.73 | 8.929e-23 | 1.456e-20 |
| Venus Sign Ingress | Nifty 50 | 10 | 337 | 4.001 | 0.4212 | 3.579 | 69.14 | 1.6e-19 | 1.936e-17 |
| Venus Sign Ingress | Nifty 50 | 20 | 337 | 8.109 | 0.8264 | 7.283 | 68.84 | 5.174e-23 | 8.82e-21 |
| Venus Sign Ingress | Nifty Bank | 1 | 337 | 0.7692 | 0.06023 | 0.709 | 66.17 | 7.509e-14 | 6.868e-12 |
| Venus Sign Ingress | Nifty Bank | 3 | 337 | 2.376 | 0.1819 | 2.194 | 71.22 | 1.416e-21 | 1.993e-19 |
| Venus Sign Ingress | Nifty Bank | 5 | 337 | 3.46 | 0.3 | 3.16 | 68.25 | 2.262e-20 | 2.925e-18 |
| Venus Sign Ingress | Nifty Bank | 10 | 337 | 4.986 | 0.5834 | 4.403 | 69.14 | 1.028e-18 | 1.134e-16 |
| Venus Sign Ingress | Nifty Bank | 20 | 337 | 7.346 | 1.172 | 6.173 | 68.84 | 3.28e-19 | 3.844e-17 |
| Venus Sign Ingress | Nifty Midcap 100 | 1 | 337 | 0.07621 | 0.05397 | 0.02224 | 66.17 | 0.7763 | 0.8736 |
| Venus Sign Ingress | Nifty Midcap 100 | 3 | 337 | 0.1198 | 0.1609 | -0.04106 | 41.84 | 0.756 | 0.8596 |
| Venus Sign Ingress | Nifty Midcap 100 | 5 | 337 | 0.2496 | 0.266 | -0.01642 | 41.25 | 0.922 | 0.9665 |
| Venus Sign Ingress | Nifty Midcap 100 | 10 | 337 | 1.612 | 0.532 | 1.08 | 74.18 | 3.853e-05 | 0.0004572 |
| Venus Sign Ingress | Nifty Midcap 100 | 20 | 337 | 2.281 | 1.065 | 1.217 | 70.33 | 0.0006083 | 0.003958 |
| Venus Sign Ingress | Nifty Midcap 150 | 1 | 337 | 0.4768 | 0.05323 | 0.4236 | 65.28 | 5.31e-08 | 2.096e-06 |
| Venus Sign Ingress | Nifty Midcap 150 | 3 | 337 | 0.3938 | 0.1594 | 0.2343 | 70.62 | 0.03374 | 0.09642 |
| Venus Sign Ingress | Nifty Midcap 150 | 5 | 337 | 0.6305 | 0.2642 | 0.3663 | 67.06 | 0.01282 | 0.04658 |
| Venus Sign Ingress | Nifty Midcap 150 | 10 | 337 | 1.637 | 0.5204 | 1.117 | 68.25 | 1.326e-05 | 0.000203 |
| Venus Sign Ingress | Nifty Midcap 150 | 20 | 337 | 1.827 | 1.047 | 0.7799 | 67.95 | 0.01069 | 0.04018 |
| Venus Sign Ingress | BSE Sensex | 1 | 337 | 0.1068 | 0.05036 | 0.0564 | 55.49 | 0.4635 | 0.6414 |
| Venus Sign Ingress | BSE Sensex | 3 | 337 | 0.3084 | 0.1513 | 0.1571 | 60.53 | 0.2216 | 0.386 |
| Venus Sign Ingress | BSE Sensex | 5 | 337 | 0.3659 | 0.2506 | 0.1153 | 57.57 | 0.4969 | 0.6739 |
| Venus Sign Ingress | BSE Sensex | 10 | 337 | 0.5859 | 0.4957 | 0.09028 | 58.75 | 0.7239 | 0.8398 |
| Venus Sign Ingress | BSE Sensex | 20 | 337 | 0.9727 | 1.002 | -0.02895 | 59.35 | 0.9335 | 0.9724 |

## 5. Highlights

Only combinations with at least 10 observations that survive Benjamini-Hochberg correction at q<0.05 are listed below.

### Strongest positive findings

* When Jupiter opposed Mars (20 events since 2001), Nifty Bank averaged +6.08% over the next 5 trading days (base rate +0.30%). Win rate 80.0%. That is +5.78 pp above the unconditional baseline. Statistically significant at p=0.0001187 and after Benjamini-Hochberg correction (q=0.001129).
* When Mars opposed Venus (12 events since 2001), Nifty Bank averaged +5.39% over the next 5 trading days (base rate +0.30%). Win rate 83.3%. That is +5.09 pp above the unconditional baseline. Statistically significant at p=0.00386 and after Benjamini-Hochberg correction (q=0.01725).
* When Mars conjoined Sun (13 events since 2000), Nifty Bank averaged +5.36% over the next 5 trading days (base rate +0.30%). Win rate 92.3%. That is +5.06 pp above the unconditional baseline. Statistically significant at p=0.001902 and after Benjamini-Hochberg correction (q=0.009772).
* When Jupiter opposed Venus (24 events since 2000), Nifty Bank averaged +5.20% over the next 5 trading days (base rate +0.30%). Win rate 91.7%. That is +4.90 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.000275).
* When Jupiter opposed Mars (20 events since 2001), Nifty 50 averaged +5.08% over the next 5 trading days (base rate +0.22%). Win rate 80.0%. That is +4.86 pp above the unconditional baseline. Statistically significant at p=0.00041 and after Benjamini-Hochberg correction (q=0.002945).
* When Venus turned direct (16 events since 2001), Nifty Bank averaged +5.06% over the next 5 trading days (base rate +0.30%). Win rate 93.8%. That is +4.76 pp above the unconditional baseline. Statistically significant at p=0.00123 and after Benjamini-Hochberg correction (q=0.006989).
* When Saturn changed sign (23 events since 2000), Nifty Bank averaged +4.75% over the next 5 trading days (base rate +0.30%). Win rate 69.6%. That is +4.45 pp above the unconditional baseline. Statistically significant at p=0.002022 and after Benjamini-Hochberg correction (q=0.01014).
* When Mercury opposed Saturn (28 events since 2000), Nifty Bank averaged +4.66% over the next 5 trading days (base rate +0.30%). Win rate 71.4%. That is +4.36 pp above the unconditional baseline. Statistically significant at p=0.0006759 and after Benjamini-Hochberg correction (q=0.004311).
* When Mars conjoined Sun (13 events since 2000), Nifty 50 averaged +4.53% over the next 5 trading days (base rate +0.22%). Win rate 76.9%. That is +4.32 pp above the unconditional baseline. Statistically significant at p=0.004496 and after Benjamini-Hochberg correction (q=0.01949).
* When Ketu formed a trine with Mercury (56 events since 2000), Nifty Bank averaged +4.58% over the next 5 trading days (base rate +0.30%). Win rate 82.1%. That is +4.28 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=3.493e-06).
* When Mars formed a square with Saturn (31 events since 2000), Nifty Bank averaged +4.55% over the next 5 trading days (base rate +0.30%). Win rate 77.4%. That is +4.25 pp above the unconditional baseline. Statistically significant at p=<0.0001 and after Benjamini-Hochberg correction (q=0.0006159).
* When Mars opposed Saturn (13 events since 2001), Nifty Bank averaged +4.54% over the next 5 trading days (base rate +0.30%). Win rate 84.6%. That is +4.24 pp above the unconditional baseline. Statistically significant at p=0.01159 and after Benjamini-Hochberg correction (q=0.04282).

### Strongest negative findings

* When Ketu opposed Venus (30 events since 2000), BSE Sensex averaged -1.48% over the next 5 trading days (base rate +0.25%). Win rate 26.7%. That is -1.73 pp below the unconditional baseline. Statistically significant at p=0.001279 and after Benjamini-Hochberg correction (q=0.007175).
* When Rahu conjoined Venus (30 events since 2000), BSE Sensex averaged -1.48% over the next 5 trading days (base rate +0.25%). Win rate 26.7%. That is -1.73 pp below the unconditional baseline. Statistically significant at p=0.001279 and after Benjamini-Hochberg correction (q=0.007175).
* When Jupiter turned direct (24 events since 2001), BSE Sensex averaged -1.31% over the next 5 trading days (base rate +0.25%). Win rate 37.5%. That is -1.56 pp below the unconditional baseline. Statistically significant at p=0.006207 and after Benjamini-Hochberg correction (q=0.0254).
* When Moon changed sign (4302 events since 2000), Nifty Midcap 100 averaged +0.10% over the next 5 trading days (base rate +0.27%). Win rate 39.6%. That is -0.17 pp below the unconditional baseline. Statistically significant at p=0.01304 and after Benjamini-Hochberg correction (q=0.04719).

### Null results

369 event/index combinations with at least 20 observations showed no effect that survives multiple-testing correction. The largest absolute differences from the base rate were:

| Event | Index | N | Mean ret | Base rate | Excess | p-value | q-value (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Saturn-Sun Conjunction | Nifty Bank | 26 | 3.333 | 0.3 | 3.033 | 0.0166 | 0.05701 |
| Jupiter-Sun Opposition | Nifty Bank | 24 | 3.182 | 0.3 | 2.882 | 0.02536 | 0.07841 |
| Jupiter Retrograde Station | Nifty Bank | 24 | 3.176 | 0.3 | 2.876 | 0.02247 | 0.07184 |
| Saturn-Venus Opposition | Nifty Bank | 26 | 3.141 | 0.3 | 2.841 | 0.01699 | 0.05791 |
| Mars-Sun Square | Nifty Bank | 24 | 3.023 | 0.3 | 2.723 | 0.03861 | 0.1063 |
| Saturn Retrograde Station | Nifty Bank | 26 | 3.001 | 0.3 | 2.701 | 0.04815 | 0.1249 |
| Saturn-Venus Conjunction | Nifty Bank | 30 | 2.917 | 0.3 | 2.617 | 0.03937 | 0.1074 |
| Saturn-Sun Conjunction | Nifty 50 | 26 | 2.748 | 0.2178 | 2.53 | 0.01664 | 0.05708 |
| Mars-Venus Conjunction | Nifty 50 | 21 | 2.731 | 0.2178 | 2.513 | 0.02194 | 0.07068 |
| Saturn-Venus Conjunction | Nifty 50 | 30 | 2.731 | 0.2178 | 2.513 | 0.01688 | 0.05765 |
| Ketu-Sun Opposition | Nifty Bank | 28 | 2.757 | 0.3 | 2.457 | 0.04552 | 0.1196 |
| Rahu-Sun Conjunction | Nifty Bank | 28 | 2.757 | 0.3 | 2.457 | 0.04552 | 0.1196 |
| Jupiter-Sun Opposition | Nifty 50 | 24 | 2.671 | 0.2178 | 2.453 | 0.02846 | 0.08543 |
| Ketu-Sun Conjunction | Nifty Bank | 29 | 2.732 | 0.3 | 2.432 | 0.04765 | 0.1238 |
| Rahu-Sun Opposition | Nifty Bank | 29 | 2.732 | 0.3 | 2.432 | 0.04765 | 0.1238 |

## 6. Category roll-ups

Every event type inside a category pooled together, weighted by sample size.  This is the broadest view of the dataset.

| Category | Index | Window | N | Mean ret | Base rate | Excess | Win % | Best p | Best q (BH) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Conjunctions (Yuti) | BSE Sensex | 1 | 1215 | 0.04444 | 0.05036 | -0.005919 | 52.76 | 0.02855 | 0.08557 |
| Conjunctions (Yuti) | BSE Sensex | 3 | 1214 | 0.1338 | 0.1513 | -0.01748 | 54.37 | 0.002123 | 0.01048 |
| Conjunctions (Yuti) | BSE Sensex | 5 | 1214 | 0.1834 | 0.2506 | -0.06721 | 54.2 | 0.001279 | 0.007175 |
| Conjunctions (Yuti) | BSE Sensex | 10 | 1213 | 0.5151 | 0.4957 | 0.01945 | 57.87 | 0.02443 | 0.07635 |
| Conjunctions (Yuti) | BSE Sensex | 20 | 1213 | 0.972 | 1.002 | -0.02963 | 59.03 | 0.05136 | 0.1309 |
| Conjunctions (Yuti) | Nifty 50 | 1 | 1215 | 0.3587 | 0.04492 | 0.3138 | 65.43 | 3.098e-06 | 6.314e-05 |
| Conjunctions (Yuti) | Nifty 50 | 3 | 1214 | 1.638 | 0.1333 | 1.504 | 66.06 | 1.984e-09 | 1.078e-07 |
| Conjunctions (Yuti) | Nifty 50 | 5 | 1214 | 2.818 | 0.2178 | 2.6 | 66.64 | 2.654e-13 | 2.211e-11 |
| Conjunctions (Yuti) | Nifty 50 | 10 | 1213 | 3.896 | 0.4212 | 3.475 | 68.43 | 8.137e-13 | 6.357e-11 |
| Conjunctions (Yuti) | Nifty 50 | 20 | 1213 | 7.754 | 0.8264 | 6.927 | 69.58 | 4.69e-12 | 3.589e-10 |
| Conjunctions (Yuti) | Nifty Bank | 1 | 1215 | 0.6932 | 0.06023 | 0.633 | 64.53 | 2.403e-06 | 5.088e-05 |
| Conjunctions (Yuti) | Nifty Bank | 3 | 1214 | 2.057 | 0.1819 | 1.875 | 65.24 | 1.467e-09 | 8.338e-08 |
| Conjunctions (Yuti) | Nifty Bank | 5 | 1214 | 3.202 | 0.3 | 2.902 | 66.06 | 1.434e-13 | 1.25e-11 |
| Conjunctions (Yuti) | Nifty Bank | 10 | 1213 | 4.944 | 0.5834 | 4.361 | 67.19 | 5.741e-14 | 5.52e-12 |
| Conjunctions (Yuti) | Nifty Bank | 20 | 1213 | 6.994 | 1.172 | 5.822 | 68.84 | 2.106e-10 | 1.41e-08 |
| Conjunctions (Yuti) | Nifty Midcap 100 | 1 | 1215 | 0.06099 | 0.05397 | 0.007029 | 64.53 | 0.003094 | 0.01438 |
| Conjunctions (Yuti) | Nifty Midcap 100 | 3 | 1214 | 0.05528 | 0.1609 | -0.1056 | 38.47 | 0.02754 | 0.0833 |
| Conjunctions (Yuti) | Nifty Midcap 100 | 5 | 1214 | 0.03402 | 0.266 | -0.232 | 39.7 | 0.02972 | 0.08817 |
| Conjunctions (Yuti) | Nifty Midcap 100 | 10 | 1213 | 1.471 | 0.532 | 0.9391 | 67.85 | 0.0002096 | 0.001731 |
| Conjunctions (Yuti) | Nifty Midcap 100 | 20 | 1213 | 2.208 | 1.065 | 1.143 | 68.59 | 0.004565 | 0.01968 |
| Conjunctions (Yuti) | Nifty Midcap 150 | 1 | 1215 | 0.4008 | 0.05323 | 0.3476 | 62.88 | 3.244e-05 | 0.0004055 |
| Conjunctions (Yuti) | Nifty Midcap 150 | 3 | 1214 | 0.2257 | 0.1594 | 0.06629 | 64.17 | 0.03171 | 0.09226 |
| Conjunctions (Yuti) | Nifty Midcap 150 | 5 | 1214 | 0.5254 | 0.2642 | 0.2612 | 65.65 | 0.02536 | 0.07841 |
| Conjunctions (Yuti) | Nifty Midcap 150 | 10 | 1213 | 1.682 | 0.5204 | 1.162 | 66.53 | 2.048e-05 | 0.0002888 |
| Conjunctions (Yuti) | Nifty Midcap 150 | 20 | 1213 | 1.813 | 1.047 | 0.7654 | 68.84 | 0.001983 | 0.01001 |
| Direct stations (Anuvakra) | BSE Sensex | 1 | 162 | -0.02446 | 0.05036 | -0.07482 | 51.23 | 0.01913 | 0.06436 |
| Direct stations (Anuvakra) | BSE Sensex | 3 | 162 | 0.09131 | 0.1513 | -0.06 | 56.17 | 0.009254 | 0.03541 |
| Direct stations (Anuvakra) | BSE Sensex | 5 | 162 | -0.04921 | 0.2506 | -0.2998 | 51.85 | 0.006207 | 0.0254 |
| Direct stations (Anuvakra) | BSE Sensex | 10 | 162 | 0.02893 | 0.4957 | -0.4667 | 58.64 | 0.003529 | 0.01606 |
| Direct stations (Anuvakra) | BSE Sensex | 20 | 162 | 0.5277 | 1.002 | -0.4739 | 57.41 | 0.01479 | 0.05163 |
| Direct stations (Anuvakra) | Nifty 50 | 1 | 162 | 0.2657 | 0.04492 | 0.2208 | 61.73 | 0.004575 | 0.01969 |
| Direct stations (Anuvakra) | Nifty 50 | 3 | 162 | 1.729 | 0.1333 | 1.596 | 67.9 | 0.0001559 | 0.001392 |
| Direct stations (Anuvakra) | Nifty 50 | 5 | 162 | 2.766 | 0.2178 | 2.548 | 64.2 | 0.0002308 | 0.001842 |
| Direct stations (Anuvakra) | Nifty 50 | 10 | 162 | 3.802 | 0.4212 | 3.38 | 72.22 | 0.0002437 | 0.001924 |
| Direct stations (Anuvakra) | Nifty 50 | 20 | 162 | 7.689 | 0.8264 | 6.863 | 68.52 | 6.906e-05 | 0.0007378 |
| Direct stations (Anuvakra) | Nifty Bank | 1 | 162 | 0.7019 | 0.06023 | 0.6417 | 64.81 | 0.008944 | 0.03443 |
| Direct stations (Anuvakra) | Nifty Bank | 3 | 162 | 2.169 | 0.1819 | 1.987 | 64.2 | 0.0008168 | 0.005038 |
| Direct stations (Anuvakra) | Nifty Bank | 5 | 162 | 3.072 | 0.3 | 2.772 | 64.81 | 0.0009173 | 0.00546 |
| Direct stations (Anuvakra) | Nifty Bank | 10 | 162 | 4.58 | 0.5834 | 3.997 | 67.28 | 0.0003909 | 0.00283 |
| Direct stations (Anuvakra) | Nifty Bank | 20 | 162 | 6.33 | 1.172 | 5.157 | 64.81 | 0.005784 | 0.02407 |
| Direct stations (Anuvakra) | Nifty Midcap 100 | 1 | 162 | -0.05101 | 0.05397 | -0.105 | 64.2 | 0.2541 | 0.4265 |
| Direct stations (Anuvakra) | Nifty Midcap 100 | 3 | 162 | 0.1342 | 0.1609 | -0.02664 | 40.74 | 0.008619 | 0.03342 |
| Direct stations (Anuvakra) | Nifty Midcap 100 | 5 | 162 | 0.01177 | 0.266 | -0.2542 | 43.21 | 0.04012 | 0.1087 |
| Direct stations (Anuvakra) | Nifty Midcap 100 | 10 | 162 | 1.782 | 0.532 | 1.25 | 73.46 | 0.004051 | 0.01791 |
| Direct stations (Anuvakra) | Nifty Midcap 100 | 20 | 162 | 2.464 | 1.065 | 1.4 | 71.6 | 0.02399 | 0.07552 |
| Direct stations (Anuvakra) | Nifty Midcap 150 | 1 | 162 | 0.3222 | 0.05323 | 0.269 | 60.49 | 0.008724 | 0.03376 |
| Direct stations (Anuvakra) | Nifty Midcap 150 | 3 | 162 | 0.2894 | 0.1594 | 0.1299 | 69.14 | 0.02595 | 0.07958 |
| Direct stations (Anuvakra) | Nifty Midcap 150 | 5 | 162 | 0.358 | 0.2642 | 0.09378 | 63.58 | 0.0186 | 0.063 |
| Direct stations (Anuvakra) | Nifty Midcap 150 | 10 | 162 | 1.381 | 0.5204 | 0.8605 | 69.14 | 0.001313 | 0.007304 |
| Direct stations (Anuvakra) | Nifty Midcap 150 | 20 | 162 | 1.623 | 1.047 | 0.5755 | 67.28 | 0.01997 | 0.06609 |
| Major aspects (Trine / Square / Opposition) | BSE Sensex | 1 | 4616 | 0.02891 | 0.05036 | -0.02145 | 51.93 | 0.01198 | 0.04396 |
| Major aspects (Trine / Square / Opposition) | BSE Sensex | 3 | 4616 | 0.1881 | 0.1513 | 0.03675 | 55.29 | 0.0003447 | 0.00257 |
| Major aspects (Trine / Square / Opposition) | BSE Sensex | 5 | 4614 | 0.2739 | 0.2506 | 0.02333 | 56.63 | 0.001279 | 0.007175 |
| Major aspects (Trine / Square / Opposition) | BSE Sensex | 10 | 4613 | 0.5605 | 0.4957 | 0.06483 | 59.05 | 0.001166 | 0.006666 |
| Major aspects (Trine / Square / Opposition) | BSE Sensex | 20 | 4605 | 1.032 | 1.002 | 0.03033 | 60.33 | 0.05136 | 0.1309 |
| Major aspects (Trine / Square / Opposition) | Nifty 50 | 1 | 4616 | 0.3395 | 0.04492 | 0.2946 | 65.27 | 1.04e-05 | 0.0001653 |
| Major aspects (Trine / Square / Opposition) | Nifty 50 | 3 | 4616 | 1.688 | 0.1333 | 1.555 | 66.75 | 2.52e-08 | 1.139e-06 |
| Major aspects (Trine / Square / Opposition) | Nifty 50 | 5 | 4614 | 2.912 | 0.2178 | 2.694 | 68.88 | 5.94e-10 | 3.713e-08 |
| Major aspects (Trine / Square / Opposition) | Nifty 50 | 10 | 4613 | 3.925 | 0.4212 | 3.504 | 69.76 | 8.129e-10 | 4.763e-08 |
| Major aspects (Trine / Square / Opposition) | Nifty 50 | 20 | 4605 | 7.908 | 0.8264 | 7.082 | 71.29 | 5.287e-11 | 3.741e-09 |
| Major aspects (Trine / Square / Opposition) | Nifty Bank | 1 | 4616 | 0.669 | 0.06023 | 0.6088 | 64.95 | 4.3e-07 | 1.222e-05 |
| Major aspects (Trine / Square / Opposition) | Nifty Bank | 3 | 4616 | 2.154 | 0.1819 | 1.973 | 67.01 | 1.472e-08 | 7.262e-07 |
| Major aspects (Trine / Square / Opposition) | Nifty Bank | 5 | 4614 | 3.317 | 0.3 | 3.017 | 68.14 | 1.963e-09 | 1.078e-07 |
| Major aspects (Trine / Square / Opposition) | Nifty Bank | 10 | 4613 | 4.911 | 0.5834 | 4.328 | 69.67 | 7.046e-10 | 4.262e-08 |
| Major aspects (Trine / Square / Opposition) | Nifty Bank | 20 | 4605 | 7.183 | 1.172 | 6.011 | 70.31 | 1.625e-09 | 9.092e-08 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 100 | 1 | 4616 | 0.04212 | 0.05397 | -0.01184 | 65.12 | 0.008682 | 0.03363 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 100 | 3 | 4616 | 0.1086 | 0.1609 | -0.05231 | 40.25 | 0.003292 | 0.01516 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 100 | 5 | 4614 | 0.1695 | 0.266 | -0.09654 | 40.66 | 0.01438 | 0.05035 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 100 | 10 | 4613 | 1.681 | 0.532 | 1.149 | 70.37 | 8.654e-05 | 0.0008771 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 100 | 20 | 4605 | 2.442 | 1.065 | 1.378 | 69.55 | 0.0002161 | 0.001759 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 150 | 1 | 4616 | 0.3956 | 0.05323 | 0.3423 | 62.98 | 5.782e-06 | 0.0001008 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 150 | 3 | 4616 | 0.2726 | 0.1594 | 0.1131 | 65.34 | 0.0008221 | 0.005058 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 150 | 5 | 4614 | 0.5822 | 0.2642 | 0.3179 | 66.71 | 0.002136 | 0.0105 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 150 | 10 | 4613 | 1.68 | 0.5204 | 1.159 | 68.16 | 2.808e-05 | 0.000361 |
| Major aspects (Trine / Square / Opposition) | Nifty Midcap 150 | 20 | 4605 | 1.922 | 1.047 | 0.8746 | 70.05 | 0.0005151 | 0.003531 |
| Retrograde stations (Vakra) | BSE Sensex | 1 | 164 | 0.1534 | 0.05036 | 0.103 | 54.27 | 0.1083 | 0.2299 |
| Retrograde stations (Vakra) | BSE Sensex | 3 | 164 | 0.05282 | 0.1513 | -0.09849 | 60.37 | 0.3902 | 0.5731 |
| Retrograde stations (Vakra) | BSE Sensex | 5 | 164 | 0.1373 | 0.2506 | -0.1133 | 59.76 | 0.3822 | 0.5648 |
| Retrograde stations (Vakra) | BSE Sensex | 10 | 163 | 0.1798 | 0.4957 | -0.3159 | 57.67 | 0.3151 | 0.4926 |
| Retrograde stations (Vakra) | BSE Sensex | 20 | 163 | 0.6681 | 1.002 | -0.3336 | 57.06 | 0.3103 | 0.4872 |
| Retrograde stations (Vakra) | Nifty 50 | 1 | 164 | 0.3998 | 0.04492 | 0.3548 | 64.63 | 0.009853 | 0.03732 |
| Retrograde stations (Vakra) | Nifty 50 | 3 | 164 | 1.675 | 0.1333 | 1.542 | 70.12 | 1.637e-05 | 0.0002426 |
| Retrograde stations (Vakra) | Nifty 50 | 5 | 164 | 2.81 | 0.2178 | 2.592 | 68.29 | 5.85e-06 | 0.0001016 |
| Retrograde stations (Vakra) | Nifty 50 | 10 | 163 | 3.697 | 0.4212 | 3.276 | 68.71 | 0.0001279 | 0.0012 |
| Retrograde stations (Vakra) | Nifty 50 | 20 | 163 | 7.754 | 0.8264 | 6.927 | 72.39 | 3.892e-05 | 0.0004604 |
| Retrograde stations (Vakra) | Nifty Bank | 1 | 164 | 0.7954 | 0.06023 | 0.7352 | 68.9 | 8.844e-05 | 0.0008916 |
| Retrograde stations (Vakra) | Nifty Bank | 3 | 164 | 2.295 | 0.1819 | 2.113 | 71.34 | 4.532e-06 | 8.371e-05 |
| Retrograde stations (Vakra) | Nifty Bank | 5 | 164 | 3.325 | 0.3 | 3.025 | 68.29 | 6.789e-06 | 0.0001152 |
| Retrograde stations (Vakra) | Nifty Bank | 10 | 163 | 4.852 | 0.5834 | 4.269 | 68.71 | 8.113e-05 | 0.0008313 |
| Retrograde stations (Vakra) | Nifty Bank | 20 | 163 | 7.254 | 1.172 | 6.082 | 70.55 | 0.0003622 | 0.002668 |
| Retrograde stations (Vakra) | Nifty Midcap 100 | 1 | 164 | 0.04035 | 0.05397 | -0.01361 | 61.59 | 0.1427 | 0.2832 |
| Retrograde stations (Vakra) | Nifty Midcap 100 | 3 | 164 | 0.09512 | 0.1609 | -0.06574 | 37.2 | 0.2301 | 0.396 |
| Retrograde stations (Vakra) | Nifty Midcap 100 | 5 | 164 | 0.02715 | 0.266 | -0.2389 | 39.63 | 0.1431 | 0.2838 |
| Retrograde stations (Vakra) | Nifty Midcap 100 | 10 | 163 | 1.309 | 0.532 | 0.7767 | 69.33 | 0.003735 | 0.01675 |
| Retrograde stations (Vakra) | Nifty Midcap 100 | 20 | 163 | 2.273 | 1.065 | 1.209 | 66.26 | 0.03119 | 0.09108 |
| Retrograde stations (Vakra) | Nifty Midcap 150 | 1 | 164 | 0.4927 | 0.05323 | 0.4394 | 63.41 | 0.005948 | 0.02465 |
| Retrograde stations (Vakra) | Nifty Midcap 150 | 3 | 164 | 0.2258 | 0.1594 | 0.06632 | 67.07 | 0.338 | 0.5183 |
| Retrograde stations (Vakra) | Nifty Midcap 150 | 5 | 164 | 0.4456 | 0.2642 | 0.1814 | 64.63 | 0.1592 | 0.3081 |
| Retrograde stations (Vakra) | Nifty Midcap 150 | 10 | 163 | 1.381 | 0.5204 | 0.8606 | 65.64 | 0.03092 | 0.09059 |
| Retrograde stations (Vakra) | Nifty Midcap 150 | 20 | 163 | 1.722 | 1.047 | 0.6746 | 70.55 | 0.02288 | 0.07291 |
| Sign ingress (Rashi Sankranti) | BSE Sensex | 1 | 5640 | 0.06158 | 0.05036 | 0.01122 | 53.48 | 0.03639 | 0.1022 |
| Sign ingress (Rashi Sankranti) | BSE Sensex | 3 | 5639 | 0.1699 | 0.1513 | 0.01861 | 55.61 | 0.1329 | 0.2693 |
| Sign ingress (Rashi Sankranti) | BSE Sensex | 5 | 5636 | 0.2397 | 0.2506 | -0.01089 | 56.09 | 0.1324 | 0.2687 |
| Sign ingress (Rashi Sankranti) | BSE Sensex | 10 | 5633 | 0.5365 | 0.4957 | 0.04084 | 58.46 | 0.2001 | 0.3606 |
| Sign ingress (Rashi Sankranti) | BSE Sensex | 20 | 5626 | 1.027 | 1.002 | 0.02507 | 60.01 | 0.2645 | 0.4383 |
| Sign ingress (Rashi Sankranti) | Nifty 50 | 1 | 5640 | 0.3745 | 0.04492 | 0.3296 | 66.24 | 1.032e-35 | 3.226e-33 |
| Sign ingress (Rashi Sankranti) | Nifty 50 | 3 | 5639 | 1.723 | 0.1333 | 1.589 | 67.69 | 8.809e-155 | 4.719e-152 |
| Sign ingress (Rashi Sankranti) | Nifty 50 | 5 | 5636 | 2.953 | 0.2178 | 2.735 | 68.56 | 6.041e-203 | 1.133e-199 |
| Sign ingress (Rashi Sankranti) | Nifty 50 | 10 | 5633 | 4.012 | 0.4212 | 3.591 | 69.77 | 1.481e-194 | 1.852e-191 |
| Sign ingress (Rashi Sankranti) | Nifty 50 | 20 | 5626 | 8.133 | 0.8264 | 7.307 | 71.22 | 1.839e-243 | 6.897e-240 |
| Sign ingress (Rashi Sankranti) | Nifty Bank | 1 | 5640 | 0.7317 | 0.06023 | 0.6715 | 65.99 | 2.282e-71 | 9.507e-69 |
| Sign ingress (Rashi Sankranti) | Nifty Bank | 3 | 5639 | 2.213 | 0.1819 | 2.031 | 67.1 | 1.037e-143 | 4.862e-141 |
| Sign ingress (Rashi Sankranti) | Nifty Bank | 5 | 5636 | 3.368 | 0.3 | 3.068 | 67.71 | 5.267e-169 | 3.292e-166 |
| Sign ingress (Rashi Sankranti) | Nifty Bank | 10 | 5633 | 5.011 | 0.5834 | 4.428 | 69.13 | 2.206e-175 | 2.068e-172 |
| Sign ingress (Rashi Sankranti) | Nifty Bank | 20 | 5626 | 7.385 | 1.172 | 6.213 | 70.32 | 4.784e-170 | 3.588e-167 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 100 | 1 | 5640 | 0.05879 | 0.05397 | 0.004829 | 65.44 | 0.08439 | 0.1902 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 100 | 3 | 5639 | 0.05039 | 0.1609 | -0.1105 | 39.26 | 0.05152 | 0.1312 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 100 | 5 | 5636 | 0.09752 | 0.266 | -0.1685 | 39.3 | 0.01304 | 0.04719 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 100 | 10 | 5633 | 1.595 | 0.532 | 1.063 | 69.48 | 1.226e-26 | 2.704e-24 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 100 | 20 | 5626 | 2.425 | 1.065 | 1.36 | 69.94 | 5.657e-21 | 7.577e-19 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 150 | 1 | 5640 | 0.4319 | 0.05323 | 0.3787 | 64.65 | 2.614e-42 | 9.801e-40 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 150 | 3 | 5639 | 0.2677 | 0.1594 | 0.1082 | 65.92 | 0.02008 | 0.06611 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 150 | 5 | 5636 | 0.5601 | 0.2642 | 0.2959 | 67 | 5.888e-07 | 1.512e-05 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 150 | 10 | 5633 | 1.686 | 0.5204 | 1.165 | 68.1 | 1.537e-38 | 5.238e-36 |
| Sign ingress (Rashi Sankranti) | Nifty Midcap 150 | 20 | 5626 | 1.979 | 1.047 | 0.9314 | 70.09 | 7.04e-14 | 6.6e-12 |

The complete row-level table (every event type, every index, every window) is in `reports/effects_summary.json` and `data/processed/correlation_results.csv`.

## 7. How to read this

* **Mean ret** is the average forward return over the sessions following the event.
* **Base rate** is the average forward return over all sessions, regardless of events.
* **Excess** is the difference between the two, in percentage points.
* **Win %** is the share of event windows with a positive return.
* **p-value** is the two-sided probability under the null hypothesis that event windows behave like any other window.
* A large sample with a small effect is still a small effect; a small sample with a large effect is suggestive but fragile.

_No claim is made that planetary positions cause price movement. This report quantifies what the historical data shows, including the cases where it shows nothing._
