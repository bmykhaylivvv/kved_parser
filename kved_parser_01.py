"""
Module documentation
"""
import json
import pprint


PATH = "kved.json"
source_json = open(PATH, encoding="utf-8")

data = json.load(source_json)

def parse_kved(class_code):
    """
    Documentation
    """
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
                        

                        result = {"Class_Name": class_name, "Group_Name": group_name,\
                             "Division_Name": division_name, "Section_Name": section_name,\
                                  "Section_Children": int(section_num),\
                                       "Division_Children": int(division_num),\
                                            "Group_Children": int(group_num)}
    return result

print(parse_kved("01.11"))

def write_json(parsed_json):
    """
    Documentation
    """
    final_json = {"name": parsed_json['Class_Name'],
                "type": "class",
                "parent": {
                    "name": parsed_json['Group_Name'],
                    "type": "group",
                    "num_children": parsed_json['Group_Children'],
                    "parent": {
                        "name": parsed_json['Division_Name'],
                        "type": "division",
                        "num_children": parsed_json['Division_Children'],
                        "parent": {
                            "name": parsed_json['Section_Name'],
                            "type": "section",
                            "num_children": parsed_json['Section_Children']
                    }
                }}}

    with open("kved_results.json", "w") as kved_result:
        json.dump(final_json, kved_result, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    write_json(parse_kved("01.11"))

