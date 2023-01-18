![Far Cry 3](Images\farcry3.png "Shot by originalnicodr"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes*
Ansel | No
Graphics API | DirectX 11

## Tools

* [Cheat Engine table by One3rd](..\CheatTables\FarCry3_Screenshooting.CT)  
**Features**: Freecam, FoV control, HUD toggle, timestop.

* [Hud toggle](../ShaderTogglers/far_cry_3.ini) requires Reshade 5+ with [Shader Toggler](https://framedsc.com/ReshadeGuides/Addons/shader_toggler_repository.htm)  
**Features**: Map, ammunition, mission information, enemy marks, enemy silhouette trough walls, and enemy attention indicator toggles.

@alert Important!
Select the game graphic API to dx11 in the video option for the table to work.
@end

## Controls

There are two "methods" for the cheat table to get the freecam. I suggest trying the one with `F2` by default (backup freecam on the cheat table), and when that doesn't work use the freecam with `F1`. Also, the game has both keys binded to opening menus in-game, so you may want to rebind those.

Command | Key
--|--
Toggle FreeCamera | `F1` / `F2`
Toggle HUD | `Numpad 0`
Pause | `P` | 
Unpause | `Shift` + `P`
Change camera orientation | `Mouse`
Move the camera in the world coordinates | `Numpad 4, 5, 6, 8` 
Move the camera downwards / upwards | `Numpad 7` / `Numpad 9`
Move the camera faster | Hold `Ctrl` while moving
Move the camera slower | Hold `Alt` while moving

Since we are using the gameplay controls to move the camera orientation, we won't be able to change its orientation in cutscenes.

To be able to change the camera orientation when the game is paused [disable negative mouse acceleration](https://www.pcgamingwiki.com/wiki/Far_Cry_3#Negative_mouse_acceleration).

Even tho the cheat table has the option to turn off the HUD, I would still suggest using the shader toggler linked above (with `Caps Lock`) since it covers more stuff than just the minimap and ammunition.

## Tips and Tricks
Change definitions on the fly may cause crashes.

## Reshade
### Depth Buffer
The game has some faulty depth buffer detection at times, so you will probably have to reselect it before working on a shot.

### Shader crash
I encountered some crashes when trying to turn on a shader for the first time after a while of starting the game (for example, turning on Cinematic DOF). I have tried turning on the shaders that I want to use at least once just after starting the game to avoid crashing afterward.

### Screenshot
I noticed that Reshade's screenshot functionality wasn't working without Reshade menu being open. So open the menu when taking a screenshot to make sure it's taken.

## Optional
* [Scipt loader](https://discord.com/channels/846424998888734731/846426659250765894/939880964451090482) from the [FarCry:Modding discord](https://discord.com/invite/B42Bqz5RQn). Use [this](https://downloads.fcmodding.com/fc3/mod-installer/) to install it. You can see the available functions and example scripts [here](https://www.unknowncheats.me/forum/far-cry/237567-cry-3-script-loader-norway-_-1999-pc.html).
* [Disabling post-processing effects separately](https://www.pcgamingwiki.com/wiki/Far_Cry_3#Disabling_post-processing_effects_separately)
* [Better HBAO](https://www.nexusmods.com/farcry3/mods/219)
* [Force HBAO+](https://www.pcgamingwiki.com/wiki/Far_Cry_3#Ambient_occlusion)

## Useful Links
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Far_Cry_3)
* [Nexus Mods](https://www.nexusmods.com/farcry3) 
