import pandas as pd
import numpy as np
import sys
import os

# Read input file
input_data = pd.read_csv(sys.argv[1], header=0)

# Prepare an empty DataFrame for output
output = pd.DataFrame(columns=[f"{col}_max" for col in input_data.columns] +
                      [f"{col}_min" for col in input_data.columns] +
                      [f"{col}_median" for col in input_data.columns])

# Calculate statistics for each column
for column_name, column_data in input_data.items():
    max_val = column_data.max()
    min_val = column_data.min()
    median_val = column_data.median()

    # Add calculated values to the output DataFrame
    output.loc[0, f"{column_name}_max"] = max_val
    output.loc[0, f"{column_name}_min"] = min_val
    output.loc[0, f"{column_name}_median"] = median_val

# Extract filename without extension
filename_without_extension = os.path.splitext(sys.argv[1])[0]

# Write output DataFrame to CSV file
output.to_csv(f"{filename_without_extension}_modelInput.csv", index=False)