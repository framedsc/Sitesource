![Dragon's Dogma 2](Images\dd2_header.png "Shot by moyevka"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Hotsampling | Yes¹
DSR | Yes
Custom Aspect Ratios | Yes¹
Reshade | Yes¹
Ansel | No
Graphics API | DirectX 12

¹ - requires REFramework

## Tools
- [REFramework by praydog](https://www.nexusmods.com/dragonsdogma2/mods/8)  
Features: A mod framework, scripting platform, and modding tool for RE Engine games
- [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
[Features](https://opm.fransbouma.com/Cameras/dd2.htm): Camera control, FoV control, HUD toggle, timestop/gamespeed, hotsampling, in-game DoF toggle, better shadow filtering, higher LODs
- [RELit by Originalnicodr and Otis_inf](https://github.com/originalnicodr/RELit)  
[Features](../GeneralGuides/relit.htm): Custom lights, global light control, exposure control

@alert important
REFramework is necessary in order to use any tools including Reshade. If you run into troubles with the public releases of REFramework, [try its nightly releases.](https://github.com/praydog/REFramework-nightly/releases)
@end

## Installing Reshade
The installation process for Reshade and its shaders is slightly different in Dragon's Dogma 2, as REFramework makes its own changes as to how external files are loaded to the game. REFramework creates a `_storage_` folder to which all external files, such as DLLs and ADDONs, are copied into. If you're unable to get any addons, such as ShaderToggler or IGCSDOF, to install correctly, try dropping them directly into this `_storage_` folder instead. 

Reshade shaders and textures can also fail to be found due to this change in file structure. You will have to manually point Reshade to your shaders and textures folders for them to load in correctly.

## Hotsampling
The game needs to run in **windowed mode** in order for the game to hotsample correctly to different aspect ratios. Hotsampling in borderless windowed will cause black bars to appear.

## Shooting without IGCS
If you don't have access to the Otis_Inf camera tools, it is still possible to take shots of the game using REFramework's built-in features.

### Timescale & Freecam
REFramework has its own freecam and gamespeed controls. FOV control can be found under the Camera dropdown, check Use Custom Global FOV to enable use of the slider. 

@alert neutral
The freecam will not move when timescale is set to `0`. The minimum value is `0.0001` - the game is still in motion, but it should give you enough time to compose a shot.
@end

### Hotsampling with SRWE
REFramework includes rendering fixes under its Graphics dropdown which do force the game to render correctly to different aspect ratios while running in borderless windowed.

@alert warning
...however, having these boxes ticked will cause FOV changes (with both REFramework and IGCS) to be extremely buggy!
@end

## EMV Engine
Dragon's Dogma 2, through REFramework, supports the [Enhanced Model Viewer Engine](https://github.com/alphazolam/EMV-Engine) repository of scripts. You can use these scripts to hide characters from a scene, pose them, move them around, and so much more. [Read our site guide](../GeneralGuides/emv_engine.htm) on the scripts on how you can use these scripts in your shots.

Here is a small list of some useful IDs:

ID | Character
-- | --
`ch000000_00` | Player
`ch100000_00` | Main Pawn
`ch111xxx` | other pawns in your party
`ch110xxx` | other pawns in the world

### Poser Quickstart Guide
A good use of EMV's poser is to edit eye rotations so your subjects look a little less dead.

1. open Script Generated UI
2. open Collection
3. click Detach Window
4. click Search, no need to change any settings
5. choose an ID
6. dropdown the same ID again
7. expand Poser
8. for Filter, type `eye`
9. `L_Eye` and `R_Eye` are at the bottom of the results

## Useful Links
- [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Dragon's_Dogma_II)