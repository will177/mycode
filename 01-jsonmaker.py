#!/usr/bin/python3
"""Author: Will V | Email: will177@gmail.com | learning json with python"""

# Python has no json support

import json

def main ():
    videogames = [{"game1": "red dead redemption", "game2": "Witcher", "game3": "Starcraft", "game4": "faster than light"}, {"game1": "paperboy", "game2": "donkey kong"}]

    # show the values of video games
    print(videogames)

    # create a local file

    with open("videogames.json", "w") as vidfile:
        json.dump(videogames, vidfile)


main()

