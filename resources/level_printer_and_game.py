import curses 

def fight_event(stdscr):
    # Clear the screen
    stdscr.clear()

    # Display the fight event
    stdscr.addstr(0, 0, "Fight Event: Press 'q' to exit the fight.")

    # Implement the fight logic here
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

def find_enemies(map_rows):
    enemies = []
    for y in range(1, len(map_rows) - 1):
        for x in range(1, len(map_rows[0]) - 1):
            if map_rows[y][x] == '&':
                enemies.append((y, x))
    return enemies

def move_enemy_towards_player(enemies, player_y, player_x, map_rows):
    for i in range(len(enemies)):
        enemy_y, enemy_x = enemies[i]
        if enemy_y < player_y:
            map_rows[enemy_y] = map_rows[enemy_y][:enemy_x] + ' ' + map_rows[enemy_y][enemy_x + 1:]
            enemy_y += 1
        elif enemy_y > player_y:
            map_rows[enemy_y] = map_rows[enemy_y][:enemy_x] + ' ' + map_rows[enemy_y][enemy_x + 1:]
            enemy_y -= 1
        if enemy_x < player_x:
            map_rows[enemy_y] = map_rows[enemy_y][:enemy_x] + ' ' + map_rows[enemy_y][enemy_x + 1:]
            map_rows[enemy_y] = map_rows[enemy_y][:enemy_x + 1] + '&' + map_rows[enemy_y][enemy_x + 2:]
            enemy_x += 1
        elif enemy_x > player_x:
            map_rows[enemy_y] = map_rows[enemy_y][:enemy_x] + ' ' + map_rows[enemy_y][enemy_x + 1:]
            map_rows[enemy_y] = map_rows[enemy_y][:enemy_x - 1] + '&' + map_rows[enemy_y][enemy_x:]
            enemy_x -= 1
        enemies[i] = (enemy_y, enemy_x)

def handle_map(map_data):
    # Split the map into rows
    map_rows = map_data.split('\n')

    # Initialize the user's position
    y = 1
    x = 1

    # Initialize curses
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)

    # Find the '&' characters in the map
    enemies = find_enemies(map_rows)

    while True:
        # Display the map
        for i, row in enumerate(map_rows):
            if i == y:
                stdscr.addstr(i, 0, row[:x] + '@' + row[x + 1:])
            else:
                stdscr.addstr(i, 0, row)
        
        # Check for collision between '&' characters and the player
        for enemy_y, enemy_x in enemies:
            if enemy_y == y and enemy_x == x:
                stdscr.addstr(i + 1, 0, "Fight event triggered!")
                stdscr.refresh()
                # Implement the 'fight' event here
                curses.endwin()  # End curses for map
                curses.wrapper(fight_event)  # Start the fight event
                stdscr = curses.initscr()  # Initialize curses for map again
        
        # Move the '&' characters towards the player
        move_enemy_towards_player(enemies, y, x, map_rows)
        
        for enemy_y, enemy_x in enemies:
            stdscr.addstr(enemy_y, enemy_x, '&')

        stdscr.refresh()

        # Check for events at the user's current position
        current_char = map_rows[y][x]
        if current_char == '!':
            stdscr.addstr(i + 1, 0, "Item grabbed event triggered!")
            # Implement the 'item_grabbed' event here
        stdscr.refresh()

        # Get user input
        move = stdscr.getch()
        if move == ord('q'):
            break
        elif move == ord('w') and map_rows[y - 1][x] != '#':
            map_rows[y] = map_rows[y][:x] + ' ' + map_rows[y][x + 1:]
            y -= 1
        elif move == ord('a') and map_rows[y][x - 1] != '#':
            x -= 1
        elif move == ord('s') and map_rows[y + 1][x] != '#':
            map_rows[y] = map_rows[y][:x] + ' ' + map_rows[y][x + 1:]
            y += 1
        elif move == ord('d') and map_rows[y][x + 1] != '#':
            x += 1

    # Clean up curses
    curses.endwin()



