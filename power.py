import board

def power(actionType, itemString, choiceList):
    functionMap = {
                  "question": question(itemString, choiceList),
                  "questionNoEsc": questionNoEsc(itemString, choiceList),
                  "choice"  : choice(itemString, choiceList),
                  "assent"  : assent(itemString, choiceList)
                  }
    return functionMap[actionType]

def question(itemString, choiceList):
    return board.loopBottom(itemString, choiceList)

def questionNoEsc(itemString, choiceList):
    return board.loopBottomNoEsc(itemString, choiceList)

def assent(itemString, choiceList):
    return board.drawBottom(itemString, choiceList)
    
def choice(itemString, choiceList):
    # Will never be call
    return

def districtsGold(itemString, choiceList):
    gold = 0
    from main import playerList
    for p in playerList:
        if p.current:
            break
    for d in p.city:
        if idMap[d].color == p.character.color or d == 26: gold += 1
    return gold

