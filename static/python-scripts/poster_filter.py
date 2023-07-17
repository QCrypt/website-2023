# created by ChatGPT: https://chat.openai.com/share/2f8736f4-998c-4d38-855a-716b0d640169

import json

def filter_json(input_file, output_file1, output_file2, pid_list):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    matching_entries = []  # List to store matching entries
    non_matching_entries = []  # List to store non-matching entries

    # Iterate over each entry in the input data
    for entry in data:
        if 'pid' in entry and entry['pid'] in pid_list:
            # Entry has a "pid" field and its value is in the specified pid_list
            matching_entries.append(entry)
        else:
            # Entry does not have a "pid" field or its value is not in the specified pid_list
            non_matching_entries.append(entry)

    # Write the matching entries to output_file1 as JSON
    with open(output_file1, 'w') as f1:
        json.dump(matching_entries, f1, indent=4)

    # Write the non-matching entries to output_file2 as JSON
    with open(output_file2, 'w') as f2:
        json.dump(non_matching_entries, f2, indent=4)

    print("Filtered data saved successfully!")

# Example usage
input_file = 'data.json'  # Path to the input JSON file
output_file1 = 'matching_entries.json'  # Path to save the matching entries JSON file
output_file2 = 'non_matching_entries.json'  # Path to save the non-matching entries JSON file
pid_list = [1, 3, 5]  # List of pids to match

# filter_json(input_file, output_file1, output_file2, pid_list)
filter_json('posters.json', 'posters_monday.json', 'posters_tuesday.json', [5, 9, 16, 27, 37, 39, 45, 48, 60, 65, 68, 71, 74, 82, 85, 89, 91, 93, 95, 98, 108, 112, 114, 116, 119, 121, 123, 125, 127, 131, 134, 136, 138, 140, 142, 145, 148, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177])
