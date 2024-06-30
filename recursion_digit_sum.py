def get_sum(number, sum=0):
    # базовый случай, выполняемый без рекурсии
    if len(number) < 1:
        return sum
    else:
        sum += int(number[-1])
        return get_sum(number[:len(number) - 1], sum)


num = '25'
print(get_sum(num))

# ndg = lambda x: 1 if x < 10 else ndg(x // 10) + 1
#
# print(ndg(int(input())))