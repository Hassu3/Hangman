import emoji
import random

words = ['kacha', 'dragon', 'dog', 'cat', 'dinosaur', 'tank', 'rafał', 'kuba', 'roses', 'predator', 'pyton']
hangman = random.choice(words)
print("Welcome")
password = list(len(hangman) * "-")
print("Guess the password " + ''.join(password))

p = 6
z = 5
x = 0
i = 0
answer = ""
letter_from_user = ""
draw = ['', 'You have 4 more chances', 'You have 3 more chances', 'You have 2 more chances',
        'You have 1 more chances', 'You were hanged x_x', ]

while answer != hangman and x != z:
    if z - x < p:
        print(draw[i])
        i += 1
        p -= 1
    if x != z:
        letter_from_user = input('please enter a letter ')
        x += 1
    y = -1
    for letters_in_word in hangman:
        y += 1
        if letter_from_user.lower() == letters_in_word:
            password[y] = letter_from_user.lower()
            answer = "".join(password)  # change list to string
            print(answer.lower())
            z += 1

    if answer.lower() == hangman.lower():
        print(emoji.emoji_converter("Bravo, You WIN! :) The answer is " + answer.title()))
        break
else:
    print(emoji.emoji_converter("You have lost :( Correct answer is: " + hangman.title() + " " + draw[5]))