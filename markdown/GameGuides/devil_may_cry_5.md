![Devil May Cry 5](Images\dmc5_header.png "Shot by Langgi"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | No *
Reshade | Yes (DX11)
Ansel | No
DirectX versions | DirectX 11, DirectX 12

\* Custom aspect ratios achieved via CE Table  
 
## Tools

* [CE Table by Kputt + Jim2point0](..\CheatTables\DevilMayCry5AOB.ct)  
**Features**: Photo Mode Camera control, FOV Control, Custom Aspect Ratios  
**Instructions**: Only use 1 aspect ratio script at a time. Disable one before enabling another. Aspect Ratio Scripts will only work if you haven't patched the EXE. So if you've modified the EXE to work with another aspect ratio by default, you won't be able to use these scripts.
* [Photo Mode Logo Removal](https://drive.google.com/open?id=1Lxvah9oRk3py8duGCDbHeMgcwUP_jC8O)  
**Features**: Removes the logo in photo mode.  
**Instructions**: Extract files to EXE folder. Press Caps lock to toggle.

## Tips and Tricks

In order to use ReShade, you'll need the game to boot in DX11. In your game's folder, open `dmc5config.ini` and change the following line:

```TargetPlatform=DirectX11```