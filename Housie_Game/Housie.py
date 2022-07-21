import random

MAIN_LIST = random.sample(range(1,101),12) 

player1 = MAIN_LIST[:6]
player2 = MAIN_LIST[6:]

random.shuffle(MAIN_LIST)
EXTRA_LIST = MAIN_LIST
print(MAIN_LIST)
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")

status = True
while status:
    RANDOM_TICKET = random.choice(EXTRA_LIST)
    print(input(f"Number: {RANDOM_TICKET}"))
    #print("---> ",RANDOM_TICKET)
    if RANDOM_TICKET in player1:
        player1.remove(RANDOM_TICKET)
        EXTRA_LIST.remove(RANDOM_TICKET)
        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")
    else:
        player2.remove(RANDOM_TICKET)
        EXTRA_LIST.remove(RANDOM_TICKET)
        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")
    if len(player1)==0:
        status = False
        print("PLAYER 1 WON ")
    elif len(player2)==0:
        status = False
        print("PLAYER 2 WON ")
