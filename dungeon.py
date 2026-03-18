import random
from os import system as sys

def diceRoller(count,sides):
    return sum(random.randint(1,sides) for _ in range(count))

def moving(direction, player):
    if direction == "north":
        player["y"] += 1
    elif direction == "south":
        player["y"] -= 1
    elif direction == "east":
        player["x"] += 1
    elif direction == "west":
        player["x"] -= 1
    return player

def roomGen(entered_from):
    door_swap = {"north" : "south", "south" : "north", "east" : "west", "west" : "east" }
    last_door = door_swap[entered_from]
    possible_doors = [ "north", "south", "east", "west" ]
    possible_doors.remove(last_door)
    random_door = random.choice(possible_doors)
    doors = [ last_door, random_door ]
    monster = random.choice([ None, "Goblin", "Zombie", "Ghoul" ])
    description = random.choice(["a long hallway","guard quarters","torture chamber","an old monster's lair"])
    flavor = random.choice(["covered with cobwebs","with a fallen adventurer","strange runes drawn on the floor","with a musty smell in the air"])
    descript = f"{description}, {flavor}, there are doors to the {' and '.join(doors)}"
    if monster:
        monster = {"type" : monster, "hp" : diceRoller(1,8), "ac" : 10 }
        descript = descript + f" ... THERE IS A {monster["type"]} ABOUT TO ATTACK!"
    room_dict = { "description" : descript, "doors" : doors, "monster" : monster }
    return room_dict

def combat(player,monster):
    mon_init = diceRoller(1,6)
    player_init = diceRoller(1,6)
    if player_init >= mon_init:
        monster["hp"] -= diceRoller(1,6)
        if monster["hp"] <= 0:
            return player, monster
        player["hp"] -= diceRoller(1,6)
        return player, monster
    else:
        player["hp"] -= diceRoller(1,6)
        if player["hp"] <= 0:
            return player, monster
        monster["hp"] -= diceRoller(1,6)
        return player, monster

def main():
    sys('clear')
    heading = "## DUNGEON CRAWLER ##"
    cmd = input(f"{heading}\n\nWelcome to the dungeon\nEnter your name to continue\nOr enter 'quit' to exit the game\n\n> ")
    if cmd == "quit":
        quit()
    player = { "name" : cmd, "hp" : 10, "ac" : 11, "x" : 0, "y": 0, "items" : ["sword"], "combats" : 0, "rooms explored" : 1 }
    dungeon = { 0 : { 0 : { "description" : "a grand entrance, covered with cobwebs, there is a door to the north", "doors" : ["north"], "monster" : None } } }
    message = ""
    actions = [ "north", "south", "east", "west", "fight"]
    while cmd != "quit" and player["hp"] > 0:
        sys('clear')
        x = player["x"]
        y = player["y"]
        room = dungeon[x][y]
        cmd = input(f"{heading}\n\nRoom Description:\n{room["description"]}\n\nLast Event:\n{message}\n\n> ").lower()
        if cmd in actions:
            if cmd in ["north","south","east","west"]:
                if cmd not in room["doors"]:
                    message = "there is no door there"
                else:
                    player = moving(cmd, player)
                    new_x = player["x"]
                    new_y = player["y"]
                    if new_x not in dungeon.keys():
                        dungeon[new_x] = {}
                    if new_y not in dungeon[new_x].keys():
                        dungeon[new_x][new_y] = roomGen(cmd)
                    message = "moving " + cmd
                    player["rooms explored"] += 1
            if cmd == "fight":
                if room["monster"]:
                    player, room["monster"] = combat(player,room["monster"])
                    message = f"You swing your blade! New Stats: {player["name"]} HP {player["hp"]}  |  {room["monster"]["type"]} HP {room["monster"]["hp"]}"
                    if player["hp"] <= 0:
                        message = f"you have been killed by the {room["monster"]["type"]}"
                    if room["monster"]["hp"] <= 0:
                        player["combats"] += 1
                        message = f"You have slain the {room["monster"]["type"]}! New Stats: {player["name"]} HP : {player["hp"]}, Combats : {player["combats"]}"
                        room["description"] = room["description"].split(" ...")[0] + f" ... a slain {room["monster"]["type"]} lies on the ground"
                        room["monster"] = None
                else:
                    message = "there is nothing to fight"
            if cmd == "search":
                message = "searching"
        else:
            message = "that is not a command try one of: " + ", ".join(actions)
    print(f"\n## GAME OVER ##\nFinal Score:\n{player["name"]} | {player["combats"]} combats | {player["rooms explored"]} rooms explored\n")

main()
