#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os


# Import the functions from the previous scripts
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []


# Add all arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
