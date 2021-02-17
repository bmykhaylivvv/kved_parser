"""
Module documentation
"""
import json
import pprint


PATH = "kved.json"
source_json = open(PATH, encoding="utf-8")

data = json.load(source_json)
class_code = "01.12"

def parse_kved(class_code):
    for section in data["sections"][0]:
        section_name = section["sectionName"]
        section_num = len(data["sections"][0])
        for division in section["divisions"]:
            division_name = division["divisionName"]
            division_num = len(section["divisions"])
            for group in division["groups"]:
                group_name = group["groupName"]
                group_num = len(division["groups"])
                for group_class in group["classes"]:
                    if group_class["classCode"] == class_code:
                        class_name = group_class["className"]

                        # print("Class:  " + class_name)
                        # print("Section:  " + section_name)
                        # print("Division:  " + division_name)
                        # print("Group:  " + group_name)
                        print(section_num)
                        print(division_num)
                        print(group_num)
                        result = {"Class_Name": class_name, "Group_Name": group_name,\
                             "Division_Name": division_name, "Section_Name": section_name}
                        return result
                    # print(className)

# Додати num_children
print(parse_kved("01.11"))