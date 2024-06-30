def is_valid(string):
    return all([string.isdigit(), 4 <= len(string) <= 6])