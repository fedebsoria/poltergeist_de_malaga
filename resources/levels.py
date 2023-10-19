from . import auxiliars as aux

LEVEL_1 = "./resources/levels_maps/level_1.txt"
LEVEL_2 = "./resources/levels_maps/level_2.txt"
LEVEL_3 = "./resources/levels_maps/level_3.txt"

level = 0

#This function reads a map stored in file and saves it in the var level
def level_file_read(n_level):
    if n_level == '1':
        aux.clean_screen()
        with open(LEVEL_1, 'r') as level_file:
            level = level_file.read()
    elif n_level == '2':
        aux.clean_screen()
        with open(LEVEL_2, 'r') as level_file:
            level = level_file.read() 
    elif n_level == '3':
        aux.clean_screen()
        with open(LEVEL_3, 'r') as level_file:
            level = level_file.read()
    else:
        return -1
    return level

#this function was made to test the reading function
def print_map_test(n_level):
    
    actual_map = level_file_read(n_level)

    print (actual_map)
