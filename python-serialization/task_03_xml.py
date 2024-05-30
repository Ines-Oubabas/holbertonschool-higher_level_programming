#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Create the root element
    root = ET.Element("data")

    # Iterate through dictionary items and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create an ElementTree object from the root element
    tree = ET.ElementTree(root)

    # Write the tree to a file
    tree.write(filename)

def deserialize_from_xml(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct the dictionary
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary

if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
