#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False

    def print_board(self, reveal=False):
        clear_screen()
        print('    ' + '   '.join(str(i) for i in range(self.width)))
        print('  ' + '---' * self.width)
        for y in range(self.height):
            print(f"{y} |", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print(' * ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f' {count} ' if count > 0 else '   ', end='')
                else:
                    print(' . ', end='')
            print('|')
        print('  ' + '---' * self.width)

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            self.game_over = True
            return False
        if self.revealed[y][x]:
            return True
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print("Coordinates out of range. Try again.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\nGame Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        else:
            print("\nCongratulations! You've cleared the minefield.")

def main():
    print("Welcome to Minesweeper!")
    try:
        width = int(input("Enter width of the grid (default 10): ") or 10)
        height = int(input("Enter height of the grid (default 10): ") or 10)
        mines = int(input(f"Enter number of mines (default {max(10, width * height // 10)}): ") or max(10, width * height // 10))
        if mines >= width * height:
            print("Too many mines! Adjusting to maximum allowable.")
            mines = width * height - 1
        game = Minesweeper(width, height, mines)
        game.play()
    except ValueError:
        print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()

