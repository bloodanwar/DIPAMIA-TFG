import pandas as pd
import numpy as np
import sys
from itertools import combinations
import os

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


def getPointCoords(point, row):
    column=(point*3)-1
    z=df.iloc[row,column]
    y=df.iloc[row,column-1]
    x=df.iloc[row,column-2]

    return ([x,y,z])

def calculate_angle_sagittal(p1, p2, p3): #ignoring z coord
    v1 = np.array([p1[0]-p2[0], p1[1]-p2[1]])
    v2 = np.array([p3[0]-p2[0], p3[1]-p2[1]])
    dot_product = np.dot(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos_theta = dot_product / norms
    angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

def calculate_angle_frontal(p1, p2, p3): #ignoring x coord
    v1 = np.array([p1[1]-p2[1], p1[2]-p2[2]])
    v2 = np.array([p3[1]-p2[1], p3[2]-p2[2]])
    dot_product = np.dot(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos_theta = dot_product / norms
    angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

def calculate_angle_transversal(p1, p2, p3): #ignoring x coord
    v1 = np.array([p1[0]-p2[0], p1[2]-p2[2]])
    v2 = np.array([p3[0]-p2[0], p3[2]-p2[2]])
    dot_product = np.dot(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos_theta = dot_product / norms
    angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

angles_sagittal = pd.DataFrame()
angles_frontal = pd.DataFrame()
angles_transversal = pd.DataFrame()

for index, row in df.iterrows():
    angles_sagittal_row = []
    angles_frontal_row = []
    angles_transversal_row = []

    for key, value in connections.items():
        if len(value) == 1:
            continue
        else:
            connected_combinations = list(combinations(value, 2))
            for connected_pair in connected_combinations:
                pA = getPointCoords(connected_pair[0], index)
                pB = getPointCoords(key, index)
                pC = getPointCoords(connected_pair[1], index)

                angles_sagittal_row.append(calculate_angle_sagittal(pA, pB, pC))
                angles_frontal_row.append(calculate_angle_frontal(pA, pB, pC))
                angles_transversal_row.append(calculate_angle_transversal(pA, pB, pC))
                header = f"Ang_{connected_pair[0]}_{key}_{connected_pair[1]}"
                if header not in angles_sagittal.columns: angles_sagittal[header] = ""
                if header not in angles_frontal.columns: angles_frontal[header] = ""
                if header not in angles_transversal.columns: angles_transversal[header] = ""
    angles_sagittal = pd.concat([angles_sagittal, pd.DataFrame([angles_sagittal_row], columns=angles_sagittal.columns)], ignore_index=True)
    angles_frontal = pd.concat([angles_frontal, pd.DataFrame([angles_frontal_row], columns=angles_frontal.columns)], ignore_index=True)
    angles_transversal = pd.concat([angles_transversal, pd.DataFrame([angles_transversal_row], columns=angles_transversal.columns)], ignore_index=True)


filename_without_extension = os.path.splitext(sys.argv[1])[0]

angles_sagittal.to_csv(f"{filename_without_extension}_sagittal.csv", index=False)
angles_frontal.to_csv(f"{filename_without_extension}_frontal.csv", index=False)
angles_transversal.to_csv(f"{filename_without_extension}_transversal.csv", index=False)