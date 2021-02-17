"""
Module documentation
"""
import json
import pprint


PATH = "kved.json"
source_json = open(PATH, encoding="utf-8")

data = json.load(source_json)
class_code = "01.11"

for section in data["sections"][0]:
    section_name = section["sectionName"]
    for division in section["divisions"]:
        division_name = division["divisionName"]
        for group in division["groups"]:
            group_name = group["groupName"]
            for group_class in group["classes"]:
                if group_class["classCode"] == class_code:
                    class_name = group_class["className"]
                    print("Class:  " + class_name)
                    print("Section:  " + section_name)
                    print("Division:  " + division_name)
                    print("Group:  " + group_name)
                    # print(className)