import pickle
import sys

filename = input()

with open(filename, mode='rb') as file:
    func = pickle.load(file)

print(func(*list(map(str.strip, sys.stdin))))

