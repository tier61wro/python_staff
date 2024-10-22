import json
json_string = '''
{
  "string": "Это строка",
  "number": 12345,
  "boolean_true": true,
  "boolean_false": false,
  "null_value": null,
  "array": [1, "строка", false, null],
  "object": {
    "key1": "значение 1",
    "key2": 42,
    "key3": [true, null, "еще одна строка"]
  }
}
'''
data = json.loads(json_string)
print(type(data))
print(data.get("number"))

# Открытие файла с JSON данными
with open('data.json', 'r', encoding='utf-8') as file:
    data_from_file = json.load(file)


invalid_json = '{name: "John", age: 30}'

# try:
#     json_string = json.loads(invalid_json)
# except Exception as e:
#     print(f"got some error: {e}")

import yaml

data_yaml = yaml.safe_load(open('file.yaml', 'r'))
print(f"{data_yaml=}")

#=======================
# XML
import xml.etree.ElementTree as ET
tree = ET.parse('company.xml') # или ET.fromstring(xml_data)
root = tree.getroot()
print(root)
print(tree)
names = [el.text for el in root.findall('.//name')]
print(names) # ['John Doe', 'Jane Smith']