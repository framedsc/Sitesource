![Grand Theft Auto V](Images\gtav_header.png "Shot by SammirLlm"){.shadowed}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 10, DirectX 11
 


## Essentials


- [Open IV](https://openiv.com): Important tool to manage game’s directories, install ASI loader, mods and edit files.
- [ScripthookV](https://www.dev-c.com/gtav/scripthookv): Essential to use gta v script native functions in custom .asi plugins.
- [Community ScripthookV.NET](https://www.gta5-mods.com/tools/scripthookv-net): Allows running scripts written in any .NET language ingame.
- [Heaplimit adjuster](https://www.gta5-mods.com/tools/heapadjuster): Increases the default game allocator heap (also included with NVE).
- [Packfile limit adjuster](https://www.gta5-mods.com/tools/packfile-limit-adjuster): Doubles the amount of packfiles, aka RPFs, the game can handle.
 

## Tools

- [No Rockstar Editor Restrictions](https://www.gta5-mods.com/scripts/no-rockstar-editor-restrictions): Removes camera limits for Rockstar Editor.
- [Menyoo](https://www.gta5-mods.com/scripts/menyoo-pc-sp): Car/objects spawning/tuning, character customization, poses etc.
- [Native Trainer](https://www.gta5-mods.com/scripts/enhanced-native-trainer-zemanez-and-others) 
- [Simple Trainer](https://www.gta5-mods.com/scripts/simple-trainer-for-gtav): Weather/time, teleporting to locations.

An advantage of using the Rockstar Editor is that byou can save the project and camera position so that crashes arent that impactful.

If you use R editor, don't install NVE motion blur, since it will be captured by R Editor without the possibility to remove it, only use Enhanced Video Editor that lets you tweak it via a dedicated .ini

- Alternative cam: [Freecam V](https://www.gta5-mods.com/scripts/freecamv-net)

## Gameconfig

A custom `gameconfig.xml` is highly recommended if you plan to mod the game and add elements like cars, maps, peds etc. There are a lot of custom Gameconfigs, if you purchase Natural Vision Evolved just install the one that comes with it, otherwise [this](https://www.gta5-mods.com/misc/gta-5-gameconfig-300-cars) one is frequently used.

**Caution**: It’s highly recommended that you create a “mods” folder inside your GTA V main directory in which you have to copy all the folders that are going to be modified before you start modding the game, specifically the “update” folder and the “X64” folder; Open IV will ask you and do this automatically the first time you launch it and everytime you try to edit a file outside of the “mods” folder. 



## Optionals

- [Scene Director](https://www.gta5-mods.com/scripts/scene-director): Many useful functions like spawnable custom lights.
- [Extended Video Editor](https://www.gta5-mods.com/scripts/extended-video-export): Advanced Motion Blur, High-res video export.

## Graphic mods (pick one)

- [NaturalVision Evolved](https://www.patreon.com/razedmods)
- [QuantV 3.0](https://www.patreon.com/QuantV)
- (Free) [QuantV 2.0](https://www.gtainside.com/en/gta5/mods/119996-quantv-2-1-4/): Includes a trainer with a cam tool. 
- (Free) [NaturalVision Remastered (2018)](https://www.youtube.com/watch?v=sctUtDoFLms): DL link in the description.
- (Free) [Visual V](https://www.gta5-mods.com/misc/visualv)

## Textures/LOD Stuff

[GTA V Remastered](https://gta5-mods.com/maps/grand-theft-auto-v-remastered-add-on)

ATTENTION: If you are using Nve and install GTA V remastered or any other similar mod that adds props/custom maps as this will eat up the game's memory and its not really necessary since Nve does add a lot of stuff already. Could lead to vehicles no loading textures correctly among other problems.


## ENB (Optional, tanks performances)

- Default presets Included with NVE
[Personal preset choice](https://www.mediafire.com/file/x0f18rkv6zj470n/MONSTER_KILLER00K%27s_ENB.rar/file) by Monster Killer00k

Attention: If you want to use this ENB preset, or any other custom preset with NVE, always Install the NVE preset first, then open up the third parties' preset folder and drag/drop these three files only into your GTA V main folder: enbseries folder, enbseries.ini and enblocal.ini, overwrite when asked.

- [Suggested](https://nl.gta5-mods.com/scripts/disable-input-on-enb-editor): Disable Input on ENB Editor (No game inputs while ENB editor is open) 




If you want to use ENB toghether with Reshade just edit enblocal.ini with Notepad++ and replace these lines under [PROXY]:

```
EnableProxyLibrary=true
InitProxyFunctions=false
ProxyLibrary=d3d11.dll
```


## Useful tutorials


- [Install Open IV](https://www.youtube.com/watch?v=OPN9YroBcTs)
- [Install NVE](https://www.youtube.com/watch?v=52mwjzOXzo0)
- [Menyoo Tutorial](https://www.youtube.com/watch?v=NvxBWuNXRvw)
- [Crash Fix Ver. 1.2372](https://www.youtube.com/watch?v=NZlF9FbPA6E)
- [List of well optimized mods](https://discord.com/channels/334343104284852224/629894339681583124/775146822988988416) from [Grove Street Families discord server](https://discord.gg/muTdyKjK)




## Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Grand_Theft_Auto_V)
