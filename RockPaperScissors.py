import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_list = [rock,paper,scissors]

option_picked = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if (option_picked == '0'):
  print(f"You choose: {rock}")
  computer_option = random.choice(random_list)
  print(f"Computer choose: {computer_option}")
  if (option_picked == '0' and computer_option == random_list[0]):
    print("Tie")
  elif (option_picked == '0' and computer_option == random_list[1]):
    print("You lose")
  elif (option_picked == '0' and computer_option == random_list[2]):
    print("You win")
	
elif (option_picked == '1'):
  print(f"You choose: {paper}")
  computer_option = random.choice(random_list)
  print(f"Computer choose: {computer_option}")
  if (option_picked == '1' and computer_option == random_list[1]):
    print("Tie")
  elif (option_picked == '1' and computer_option == random_list[2]):
    print("You lose")
  elif (option_picked == '1' and computer_option == random_list[0]):
    print("You win")
	
elif (option_picked == '2'):
  print(f"You choose: {scissors}")
  computer_option = random.choice(random_list)
  print(f"Computer choose: {computer_option}")
  if (option_picked == '2' and computer_option == random_list[2]):
    print("Tie")
  elif (option_picked == '2' and computer_option == random_list[0]):
    print("You lose")
  elif (option_picked == '2' and computer_option == random_list[1]):
    print("You win")
	
else:
  print("You did not pick from 0, 1 or 2")
 