![Cyberpunk 2077](Images\cyberpunk2077_header.png "Shot by Lazaro"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes, 4.9.1 is recommended.
Ansel | No
DirectX versions |  DirectX 12
Guide Updated For Game Version | 1.3
 
## Tools

* [Camera Tools with Cyberlit by Otis_Inf](https://patreon.com/Otis_Inf)   
**Features**: Photo Mode Camera control, FOV Control, Custom Aspect Ratios, Time Of Day, Camera Paths and custom lights.  
* [Photomode Improvement with lookat controls CT By Deadendthrills and Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Lock torso/head in place to control eyes separately.

## Essential Mods

* [Cyber Engine Tweaks](https://www.nexusmods.com/cyberpunk2077/mods/107) / [Wiki](https://wiki.redmodding.org/cyber-engine-tweaks/)
Required by many mods.

* [Cybercat Save Editor](https://www.nexusmods.com/cyberpunk2077/mods/718)  
**Features**: Edit the appeareance of V without starting a new game.

##  Mods for Setting Up Screenshots

* [Appearance Menu Mod](https://www.nexusmods.com/cyberpunk2077/mods/790) / [Discord](https://discord.com/invite/47jV2rNdgn)  
**Features**: Spawn, move and remove characters and objects. Save and teleport to locations. And much more.
* [Freefly](https://www.nexusmods.com/cyberpunk2077/mods/780)  
**Features**: Enable noclip to fly V to places you wouldn't normally be able to reach.

## Graphical Tweaks
* [Update Nvidia DLSS](https://www.techpowerup.com/download/nvidia-dlss-dll/)   
  Update DLSS from 2.1 to 2.2.X. Add to \Cyberpunk 2077\bin\x64 and overwrite. Tested up to 2.2.16.

* [Cinematic RTX](https://www.tomshardware.com/uk/news/how-to-unlock-cyberpunk-2077-cinematic-rtx-mode)   
 Add an extra level of ray tracing.

 * Increase Draw Distance and Reduce Pop-in. __Your mileage may vary with this one__.
 In `\Cyberpunk 2077\engine\config\platform\pc` create a new file called `DrawDistanceBoost.ini` and paste the following:
 ```
 [Streaming]
DistanceBoost = 60.000000
``` 
 In ```\Cyberpunk 2077\engine\config\platform\pc``` open ```rendering.ini``` and change it to:
 ```
[LevelOfDetail]
DecalsHideDistance = 100.0
```

## Tips and Tricks


* Create more natural poses by using Appearence Menu Mod to swap an NPC to V (or anyone) to have them play out their NPC animations, enter photomode when you see a pose you want.
  * See also: [NoraLee's Pose Mod](https://www.nexusmods.com/cyberpunk2077/mods/2831) and [Ferret's Poses](https://www.nexusmods.com/cyberpunk2077/mods/2718), amongst many others.
* In the abscense of Cyberlit, Use Appearence Menu Mod to spawn in game light objects to light up a scene, allbeit with less control. 
* There can often be lots of artifacting around hair textures and these are amplified when using various reshade effects. One way to minimise this is to use [Reallongexposure.fx from CobraFX](https://github.com/LordKobra/CobraFX) to create a 'long exposure' which helps to blend together the issues. This is less of an issue with DLSS enabled.  [Example.](../Images/cp_RLEexample.png)
* Using Cyberlit, create a 0 intensity light to use as a camera anchor point then use 'Move camera to light' to quickly get back to your shot angle. The same can be done by using ICGS camera paths to create multiple camera points.
* Spawn objects to create scenes or photo studios.
  [Example.](../Images/cp_AMMexample.png)
* Disable in game depth of field completely, photo mode included, by going inside `\Cyberpunk 2077\engine\config\platform\pc` create a new filed called `DisableDepthOfField.ini`  and paste the following:
```
[Developer/FeatureToggles]

DepthOfField = False
```
* In the event of another game update breaking lots of mods, you can make a copy of your `Cyberpunk 2077` game folder before the update and play it outside of Steam/GOG whilst you wait for mod updates or if you prefer to stick to a certain version of the game.
* If you find Reshade is causing performance issues, enable `copy depth buffer before clear operations` until it's time to compose a shot.

## Broken Mods 
Useful mods broken by the 1.3 update that are worth using once updated. These work fine if you remained on 1.23.

* [Photo Mode Unlocked](https://www.nexusmods.com/cyberpunk2077/mods/3035)  
**Features**: Enables look at for any pose. Removes many limits of photo mode.

* [City H4ck](https://www.nexusmods.com/cyberpunk2077/mods/808)  
**Features**: Control aspects of Night City such as street lights, TVs and Vehicles.

* [Settings Manager](https://www.nexusmods.com/cyberpunk2077/mods/2332)   
**Features**: Save your game settings to presets, and switch between them anytime

* [Object Spawner](https://www.nexusmods.com/cyberpunk2077/mods/2833)   
 **Features**: Spawn over 16k different items. 
 
## Useful Links
* [Nexus Mods](https://www.nexusmods.com/cyberpunk2077)
* [Cyberpunk 2077 Modding Discord](https://discord.com/invite/BTApCbE) Many exclusive mods available through Discord.
* [Cyberlit Guide](../GeneralGuides/cyberlit.htm)
* [Clothing Catalog](https://steamcommunity.com/sharedfiles/filedetails/?id=2328941813) / [Alternate](https://cp2077.8713.su/) / [Hash list](https://docs.google.com/spreadsheets/d/1CCOmY__uhYhpRixs3XizqwUvx1LICqa2GrmyVpA2Nlc/edit#gid=1420053180)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Cyberpunk_2077)