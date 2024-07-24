# GatorArchipelago: APWorld for Lil Gator Game
Lil Gator Game is a game about being an adorable gator who is getting all of their friends involved in their giant hero quest in order to convince their big sister to stop working on her college assignment and instead play with them.

This project is an apworld that works with Archipelago and a plugin for Lil Gator Game ([mod link](https://github.com/natronium/GatorRando)) to take the things your character would receive throughout the game and randomize them through either a solo or multiworld experience. If you are not familiar with Archipelago, we recommend reading Archipelago's introduction documents starting with the [FAQ](https://archipelago.gg/faq/en/).

## Instructions
1. Setup the [GatorRando mod](https://github.com/natronium/GatorRando) as described in its repo.
2. Download the apworld provided on the releases page (or `git clone` the repo and zip the folder into a file named lil_gator_game.apworld)
3. Set your options in a .yaml file as described below.
4. Install [Archipelago 0.5.0+](https://github.com/ArchipelagoMW/Archipelago/releases/tag/0.5.0) (or follow their instructions to run from source)
5. Doubleclick the apworld---it should be "installed" (copied) into the custom_worlds folder in your Archipelago installation folder
6. Put your yaml (see Creating Your Yaml below) and yamls for any other players/games in the Players folder (note that you will need to run the Archipelago Launcher and click on "Generate template options" to create this folder)
7. Push the Generate button in the Launcher.
8. Host the generated game locally either by hitting Host Game and selecting the AP_{numbers}.zip in your output folder or host it through [archipelago.gg](https://archipelago.gg) by uploading that zip to https://archipelago.gg/uploads

### Recommendations for Better Play Experiences
- Download [Poptracker](https://poptracker.github.io/) and use the pack available at https://github.com/natronium/GatorPop.
- If you are having trouble finding a specific pot, you can search the map available at https://natronium.github.io/GatorMap/ to find all the pots, chests, and races with their locations labeled as they are in the Archipelago.

## Creating your yaml
We recommend starting with the basic yaml template provided in the repo. If you would like to experiment with options not listed in the basic template provided here, you can check the [advanced yaml instructions](https://archipelago.gg/tutorial/Archipelago/advanced_settings/en) provided by Archipelago.

### Lil Gator Game Specific Options
- Start With Freeplay (If enabled, does the following)
	- After prologue, game will advance to the state on Tutorial Island where Lil Gator will talk to Big Sis to show off their hat, sword, and shield
	- After talking to Big Sis, the Main Island will be unlocked (no more invisible wall around Tutorial Island), Tom will call, and the Friend Counter will be enabled
	- Jill, Avery!, and Martin's Tutorial Island Quests will still be available to complete to receive the associated checks 
- Require Shield Jump
	- If enabled, logic may require the player to reach higher places than possible with just a jump by using their shield at the top of their jump
- Harder Ranged Quests
	- If enabled, for Penelope (Bastion Beaver) and Andromeda (Space Hawk), a ranged weapon is no longer required and logic may require the player to jump off the cliff and knock down the relevant cardboard with another relevant cardboard destroyer.