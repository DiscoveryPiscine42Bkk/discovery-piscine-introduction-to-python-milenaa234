def array_of_names(name_dict):
    full_name = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_name.append(full_name)
    return full_name

persons = {
    "Natthaphong": "Kaewduangdee",
    "Charukan": "Sombut",
    "peemai": "fang",
    "fang": "peemai"
 }

print(array_of_names(persons))