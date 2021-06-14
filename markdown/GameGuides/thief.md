![Thief](Images\thief.png "Shot by Originalnicodr")
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11
 
## Tools
 
* [Edited Cheat engine table by IDK31](..\CheatTables\thief_fc_1.1.CT)  
**Features**: Free Camera, FOV, Timestop, HUD toggle
 
## Controls
 
Description | Key
--|--
Toggle free camera | PageDown
Move forwards, backwards, left, right, up, down | `NumPad 8`, `Numpad 5`, `Numpad 4`, `Numpad 6`, `Numpad 9`, `Numpad 7`
Change camera orientation up, down, left, right | `NumPad +` + `Numpad 8`, `Numpad +` + `Numpad 5`, `Numpad +` + `Numpad 4`, `Numpad +` + `Numpad 6`
Increase, decrease FOV | `NumPad +` + `Numpad 7`, `Numpad +` + `Numpad 9`
Camera tilt | `NumPad +` + `Numpad 1`, `Numpad +` + `Numpad 3`
Reset tilt | `NumPad +` + `Numpad 2`
Change tilt to 90° | `NumPad +` + `Numpad .`
Disable/Enable HUD | `H`, `G`
Change game speed | `F5`-`F11` (default=`F9`)
Save current settings | ALT + [number 1 to 9]
Load current settings | ALT + [number 1 to 9]
Undo: Load previous settings | 0
Teleport | End
 
 
Don't press the 0 key without having a setting saved, otherwise the game will crash.
 
For fancy camera movement (to use in videos for instance) you can use the control below
 
Key| Description
--|--
Rotate camera up, down, left, right | `NumPad Enter` + `Numpad 8`, `Numpad Enter` + `Numpad 5`, `Numpad Enter` + `Numpad 4`, `Numpad Enter` + `Numpad 6`
Move forward,backward (cam only) | `NumPad Enter` + `Numpad 9`, `Numpad Enter` + `Numpad 7`
Dolly zoom in,out | `NumPad Enter` + `Numpad 1`, `Numpad Enter` + `Numpad 3`
Reset dolly zoom | `NumPad Enter` + `Numpad 2`
Point camera Up/Down | `Numpad 1`, `Numpad 3`
 
And finally, you can change the velocity of the camera movement, camera orientation and field of view if you hold down the keys 'C', 'F' and 'T' for slow, fast and faster change of values respectively.
 
## Engine edits
 
To improve the quality of the game you can modify the `BaseEngine.ini` file located in `\Steam\steamapps\common\Thief\Engine\Config` changing the values written below:
 
```
[MemoryPools]
FLightPrimitiveInteractionInitialBlockSize=1024
FModShadowPrimitiveInteractionInitialBlockSize=1024
 
[SystemSettings]
...
DepthOfField=False
...
AllowImageReflections=True
AllowImageReflectionShadowing=True
SkeletalMeshLODBias=-1
ParticleLODBias=-1
...
MaxAnisotropy=16
...
MaxShadowResolution=2048
...
ResX=1920
ResY=1080
//or whatever res you will be using in gameplay
...
bEnableBranchingPCFShadows=True
...
bEnableForegroundSelfShadowing=True
```
 
 
## Disabling the shroud/white flash/proxy light effects
 
There are some effects that appear when being in the shadows and in the light that can mess with your shot (and the brightness variates depending if you are in the shadow or not). To remove them follow the steps bellow.
 
1. Go to `Steam\steamapps\common\Thief\ThiefGame\CookedPCNG\`
2. Make a backup of thiefgame.u just in case
3. Download the [Unreal Package Decompressor](https://www.gildor.org/downloads) and unzip decompress.exe, put it anywhere
4. Drag thiefgame.u onto decompress.exe you should now have a new thiefgame.u in `\Steam\steamapps\common\Thief\ThiefGame\CookedPCNG\unpacked\`
5. Open `\Steam\steamapps\common\Thief\ThiefGame\CookedPCNG\unpacked\thiefgame.u` in a hex editor like [HxD](http://mh-nexus.de/en/programs.php).
 
To disable the black vignette around the screen's edge while in shadow:
```
Search for Hex-value: 00 00 00 00 00 00 00 00 00 CD CC 4C 3F 36 3D 00
Replace with Hex-value: 00 00 00 00 00 00 00 00 00 00 00 00 00 36 3D 00
```
 
To disable the screen-wide flash upon entering light:
```
Search for Hex-value: 3E 9C DE F4 3E 9C DE F4 3E CD CC CC 3E A4 3D 00
Replace with Hex-value: 3E 9C DE F4 3E 9C DE F4 3E 00 00 00 00 A4 3D 00
```
 
If you also want to disable (or edit) the brightness increase when  the character enters the shadows (which is not recommended since it would make it very difficult to discern objects in the dark) you can read about it [here](https://steamcommunity.com/app/239160/discussions/0/617328415061772742/#c617328415064759506).
 
Save and fire up the game. When you start the game, it will notify you that its using thiefgame.u in the unpacked directory and not your original one, just hit ok and the launcher should start.
 
## Tips
- If you see parts of the character start to deform when paused in cutscenes (like the hood) press h (open the menu) or advance the time a little bit (you can advance time with F6 so you advance it as little as possible).
- The pause disables particles like rain or birds, so if you want them in your shots and want the pause use a low speed like F6.
- If you move the camera in paused cutscenes you will get some kind of blur. One way to avoid this is by continuing the time a bit with low speed until the blur is gone (at the risk of having a different composition to the one you had). Alternatively, you can try rotating the camera until there is no blur and changing the tilt to 90° or reseting it to to get to the original orientation (for some reason changing the rotation of the camera quickly does not add nor take this blur).
 
 
## Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Thief)
* [Tweaks and Tips](https://docs.google.com/document/d/1KKUdephyihaoQrm7WEZ9gNbDG9WysjRirCzcuvUrLv8)
* [More Tweaks & Fixes](https://forums.thedarkmod.com/index.php?/topic/16001-thief-4-tweaks-fixes/)
 
 
 
 


