import os
from termcolor import colored
import keyboard
from time import sleep

from resources import idMap

# Size of terminal
termSize = os.get_terminal_size()

def drawTop(playerList, discardList, line=-1, column=-1):
    nbPlayer = len(playerList)
    # Create the pointer to highlight an item of the board
    pointer = []
    for i in range(11):
        pointer.append([[]] * nbPlayer)
    if line >= 0 and line <= 11 and column >=0 and column <= nbPlayer - 1:
        pointer[line][column] = ["reverse"]
 
    # Use a number of blank space calculated from the terminal size to center the board
    screen = [" " * int(((termSize[0] - (20 * nbPlayer)) / 2))] * (termSize[1] - 2)
    for i in range(1, 9):
        screen[i] = " " * int((termSize[0] - 116) / 2)
    screen[1] += "   █████████  █████ ███████████   █████████   ██████████   ██████████ █████       █████       ██████████  █████████ "
    screen[2] += "  ███░░░░░███░░███ ░█░░░███░░░█  ███░░░░░███ ░░███░░░░███ ░░███░░░░░█░░███       ░░███       ░░███░░░░░█ ███░░░░░███"
    screen[3] += " ███     ░░░  ░███ ░   ░███  ░  ░███    ░███  ░███   ░░███ ░███  █ ░  ░███        ░███        ░███  █ ░ ░███    ░░░ "
    screen[4] += "░███          ░███     ░███     ░███████████  ░███    ░███ ░██████    ░███        ░███        ░██████   ░░█████████ "
    screen[5] += "░███          ░███     ░███     ░███░░░░░███  ░███    ░███ ░███░░█    ░███        ░███        ░███░░█    ░░░░░░░░███"
    screen[6] += "░░███     ███ ░███     ░███     ░███    ░███  ░███    ███  ░███ ░   █ ░███      █ ░███      █ ░███ ░   █ ███    ░███"
    screen[7] += " ░░█████████  █████    █████    █████   █████ ██████████   ██████████ ███████████ ███████████ ██████████░░█████████ "
    screen[8] += "  ░░░░░░░░░  ░░░░░    ░░░░░    ░░░░░   ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░  ░░░░░░░░░  "
    screen[9]  += ("┌" + ("─" * 19 + "┬") * nbPlayer)[:-1] + "┐"
    screen[10] += "│"
    screen[11] += ("├" + ("─" * 19 + "┼") * nbPlayer)[:-1] + "┤"
    screen[12] += "│"
    screen[13] += ("├" + ("─" * 19 + "┼") * nbPlayer)[:-1] + "┤"
    screen[14] += "│"
    screen[15] += "│"
    screen[16] += ("├" + ("─" * 19 + "┼") * nbPlayer)[:-1] + "┤"
    screen[17] += "│"
    screen[18] += "│"
    screen[19] += "│"
    screen[20] += "│"
    screen[21] += "│"
    screen[22] += "│"
    screen[23] += "│"
    screen[24] += "│"
    screen[25] += "│"
    screen[26] += ("└" + ("─" * 19 + "┴") * nbPlayer)[:-1] + "┘"

    # Add players and city to screen
    for j in range(nbPlayer):
        pl = playerList[j]
        # Handle the name of the player
        if pl.isking:
            name = colored(" " + playerList[j].name[:-5] + colored(" Roi ", "yellow") + " ", attrs=pointer[0][j])
        else:
            name = colored(" " + playerList[j].name + " ", attrs=pointer[0][j])
        # Handle the character card of the player
        char = playerList[j].character
        if char == None:
            char = "                   "
        elif playerList[j].revealed == False:
            char = " xxxxxxxxxxxxxxxxx "
        else:
            char = " " + idMap[char].name + " "
        char = colored(char, attrs=pointer[1][j])
        # Handle number of cards in hand and gold of the player
        handsize = len(playerList[j].hand)
        if handsize > 9:
            handsize = str(handsize) + " cartes en main  "
        elif handsize > 1:
            handsize = str(handsize) + " cartes en main   "
        else:
            handsize = str(handsize) + " carte en main    "
        # Handle gold of the player
        gold = playerList[j].gold
        if gold > 9:
            gold = str(gold) + " pièces d'or     "
        elif gold > 1:
            gold = str(gold) + " pièces d'or      "
        else:
            gold = str(gold) + " pièce d'or       "
        # Add name, handsize and gold to the screen
        screen[10] += name + "│"
        screen[12] += char + "│"
        screen[14] += handsize + "│"
        screen[15] += gold + "│"
        # Add the city of the player to the screen
        for i in range(9):
            try:
                di = playerList[j].city[i]
                di = colored(str(idMap[di].cost) + " " + idMap[di].name, attrs=pointer[i + 2][j])
            except IndexError:
                di = colored("                   ", attrs=pointer[i + 2][j])
            screen[17 + i] += di + "│"
    # Add the discard list to the screen
    screen[27] += "Personnages défaussés :" + " " + " xxxxxxxxxxxxxxxxx " 
    try: 
        screen[27] += " " + idMap[discardList[1][0]].name
        screen[27] += " " + idMap[discardList[1][1]].name
    except: ""
    # Add the murdered character to the screen
    try: screen[28] += "Personnage assassiné:  " + idMap[discardList[1][2]].name
    except: ""
    # Add the stealed character to the screen
    try: screen[29] += "Personnage volé:       " + idMap[discardList[1][3]].name
    except: ""
    
    # Description of the pointed element
    if line == 0:
        screen[termSize[1] - 13] += playerList[column].name
        screen[termSize[1] - 12] += "est une IA" if playerList[column].ai else "est un vrai joueur" 
        if playerList[column].isking: screen[termSize[1] - 11] += "est le Roi"
    elif line == 1:
        if playerList[column].revealed: 
            screen[termSize[1] - 13] += idMap[playerList[column].character].name
            screen[termSize[1] - 12] += "Effet:"
            screen[termSize[1] - 11] += idMap[playerList[column].character].effect[0]
            screen[termSize[1] - 10] += idMap[playerList[column].character].effect[1]
            screen[termSize[1] - 9]  += idMap[playerList[column].character].effect[2]
        elif playerList[column].character == None:
            screen[termSize[1] - 13] += "Ce joueur n'a pas encore choisi de personnage"
        else:
            screen[termSize[1] - 13] += "Le personnage de ce joueur n'a pas encore été révélé."
    elif line >= 2:
        try:
            screen[termSize[1] - 13] += idMap[playerList[column].city[line - 2]].name
            screen[termSize[1] - 12] += f"Coût de construction: {idMap[playerList[column].city[line - 2]].cost}"
            screen[termSize[1] - 11] += "Effet:"
            screen[termSize[1] - 10] += idMap[playerList[column].city[line - 2]].effect[0]
            screen[termSize[1] - 9]  += idMap[playerList[column].city[line - 2]].effect[1]
            screen[termSize[1] - 8]  += idMap[playerList[column].city[line - 2]].effect[2]
        except: ""

    clearAll()
    # Handle terminal too small
    if termSize[1] < 42:
        screen = screen[9:]
    for s in screen:
        print(s)


def drawBottom(itemString, playerList, choiceList):
    for pl in playerList:
        if pl.current: break
    try:
        line = pointer.index(["reverse"])
    except:
        line = 0
    screen = [""] * 13
    # Add bottom line to screen
    screen[0] = "─" * 59 + "┬" + "─" * (termSize[0] - 140) + "┬" + "─" * 19 + "┬" + "─" * 59 
    if len(pl.hand) > 9:
        handSize = str(len(pl.hand)) + " cartes en main: "
    elif len(pl.hand) < 1:
        handSize = str(len(pl.hand)) + " carte en main:   "
    else:
        handSize = str(len(pl.hand)) + " cartes en main:  "
    screen[1] += " " + itemString + "│" + " " * (termSize[0] - 140) + "│" + handSize + "│"
    for i in range(11):
    # Draw the choice list
        try:
            screen[i + 2] += colored(" " + idMap[abs(choiceList[i])].name , attrs=pointer[i])
            if choiceList[i] < 100:
                try: 
                    screen[i + 2] += " " + colored(" " + idMap[abs(choiceList[i + 11])].name , attrs=pointer[i]) + " "
                except:
                    screen[i + 2] += "                                         "
            else :
                screen[i + 2] += ""
            screen[i + 2] += "│" + " " * (termSize[0] - 140)  + "│"
        except:
            screen[i + 2] += "                                                           │" + " " * (termSize[0] - 140)  + "│"
    # Draw the hand
        try:
            screen[i + 2] += str(idMap[pl.hand[i]].cost) + " " + idMap[pl.hand[i]].name + "│"
        except:
            screen[i + 2] += "                   │"
    # Draw the effect of a district card
    try:
        if choiceList[line] < 40:
            screen[1] += " " + idMap[choiceList[line]].name
            screen[2] += f" Coût de construction {idMap[choiceList[line]].cost}:"
            screen[4] += " " + idMap[choiceList[line]].effect[0]
            screen[5] += " " + idMap[choiceList[line]].effect[1]
            screen[6] += " " + idMap[choiceList[line]].effect[2]
        # Draw the properties of a player
        elif choiceList[line] < 50:
            screen[1] += " " + idMap[choiceList[line]].name
            screen[2] += " " + idMap[choiceList[line]].gold
        # Draw the effect of a character card
        elif choiceList[line] < 60:
            screen[1] += " " + idMap[choiceList[line]].name
            screen[3] += " " + idMap[choiceList[line]].effect[0]
            screen[4] += " " + idMap[choiceList[line]].effect[1]
            screen[5] += " " + idMap[choiceList[line]].effect[2]
    except: ""
    # Print the bottom of the screen
    clearBottom()
    for string in screen:
        print(string)
    
def loopTop(playerList, discardList, line=0, column=0):
    nbPlayer = len(playerList)
    while True:
        drawTop(playerList, discardList, line, column)
        sleep(.2)
        key = keyboard.read_key()
        if key == "down" and line != 10:
            line += 1
        elif key == "up" and line != 0:
            line -= 1
        elif key == "right" and column != nbPlayer - 1:
            column += 1
        elif key == "left" and column != 0:
            column -= 1
        elif key == "enter":
            print("\033[1A", end="")
            return line, column
        elif key == "esc":
            return -1, -1
    
def loopBottom(itemString, playerList, choiceList, noEsc=False):
    nbLine = len(choiceList)
    global pointer
    pointer = [[]] * nbLine
    line = 0
    while True:
        pointer[line] = ["reverse"]
        drawBottom(itemString, playerList, choiceList)
        pointer[line] = []
        sleep(.2)
        key = keyboard.read_key()
        if key == "down" and line != nbLine - 1:
            line += 1
        elif key == "up" and line != 0:
            line -= 1
        elif key == "enter":
            print("\033[1A", end="")
            return choiceList[line]
        elif key == "esc" and noEsc == False:
            return 0

def bottomAssent(itemString, playerList, choiceList):
    drawBottom(itemString, playerList, choiceList)
    sleep(.2)
    key = keyboard.read_key()
    if key == "enter":
        print("\033[1A", end="")

def clearAll():
    os.system("clear")

def clearBottom():
    for i in range(13):
        print("\x1b[2K", end="")
        print("\033[1A", end="")
    print("\r\x1b[2K", end="")

