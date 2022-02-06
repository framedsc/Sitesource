![Code Vein](Images\codevein_header.png "Shot by ItsYFP"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | unknown
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [UE4 Console Unlocker (UUU) by Otis_Inf & Sunbeam](../GeneralGuides/universal_ue4_consoleunlocker.htm)  
**Features**: Free camera, HUD toggle, Pause Game, FOV Control, in-game dev console

@alert Info
When you use the UUU, it'll enable the in-game dev console. The code of the game however has `Insert` bound to open the dev console. This is likely left in the game
by a developer as it wouldn't harm anyone as by default the dev console isn't available. However with the UUU it is available and as the UUU also binds `Insert` to activate
the free camera, this can be a bit annoying. To solve this, in the UUU keybindings panel, choose another key to activate the camera. 
@end

## Tips and Tricks

### Useful Console Commands

Besides the usual UUU features, you could try these console commands in the in-game console:

`ToggleDebugCamera`
:	Enables the UE4 debug camera. This shouldn't be your first choice (as it doesn't have Tilt) but it can be handy as you can use it 
in combination with the teleport command (see below).

`TeleportToDebugCamera`/`Teleport`
:	Teleports your character to the current camera location (Dosent work in small rooms)

`slomo 0.5` / `slomo 1.0`
:	Slow motion / Normal game speed

`playersonly`
:	Forces Monsters in idel Animation, Player Character can keep moving around

`r.SceneColorFringeQuality 0`
:	Removes the awful CA

The console has a history. Simply press arrow-up to get the list of last entered commands. This allows you to quickly switch between previously entered commands like `ToggleDebugCamera`, `r.PostProcessAAQuality 2` etc. It's advisable to switch off the HUD before enabling the debug camera, as sometimes some HUD elements aren't hidden when the debug camera is enabled.


##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Code_Vein)
