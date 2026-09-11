![Bloodborne](Images\Bloodborne.png "Shot by ChevalierJavad"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Not Tested
Custom Aspect Ratios | No
Reshade | Yes (With Vulkan)
Ansel | No
Graphics API | Vulkan
 
## Tools

* [Fov Control CT by Skall](https://www.nexusmods.com/bloodborne/mods/76)  
**Features**: the Title speaks for itself.
* [My own Bloodborne.xml](../GuideResources/Bloodborne/Bloodborne.xml)  
**Features**: Debug Camera, disable Chromatic Aberration, Depth of Field, and Motion Blur, **Very Important**.
* [Debug Menu](https://www.nexusmods.com/bloodborne/mods/253)  
**Features**: Freeze Enemy AI, Enable No Damage, Change the Time of Day, and more.

## Installation

- First off, make sure the emulator is running on the latest update.   
- Right-click on Bloodborne inside the menu > **Cheats/Patches** > select **Patches** from the top > in select **Patch files**, select `Bloodborne.xml`, and set repository on the bottom to **shadPS4** and then hit **Download Patches**.
- Make sure you download patches from the **shadPS4** repository in the emulator instead of goldhen.  
- Once downloaded, enable these options:
  - Disable Chromatic Aberration
  - Disable Depth of Field
  - Disable Motion Blur
  - Restore Debug Menu
  - Restore Debug Camera
- Follow the same steps but with the `debug menu.xml`.

@alert Info
Also make sure to read the descriptions for each patch you enable.
@end

There are also other patches there that could be useful for gameplay, so make sure to take a look at the rest.

@alert Warning!
Some may not see some of the options to download from shadPS4 repository. No worries, I have provided a link to my own [Bloodborne.xml](../GuideResources/Bloodborne/Bloodborne.xml). Download it and paste it in `YourGameDirectory\user\patches\shadPS4`. By doing this you no longer need to download the patches from inside the emulator.
@end

## Controls 

Key | Command
--|--
<font face="ControllerPS">< + x</font> | Toggle debug camera
<font face="ControllerPS"><</font> | Move camera forward / backward / left / right
<font face="ControllerPS">></font> | Camera orientation
<font face="ControllerPS">{  }</font> | Move camera up / down

To Disable the Hud, simply go to the in-game settings **System Settings** > **Environment** > **Display Hud** and turn it off.

Inject the cheat engine table into ShadPS4 (you can use [our guide](../GeneralGuides/cheat_engine_tables.md) to learn how). Enable the script and leave it enabled. The script might take a little time before being enabled.

Key | Command
--|--
`Numpad +` / `Numpad -` | Increase / decrease fov

@alert Warning!
When you have found the FOV you would like to play with, you **must** freeze the value. 
To do so, when you have enabled the script, you need to click on the box near "fov value" and that's it! If not, the FOV will reset after your death!
@end

### Debug Menu Guide
Access the menu by pressing left on your controller's Touchpad. If you don't own a PS4 controller, be sure to rebind it to an input you have access to by going to the "back button behavior" options of the emulator.

Then, inside the debug menu, you can press <font face="ControllerPS">c</font> to **Enter**, <font face="ControllerPS">x</font> to **Go Back**, and <font face="ControllerPS">D</font> to **Enable**/**Disable** options.

In the debug menu, by going to **GAME** > **CHR INS** > **CHR DBG** you can enable:

Menu Option|Description
--|--
Player No Dead | You can still take damage, but you won't die.
All No Move | The enemies will stop moving, but they attack once you get close to them.
All No Attack | The enemies will not attack you.
All No Update AI | When getting close to enemies, they will turn around and face the character. With this enabled, they don't look at the character anymore.
Switch All No Update | Completely freezes the AI, while you can still move around.

@alert Info
Apparently, there's another option, which is to control enemies. Unfortunately, I couldn't get it to work. Enabling the **Enemy Control** from the game patches will not work with the Debug Camera.
@end

To change the Time of Day, head over to **GameData**. There, enable `MapTimeslotRealtimeDebug`, and finally change the ToD by using `MapTimeslot`. You should have 4 options there.

@alert Warning!
Keep in mind that changing the time of day too much will crash the game.
@end

## Useful Links

* [No Player Light](https://www.nexusmods.com/bloodborne/mods/46)
* [Shadows of the Hunt](https://www.nexusmods.com/bloodborne/mods/45) Adds dynamic shadows to everything, better LOD, disables AO and AA to reintroduce "better ones" with reshade and more. Didn't include it in the guide as FPS dropped, and even textures were flickering in my testing (besides other issues).
