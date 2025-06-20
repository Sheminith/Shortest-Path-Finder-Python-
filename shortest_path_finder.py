import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for row_idx, row_val in enumerate(maze):
        for col_idx, col_val in enumerate(row_val):
            if (row_idx, col_idx) in path:
                stdscr.addstr(row_idx, col_idx*2, "X", RED) #multiply the row and col to create more space
            else:
                stdscr.addstr(row_idx, col_idx*2, col_val, BLUE) #multiply the row and col to create more space

def find_start(maze, start):
    for row_idx, row_val in enumerate(maze):
        for col_idx, col_val in enumerate(row_val):
            if col_val == start:
                return row_idx, col_idx
            
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos])) #current position, new_path

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2) # to slower the visuals
        stdscr.refresh()
        
        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0: #UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): #DOWN
        neighbors.append((row + 1, col))
    if col > 0: #LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

def main(stdscr):
    # create a color pair
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) #id, foreground, background
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # blue_and_black = curses.color_pair(1)

    # Add hello world text
    # stdscr.clear()
    # stdscr.addstr(0, 0, "Hello world!", blue_and_black) #row, column, text, color_pair
    # stdscr.refresh()
    # stdscr.getch()

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)