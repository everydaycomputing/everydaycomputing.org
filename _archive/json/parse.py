# coding=utf-8
import json
import sys

#with open('sequencing.json', 'r') as f:
with open('conditionals.json', 'r') as f:
    data = json.load(f)

out = []
for list in data['lists']:
    if list['closed'] == False:
        print "{value: '" + list['name'] + "', text: '" + list['name'] +"'},"
        out.append(list['name'])

#with open('s.json', 'w') as f:
#     json.dump(out, f)
#print(data)
#json.dump(data, f)


#with open('sequencing.json', encoding='utf-8') as data_file:
#    data = json.loads(data_file.read())
