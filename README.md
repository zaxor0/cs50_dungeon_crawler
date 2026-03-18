# DUNGEON CRAWLER

## Video Demo:
<https://github.com/zaxor0/cs50_dungeon_crawler/blob/main/dungeon.gif>

## Description:
A 100 line dungeon crawler; explore a randomly generated dungeon, fight monsters, try to surive!

### Functions
The code consists of 4 functions:
1. A dice roller, you provide the count of dice and the sides, like 3 six sided or 1 d20.
2. A move function, this updates the player coordinates and is required for more rooms to be generated.
3. A room generator, this provides a random room description and possible a random monster.
4. A combat function, this takes the player and monster stats, rolls for initiave, then deals damage.

### Main Function
The main function provides the following:
1. The character dictionary, that has all the necessary stats
2. The dungeon dictionary, which has a 2d aspect to it, to help track the player coordinates.
4. A list of possible player commands, such a movement and combat.
3. The while loop which contains the core gameplay.

### Deep Dive
Let's first look at the main function. There is a basic header and some description of the game, this relies on a player input. This method is reused in the main while loop. We take the player's input as a "command" which is the variable cmd. If this is anything other than "quit" we treat it as the player name. This variable is passed into the player dictionary too.

Next we build out the dungeon, this is a 2d dictionary starting at [0,0], with a basic description, and no monsters. As the player moves through the dungeon, we will check to see if a room is defined at their coordinates [player x, player y], and if the is not room create one. If there is a room, we pull that room out of the dungeon dictionary. This lets us have persistent rooms.

Next is a list of commands, these are just movement and fighting, can call their associated functions. We can expand on this with maybe search or other actions a player would like to do, only insofar as we also create an associated function.

In the while loop, the core gameplay, we ask the player what they want to do. If its movement, we perform the above regarding dungeon rooms, if it is fight then the combat function is called only if there is a monster in the room, otherwise we point out there is nothing to fight.

For combat, within the core gameplay while loop, we can do this if there is a monster in the room. We first roll 1d6 for the player and monster, to see who attacks first then roll for damage. This could be expanded with "to-hit" rolls to see if anyone misses. Then we return the updated objects with their new stats.

In the event of a monster death, we update the room description to include this, as well as set the "monster" to None.

The game ends when either the player's HP is 0 or less, or if the player executes the "quit" command.

The final output is number of rooms explored and the number of combats won.

