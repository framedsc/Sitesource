![Journey](Images/journey_header.png "Shot by Smithy"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes ([see notes](#dsr))
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
 
## Tools

* [Cheat Engine Table by SkallEdit & PvPkw2](https://drive.google.com/file/d/1h6j8rHKxsrBw1t-9-dMm4I42huQNCefq/view)  
**Features**: Freecam, Timestop, FoV control 

## Controls 

Key	| Command
--|--
`Num 0` | Pause time
`Num Dec` | Resume time
`Insert` | Toggle camera
`Num 8` / `Num 5` | Move camera forward / backward
`Num 4` / `Num 6` | Move camera left / right
`Num 7` / `Num 9` | Move camera up / down
`Num 1` / `Num 3` | Roll/tilt camera
Arrow keys | Rotate camera
`Num +` / `Num -` | Change FoV

## Tips and Tricks

### Camera Control

@alert important
You will need to toggle the camera on then off at least once before all the controls work.
@end

When activated, the camera faces 180° from the player's direction. Camera movement is tied to the world space, i.e. the directions are relative to what the game world thinks is North, South, East, and West. When turning the camera, these directions will reverse. This is expected behavior. Camera rotation controls remain constant.

A gamepad can be used to control the freecam, but a keyboard can be more precise.

### Disabling Barrel Distortion and Vignette

The game uses a barrel distortion effect that causes the depth buffer to be out of alignment. Download and install this [3D Vision Fix](https://helixmod.blogspot.com/2021/04/journey.html) to disable that effect as well as the vignette effects used in some scenes.

### RealLongExposure.fx

Since the character’s clothes and certain visual effects (such as dust particles) continue moving even when paused, you can use the [RealLongExposure shader](https://framedsc.com/ReshadeGuides/RealLongExposure.htm) in ReShade to create some cool effects while time is stopped.

### DSR 

While the game supports DSR resolutions, the final image on your display may look jaggy or pixelated. It's recommended to set your desktop resolution to the same DSR value you use in-game to avoid this.

### Online Connectivity

The game may still connect you with players even with the cracked exe. Play in Steam Offline Mode.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Journey)