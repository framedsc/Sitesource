![Hitman 3](..\Images\hitman3.png "Shot by Tokenass"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | Yes
Graphics API | DirectX 12
Game version | 3.130.0
 
## Tools
* [ZHMModSDK](https://github.com/OrfeasZ/ZHMModSDK/releases/tag/v1.6.0)  
**Features**: Mod Loader and Mods - Freecam, SkipIntro, NoPause etc.

* [Cheat Table](../CheatTables/Hitman_3_3.100.0_1.3.CT)  
**Features**: Ansel Unlock, Invisible HUD, Game Freeze


## ZHMModSDK Installation

1.  Click on the link above or click [here](https://github.com/OrfeasZ/ZHMModSDK/releases/tag/v1.6.0) and download the `ZHMModSDK-Release.zip` file. 

@alert tip
Make sure to download the version of the SDK which is compatible with your game version
@end

2.  Extract the file and paste its contents in `Hitman 3\Retail` folder.

3. Download this [file](https://mega.nz/file/uDhiELDR#DkBbDhb5W-bKAMhGpkW4mQ0RICDQEfvYqz-1M5gn2pQ) and paste it in `Hitman 3\Retail` folder.
**Optionally** you can just create a new `text document`, rename it to `mods.ini`, paste this line in the file,
```
[skipintro]
```
save it and paste the file in the `Hitman 3\Retail` folder.

*This step is done because the SDK has a bug which causes the game to freeze at startup (4/5 times) so the `mods.ini` file activates `skipintro` mod which skips the game intro hence bypassing this bug.*

## Cheat Table

To use the cheat table you need to have [Cheat Engine](https://www.cheatengine.org) installed.

When you are *ingame* open the cheat table and select **Hitman 3** from the Processes. You need to press `Esc` once to make the Cheat Table work.

@alert important
The No HUD script does not hide the **Saving** box which shows up every few minutes
@end

## Using Freecam

The **ZHMModSDK** comes with some preinstalled mods including Freecam.
You can check the total list of mods from the [SDK repository](https://github.com/OrfeasZ/ZHMModSDK)

Once the above steps are done and you are in the *main menu/ingame*, press the `~` key to open up the console and select the **Freecam** and **Nopause** mods and click **OK**.

Disable the HUD using the CT. You can freeze/unfreeze the game using the `key 5`/`key 4`.

To enable the freecam make sure that the game is unpause and press `P`. This will show up the freecam controls for the first time which you can close by bringing up the cursor by pressing `~` key.

Once you have lined up the shot you can lock the camera by quickly unfreezing and pressing the `F3` key which locks the camera enabling Agent 47's movement and then freezing the game again

## Freecam Controls

Keys	| Action
--|--
`P` | Toggle freecam
`F3` | Toggle camera lock 47 input
`Ctrl + W/S` /  Y + LS  | Change FOV
`Ctrl + A/D` / A + LS | Roll camera
`Alt + W/S` / B + RS | Change camera speed
`Space + Q/E` / LB + RS | Change camera height
`Space + W/S` | Move camera forward/backward on axis
`Shift` / RB | Increase speed while holding
` ` / A + Click in LS | Reset rotation
` ` / LB | Keeps camera still while you control 47


## Hotsampling
The game hotsamples with SRWE. The Ansel supersampling feature is a hit or miss.
Enable The NoPause mod so that the game doesn't pause when alt-tabbing.
Make sure that the game is windowed when using SRWE.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Hitman_3)
* [Nexusmods](https://www.nexusmods.com/hitman3?tab=popular+%28all+time%29)
