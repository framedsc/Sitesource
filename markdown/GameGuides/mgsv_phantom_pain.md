![Metal Gear Solid V: The Phantom Pain](\Images\phantom_pain.png "Shot by Originalnicodr")

[//]: #\Images\phantom_pain.png

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes (read description)
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [Camera tools by Otis and Jan Schatter](https://github.com/FransBouma/InjectableGenericCameraSystem/tree/master/Cameras/MGS5)  
**Features**: Free Camera, FOV, Timestop, HUD toggle, DOF control, time of day and weather control.

## Usage

1. Extract files where ever you want
2. Start the game
3. Launch the tools as admin
4. A console window should appear with some text confirming everything's OK

## Controls

- Ctrl-INS                              : Open / close in-game main menu
- Ctrl-Mouse wheel                      : Resize font
- INS                                   : Enable/Disable camera
- HOME                                  : Lock / unlock camera movement
- ALT + rotate/move                     : Faster rotate / move
- Right-CTRL + rotate/move              : Slower rotate / move
- Controller Y-button + l/r-stick       : Faster rotate / move
- Controller X-button + l/r-stick       : Slower rotate / move
- Arrow up/down or mouse or r-stick     : Rotate camera up/down
- Arrow left/right or mouse or r-stick  : Rotate camera left/right
- Numpad 8/Numpad 5 or l-stick          : Move camera forward/backward
- Numpad 4/Numpad 6 or l-stick          : Move camera left / right
- Numpad 7/Numpad 9 or l/r-trigger      : Move camera up / down
- Numpad 1/Numpad 3 or d-pad left/right : Tilt camera left / right
- Numpad +/- or d-pad up/down           : Increase / decrease FoV
- Numpad * or controller B-button       : Reset FoV
- Numpad 0                              : Pause game. Press ESC twice to unpause (through menu)
- ALT+H                                 : Help

Timestop
========================
In the camera tools, one timestop is implemented, as Numpad 0. This timestop works in-game during normal gameplay and during cutscenes.
It's the menu timestop without showing the menu. However as I couldn't find a toggle switch for it, (resetting it to the old value leaves the
game paused) you have to use the menu show/hide keys to unpause the game, which is ESC or the menu button on the controller. 
So TL;DR: to pause the game: press Numpad 0. To then unpause the game after that, press ESC (will show the menu) and again ESC
(to get rid of the menu and continue the game). Easy.

DoF
========================
In the camera menu (Control+INS) you'll find DoF controls. These controls work when the camera is enabled. 

Time of Day and Weather control
==========================================================
In order to efectivly control time of day and Weather the game must be unpaused and the camera must be enabled, otherwise the game's values are overwriting your changes. This is done to avoid you configuring things which have a negative effect on gameplay. 

## Reshade

To be able to use reshade in the game you will need:
 
* [DXVK](https://github.com/doitsujin/dxvk/releases/tag/v1.8.1) (drop the DLLs from the x64 directory into the game's root dir), which will convert DirectX to Vulkan (v1.8.1 was suggested, but feel free to try a newer version).
* Install Reshade as Vulkan globally (the second button on Reshade's installer).
 
Other methods for using reshade in the game involve defocusing the games window when the game is being initialized, but the method described above seems to work well. Overlays (Steam/Afterburner/etc) also work fine with this method.

## Useful Links

* [Infinite Heaven mod](https://www.nexusmods.com/metalgearsolidvtpp/mods/45)
* [Post-processing mod](https://www.nexusmods.com/metalgearsolidvtpp/mods/406/)
* [Anti-Aliasing Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1210727595)
* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Metal_Gear_Solid_V:_The_Phantom_Pain)