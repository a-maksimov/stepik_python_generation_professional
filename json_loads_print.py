import json
import sys

json_string = sys.stdin.read()

json_dict = json.loads(json_string)

[print(f'{key}: {", ".join(map(str, value))}' if isinstance(value, list) else f'{key}: {value}') for key, value in json_dict.items()]