#!/usr/bin/env python3

#Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
RPM GAME
========
Commands:
    go [direction]
    get [item]
''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the  ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['items'])
    print("--------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

        'Hall' : {
            'south' : 'Kitchen'
            },
        'Kitchen' : {
            'north' : 'Hall'
            }
        }
#Start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

    showStatus()
    #get the plyers's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east; would give the list:
    #['go','east']
    move = '';
    while move == '':
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed whenever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room



