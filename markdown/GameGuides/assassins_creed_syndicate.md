![Assassin's Creed Syndicate](Images\acsyndicate_header.png "Shot by Vikster"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes (DX11)
Ansel | No
Graphics API | DirectX 11
 
## Tools

* [Hatti's Camera Tools (Password: CinematicTools)](https://www.mediafire.com/file/e74f8n4f0p59fe3/AC-f043a6.rar/file)  
__Features__: Camera control (gamepad support), FOV Control, Camera/Rotation Speed, UI toggle (also includes Extreme Injector within downloaded folder).
* [Shader toggler](../ShaderTogglers/assassins_creed_syndicate.ini)  
__Features__: HUD toggle and CA toggle for the DLC. Requires Reshade 5+ with [ShaderToggler add-on](../ReshadeGuides/Addons/shader_toggler_repository.htm).
* [Merged Anti-Cheat Table by Paul44 and One3rd](..\CheatTables\ACS_Varia_v3.4_Released_stoptime_resolution.CT)  
**Features**: Disables the game's anti-cheat, timestop and fullscreen resolution selector.

## Cheat Table

The anti-debug script is needed to inject the camera tools without it instantly crashing the game. Even with this the game will crash and frequently. If you absolutely want to shoot this game I've found that to get the best mileage you'll need to open the table, enable cheats (which runs through the threads), enable the timestop "enable script" and then only inject the camera tools when you come to a scene where you want to use it. After injecting the camera tools the game is guaranteed to crash anywhere between 2 to 20 minutes later. Without the camera tools injected it may run longer. This game is a pain to try to shoot.

The Fullscreen Resolution Selector allows changing DSR resolutions when timestop is being used.

## Tips and Tricks

### Hatti's Camera Controls

Command | Keyboard / Controller
--|--
 Toggle camera | `INS`
Rotate camera | `Arrow Keys` / <font face="Controller">></font>
Move camera forward / backward | `Num 8` / `Num 5` / <font face="Controller"><</font>
Move camera left / right | `Num 4` / `Num 6` / <font face="Controller"><</font>
Move camera up / down | `Num 7` / `Num 9` / <font face="Controller">{ / }</font>
Roll camera left / right | `Num 1` / `Num 3` / <font face="Controller">[ / ]</font>
Increase / decrease FoV | `PgUp` / `PgDn` / <font face="Controller">W / X</font>

The camera tools' user interface is automatically opened when the .dll is injected. Navigate the window with the arrow keys but DO NOT close it otherwise the game will also close itself immediately.

The freecam is enabled with the _Enter_ key through the user interface's window or by pressing the _Insert_ key while in-game. Movement and rotation speeds can only be adjusted through the window. You can experiment with the input speeds to allow for more accurate camera movement (values as low as 0.01 are possible).

### Notes on the timestop table and camera tools

Be informed that using the timestop table is prone to crashing the game. It also cannot stop the weather meaning rain will continue to fall and the intensity of sunlight may change. Some cutscenes will continue to progress their dialogue but the actors will remain frozen. 

Though unlikely, the camera tools will sometimes cause the game to crash. The tools' UI toggle may also be unresponsive so the shader toggler mod can be used as an alternative. Make sure to inject the tools and cheat table AFTER loading into London to minimize the likelihood of crashes.


### Setting up ReShade's depth buffer

If you plan on using ReShade, note that Assassin's Creed Syndicate uses a reversed depth buffer. This means that you will need to go through the global processor definitions and change `RESHADE_DEPTH_INPUT_IS_REVERSED ` from 0 to 1. This step is essential otherwise depth-related shaders will stay broken by default.

### Disabling Depth of Field and in-game Fog

Assassin's Creed Syndicate does not allow you to disable depth of field while in-game, you'll have to do it by editing the configuration file. You can do this by navigating to `%USERPROFILE%\Documents\Assassin's Creed Syndicate` and opening _AC.ini_. Search for `PostFX` and change the value from 1 to 0. 

To disable fog, search for `Fog` :) in the same configuration file and change 1 to 0. If either parameter does not exist, simply add them in yourself.

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Assassin%27s_Creed_Syndicate)

