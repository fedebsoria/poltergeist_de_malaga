"""This is the main folder which will start the game calling other functions"""
#from resources import intro, level_file_reader, level_printer_and_game
from resources import intro, level_file_reader,level_printer_and_game, fight_event


def main():
    intro.intro()
    level =  1;
    map_load = level_file_reader.level_file_read(level)
    level_printer_and_game.handle_map(map_load)

if __name__ == "__main__":
    main()