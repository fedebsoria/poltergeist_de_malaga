"""This is the main folder which will start the game calling other functions"""

from resources import intro, levels

def main():

    game_status = intro.intro()

    if game_status == 0:
        levels.print_map_test('1')
    else:
        return -1
    
    return 0

if __name__ == "__main__":
    main()