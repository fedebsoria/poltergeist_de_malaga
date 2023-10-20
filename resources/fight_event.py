from . import auxiliars as aux

def fight(stdscr):
    # Clear the screen
    stdscr.clear()

    # Display the fight event
    stdscr.addstr(0, 0, "Fight Event: Press 'q' to exit the fight.")

    # Implement the fight logic here
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break