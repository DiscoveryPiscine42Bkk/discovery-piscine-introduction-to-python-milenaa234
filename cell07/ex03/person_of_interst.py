def famous_births(figures):

    sorted_figures = sorted(figures.values(), key=lambda person: int(person["date_of_birth"]))

    for person in sorted_figures:
        print(f'{person["name"]} is great scientist born in {person["date_of_birth"]}')

        scientists = {
            "a": { "name": "G", "date_of_birh": "3333" },
            "b": { "name": "E", "date_of_birh": "6666" },
            "c": { "name": "N", "date_of_birh": "1000" },
            "d": { "name": "O", "date_of_birh": "2007" },
        }

        famous_births(scientists)