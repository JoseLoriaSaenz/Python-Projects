computer_choice = "scissors"
user_choice = input("Do you want rock, paper or scissors? ")

if computer_choice == user_choice:
    print('TIE')
elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") 
        or (user_choice == "scissors" and computer_choice == "paper")):
    print('YOU WIN!')
else:
    print('YOU LOOSE!')