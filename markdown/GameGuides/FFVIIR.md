![Final Fantasy VII Remake](Images\ffviir_header.png "Shot by Otis_Inf"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Ansel | No
Hotsampling | No
DSR | Yes ([see notes](#dsr))
Custom Aspect Ratios | No
Reshade | Yes
Graphics API | DirectX 11 and DirectX 12
 
## Tools

* [Universal Unreal Engine Unlocker v4.1.7 or later by Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Camera, FoV, timestop, gamespeed, custom lights.

* [Cheat table by Otis_Inf and Skall](https://patreon.com/Otis_Inf)  
**Features**: HUD toggle, DoF control, Wider FoV during gameplay, control over some CVars. This table is available on Otis_Inf's patreon. 

* [FFVIIHook by emoose](https://www.nexusmods.com/finalfantasy7remake/mods/74)  
**Features**: Enables console and [use of WindowsNoEditor .ini files](./../GeneralGuides/ue4guide.htm#engine-renderer-settings).

## Characteristics

### Custom lights with the UUU

The UUU allows you to create custom lights in the game. The lights might not be visible at first, because the default light intensity is very low (20). To see the light, increase the intensity of the light by a lot (like into the millions a lot). To be able to set a higher value for the light intensity, you might also want to increase the light intensity max value. 

Most features of the UE4 lights work, pay close attention to the inner cone width, which is often set to the same value as the outer cone width, giving a hard edge to the light. 

A very low shadow bias (near 0) might be required for shadows to show up.

@alert info
In some areas, like certain rooms, it might be lights don't work; no matter how high you set the intensity, no light will appear. 
@end

### DoF Control

The cheat table allows you to control the DoF *when it's enabled in-game*. So when the DoF is visible in-game, like in a cutscene, you can control it with the cheat table. `Ctrl-F1` toggles the control over the in-game DoF in that situation. It won't turn on the DoF in gameplay however if it's not already enabled by the game. If you want to have DoF in gameplay, you have to use Reshade DOFs. 

#### Updating the DoF values when the game is paused

The UUU has two pause functions: `Numpad 0` (UWorld pause) and `PageDown` (Slowmo pause). For Final Fantasy VII Remake, both are usable, however when you want to control the in-game DoF, `PageDown` is preferable: when you pause the game using `Numpad 0` and change the DoF values using the cheat table, nothing happens till you skip a frame, using `PageUp`. When you pause the game with `PageDown` however, changing the DoF values will show immediately effect and you can easily control where to set the focal point.

### Pausing the game

To pause the game to take shots, always try to use `PageDown` first. This only goes wrong when you move your character in some situations, like in combat. In that case, the `Numpad 0` pause works better. 

## Features of the UUU that aren't supported

- No hotsampling. None at all. You can only DSR up to 4K.
- No console input. While the UUU does activate the UE4 dev console, keyboard input isn't reaching the console if the key is used by the game, e.g. enter. This is solved with FFVIIHook, which allows you to use the console normally.
- No HUD toggle. The HUD is made with a 3rd party library and the UUU can't hide it. To hide the HUD, use the cheat table's HUD toggle or [ShaderToggler](./../ReshadeGuides/Addons/shader_toggler_repository.htm). 
- (*v4.4.0 and above*) Limited control over in-game post-processing using the *Post-processing* tab.

#### UUU Ultrawide

The UUU can enable ultrawide support in UE4 games, however this doesn't work as expected in FFVIIR due to the strict 16:9 limitation. If you run an ultrawide monitor, upon injecting the UUU, your game will become squished. It can be unsquished by choosing a 16:9 hotsampling resolution.

## DSR

**Borderless Fullscreen DSR by default** - with an option to set resolution scaling as a percentage of the current screen resolution. Use this option to increase image quality of screenshots (this will not affect the final size of the screenshot). 

It is possible to force exclusive fullscreen with FFVIIHook, the game set to run in DX11 mode, and a modified `Engine.ini` with this line: `r.SetRes=3840x2160f`. Appending `f`, `wf` or `w` at the end of the specified resolution forces fullscreen, borderless fullscreen and windowed modes respectively.

Additionally, launching the game with `r.SetRes=3840x2160` causes the game to start at 3840x2160, no matter your current desktop resolution. You can then use a tool like SRWE and downscale the window to fit within your monitor. This allows you to capture 4K shots without needing to DSR your entire desktop. 

Despite `r.ScreenPercentage` being exposed by the cheat table and FFVIIHook, it seems that setting it higher than an internal resolution of 4096 causes bright green artifacts to appear.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Final_Fantasy_VII_Remake_Intergrade)
* [Change or summon non-mainline characters](https://www.nexusmods.com/finalfantasy7remake/mods/92) (Nexus Mods)
