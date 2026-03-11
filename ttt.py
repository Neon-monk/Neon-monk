from random import randrange

game_table = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
free_boxes = 8
game_over = False

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console

    # Print 1st row
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ", board[0][0], "   |   ", board[0][1], "   |   ", board[0][2], "   |   ", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")

    # Print 2nd row
    print("|       |       |       |")
    print("|   ", board[1][0], "   |   ", board[1][1], "   |   ", board[1][2], "   |   ", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")

    # Print 3rd row
    print("|       |       |       |")
    print("|   ", board[2][0], "   |   ", board[2][1], "   |   ", board[2][2], "   |   ", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision

    global free_boxes
    player_move_made = False
    box_taken = False

    # Prompt for a number (1-9) until a move is made
    while player_move_made == False:
        # Non-integer is entered - Print warning, reprompt
        try:
            player_move = int(input("Enter your move: "))
        except ValueError:
            print("Please enter a number between 1-9")
            continue

        # Invalid number is entered - Print warning, reprompt
        if player_move < 1 or player_move > 9:
            print("That is not a valid box number!")
            continue
        # Valid number is entered
        else:
            # Check if box is taken
            for row in range(len(board)):
                for column in range(len(board)):
                    # Box is not taken - Replace number with 'O'
                    if board[row][column] == player_move:
                        board[row][column] = 'O'
                        free_boxes -= 1
                        player_move_made = True
                        display_board(board)
                        break
            # Box is taken
            if player_move_made == False:
                print("That box is already taken!")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers

    free_spaces = []

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != 'O' and board[row][column] != 'X':
                free_spaces.append((row, column))

    #print("Free spaces:", free_spaces)

def victory_for(board):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    global free_boxes
    global game_over

    while game_over == False:
        # Check diagonals
        if board[0][0] == 'X' and board[2][2] == 'X' \
        or board[0][2] == 'X' and board[2][0] == 'X':
            print("Computer wins!")
            game_over = True
            break
        # Check columns
        if game_over == False:
            for i in range(3):
                if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
                    print("Computer wins!")
                    game_over = True
                    break
                elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
                    print("You won!")
                    game_over = True
                    break
        # Check rows
        if game_over == False:
            for i in range(3):
                if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
                    print("Computer wins!")
                    game_over = True
                    break
                elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
                    print("You won!")
                    game_over = True
                    break

        if game_over == False and free_boxes == 0:
            print("Tie!")
            game_over = True

def draw_move(board):
    # The function draws the computer's move and updates the board

    global free_boxes
    computer_move_made = False

    # Pick a random box on the board
    while computer_move_made == False:
        for _ in range(free_boxes):
            random_row = randrange(3)
            random_column = randrange(3)

            # Check if box is available
            if board[random_row][random_column] != 'O' and board[random_row][random_column] != 'X':
                # Box is available, place 'X' on board
                board[random_row][random_column] = 'X'
                free_boxes -= 1
                computer_move_made = True
                break

while game_over == False:
    display_board(game_table)
    enter_move(game_table)

    if free_boxes < 5:
        victory_for(game_table)

    draw_move(game_table)
