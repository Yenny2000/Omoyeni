import random

comp_wins = 0
player_wins = 0

def choose_option ():
    user_choice = input ('Choose Rock, Paper or Scissors: ')
    if user_choice in ['Rock', 'rock', 'R', 'r']:
        user_choice = 'r'
    elif user_choice in ['Paper', 'paper', 'P', 'p']:
          user_choice = 'p'
    elif user_choice in ['Scissors', 'scissors', 'S', 's']:
          user_choice = 's'
    else: 
         print('error')
    return user_choice    
def computer_option():
         comp_choice = random.randint (1, 3)
         if comp_choice == 1:
             comp_choice = 'r'
         elif comp_choice == 2: 
             comp_choice = 'p'
         else:
             comp_choice ='s'
         return comp_choice
         
while True:
     print('') 
     user_choice = choose_option()
     comp_choice = computer_option()
     print('')

     if user_choice == 'r':
      if comp_choice =='r':
          print ('Player; rock, CPU; rock. You tied')   
      elif comp_choice =='p':
          print ('Player; rock, CPU; paper. You lose') 
          comp_wins +=1

      elif comp_choice =='s':
          print ('Player; rock, CPU; scissors. You win') 
          player_wins +=1

     if user_choice == 'p': 
       if comp_choice =='r':
         print ('Player; paper, CPU; rock. you win')
         player_wins += 1

         if comp_choice =='p':
          print ('Player; paper, CPU; paper. you tied')

       if comp_choice =='s':
         print ('Player; paper, CPU; scissors. you lose')
         comp_wins +=1
     if user_choice == 's':
          if comp_choice =='r':
           print ('Player; scissors, CPU; rock. you lose')
           comp_wins += 1
     if comp_choice =='s':
         print ('Player; scissors, CPU; scissors. you tied')

     if comp_choice =='p':
         print ('Player; scissors, CPU; paper. you win')
         player_wins +=1

print('')
print('Player wins:' + str(player_wins))
print('Computer wins:'+ str(comp_wins))
print('')

user_choice = input('do you want to play again? (y/n')
