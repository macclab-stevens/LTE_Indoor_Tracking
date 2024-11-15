#! /usr/bin/python3
import json
import csv
import os
import pandas as pd
 
 
# Opening JSON file and loading the data
# into the variable data
# Get the current directory
# current_dir = os.getcwd()
# print(current_dir)
# # Get the parent directory
# parent_dir = os.path.dirname(current_dir)
# print(parent_dir)
# # Construct the file path
# file_path = os.path.join("..", "logs","20241113","enb_report.json")
# print(file_path)
# filename="../logs/20241112/enb_report.json"

# df = pd.read_json("test.json")
# print(df)
# df.to_csv("test.csv")

# data = json.load("test.json")
with open('test.json', 'r') as file:
    json_data = json.load(file)
print(json_data)

# Function to flatten the JSON
def flatten_json(data):
    records = []
    for entry in data:
        base_info = {
            "type": entry["type"],
            "timestamp": entry["timestamp"]
        }
        for cell in entry["cell_list"]:
            cell_info = cell["cell_container"]
            for ue in cell_info["ue_list"]:
                ue_info = ue["ue_container"]
                for bearer in ue_info["bearer_list"]:
                    bearer_info = bearer["bearer_container"]
                    # Combine all information into a single record
                    record = {**base_info, **cell_info, **ue_info, **bearer_info}
                    records.append(record)
    return records

# Flatten the JSON data
flattened_data = flatten_json(json_data)

# Convert to a DataFrame
df = pd.DataFrame(flattened_data)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("flattened_json_data.csv", index=False)