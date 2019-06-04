#!/usr/bin/python3
""" Author Will V || learning about NSA APIs and dev keys """

import requests
import pprint
MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def keyharvester():
    with open ("/home/student/nasa.key", "r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')


def main():
    # harvest our key from /home/student/nasa.key
    nasakey = keyharvester()


    # append our key to MYAPI

    # call the API (request.get()) and pull off json (.json())
    resp = requests.get(MYAPI + nasakey)
    asteroidz = resp.json()

    # Parse json - 
    #pprint.pprint(asteroidz["near_earth_objects"])
    for bigrock in asteroidz["near_earth_objects"]:
        print(bigrock)
        print()

    # pull json off response

    # decode json - loop across "near_earth_objects" to reveal astroids

    # only display those that may pose a danger to Zach having a good weekend
if __name__ == "__main__":
    main()
