import random
import string


# not so smart boggle board
# def boggle():
#     board = [
#         ["a","-","-","-"],
#         ["-","s","-","-"],
#         ["-","-","d","-"],
#         ["-","-","d","-"]
#     ]

#     for row in board:
#         for index, letter in enumerate(row): #letter is the string value itself
#             row[index] = random.choice(string.ascii_letters)
    
    
    # print('==============')
    # for row in board:
    #     print(" | ".join(row).upper())
        
    # print("==============")
        

# boggle()

#
#
#
#
#
#

#smarter boggle board

def check(user_input, selected_row, x, y, i):
    #horizontal
    
    if i == len(user_input):
        return True
    else:
        if f'{user_input[i].upper()} ' == selected_row[x - 1]:
            print('1')
            return check(user_input, selected_row, x-1, y, i+1)
        elif f'{user_input[i].upper()} ' == selected_row[x + 1]:
            print('2')
            return check(user_input, selected_row, x+1, y, i+1)
        else:
            return False





def boggle():
    board = [
        ["-","-","-","-"],
        ["-","-","-","-"],
        ["-","-","-","-"],
        ["-","-","-","-"]
    ]

    dice=[
        'AAEEGN',
        'ELRTTY',
        'AOOTTW',
        'ABBJOO',
        'EHRTVW',
        'CIMOTU',
        'DISTTY',
        'EIOSST',
        'DELRVY',
        'ACHOPS',
        'HIMNQU',
        'EEINSU',
        'EEGHNW',
        'AFFKPS',
        'HLNNRZ',
        'DEILRX'
    ]
###########################################################################
    for row in board:
        for index, letter in enumerate(row):
            random.shuffle(dice)
            selected_dice = list(dice[random.randint(0, 15)])
            random.shuffle(selected_dice)
            if selected_dice[0] == 'Q':
                row[index] = 'Qu'
            else:
                row[index] = selected_dice[0].ljust(2)
            
############################################################################
    print('=================')
    for row in board:
        new_board = " | ".join(row)
        print(new_board)
    print("=================")

    user_input= input("Enter a word: ")
#############################################################################
    x=0
    y=0
    i=1
    for y_coord, row in enumerate(board):
        if f'{user_input[0].upper()} ' in row:
            y = y_coord
            for x_coord, letter in enumerate(row):
                if f'{user_input[0].upper()} ' == letter:
                    x = x_coord

    selected_row = board[y]
    print(selected_row)

    if check(user_input, selected_row, x, y, i):
        print('success')
    else:
        print('fail')
    



    



boggle()