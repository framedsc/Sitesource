![RoboCop: Rogue City](Images\robocop_rogue_city_header.png "Shot by Dogmod"){.shadowed .autosize}
## Summary
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (use windowed fullscreen)
DSR | Yes
Custom Aspect Ratios | Yes  
Reshade | Yes
Ansel | No
Graphics API | DirectX 12
Game version |  <font face="Stores">S</font> 1.1.1.0

@alert neutral  
This guide is for an Unreal Engine 5 game that can use the [Universal Unreal Unlocker](https://opm.fransbouma.com/uuuv5.htm).  
@end

## Tools

* [Unreal Engine 5 Unlocker](https://opm.fransbouma.com/uuuv5.htm)  
**Features**: Camera, HUD toggle, Hotsampling, Console, Timestop, Slowmo, Custom lights, Post-processing 

All features are tested and working on the release version of the game (<font face="Stores">S</font> 1.1.1.0)

## IGCS Depth of Field quirks

Generally, IGCS Depth of Field works great with RoboCop. However, achieving extreme levels of DOF requires inputting 
**Max. bokeh size** manually in Reshade. By default, **Max. bokeh size** is capped at 10.000. For RoboCop this 
may not be enough in some cases. To input a bigger value, double click the **Max. bokeh size** number and input whatever
value you need. 

When using upscaling with IGCS Depth of Field, images may turn out blurry. To avoid this,
set **Number of frames to wait per frame** to 5. This will increase the time it takes to complete a shot, but
the focal point will be correct.

## Known issues

### Arm rig visible when camera is active

When hiding the HUD using Unreal Engine 5 Unlocker, arm rig remains visible in the scene.

To fix this, check **Toggle player visibility** in **Misc. adjustments** in Unreal Engine 5 Unlocker.

### Possible crash when issuing a ticket

If Unreal Engine 5 Unlocker is injected when issuing a car ticket in game (part of Serve and Protect side quest),
the game may throw an exception and crash.

Reloading a level from the beginning may solve the issue (using saves the game creates at the beginning of every mission).

If you don't want to reload, this can somewhat be avoided by closing Unreal Engine 5 Unlocker before issuing the ticket. 
The game will not crash right away, but injecting Unreal Engine 5 Unlocker later will cause the exception again. You can ignore the window and reach
a checkpoint to save the game, but camera tools will not work and pressing **OK** in the exception window will crash the game.

Issuing a ticket, saving, then reopening the game and injecting Unreal Engine 5 Unlocker should not crash the game.

Rarely, this crash may also occur when reinjecting Unreal Engine 5 Unlocker.

### Camera in cutscenes

Currently, you can't control the camera in cutscenes. However, camera control does work in the main menu 
and can be used for photos with full Robocop model.
