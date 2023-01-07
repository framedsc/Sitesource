![Far Cry 3](Images\farcry3.png "Shot by originalnicodr"){.shadowed .autosize}

WIP GUIDE, dont add on docnet.json yet.

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes*
Reshade | Yes*
Ansel | No
Graphics API | DirectX 11

## Tools

* [Cheat Engine table by One3rd]()  
**Features**: Freecam, FoV control, HUD toggle, timestop

* [Hud toggle](https://framedsc.com/ShaderTogglers/) requires Reshade 5+ with [Shader Toggler](https://framedsc.com/ReshadeGuides/Addons/shader_toggler_repository.htm)


@alert Important!
Select the game graphic api to dx11 in the video option for the table to work.
@end

## Controls

There are two "methods" for the cheat table to get the freecam. I suggest trying the one with `F2` by default (backup freecam on the cheat table), and when that doesnt work to use the freecam with `F1`.

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

Since we are using the gameplay controls to move the camera orientation, we wont be able to change its orientation in cutscenes.

To be able to change the cams orientation when the game is paused [disable negative mouse acceleration](https://www.pcgamingwiki.com/wiki/Far_Cry_3#Negative_mouse_acceleration).

## Tips and Tricks
Change definitions my cause crashes.

## Reshade
### Depth Buffer
The game has some faulty depth buffer detection, so you will probably have to reselect it before working on a shot.

### Shader crash
I encoutnered some crashed depending on the shader I tried to turn on after a while of starting the game (for example, I havent been able to use Cinematic DOF because of it). I have tried turning on the shaders that I want to use at least once just after starting the game to avoid crashing afterwards.

### Screenshot

I noticed that Reshade's screenshot functionality wasnt working without the menu. You have to open the menu for the screenshot to be taken.


## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Far_Cry_3)
* [Nexus Mods](https://www.nexusmods.com/farcry3) 


Scipt loader: https://discord.com/channels/846424998888734731/846426659250765894/939880964451090482
spawner: https://discord.com/channels/846424998888734731/846426659250765894/940744190160158770
https://downloads.fcmodding.com/fc3/mod-installer/
https://www.nexusmods.com/farcry3/mods/219