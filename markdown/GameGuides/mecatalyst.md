![Mirror's Edge Catalyst](Images\mecatalyst_header.png "Shot by ItsYFP"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | Yes
Graphics API | DirectX 11
 
## Tools

* [Cinematic Tools by Hattiwatti (Password: CinematicTools)](https://mega.nz/#!8dgWRYKa!QauLJZVyPHvmt4EOxCmQR0WDAOR2ygMYg8rFYLqtgAE)  
    **Features**: Free Camera, Timestop, FOV Control, Hide HUD (read the Readme File for Hotkeys) 

* [Frosty's Mod Manager](https://frostytoolsuite.com/downloads.html)  
    **Features**: Requirement for most mods for Mirror's Edge Catalyst. If you want access to the Steam overlay use [Frosty's Fix](https://github.com/Dyvinia/FrostyFix/releases)

## Tips and Tricks

### Hotsampling and Custom Aspect Ratios

Mirror's Edge Catalyst supports SRWE by default and is capable of both hotsampling and custom aspect ratios without tweaking any settings. Make sure to run the game in Windowed, as it has not been tested in Borderless mode.

### Disabling the Built-in Anti-Aliasing

The game uses supersampled anti-aliasing combined with temporal anti-aliasing, which can be quite performance intensive. For better performance and to be sure they don't interrupt ReShade, you can disable both forms of anti-aliasing in the game's config files found in Documents folder.

1. Start the Windows file explorer and navigate to the Documents folder which is in `%USERPROFILE%\Documents\` by default.
2. Open the Mirror's Edge Catalyst folder, and find the folder named `settings`, then look for the file titled `PROF_SAVE_profile` and open it with your preferred text editor.
3. Change both values for `GstRender.AntiAliasingDeferred` and `GstRender.AntiAliasingPost` to 0.

After doing this, it's recommended to use another form of AA through ReShade, as the game's visual design will make edges stand out more. Using SweetFX's SMAA is a good alternative.

### Mods for Easier Photography

Catalyst runs the game with depth of field and motion blur enabled, though you can disable motion blur in the settings, disabling the different kinds of depth of field during certain actions in game requires the use of a mod. You can use [No Visual Environment Effects](https://www.nexusmods.com/mirrorsedgecatalyst/mods/73) and [Disable Runner's Flow Color Correction](https://www.nexusmods.com/mirrorsedgecatalyst/mods/35/) to completely disable visual effects like color correction, chromatic aberration, and depth of field. These mods only disables these effects during combat and or freerunning, so you are free to manipulate them through shaders as you wish.

The utility mod [Debug Startpoint Selector](https://www.nexusmods.com/mirrorsedgecatalyst/mods/5) includes a menu to select and begin in any startpoint set by the game. This mod and the ones above use [Frosty's Mod Manager](https://frostytoolsuite.com/downloads.html). 


### Setting up Reshade's Depth Buffer

Mirror's Edge Catalyst uses a reversed depth buffer, so ReShade needs to be set up to access this properly. Open the global preprocessor definitions tab and change `RESHADE_DEPTH_INPUT_IS_REVERSED ` from 0 to 1. This allows for shaders to access depth effects, which will be mentioned in the next section.

### Using Hatti's Camera Tools
Hattiwatti's tools are quite extensive, and this section will try to simplify them for easier understanding.

Key	| Command
--|--
`INS` | Toggle camera
`DEL` | Timestop
`HOME` | Toggle HUD
`END` | Block input to game

These settings can also be opened in the tools' accompanying GUI. For an easier time, it is recommended to freeze time using *DELETE* and tweaking the camera's settings through the GUI.

These are the movement controls for both keyboard and controller:

Key	| Command
--|--
`Arrow Keys` ¹ / RS | Look around
`Num 8` / `Num 5` ¹ / LS | Move camera forward / backward
`Num 4` / `Num 6` ¹ / LS | Move camera left / right
`Num 7` / `Num 9` / LT / RT | Move camera up / down
`Num 1` / `Num 3` / LB / RB | Roll camera left / right
`PgUp` / `PgDn` / D-pad Up/Down | Increase / decrease FoV ²

¹ - Blocking input to game allows WASD + Mouselook.  
² - To enable custom FoV, set `Override FOV` to `1`.

The GUI is not only the preferred way of tweaking the camera, but it is also the only way to access different environment controls such as setting up additional lights. These can be found in the tabs present alongside `Camera`. Note that all the values including the camera's speed can be lower than 1, for more precise movement or intensities.

The tool's GUI has some effects that are also available in ReShade, so you may opt for the ingame Depth of Field instead of your usual DoF shader of choice. Remember to experiment with the different effects, especially with Outdoor Environment Light and the Light Manager in `Misc/About` as these are unique to the tool. With the Light Manager you can achieve effects similar to three-point lighting and other lighting systems, or even make your own! :D

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Mirror%27s_Edge_Catalyst)
