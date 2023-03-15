![Inside](Images\inside_header.png "Shot by cHota gAbbar"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes (through Desktop)
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
Game version | <font face="Stores"> E </font> <font face="Stores"> S </font> 5.0.4

## Tools

* [Free cam by Abarichello](https://github.com/abarichello/inside-noclip)  
  This Cheat Engine table works with the **Steam** <font face="Stores"> S </font> version. It unlocks the camera and allows it to move freely in the game's 2.5D space. Clone the repository or zip and extract to download the files. Follow the instructions on the Github page to use the tool. Below is a basic summary of the flow:-

  1. Open the CET and attach it to the game's executable process.
  2. In the CET, click on *Activate Mono Features* in the *Mono* tab.
  3. Use the *tilde* (`~`) key to toggle the freecam. Toggling off the freecam brings the camera back to its original position.
  4. On pressing `~`, a screen will pop up showing the Lua output everytime you press the key. In that window, go to *View* and uncheck *Show on print*.
  5. Use the following keys to control the camera:
      * `Numpad +/-`: Camera Zoom In/Zoom Out / X Position
      * `-/=`: Camera Fast Zoom In/Out / X Position
      * `Numpad 2/8`: Camera Y Coordinates
      * `Numpad 4/6`: Camera Z Coordinates
      * `Numpad 1/3`: Camera Pitch
      * `Numpad 7/9`: Camera Yaw

@alert info
Although the camera movement is quite smooth, it has a bit of inertia and continues to move slightly even after the key is no longer being pressed. As a result, it lacks the finegrain control of the CET below.
@end

* [Camera unlocker by IDK31 and One3rd](..\CheatTables\INSIDE_Epic_Store_V1.0.CT)  
  This Cheat Engine table works with both the **Steam** <font face="Stores"> S </font> and the **Epic Games Store** <font face="Stores"> E </font> versions. Compared to the previous table, this one has finer camera control and even allows the player to pause the game and disable the Main Menu HUD. A basic summary of the flow is:-

  1. Open the CET and attach it to the game's executable process.
  2. In the CET, click on *Activate Mono Features* in the *Mono* tab.
  3. While in-game, toggle the Main Menu once. Then press `Caps Lock` and wait for the script to be enabled. Now upon pressing `ESC`, the Main Menu is no longer visible and the game will be paused.
  4. Enable the freecam script (you may add a hotkey to toggle this) and use the following keys to move the camera:
      * `Numpad 2/8`: Y axis
      * `Numpad 4/6`: X axis
      * `Numpad 3/9`: Z axis
      * `Arrow keys`: X/Y axis rotation
  5. Pressing `ESC` again will unpause the game and bring the camera back to its original position.

@alert warning
Keeping the freecam script enabled during gameplay will result in the camera being jittery.
@end

## Notes

The in-game resolution settings caps out at your desktop resolution. If you want to play at higher resolutions (like 4K), set your desktop resolution to the corresponding value; only then the in-game settings show the higher resolutions.

## Useful links

* [PC Gaming wiki](https://www.pcgamingwiki.com/wiki/Inside)