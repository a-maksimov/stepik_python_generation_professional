# def print_digits(number):
#     if number > 0:
#         print(number % 10)
#         number //= 10
#         print_digits(number)

# печатаем последнюю цифру и, пока число больше 10, убираем последнюю цифру
def print_digits(n):
    print(n % 10)
    if n > 10:
        print_digits(n // 10)

print_digits(123456)
