import random as rand
import os, sys

from board import drawTop, loopTop
from resources import idMap
import deck

START_GOLD = 50
START_HAND = 2

def main():
    playerList = initgame()
    end = False
    while end == False:
        game(playerList)
        end = endOfGame(playerList)
    pointsCount(playerList)
    for p in playerList:
        print(p.name, p.points)

def initgame():
    # Verify terminal size
    termSize = os.get_terminal_size()
    if termSize[1] < 34 or termSize[0] < 140:
        sys.exit("Terminal too small")
    # Choose the number of players
    while True:
        try:
            nbPlayer = int(input("Quel nombre de joueurs ? : "))
            if nbPlayer > 7 or nbPlayer < 4:
                print("Merci de choisir un nombre compris entre 4 et 7")
            else:
                break
        except ValueError:
            print("Ceci n'est pas un nombre valide")
    
    # Initialize playerList, player treasure, player hand and the king
    playerList = []
    for i in range(nbPlayer):
        idMap[i + 41].gold = START_GOLD
        idMap[i + 41].hand = deck.draw(START_HAND)
        idMap[i + 41].city = deck.draw(6)
        playerList.append(idMap[i + 41])
    rand.choice(playerList).isking = True
    
    return playerList

def game(playerList):
    nbPlayer = len(playerList)
    # Clean player and find the king
    for p in playerList:
        p.character = None
        p.murdered = False
        p.stealed = False
        p.revealed = False
        if p.isking:
            j = playerList.index(p)

    # Discard characters based on number of players and return both discarded and non discarded
    discardList, charList = discardChar(nbPlayer)
    
    # Each player choose their character, beginning by the king
    for i in range(nbPlayer):
        drawTop(playerList, discardList, 0, j)
        # If i == 6 there is 7 player and this is the last player to choose so we add the character discarded face down to the choices
        if i == 6 : charList.append(discardList[0])
        playerList[j].current = True
        if not playerList[j].ai:
            charChoice = 0
            while charChoice == 0:
                charChoice = idMap[100].exe(playerList, charList)
                # Handle exploring the board during character selection
                if charChoice == 0: loopTop(playerList, discardList)
            playerList[j].character = charChoice
            idMap[101].updateName(idMap[charChoice].name)
            idMap[101].exe(playerList)
        charList.remove(charChoice)
        playerList[j].current = False
        # If j == nbPlayer we arrive at the end of the list so index 0 gets to choose next
        j += 1
        if j == nbPlayer:
            j = 0
    
    # Decide which player has to play based on the character they pick
    for i in range(51, 59):
        for p in playerList:
            if p.character == i:
                p.current = True
                AIturn(playerList, discardList) if p.ai else turn(playerList, discardList)
                p.current = False
        
    return playerList

# Discard a number of character cards based on the number of players, return a list with the face down at index 0 and the face up at index 1
def discardChar(nbPlayer):
    charList = list(range(51, 59))
    # Always discard one character face down
    discardList = [rand.choice(charList), [None, None, None, None]]
    charList.remove(discardList[0])
    # If 4 or 5 players, one discarded face up
    if nbPlayer <= 5:
    # King can't be discarded face up
        char = rand.choice(charList)
        while char == 54:
            char = rand.choice(charList)
        discardList[1][0] = char
        charList.remove(char)
    # If 4 players, one more discarded face up
    if nbPlayer <= 4:
    # King can't be discarded face up
        char = rand.choice(charList)
        while char == 54:
            char = rand.choice(charList)
        discardList[1][1] = char
        charList.remove(char)
    return discardList, charList

def turn(playerList, discardList):
    # Found the current player
    plIndex = 0
    for pl in playerList:
        if pl.current: break
        else: plIndex += 1
    # Cancel the turn if the player was murdered
    if pl.murdered:
        return
    # Reveal the character of the player
    pl.revealed = True
    # Set the buildLimit
    buildLimit = 3 if pl.character == 57 else 1
    # Set the new king if the king is revealed
    kingMessage  = []
    if pl.character == 54:
        for p in playerList:
            p.isking = False
        pl.isking = True
        kingMessage = [102]
    # Steal the player if he is stealed
    stealMessage = []
    if pl.stealed:
        for p in playerList:
            if p.character == 52:
                p.gold += pl.gold
                pl.gold = 0
                idMap[149].updateName(p.name)
                stealMessage = [149]
    # Create the list of possible actions
    actions = [110] + idMap[pl.character].actions
    obslib = [False, False]
    for d in pl.city:
        # If the player has the observatory
        if d == 20:
            obslib[0] = True
        # Action of the laboratory
        elif d == 21:
            actions += [180]
        # Action of the Smithy
        elif d == 22:
            actions += [185]
        # If the player has the Library
        elif d == 27:
            obslib[1] = True
    # Begin the turn
    drawTop(playerList, discardList, 0, plIndex)
    idMap[105].exe(playerList, kingMessage + stealMessage)
    while True:
        cho = idMap[109].exe(playerList, actions)

        # Gold of Draw
        if cho == 110:
            # Test for observatory and Library
            drawNb = 3 if obslib[0] else 2
            drawMsg = 113 if obslib[1] else 112
            idMap[drawMsg].updateName(drawNb)
            goldOrCard = idMap[111].exe(playerList, [114, drawMsg])
            # Gold
            if goldOrCard == 114:
                pl.gold += 2
                idMap[134].updateName(2)
                idMap[134].exe(playerList)
            # Draw with Library
            elif goldOrCard == 113:
                pl.hand.extend(deck.draw(drawNb))
            # Draw without Library
            elif goldOrCard == 112:
                dra = deck.draw(drawNb)
                drawChoice = idMap[115].exe(playerList, dra)
                pl.hand.append(drawChoice)
                dra.remove(drawChoice)
                deck.discard(dra)
            # If we don't escape the choice
            if goldOrCard != 0:
                actions.remove(110)
                actions.extend([120, 200])
        # Build district
        elif cho == 120:
            # HandSize = 0
            if len(pl.hand) == 0: idMap[151].exe(playerList)
            else:
                disChoice = idMap[121].exe(playerList, pl.hand)
                double = False
                for d in pl.city:
                    # District already in city
                    if disChoice == d: double = True
                if disChoice == 0: ""
                # Double in city
                elif double: idMap[122].exe(playerList)
                # Not Enough gold
                elif idMap[disChoice].cost > pl.gold: idMap[123].exe(playerList)
                # Build district
                else:
                    pl.city.append(disChoice)
                    pl.hand.remove(disChoice)
                    pl.gold -= idMap[disChoice].cost
                    idMap[124].updateName(idMap[disChoice].name, idMap[disChoice].cost)
                    idMap[124].exe(playerList)
                    # Laboratory and Smithy
                    if disChoice == 21: actions += [180]
                    if disChoice == 22: actions += [185]
                    # City finished
                    if len(pl.city) == 7: idMap[195].exe(playerList)
                    buildLimit -= 1
                    if buildLimit == 0: actions.remove(120)
        # Gold from district's color
        elif cho == 130 or cho == 131 or cho == 132 or cho == 133:
            gold = takeGold(pl)
            idMap[134].updateName(gold)
            idMap[134].exe(playerList)
            pl.gold += gold
            actions.remove(cho)
        # Assassin
        elif cho == 140:
            charChoices = list(range(52, 59))
            for char in discardList[1]:
                charChoices.remove(char) if char != None else ""
            charChoice = idMap[141].exe(playerList, charChoices)
            if charChoice != 0:
                for p in playerList:
                    if p.character == charChoice: p.murdered = True
                    discardList[1][2] = charChoice
                idMap[142].updateName(idMap[charChoice].name)
                idMap[142].exe(playerList)
                actions.remove(140)
        # Thief
        elif cho == 145:
            charChoices = list(range(53, 59))
            for char in discardList[1]:
                try: charChoices.remove(char)
                except: ""
            charChoice = idMap[146].exe(playerList, charChoices)
            if charChoice != 0:
                for p in playerList:
                    if p.character == charChoice: p.stealed = True
                    discardList[1][3] = charChoice
                idMap[147].updateName(idMap[charChoice].name)
                idMap[147].exe(playerList)
                actions.remove(145)
        # Magician1
        elif cho == 150:
            if len(pl.hand) == 0: idMap[151].exe(playerList)
            else:
                discarded = []
                while True:
                    idMap[153].updateName(len(discarded), len(discarded))
                    cardChoice = idMap[152].exe(playerList, pl.hand + [153] + discarded)
                    # Esc was pressed, return to actions of the turn, cancel discard
                    if cardChoice == 0:
                        for i in range(len(discarded)): discarded[i] *= -1
                        pl.hand.extend(discarded)
                        break
                    # Confirm power of the magician: discard cards and draw that many
                    elif cardChoice == 153:
                        dra = deck.draw(len(discarded))
                        pl.hand.extend(dra)
                        for i in range(len(discarded)): discarded[i] *= -1
                        deck.discard(discarded)
                        idMap[154].updateName(len(discarded))
                        idMap[154].exe(playerList, dra)
                        # Remove powers of the magician
                        actions.remove(150)
                        actions.remove(155)
                        break
                    # Hand from discard pile
                    elif cardChoice < 0:
                        discarded.remove(cardChoice)
                        cardChoice *= -1
                        pl.hand.extend([cardChoice])
                    # Discard pile from hand
                    else:
                        pl.hand.remove(cardChoice)
                        cardChoice *= -1
                        discarded.extend([cardChoice])
        # Magician2
        elif cho == 155:
            plaChoices = list(range(41, 41 + len(playerList)))
            plaChoices.remove(plIndex + 41)
            plaChoice = idMap[156].exe(playerList, plaChoices)
            if plaChoice != 0:
                pl.hand, playerList[plaChoice - 41].hand = playerList[plaChoice - 41].hand, pl.hand
                idMap[157].updateName(idMap[plaChoice].name)
                idMap[157].exe(playerList)
                actions.remove(150)
                actions.remove(155)
        # Merchant
        elif cho == 160:
            pl.gold += 1
            idMap[161].exe(playerList)
            actions.remove(160)
        # Architect
        elif cho == 165:
            dra = deck.draw(2)
            pl.hand.extend(dra)
            idMap[154].updateName(2)
            idMap[154].exe(playerList, dra)
            actions.remove(165)
        # Warlord
        elif cho == 170:
            plaChoice = idMap[171].exe(playerList, list(range(41, 41 + len(playerList))))
            plaIndex = plaChoice - 41
            # Esc pressed
            if plaChoice == 0: ""
            # Bishop
            elif playerList[plaIndex].character == 55: idMap[172].exe(playerList)
            # City finished
            elif len(playerList[plaIndex].city) >= 7: idMap[177].exe(playerList)
            else:
                while True:
                    disChoice = idMap[173].exe(playerList, playerList[plaIndex].city)
                    # Esc pressed
                    if disChoice == 0: break
                    else:
                        disCost = idMap[disChoice].cost - 1
                        # Great Wall
                        for d in playerList[plaIndex].city: 
                            if d == 28: disCost += 1
                    # "Keep" selected
                    if disChoice == 19: idMap[174].exe(playerList)
                    # Not enough gold
                    elif disCost > pl.gold: idMap[123].exe(playerList)
                    else:
                        pl.gold -= disCost
                        playerList[plaIndex].city.remove(disChoice)
                        idMap[178].updateName(idMap[disChoice].name, playerList[plaIndex].name)
                        idMap[178].exe(playerList)
                        actions.remove(170)
                        # Graveyard power
                        for p in playerList:
                            if not p.current:
                                for d in p.city:
                                    if d == 23 and p.gold >= 1:
                                        idMap[190].updateName(p.name[:-5], idMap[disChoice].name)
                                        cho = idMap[190].exe(playerList, [191, 192])
                                        if cho == 191:
                                            p.gold -= 1
                                            p.hand.append(disChoice)
                                            idMap[193].exe(playerList)
                        break
        # Laboratory
        elif cho == 180:
            # Handsize = 0
            if len(pl.hand) == 0: idMap[151].exe(playerList)
            else:
                cardChoice = idMap[181].exe(playerList, pl.hand)
                if cardChoice != 0:
                    pl.hand.remove(cardChoice)
                    deck.discard([cardChoice])
                    idMap[182].updateName(idMap[cardChoice].name)
                    idMap[182].exe(playerList)
                    actions.remove(180)
        # Smithy
        elif cho == 185:
            # Not enough gold
            if pl.gold < 2:idMap[123].exe(playerList)
            else:
                dra = deck.draw(3)
                pl.hand.extend(dra)
                idMap[154].updateName(3)
                idMap[154].exe(playerList, dra)
                actions.remove(185)
        # Endturn
        elif cho == 200:
            idMap[201].exe(playerList)
            return
        # Explore board
        elif cho == 0:
            loopTop(playerList, discardList)
        
        drawTop(playerList, discardList, 0, plIndex)
    return

def takeGold(pl):
    gold = 0
    for d in pl.city:
        if idMap[d].color == idMap[pl.character].color or d == 26: gold += 1
    return gold

def endOfGame(playerList):
    for p in playerList:
        if len(p.city) >= 7:
            return True
    return False

def pointsCount(playerList):
    # Count points for who finished first and who finished
    isFirst = True
    for i in range(1, 9):
        for p in playerList:
            if idMap[p.character].number == i and len(p.city) >= 7 and isFirst:
                p.points += 4
                isFirst = False
            elif idMap[p.character].number == i and len(p.city) >= 7:
                p.points += 2
    # Count points for total cost of city + colors + purple districts
    for p in playerList:
        colors = []
        for d in p.city:
            # Costs
            p.points += idMap[d].cost
            # Purple
            if d == 24: p.points += p.gold
            if d == 25: p.points += len(p.hand)
            if d == 29 or d == 30: p.points += 2
            # Colors
            if d == 18: colors.append("hauntedCity")
            elif idMap[d].color not in colors: colors.append(idMap[d].color)
        if len(colors) >= 5: p.points += 3 
    return playerList

if __name__ == "__main__":
    main()
