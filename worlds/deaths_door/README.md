# DeathsDoorArchipelago: APWorld for Death's Door
Death's Door is a game about being a crow whose job it is to collect souls, who then accidentally stumbles into a grand conspiracy about the nature of life and death. Also, you hit things with weapons.

This project is an [Archipelago](https://archipelago.gg/) apworld for [Death's Door](https://store.steampowered.com/app/894020/Deaths_Door/) that works with a [mod](https://github.com/Chris-Is-Awesome/DDArchipelagoRandomizer/). Together, they will take the things your character would pick up throughout the game and randomize them, potentially between multiple games. If you are not familiar with Archipelago, we recommend reading Archipelago's introduction documents starting with the [FAQ](https://archipelago.gg/faq/en/).

## Instructions
1. Setup the [Death's Door Archipelago Mod mod](https://github.com/Chris-Is-Awesome/DDArchipelagoRandomizer/) as described in its README.
2. Install [Archipelago 0.6.3+](https://github.com/ArchipelagoMW/Archipelago/releases/) (or follow their instructions to run from source)
3. Download the latest apworld provided on the [releases page](https://github.com/roseasromeo/DeathsDoorAPWorld/releases/latest)
    - Check to make sure the name of your download does not have any artifacts (i.e. no (1) or other browser added names). The apworld should be named "deaths_door.apworld"
    - To create the apworld from scratch: download this repo's source code and zip the whole folder into a file named deaths_door.apworld. The zip/apworld file should contain a `deaths_door` folder at the top level 
4. On Windows, double-click the apworld &mdash; it should be "installed" (copied) into the `custom_worlds` folder in your Archipelago installation folder. (On Linux and Mac, manually copy the apworld into the `custom_worlds` folder)
5. Set your options in a .yaml file [as described below](#creating-your-yaml), and put that yaml file and yamls for any other players/games in the `Players` folder in your Archipelago installation folder (note that you will need to run the Archipelago Launcher and click on "Generate template options" to create this folder)
    - Make sure you remove any yamls for people who are not playing this time! If you're planning to play one "world" of Death's Door, there should only be one yaml
    - The "name" at top of the yamls needs to be unique for each player in the game (sorry, not everyone can be "CAAAAAAW")
6. Push the Generate button in the Launcher.
7. Host the generated game locally either by hitting Host Game and selecting the AP_{numbers}.zip in the `output` folder (in your Archipelago installation folder) or host it through [archipelago.gg](https://archipelago.gg) by uploading that zip to https://archipelago.gg/uploads

### Recommendations for Better Play Experiences
- Download [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) and use it to track which locations are in logic.
- Use the text client (which you can also open from the Archipelago Launcher) alongside your game. Using the text client will allow you to see what items you are sending and receiving in more detail.

## Creating your yaml
Start by installing the apworld (Steps 2-4 in [Instructions](#instructions)). Open the Archipelago Launcher and click `Generate Template Options`. On Windows, a File Explorer should open to the newly generated folder of template yamls (on other OSs, you will need to navigate to your Archipelago installation, then to `Players/Templates`). Within that file, you'll see all of the options available in Death's Door (Death's Door specific options are described [below](#deaths-door-specific-options)) If you would like to experiment with other options not listed here, you can check the [advanced yaml instructions](https://archipelago.gg/tutorial/Archipelago/advanced_settings/en) provided by Archipelago.

### yaml Recommendations
- In small multiworlds, under current options available, we highly recommend that you leave `early_important_item` set to `early` or change it to `local_early`. This option reduces the likelihood that the fill algorithm will back itself into a corner.

### Death's Door Specific Options
- Start Day or Night
    - Choose whether to start with daytime or nighttime. Must access Rusty Belltower Bell in game to toggle using the Rusty Belltower Key (or a glitch).
- Early Important Item
    - Choose whether one random important item will be placed early in the multiworld ("early"), early and in your world ("local_early"), or be allowed to be randomly placed ("random_placement").
    - If random placement, generation is more likely to fail.
    - Important items are all non-boss doors, Hookshot, Bomb, and Fire since these unlock access to more early game checks.
- Starting Weapon
    - Choose which weapon you would like to start with (others will be shuffled into the itempool as useful items, or progression if Roll Buffers are on).
    - Note: Umbrella is a much worse weapon than the other 4. Choose at your own risk.
    - If Weapons are not randomized, your starting weapon will be forced to be the Reaper's Sword.
- Planted Pots Required
    - Choose how many planted seeds are required to unlock the Green Tablet door in the Estate of the Urn Witch Family Tomb. Vanilla is 50, defaults to 25. Adjusts the number of Life Seeds that are marked as progression. If you are having generation failures due to FillError, consider lowering this number.
- Extra Life Seeds, Magic Shards, Vitality Shards
    - Extra of those items (20 max Life Seeds, 8 max each for Shards). Replace 100 Souls items in the pool. Will be set to 0 if Soul Orbs are not randomized.
- Remove Spell Upgrades
    - Removes spell upgrades from the pool, so that there is only 1 Fire, 1 Bomb, and 1 Hookshot in the pool (and no upgrade for Arrow)
- Gate Rolls Glitch
    - Adds the option in logic of rolling through gates.
        - Estate entrance to Crypt through metal gate
        - Mushroom Dungeon Lobby to Overgrown Ruins through vines
        - Mushroom Dungeon Ancient Door to Lobby through a metal gate and a cobweb
        - Ceramic Manor Lobby to the Manor exit to Estate through breakable-pot door
- Bomb Bell Glitch
    - Add the option in logic of shooting the Rusty Belltower with a Bomb from a railing to trigger the Day/Night switch.
- Offscreen Targeting Tricks
    - Add in logic three tricks in which you must target an enemy or switch from offscreen.
        - Open the switch between Lost Cemetery and Stranded Sailor caves using an Arrow through a fire source instead of Fire
        - Open a bomb wall in Overgrown Ruins lower by hitting an offscreen bomb flower with an arrow
        - Open the path backwards from Flooded Fortress Frog King Statue back to the entrance by hitting a switch offscreen
- Geometry Exploits
    - Adds in logic a series of exploits where you roll on unintended surfaces.
        - Rolling across the walls near the ladder immediately outside the exit from Lost Cemetery to Stranded Sailor Caves to navigate around the switch on the Lost Cemetery side
        - Rolling behind the grate in Castle Lockstone East Upper down to East
        - Rolling onto the wall from the upper right platform in Lockstone East Upper after making it go up to get into East Upper Keyed Door without the lever
        - When coming from the Old Watchtowers Barb Elevator, the lever to Ice Skating Start can be skipped by hooking over the gate from the ledge around the top of the elevator
        - In Overgrown Ruins, access the Soul Orb in Lower that requires Hookshot by rolling onto the wall above and falling down. Standalone randomizer notes that this roll may require Haste (rolling stat) >=2.
        - In Overgrown Ruins, access the Soul Orb in the Lord of Doors Hookshot arena by ???. Standalone randomizer is missing a description of this one, but best guess it is the same as the above.
- Roll Buffers
    - Adds in logic roll buffers, where you roll in mid-air after a heavy attack. Three of these tricks can be performed with any weapon but the hammer. Two are doable only with Rogue Daggers. This option will cause all weapons besides the hammer to be marked as progression.
        - Hall of Doors - Surveillance Device: Heavy to the right and roll down-right from behind the bin near the Discarded Umbrella check
        - Hall of Doors - Bomb Secret Soul Orb: Same as above
        - Hall of Doors - Hookshot Secret Soul Orb: Up-right heavy and roll from above the Lord of Doors poster by the staircase near the Bomb Avarice Chest (Rogue Daggers only)
        - Hall of Doors - Modern Door Scale Model: Same as above (Rogue Daggers only)
        - Castle Lockstone - West Locked Crow: Heavy out of the ledge above the gate then immediately roll back
- Unrandomized Pools
    - Remove sets of item-location pairs from being randomized. Warning: removing too many pools (especially Soul Orbs) will cause generation errors, especially in small multiworlds. See the template yaml for more details.

## Contributing

If you're interested in helping out, join the discussion in the [Archipelago Discord server](https://discord.com/invite/8Z65BR2).
We talk about the development of this in the Death's Door thread in the `future-game-design` forum!

## Acknowledgements

A huge amount of credit for the original logic, options, and structure of what is randomized goes to [dpinela](https://github.com/dpinela) for their work on the [Multiworld Randomizer](https://github.com/dpinela/DeathsDoor.Randomizer). Many of the glitch option descriptions are pulled from their comments.

This apworld's logic structures rely on [rule_builder](https://github.com/ArchipelagoMW/Archipelago/pull/5048) by DrTChops. This apworld would have taken dramatically longer to build without it.
