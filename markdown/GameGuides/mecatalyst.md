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
    **Features**: Free Camera, Timestop, FOV Control, Hide HUD, Postprocessing, High LOD, shadow resolution, timescale and more.
* [Time Changer Tool](https://bitbucket.org/timm0e/mec-tc-release/wiki/MEC-TC)  
    **Features**: ToD control. Use alongisde [Reset Lighting Button](https://www.nexusmods.com/mirrorsedgecatalyst/mods/163).
* [Frosty's Mod Manager](https://frostytoolsuite.com/downloads.html)  
    **Features**: Requirement for most mods for Mirror's Edge Catalyst. If you want access to the Steam overlay use [Frosty's Fix](https://github.com/Dyvinia/FrostyFix/releases).

## Hattiwatti Tools Usage
Hattiwatti's tools are quite extensive, and this section will try to simplify them for easier understanding.

Command | Key
--|--
Toggle camera | `INS`
Timestop | `DEL`
Toggle HUD | `HOME`
Block input to game | `END`

These settings can also be opened in the tools' accompanying GUI. For an easier time, it is recommended to freeze time using `DELETE` and tweaking the camera's settings through the GUI.

These are the movement controls for both keyboard and controller:

Command | Keyboard - Controller
--|--
Look around | `Arrow Keys` ¹ / <font face="Controller">></font>
Move camera forward / backward / left / right | `Num 8` / `Num 5` / `Num 4` / `Num 6` ¹ - <font face="Controller"><</font>
Move camera up / down | `Num 7` / `Num 9` - <font face="Controller">{ / }</font>
Roll camera left / right | `Num 1` / `Num 3` - <font face="Controller">[ / ]</font>
Increase / decrease FoV ² | `PgUp` / `PgDn` - <font face="Controller">W / X</font>

¹ - Blocking input to game allows WASD + Mouselook.  
² - To enable custom FoV, set `Override FOV` to `1`.

@alert important
Once you finish shooting a scene, to return the handling of the FOV to the game change the `Override FOV` setting to `0` and then to `-1` once again.
@end

The GUI is not only the preferred way of tweaking the camera, but it is also the only way to access different environment controls such as setting up additional lights, which can be found in the **MISC/ABOUT** tab. Note that all the values including the camera's speed can be lower than 1, for more precise movement or intensities.

Before changing any of the postprocessing settings on the **ENVIRONMENT** tab go to the **CONTROLS** submenu, and press **GET VALUES**. After doing so, the way the GUI works is that, in order for the game to take effect for any changes done in any of the **ENVIRONMENT** submenues you have to turn it on in the **CONTROLS** submenu. Meaning that you can play around with a submenu settings and then turn it off while keeping the settings saved in case you want to use them in another scene.

For disabling the games vignette go to **ENVIRONMENT** tab and to the submenu **TONEMAP**. You should find the ticking box at the bottom. This submenu also lets you modify the exposure. To do so disable the **AUTOMATIC EXPOSURE** checkbox and play with **EXPOSURE** and **COMPENSATION** fields.

To enable the High LOD setting go to the **CAMERA** tab and click on **FIX LOD**. Timescale and shadow resolution options can be found on the **MISC/ABOUT** tab.

## Time Changer Tool Usage

Run the *MEC-TC* exe after starting the game. It will hook into it automatically.

Changing the time of day would only take effect with the game unpaused, so do that beforehand. Also, once you settle into a particular ToD you like, open the main menu and click on the "Reset Lighting" button that comes from installing [this mod](https://www.nexusmods.com/mirrorsedgecatalyst/mods/163). This will reset all of the enviroment lighting to nativly match the newly selected ToD.

## Tips and Tricks

### Disabling the Built-in Anti-Aliasing

The game uses supersampled anti-aliasing combined with temporal anti-aliasing, which can be quite performance intensive. For better performance and to be sure they don't interrupt ReShade, you can disable both forms of anti-aliasing in the game's config files found in Documents folder.

1. Start the Windows file explorer and navigate to the Documents folder which is in `%USERPROFILE%\Documents\` by default.
2. Open the Mirror's Edge Catalyst folder, and find the folder named `settings`, then look for the file titled `PROF_SAVE_profile` and open it with your preferred text editor.
3. Change both values for `GstRender.AntiAliasingDeferred` and `GstRender.AntiAliasingPost` to 0.

After doing this, it's recommended to use another form of AA through ReShade, as the game's visual design will make edges stand out more. Using SweetFX's SMAA is a good alternative.

However, do note that turning the native AA off would lead to some artifacts in the enviroment edges, so if your PC is beefy enough consider leaving this on.

### Mods for Easier Photography

Catalyst runs the game with depth of field and motion blur enabled, though you can disable motion blur in the settings, disabling the different kinds of depth of field during certain actions in game requires the use of a mod. You can use [No Visual Environment Effects](https://www.nexusmods.com/mirrorsedgecatalyst/mods/73) and [Disable Runner's Flow Color Correction](https://www.nexusmods.com/mirrorsedgecatalyst/mods/35/) to completely disable visual effects like color correction, chromatic aberration, and depth of field. These mods only disables these effects during combat and or freerunning, so you are free to manipulate them through shaders as you wish.

### Setting up Reshade's Depth Buffer

Mirror's Edge Catalyst uses a reversed depth buffer, so ReShade needs to be set up to access this properly. Open the global preprocessor definitions tab and change `RESHADE_DEPTH_INPUT_IS_REVERSED ` from 0 to 1. This allows for shaders to access depth effects, which will be mentioned in the next section.

### Misc

- Faith face texture goes low-res when reducing the FOV too much, so be careful with that.
- Third person cutscenes are pre-rendered, so no way to take shots from them.

## Optional Mods

The following mods use [Frosty's Mod Manager](https://frostytoolsuite.com/downloads.html):

* [Debug Startpoint Selector](https://www.nexusmods.com/mirrorsedgecatalyst/mods/5)
* [Better Billboards mod](https://www.nexusmods.com/mirrorsedgecatalyst/mods/76)
* [Better Screen Space Reflection view distance](https://www.nexusmods.com/mirrorsedgecatalyst/mods/110)
* [No Horizontal bloom lens reflection and vignette](https://www.nexusmods.com/mirrorsedgecatalyst/mods/97)
* [EXTENDED city](https://www.nexusmods.com/mirrorsedgecatalyst/mods/202)

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Mirror%27s_Edge_Catalyst)
