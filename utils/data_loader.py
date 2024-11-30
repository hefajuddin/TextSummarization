import json

def load_data(file_path):
    """Load sample texts from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data