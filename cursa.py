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
    stdscr.vline(0,0,"+",20)
    stdscr.vline(0,20,"+",20)
    stdscr.hline(0,0,"+", 20)
    stdscr.hline(19,0,"+", 20)

    text = ["Never", "gonna", "give ", "you  ", "up!  ", "     "]
    for i in text:
        stdscr.addstr(9, 9, i, RED_AND_BLACK)
        stdscr.refresh()
        time.sleep(1.5)
    
    stdscr.addstr(21,0, "Type your favorite 5-letter word: ")
    inputed_text = ["","","", "", ""]
    for i in range(5):
        inputed_text[i] = stdscr.getch(21, 35+i)
        stdscr.addch(21, 35+i, inputed_text[i])
        stdscr.refresh()

    counter_var = 0
    start_position = [3,2]
    for i in inputed_text:
        stdscr.addch(start_position[0], start_position[1]+counter_var, i, GREEN_AND_BLACK)
        stdscr.refresh()
        time.sleep(1)
        counter_var += 1

    time.sleep(3) # a bit waity waity

    #clearing and creating the field again
    stdscr.clear()
    stdscr.vline(0,0,"+",20)
    stdscr.vline(0,20,"+",20)
    stdscr.hline(0,0,"+", 20)
    stdscr.hline(19,0,"+", 20)
    stdscr.refresh()


    stdscr.getch()

wrapper(main)