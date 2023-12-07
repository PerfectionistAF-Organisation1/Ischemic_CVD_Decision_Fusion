import json
d = {'country': 'Germany',
     'capital': 'Berlin'}
file = open("dictionary_data.json", "w")
json.dump(d, file)
file.close()
file = open("dictionary_data.json", "r")
output = file.read()
print(output)
file.close()