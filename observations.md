Observations with $q = 2$, and a nilpotency degree of $q + 2 = 4$ 
| Length | $\#$ of Sequences that satisfy all constraints |
-- | --- 
| 4 | 5 |
| 5 | 9 |
| 6 | 17 |
| 7 | 31 |
| 8 | 52 |
| 9 | 92 |
| 10 | 160 |
| 11 | 282 |
| 12 | 466 |
| 13 | 770 |
| 14 | 1297 |
| 15 | 2202 |
| 16 | 3724 |
| 17 | 6335 |
| 18 | 10770 |
| 19 | 18297 |
| 20 | 31028 |
| 21 | 52648 |
| 22 | 89324 |
| 23 | 151477 |
| 24 | 256868 |
| 25 | 435710 |

Looks roughly $\mathcal{O}(2^n)$. To show no sequence with bounded nilpotency degree exists, we would need either this number to go to $0$ or more constraints (e.g. actually figuring out which points lie on all hypersurfaces)

As a check that the code is reasonable, $q = 2$ and nilpotency degree $3$ gives no good sequences of length $\geq 9$
