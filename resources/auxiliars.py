import os
#cleans the terminal window
def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")