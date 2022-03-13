import art
import random
import os

# NUMBER GUESSING!

# Original loop!
while True:

    # Displaying starting of the game
    print(art.logo)
    print('\nWELCOME TO THE NUMBER GUESSING GAME! 😃')
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    print('\nYou have to choose a number between 1-100')

    # Ask for difficulty
    print('\nPlease choose your difficulty:-')
    print('Press (1) for easy mode. (12 choices)')
    print('Press (2) for medium mode. (8 choices)')
    print('Press (3) for hard mode. (5 choices)')
    print('Press (4) for 🔥GOD🔥 mode!')
    print('Press (0) to exit game.')
    difficulty = input('Enter your choice: ')

    # Create a random number between 1 and 100
    random_number = random.randint(1,100)

    # Set up up the difficulty as per the user's choice
    if difficulty == '1':
        life = 12
    elif difficulty == '2':
        life = 8
    elif difficulty == '3':
        life = 5
    elif difficulty == '4':
        life = 1
    elif difficulty == '0':
        print('\nExiting game!\n')
        break
    else:
        print('\nInvalid input! Exiting game!\n')
        break

    # User starting to guess the number!
    print('\n! GAME ON ! \nBest of luck 😃')

    # Game starts

    # GOD MODE!
    if life == 1:
        print('\nWELCOME TO GOD MODE 🔥\nYou will only have 1 choice!')
        user_guess = int(input('Enter guess: '))
        
        # Checking win or loose
        if user_guess == random_number:
            print('\nCONGRATULATIONS!! 🍾🍾\nYou won the GOD mode challenge!')
        else:
            print('\nSorry! 🥱\nYou failed GOD mode challenge!')
            print(f"Correct answer is {random_number}")

    # NORMAL MODE
    else:        
        while True:
            # Checking for conditions!
            print(f"\nYour lives: {life}")
            user_guess = int(input('Enter guess: '))
            if user_guess == random_number:
                print(f'\nCongratulations! 🤩\nYou guessed correctly with {life} number of lives!')
                break
            elif user_guess > random_number: # 80 , 40
                print('\nSorry your guessed number is bigger than answer! 😐')
                life -= 1
            elif user_guess < random_number:
                print('\nSorry your guessed number is smaller than answer! 🤐')
                life -= 1
                
            # Checking if out of lives!
            if life == 0:
                print('\nSorry game over!\nYou are out of lives! 🙁')
                print(f"Correct answer is {random_number}")
                break
            
    # Asking if they again want to play the game!
    play_again = input('\nDo you want to play again? (Y/N): ')

    if play_again[0].upper() == 'Y':
        os.system('cls')
        continue
    elif  play_again[0].upper() == 'N':
        print('\nThank you for playing with us! 😊\n')
        break
    else:
        print('\nInvalid input! Exiting game!\n')
        break