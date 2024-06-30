def to_binary(number):
    res = ''
    if number == 0:
        return 0
    else:
        def div(number, res):
            if number == 0:
                return res
            elif number % 2 == 0:
                res += '0'
            else:
                number -= 1
                res += '1'
            return div(number // 2, res)

    return div(number, res)[::-1]

# def to_binary(number):
#     if number <= 1:
#         return str(number)
#     return to_binary(number // 2) + str(number % 2)

print(to_binary(256))
