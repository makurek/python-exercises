import xml.etree.ElementTree as ET
import json
from io import StringIO


tree = ET.parse('exercise-0001-xml-file-handling.xml')
#print(type(tree))
root = tree.getroot()
#print(type(root))

result = []

for person in root.iter('person'):
    person_dict = {}
    person_dict = person.attrib
    hobbies = []
    for hobby in person.iter('hobby'):
        hobbies.append(hobby.attrib)
    children = []
    for child in person.iter('child'):
        children.append(child.attrib)
    person_dict['hobbies'] = hobbies
    person_dict['children'] = children
    print(person_dict)
    result.append(person_dict)

with open("exercies-0001-output-json.json", "w") as write_file:
    json.dump(result, write_file, indent=4)

