import random
import time
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board, revealed):
    for i in range(len(board)):
        row = ''
        for j in range(len(board[i])):
            if revealed[i][j]:
                row += f' {board[i][j]} '
            else:
                row += ' * '
        print(row)
    print()


def create_board(size):
    num_pairs = (size * size) // 2
    numbers = list(range(1, num_pairs + 1)) * 2
    random.shuffle(numbers)

    board = []
    for i in range(size):
        board.append(numbers[i*size:(i+1)*size])
    
    return board


def all_pairs_found(revealed):
    return all(all(row) for row in revealed)

def memory_puzzle(size=4, time_limit=60):
    
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]

    start_time = time.time()

    while not all_pairs_found(revealed):
        clear_console()
        print_board(board, revealed)

      
        current_time = time.time()
        if current_time - start_time > time_limit:
            print("Time's up! You lost.")
            return
        
        try:
          
            print("Enter coordinates for the first card (row and column): ")
            row1, col1 = map(int, input().split())
            if revealed[row1][col1]:
                print("Card already revealed! Try again.")
                time.sleep(2)
                continue

       
            revealed[row1][col1] = True
            clear_console()
            print_board(board, revealed)

          
            print("Enter coordinates for the second card (row and column): ")
            row2, col2 = map(int, input().split())
            if revealed[row2][col2]:
                print("Card already revealed! Try again.")
                revealed[row1][col1] = False  
                time.sleep(2)
                continue

            revealed[row2][col2] = True
            clear_console()
            print_board(board, revealed)

            
            if board[row1][col1] != board[row2][col2]:
                print("No match! Cards will be hidden again.")
                time.sleep(2)
                revealed[row1][col1] = False
                revealed[row2][col2] = False
            else:
                print("Match found!")
                time.sleep(1)

        except (ValueError, IndexError):
            print("Invalid input. Please enter valid coordinates.")
            time.sleep(2)

    print("Congratulations! You found all pairs.")


if __name__ == "__main__":
    size = 4
    time_limit = 60  
    memory_puzzle(size, time_limit)
