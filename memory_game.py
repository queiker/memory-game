import os
import random

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def get_game_difficulty():
    width = 5
    height = None

    while height == None:
        user_input = int(input("Choose game difficulty: 1-easy, 2-medium, 3-hard: "))

        if user_input == 1:
            height = 4
        elif user_input == 2:
            height = 6
        elif user_input == 3:
            height = 10
        else:
            print("Incorect input!!")

    return width, height


def init_board(width, height):

#20,30,50
    if width*height % 2 != 0 :
        print("błąd programisty nie można wykonać funkcji")
    else:
        alphabet = "abcdefghijklmntoprstuwabcdefghijklmntoprstuw"
        digit_number = width*height
        digits_to_board = ""
        for i in range(0, int((width*height)/2)) :
            digits_to_board += alphabet[i]
            digits_to_board += alphabet[i]

        print(digits_to_board)
        list_of_digits = list(digits_to_board)
        #random.shuffle(list_of_digits)
        random.shuffle(list_of_digits)

        
        
        print(list_of_digits)
        board = []
        d = 0 
        for w in range(0, width):
            board.append([])
            for h in range(0, height):
                board[w].append(list_of_digits[d])
                d += 1


    
    #print(board)
    return board


def init_hidden_board(width, height):
    #return [["#","#","#"], ["#","#","#"], ["#","#","#"]]
    board = []
    for w in range(0, width):
        board.append([])
        for h in range(0, height):
            board[w].append("#")
    return board



def print_hidden_board(hidden_board):
    letters = ["A","B","C","D","E","F","G","H","I",]
    
    header_to_print = "  "
    for i in range(len(hidden_board[0])):
        header_to_print += letters[i]

    print(header_to_print)

    # ["#","#","#"]
    # 1
    for row_index in range(len(hidden_board)):
        row_to_print = str(row_index + 1) + " "
        for item in hidden_board[row_index]: # ["#","#","#"]
            row_to_print += item
        print(row_to_print)

def map_letter_to_coord(letter):
    if letter == "A":
        return 0

    if letter == "B":
        return 1

    if letter == "C":
        return 2
    
    if letter == "D":
        return 3

    if letter == "E":
        return 4

    if letter == "F":
        return 5

    #TODO

    return None

def map_letter_to_coord2(letter):
    letters = ["A","B","C","D","E","F","G","H","I",]

    for i in range(len(letters)):
        if letters[i] == letter:
            return i

    return None

def map_letter_to_coord3(letter):
    letters = ["A","B","C","D","E","F","G","H","I",]
    try:
        return letters.index(letter)
    except ValueError:
        return None


def get_user_input(width, height, hidden_board):
    input_incorrect = True

    while input_incorrect:
        user_input = input("Give coordinates(f.e. B2): ") # "B2"
        input_incorrect = False
        # możlisc b2 2b

        user_letter = user_input[0]
        user_number = user_input[1:]

        col_index = map_letter_to_coord2(user_letter.upper())
        row_index = int(user_number) - 1

        if col_index >= width or col_index < 0:
            print("Incorect letter!!!")
            input_incorrect = True

        if row_index >= height or row_index < 0:
            print("Incorect number!!!")
            input_incorrect = True

        if hidden_board[row_index][col_index] != "#":
            print("Place already discoverd!!!")
            input_incorrect = True

        # alternatywa dla 3 ifów zrobić to na if elif elif else
        

    return row_index, col_index

def mark(row, col, board, hidden_board):
    hidden_board[row][col] = board[row][col]
    return hidden_board

def unmark(row, col, hidden_board):
    hidden_board[row][col] = "#"
    return hidden_board

def main():
    print("Memory game")
    width, height = get_game_difficulty()
    board = init_board(width, height)
    hidden_board = init_hidden_board(width, height)

    while True:
        clear_screen()
        print_hidden_board(hidden_board)
        user_first_input = get_user_input(width, height, hidden_board)
        hidden_board = mark(user_first_input[0], user_first_input[1], board, hidden_board)
        clear_screen()
        print_hidden_board(hidden_board)
        user_second_input = get_user_input(width, height, hidden_board)
        hidden_board = mark(user_second_input[0], user_second_input[1], board, hidden_board)

        clear_screen()
        print_hidden_board(hidden_board)
        if board[user_first_input[0]][user_first_input[1]] == board[user_second_input[0]][user_second_input[1]]:
            print("You have guessed")
            input("Press enter to continue")
        else:
            hidden_board = unmark(user_first_input[0], user_first_input[1], hidden_board)
            hidden_board = unmark(user_second_input[0], user_second_input[1], hidden_board)
            print("Wrong guess")
            input("Press enter to continue")

        


if __name__ == "__main__":
    main()
