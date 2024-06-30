def convert(string):
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_syms_len = len(list(filter(lambda sym: sym in upper_letters, string)))
    lower_syms_len = len(list(filter(lambda sym: sym in lower_letters, string)))
    if lower_syms_len >= upper_syms_len:
        return string.lower()
    else:
        return string.upper()


# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()

print(convert('BEEgeek'))

print(convert('pyTHON'))

print(convert('pi31415!'))
