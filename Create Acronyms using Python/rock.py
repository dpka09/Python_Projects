# import random

# attributes='abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
# len=int(input("Enter length"))
# print("".join(random.sample(attributes,len)))


# import random
# passlen = int(input("enter the length of password"))
# s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# p = "".join(random.sample(s,passlen ))
# print(p)


import random


choices=['Rock','Paper','Scissor']

computer_score=0
player_score=0

while True:
    #computer=random.choice(choices)
    player= input("Rock , Paper or Scissor ?\n").capitalize()
    computer=random.choice(choices)
    print("Computer ans: ", computer)
    if player==computer:
        print("Its a Tie")
    elif player == 'Rock' and computer=='Scissor':
        print("Player smashes Computer")
        player_score=player_score+1
    elif player == 'Rock' and computer =='Paper':
        print("Computer smashes Player")
        computer_score= computer_score+1
    elif player== 'Paper' and computer == 'Rock':
        print("Player smashes Computer")
        player_score= player_score+1
    elif player == 'Paper' and computer== 'Scissor':
        print("Computer smashes Player")
        computer_score= computer_score+1
    elif player == 'Scissor' and computer  =='Rock':
        print('Computer smashes Player')
        computer_score= computer_score+1
    elif player== 'Scissor' and computer == 'Paper':
        print("Player smashes Computer")
        player_score= player_score+1
    elif player == 'End':
        print("Computer_score: {}".format(computer_score))
        print("Player_score: {}".format(player_score))
        if computer_score> player_score:
            print ('Computer wins!!!!')
        else:
            print("PLayer wins!!!!")
        
        break

