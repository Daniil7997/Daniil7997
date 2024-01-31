import random
import re


def input_letter():
    while True:
        try_input = input('введите букву: ')
        if len(try_input) == 1 and re.match('[А-Яа-я]', try_input):
            return try_input


def input_heal():
    while True:
        try_input = input('количество попыток: ')
        if re.match('[0-9]+', try_input) and int(try_input) > 0:
            return try_input


def replace():
    global heal
    if letter_input not in letter_word:
        heal = heal - 1
        print(f'ошибка! -1 попытка. количество попыток: {heal}')
    while letter_input in letter_word:
        index = letter_word.index(letter_input)
        guess_word[index] = letter_input
        letter_word[index] = '_'
        print(*guess_word)


while True:

    heal = int(input_heal())

    word_list = ["кошка", "собака"]
    secret_word = random.choice(word_list)

    print(f'Длина слова {len(secret_word)} букв')

    letter_word = list(secret_word)

    guess_word = []
    for i in range(len(letter_word)):
        guess_word.append('_')

    while "_" in guess_word:

        if heal <= 0:
            print('не получилось =(')
            break

        letter_input = input_letter()
        replace()

    if guess_word == list(secret_word):
        print('ПОБЕДА!!!')

    answer_up = None
    while answer_up != 'ДА' and answer_up != 'НЕТ':
        answer_up = input('Хотите сыграть ещё ? ДА или НЕТ ?').upper()

    if answer_up == 'ДА':
        continue
    elif answer_up == 'НЕТ':
        break
