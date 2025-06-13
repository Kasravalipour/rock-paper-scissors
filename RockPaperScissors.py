import random

round_count = 0

# every 4 rounds
def ask():
     answer = input('do you wonna play?(y/n): ').lower()
     if answer in ['y', 'n']:
          return answer == 'y'
     

while True:
    user_action = input('Enter your choice : ')
    ai_actions = ['rock', 'paper', 'scissors']
    ai_move = random.choices(ai_actions)

# show the choises
    print(f"\nYou choose {user_action}, and the camputer choose {ai_move}")

# how is the winner?
# halaty ke mosavi beshan
    if user_action == ai_actions:
        print(f"both players choosed {user_action}, DRAW!")

    # human comes rock
    if user_action == 'rock' and ai_move =='rock':
        print('Draw!')

    elif user_action == 'rock' and ai_move == "paper":
        print('ai win !')
    
    elif user_action == 'rock' and ai_move == 'scissors':
        print('human win !')
    
    # human comes paper
    if user_action == 'paper' and ai_move == 'paper':
        print(f"both players choosed {user_action}, DRAW!")

    elif user_action == 'paper' and ai_move == 'rock':
            print(F'you comed paper and ai comes {ai_move}, YOU WIN !')

    elif user_action == 'paper' and ai_move == 'scissors':
         print(f'you comed paper and ai choosed {ai_move}, AI WINS')

    # humman comes scissors
    if user_action == 'scissors' and ai_move == 'scissors':
         print(f'both sides choosed {user_action}, DRWA!')
    
    elif user_action == 'scissors' and ai_move == 'rock':
         print(f'you choosed {user_action} and ai choosed {ai_move}, HUMAN WINS')
        
    elif user_action == 'scissors' and ai_move == 'paper':
         print(f'you choosed {user_action} and ai choosed {ai_move}, HUMAN WINS !')


    #if roun