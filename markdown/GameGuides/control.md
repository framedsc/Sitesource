![Control](Images\control_header.png "Shot by Jim2point0")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (with tools)
DSR | No *
Custom Aspect Ratios | Yes
Reshade | Yes (DirectX 11)
Ansel | No
DirectX versions | DirectX 11, DirectX 12

\* To use a DSR resolution, set your desktop resolution to it first, then you should be able to select it in-game. You will not see all DSR resolutions though.
 
## Tools

* `Cheat Engine Table by Otis_Inf & HattiWatti`  
[DX11](https://framedsc.github.io/CheatTables/Control_DX11_Otis.CT)  
[DX12](https://framedsc.github.io/CheatTables/Control_DX12_Otis.CT)  
**Features**: Debug Camera, FOV, Time stop, Hotsampling, Hud Toggle, Render Toggles

## Using The CE Table

First, [read the general Cheat Engine guide](https://framedsc.github.io/GeneralGuides/cheat_engine_tables.htm) if you have't already to learn how to use cheat engine table (don't worry, it's easy).

To enable hotsampling (via SRWE)... enable the hotsampling script. I also had to check the `Force EXITSIZEMOVE` option in SRWE. Press `ESC` in-game in order to alt-tab to SRWE. After changing the resolution, alt-tab back to the game and press `ESC` again to force the game to update.

All hotkeys are mentioned in the table, but here's some general info.

* **Debug Camera** - **`Insert`**  
The default speed is insanely fast, so use the mouse wheel to slow it down (or speed it up).  
The default rotation speed is perfect for controllers. If using a keyboard: Press `F9` after enabling the camera to slow the rotation speed for mice. `Numpad -/+` will change the camera FOV. 
* **Toggle Freeze** - **`Numpad 0`**
* **Toggle Hud** - **`Delete`**  
Press ESC twice to force the changes. This can be done while the game is frozen.

The render effect section contains some more useful toggles. Hotkeys for these are listed in the table.

## ReShade

There is a DX12 ReShade DLL floating around, but be aware that this DLL may cause issues when playing Control. Several users experienced memory leaks, causing VRAM usage to climb, which is accelerated at high resolutions. Eventually the game will stop loading textures, forcing you to restart the game. 