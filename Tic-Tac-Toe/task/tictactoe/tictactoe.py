game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
count = 0


def show():
    print("---------")
    print("|", " ".join(game[0]), "|")
    print("|", " ".join(game[1]), "|")
    print("|", " ".join(game[2]), "|")
    print("---------")


def check():
    x = list("".join(game[0] + game[1] + game[2]))
    if x[0] == x[1] == x[2] and x[0] != " ":
        return f"{game[0][0]} wins"
    elif x[3] == x[4] == x[5] and x[3] != " ":
        return f"{game[1][0]} wins"
    elif x[6] == x[7] == x[8] and x[6] != " ":
        return f"{game[2][0]} wins"
    elif x[0] == x[3] == x[6] and x[0] != " ":
        return f"{game[0][0]} wins"
    elif x[1] == x[4] == x[7] and x[1] != " ":
        return f"{game[0][1]} wins"
    elif x[2] == x[5] == x[8] and x[2] != " ":
        return f"{game[0][2]} wins"
    elif x[0] == x[4] == x[8] and x[0] != " ":
        return f"{game[0][0]} wins"
    elif x[2] == x[4] == x[6] and x[2] != " ":
        return f"{game[0][2]} wins"
    elif " " not in x:
        return "Draw"


def add():
    global count

    try:
        coord = list(map(int, input("Enter the coordinates: ").split(" ")))
        if any([True for i in coord if i > 3]):
            print("Coordinates should be from 1 to 3!")
            add()
        elif game[coord[0]-1][coord[1]-1] != " ":
            print("This cell is occupied! Choose another one!")
            add()
        else:
            game[coord[0]-1][coord[1]-1] = "X" if count % 2 == 0 else "O"
            check()
            count += 1
    except ValueError:
        print("You should enter numbers!")
        add()


while count < 9:
    show()
    add()
    if check() is not None:
        show()
        print(check())
        break
