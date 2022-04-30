![Mad Max](Images\MadMax_header.png "Shot by One3rd"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (DX11)
Ansel | No
Graphics API | DirectX 11
Game version | 1.0.3.0

## Tools

* [Cheat Engine Table](..\CheatTables\MadMax_v2.0.CT)  
**Features**: Photo Mode Camera range, FOV Control, Custom Aspect Ratios, Timeflow control, Function call handler, Cheats  
* [Hud Removal Tool](https://mega.nz/file/uVxVyZib#5U_JlrGKMKnpO1WRGdAu9EHUZspNHND_UApznFVDx8c)  
**Features**: Ingame and Photo Mode toggle, screen effects toggle, Distant DOF removal

## Controls 

Key	| Command
--|--
`X`+`C` or <font face="Controller">< + ></font> | Ingame Photo Mode (can also access through pause menu)
`F1` | Toggle Photo Mode FOV control
`Num +` / `Num -` | Increase / decreas FOV
`F2` | Unlock aspect ratio
`F3` | Infinite Fuel / scraps
`F4` | Infinite health for Max 
`F5` | Enable Timeflow script, press again to stop time (Timeflow = 0.01)
`ALT`+`F5` | Normal time (Timeflow = 1)
`CTRL`+`F5` | Timeflow = 0.1 
`SHIFT`+`F5` | Timeflow = 0.5
`F6` | Timeflow = 0.001 
`F7` | Timeflow = 0.1
`F8` | Timeflow = 0.5
`CAPS LOCK` or <font face="Controller">></font> | Toggle HUD
`Num 1` | Toggle broken glass screen effects
`Num 2` | Toggle fight effects such as sparks, outlines and distortion waves

## Tips and Tricks

### Function Call Handler

The function call handler script can be used to run specific game functions to change the weather, time of day, call storms, spawn cars, change camera, run cheats, etc...

To use the function call handler enable the script, paste the function you want to call into the value of the `stringArg` field then press <code>&#96;</code> to run the function. The functions can also be selected from the `stringArg` dropdown or set with some pre-defined key binds, some of the more useful ones in the table below.

@alert tip  
Make sure to enable the function call handler script *before* using any of the function keybinds. The game may crash otherwise.
@end

Key	| Function Call Command
--|--
`Num 1` | Clear weather
`Num 2` | Heavy clouds
`Num 3` | Overcast clouds
`Num 4` | Storm trigger (same as thunderstorm?)
`ALT`+`Num 4` | Storm stop
`Num 5` | Sandstorm trigger
`ALT`+`Num 5` | Thunderstorm trigger
`Num 6` | Set current time to midday
`ALT`+`Num 6` | Set current time to midnight
`Num 7` | Disable enemy AI
`ALT`+`Num 7` | Enable enemy AI
`Num 9` | Kill everyone in local proximity
`CTRL`+`SHIFT`+`1` | Set signature car invulnerable
`CTRL`+`SHIFT`+`2` | Refill player health
<code>&#96;</code> | Run Set Function Call command

For a complete list of the available functions see the `Table Extras` section in the CE table. These notes have been copied and pasted from the original source table.

### Time Of Day
The time of day can be changed by advancing it quickly to get to the time or sun position that you want. Going back in time causes temporal issues and should be avoided at all costs.

Key	| Command
--|--
`SHIFT`+`=` | Toggle Time of Day script
`]` | increase time multiplier by 2 (this stacks)
`[` | set TOD advancedment to 0
`SHIFT`+`[` | set TOD advancement back to default of 0.0333

### DOF removal
Installing the HUD Toggle also removes the in-game near and far DOF blur. If you want to re-enable the DOF blur, go to the `ShaderFixes` folder and delete the `a0c74b6c6279d9d1-cs.txt` file.

### Remove Vignette
To remove the ingame vignette effect edit the `settings.ini` file in the game folder. Under the [Graphics] section change `EdgeFade=1` to `EdgeFade=0`.

### Using Video Capture Mode for Motion Blur
The built-in Photo Mode has a Video Mode feature that is enabled when two controllers are connected. The second controller is then used to control the in-game camera while the first controller (or KB and Mouse) control the car and Max. This [video](https://youtu.be/uOFPcWvuXSA?t=290) can help describe the feature further.

The workflow for this was to:
1. Set Timeflow to 0.01 (press `F5` twice)
2. Go into `Photo Mode` (`X`+`C` or <font face="Controller">< + ></font>), set the filter, position the camera where you want it anchored
3. Go into `Video Mode` (`R` or <font face="Controller">Y</font>) then Begin Session (`ENTER` or <font face="Controller">A</font>)
4. Review the Capture Video notes and buttons. Press `ENTER` again.
5. As soon as you are in Video Capture Mode press <font face="Controller">A</font> on the second controller to anchor the camera in it's current position. The camera will follow the car or Max.
6. Set Timeflow to 0.1 (`F7`), start long exposure, wait 1s - 2s or longer and stop the long exposure. Take screenshot.
7. Set Timeflow back to 0.01 (`F5`) to freeze things in place in case you need to redo the shot.

![Video Capture Mode](Images\MadMax_CaptureVideo.png "The controls for Video Capture Mode when using a controller"){.shadowed .autosize}

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Mad_Max)
* Referenced [Mad Max 1.03 AOB Cheat Table (God Mode and more) GOG and Steam](https://fearlessrevolution.com/viewtopic.php?t=15023) CE table with additional instructions on function call handler