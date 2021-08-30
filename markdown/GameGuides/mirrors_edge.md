![Mirror's Edge](Images\mirrors_edge.png "Shot by Barkar B"){.shadowed}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
DirectX versions | DirectX 9
 
## Tools
 
* [Freecam by IDK31](..\CheatTables\MirrorsEdge_freecam0.02.CT)  
**Features**: Free Camera, FOV, Slowmotion, HUD toggle, tonnemapping, DOF, and more effects.
* [Console mod](https://www.moddb.com/games/mirrors-edge/addons/windowed-mode-and-console)
## Usage
 
Once you load the cheat engine table you will need to click the boxes of the loaded table the features you want to use for using them.
 
## Controls
 
Description | Key
--|--
Toggle free camera | PageDown
Move forwards, backwards, left, right, up, down | `NumPad 8`, `Numpad 5`, `Numpad 4`, `Numpad 6`, `Numpad 9`, `Numpad 7`
Change camera orientation up, down, left, right | `NumPad +` + `Numpad 8`, `Numpad +` + `Numpad 5`, `Numpad +` + `Numpad 4`, `Numpad +` + `Numpad 6`
Increase, decrease FOV | `NumPad +` + `Numpad 7`, `Numpad +` + `Numpad 9`
Camera tilt | `NumPad +` + `Numpad 1`, `Numpad +` + `Numpad 3`
Reset tilt | `NumPad +` + `Numpad 2`
Change game speed | `F5`-`F11` (default=`F9`)
 
To toggle the HUD you can use the table directly, but since it doesn't have a hotkey attached you can go to the file `TdInput.ini` located at `C:\Users\YourUser\Documents\EA Games\Mirror's Edge\TdGame\Config` and add the following line just below `bEnableMouseSmoothing=true`:
 
```
Bindings=(Name="H",Command="Showhud",Control=False,Shift=False,Alt=False)
```
 
The cheat engine table has some extra stuff, like DOF control and tonemapping if you are interested in that.
 
## Engine edit
 
As with other Unreal Engine 3 games, you can edit the `TdEngine.ini` file located at `C:\Users\User\Documents\EA Games\Mirror's Edge\TdGame\Config` to "enhance a couple of things. Below there is a couple of values you can change, but feel free to look up engine edits from other games to try it here or play around with different values:
 
```
ShadowFilterRadius=5
...
[MemoryPools]
FLightPrimitiveInteractionInitialBlockSize=1024
FModShadowPrimitiveInteractionInitialBlockSize=1024
```
 
## How to change definitions
 
The game doesn't hotsample, however you can use the console to change to another definition without needing to go to the menu. Make sure that you are playing fullscreen and have the PsycsX option turned off in the video menu, otherwise it will brick the game every time you alt-tab or change resolutions.
 
To be able to use the console with the tilde key you will need to set up your keyboard language to English (United States).
 
To change definitions use the command `setres XxY` in the console, where X is the width and Y is the height of the definition to use. You can also set up a hotkey for resolutions in the `TdInput.ini`:
 
```
Bindings=(Name="Y",Command="setres 3840x2160",Control=False,Shift=False,Alt=False)
```
 
Bare in mind that you can only use definitions that can be selected in the graphics options, so [set up your DSR definitions](https://framedsc.github.io/GeneralGuides/custom_dsr_resolutions.htm) if you haven't done so yet. These commands can also be assigned to hotkeys in the `TdInput.ini` file, if you have troubles using the console.
 
It's worth mentioning tho that, since the game uses a pre-baked shadowmap, it means that it is not being calculated in real time, so using the command tildeshot ("tildeshot n" will take a shot of the game, which resolution would be n times the resolution the game is running) might be more viable for getting highdefinition shots than in other games, the downside of that would be not being able to use reshade in the shot. These shots are stored in `C:\Users\User\Documents\EA Games\Mirror's Edge\TdGame\ScreenShots`.
 

 
## More useful commands
 
- `suicide`: Somtimes, if you activate the freecam when there are enemies in the level, the camera will show they pov after turning off the freecam. In these cases you have no choice but to use a command like this to restart from the last checkpoint. 
- `god`: So if you get hit your vision won't get obscured and you won't be forced to restart from the last checkpoint before finishing with a shot.
- `killbots`: If you want to kill all the enemies in a section so they don't bother you.
- `SHOW DYNAMICSHADOWS`: Toggle Dynamic Shadows.
- `SHOW POSTPROCESS`: Switches post processing on and off. That's basically color and contrast correction. It might be useful in certain scenes.
 
[List of commands](https://pastebin.com/wNzxR0By)
 
## Tips
 
- The game doesn't technically have a pause option, just slowing time a lot. If you already have the composition but want to play with reshade, opening the console will pause the game. So you can set up a shot, open the console, set up canvasfog or cinematicdof in reshade, change resolutions with the console, close the console and take the shot.  
## Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Mass_Effect:_Andromeda)
* [Maps and other mods](https://www.moddb.com/games/mirrors-edge/addons)
* [Maps and time trials](https://www.reddit.com/r/mirrorsedge/comments/417khh/01152015_updated_mods_list/)
* [Mirror's Edge Mod Archive](https://archive.org/details/mirrorsedge_modarchive)
* [Cheat table with Free Roam, teleport and more](https://fearlessrevolution.com/viewtopic.php?t=15343)
* [Alternative console](https://github.com/btbd/mmultiplayer)
* [Mirror's edge modding discord](https://discord.com/invite/gV8QW6F)
