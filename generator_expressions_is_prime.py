def is_prime(number):
    return all([number != 1, not any(number % i == 0 for i in range(2, number + 1) if i != number)])


print(is_prime(7))

print(is_prime(8))

print(is_prime(1))

# Нужно проверить равняется ли сумма делителей числа (т.е. к генераторному выражению применить сумму)
# самому числу плюс единице. И не нужно никаких дополнительных проверок