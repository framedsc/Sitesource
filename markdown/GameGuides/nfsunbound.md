![Need For Speed Unbound](Images\nfsunbound.png "Shot by pvp"){.shadowed .autosize}

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

## Tools

* [Camera toolkit by ARCHIE](https://nfsmods.xyz/mod/4364)  
**Features**: Tool to control in-game camera and its various features.

* [Hud toggle and Cartoon Effect disable](https://framedsc.com/ShaderTogglers/nfs_unbound.ini) requires Reshade 5+ with [Shader Toggler](../ReshadeGuides/Addons/shader_toggler_repository.htm)

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

## Camtool controls

Key	| Command
--|--
`F1` | Toggle UI
`F2` | Toggle Camera
`Caps Lock` | Toggle HUD
`F5` | Pause Game
`Y, H` | Camera Up / Down
`J, L` | Camera Left / Right
`I, K` | Camera Forward / Backward

@alert info You can change the default camera tool keybinds by finding the keycodes of the keys you want to use [here]( https://www.toptal.com/developers/keycode) and changing them inside the included "CameraToolKit.ini" file.
@end

## Reshade
@alert important
When hotsampling your depth-buffer might change which will require you to manually reselect the correct depth-buffer.
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Need_for_Speed_Unbound)
* [Nexus Mods](https://www.nexusmods.com/needforspeedunbound) 
* [NFS Mods](https://nfsmods.xyz/search?search=NFS&game=18)
