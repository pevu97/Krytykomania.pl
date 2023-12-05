import json

with open('film_list.txt', 'r', encoding='utf-8-sig') as f:
    content = f.read()
    print(type(content))

# Verify that the file is valid JSON
try:
    data = json.loads(content)
except json.JSONDecodeError as e:
    print(f"ERROR procesing JSON file: {e}")
    data = {}

if data:
    # Sort
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

    with open('film_list.txt', 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=2)
else:
    print("JSON file is empty.")
