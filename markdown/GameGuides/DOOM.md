![DOOM](Images\doomheader.png "Shot by Philos"){.shadowed}

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
API versions | OpenGL, Vulkan (see notes)
Compatible with | Current (6.66) (see notes)
See notes | Yes

## Tools

* [Camera tools by Otis_Inf](https://github.com/FransBouma/InjectableGenericCameraSystem/tree/master/Cameras/DOOM)  
**Features**: Camera control, FoV control, Timestop
* [CE Table by DET](..\CheatTables\DOOMx64_DET.CT)
**Features**: AR fix, FoV control

## Compatibility

To use the camera tools, you'll need to downgrade game binaries. Please use the guide on FRAMED to learn how to [Revert Game Update using Steam Console](https://framedsc.github.io/GeneralGuides/steam_update_guide.htm). After the first step you can download the necessary binaries with using this code: `download_depot 379720 379721 907965064786099828`. Then you need to copy these files to your game folder. (explained at step 6) 

@alert important
Camera tools only works with **OpenGL API**. To change API go to `Settings > Advanced > Graphics API`.
@end

## Troubleshooting

First, try to start camera with only starting it as administrator. **IF everything's fine, then you don't need to apply these steps below.** 

1. Start camera tools as administrator (For real)
	1. Right click to `DOOMx64.exe` go to `Properties > Compatibility`
	2. Click the `Change settings for all users` button
	3. Check `Run this program as an administrator` and press OK
	4. Right click to `IGCSInjector.exe` and click `Run as administrator` (Yes still, you know Windows)

2. Disable Windows UAC
 You may need to disable Windows UAC. To do this use [this guide on winaero.com](https://winaero.com/blog/how-to-turn-off-and-disable-uac-in-windows-10/). You don't need to download the app, just apply **Option one**, and **Option two**.

3. Be patient
 Camera tools may not work as the game started. Kill some monsters, open the map, kill more monsters, spent some time, then try to start camera. 
 
## Hotsampling & Custom AR

By default changing AR via SRWE will likely give you a bad result like stretching. You have two options to avoid this.

1. **Custom AR With CE Table**
 Simply download the provided [CE Table by DET](..\CheatTables\DOOMx64_DET.CT) and check 'nuke portrait check / control FOV'. Now you can use any aspect ratio through SRWE. It's highly suggested to change CE Table's hotkeys for controlling FOV, otherwise it'll conflict with Camera Tools' FOV Control. 

2. **Custom AR Without CE Table**
 As you stick with default AR there won't be a problem about stretching. Simply multiply the current windowed resolution on SRWE with 3, 4 or higher depending on your PC specs to avoid stretching. For example if your windowed resolution is `1616x939` then `1616 x 4 = 6464` `939 x 4 = 3756` so `6464x3756` is your hotsampled resolution. Use [AspectRatioComposition.fx made by Daodan317081](https://github.com/Daodan317081/reshade-shaders/blob/master/Shaders/AspectRatioComposition.fx) to preview in-game custom AR. Placing this shader at the bottom of shader list and binding a key to toggle it is highly recommended. After taking shot, you can crop it with your favorite image editor. (Photoshop and GIMP allows you to crop image by entering aspect ratios) 

@alert info
Custom Aspect Ratios with DSR not tested.
@end

## Reshade & DoF

Reshade DoF tested on current latest version of Reshade (4.4.1). Since the current version of Reshade for OpenGL has no option for selecting specific depth buffer (choosing automatically), it may not work as expected every time. Resizing window affects depth buffer in both way good and bad. So if you experiencing issues with depth buffer try resizing resolution via SRWE. 

## Using Camera

1. Enable camera by pressing `Insert`
2. Press `Numpad .` to block input to game
3. Place camera for a cool shot then press `Home` (here you can make changes with Reshade)
4. Switch SRWE to hotsample by pressing `Alt+Tab`. Game will automatically open the menu don't worry
5. Set your new resolution then switch back to game
6. Press `Numpad .` to enable input to game then press `ESC` to close menu
7. After menu is closed press `Numpad .` to block input again
8. Take your shot

@alert info
Step 4, 5, 6, 7 is not necessary if you go with DSR.
@end

## Photo Mode

To use photo mode, it has to be on a level that has already been completed once. Then you can enable it via `Settings > Game > DOOM Photo Mode`. Photo mode only works on the three basic difficulty modes: I'm too young to die, Hurt me plenty and Ultra-violence. Once you enabled the Photo Mode, press `\` key to open it. 

@alert info
Using camera tools with photo mode not tested.
@end

## Useful links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Doom_(2016))