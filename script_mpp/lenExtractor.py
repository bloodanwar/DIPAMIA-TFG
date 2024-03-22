import pandas as pd
import numpy as np
import sys
from itertools import combinations
import os
import math

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(sys.argv[1], header=0)

connections = {
    0: [1, 4],1: [0, 2],2: [1, 3],3: [2, 7],4: [0, 5],5: [4,6],6: [5,8],7: [3],8: [6],9: [10],
    10: [9],11: [12,13,23],12: [11,14,24],13: [11,15],14: [12,16],15: [13,17,19,21],16: [14,18,20,22],17: [19,15],18: [20,16],19: [17,15],
    20: [18,16],21: [15],22: [16],23: [11,24,25],24: [12,23,26],25: [23,27],26: [24,28],27: [29,31],28: [30,32],29: [27,31],
    30: [28,32],31: [27,29],32: [28,30]
}


# Rename columns for clarity
columns = []
for i in range(33):
    columns.append(f"Joint_{i}_X")
    columns.append(f"Joint_{i}_Y")
    columns.append(f"Joint_{i}_Z")
df.columns = columns

column_mapping = {
}

def rename_columns(df, mapping):
    df = df.rename(columns=mapping)
    return df


def getPointCoords(point, row):
    column=(point*3)-1
    z=df.iloc[row,column]
    y=df.iloc[row,column-1]
    x=df.iloc[row,column-2]

    return ([x,y,z])

def calculate_Len_sagittal(p1, p2,): #ignoring z coord
    a = [p1[0],p1[1]]
    b= [p2[0],p2[1]]
    return abs(math.dist(a, b))

def calculate_Len_frontal(p1, p2): #ignoring x coord
    a = [p1[1],p1[2]]
    b= [p2[1],p2[2]]
    return abs(math.dist(a, b))

def calculate_Len_transversal(p1, p2): #ignoring x coord
    a = [p1[0],p1[2]]
    b= [p2[0],p2[2]]
    return abs(math.dist(a, b))

Len_sagittal = pd.DataFrame()
Len_frontal = pd.DataFrame()
Len_transversal = pd.DataFrame()

for index, row in df.iterrows():
    Len_sagittal_row = []
    Len_frontal_row = []
    Len_transversal_row = []

    for key, value in connections.items():
        if len(value) < 1:
            continue
        else:
            connected_combinations = list(combinations(value, 1))
            for connected_pair in connected_combinations:
                pA = getPointCoords(connected_pair[0], index)
                pB = getPointCoords(key, index)

                Len_sagittal_row.append(calculate_Len_sagittal(pA, pB))
                Len_frontal_row.append(calculate_Len_frontal(pA, pB))
                Len_transversal_row.append(calculate_Len_transversal(pA, pB))
                header = f"Len_{connected_pair[0]}_{key}"
                if header not in Len_sagittal.columns: Len_sagittal[header] = ""
                if header not in Len_frontal.columns: Len_frontal[header] = ""
                if header not in Len_transversal.columns: Len_transversal[header] = ""
    Len_sagittal = pd.concat([Len_sagittal, pd.DataFrame([Len_sagittal_row], columns=Len_sagittal.columns)], ignore_index=True)
    Len_frontal = pd.concat([Len_frontal, pd.DataFrame([Len_frontal_row], columns=Len_frontal.columns)], ignore_index=True)
    Len_transversal = pd.concat([Len_transversal, pd.DataFrame([Len_transversal_row], columns=Len_transversal.columns)], ignore_index=True)

# Rename columns using the mapping dictionary
Len_sagittal = rename_columns(Len_sagittal, column_mapping)
Len_frontal = rename_columns(Len_frontal, column_mapping)
Len_transversal = rename_columns(Len_transversal, column_mapping)


filename_without_extension = os.path.splitext(sys.argv[1])[0]

Len_sagittal.to_csv(f"{filename_without_extension}_len_sagittal.csv", index=False)
Len_frontal.to_csv(f"{filename_without_extension}_len_frontal.csv", index=False)
Len_transversal.to_csv(f"{filename_without_extension}_len_transversal.csv", index=False)