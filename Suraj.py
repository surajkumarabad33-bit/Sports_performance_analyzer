# Sports Performance Analyzer (PS No. 21)
# Concepts used: NumPy, Pandas, Matplotlib, Statistics

import numpy as np                   # NumPy -> mean, median, std, max, min
import pandas as pd                  # Pandas -> load CSV, clean data, groupby()
import matplotlib.pyplot as plt      # Matplotlib -> line chart and bar chart

# ---------------------------------------------------------------
# STEP 1: LOAD THE CSV FILE (Pandas)
# ---------------------------------------------------------------
# header=None  -> the file has no heading line, so we give names ourselves
# dtype=str    -> read everything as text, so a wrong value like 'abc' is not lost
# keep_default_na=False -> a blank cell stays "" (not NaN)
df = pd.read_csv("scores.csv", header=None, names=["Player", "Match", "Score"],
                 dtype=str, keep_default_na=False)

# If the file does have a heading line (Player,Match,Score), remove that line
df = df[df["Player"] != "Player"].reset_index(drop=True)

# ---------------------------------------------------------------
# STEP 2: CLEAN THE DATA (skip invalid or missing scores)
# ---------------------------------------------------------------
good_rows = []                                   # empty list to keep only the valid rows

for i, row in df.iterrows():                     # go through the table row by row
    row_no = i + 1                               # Pandas counts from 0, we want Row 1, Row 2 ...
    try:                                         # try to turn the score text into a number
        score = float(row["Score"])              # 'abc' or blank will fail here
    except ValueError:                           # the score was not a number
        print(f"Row {row_no} skipped: invalid Score '{row['Score']}'.")
        continue                                 # skip this row, go to the next one
    if score < 0:                                # a score can never be negative
        print(f"Row {row_no} skipped: Score cannot be negative.")
        continue                                 # skip this row, go to the next one
    good_rows.append([row["Player"], int(row["Match"]), score])   # row is valid -> keep it

data = pd.DataFrame(good_rows, columns=["Player", "Match", "Score"])   # table of valid rows only

if len(data) == 0:                               # nothing valid is left
    print("No valid data to analyse.")
    raise SystemExit                             # stop the program

# ---------------------------------------------------------------
# STEP 3: MENU
# ---------------------------------------------------------------
print("1. Player stats")
print("2. Statistics and trend")
print("3. Min score and bar chart")
choice = input("Enter menu option: ").strip()    # read the user's choice

# ---------------------------------------------------------------
# OPTION 1: PLAYER STATS (groupby)
# ---------------------------------------------------------------
if choice == "1":
    group = data.groupby("Player")["Score"]      # groupby(): one group of scores per player
    avg = group.mean()                           # average score of each player
    best = group.max()                           # best (highest) score of each player
    total = group.sum()                          # total score of each player
    top = avg.idxmax()                           # name of the player with the highest average

    if len(avg) == 1:                            # only one player (minimum input)
        std = np.std(data["Score"])              # NumPy standard deviation (population, default)
        print(f"{top}: Avg {avg[top]:.2f} | Best {best[top]:g} | Std Dev: {std:.2f}")
        print(f"Top performer: {top}")
    else:                                        # many players
        for name in avg.index:                   # print one line per player
            print(f"{name}: Avg {avg[name]:.2f} | Best {best[name]:g} | Total {total[name]:g}")
        print(f"Top performer: {top} (Avg {avg[top]:.2f})")

# ---------------------------------------------------------------
# OPTION 2: STATISTICS + LINE CHART
# ---------------------------------------------------------------
elif choice == "2":
    scores = data["Score"].to_numpy()            # scores as a NumPy array
    mean = np.mean(scores)                       # average of all scores
    median = np.median(scores)                   # middle value of the sorted scores
    std = np.std(scores)                         # population standard deviation
    pos = np.argmax(scores)                      # position of the highest score
    top_row = data.iloc[pos]                     # the row that has the highest score
    print(f"Mean: {mean:.2f} | Median: {median:.2f} | Std Dev: {std:.2f} | "
          f"Max: {top_row['Score']:g} ({top_row['Player']}, Match {top_row['Match']})")

    match_avg = data.groupby("Match")["Score"].mean()    # groupby(): average score of each match
    text = [f"Match {m}: {a:.2f}" for m, a in match_avg.items()]   # "Match 1: 35.00" for every match
    print("Match-wise average: " + " | ".join(text))

    plt.plot(match_avg.index, match_avg.values, marker="o")   # LINE chart of match averages
    plt.title("Score Trend")                     # chart title
    plt.xlabel("Match")                          # x-axis label
    plt.ylabel("Average Score")                  # y-axis label
    plt.xticks(match_avg.index)                  # show whole match numbers only
    print("Line chart 'Score Trend' displayed")
    plt.show()                                   # open the chart window

# ---------------------------------------------------------------
# OPTION 3: MIN SCORE + BAR CHART
# ---------------------------------------------------------------
elif choice == "3":
    print(f"Min: {np.min(data['Score']):g}")     # NumPy minimum score
    avg = data.groupby("Player")["Score"].mean() # average score of each player
    plt.bar(avg.index, avg.values)               # BAR chart of player averages
    plt.title("Average Score per Player")        # chart title
    plt.xlabel("Player")                         # x-axis label
    plt.ylabel("Average Score")                  # y-axis label
    print("Bar chart 'Average Score per Player' displayed")
    plt.show()                                   # open the chart window

else:
    print("Invalid option.")
