![Control](Images\control_header.png "Shot by Jim2point0")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes (with tools)
DSR | Yes (not all resolutions are supported)
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11, DirectX 12

## Mods

* [Loose Files Loader](https://www.nexusmods.com/control/mods/11): This mod does not do anything on its own but is used by other mods that supply loose files.

* [Tweakables](https://www.nexusmods.com/control/mods/14): This mod allows the player to customize a wide variety of the game's tweakable parameters. 

* [Photomode Range Unlocker](https://www.nexusmods.com/control/mods/23): This mod unlocks the in-game Photomode allowing the player to move the camera to greater distances than what is possible in the vanilla game.

## Tools

* [Reshade](https://reshade.me/): A fantastic piece of software that allows players to heavily customize how the game looks. Refer to these [series of guides](https://framedsc.github.io/ReshadeGuides/index.htm) for more detail.

* [Simple Runtime Window Editor (SRWE)](https://github.com/dtgDTGdtg/SRWE): This tool is needed to rescale the game window to custom sizes for the purpose of taking screenshots at a very high resolution

* [Cheat Engine Table by Otis_Inf & HattiWatti](..\CheatTables\Control_DX12_Hotsampling.CT): This tool is used to perform Hotsampling. To learn more, refer to this [Cheat Engine Table guide](https://framedsc.github.io/GeneralGuides/cheat_engine_tables.htm).

## Workflow
First, run the game as adminstrator. [*Note*: Only the DX12 exe supports Raytracing].

Alt-tab out of the game to run both SRWE (as administrator) and Control's Cheat Engine table. Attach both of them to Control's exe process and hop back in game.

When you feel like taking a shot, press `ESC`, change the game's Display Mode to `Windowed` and open the Photo Mode. Frame your shot and add any Reshade effect if you want. When you are satisfied with the composition and the colors, alt-tab out and in SRWE, set the Width and Height according to the resolution you want to take the shot in. Remember to check the `Force EXITSIZEMOVE` option in SRWE. After setting the resolution, alt-tab back in to the game and wait for 1-2 second while Reshade reloads the effects. Take the screenshot using Reshade's screenshot keybind.

## Rough Edges
The game seems to have some issues with noise, which is exacerbated with Raytracing, especially on walls and doors in some cases. Texture breaking has also been noticed at certain resolutions and aspect ratios.

## Useful links

[PC Gaming wiki](https://www.pcgamingwiki.com/wiki/Control)