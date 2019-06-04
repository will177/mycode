#!/usr/bin/python3
""" Author: Will V | learning about api """

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main ():
    try:
        # make request
        resp = requests.get(MAJORTOM)
        # pyj = requests.get(MAJORTOM).json() this can save more lines

        pyj = resp.json() 

        # Parse out json we stripped off response
        astrocosmo = pyj.get("people")
        
        # display selected data on screen - names of people in space
        print("CURRENTLY IN SPACE:") 
        for spaceperson in astrocosmo:
            print(spaceperson["name"])
    except:
        print("API is unavailable at the moment")
        exit()
if __name__ == "__main__":
    main()
