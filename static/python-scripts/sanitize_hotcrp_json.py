### This script (generated by GPT4) sanitizes the JSON export from HotCRP to remove sensitive data

import json

# The keys you want to remove
keys_to_remove = {"email", "pc_conflicts", "metadata", "eligible_student_paper_prize", "talk_poster", "submitted_at", "decision", "status", "submitted", "submission"}

def sanitize_data(data):
    """Recursively sanitize a dictionary by removing specific keys."""
    if isinstance(data, dict):
        return {key: sanitize_data(value) for key, value in data.items() if key not in keys_to_remove}
    elif isinstance(data, list):
        return [sanitize_data(value) for value in data]
    else:
        return data

def sanitize_json_file(input_file, output_file):
    """Read a JSON file, sanitize it, and write the sanitized data to a new JSON file."""
    with open(input_file, 'r') as f:
        data = json.load(f)

    sanitized_data = sanitize_data(data)

    with open(output_file, 'w') as f:
        json.dump(sanitized_data, f, indent=4)

# Run the script
sanitize_json_file('hotcrp_posters.json', 'posters.json')
