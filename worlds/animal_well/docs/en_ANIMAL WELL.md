# ANIMAL WELL

## Where is the options page?
Generate a template yaml by placing the apworld in your `lib/worlds` folder, then opening the Archipelago Launcher and clicking on Generate Template Options.
When the game is on the website,
The [player options page for this game](../player-options) contains all the options you need to configure and export a config file.

## I haven't played ANIMAL WELL before.
It is recommended to play the vanilla game first. The randomizer will spoil mechanics, items, and the locations of secrets.
We recommend you find all of the eggs, all of the equipment items, and as many bunnies as you can before playing this randomizer.

## What does randomization do to this game?
All items you can find in chests (eggs, toys, keys, matches) are shuffled into the item pool.

## What is the goal of ANIMAL WELL when randomized?
The standard goal is the same as the vanilla game. Find the 4 flames and set off the fireworks at the end.
There will be alternate goals later in development.

## How many checks are in ANIMAL WELL?
There are around 100 checks in ANIMAL WELL. The amount varies based on a few options, and there will likely be more options in the future to increase the number of locations.
When we have finalized these options, this doc will be updated to reflect the actual numbers.

## What do items from other worlds look like in ANIMAL WELL?
They just look like the standard chests.

## Is there a tracker pack?
There is a [Poptracker Pack](https://github.com/SporyTike/ANIMAL-WELL-AP-Tracker/releases/latest) which was made by SporyTike.
If you find issues in the tracker pack, please let them know about them.
Universal Tracker is also an option, and will not run into any of its common issues.

## What should I know regarding logic?
Locations that may softlock you (such as the B. Wand chest) are included in logic. To escape these softlocks, you can either quit to menu and continue (the chest will appear closed, but you will have already sent the check, so it's fine), or you can use the Warp to Hub button in the pause menu.

## Does this game have item and location groups?
Yes! To find what they are, type `/item_groups` or `/location_groups` into the ANIMAL WELL Client, or the Archipelago Text Client while connected to an ANIMAL WELL session.

## What are the current known issues?
The client rarely fails for no discernable reason when opening a chest. We do not know why yet. If it fails, please let us know in the discord and send us your log file (in your `Archipelago/logs` folder). We may ask you to troubleshoot a few things as well.
Some yaml options are missing. This is intentional. They don't work yet.

## Who contributed to this?
ScipioWright and RoobyRoo wrote a majority of the logic and apworld.
Franklesby wrote the client. Dicene and Dregu contributed major features to the client.
Various others helped with some bug fixes and minor additions.
Special thanks to SporyTike for making the poptracker, GameWyrm for their help early on, and Kevin for convincing Scipio to get the game.
