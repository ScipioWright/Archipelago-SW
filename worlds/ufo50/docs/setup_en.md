# UFO 50 Setup Guide

## Required Software
- [UFO 50](https://store.steampowered.com/app/1147860/UFO_50/) for PC
- The [UFO 50 APWorld](https://github.com/UFO-50-Archipelago/Archipelago/releases)

## Installation

### Automated Installation
Place the UFO 50 APWorld in your `custom_worlds` folder.
Open the UFO 50 Client and follow the prompts shown.

### Manual Installation

Extra required software:
- A way to apply `.bsdiff4` patches, such as [bspatch](https://www.romhacking.net/utilities/929/).

Steps:
1. Copy all of your UFO 50 files to a safe location.
2. Extract all files from `ufo_50_archipelago.zip` into the same directory as the files extracted in the previous step.
   * This should include, at least, `ufo_50_basepatch.bsdiff4` and `gm-apclientpp.dll`.
3. If you don't have `original_data.win`, copy `data.win` and rename its copy to `original_data.win`.
   * By keeping an unmodified copy of `data.win`, you will have an easier time updating in the future.
4. Apply the `ufo_50_basepatch.bsdiff4` patch using your patching software.
5. To launch the game, run `ufo50.exe`.

### Downpatching

As UFO 50 is a game that is still receiving updates, periods of time between new official patches and the mod being updated will exist.
Therefore, the user may end up having to either wait for the mod to be updated or use an older version of the game in order to play.  You can check which version of UFO 50 the mod targets [in the patch releases page](https://github.com/UFO-50-Archipelago/Patch/releases).

You can download a version of UFO 50 published on a specific date by going to the [UFO 50 SteamDB page](download_depot 1147860 1147861 3089918629065615857) and pressing on the "copy to clipboard" button of the release you want. Follow the instructions from there.

## Joining a MultiWorld Game

Launch the game and continue until you reach the profile select screen, which has been replaced with the connection screen.

From here, enter the different menus and type in the following details in their respective fields. In order:
- **server:port** (e.g. `archipelago.gg:38281`)
   * If hosting on the website, this detail will be shown in your created room.
- **slot name** (e.g. `Player`)
   * This is your player name, which you chose along with your player options.
- **password** (e.g. `123456`)
  * If the room does not have a password, it can be left empty.
