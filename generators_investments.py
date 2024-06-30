with open('investment.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, data)) for data in line_values)
    result = sum(int(line_dict['raisedAmt']) for line_dict in line_dicts if line_dict['round'] == 'a')
    print(result)