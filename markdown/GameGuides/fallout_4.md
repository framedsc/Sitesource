![Fallout 4](Images\fallout_4.png "Shot by IronGauntlet"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
Game version | 1.10.163.0
 
## Tools

* [FO4 Photomode](https://www.nexusmods.com/fallout4/mods/49997)  
**Features**: Camera control, FoV control, HUD toggle, timestop/gamespeed, ingame DOF control, player position adjustment.

* [Screen Archer Menu](https://www.nexusmods.com/fallout4/mods/66047)  
**Features**: Camera control, light spawning and control, posing.

## Controls 

Function | Key
--|--
Toggle camera | `Pause menu` / `Bindable Key (MCM)`
Move camera forward / backward | `W` / `S`
Move camera left / right | `A` / `D`
Move camera up / down | `Left Mouse` / `Right Mouse`
Take a screenshot | `Spacebar`

## Essentials

* [Fallout 4 Script Extender](https://www.nexusmods.com/fallout4/mods/42147) Required to run most mods

* [Mod Configuration Manager](https://www.nexusmods.com/fallout4/mods/21497) Required to edit hotkeys for most mods

## Graphic Mods/Improvements

* [ENB for Fallout 4](http://enbdev.com/mod_fallout4_v0489.htm) Post-process graphical improvements for the game, such as improved SSR, SSGI.

* [PRC-X](https://www.nexusmods.com/fallout4/mods/6796) ENB addon that adds lots of colorgrades/frames. You NEED base ENB dlls for this.

* [NAC-X](https://www.nexusmods.com/fallout4/mods/46722) Adds a variety of weather/climate changes, and also adds a few post-processing effects (you might have to disable a few for the photomode mod to function properly). Also has options to control Ingame DOF.

* [Enhanced Lights and FX](https://www.nexusmods.com/fallout4/mods/13596) Interior lighting overhaul, good for shots.

* [Fallout 4 - Texture Optimization Project](https://www.nexusmods.com/fallout4/mods/978) Renders textures appropriately to maintain stable frame rates.

## How to Use PRC-X

Fallout 4 has an interesting ENB addon mod called [PRC-X](https://www.nexusmods.com/fallout4/mods/6796), which gives you several options to configure how the game looks, varying from colorgrades to frames and borders. There are three versions of this mod, but the preferable one is Advanced.

To install this mod, you will need the latest version of [ENB](http://enbdev.com/download_mod_fallout4.html). From the "Wrapper Version" folder, transfer `d3d11.dll` and `d3dcompiler_46e.dll` to the main game folder and then transfer all files for PRC-X.

Activate the ENB menu in-game by pressing the `End` key (rebindable). Then, the helper screen will tell you how to configure the ENB.

@alert important
Reshade effects that use the depth buffer (like CineDOF) can mess with the negative print paper, so it's advised to use ENB DOF with the frames.
@end

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Fallout_4)
