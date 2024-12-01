import json
# We can use this block of code when we get Text from sample_texts.json
def load_data(file_path):
    """Load sample texts from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data