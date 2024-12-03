import os
import json
import urllib.parse

# Replace with the path to your local folder containing the assets
folder_path = r"C:\\Users\\James D\\Pictures\\IVP Thumbnails\\Debug"
base_url = "https://full3sixty.github.io/ivp-thumbnails.github.io/Debug/"  # Replace with your GitHub Pages URL
output_file = "file_list_debug.json"

def generate_json(folder_path, base_url, output_file):
    file_list = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            # Create relative file path
            relative_path = os.path.relpath(os.path.join(root, file), folder_path)
            # URL-encode the relative path
            encoded_path = urllib.parse.quote(relative_path.replace("\\", "/"))  # Use '/' for URL paths
            # Add encoded URL to the list
            file_list.append(base_url + encoded_path)

    # Write the list to a JSON file
    with open(output_file, "w") as json_file:
        json.dump(file_list, json_file, indent=4)

    print(f"JSON file generated: {output_file}")

# Call the function
generate_json(folder_path, base_url, output_file)
