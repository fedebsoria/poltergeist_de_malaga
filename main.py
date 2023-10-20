"""This is the main folder which will start the game calling other functions"""

from resources import intro, levels

def main():

    level = 1
    my_position = [1, 1]
    map_poltergeist = []

    game_status = intro.intro()

    if game_status == 1:
        levels.level_draw_and_controls(level, my_position, map_poltergeist)
    else:
        return -1
    
    return 0

if __name__ == "__main__":
    main()