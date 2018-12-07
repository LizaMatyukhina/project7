import random

file_start = input('Enter the file name: ')
a = []
b = []

try:
    input_file = open(file_start, 'r')
    with open(file_start) as f_in:
        for line in f_in:
            a.append(line.strip())
            b.append(line.strip())
        for _ in range(len(a)):
            person = input('Enter your name and surname: ')
            while (person in a) is False:
                print('Your name was not find, please, try again!!')
                person = input()
            a.remove(person)
            b.remove(person)
            your_person = random.choice(b)
            b.remove(your_person)
            b.append(person)
            print('Your person for a game "Secret Santa" is: {}'.format(your_person))
except FileNotFoundError:
    print('File was not find:(')