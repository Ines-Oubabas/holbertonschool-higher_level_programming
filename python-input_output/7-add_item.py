#!/usr/bin/python3
"""
   function file for add_item.json
"""

import sys
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    # Check if the file exists, if not create it
    if not exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    # Load the list from the file
    my_list = load_from_json_file("add_item.json")

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
