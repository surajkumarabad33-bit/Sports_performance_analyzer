
# Sports Performance Analyzer (PS 21)

## Problem in simple words
`scores.csv` has `Player, Match, Score`. The program must load it, remove bad rows, and show
each player's average / best score, the top performer, overall statistics, and charts.

## Run
```
pip install numpy pandas matplotlib
python sports_analyzer.py        # then type menu option 1, 2 or 3
python tests/run_tests.py        # runs the 4 test cases
```

## Concepts used (only those in the problem statement)
| Concept | Meaning | Used for |
|---|---|---|
| Pandas `read_csv` | loads a CSV into a table (DataFrame) | Step 1 |
| Data cleaning (`try/except`, `if`) | skip rows that are not numbers or are negative | Step 2 |
| `groupby()` | split rows into groups (per player / per match) and calculate on each | options 1, 2, 3 |
| NumPy | fast maths on arrays: `mean`, `median`, `std`, `max`, `min`, `argmax` | options 1, 2, 3 |
| Mean | sum / count = (40+60+30+50)/4 = 45 | option 2 |
| Median | middle of sorted values = (40+50)/2 = 45 | option 2 |
| Standard deviation | spread of scores; population formula = np.std default = 11.18 | options 1, 2 |
| Matplotlib | `plot` = line chart, `bar` = bar chart, with title and labels | options 2, 3 |

## Program flow
1. Load CSV -> 2. Clean (skip bad rows) -> 3. Show menu -> 4. Calculate -> 5. Print / chart

## Test results
| Test | Result |
|---|---|
| 1 Normal input (option 1) | PASS |
| 2 Boundary input (option 1) | PASS |
| 3 Invalid input | PASS |
| 4 Statistics and trend (option 2) | PASS |
