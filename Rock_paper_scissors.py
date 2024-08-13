# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 04:49:34 2024

@author: USER-PC
"""

##Random generator
import random

rand_2 = random.random() * 5
print(rand_2)

##Banker's Roulette
names_string = input("Give the name seperated by commas:\n")
names = names_string.split(', ')
print(names)
##Randomly selecting a name
sel = random.randint(0, 4)
print(f'{names[sel]} is going to buy the meal today!')

##Treasure map
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","️⬜️","️⬜️"]
line3 = ["⬜️","️⬜️","️⬜️"]
##Map creation
maps = [line1, line2, line3]
print(maps)
print('Hiding your treasure! X maps the spot')
position_x = int(input('Where would you like to place the treasure? (Rows)\n'))
position_y = int(input('Where would you like to place the treasure? (Columns)\n'))
maps[position_x-1][position_y-1] = 'X'
print(maps)

##Alternatively_Treasure map
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","️⬜️","️⬜️"]
line3 = ["⬜️","️⬜️","️⬜️"]
##Map creation
maps = [line1, line2, line3]
print(maps)
print('Hiding your treasure! X maps the spot')
position = input('Where would you like to hide the treasure?\n')
letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_ind = abc.index(letter)
number_ind = int(position[1]) - 1                      
maps[letter_ind][number_ind] = 'X'
print(f'{line1}\n{line2}\n{line3}')

##Rock_Paper_Scissors
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

human = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n')) 
computer = random.randint(0, 2)
options = ['rock', 'paper', 'scissors']
human_choice = options[human]
computer_choice = options[computer]
##Evaluate the results
if human == computer:
    print('You selected', options[human],'and the computer selected', options[computer])
    print("That's a draw!")
elif human_choice == 'rock' and computer_choice == 'paper':
    print('You selected', human_choice,'and the computer selected', computer_choice)
    print("You lose")
    print(paper)
elif human_choice == 'rock' and computer_choice == 'scissors':
    print('You selected', human_choice,'and the computer selected', computer_choice)
    print("You win")
    print(rock)
elif human_choice == 'paper' and computer_choice == 'scissors':
    print('You selected', human_choice,'and the computer selected', computer_choice)
    print("You lose")
    print(scissors)
elif human_choice == 'paper' and computer_choice == 'rock':
    print('You selected', human_choice,'and the computer selected', computer_choice)
    print("You win")
    print(paper)
elif human_choice == 'scissors' and computer_choice == 'rock':
    print('You selected', human_choice,'and the computer selected', computer_choice)
    print("You lose")
    print(rock)
elif human_choice == 'scissors' and computer_choice == 'paper':
    print('You selected', human_choice,'and the computer selected', computer_choice)
    print("You win")
    print(scissors)
else:
    print('Invalid result...Game over!!')
    


