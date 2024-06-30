def get_length(number, counter=1):
    # базовый случай, выполняемый без рекурсии
    if len(number) <= 1:
        return counter
    #
    else:
        counter += 1
        return get_length(number[1:], counter)


num = input()
print(get_length(num))

# ndg = lambda x: 1 if x < 10 else ndg(x // 10) + 1
#
# print(ndg(int(input())))