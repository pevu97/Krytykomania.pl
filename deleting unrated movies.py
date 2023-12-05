import json

with open("film_list.txt", 'r', encoding='latin-1') as file:
    content = file.read()

# Verify that the file is valid JSON
try:
    data = json.loads(content)
except json.JSONDecodeError as e:
    print(f"ERROR procesing JSON file: {e}")
    data = {}

# Delete keys that value is 0
filtered_data = {key: value for key, value in data.items() if value != 0}

# Save new data to file
with open("film_list.txt", 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=2)
