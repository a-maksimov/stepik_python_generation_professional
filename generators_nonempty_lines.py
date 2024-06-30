def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        file_lines = (line for line in file)
        yield from (line.strip() if len(line) <= 25 else "..." for line in file_lines if line.strip())

