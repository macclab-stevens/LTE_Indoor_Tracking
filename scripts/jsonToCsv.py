#! /usr/bin/python3
import json
import pandas as pd
import os
import sys

outputReportName = 'enb_report.csv'

# Function to flatten the JSON data
def flatten_json(data):
    records = []
    for entry in data:
        unix_ms_timestamp = int(entry["timestamp"] * 1000)
        base_info = {
            "type": entry["type"],
            "timestamp": unix_ms_timestamp
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

def processJsonFile(subfolder_path):
    read_file = os.path.join(subfolder_path,'enb_report.json')
    with open(read_file, 'r') as file:
        raw_data = file.read()

    # Fix the format: Wrap the data in square brackets and add commas between objects
    formatted_data = "[" + raw_data.replace("}\n{", "},\n{") + "]"

    # Parse the formatted data into a Python list
    data = json.loads(formatted_data)

    # Flatten the JSON data
    flattened_data = flatten_json(data)

    # Convert to a DataFrame
    df = pd.DataFrame(flattened_data)

    # Display the DataFrame
    pd.set_option('display.max_columns', None)
    df = df.drop(columns=['ue_list'])
    df = df.drop(columns=['bearer_list'])
    
    print(df)

    # Save the DataFrame to a CSV file
    outputFile = os.path.join(subfolder_path,outputReportName)
    df.to_csv(outputFile, index=False)

if __name__ == '__main__':

    # processJsonFile("../logs/20241113")
    # exit()
    # try:
    #     targetFolder = sys.argv[1]
    #     # targetFolder = os.path.join("..","logs","20241205")
    #     print(targetFolder)
    # except:
        # print("No input arg using logs folder")
    # Get the current working directory
    current_dir = os.getcwd()

    # Check if the script is in the 'scripts' folder
    if os.path.basename(current_dir) == "scripts":
        print("Script is running in the 'scripts' folder.")
    else:
        print(f"you did not run jsonToCsv.py from the 'scripts' folder. Current directory: {current_dir}")
        sys.exit("Please run this script from the 'scripts' folder.")
    
    logsFolder = os.path.join("..","logs")
    # Load the improperly formatted JSON data
    # targetFolder = os.path.join("..","logs","20241205")
    # Iterate through each subfolder
    print(logsFolder)
    for root, dirs, files in os.walk(logsFolder):
        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            print(f"... Checking Subfolder: {subfolder_path}")
            if "enb_report.json" not in os.listdir(subfolder_path):
                print(f"enb_report.json not found in folder: {subfolder_path} . Skipping...")
                continue
            #check if there is already a csv file that we want in the folder:
            if outputReportName in os.listdir(subfolder_path):
                print(f"enb_report.csv already in folder: {subfolder_path} . Skipping....")
                continue
            else: processJsonFile(subfolder_path)
        # To avoid recursion into subfolders
        break
    exit()
