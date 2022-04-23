![DOOM](Images\doomheader.png "Shot by Philos"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (see notes)
Hotsampling | Yes (see notes)
DSR | Yes
Custom Aspect Ratios | Yes (see notes)
Reshade | Yes (see notes)
Reshade DoF | Yes (see notes)
Ansel | No
Graphics API | OpenGL, Vulkan (see notes)
Compatible with | Current (6.66) (see notes)
See notes | Yes

## Tools

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Camera control, FoV control, Timestop
* [CE Table by DET](..\CheatTables\DOOMx64_DET.CT)  
**Features**: AR fix, FoV control

## Compatibility

To use the camera tools, you'll need to downgrade the game's binaries. Please use the guide on FRAMED to learn how to [Revert Game Update using Steam Console](https://framedsc.github.io/GeneralGuides/steam_update_guide.htm). After the first step you can download the necessary binaries using this code: `download_depot 379720 379721 907965064786099828`. Then you need to copy these files to your game folder. (explained at step 6) 

@alert important
Camera tools only work with **OpenGL API**. To change API go to `Settings > Advanced > Graphics API`.
@end

## Troubleshooting

First, run the camera tools as administrator. **IF everything's fine, then you don't need to apply the steps below.** 

1. **Running the tools as administrator**
	* Right click on `DOOMx64.exe` go to `Properties > Compatibility`
	* Click the `Change settings for all users` option
	* Check `Run this program as an administrator` and press OK
	* Right click to `IGCSInjector.exe` and click `Run as administrator`
2. **Disable Windows UAC**  
You may need to disable Windows UAC. To do this use [this guide on winaero.com](https://winaero.com/blog/how-to-turn-off-and-disable-uac-in-windows-10/). You don't need to download the app, just apply **Option one**, and **Option two**.
3. **Be patient**  
Camera tools may not work as the game started. Kill some monsters, open the map, kill more monsters, spent some time, then try to start camera.  

## Hotsampling & Custom AR

By default changing AR via SRWE will likely cause a stretched output. There are two ways to avoid it:

1. **Custom AR With CE Table**  
Simply download the provided [CE Table by DET](..\CheatTables\DOOMx64_DET.CT) and check 'nuke portrait check / control FOV'. Now you can use any aspect ratio through SRWE. It's highly recommended to change CE Table's hotkeys for controlling FOV, otherwise it'll conflict with Camera Tools' FOV Control. 

2. **Custom AR Without CE Table**  
There shouldn't be any stretched output if you stick to your default AR. Simply multiply the current windowed resolution on SRWE by 3, 4 or higher depending on your PC specs to avoid stretching. For example if your windowed resolution is `1616x939` then `1616 x 4 = 6464` `939 x 4 = 3756` so `6464x3756` is your hotsampled resolution. Use [AspectRatioComposition.fx made by Daodan317081](https://github.com/Daodan317081/reshade-shaders/blob/master/Shaders/AspectRatioComposition.fx) to preview in-game custom AR. Placing this shader at the bottom of the shader list and binding a key to toggle it, is highly recommended. After taking shot, you can crop it with your favorite image editor. (Photoshop and GIMP allows you to crop image by entering aspect ratios) 

@alert info
Custom aspect ratios with DSR not tested.
@end

## Reshade & DoF

Reshade DoF was tested on the latest version of Reshade (4.4.1). Since there is no option to select a specific depth buffer on Reshade 4.4.1 for OpenGL, it may not work as expected every time. Resizing the window affects the depth buffer in both good and bad ways. If you are experiencing issues with the depth buffer, try resizing the resolution via SRWE.

## Using the Camera

1. Enable the camera by pressing `Insert`
2. Press `Numpad .` to block input to the game
3. Place camera for a cool shot then press `Home` to lock camera
4. Switch to SRWE to hotsample by pressing `Alt+Tab`. The game will automatically open up the menu don't worry
5. Set your new resolution then switch back to the game
6. Press `Numpad .` to enable input to the game then press `ESC` to close the menu
7. After the menu is closed press `Numpad .` to block input again
8. Take your shot

@alert info
Steps 4, 5, 6, 7 are not necessary if you go with DSR.
@end

## Photo Mode

To use the photo mode, you need to have already beat the game at least once. You can then enable it via `Settings > Game > DOOM Photo Mode`. The photo mode only works on the three basic difficulty modes: I'm too young to die, Hurt me plenty and Ultra-violence. Once you enable the Photo Mode, press `\` key to open it. 

@alert info
Using the camera tools along with the photo mode, has not been tested.
@end

## Useful links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Doom_(2016))
