![Prey](Images\prey.png "Shot by originalnicodr"){.shadowed .autosize}
## Summary
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No 
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
Game version | </font> <font face="Stores"> S </font> 1.0.1.0 [*](#notes)
 
## Tools

* [Chairloader by thelivingdiamond](https://github.com/thelivingdiamond/Chairloader/releases)  
**Free Features**: 
Free camera, console, entity editor and spawner, and more.
* [HUD toggle](../ShaderTogglers/prey.ini) requires Reshade 5+ with [Shader Toggler](https://framedsc.com/ReshadeGuides/Addons/shader_toggler_repository.htm).

## Installation

- Install Reshade 5+ with addon support. Then follow the guide [here](https://framedsc.com/ReshadeGuides/Addons/shader_toggler_repository.htm) to install the Shader Toggler addon and the HUD toggle .ini above.
- After following the installation instructions, open Chairloader, click on the "options" button on the lower right, and enable "Load Chariloader", "Load Editor" and "Dev Mode".
- Launch the game from the Chairloader.

## Usage

Feature | Key
--|--
Turn on freecam | F4
Pause | P
Allows camera movement | Right Mouse Click
Camera orientation | Right Mouse
Move forward, backward, left, right | W, A, S, D (while right mouse click) 
Move up, down | Q, E (while right mouse click)
Faster movement | Shift
HUD toggle | Caps Lock

## Console

To open the console press `F1` to bring the mod menu, and click "Chairloader" on the top left, "Show Console".

If you want to change the FOV of the editor freecam enter the command `ed_ViewFov X` where X is the new fov value you want to use.

In this console you can also modify the speed of the freecam with the `ed_ViewMaxSpeed` and `ed_ViewMinSpeed` CVars.

For more CVars and commands you can dump the available ones by going to the mod menu, clicking on the Console menu, and then clicking on "Dump Commands to the console" and "Dump CVars to file".

## Notes

- It is recommended to load your save after a screenshoting session just in case messing with the editor caused some kind of problem to your save (soft blocking, save corruption, etc.).

- [Real Lights plus Ultra Graphics Mod](https://www.nexusmods.com/prey2017/mods/22), at the time of writing is not compatible with Chairloader. Even after following [these instructions](https://forums.nexusmods.com/index.php?showtopic=12760767/#entry123085836). It will load but it won't look good (excessive exposure of some lights, no real-time shadows, wrong materials for glass). I would suggest looking up if someone made the mod compatible with Chairloader, but in the meantime, I would suggest against using this.

- Even tho I tested this on the latest version on Steam, the mod patches the .exe to be like the one in the Epic Game Store, so this guide should function equally no matter the store.

- The editor allows a ton of freedom, like spawning enemies and NPCs, moving objects around, and more. Feel free to play around with it and collaborate with this guide if you feel like it!

- Beware of not leaving the in-game mouse visible. You can put it over one of the mod menu elements (which will be hidden with the HUD toggle) or outside of the screen.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Prey_(2017))
