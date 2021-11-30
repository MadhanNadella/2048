import board12 as bd
# import keyboard as kb



# print(
#     "Instructions:
#     Hi, welcome to 
#     ")

instructions = """
Hi, welcome to 2048!
Press Y to start the game
You can press Q at any point in the game to exit the game
"""

print(instructions)

while(1):
    inp=input("Key: ")
    # print(inp)
    if(inp=='y' or inp=='Y'):
        print("Great! Let's start the game")
        break
    elif(inp=='Q' or inp=='q'):
        print("Exiting the game.")
        exit()
    else:
        print("Invalid Key\n")


# a.printmatrix()

# instructions="""
# Press A S D W keys to swipe left, down, right and up. 
# """

# while(1):
#     inp=input("Key: ")
#     print(inp)
#     ismax=0
#     if(inp=='A' or inp == 'a'):
#         ismax= a.rearrange_rows(1)
#         a.regenerate()
#         a.printmatrix()
#     elif(inp=='D' or inp == 'd'):
#         ismax= a.rearrange_rows(-1)
#         a.regenerate()
#         a.printmatrix()
#     elif(inp=='W' or inp == 'w'):
#         ismax = a.rearrange_cols(1)
#         a.regenerate()
#         a.printmatrix()
#     elif(inp=='S' or inp == 's'):
#         ismax = a.rearrange_rows(-1)
#         a.regenerate()
#         a.printmatrix()
#     elif(inp=='Q' or inp=='q'):
#         print("Exiting the game.")
#         exit()
#     else:
#         print("Invalid key")

#     if(ismax==1):
#         print("Congratulations! You won!!")
#     elif(ismax==-1):
#         print("You lost. Better luck next time")

def play():
    a=bd.GameBoard()
    a.generate_initial()
    a.printmatrix()

    instructions="""
Press A S D W keys to swipe left, down, right and up. 
    """
    print(instructions)

    while(1):
        inp=input("Key: ")
        # print(inp)
        ismax=0
        if(inp=='A' or inp == 'a'):
            ismax= a.rearrange_rows(1)
            a.regenerate()
            a.printmatrix()
        elif(inp=='D' or inp == 'd'):
            ismax= a.rearrange_rows(-1)
            a.regenerate()
            a.printmatrix()
        elif(inp=='W' or inp == 'w'):
            ismax = a.rearrange_cols(1)
            a.regenerate()
            a.printmatrix()
        elif(inp=='S' or inp == 's'):
            ismax = a.rearrange_cols(-1)
            a.regenerate()
            a.printmatrix()
        elif(inp=='Q' or inp=='q'):
            print("Exiting the game.")
            exit()
        else:
            print("Invalid key")

        if(ismax==1):
            print("Congratulations! You won!!")
        elif(ismax==-1):
            print("You lost. Better luck next time")

while(1):
    play()

    replay="""
Press R to play again. Press Q to quit.
    """

    while(1):
        inp=input("Key: ")
        # print(inp)
        if(inp=='r' or inp=='R'):
            print("Great! Let's start the game")
            continue
        elif(inp=='Q' or inp=='q'):
            print("Exiting the game.")
            exit()
        else:
            print("Invalid Key\n")