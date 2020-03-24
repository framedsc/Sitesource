![Star Wars Jedi: Fallen Order](Images\swjfo_header.png "Shot by Ichisake"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes*
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [Injectable camera for Star Wars Jedi: Fallen Order by Frans Bouma & Skall](https://github.com/FransBouma/InjectableGenericCameraSystem/tree/master/Cameras/SWFO)  
**Features**: Freecam (Movement & Rotation), FOV Control, Panorama / lightfield shots, black bar removal from cutscenes.

* [UE4 Console Unlocker by Frans Bouma & Sunbeam](../GeneralGuides/universal_ue4_consoleunlocker.htm)  
**Features**: Enable Official Photo Mode, FOV Control, Hide HUD, timestop/pause (multiple options), debug console for tweaks. Read the UE4 console unlocker guide for details
and the [UE4 tweak guide](../GeneralGuides/ue4guide.htm) for hints.


## Tips and Tricks

Useful console commands: 

TogglePhotoMode
:	Enables the official photo mode for Fallen Order by Respawn.

`r.DepthOfFieldQuality 0` 
:	Disables the vanilla DOF

`r.motionblurquality 0`
:	Disables the motion blur

The console has a history. Simply press arrow-up to get the list of last entered commands. This allows you to quickly switch between 
previously entered commands like r.PostProcessAAQuality 2 etc. It's advisable to use the `PageDown` based timestop provided by the console unlocker as that one works
in cutscenes too.

## Useful links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Star_Wars_Jedi:_Fallen_Order)