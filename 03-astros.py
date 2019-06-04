#!/usr/bin/python3
""" Author: Will V | learning about api """


import json
import urllib.request

MAJORTOM = "http://api.open-notify.org/astros.json"

def main ():
    # make request
    resp = urllib.request.urlopen(MAJORTOM)
    #print(dir(resp)) returns the methods to our resp object
    # make python strip json  data FROM the 200 response
    jstring = resp.read()
    # convert string data to JSON
    #print(jstring)
    #print(type(jstring))
    #print(dir(jstring))
    pyj = json.loads(jstring.decode('utf-8'))

    # Parse out json we stripped off response
    astrocosmo = pyj.get("people")
    print("CURRENTLY IN SPACE:") 
    for spaceperson in astrocosmo:
        print(spaceperson["name"])
     
    # display selected data on screen - names of people in space
if __name__ == "__main__":
    main()
