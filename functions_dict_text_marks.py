def remove_marks(text, marks):
    remove_marks.__dict__['count'] = remove_marks.__dict__.setdefault('count', 0) + 1
    for mark in marks:
        text = text.replace(mark, '')
    return text

text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)