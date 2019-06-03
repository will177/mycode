#!/usr/bin/python3
"""Author Will V | Learning GOTjson.py"""

# pull in json lib so we can parse out json
import json

def main():
    # open the johnsnow.json file in read mode
    with open ("jonsnow.json", "r") as gotdata:
        jonsnow = gotdata.read() # grab file as read only
        GOTpy = json.loads(jonsnow) # converts string to pythonic LISTs and DICTs
    print (GOTpy) #display the GOT data
    print (GOTpy["url"]) # display values assoc. With URL
    print (GOTpy["titles"][0]) # Display values associate with titles

        # create a loop to move across aliases
    with open("aliases.txt", "w") as jsaliases:
        for gotalias in GOTpy["aliases"]:
            print(gotalias, file=jsaliases)

    print (GOTpy["aliases"])

    
    # parse the jonsnow.json for ...
    # display the character name
    # display character alias /titles
    # display the API for ????
if __name__ == "__main__":
    main()

