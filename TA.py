import curses
from curses import wrapper
import time

def main(stdscr):
# Suggested code may be subject to a license. Learn more: ~LicenseLog:4041265646.
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3727030753.
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    RED_FONT = curses.color_pair(1)
    GREEN_FONT = curses.color_pair(2)

    c = 15 
    t = 0.2

    for f in range(2*c):
        stdscr.addch(0,f,"+")
        stdscr.refresh()
        time.sleep(t)
    
    for f in range(c):
        stdscr.addch(f,0,"+")
        stdscr.refresh()
        time.sleep(t)
    
    for f in range(c):
        stdscr.addch(f,2*c-1,"+")
        stdscr.refresh()
        time.sleep(t)

    for f in range(2*c):
        stdscr.addch(c,f,"+")
        stdscr.refresh()
        time.sleep(t)

    current_ch = "f"
    current_ch_is_not_space = True
    Question = "blabla"
    stdscr.addstr(16,2,Question,GREEN_FONT)
    pos = 3
    while current_ch_is_not_space:
        current_ch = stdscr.getch(16,pos+len(Question))
        stdscr.addch(16,pos+len(Question),current_ch)
        pos += 1
        stdscr.refresh()
        current_ch_is_not_space = len(current_ch) != 32

    stdscr.getch(16,2)


wrapper(main)    