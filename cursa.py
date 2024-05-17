import curses # imports curses module, that let's us manipulate the terminal
from curses import wrapper
import time 



def main(stdscr):
    #initalise colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_YELLOW)

    # put colors into varieble
    RED_AND_BLACK = curses.color_pair(1)
    WHITE_AND_BLACK = curses.color_pair(2)
    GREEN_AND_BLACK = curses.color_pair(3)
    WHITE_AND_YELLOW = curses.color_pair(4)
    stdscr.clear()
    #stdscr.refresh()
    # making a field
    for f in range( 20):
       stdscr.addstr(f, 0, "+")
       stdscr.addstr(f, 19, "+")
       stdscr.addstr(0, f, "+")
       stdscr.addstr(20, f, "+")
    stdscr.refresh()

    

    stdscr.getch()

wrapper(main)