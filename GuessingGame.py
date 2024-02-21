# GUESSING NUMBER GAME
# The game will have 2 players or more. 
    # If user inputs more players or less players then will ask to repeat. 

# Each player will be assigend random list of numbers
    # each list of number will have 5 digits. NUMBERS WILL ONLY BE FROM 1-10

# Each player will have 1 turn to guess the number in the other person's list
    # Wrong guess will have an "wrong" display and right will have a "Right output"
    # the right answers will be saved. 

# Once player has guessed all numbers that player will win. 
    # Then will output the winning celebration message. 

import random

print ("WELCOME TO THE GUESSING NUMBER GAME\n created by Christopher Williams")

while True:
    numOfPlayers = input("Enter the number of players (2 - 4): ")
    if numOfPlayers.isdigit():
        numOfPlayers = int(numOfPlayers)
        if numOfPlayers >=2 and numOfPlayers <= 4:
            break
        else:
            print("Number must be 2 - 4 players")
    else:
        print("Invalid input")
 
playerNames = []
playersNumbers = []
guessedNumbers = {}


for _ in range(numOfPlayers):
    enterName = input("Enter player name: ")
    playerNames.append(enterName)
    randomNumbers = [random.randint(1, 10) for _ in range(5)]
    playersNumbers.append(randomNumbers)
    guessedNumbers[enterName] = set()

for i, (name, numbers) in enumerate(zip(playerNames, playersNumbers), start=1):
    print(f"Player {i}: {name} Random numbers are: {numbers}")


current_player_index = 0 
while True:
    current_player = playerNames[current_player_index]  
    opponent_numbers = playersNumbers[(current_player_index + 1) % numOfPlayers]  
    print(f"\n{current_player}, it's your turn to guess {playerNames[(current_player_index + 1) % numOfPlayers]}'s numbers!")

    guessed_numbers = guessedNumbers[current_player]  
    while True:  
        guess = int(input("Enter your guess (a number between 1 and 10): "))
        if guess in guessed_numbers:
            print("You've already guessed this number. Try again!")
        else:
            guessed_numbers.add(guess)
            if guess in opponent_numbers:
                print("Correct guess! You got it right!")
            else:
                print("Incorrect guess..")
            break  


    if guessed_numbers == set(opponent_numbers):  
        print(f"{current_player} has guessed all numbers! They win!")
        break

    current_player_index = (current_player_index + 1) % numOfPlayers  
