import pandas as pd
import numpy as np
import sys
import os
#TODO hardcodear los nombres de los archivos para el make
#TODO calcular rango articular


output = pd.DataFrame({"label": ["true"]})

print(f"len(sys.argv):{len(sys.argv)}")

for i in range(len(sys.argv)-1):
    print(f"i:{i}")

    # Read input file
    input_data = pd.read_csv(sys.argv[i+1], header=0)

    trueF = sys.argv[2]

    # Prepare an empty DataFrame for output
    table = pd.DataFrame(columns=[f"{col}_max" for col in input_data.columns] +
                        [f"{col}_min" for col in input_data.columns] +
                        [f"{col}_median" for col in input_data.columns])

    # Calculate statistics for each column
    for column_name, column_data in input_data.items():
        max_val = column_data.max()
        min_val = column_data.min()
        median_val = column_data.median()

        # Add calculated values to the output DataFrame
        table.loc[0, f"{column_name}_max"] = max_val
        table.loc[0, f"{column_name}_min"] = min_val
        table.loc[0, f"{column_name}_median"] = median_val

        table = table.reset_index(drop=True)
        output = output.reset_index(drop=True)
        output =pd.concat([output, table], axis=1)




# Write output DataFrame to CSV file
output.to_csv(f"modelInput.csv", index=False)