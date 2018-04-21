from curses import wrapper
import curses
from time import sleep


def main(stdscr):
    curses.noecho()
    #stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    #for i in range(0, 11):
    #    v = i-10
    #    stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, v))



    for i in range(10, 40):
        #stdscr.erase()
        stdscr.addch(i, i, 'A')
        sleep(0.1)
        stdscr.refresh()

    # Press any key to stop
    stdscr.getkey()

wrapper(main)