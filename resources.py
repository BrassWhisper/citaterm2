from termcolor import colored

import board

# Districts
class district:
    def __init__(self, name, cost, color, effect):
        self.name = name
        self.cost = cost
        self.color = color
        self.effect = effect

tavern           = district(colored("Taverne          ", "green"  ), 1, "green",
                                    ["L'âtre est toujours chaud dans l'un des commerces les plus", 
                                     "animé de la ville mais c'est le soir quand les ménestrels", 
                                     "content leurs histoires que l'ambiance est à son apogée."])
tradingPost      = district(colored("Échoppe          ", "green"  ), 2, "green",
                                    ["Un magasin de première nécessité au pieds des habitations.", 
                                     "Avec ce dernier, les riverains s'assurent de ne manquer de", 
                                     "rien, la diversité des produits y est garantie."])
market           = district(colored("Marché           ", "green"  ), 2, "green",
                                    ["Les vendeurs arrivent tôt le matin sur la place pour", 
                                     "dresser leur stand et c'est un rendez-vous immanquable", 
                                     "pour les citadins qui y viennent presque tous les jours."])
docks            = district(colored("Comptoir         ", "green"  ), 3, "green",
                                    ["Dans ce bâtiment les marchands discutent les taxes sur", 
                                     "leurs produits avec l'administration locale. C'est", 
                                     "pourquoi ceux qui font fortune sont bons négociateurs."])
harbor           = district(colored("Port             ", "green"  ), 4, "green",
                                    ["Un défilé ininterrompu de caravelles et de galions, tous", 
                                     "chargés de produits exotiques et luxueux. Soie et épices", 
                                     "sont déchargées ici à destination du reste du royaume."])
townHall         = district(colored("Hôtel de Ville   ", "green"  ), 5, "green",
                                    ["Le haut-lieu des décisions politiques et commerçantes de", 
                                     "la ville. Dans ces bureaux se négocient des sommes à faire", 
                                     "pâlir les nobles, rougir les clercs et rager la plèbe."])
temple           = district(colored("Temple           ", "blue"   ), 1, "blue",
                                    ["Dans une salle quelques bougies et un autel. Voilà de quoi", 
                                     "rendre mystique un lieu assez banal au premier abord mais", 
                                     "qui renferme plus de pouvoir que bien des châteaux."])
church           = district(colored("Église           ", "blue"   ), 2, "blue",
                                    ["La mémoire du village commence avec la construction de ce", 
                                     "modeste édifice. Tous les prétextes sont bons pour s'y", 
                                     "rassembler, dans la joie comme dans la tristesse."])
monastery        = district(colored("Monastère        ", "blue"   ), 3, "blue",
                                    ["Derrière ces murs le silence du grattement du papier et", 
                                     "des capes qui frottent le sol. L'esprit des moines est", 
                                     "aussi impénétrable qu'ils restent muets."])
cathedral        = district(colored("Cathédrale       ", "blue"   ), 5, "blue",
                                    ["La magnificence du divin dans ce qu'elle a de plus beau et", 
                                     "de plus aliénant. Parcourez la nef et sentez peser sur", 
                                     "vous le regard du Très-Haut."])
watchtower       = district(colored("Tour de Guet     ", "red"    ), 1, "red",
                                    ["Une modeste tour aux portes du royaume. Les gardes", 
                                     "qui sont envoyés là-bas voient cela comme une punition,", 
                                     "les frontières sont paisible la plupart du temps."])
prison           = district(colored("Prison           ", "red"    ), 2, "red",
                                    ["Ne prétez pas trop attention aux cris d'agonie qui", 
                                     "s'échappent des fenêtres barrées. La moindre écoute de ces", 
                                     "râles vous fera frémir de terreur."])
battlefield      = district(colored("Caserne          ", "red"    ), 3, "red",
                                    ["Un camp d'entrainement somme toute assez banal. Tous les", 
                                     "soldats du royaume sont passés sous la direction de ces", 
                                     "instructeurs sévères."])
fortress         = district(colored("Forteresse       ", "red"    ), 5, "red",
                                    ["La puissance et la technologie militaire à leur apogée.", 
                                     "Les murs hauts dissuadent toute attaque frontale et la", 
                                     "surveillance sans faille écarte les meilleurs espions."])
manor            = district(colored("Manoir           ", "yellow" ), 3, "yellow",
                                    ["Une résidence de choix au mileu de bois", 
                                     "giboyeux. Ce prestigieux domaine se transmet", 
                                     "de générations en générations"])
castle           = district(colored("Château          ", "yellow" ), 4, "yellow",
                                    ["Cet édfice massif surplombe toute la région. Les ennemis", 
                                     "du royaume comme ses habitant se sentent souvent écrasés", 
                                     "par la puissance qui en émane."])
palace           = district(colored("Palais           ", "yellow" ), 5, "yellow",
                                    ["Les richesses amassées dans tout le royaume sont réunies", 
                                     "dans ce majestueux palace. Les réceptions fréquentes", 
                                     "rassemblent parfois les dirigeants des pays voisins"])
hauntedCity      = district(colored("Cour des Miracles", "magenta"), 2, "magenta",
                                    ["Pour le calcul du score, la Cour des Miracles est", 
                                     "considérée comme un quartier de la couleur de votre choix.",
                                     ""])
keep             = district(colored("Donjon           ", "magenta"), 3, "magenta",
                                    ["Le Donjon ne peut pas être détruit par le Condottiere.",
                                     "",
                                     ""])
observatory      = district(colored("Observatoire     ", "magenta"), 4, "magenta",
                                    ["Si vous choississez de piocher des cartes au début de", 
                                     "votre tour, piochez en 3 au lieu de 2. Choisissez-en une", 
                                     "et défaussez les 2 autres."])
laboratory       = district(colored("Laboratoire      ", "magenta"), 5, "magenta",
                                    ["Une fois par tour, vous pouvez défausser 1 carte et", 
                                     "recevoir 2 pièces d'or.",
                                     ""])
smithy           = district(colored("Forge            ", "magenta"), 5, "magenta",
                                    ["Une fois par tour, vous pouvez payer 2 pièces d'or pour",
                                     "piocher 3 cartes.",
                                     ""])
graveyard        = district(colored("Cimetière        ", "magenta"), 5, "magenta",
                                    ["Lorsque le Condottiere détruit un quartier, vous pouvez", 
                                     "payer 1 pièce d'or pour le prendre dans votre main. Vous",
                                     "ne pouvez pas le faire si vous êtes vous-même Condottiere"])
imperialTreasure = district(colored("Trésor Impérial  ", "magenta"), 5, "magenta",
                                    ["A la fin de la partie, marquez 1 point supplémentaire", 
                                     "pour chaque pièce d'or dans votre trésor.",
                                     ""])
mapRoom          = district(colored("Salle des Cartes ", "magenta"), 5, "magenta",
                                    ["A la fin de la partie, marquez 1 point supplémentaire", 
                                     "pour chaque carte dans votre main.",
                                     ""])
schoolOfMagic    = district(colored("École de Magie   ", "magenta"), 6, "magenta",
                                    ["Pour la perception des revenus, l'Ecole de Magie est", 
                                     "considérée comme un quartier de la couleur de votre",
                                     "choix."])
library          = district(colored("Bibliothèque     ", "magenta"), 6, "magenta",
                                    ["Si vous choisissez de piocher des cartes au début de votre",
                                     "tour, conservez-les toutes.",
                                     ""])
greatWall        = district(colored("Grande Muraille  ", "magenta"), 6, "magenta",
                                    ["Le prix à payer par le Condottiere pour détruire vos",
                                     "autres quartiers est augmenté de 1.",
                                     ""])
university       = district(colored("Université       ", "magenta"), 6, "magenta",
                                    ["Coûte 6 pièces d'or à bâtir mais vaut",
                                     "8 points pour le calcul du score.",
                                     ""])
dragonGate       = district(colored("Dracoport        ", "magenta"), 6, "magenta",
                                    ["Coûte 6 pièces d'or à bâtir mais vaut", 
                                     "8 points pour le calcul du score.",
                                     ""])

# Define the class player
class player:
    def __init__(self, name):
        self.name = name
        self.character = None
        self.gold = 0
        self.hand = []
        self.city = []
        self.isking = False
        self.ai = False
        self.current = False
        self.points = 0
        self.murdered = False
        self.stealed = False
        self.revealed = False

playerList = []
for i in range(7):
    playerList.append(player(f"player{i + 1}          "))

# Characters
class character:
    def __init__(self, name, number, color, actions, effect):
        self.name = str(number) + ": " + name
        self.number = number
        self.color = color
        self.actions = actions
        self.effect = effect

char1 = character("Assassin      ", 1, ""      , [140], ["L'Assassin peut tuer un personnage de son choix.", 
                                                      "Celui-ci ne jouera pas durant ce tour.",
                                                      ""])
char2 = character("Voleur        ", 2, ""      , [145], ["Le Voleur peut voler le personnage de son choix.", 
                                                  "Quand le personnage détroussé sera révélé, il", 
                                                  "donnera tout son or au voleur."])
char3 = character("Magicien      ", 3, ""      , [150, 155], ["Au Choix :", 
                                                  "-Echanger sa main avec celle du joueur de son choix",
                                                  "-Echanger x cartes de sa main contre x cartes de la pioche"])
char4 = character("Roi           ", 4, "yellow", [130], ["Le Roi prend la Couronne.", 
                                                  "Il choisira son personnage en premier au prochain tour.", 
                                                  "Ses quartiers " + colored("nobles", "yellow") + " rapportent"])
char5 = character("Evêque        ", 5, "blue"  , [131], ["L'Evêque est immunisé contre le Condottiere sauf s'il", 
                                                  "a été assassiné.", 
                                                  "Ses quartiers " + colored("religieux", "blue") + " rapportent"])
char6 = character("Marchand      ", 6, "green" , [132, 160], ["Le Marchand reçoit 1 pièce d'or au début de son tour.", 
                                                  "Ses quatiers " + colored("commerçants", "green") + " rapportent", 
                                                  ""])
char7 = character("Architecte    ", 7, ""      , [165], ["L'Architecte pioche 2 cartes supplémentaires au début", 
                                                  "de son tour.", 
                                                  "Il peut bâtir jusqu'à 3 quartiers"])
char8 = character("Condottiere   ", 8, "red"   , [170, 133], ["Le Condottiere peut détruire un quartier en payant", 
                                                  "son coût de construction moins 1.", 
                                                  "Ses quartiers " + colored("militaires", "red") + " rapportent"])

# Class item
class item:
    def __init__(self, actionFunct, name1, name2 = "", name3 = ""):
        self.name = name1
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.actionFunct = actionFunct
    def updateName(self, arg1="", arg2="", arg3=""):
        self.name = self.name1 + str(arg1) + self.name2 + str(arg2) + self.name3 + str(arg3)
    def exe(self, playerList, choiceList = []):
        return self.actionFunct(self.name, playerList, choiceList)

# Functions of items
def question(itemString, playerList, choiceList):
    return board.loopBottom(itemString, playerList, choiceList)

def questionNoEsc(itemString, playerList, choiceList):
    return board.loopBottom(itemString, playerList, choiceList, True)

def assent(itemString, playerList, choiceList):
    return board.bottomAssent(itemString, playerList, choiceList)
    
def choice(itemString, playerList, choiceList):
    # Will never be call
    return

idMap = {
        # Districts
        1  : tavern,
        2  : tradingPost,
        3  : market,
        4  : docks,
        5  : harbor,
        6  : townHall,
        7  : temple,
        8  : church,
        9  : monastery,
        10 : cathedral,
        11 : watchtower,
        12 : prison,
        13 : battlefield,
        14 : fortress,
        15 : manor,
        16 : castle,
        17 : palace,
        18 : hauntedCity,
        19 : keep,
        20 : observatory,
        21 : laboratory,
        22 : smithy,
        23 : graveyard,
        24 : imperialTreasure,
        25 : mapRoom,
        26 : schoolOfMagic,
        27 : library,
        28 : greatWall,
        29 : university,
        30 : dragonGate,
        # Players
        41 : playerList[0],
        42 : playerList[1],
        43 : playerList[2],
        44 : playerList[3],
        45 : playerList[4],
        46 : playerList[5],
        47 : playerList[6],
        # Characters
        51 : char1,
        52 : char2,
        53 : char3,
        54 : char4,
        55 : char5,
        56 : char6,
        57 : char7,
        58 : char8,
        # Items of choosing a character
        100: item(question, "Que choisissez-vous ?                                     "),
        101: item(assent  , "Vous avez choisi ", "                        "),
        102: item(assent  , "Vous devenez le Roi.                                      "),
        103: item(assent  , "Il devient le Roi.                                        "),
        104: item(assent  , ""," devient le Roi.                         "),
        # Beginning of the turn
        105: item(assent  , "Vous commencez votre tour.                                "),
        106: item(assent  , "", " commence son tour.                      "),
        # Items of the turn
        109: item(question, "Quelle action faites-vous ?                               "),
        110: item(choice  , "Prendre de l'or ou des cartes                             "),
        111: item(question, "Choisissez vous l'or ou les cartes ?                      "),
        112: item(choice  , "Piocher ", " quartiers, en conserver 1 et défausser le reste "),
        113: item(choice  , "Piocher ", " quartiers                                       "),
        114: item(choice  , "Prendre 2 pièces d'or dans la banque                      "),
        115: item(questionNoEsc, "Quel quartier choisissez-vous ?                           "),
        116: item(assent  , "", " pioche une carte.                       "),
        117: item(assent  , "", " pioche ", " cartes.                         "),
        # Building a district
        120: item(choice  , "Bâtir un quartier                                         "),
        121: item(question, "Quel bâtiment voulez-vous construire ?                    "),
        122: item(assent  , "Vous avez déjà ce quartier dans votre cité                "),
        123: item(assent  , "Vous n'avez pas assez de pièces d'or.                     "),
        124: item(assent  , "Vous construisez ", " pour ", " pièces d'or.    "),
        125: item(assent  , "", " construit ", "             "),
        # Gold gained from district's color
        130: item(choice  , "Percevoir les revenus de ses quartiers jaunes             "),
        131: item(choice  , "Percevoir les revenus de ses quartiers bleus              "),
        132: item(choice  , "Percevoir les revenus de ses quartiers verts              "),
        133: item(choice  , "Percevoir les revenus de ses quartiers rouges             "),
        134: item(assent  , "Vous récupérez ", " pièces d'or.                             "),
        135: item(assent  , "", " récupère ", " pièces d'or                   "),
        # Power of the Assassin
        140: item(choice  , "Assassiner un personnage                                  "),
        141: item(question, "Choisissez un personnage à assassiner.                    "),
        142: item(assent  , "Vous assassinez le ", "          "),
        143: item(assent  , "", " assassine le ", "                      "),
        144: item(assent  , "", " était assassiné ce tour                 "),
        # Power of the Thief
        145: item(choice  , "Voler un personnnage                                      "),
        146: item(question, "Choisissez un personnage à voler.                         "),
        147: item(assent  , "Vous volez le ", "                           "),
        148: item(assent  , "", " vole le ", "               "),
        149: item(assent  , "Vous vous faites voler par ", "              "),
        1492: item(assent  , "Il se fait voler par ", "                   "),
        # Powers of the magician
        150: item(choice  , "Echanger x cartes de sa main contre x cartes de la pioche "),
        151: item(assent  , "Vous n'avez pas de cartes en main.                        "),
        152: item(question, "Choisissez une carte à défausser.                         "),
        153: item(choice  , "Echanger ", " cartes contre ", " cartes de la pioche            "),
        154: item(assent  , "Vous piochez ", " cartes.                                    "),
        155: item(choice  , "Echanger votre main avec celle d'un joueur                "),
        156: item(question, "Echanger votre main avec quel joueur ?                    "),
        157: item(assent  , "Vous échangez votre main avec ", ""),
        158: item(assent  , "", " échange ", " cartes de sa main avec la pioche                     "),
        159: item(assent  , "", " échange sa main avec ", "                      "),
        # Power of the Merchant
        160: item(choice  , "Prendre une pièce d'or                                    "),
        161: item(assent  , "Vous récupérez 1 pièce d'or.                              "),
        162: item(assent  , "", " récupère une pièce d'or.                "),
        # Power of the Architect
        165: item(choice  , "Piocher 2 cartes supplémentaires                          "),
        # Power of the Warlord
        170: item(choice  , "Détruire un quartier pour son coût de construction moins 1"),
        171: item(question, "Détruire un bâtiment de la cité de quel joueur ?          "),
        172: item(assent  , "Vous ne pouvez pas détruire un bâtiment de l'évêque.      "),
        173: item(question, "Détruire quel bâtiment ?                                  "),
        174: item(assent  , "Vous ne pouvez pas détruire le donjon.                    "),
        176: item(assent  , "Aucun quartier à détruire dans cette cité                 "),
        177: item(assent  , "Vous ne pouvez pas détruire un quartier d'une cité finie. "),
        178: item(assent  , "Vous détruisez ", " de ", "     "),
        179: item(assent  , "", " détruit ", " de "), # player.name[:-5], district.name, player.name[:-1]
        # Power of the Laboratory
        180: item(choice  , "Laboratoire: Se défausser d'une carte pour 2 pièces d'or  "),
        181: item(question, "Choisissez une carte à défausser.                         "),
        182: item(assent  , "Vous défaussez ", " et recevez 2 pièces.     "),
        183: item(assent  , "", " défausse une carte et reçoit 2 pièces.  "),
        # Power of the Smithy
        185: item(choice  , "Forge: Payer 2 pièces d'or pour piocher 3 cartes          "),
        187: item(assent  , "  ", "  ", "   "),
        188: item(assent  , "", " paye 2 pièces d'or et pioche 3 cartes.  "),
        # Power of the Graveyard
        190: item(questionNoEsc, "", ": Payer 1 pour récupérer ", "?   "), # player.name[:-5]
        191: item(choice  , "Oui                                                       "),
        192: item(choice  , "Non                                                       "),
        193: item(choice  , "Vous récupérez ", "                          "),
        # End of the game
        195: item(assent  , "Vous avez fini votre cité !                               "),
        196: item(assent  , "", " a fini sa cité !                        "),
        # End of turn
        200: item(choice  , "Finir le tour                                             "),
        201: item(assent  , "Vous finissez votre tour.                                 "),
        202: item(assent  , "", " finit son tour.                         ") 
            }
