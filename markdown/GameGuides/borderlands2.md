![Borderlands 2](Images\borderlands2_header.png "Shot by Jim2point0"){.shadowed .autosize}

##Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Ansel | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Graphics API | DirectX 9

@alert important
The guide below is outdated. It's unlikely the original author will update the cheat table, so either [rollback to a previous version of the game](../GeneralGuides/steam_update_guide.htm) to use the cheat engine table linked below or try out [this new photomode mod](https://bl-sdk.github.io/mods/Photomode/) and [this cheats mod](https://bl-sdk.github.io/mods/ApplesBorderlandsCheats/).
@end
 
## Tools

* [Community CE Table](..\CheatTables\Borderlands2.CT)  
**Features**: UE3 Cheats, Freecam, Time of day, and much more. 

## Using the CE Table

When you open it, you'll see the main script `[Enable]`. Check that or press **F2** to enable most functionality.

Inside you'll see a group called "[screenshotting]." This is where the useful scripts and pointers for this guide are located.

### Unreal Engine Cheats  
Enable this script to enable native UE3 cheats. F3 will toggle this.  
Hotkeys:  

* **Numpad 1:** Playersonly (freezes everything except your player)  
* **Numpad 2:** Fly (allows your character to fly)  
* **Numpad 3:** Ghost (pass through walls)  
* **Numpad 4:** God mode

### FreeCam v4.0  
The free camera. **F5** toggles between 3rd person, free camera, fixed camera, and 1st person. 
Pressing the **middle mouse** button will reset the free camera position. Alternatively you can use **F6**, which cycles through 
the cameras in a different order.

Some keys I added while in free camera mode:  

* **ALT+O**** to move the camera really fast  
* **ALT+P** to move the camera at the default speed  
* **Page up** - move the camera straight up  
* **Page down** - move the camera straight down  

### Day\Night Time and Visibility  
This is only available on maps where the time of day progresses naturally. Use the **[ ]** keys to change it. Hold **ALT** for larger changes. **Numpad .** will toggle freezing it.

Press **ALT+V** to become invisible to enemies (they won't attack you). Press **ALT+B** to become visible again.

## Unlock the game's console
Open your WillowInput.ini file located here:  
```Documents\My Games\borderlands 2\willowgame\Config\WillowInput.ini```

Locate `[Engine.Console]` and add hotkeys to `ConsoleKey` and `TypeKey`. Example:
```
[Engine.Console]
ConsoleKey=Tilde
TypeKey=Backslash
```

Useful console commands:  
* **togglehud**  
* **fov X**  (where X is the desired FOV)

## Fix the ReShade depth buffer
By default, the depth buffer in Borderlands 2 doesn't function correctly in ReShade. To fix it, you need to open the `global preprocessor definitions` and change `RESHADE_DEPTH_INPUT_IS_REVERSED` to 0. Like in this screenshot:

![screenshot](https://i.imgur.com/21idGd2.png)
