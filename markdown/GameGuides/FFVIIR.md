![Final Fantasy VII Remake](Images\ffviir_header.png "Shot by Otis_Inf"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Ansel | No
Hotsampling | No
DSR | Yes*
Custom Aspect Ratios | No
Reshade | Yes
Graphics API | DirectX 11 and DirectX 12
 
## Tools

* [Universal Unreal Engine Unlocker v4.1.7 or later by Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Camera, fov, timestop, gamespeed, custom lights.

* [Cheat table by Otis_Inf and Skall](https://patreon.com/Otis_Inf)  
**Features**: Hud toggle, DoF control, Wider FoV during gameplay, control over some CVars. This table is available on Otis_Inf's patreon. 

## Characteristics

### Custom lights with the UUU
The UUU allows you to create custom lights in the game. The lights might not be visible at first, because the default light intensity is
very low (20). To see the light, increase the intensity of the light a lot. To be able to set a high value for the light intensity you might also want
to increase the light intensity max value. 

Most features of the UE4 lights work, pay close attention to the inner cone width, which is often set to the same value as the outer cone width, giving a 
hard edge to the light. 

@alert info
In some areas, like certain rooms, it might be lights don't work; no matter how high you set the intensity, no light will appear. 
@end

### DoF Control
The cheat table allows you to control the DoF *when it's enabled in-game*. So when the DoF is visible in-game, like in a cutscene, you can control
it with the controls in the cheat table. `Ctrl-F1` toggles the control over the in-game DoF in that situation. It won't turn on the DoF in gameplay however if it's not
already enabled by the game. If you want to have DoF in gameplay, you have to use reshade. 

#### Updating the DoF values when the game is paused
The UUU has two pause functions: `Numpad 0` (UWorld pause) and `PageDown` (Slowmo pause). For Final Fantasy VII Remake, both are usable, however when you
want to control the in-game DoF, `PageDown` is preferable: when you pause the game using `Numpad 0` and change the DoF values using the cheat table, nothing
happens till you skip a frame, using `PageUp`. When you pause the game with `PageDown` however, changing the DoF values will show immediately effect and you can
easily control where to set the focal point.

### Pausing the game
To pause the game to take shots, always try to use `PageDown` first. This only goes wrong when you move your character in some situations. In that case press `Numpad 0` to pause. 

## Features of the UUU that aren't supported

- No hotsampling. There's no hotsampling support of any kind. The game is also running into issues with resolutions higher than 4K. 
- No console input. While the UUU does activate the UE4 dev console, keyboard input isn't reaching the console if the key is used by the game, e.g. enter. 
- No hud toggle. The hud is made with a 3rd party library and the UUU can't hide it. To hide the hud, use the cheat table's Hud toggle. 

## DSR

**Borderless Fullscreen DSR only** - with an option to set resolution scaling as a percentage of the current screen resolution. Use this option to increase image quality of screenshots (this will not affect the final size of the screenshot).

You cannot save screenshots any higher than your current desktop resolution, regardless of the resolution set in the in-game options. Make sure your desktop resolution matches the size you wish your screenshots to be.

### Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Final_Fantasy_VII_Remake_Intergrade)
* [Change or summon non-mainline characters](https://www.nexusmods.com/finalfantasy7remake/mods/92)
