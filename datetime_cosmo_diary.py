from datetime import datetime

with open('diary.txt', 'r', encoding='utf-8') as file:
    diary_notes = file.read().split('\n\n')

date_format = '%d.%m.%Y; %H:%M'
diary_dict = {datetime.strptime(note.split('\n', 1)[0].strip(), date_format): note.split('\n', 1)[1]
              for note in diary_notes}

for item in sorted(diary_dict):
    print(item.strftime(date_format))
    print(diary_dict[item])
    print()