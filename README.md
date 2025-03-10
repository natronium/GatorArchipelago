# GatorArchipelago: APWorld for Lil Gator Game
Lil Gator Game is a game about being an adorable gator who is getting all of their friends involved in their giant hero quest in order to convince their big sister to stop working on her college assignment and instead play with them.

This project is an [Archipelago](https://archipelago.gg/) apworld for [Lil Gator Game](https://store.steampowered.com/app/1586800/Lil_Gator_Game/) that works with a [mod](https://github.com/natronium/GatorRando). Together, they will take the things your character would receive throughout the game and randomize them, potentially between multiple games. If you are not familiar with Archipelago, we recommend reading Archipelago's introduction documents starting with the [FAQ](https://archipelago.gg/faq/en/).

## Instructions
1. Setup the [GatorRando mod](https://github.com/natronium/GatorRando) as described in its README.
2. Install [Archipelago 0.5.1+](https://github.com/ArchipelagoMW/Archipelago/releases/tag/0.5.1) (or follow their instructions to run from source)
3. Download the latest apworld provided on the [releases page](https://github.com/natronium/GatorArchipelago/releases/latest)
	- Check to make sure the name of your download does not have any artifacts (i.e. no (1) or other browser added names). The apworld should be named "lil_gator_game.apworld"
	- To create the apworld from scratch: download this repo's source code and zip the whole folder into a file named lil_gator_game.apworld. The zip/apworld file should contain a `lil_gator_game` folder at the top level 
4. On Windows, double-click the apworld &mdash; it should be "installed" (copied) into the `custom_worlds` folder in your Archipelago installation folder. (On Linux and Mac, manually copy the apworld into the `custom_worlds` folder)
5. Set your options in a .yaml file [as described below](#creating-your-yaml), and put that yaml file and yamls for any other players/games in the `Players` folder in your Archipelago installation folder (note that you will need to run the Archipelago Launcher and click on "Generate template options" to create this folder)
	- Make sure you remove any yamls for people who are not playing this time! If you're planning to play one "world" of Lil Gator Game, there should only be one yaml
	- The "name" at top of the yamls needs to be unique for each player in the game (sorry, not everyone can be "LilGator")
6. Push the Generate button in the Launcher.
7. Host the generated game locally either by hitting Host Game and selecting the AP_{numbers}.zip in the `output` folder (in your Archipelago installation folder) or host it through [archipelago.gg](https://archipelago.gg) by uploading that zip to https://archipelago.gg/uploads

### Recommendations for Better Play Experiences
- Download [Poptracker](https://poptracker.github.io/) and use the pack available at https://github.com/natronium/GatorPop.
- If you are having trouble finding a specific location, you can search the map available at https://natronium.github.io/GatorMap/ to find all the pots, chests, and races with their locations labeled as they are in the Archipelago.
- Use the text client (which you can also open from the Archipelago Launcher) alongside your game. Using the text client will allow you to see what items you are sending and receiving, as only some sent items currently display in game.

## Creating your yaml
We recommend starting with the basic yaml template provided with the [latest release](https://github.com/natronium/GatorArchipelago/releases/latest). If you would like to experiment with options not listed in the basic template provided here, you can check the [advanced yaml instructions](https://archipelago.gg/tutorial/Archipelago/advanced_settings/en) provided by Archipelago.

### yaml Recommendations
- Especially if you are playing the randomizer for the first time, set `start_with_checkfinders: 'true'`. You will start with the Mgaphone and Texting With Jill, which can point you towards checks that are "in logic" (available to you based on your current items and settings). You'll need to change the settings for these items in your in-game Settings menu
- If you are playing with other games, we recommend setting `start_with_freeplay: 'true'` if the other games have a lot of early things they can do and `start_with_freeplay: 'false'` if they are limited. Freeplay opens up a lot of places to check, which can be good and bad, depending on your play preference, your group, and your comfort with the game
- If you are playing solo, `start_with_freeplay: 'false'` can be a good way to figure out how to play since there's a limited number of places to check, but `start_with_freeplay: 'true'` will provide a more varied experience

### Lil Gator Game Specific Options
- Start With Freeplay (If enabled, does the following)
	- After prologue, game will advance to the state on Tutorial Island where Lil Gator will talk to Big Sis to show off their hat, sword, and shield
	- After talking to Big Sis, the Main Island will be unlocked (no more invisible wall around Tutorial Island), Tom will call, and the Friend Counter will be enabled
	- Jill, Avery!, and Martin's Tutorial Island Quests will still be available to complete to receive the associated checks
- Start with Checkfinders
	- If enabled, start with the Megaphone and Texting With Jill in your starting inventory. You can change how these items behave in the Settings menu in-game
	- Recommended for folks learning the locations of checks in the game and the logic behind what items you need to reach them
- Require Shield Jump
	- If enabled, logic may require the player to reach higher places than possible with just a jump by using their shield at the top of their jump
- Harder Ranged Quests
	- If enabled, for Penelope (Bastion Beaver) and Andromeda (Space Hawk), a ranged weapon is no longer required and logic may require the player to jump off the cliff and knock down the relevant cardboard with another relevant cardboard destroyer.