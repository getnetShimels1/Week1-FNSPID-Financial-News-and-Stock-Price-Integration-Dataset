import os
import pandas as pd

# Folder containing your CSV files
folder_path = 'raw_data\yfinance_data'

# List to store DataFrames
dataframes = []

# Loop through all files in the folder
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        # Extract the company name (first four characters of the file name)
        company_name = file[:4]

        # Load the CSV file
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)

        # Add the company name column
        df["Company"] = company_name

        # Append the DataFrame to the list
        dataframes.append(df)

# Merge all DataFrames
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new CSV file in the parent folder
parent_folder = os.path.dirname(folder_path)
output_file = os.path.join(parent_folder, "companies_historical_data.csv")
merged_df.to_csv(output_file, index=False)

print(f"Merged file saved as {output_file}")
