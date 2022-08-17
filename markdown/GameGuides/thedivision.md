![The Division](Images\thedivision_header.png "Shot by SammirLlm"){.shadowed .autosize}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes ([see notes](#reshade))
Ansel | No
Graphics API | DirectX 11
 
 
## Tools
* [Cinematic Tools by Hattiwatti](https://www.mediafire.com/file/mheyys1uka0wbjd/CT_TheDivision18_20181003.rar/file)  
**Features**: Camera control, Timestop, FoV, Depth of Field, Time of day and Weather control. 
 
Key | Function
--|--|
`INS` | Toggle camera
`DEL` | Freeze time
`HOME` | Toggle game UI
`F5` | Toggle tool UI
WASD | Move camera
Mouse, Arrow Keys | Rotate camera
`Num 1` / `Num 3` | Tilt camera left / right
`PgUp` / `PgDn` | Increase / Decrease FoV
*Inside tool UI* | Weather control
*Inside tool UI* | Time of day control
*Inside tool UI* | Depth of field control
 
@alert tip 
Tools won't work with DirectX 12, so make sure it's not enabled on your video settings.
@end
 
## Troubleshooting
You should be fine with running both the game and the tools as admin, you might experience some crashes, if you can't get the tools work after several attempts, here are some things you can do:
 
1. **Start Ubisoft Connect and Steam as admin**.
2. **Start the game as admin directly from the main folder**. This should be enough, but in case that didn't work:
3. **Load the game and don't inject the tools immediately**, walk around a bit, spend some minutes, then inject the tools.  
**Optional**: You might want to use another injector, you can use ExtremeInjector unless you use Windows 10, it doesn't work with it, though you don't need to change it, the tool's injector works pretty well.
4. **Change your graphics settings**, set them to, let's say, medium or high, if you get the tools working, try changing some setting little by little, remember to reload your game whenever it tells you to do so.
 
If nothing above worked, which is unlikely, *try restarting your PC* or just *be patient and keep trying*.
 
@alert important
**Use the tools at your own risk!** Even though the game hasn't received an update in a long time, there still chance for you to get banned, I'd recommend to not spend much time with the tools on the PvP areas known as Dark Zones.
@end
 
## Reshade
 
Since the game is always online, you won't be able to use the depth buffer with the common Reshade installer, you will need to use a custom Reshade build that doesn't block the use of Reshade if the game is connected to the internet. You can find more about it [here](https://framedsc.github.io/ReshadeGuides/setupreshade.htm#depth-buffer-on-online-games).
 
 
## Hotsampling
 
Since you are running the game as admin, you would also need to run SRWE as admin for the game process to show up. 
 
Additionally, when hotsampling some tool configurations get reseted, like the blending between weathers, so beware of that.
 
## Useful Link
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Tom_Clancy%27s_The_Division)