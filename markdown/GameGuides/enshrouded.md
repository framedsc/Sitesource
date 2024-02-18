![Enshrouded](\Images\enshrouded_header.png "Shot by jim2point0"){.shadowed .autosize}
##Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Ansel | No clue
Hotsampling | No*
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Graphics API | DirectX 12

\* Hotsampling works but you lose control of the window after changing the window size with SRWE. 
 
## Tools

* [CE Table by Jim2point0 and Skall](..\CheatTables\enshrouded_v3.CT)  
**Features**: Free Camera, Timestop, FOV, Hud Toggle, Time of Day, Sun Position, and some extra visual options

## Using The CE Table

Start out by clicking the box next to "Read Camera." This fetches the camera and FOV addresses and is required for enabling the photomode. You can leave this on.

Some hotkeys can be changed (see guide on using cheat engine tables)

Currently there is no controller support, though it is planned for the future. For now, You must use a mouse to look around.  

* **Numpad 0** will toggle the photo mode. The game will pause and the freecam will be enabled. If you have an xbox controller turned on, you can use that. Otherwise it will fallback to keyboard controls.  
  ### Controller
  Dpad up/down to change FOV  
  Left/Right trigger to move up and down  
  Y = fast movement  
  A = slow movement  
  ### Keyboard
  WASD to move the camera  
  Space/Control to move up and down  
  Left ALT for slow movement  
  Arrow keys to rotate the camera  
  Numpad + and - to increase/decrease FOV  

* **DEL** toggle the HUD

* **F4** will enable time of day control. This allows you to manually change the normal day cycle with hotkeys.  
  [ ] keys = increase/decrease time of day  
  hold CTRL to move slower  

* **F5** will enable sun position control. Allows you move the sun more freely (not bound to the usual time of day track)  
  Arrow keys to move the sun  
  ↑   move sun up  
  ↓	move sun down  
  →	move sun right  
  ←	move sun left  
  hold CTRL to move slower

### Extras
The old version of the camera and FOV script are still here in case you don't have a controller and want to be able to use the mouse. But this camera will not work with the new pause. 

The offset camera allows you to change the default distance the camera sits from the player. Experiment with the values here to get an off-the-shoulder cam, or change everything to 0 for a first person camera (works surprisingly well).

## Using higher resolutions

Using Nvidia DSR, you can enable higher resolutions to be selected in-game. That said, selecting higher resolutions in-game will scale the the resolution internally, but will not capture at the selected res. 

In order to capture higher resolutions, you'll need to set your desktop resolution to the DSR res first. The nice thing is that the game updates to include your new desktop res after you change it. After changing your desktop res, swap between windowed and fullscreen in-game to update to the new res. This will also work with custom aspect ratios like 3:4.

## ReShade, depth of field, etc

You'll need to manually select the depth buffer in order to get depth shaders working. What seems to work best is disabling reshade first, selecting one of the top depth buffers with the most writes, and then enabling reshade again. 