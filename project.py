import random


while True:
    choice = input('Roll the Dice y/n: ')
    if choice=='y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice=='n':
       print('Thanks for playing. Byee!!!')
    break
else:
    print('Invalid choice!!!!')







import random

while True:

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print(f'You rolled: ({die1}, {die2})')

    choice = input('Roll again? y/n: ')

    if choice == 'n':
        print('Thanks for playing. Byee!!!')
        break

    elif choice != 'y':
        print('Invalid choice!!!!')
        break






import random

num_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
        if guess<num_guess:
            print('Too Low!')
        elif guess>num_guess:
            print('Too High!!')
        else:
            print('Congratulations!!!! You guessed right')
            break
    except ValueError:
        print('Please enter a valid number!!!')










import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
 
emojis = {ROCK:'🥌', PAPER:'📃', SCISSORS:'✂'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper or Scissors? (r/p/s): ')
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid Choice')
def display_chices(user_choice, comp_choice):
    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[comp_choice]}')

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
            print('TIE!!')
    elif (
            (user_choice == ROCK and comp_choice == SCISSORS) or 
            (user_choice == SCISSORS and comp_choice == PAPER) or 
            (user_choice == PAPER and comp_choice == ROCK)):
            print('You Won 🎉')
    else:
            print('!!!YOU LOST!!!')

def game_play():
    while True:
        user_choice = get_user_choice()
        
        comp_choice = random.choice(choices)

        display_chices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)

        wanna_continue = input('Continue (y/n): ').lower()
        if wanna_continue == 'n':
            print('Thanks for playing! 👋')
            break

game_play()


#QR Code Generator

import qrcode

data = input('Enter the data to encode in the QR code: ').strip()
filename = input('Enter the filename to save the QR code (e.g., qrcode.png): ').strip()
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
#qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(filename)
print(f'QR Code generated and saved as {filename}')