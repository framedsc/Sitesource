![Control](Images\control_header.png "Shot by Jim2point0")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes (with tools)
DSR | Yes (not all resolutions are supported)
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11, DirectX 12

## Mods

* [Loose Files Loader](https://www.nexusmods.com/control/mods/11): This mod does not do anything on its own but is used by other mods that supply loose files.
* [Tweakables](https://www.nexusmods.com/control/mods/14): This mod allows the player to customize a wide variety of the game's tweakable parameters. 
* [Photomode Range Unlocker](https://www.nexusmods.com/control/mods/23): This mod unlocks the in-game Photomode allowing the player to move the camera to greater distances than what is possible in the vanilla game.

## Tools

* [Cheat Engine Table by Otis_Inf & HattiWatti](..\CheatTables\Control_DX12_Hotsampling.CT): This tool is used to perform Hotsampling. To learn more, refer to this [Cheat Engine Table guide](https://framedsc.github.io/GeneralGuides/cheat_engine_tables.htm).

## Workflow
First, run the game as adminstrator. [*Note*: Only the DX12 exe supports Raytracing].

Alt-tab out of the game to run both SRWE (as administrator) and Control's Cheat Engine table. Attach both of them to Control's exe process and hop back in game.

When you feel like taking a shot, press `ESC`, change the game's Display Mode to `Windowed` and open the Photo Mode. Frame your shot and add any Reshade effect if you want. When you are satisfied with the composition and the colors, alt-tab out and in SRWE, set the Width and Height according to the resolution you want to take the shot in. Remember to check the `Force EXITSIZEMOVE` option in SRWE. After setting the resolution, alt-tab back in to the game and wait for 1-2 second while Reshade reloads the effects. Take the screenshot using Reshade's screenshot keybind.

## Tips and Tricks

* **Administrator Mode**
In its default state, it might not be possible to run the game in administrator mode from launchers such as Steam, EGS etc. You have to manually run the game's executable as adminstrator. However, when you do this, the launcher doesn't detect that the game is running and as such, it does not track things such as the hours you spent in-game, etc. If you think this is an issue or feel that manually launching the game as administrator everytime is a hassle, you can follow the steps below: 

    1. Go to Control's installation directory.
    2. Right-click on `Control.exe`, go to the Compatibility tab, and check the `Run this program as administrator` box.
    3. Similarly, right-click on `Control_DX11.exe` or `Control_DX12.exe` (depending on which version of the game you want to play), go to the Compatibility tab, and check the `Run this program as administrator` box.
    4. Go to the launcher's installation directory, right-click on its .exe, go to the Compatibility tab, and check the `Run this program as administrator` box.
    5. Open the launcher and start the game.

Steps 2 and 4 are necessary (and not just 3) because when you start the game using the launcher, it runs `Control.exe` and from there, you choose which version (and thus which .exe) you want to play. If `Control_DX11.exe` or `Control_DX12.exe` has administrator status, `Control.exe` needs to have it as well to be able to run them and in turn, the launcher needs to have the elevated status as well.

* **Hotsampling and SRWE**: If you directly hotsample to a high resolution, you might experience crashes even though theoretically your GPU can handle that particular resolution. So, the best practice is, before you set your hotsample resolution, switch to a lower one, like 1 Megapixel in SRWE. Only after that, set the resolution you want to shoot in.

    Setting a low resolution first everytime you switch it prevents the game from bugging out. The game might take a few seconds to readjust. (Afterburner overlay can help you monitor that)

    If you happen to get low quality textures, go into Settings and turn the Texture Quality down, confirm, then up again; that should reload them correctly.


## Rough Edges
The game seems to have some issues with noise, which is exacerbated with Raytracing, especially on walls and doors in some cases. Texture breaking has also been noticed at certain resolutions and aspect ratios.

## Useful links

* [Unlock the PS4 exxclusive outfit](https://cdn.discordapp.com/attachments/762793138480742411/881914438091935844/Desktop_Screenshot_zzz.png)
* [PC Gaming wiki](https://www.pcgamingwiki.com/wiki/Control)