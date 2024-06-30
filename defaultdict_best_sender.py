from collections import defaultdict


def best_sender(messages, senders):
    messages_dict = defaultdict(int)
    for message, sender in zip(messages, senders):
        messages_dict[sender] += len(message.split())
    return max(sorted(messages_dict, reverse=True), key=lambda name: messages_dict[name])


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))
