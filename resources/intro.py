import readchar

INTRO_ART = "./resources/art/intro.txt"

def intro():
    start_game = ""

    """ open the file with the intro art """
    with open(INTRO_ART, 'r') as level_art:
        main_intro = level_art.read()

    """ waits until the user press 'enter' """
    while (start_game != '\r'):
        print(main_intro)
        start_game = readchar.readkey()
    return  1
