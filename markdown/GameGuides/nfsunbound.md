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
Game version | 1.00

## Tools

* [HUD toggle and Cartoon Effect disable](../ShaderTogglers/nfs_unbound.ini) requires Reshade 5+ with [ShaderToggler add-on](../ReshadeGuides/Addons/shader_toggler_repository.htm).

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

@alert important
When hotsampling your depth-buffer might change which will require you to manually reselect the correct depth-buffer.
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Need_for_Speed_Unbound)