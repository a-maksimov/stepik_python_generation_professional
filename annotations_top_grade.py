def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    top_grade = max(grades['grades'])
    del grades['grades']
    grades['top_grade'] = top_grade
    return grades


info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))
