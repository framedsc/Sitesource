![Metal Gear Rising: Revengeance](Images\metalgearrising.png "Shot by Stellasin"){.shadowed .autosize}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR/Custom Resolution | Yes (Read Below)
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 9
 
## Tools
 
* [Cheat Table by IPG Xapek](..\CheatTables\METAL_GEAR_RISING_REVENGEANCE-FreeCam-Fov-NoHUD-StopTime.CT)   
**Features**: Freecam, Timestop, UI Toggle, FOV Control 

## Tips and Tricks

### Installation & Use

After loading into a level, run the cheat table and select the Metal Gear Rising process. Use the hotkeys mentioned below to use the tool. 

### Resolution Fix 

The game supports only until 1080p by default. The 1080p option will look normal at first glance, but upon closer inspection it's actually 1080p upscaled to your native resolution. If you have a monitor that is larger than 1080p, follow the steps below:

1. Download MGROverride from [here](https://community.pcgamingwiki.com/files/file/722-mgroverride/).

2. Place the exe in your game folder and run it. 

3. Set the game exe path, enter your desired resolution and hit patch. Also have a backup of your original game exe if necessary.

4. Ingame, go to Options> Graphic Options and set the resolution to 800x600. This is the new resolution that you created.

**Note:** The game will change the resolution back to 1080p on launch, so you have to manually change it everytime you play. 

### DSR/Custom Resolution 

If you want to increase the resolution beyond your monitor's native resolution, follow the steps below: 

1. Follow until Step 3 from the Resolution Fix above.

2. Next make sure you have your Custom Resolution added in Nvidia Control Panel. Follow [this tutorial](https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-us/mergedProjects/nvdsp/To_create_custom_timings_for_your_HDTV_display.htm#:~:text=To%20create%20custom%20resolutions%20for%20your%20display&text=From%20the%20NVIDIA%20Control%20Panel,box%2C%20click%20Create%20Custom%20Resolution) if you need to make it.

3. Go to Windows Settings> System> Display. In the screen resolution dropdown, select the resolution that you made, then keep changes. 

4. Launch the game and once ingame set the resolution to 800x600. This method works both with windowed mode and fullscreen.

**Note:**  The reason for changing resolution in windows settings is because the game switches back to 1080p once you go fullscreen, and windowed mode is overscaled with no way to resize the window. The game only supports 16:9 resolutions. Trying a resolution with a different aspect ratio stretches the image (This was tested on a 16:9 monitor, so it might behave different on ultrawide monitors).

### ReShade Support

Make sure to install ReShade with DirectX 9. Turn off MSAA in Graphic Options ingame to used depth based shaders, else they will not work. You can use any other AA from ReShade instead. 

### IPG Xapek's Cheat Table Controls

Key | Function
--|--|
F1 | Turn Off HUD
Right Ctrl + F1 | Turn On HUD
F2 | Enable Timestop
F3 | Disable Timestop
F4 | Toggle FOV Control 
NUM - | Decrease FOV
NUM + | Increase FOV
F5 | Toggle Camera Control
NUM 4,5,6,8 | Move Camera 
NUM 7,9 | Camera Height
F6 | Lock Mouse
F7 | Toggle Camera Look (Disables Camera Movement)
I,K,O,P | Look Around 
Mouse, Arrow Keys | Camera Orbit
Ctrl + F2 | Enable Slow Motion
Shift | Disable Slow Motion
Ctrl + F3 | Enable Timestop except Raiden
Ctrl + F4 | Disable Timestop 

@alert tip
The Camera behaves very strangely in this game, and often changes position on it's own and while exiting ReShade. It is recommended to use ReShade's Freezeshot shader to Freeze the camera where you need it before capturing. Shaders like Magic Border and Letterbox can be used to determine cropping ratios to frame your shot. 
@end

### Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Metal_Gear_Rising:_Revengeance)