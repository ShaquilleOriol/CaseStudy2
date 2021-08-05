import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the three csv files which contains the score of same students in term1 for each Subject
MathScores = pd.read_csv("MathScoreTerm1.csv")
DS_score = pd.read_csv("DSScoreTerm1.csv")
physicsScore = pd.read_csv("PhysicsScoreTerm1.csv")

print(physicsScore.head())
print(MathScores.head())
print(DS_score.head())



# 2. Remove the name and ethnicity column (to ensure confidentiality)
del MathScores["Name"]
del MathScores["Ethinicity"]

del physicsScore["Name"]
del physicsScore["Ethinicity"]

del DS_score["Name"]
del DS_score["Ethinicity"]

print(MathScores.head())
print(physicsScore.head())
print(DS_score.head())


# 3. Fill missing score data with zero
MathScores.fillna(0)
physicsScore.fillna(0)
DS_score.fillna(0)

print(physicsScore.head())
print(MathScores.head())
print(DS_score.head())



# 4. Merge the three files
mergedDataFrame = MathScores.merge(DS_score, on="ID", suffixes=(
    '_math', '_ds')).merge(physicsScore, on="ID", suffixes=('_ds', '_physics'))
merged_dataFrame_filter_cols = mergedDataFrame.filter(["ID", "Score_math", "Score", "Score_ds", "Age_math"]).rename(
    columns={"Score": "Age_math", "Score_physics" : "Age"})

print(merged_dataFrame_filter_cols)


# 5. Change Sex(M/F) Columnto 1/2 for further analysis

merged_dataFrame_filter_cols["Sex"] = [1 if sex ==
                                "M" else 2 for sex in merged_dataFrame_filter_cols["Sex"]]
print(merged_dataFrame_filter_cols)


# 6. Change Sex(M/F) Columnto 1/2 for further analysis
merged_dataFrame_filter_cols.to_csv("ScoreFinal.csv")

