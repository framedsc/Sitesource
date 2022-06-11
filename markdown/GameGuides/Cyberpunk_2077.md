![Cyberpunk 2077](Images\cyberpunk2077_header.png "Shot by Lazaro"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes, with tools
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (4.9.1+)
Ansel | No
Graphics API |  DirectX 12
Guide Updated For Game Version | 1.52
 
## Tools

* [Camera Tools with Cyberlit by Otis_Inf](https://patreon.com/Otis_Inf)   
**Features**: Camera control, FoV control, HUD toggle, timestop/gamespeed, hotsampling, time of day, camera paths, photomode posing tools and custom lights.  

## Essential Mods

* [Cyber Engine Tweaks](https://www.nexusmods.com/cyberpunk2077/mods/107) / [Wiki](https://wiki.redmodding.org/cyber-engine-tweaks/)  
Required by many mods.

##  Mods for Setting Up Screenshots

* [Appearance Menu Mod](https://www.nexusmods.com/cyberpunk2077/mods/790) / [Discord](https://discord.com/invite/47jV2rNdgn)  
**Features**: Spawn, move and remove characters and objects. Save and teleport to locations. Enables look at for any pose. Removes many limits of photo mode. And much, much more.
* [Object Spawner](https://www.nexusmods.com/cyberpunk2077/mods/2833)   
**Features**: Spawn over 16k different items. 
* [Freefly](https://www.nexusmods.com/cyberpunk2077/mods/780)  
**Features**: Enable noclip to fly V to places you wouldn't normally be able to reach.
* [Appearance Change Unlocker](https://www.nexusmods.com/cyberpunk2077/mods/3850) with [Character Customization Anywhere](https://www.nexusmods.com/cyberpunk2077/mods/3930)  
**Features**: allows editing of your V while in-game. The first mod unlocks full character customisation at apartment mirrors and the second mod enables that feature to be activated anywhere with a hotkey. This replaces the CyberCAT save editor.

## Graphical Tweaks  

* [Cinematic RTX](https://www.tomshardware.com/uk/news/how-to-unlock-cyberpunk-2077-cinematic-rtx-mode)   
**Features**: Boosts raytracing quality.
* [Settings Manager](https://www.nexusmods.com/cyberpunk2077/mods/2332)   
**Features**: Save your games graphics settings to presets, and switch between them anytime.  
NOTE: If you have a preset from an older version of the game, you may need to create new presets to avoid crashes.

### Writing custom .inis
Cyberpunk 2077 allows further customisation of in-game settings through .ini tweaks. The .ini files can have any names so long as they are placed in `\Cyberpunk 2077\engine\config\platform\pc`.  

**Increase Draw Distance and Reduce Pop-in**  
*Your mileage may vary with this one.*  
Paste the following in your custom .ini:
```
[Streaming]
DistanceBoost = 60.000000
```  
In `\Cyberpunk 2077\engine\config\platform\pc` open `rendering.ini` and change it to:  
```
[LevelOfDetail]
DecalsHideDistance = 100.0
```

**Disabling Depth of Field and Bloom**  
Paste the following in your custom .ini:
```
[Developer/FeatureToggles]
DepthOfField = False
Bloom = False
```
*Disabling depth of field permanently disables it in photomode too!*

## Tips and Tricks

### Appearance Menu Mod
Create more natural poses by using Appearence Menu Mod to swap an NPC to V (or anyone) to have them play out their NPC animations, enter photomode when you see a pose you want.  

In the absence of Cyberlit, AMM can be used to spawn in-game lights, albeit with less control. AMM's spawner can also be used to build studios and scenes. [Example](../Images/cp_AMMexample.png).

Many pose packs are available that overwrite the games default photomode poses, see [NoraLee's Pose Mod](https://www.nexusmods.com/cyberpunk2077/mods/2831) and [Ferret's Poses](https://www.nexusmods.com/cyberpunk2077/mods/2718), amongst many others available.  

### Reshade

There can often be lots of artifacting around hair textures and these are amplified when using various Reshade depth effects. One way to minimise this is to use [RealLongExposure.fx from CobraFX](../ReshadeGuides/RealLongExposure.htm) to create a 'long exposure' which helps to blend together the issues. This is less of an issue with DLSS enabled.

If you find Reshade is causing performance issues, enable `Copy depth buffer before clear operations` until it's time to compose a shot.

### CyberLit

Otis_Inf's tools for Cyberpunk include CyberLit, a powerful lighting tool that can be used to light scenes almost any way you want. A full guide to all its controls can be found [here](../GeneralGuides/cyberlit.htm).

Camera positions can be saved using CyberLit. Create a 0 intensity light to use as your camera anchor point then use 'Move camera to light' to quickly get back to your shot angle. The same can be done by using ICGS camera paths to create multiple camera points.

### Miscellaneous
In the event of another game update breaking lots of mods, you can make a copy of your `Cyberpunk 2077` game folder before the update and play it outside of Steam/GOG whilst you wait for mod updates, or if you prefer to stick to a certain version of the game. 

### Custom Look-ats
An older version of this guide referenced photomode posing through a cheat table, the feature has been entirely remade and is now part of the Otis_Inf camera tools.

Additionally, posing using AMM is possible too.

@alert tip
You may also follow this fantastic [guide](https://docs.google.com/document/d/1Cj4vsnsX5MU7NnlbZakMjKsybXPUeA-h9oogRqmIhcM/edit) by Wench to better learn about using Photomode and setting up custom poses.
@end

## Useful Links
* [Nexus Mods](https://www.nexusmods.com/cyberpunk2077)
* [Cyberpunk 2077 Modding Discord](https://discord.com/invite/BTApCbE) Many exclusive mods available through Discord.
* [Clothing Catalog](https://steamcommunity.com/sharedfiles/filedetails/?id=2328941813) / [Alternate](https://cp2077.8713.su/) / [Hash list](https://docs.google.com/spreadsheets/d/1CCOmY__uhYhpRixs3XizqwUvx1LICqa2GrmyVpA2Nlc/edit#gid=1420053180)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Cyberpunk_2077)