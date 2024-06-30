def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        file_lines = (line.strip() for line in file)
        planets = []
        planet = []
        for line in file_lines:
            if line != '':
                planet.append(line)
            else:
                planets.append(planet)
                planet = []
        planets.append(planet)

        yield from (dict(parameter.split(' = ') for parameter in planet) for planet in planets)


planets = txt_to_dict()

print(next(planets))

print()

print(*planets)