![Borderlands 3](Images\borderlands3_header.png "Shot by Otis_Inf"){.shadowed}

##Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Ansel | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
DirectX versions | DirectX 11 / 12
 
## Tools

* [Universal Console Unlocker by Otis_Inf and SunBeam](..\GeneralGuides\universal_ue4_consoleunlocker.htm)  
**Features**: Unlocks the UE4 console in order to enter commands / cheats and offers a free camera among other things. The camera also works in 
the photomode. 

## Useful Console Commands

### Tweaks
Recommended console tweaks are the following. You can concatenate them together using the `|` character to one string and
copy/paste them into the console in the game. 

```
sg.ShadowQuality 5|sg.FoliageQuality 5|sg.ViewDistanceQuality 5|sg.PostProcessQuality 5|sg.EffectsQuality 5|sg.TextureQuality 5|r.Shadow.DistanceScale 4|r.Streaming.LimitPoolSizeToVRAM 0|r.Streaming.PoolSize 4096|r.Streaming.MaxTempMemoryAllowed 256|r.SSR.Quality 4|r.MaxQualityMode 1|r.StaticMeshLODDistanceScale 0.001|r.maxanisotropy 16 
```

These set all quality settings to maximum and tweak the in-game streaming configuration so when you switch to a higher resolution it's going to 
load textures much faster than with the default settings. 

### Gameplay / Screenshots

For screenshots, you can use the built-in camera of the UUU, also within the photomode. The debug camera can be handy however, hence it's mentioned below

ToggleDebugCamera
:	Enables the UE4 free camera. Use the UUU camera whenever possible however, use this camera e.g. in combination of TeleportToDebugCamera. 

TeleportToDebugCamera
:	Teleports your character to the current camera location  

slomo 0.5 / slomo 1.0
:	Slow motion / Normal game speed

showhud 0 / showhud 1
:	hides / shows the in-game HUD. This is useful if you're using the debug camera instead of the in-game photomode. It's required to specify this
command before you enable the debug camera otherwise it won't work. 

pause
:	Pauses the game, which can be handy when you're trying to take a shot during a cutscene. The Universal Console Unlocker comes with a timestop
but that doesn't pauses cutscenes properly. Specifying `pause` again continues the game

camera 3rd
:	Switch to 3rd person view. 

camera 1st
:	Switch to 1st person view

### Rendering

r.DepthOfFieldQuality 0
:	Disables the in-game DoF

r.MotionBlurQuality 0
:	Switches off motion blur. This can help with blurry elements when you pause the game and use the debug camera or the in-game photomode. 

r.DefaultFeature.LensFlare 0
:	Disables the lensflare

r.BloomQuality 0
:	Disables the bloom

r.Fog 0
:	Disables the fog

##Tips and Tricks

The console has a history. Simply press arrow-up to get the list of last entered commands. This allows you to quickly switch between previously entered
commands like Pause, r.PostProcessAAQuality 2 etc. 

## Useful links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Borderlands_3)

