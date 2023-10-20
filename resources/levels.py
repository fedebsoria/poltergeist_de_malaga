from . import auxiliars as aux
import random
import readchar
import os

LEVEL_1 = "./resources/levels_maps/level_1.txt"
LEVEL_2 = "./resources/levels_maps/level_2.txt"
LEVEL_3 = "./resources/levels_maps/level_3.txt"
POS_X = 1
POS_Y = 1

level = 1
my_position = [1, 1]
map_poltergeist = []

#This function reads a map stored in file and saves it in the var level
def level_file_read(n_level):
    if n_level == 1:
        aux.clean_screen()
        with open(LEVEL_1, 'r') as level_file:
            level = level_file.read()
    elif n_level == 2:
        aux.clean_screen()
        with open(LEVEL_2, 'r') as level_file:
            level = level_file.read() 
    elif n_level == 2:
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

def level_draw_and_controls(level, my_position, map_poltergeist):
    
    end_game = False
    battle = False
    change_map = 1
    max_poltergeist = 0;
    #create obstacle map
    obstacle_definition = level_file_read(level)
    obstacle_definition = [list(row) for row in obstacle_definition.split('\n')]

    MAP_WIDTH = len(obstacle_definition[0])
    MAP_HEIGHT = len(obstacle_definition)

    #map loop
    while end_game != True or change_map < change_map:
        if change_map == 1:
            max_poltergeist = 2
        elif change_map == 2:
            max_poltergeist = 3
        elif change_map == 3:
            max_poltergeist = 0

        #generate poltergeist in random
        while len(map_poltergeist) < max_poltergeist:
            new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

            if new_position not in map_poltergeist and new_position != my_position and\
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != '#' and\
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != '!':
                    map_poltergeist.append(new_position)
        
        for cordinate_y in range(MAP_HEIGHT):
            for cordinate_x in range(MAP_WIDTH):

                char_to_draw = "   "
                object_in_cell = None
                
                for map_object in map_poltergeist:
                    if map_object[POS_X] == cordinate_x and map_object[POS_Y == cordinate_y]:
                        char_to_draw = " & "
                        object_in_cell = map_object
                
                if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                    char_to_draw = " @ "

                    if object_in_cell:
                        map_poltergeist.remove(object_in_cell)
                        #starts the fight against the poltergeist
                        battle = True
                        #def batalla

                if obstacle_definition[cordinate_y][cordinate_x] == '#':
                    char_to_draw = "###"

                print("{}".format(char_to_draw, end=''))

        #character motion
        direction = readchar.readchar().encode().decode()
        new_position = None

        if direction == 'w':
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]
        elif direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]
        elif direction == "a":
            new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y] ]
        elif direction == "d":
            new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y] ]
        #end the loop
        elif direction == "q":
            break

        if new_position:
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != '#':
                my_position = new_position
        
        aux.clean_screen()

        #Here will go the battle
