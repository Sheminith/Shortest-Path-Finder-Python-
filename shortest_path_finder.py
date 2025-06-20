import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def main(stdscr):
    # create a color pair
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) #id, foreground, background
    blue_and_black = curses.color_pair(1)

    # Add hello world text
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello world!", blue_and_black) #row, column, text, color_pair
    stdscr.refresh()
    stdscr.getch()

wrapper(main)