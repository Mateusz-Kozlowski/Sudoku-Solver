def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                a = board[i][j]
                if a == 0:
                    print(" ")
                else:
                    print(str(a))
            else:
                a = board[i][j]
                if a == 0:
                    print(" " + " ", end="")
                else:
                    print(str(a) + " ", end="")


def solve(board):
    empty = find_empty_field(board)
    if empty is None:
        return True
    y, x = empty

    for i in range(1, 10):
        if is_correct(board, i, x, y):
            board[y][x] = i

            if solve(board):
                return True

            board[y][x] = 0

    return False


def find_empty_field(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


def is_correct(board, value, x, y):
    # check row:
    for i in range(len(board[0])):
        if board[y][i] == value and i != x:
            return False

    # check column:
    for i in range(len(board)):
        if board[i][x] == value and i != y:
            return False

    # check box (3x3 square):
    y0 = y // 3
    y0 *= 3
    x0 = x // 3
    x0 *= 3
    for i in range(y0, y0 + 3):
        for j in range(x0, x0 + 3):
            if board[i][j] == value and i != y and x != j:
                return False

    return True


def main():
    while True:
        path = str(input('Enter a file path that contains a sudoku puzzle (or q if u want to exit): '))

        if path == 'q':
            break

        try:
            with open(path) as file:
                board = [[int(x) for x in line.split()] for line in file]
                print("\nBefore solving: ")
                print_board(board)
                print("\nResolution is in progress...")
                if solve(board) is False:
                    print('\n' + "Invalid example, solving the problem is impossible!")
                else:
                    print('\n' + "Solved sudoku: ")
                    print_board(board)
                print("")
        except IOError:
            print("File not accessible")
            print('Did u forget about an extension?')
            print('Anyway try again...')


if __name__ == '__main__':
    main()

print('Code is done, so everything works fine!')
# sth
