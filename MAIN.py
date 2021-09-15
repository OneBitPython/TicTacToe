import sys

my_list = []

for i in range(9):
    my_list.append(" ")

print("\nINSTRUCTIONS\nPlayer1 is X, player2 is 0")

taken = []


def draw():
    print("\n")
    print(my_list[0] + " | " + my_list[1] + " | " + my_list[2] + " | ")
    print("-------------")
    print(my_list[3] + " | " + my_list[4] + " | " + my_list[5] + " | ")
    print("-------------")
    print(my_list[6] + " | " + my_list[7] + " | " + my_list[8] + " | ")
    print("\n")


def Won(xo, Player):
    if (
        (my_list[0] == xo and my_list[1] == xo and my_list[2] == xo)
        or (my_list[3] == xo and my_list[4] == xo and my_list[5] == xo)
        or (my_list[6] == xo and my_list[7] == xo and my_list[8] == xo)
        or (my_list[0] == xo and my_list[3] == xo and my_list[6] == xo)
        or (my_list[1] == xo and my_list[4] == xo and my_list[7] == xo)
        or (my_list[2] == xo and my_list[5] == xo and my_list[8] == xo)
        or (my_list[0] == xo and my_list[4] == xo and my_list[8] == xo)
        or (my_list[2] == xo and my_list[4] == xo and my_list[6] == xo)
    ):
        print(f"{Player}, {xo} Won")
        sys.exit(0)


while True:
    available_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    player1 = input("Where do you want to put X : ")

    if player1 not in available_options:
        print("*Invalid")
    elif player1 in taken:
        print("Already taken.")
    else:
        my_list[int(player1) - 1] = "X"
        taken.append(player1)

        if len(taken) >= 9:
            draw()
            Won("X", "player1")
            Won("O", "Player2")

            sys.exit(0)

        draw()
        Won("X", "player1")
        Won("O", "Player2")

        while True:
            player2 = input("Where do you want to put O : ")
            if player2 not in available_options:
                print("*Invalid")
            elif player2 in taken:
                print("Already taken.")
            else:
                taken.append(player2)
                my_list[int(player2) - 1] = "O"

                draw()
                Won("X", "player1")
                Won("O", "Player2")

                if len(taken) >= 9:
                    draw()
                    Won("X", "player1")
                    Won("O", "Player2")

                    sys.exit(0)

                break
