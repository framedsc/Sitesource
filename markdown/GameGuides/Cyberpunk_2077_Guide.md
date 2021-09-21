![Cyberpunk 2077](Images\cyberpunk2077_header.png "Shot by Lazaro"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes, with tools
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (4.9.1+)
Ansel | No
DirectX versions |  DirectX 12
Guide Updated For Game Version | 1.31
 
## Tools

* [Camera Tools with Cyberlit by Otis_Inf](https://patreon.com/Otis_Inf)   
**Features**: Photo Mode Camera control, FOV Control, Custom Aspect Ratios, Time Of Day, Camera Paths and custom lights.  
* [Photomode Improvement with lookat controls CT By Deadendthrills and Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Lock torso/head in place to control eyes separately.
* [Photo Mode Unlocked](https://www.nexusmods.com/cyberpunk2077/mods/3035)  
**Features**: Enables look at for any pose. Removes many limits of photo mode.

## Essential Mods

* [Cyber Engine Tweaks](https://www.nexusmods.com/cyberpunk2077/mods/107) / [Wiki](https://wiki.redmodding.org/cyber-engine-tweaks/)  
Required by many mods.
* [Cybercat Save Editor](https://www.nexusmods.com/cyberpunk2077/mods/718)  
**Features**: Edit V's appearance without starting a new game.

##  Mods for Setting Up Screenshots

* [Appearance Menu Mod](https://www.nexusmods.com/cyberpunk2077/mods/790) / [Discord](https://discord.com/invite/47jV2rNdgn)  
**Features**: Spawn, move and remove characters and objects. Save and teleport to locations. And much more.
* [Object Spawner](https://www.nexusmods.com/cyberpunk2077/mods/2833)   
 **Features**: Spawn over 16k different items. 
* [Freefly](https://www.nexusmods.com/cyberpunk2077/mods/780)  
**Features**: Enable noclip to fly V to places you wouldn't normally be able to reach.

## Graphical Tweaks
* [Update Nvidia DLSS](https://www.techpowerup.com/download/nvidia-dlss-dll/)   
  Update DLSS from 2.1 to 2.2.X. Add to \Cyberpunk 2077\bin\x64 and overwrite. Tested up to 2.2.16.
* [Cinematic RTX](https://www.tomshardware.com/uk/news/how-to-unlock-cyberpunk-2077-cinematic-rtx-mode)   
 Add an extra level of ray tracing.

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

**Tweaked Raytracing**  
```
[RayTracing]
DiffuseIlluminationAOModulation = 1.000000
AccumulationSpeed = 0.000000

[RayTracing/NRD]
DiffuseDenoisingRadius = 30.000000
DiffuseMaxAccumulatedFrameNum = 16

[RayTracing/Reflection]
EnableHalfResolutionTracing = 0
FilterRadius = 512.000000
```
Minor tweaks to how raytraced effects look in-game. Mostly to improve AO and reflections. Will probably have a performance penalty.

## Tips and Tricks

### Appearance Menu Mod
Create more natural poses by using Appearence Menu Mod to swap an NPC to V (or anyone) to have them play out their NPC animations, enter photomode when you see a pose you want.  

In the absence of Cyberlit, AMM can be used to spawn in-game lights, albeit with less control. AMM's spawner can also be used to build studios and scenes. [Example](../Images/cp_AMMexample.png).

See also: [NoraLee's Pose Mod](https://www.nexusmods.com/cyberpunk2077/mods/2831) and [Ferret's Poses](https://www.nexusmods.com/cyberpunk2077/mods/2718), amongst many others.  

### Reshade

There can often be lots of artifacting around hair textures and these are amplified when using various Reshade depth effects. One way to minimise this is to use [Reallongexposure.fx from CobraFX](https://github.com/LordKobra/CobraFX) to create a 'long exposure' which helps to blend together the issues. This is less of an issue with DLSS enabled.  [Example](../Images/cp_RLEexample.png).  

If you find Reshade is causing performance issues, enable `copy depth buffer before clear operations` until it's time to compose a shot.

### CyberLit

Otis_Inf's tools for Cyberpunk include CyberLit, a powerful lighting tool that can be used to light scenes almost any way you want. A full guide to all its controls can be found [here](../GeneralGuides/cyberlit.htm).

Camera positions can be saved using CyberLit. Create a 0 intensity light to use as your camera anchor point then use 'Move camera to light' to quickly get back to your shot angle. The same can be done by using ICGS camera paths to create multiple camera points.

### Miscellaneous
In the event of another game update breaking lots of mods, you can make a copy of your `Cyberpunk 2077` game folder before the update and play it outside of Steam/GOG whilst you wait for mod updates, or if you prefer to stick to a certain version of the game. 

### Custom Look-ats
Otis_Inf's tools also come with a [Cheat Engine](../GeneralGuides/cheat_engine_tables.htm) table that includes some advanced photomode controls including independent movement of eyes and head from the torso through the photomode's look at camera functionality. The script is tricky to use, but once mastered can unlock much more dynamic portraits.

With Look at Camera enabled, the first thing to do is set the torso position. **In order to unlock the head, the torso must have some rotation.** Once the torso position is set, hit [F7] to lock the current pose. Now, do [Ctrl+F7] then [Shift+F7] and the head should be freed to look around now. Once the head position is set, hit [Ctrl+Shift+F7]. Now, only the eyes should be able to look around. Once the eye positions are set, hit [F8] to lock everything in place.

If you need to reposition the head, press [Shift+F7] and make sure the cheat table says that the second element is unlocked. Pressing [F8] should now unlock the head (+ eyes) for further adjustments. [Ctrl+Shift+F7] to lock everything once again.

This can be used together with AMM to 'transfer' look-ats to poses that don't have it enabled. After setting up a custom look-at on a pose that supports it, use AMM > Tools > Lock Look At Camera to lock the look-at. The look-at should now stay when swapped to the pose that has it disabled.

## Broken Mods 
Useful mods broken by the 1.3 update that are worth using once updated. These work fine if you remained on 1.23.


* [City H4ck](https://www.nexusmods.com/cyberpunk2077/mods/808)  
**Features**: Control aspects of Night City such as street lights, TVs and Vehicles.

* [Settings Manager](https://www.nexusmods.com/cyberpunk2077/mods/2332)   
**Features**: Save your game settings to presets, and switch between them anytime


## Useful Links
* [Nexus Mods](https://www.nexusmods.com/cyberpunk2077)
* [Cyberpunk 2077 Modding Discord](https://discord.com/invite/BTApCbE) Many exclusive mods available through Discord.
* [Clothing Catalog](https://steamcommunity.com/sharedfiles/filedetails/?id=2328941813) / [Alternate](https://cp2077.8713.su/) / [Hash list](https://docs.google.com/spreadsheets/d/1CCOmY__uhYhpRixs3XizqwUvx1LICqa2GrmyVpA2Nlc/edit#gid=1420053180)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Cyberpunk_2077)