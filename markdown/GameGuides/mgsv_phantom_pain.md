![Metal Gear Solid V: The Phantom Pain](\Images\phantom_pain.png "Shot by Originalnicodr"){.shadowed .autosize}

[//]: #\Images\phantom_pain.png

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes ([see notes](#reshade))
Ansel | No
Graphics API | DirectX 11
 
## Tools

* [Camera tools by Otis and Jan Schatter](https://github.com/FransBouma/InjectableGenericCameraSystem/tree/master/Cameras/MGS5)  
**Features**: Free Camera, FOV, Timestop, HUD toggle, DOF control, time of day and weather control.

## Controls

Key	| Command
--|--
`CTRL` + `INS` | Toggle GUI
`CTRL` + Mouse wheel | Resize GUI
`INS` | Toggle freecam
`HOME` | Lock / unlock camera
Mouselook / Arrow keys / <font face="Controller">></font> | Rotate camera
`Num 8` / `Num 5` / <font face="Controller"><</font> | Move camera forward / backward
`Num 4` / `Num 6` / <font face="Controller"><</font> | Move camera left / right
`Num 7` / `Num 9` / <font face="Controller">{ / }</font> | Move camera up / down
`Num 1` / `Num 3` / <font face="Controller">A / D</font> | Tilt camera left / right
`Num +` / `Num -` / <font face="Controller">W / X</font> | Increase / decrease FoV
`Num *` / <font face="Controller">b</font> | Reset FoV
`ALT` / <font face="Controller">y</font> | Faster movement modifier
`R-CTRL` / <font face="Controller">x</font> | Slower movement modifier
`Num 0` | Pause game ([see notes](#timestop))
`ALT` + `H` | Show help

## Tips and Tricks

### Timestop

Timestop is implemented in the camera tools as `Num 0`. This timestop works during normal gameplay and during cutscenes. It's the same timestop as pausing the game, but without showing the menu. This means that to unpause the game, you have to use the menu show/hide keys (`ESC` or the menu button on controller).

### Depth of field

In the camera menu (`CTRL` + `INS`) you'll find in-game DoF controls. These controls work when the camera is enabled. 

### Time of Day and Weather control

In order to effectively control time of day and weather, the game must be unpaused and the camera must be enabled, otherwise the game's values are overwriting your changes. This is done to avoid you configuring things which could have a negative effect on gameplay. 

### Reshade

To be able to use Reshade in the game you will need:
 
* [DXVK](https://github.com/doitsujin/dxvk/releases/tag/v1.8.1) (drop the DLLs from the x64 directory into the game's root dir), which will convert DirectX to Vulkan (v1.8.1 was suggested, but feel free to try a newer version).
* Install Reshade as Vulkan globally (the second button on Reshade's installer).
 
Other methods for using Reshade in the game involve defocusing the game's window when the game is being initialized, but the method described above seems to work well. Overlays (Steam, Afterburner, etc.) also work fine with this method.

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Metal_Gear_Solid_V:_The_Phantom_Pain)
* [Infinite Heaven mod](https://www.nexusmods.com/metalgearsolidvtpp/mods/45) (Nexus Mods)
* [Post-processing mod](https://www.nexusmods.com/metalgearsolidvtpp/mods/406/) (Nexus Mods)
* [Anti-Aliasing Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1210727595) (Steam Community)
