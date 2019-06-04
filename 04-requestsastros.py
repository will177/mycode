#!/usr/bin/python3
""" Author: Will V | learning about api """

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main ():
    # make request
    resp = requests.get(MAJORTOM)

    pyj = resp.json() 

    # Parse out json we stripped off response
    astrocosmo = pyj.get("people")
    print("CURRENTLY IN SPACE:") 
    for spaceperson in astrocosmo:
        print(spaceperson["name"])
     
    # display selected data on screen - names of people in space
if __name__ == "__main__":
    main()
