![Titanfall 2](\Images\titanfall2.png "Shot by Phoenix")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | No
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [Camera tools by Otis](https://github.com/FransBouma/InjectableGenericCameraSystem/tree/master/Cameras/Titanfall2)  
**Features**: Free camera, FOV, Timestop and DOF control.

* [Hud toggle by The Janitor](http://www.moddb.com/games/titanfall-2/downloads/toggle-hud5)
Follow the instructions on the text file to install.

## Usage

1. Extract files wherever you want
2. Start the game as admin
3. Inject the camera AFTER you've loaded a level. It relies on the engine object which isn't known at startup
4. A console window should appear with some text confirming everything's OK

## Controls

- Ctrl-INS                              : Open / close in-game main menu
- Ctrl-Mouse wheel                      : Resize font
- INS                                   : Enable/Disable camera
- DEL                                   : Toggle first/third person (not when camera is active)
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
- Numpad 0                              : Toggle game pause
- Numpad .                              : Block input to game for camera control device

- Caps lock                             : Toggle HUD (with the HUD toggle mod installed)


## Depth buffer in ReShade
For some reason the game needs to have in-game dynamic resolution enabled for depth buffer to work properly. Alternatively you can use the engine DoF 
which can be controlled from the camera tools.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Titanfall_2)