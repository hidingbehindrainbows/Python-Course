import random
from idea import findBestMove

def win(dict3):
    if dict3[1] == dict3[2] == dict3[3]  != '':
        if dict1[1].casefold() == 'x':
            return 1
        else:
            return -1
    elif dict3[4] == dict3[5] == dict3[6]  != '':
        if dict1[4].casefold() == 'x':
            return 1
        else:
            return -1
    elif dict3[7] == dict3[8] == dict3[9] != '':
        if dict1[7].casefold() == 'x':
            return 1
        else:
            return -1
    elif dict3[1] == dict3[4] == dict3[7] != '':
        if dict1[1].casefold() == 'x':
            return 1
        else:
            return -1 
    elif dict3[2] == dict3[5] == dict3[8] != '':
        if dict1[2].casefold() == 'x':
            return 1
        else:
            return -1
    elif dict3[3] == dict3[6] == dict3[9] != '':
        if dict1[3].casefold() == 'x':
            return 1
        else:
            return -1
    elif dict3[1] == dict3[5] == dict3[9] != '':
        if dict1[1].casefold() == 'x':
            return 1
        else:
            return -1
    elif dict3[3] == dict3[5] == dict3[7] != '':
        if dict1[3].casefold() == 'x':
            return 1
        else:
            return -1
    else:
        return None
    

def drawboard(x,character,dict2):
    dict2[x] = character
    if x in {1,2,3,4,5,6,7,8,9}:
        print(f'  {dict2[1]}   |   {dict2[2]}   |   {dict2[3]}')
        print('-'*25)
        print(f'  {dict2[4]}   |   {dict2[5]}   |   {dict2[6]}')
        print('-'*25)
        print(f'  {dict2[7]}   |   {dict2[8]}   |   {dict2[9]}')
        print('*'*50)
    else:
        print("This isn't ok to type.")
        

def check(y,list2):
    if y in list2:
        y = random.randint(1,9)
        return check(y,list2)
    else:
        list2.append(y)
        return y
    
               
def check_character(character):
    if character.casefold() != 'x' and character.casefold() != 'o':
        print("This is not ok to type.")
        character = input("Enter the right one please. ")
        return check_character(character)
    else:
        return character.upper()
              


list1 = []
won = 0
dict1 = {
    1:'', 
    2:'',
    3:'',
    4:'',
    5:'',
    6:'',
    7:'',
    8:'',
    9:'',
    }
XO = input("Do you want to be X or O? ")
XO = check_character(XO)
if XO.casefold() == 'x':
    computer_character = 'O'
else:
    computer_character = 'X'
choice='-'
count=0

while count!=5:
    won = win(dict1)
    if won == 1:
        print(f"Player X has won!!!!")
        break
    elif won == -1:
        print("Player O has won!!!")
    else:
        if computer_character == 'X':
            # computer_choice = random.randint(1,9)
            computer_choice = findBestMove(dict1, computer_character, XO)
            # computer_choice = check(computer_choice,list1)
            computer_choice = computer_choice[0] * 3 + computer_choice[1] + 1
            computer_choice = check(computer_choice,list1)
            drawboard(computer_choice,computer_character,dict1)
            choice = int(input("Enter your choice: "))
            list1.append(choice)
            drawboard(choice, XO, dict1)
        else:
            choice = int(input("Enter your choice: "))
            list1.append(choice)
            drawboard(choice, XO, dict1)
            # computer_choice = random.randint(1,9)
            computer_choice = findBestMove(dict1, computer_character, XO)
            # computer_choice = check(computer_choice,list1)
            computer_choice = computer_choice[0] * 3 + computer_choice[1] + 1
            computer_choice = check(computer_choice,list1)
            drawboard(computer_choice,computer_character,dict1)
    count+=1
if count == 9:
    print("All your chances are done! Neither of you won")
