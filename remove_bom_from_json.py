import json

# Open the file and read it with error handling
with open('user_fixture.json', 'r', encoding='utf-8', errors='ignore') as f:
    try:
        # Read the JSON data
        data = json.load(f)
        print("JSON data loaded successfully")
    except json.JSONDecodeError as e:
        print(f"Error: JSONDecodeError: {e}")