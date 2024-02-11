![Enshrouded](\Images\enshrouded_header.png "Shot by jim2point0"){.shadowed .autosize}
##Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Ansel | No clue / who asked
Hotsampling | No*
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Graphics API | DirectX 12

\* Hotsampling works but you lose control of the window after changing the window size with SRWE. 
 
## Tools

* [CE Table by Jim2point0 and Skall](..\CheatTables\enshrouded_v1.CT)  
**Features**: Free Camera, FOV, Hud Toggle, Time of Day, Sun Position

## Using The CE Table

Start out by clicking the box next to "Read Camera." This fetches the camera address and is required for toggling the free camera. You can leave this on.

All Hotkeys can be changed (see guide on using cheat engine tables)

* **DEL** will toggle the free camera script.  
  Numpad 8 to move cam forward  
  Numpad 5 to move cam backwards  
  Numpad 4 to move cam left  
  Numpad 6 to move cam right  
  Numpad 9 to move cam up  
  Numpad 7 to move cam down  
  
* **F3** will enable FOV control. You can leave this on.  
  Numpad + to increase FOV  
  Numpad - to decrease FOV  
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

## Using higher resolutions

Hotsampling seems out of the question. Using Nvidia DSR, you can enable higher resolutions to be selected in-game. That said, selecting higher resolutions in-game will scale the the resolution internally, but will not capture at the selected res. In order to capture higher resolutions, you'll need to set your desktop resolution to the DSR res first. The nice thing is that the game updates to include your new desktop res after you change it. After changing your desktop res, swap between windowed and fullscreen in-game to update to the new res. This will also work with custom aspect ratios.


