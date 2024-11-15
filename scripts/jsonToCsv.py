import json
import pandas as pd

# Load the improperly formatted JSON data
file_path = 'enb_report.json'
with open(file_path, 'r') as file:
    raw_data = file.read()

# Fix the format: Wrap the data in square brackets and add commas between objects
formatted_data = "[" + raw_data.replace("}\n{", "},\n{") + "]"

# Parse the formatted data into a Python list
data = json.loads(formatted_data)

# Function to flatten the JSON data
def flatten_json(data):
    records = []
    for entry in data:
        unix_ms_timestamp = int(entry["timestamp"] * 1000)
        base_info = {
            "type": entry["type"],
            "timestamp": entry["timestamp"]
        }
        # print(entry)
        if(base_info['type'] == 'metrics'):
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
flattened_data = flatten_json(data)

# Convert to a DataFrame
df = pd.DataFrame(flattened_data)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("flattened_json_data.csv", index=False)
df.to_json("flattened_json_data.json")