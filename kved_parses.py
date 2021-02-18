"""
Module documentation
"""
import json

# PATH = "kved.json"

source_json = open("kved.json", encoding="utf-8")

data = json.load(source_json)

def json_parser(class_code):
    """
    Documentation
    """
    for section in data["sections"][0]:
        section_name = section["sectionName"]
        for division in section["divisions"]:
            division_name = division["divisionName"]
            division_num = len(section["divisions"])
            for group in division["groups"]:
                group_name = group["groupName"]
                group_num = len(division["groups"])
                for group_class in group["classes"]:
                    if group_class["classCode"] == class_code:
                        class_name = group_class["className"]
                        class_num = len(group["classes"])
                        result = {"Class_Name": class_name, "Group_Name": group_name,\
                             "Division_Name": division_name, "Section_Name": section_name,\
                                  "Class_Children": int(class_num),\
                                       "Division_Children": int(division_num),\
                                            "Group_Children": int(group_num)}
    return result


def parse_kved(class_code):
    """
    Documentation
    """
    parsed_json = json_parser(class_code)
    final_json = {"name": parsed_json['Class_Name'],
                "type": "class",
                "parent": {
                    "name": parsed_json['Group_Name'],
                    "type": "group",
                    "num_children": parsed_json['Class_Children'],
                    "parent": {
                        "name": parsed_json['Division_Name'],
                        "type": "division",
                        "num_children": parsed_json['Group_Children'],
                        "parent": {
                            "name": parsed_json['Section_Name'],
                            "type": "section",
                            "num_children": parsed_json['Division_Children']
                    }
                }}}

    with open("kved_results.json", "w") as kved_result:
        json.dump(final_json, kved_result, indent=4, ensure_ascii=False)


parse_kved("05.20")