import random as rnd

def roll_dice():
    return rnd.randint(1, 6) + rnd.randint(1, 6)

def print_player_rolled_msg(player_name, roll_value):
   print(player_name, 'rolled', roll_value)

def get_player_name(player_number):
   input_msg = 'Enter player '+ player_number +' name: '
   name = input(input_msg)
   return name


def main():
   player1 = get_player_name('1')
   player2 = get_player_name('2')

   roll1 = roll_dice()
   roll2 = roll_dice()

   print_player_rolled_msg(player1, roll1)
   print_player_rolled_msg(player2, roll2)

   if (roll1 > roll2):
      print(player1, 'wins!')
   elif (roll2 > roll1):
      print(player2, 'wins!')
   else:
      print('You tie!')

main()