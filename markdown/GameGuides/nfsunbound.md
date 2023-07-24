![Need For Speed Unbound](Images\nfsunbound.png "Shot by tripps"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 12
Game version | Vol.3

## Tools  

* [Camera toolkit by ARCHIE](https://nfsmods.xyz/mod/4364)  
**Features**: Tool to control in-game camera and its various features.
* [Frosty Mod Manager 1.0.7](https://github.com/CadeEvs/FrostyToolsuite/tree/1.0.7)
**Feature**: Utility program that allows you to organize and manage mods.
* [DatapathFix](https://github.com/Dyvinia/DatapathFixPlugin/releases)
**Feature**: Plugin for FMM to fix an issue with modding the game.

## Modifications

* [Unbound Remix](https://www.nexusmods.com/needforspeedunbound/mods/29)  
**Features**: Game enhancement mod for enhancing the customization and gameplay experience.
* [Unlock Everything](https://nfsmods.xyz/mod/4801)  
**Features**: Unlocks every in-game item.
* [Ultimate Customization](https://www.nexusmods.com/needforspeedunbound/mods/3)  
**Features**: Adds hidden parts and improves other customization options.

* [Hud Toggle and Cartoon Effect disable](https://framedsc.com/ShaderTogglers/nfs_unbound.ini) requires Reshade 5+ with [Shader Toggler](../ReshadeGuides/Addons/shader_toggler_repository.htm)

@alert important
The game requires you to use 1.0.7+ version of Frosty Mod Manager otherwise it's an instant crash during loading.
@end

## Photo mode controls 

Key	| Command
--|--
`TAB menu option` | Toggle camera
`Q` / `E` | Move up / down
`R` / `F` | Zoom in / out
`WASD` | Move camera around
`Shift` | Camera effects
`U` | Hide UI

@alert info
The Photo Mode uses a different depth-buffer compared to in-game, you may have to pick it manually for depth shaders to work properly, this is done in the Add-ons (ReShade 5+) tab.
@end

## Camtool default controls

Key	| Command
--|--
`F1` | Toggle UI
`F2` | Toggle Camera
`Caps Lock` | Toggle HUD
`F5` | Pause Game
`Y` / `H` | Camera Up / Down
`J` / `L` | Camera Left / Right
`I` / `K` | Camera Forward / Backward

@alert info 
All of the keybinds can be rebound inside the Cam Toolkit.
@end

## Reshade

@alert important
When hotsampling in built-in photo mode your depth-buffer might change which will require you to manually reselect the correct depth-buffer.
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Need_for_Speed_Unbound)
* [Nexus Mods](https://www.nexusmods.com/needforspeedunbound) 
* [NFS Mods](https://nfsmods.xyz/search?search=NFS&game=18)
