board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
win = 0


def print_board():
    print("")
    n = 0
    for i in board:
        print(str(board[n][0]) + " | " + str(board[n][1]) + " | " + str(board[n][2]))
        n += 1
    print("")


def move_x():
    position = input("Choose a position from 1 to 9: ")
    if position.isdigit():
        position = int(position)
        if 1 <= position <= 3 and board[0][position - 1] == '-':
            board[0][position - 1] = "x"
        elif 4 <= position <= 6 and board[1][position - 4] == '-':
            board[1][position - 4] = "x"
        elif 7 <= position <= 9 and board[2][position - 7] == '-':
            board[2][position - 7] = "x"
        else:
            print("Wrong move!")
            print("")
            move_x()
    else:
        print("Wrong move!")
        print("")
        move_x()


def move_o():
    position = input("Choose a position from 1 to 9: ")
    if position.isdigit():
        position = int(position)
        if 1 <= position <= 3 and board[0][position - 1] == '-':
            board[0][position - 1] = "o"
        elif 4 <= position <= 6 and board[1][position - 4] == '-':
            board[1][position - 4] = "o"
        elif 7 <= position <= 9 and board[2][position - 7] == '-':
            board[2][position - 7] = "o"
        else:
            print("Wrong move!")
            print("")
            move_o()
    else:
        print("Wrong move!")
        print("")
        move_o()


def x_win(win):
    if board[0][0] == board[0][1] == board[0][2] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[1][0] == board[1][1] == board[1][2] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[2][0] == board[2][1] == board[2][2] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[0][0] == board[1][0] == board[2][0] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[0][1] == board[1][1] == board[2][1] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[0][2] == board[1][2] == board[2][2] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[0][0] == board[1][1] == board[2][2] == 'x':
        print("Congratulations, x won!")
        return win == 1
    elif board[0][2] == board[1][1] == board[2][0] == 'x':
        print("Congratulations, x won!")
        return win == 1


def o_win(win):
    if board[0][0] == board[0][1] == board[0][2] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[1][0] == board[1][1] == board[1][2] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[2][0] == board[2][1] == board[2][2] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[0][0] == board[1][0] == board[2][0] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[0][1] == board[1][1] == board[2][1] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[0][2] == board[1][2] == board[2][2] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[0][0] == board[1][1] == board[2][2] == 'o':
        print("Congratulations, o won!")
        return win == 1
    elif board[0][2] == board[1][1] == board[2][0] == 'o':
        print("Congratulations, o won!")
        return win == 1


def clear_board():
    board[0][0] = '-'
    board[0][1] = '-'
    board[0][2] = '-'
    board[1][0] = '-'
    board[1][1] = '-'
    board[1][2] = '-'
    board[2][0] = '-'
    board[2][1] = '-'
    board[2][2] = '-'


def game():
    print_board()
    i = 0
    while True:
        print("X TURN")
        move_x()
        print_board()
        if x_win(1):
            print("Game over!")
            break
        if i == 8:
            print("It's a Tie!")
            print("Game over!")
            break
        i += 1
        print("O TURN")
        move_o()
        print_board()
        if o_win(1):
            print("Game over!")
            break
        i += 1
    again = input("Wanna play again?(y/n): ")
    if again == 'y':
        clear_board()
        game()


print("Welcome to the tic-tac-toe game!")
game()