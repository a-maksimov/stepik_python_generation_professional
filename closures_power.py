def power(degree):
    def calculate(number):
        return number ** degree
    return calculate


square = power(2)

print(square(5))
