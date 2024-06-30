from collections import Counter


def print_bar_chart(data, mark):
    max_len = len(max(data, key=len))
    for item, num in sorted(Counter(data).items(), key=lambda d: d[1], reverse=True):
        print(f'{item}'.ljust(max_len), f'|{mark * num}')


print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')
