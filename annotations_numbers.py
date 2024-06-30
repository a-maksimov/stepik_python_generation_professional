def get_digits(number: int | float) -> list[int]:
    return [int(num) for num in (str(number).replace('.', ''))]


print(get_digits(13.909934))
