![Ashen](Images\ashen_header.png "Shot by Natty Dread"){.shadowed .autosize}

##Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Ansel | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Graphics API | DirectX 11
 
## Tools

* [Console Unlocker by Sunbeam](http://fearlessrevolution.com/viewtopic.php?t=8410)  
**Features**: Unlocks the UE4 console in order to enter commands\cheats

## Useful Console Commands

### Gameplay \ Screenshots

* **ToggleDebugCamera**  
Enables the UE4 free camera
* **TeleportToDebugCamera**  
Teleports your character to the current camera location  
* **FreezeFrame**  
Freezes the game
* **FreezeFrame 1000**  
Unfreezes the game (resumes normal game speed)
* **slomo 0.5 \ slomo 1.0**  
Slow motion \ Normal game speed

### Rendering
* **r.SceneColorFringeQuality 0**  
Disables chromatic aberration
* **r.AmbientOcclusionRadiusScale 0.02**  
Better AO
* **r.EyeAdaptationQuality 0**  
**r.DefaultFeature.AutoExposure 0**  
Disables auto exposure  
* **r.ScreenPercentage**  
Dynamic resolution scaling  
* **r.MipMapLODBias**  
Global texture mipmap override  
* **r.BloomQuality 0**  
Disable bloom  
* **r.DefaultFeature.LensFlare 0**  
Disable lensflare
* **r.DepthOfFieldQuality 0**  
Disable ingame DoF
* **r.Fog 0**  
Disable fog

##Tips and Tricks

### Quickly enter console commands
There is seemingly no way to bind commands to keys using the console. If you want to freeze the game, you need to open the console and type out "FreezeFrame" or scroll up to a previously entered command and press enter.

You can use any macro software in order to create macros to open the console, type the commands, and close the console all in a split second. You can chain several commands in a single macro if you're constantly entering the same commands every time you launch the game.

Otherwise, keep the commands handy in a notepad file for quickly copy\paste. Especially for the rendering commands you want. 

### Retrieve game default values

If you put a command into the console without a value (r.AmbientOcclusionRadiusScale) you can see the default value the game uses. Useful for when you want to reset your tweaks without restarting the game.