![Assassin's Creed Unity](Images\acunity_header.png "Shot by TeoTave"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (Use [Windowed Borderless Gaming](http://westechsolutions.net/sites/WindowedBorderlessGaming/download))
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes (DX11)
Ansel | No
Graphics API | DirectX 11
 
## Tools

* [Hatti's Camera Tools (Password: CinematicTools)](https://www.mediafire.com/file/e74f8n4f0p59fe3/AC-f043a6.rar/file)  
__Features__: Camera control (gamepad support), FOV Control, Camera/Rotation Speed, UI toggle (also includes Extreme Injector within downloaded folder).
* [Skall's Unity Enhancements](../CheatTables/acunity_pphack_skall.CT)  
__Features__:  Requires Varia 3.2 Anti-Cheat Table to function - LOD improvements, remove chromatic aberration, remove Depth of Field, remove Fog
* [Toggle HUD Mod](https://www.nexusmods.com/assassinscreedunity/mods/2)  
__Features__: Configurable HUD toggle key (edit d3dx.ini) - works as a timestop when pausing the game and hiding the HUD. Supports gamepad bindings.
* [Varia 3.2 Anti-Cheat Table from FearlessRevolution by Paul44 (Password: Fearless)](https://fearlessrevolution.com/download/file.php?id=25921)  
__Features__: (Disables the game's anti-cheat) God Mode, Invisibility, Increase Inventory supplies. Works for the latest game version 1.5.0 (Uplay and Steam).


## Tips and Tricks

### Hotsampling with Windowed Borderless Gaming (WBG)

Windowed Borderless Gaming (WBG) is the only way to hotsample in Assassin's Creed Unity. It will only work if the game is set to Windowed mode under the game's graphics options. It is recommended to perform this initial process to get WBG working before injecting all of the tools.

1. Launch _WindowedBorderlessGaming.exe_ after loading the game. It will appear in your PC's system tray (click the arrow to see hidden icons if it's not visible). 
2. Right click the WBG icon in the system tray and click  _Add Window (F3)_. Go into the game and press the F3 key - the game should become a borderless window.
3. Right click on the WBG icon in the system tray once again and click _Game Settings_. The fields should occupy with information about the game (if it does not, you may have to restart the game - repeat from Step 2 once the game has loaded).
4. Type in your desired resolution (aspect ratios of 16:9 are supported) under the _Size & Offset_ section. Hit apply to set the game to this new resolution. Type in your native resolution and hit apply to return back. Repeat this process whenever you are ready to hotsample a screenshot. 

With this initial setup complete, the game will automatically switch to windowed borderless mode so long as the WBG is launched.

### Tool Injection Order

The tools must be used in a specific order (after loading your save from the main menu) to function correctly. This must be done every time the game is loaded up (excluding WBG which after an initial setup can be loaded at any point).


1. Open Cheat Engine, find the process for ACU.exe. Open ACU_Varia_v3.2_Released.CT (Anti-Cheat Table).
2. Go to _Table > Show Cheat Engine Lua Script_, then click the _Execute Script_ button at the bottom of the newly opened window. Close this window.
3. Activate _AC 6 Unity ~ v1.5.0 (Uplay and Steam)_ and click _Enable Cheats..._ Let the Lua Engine load the script (this normally takes 5 seconds, it may momentarily say "Not Responding"). Close this window when it has finished.
4. Open _Assassin's Creed Unity PP hack.CT_ (Skall's Unity Enhancements) - when prompted, merge it with the current table.
5. Open Extreme Injector found within Hatti's Camera Tools folder, and select _ACU.exe_ from the process list. Switching to Window List will make it easier to find ACU.exe.
6. Click _Add DLL_ in Extreme Injector and select _ACUnity.dll_ within Hatti's Camera Control folder. Click the inject button. You should see a success message and a new window open. __Every time you launch Extreme Injector from now on, it will save both the process and .DLL file.__
7. Launch _WindowedBorderlessGaming.exe_ if you have not done so already to set the game to windowed mode automatically (assuming you have set it up for Unity).


### Hatti's Camera Controls

**Enable/Disable Camera** - INSERT

**Move Camera** - NUMPAD 8,5,4,6,7,9 OR CONTROLLER LEFT STICK + TRIGGERS

**Rotate Camera** - ARROW KEYS + NUMPAD 1,2 OR CONTROLLER RIGHT STICK

**Increase/Decrease FoV** - PAGE UP/DOWN OR CONTROLLER LEFT & RIGHT THUMB

The interface for the tools is a separate Command Line Interface - do not close this window. Navigate the interface with the arrow keys. Confirm/cancel by pressing enter on an option. 

The _Camera Enabled_ option must be checked to enable camera movement - simply press _INSERT_ with this option checked to enable the camera.

Edit camera speed and rotation speed by pressing _ENTER_, typing in your value and pressing _ENTER_ again to confirm your changes. For a gamepad, lower speeds from 0.1-0.5 are recommended.

**Keep in mind that with the game paused, the free camera will cause some bugs**. You may see NPCs bodies morph if you move too far with the camera enabled. To resolve this, you can pause and unpause the game with the free camera still enabled. The NPCs should return to normal until you move the camera too far again. Repeatedly unpause and pause the game as needed.

### Timestop/Disable HUD

Use the [Toggle HUD Mod](https://www.nexusmods.com/assassinscreedunity/mods/2) as a way to pause the game and remove the HUD. Please note that using this as a timestop does not pause the game's weather such as overhead clouds and the dynamic lighting system. 

Download and place all files in the same folder as your game .exe. To remove all HUD completely, it is recommended to select the __All Hidden__ HUD Preset within the game's HUD options. The default controls with this mod installed are as follows:

**Toggle HUD (including menus)** - CAPS LOCK OR CONTROLLER LEFT THUMB*

**Toggle Last known position silhouette and sword trails** - H

*_The default Toggle HUD controller key interferes with Hatti's Camera Control bindings - it is recommended to change this mod's controller binding for toggling the HUD for ease of use._

1. Locate _d3dx.ini_ in the game directory, open it with a text editor and go to line 158. 
2. Replace _XB_LEFT_THUMB_ with any binding of your choice (that does not interfere with any existing tool hotkey).

### Setting up ReShade's depth buffer

Assassin's Creed Unity will break shaders that use depth when you first setup ReShade as the game uses a reversed depth buffer, so changing `RESHADE_DEPTH_INPUT_IS_REVERSED ` from 0 to 1 in the global preprocessor definitions should fix it. 
After that, you may also have to select the correct buffer depending on your ReShade version as it may choose the incorrect one by default. Keep in mind that in some cutscenes, depth shaders will not work regardless of your settings.

### Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Assassin%27s_Creed_Unity)