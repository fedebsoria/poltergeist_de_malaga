import readchar

def intro():
    start_game = ""

    print(start_game)  #\r is enter
    while (start_game != '\r'):
        print("TITULO\n")
        print("\n--ENTER--\n")
        start_game = readchar.readkey()
    return  0
