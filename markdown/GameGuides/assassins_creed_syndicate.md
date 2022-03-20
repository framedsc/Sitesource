![Assassin's Creed Syndicate](Images\acsyndicate_header.png "Shot by Vikster"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes (DX11)
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [Hatti's Camera Tools (Password: CinematicTools)](https://www.mediafire.com/file/e74f8n4f0p59fe3/AC-f043a6.rar/file)  
__Features__: Camera control (gamepad support), FOV Control, Camera/Rotation Speed, UI toggle (also includes Extreme Injector within downloaded folder).
* [Toggle HUD Mod](https://www.nexusmods.com/assassinscreedunity/mods/2)  
__Features__: UI toggle originally made for Unity, but it also works for Syndicate.
* [Timestop CT by Otis_Inf](..\CheatTables\ACS_TimeStop_AOB.CT)  
**Features**: It stops time. :)

## Tips and Tricks

### Hatti's Camera Controls

Key	| Command
--|--
`INS` | Toggle camera
`Arrow Keys` / RS | Rotate camera
`Num 8` / `Num 5` / LS | Move camera forward / backward
`Num 4` / `Num 6` / LS | Move camera left / right
`Num 7` / `Num 9` / LT / RT | Move camera up / down
`Num 1` / `Num 3` / LB / RB | Roll camera left / right
`PgUp` / `PgDn` / D-pad Up/Down | Increase / decrease FoV

The camera tools' user interface is automatically opened when the .dll is injected. Navigate the window with the arrow keys but DO NOT close it otherwise the game will also close itself immediately.

The freecam is enabled with the _Enter_ key through the user interface's window or by pressing the _Insert_ key while in-game. Movement and rotation speeds can only be adjusted through the window. You can experiment with the input speeds to allow for more accurate camera movement (values as low as 0.01 are possible).

### Notes on the timestop table and camera tools

Be informed that using the timestop table is prone to crashing the game. It also cannot stop the weather meaning rain will continue to fall and the intensity of sunlight may change. Some cutscenes will continue to progress their dialogue but the actors will remain frozen. 

Though unlikely, the camera tools will sometimes cause the game to crash. The tools' UI toggle may also be unresponsive so Unity's HUD toggle mod can be used as an alternative. Make sure to inject the tools and cheat table AFTER loading into London to minimize the likelihood of crashes.


### Setting up ReShade's depth buffer

If you plan on using ReShade, note that Assassin's Creed Syndicate uses a reversed depth buffer. This means that you will need to go through the global processor definitions and change `RESHADE_DEPTH_INPUT_IS_REVERSED ` from 0 to 1. This step is essential otherwise depth-related shaders will stay broken by default.

### Disabling Depth of Field and in-game Fog

Assassin's Creed Syndicate does not allow you to disable depth of field while in-game, you'll have to do it by editing the configuration file. You can do this by navigating to `%USERPROFILE%\Documents\Assassin's Creed Syndicate` and opening _AC.ini_. Search for `PostFX` and change the value from 1 to 0. 

To disable fog, search for `Fog` :) in the same configuration file and change 1 to 0. If either parameter does not exist, simply add them in yourself.

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Assassin%27s_Creed_Syndicate)

