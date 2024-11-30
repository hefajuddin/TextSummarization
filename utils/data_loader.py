import json
file_path="data/sample_texts.json"
def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data