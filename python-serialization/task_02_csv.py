#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            data_list = [row for row in csv_reader]
        
        json_data = json.dumps(data_list, indent=4)
        
        with open('data.json', mode='w') as json_file:
            json_file.write(json_data)
        
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
