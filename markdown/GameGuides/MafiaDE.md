![Mafia: Definitive Edition](Images\MDE_header.png "Shot by Jack Heisenburg"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes 
Ansel | No
DirectX version |  DirectX 11

 
## Tools
* [Camera Tools by Otis_Inf](https://patreon.com/Otis_Inf)   
**Features**: Freecam in gameplay (doesn't work in cutscenes), FOV Control, time stop.  
Note: You need to download Mafia 3: Definitive Edition tools, they work for Mafia: Definitive Edition, minus the hud toggle.
* [Hud Toggle by Geon](https://nohud.fandom.com/wiki/Mafia:_Definitive_Edition_No_Hud)

## Extras
* [Scripthook](https://db.nomad-group.net/page/MDE_ScriptHook:_Instructions): Player model swap, no clip movement, spawn and edit vehicles, weather controls. 
* [Scripthook Revamped](https://www.nexusmods.com/mafiadefinitiveedition/mods/58): Adds more options to Scripthook such as the ability to play character animations, change time of day, add in character props. 

### Reshade Depth Buffer
Because this game always runs in online mode you will not be able to use the depth buffer with the common reshade installer, you will need to use a custom build that doesn't block the use of reshade in online games. Find out more [here](https://framedsc.com/ReshadeGuides/setupreshade.htm#depth-buffer-on-online-games).

@alert info
Note that the game uses a reversed depth buffer. You will need to go to the global processor definitions and change `RESHADE_DEPTH_INPUT_IS_REVERSED` from `0` to `1`. This is essential and otherwise depth shaders will not work properly.
@end

### Scripthook and Reshade
If you are using Reshade alongside Scripthook, your game may no longer launch as Reshade hooks into the Scriphook launcher and interfers with the game. To fix this, edit `Mafia - Definitive Edition\ScriptHook\data\config.json` and change line 20 `"showStartupMenu"` from `true` to `false`.



## Useful Links
* [Nexus Mods](https://www.nexusmods.com/mafiadefinitiveedition)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Mafia:_Definitive_Edition)
