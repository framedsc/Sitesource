![Darksiders 3](Images\darksiders3_header.png "Shot by Otis_Inf"){.shadowed}

##Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Ansel | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
DirectX versions | DirectX 11
 
## Tools

* [Console Unlocker by Sunbeam](http://fearlessrevolution.com/viewtopic.php?t=8318)  
**Features**: Unlocks the UE4 console in order to enter commands / cheats. See below what to do to enable
the free camera.

* [Cheat table by Otis_Inf](..\CheatTables\darksiders3.CT)  
**Features**: Toggle HUD, Pause game, change resolution scaling beyond 100%. 

## Ini tweaks

To get the best out of the game, it's crucial to edit the game's ini files. These can be found in the following location:
`%LOCALAPPDATA%\Darksiders3\Saved\Config\WindowsNoEditor`. You can copy that location and paste it into the location bar of Windows Explorer ('This PC ...').
If you go into the graphics options in-game you likely will reset some values, 
so be sure to first set all options in the in-game graphics to your liking (e.g. running in windowed mode for hotsampling), quit the 
game and then edit these files. 

### GameUserSettigs.ini
Open this file in a text editor, e.g. notepad++ and under `[DS3.Graphics]` change the following values to 4.0:
```
ShadowQuality=4.000000
AntiAliasing=4.000000
ViewDistance=4.000000
TextureQuality=4.000000
PostProcessing=4.000000
EffectsQuality=4.000000
FoliageQuality=4.000000
```

Under `[ScalabilityGroups]` change the following values to '4':
```
sg.ViewDistanceQuality=4
sg.AntiAliasingQuality=4
sg.ShadowQuality=4
sg.PostProcessQuality=4
sg.TextureQuality=4
sg.EffectsQuality=4
sg.FoliageQuality=4
```

### Engine.ini
Below the lines already there (the 'Paths=...' lines) add the following section:
```
[SystemSettings]
r.Shadow.DistanceScale=4
r.MaxAnisotropy=16
r.Tonemapper.Sharpen=0.7
r.SceneColorFringeQuality=0
r.Streaming.LimitPoolSizeToVRAM=0
r.Streaming.PoolSize=4096
r.AmbientOcclusionMaxQuality=1
r.AmbientOcclusionLevels=3
r.AmbientOcclusionRadiusScale=0.08
r.AmbientOcclusion.Compute=1
r.Streaming.MaxTempMemoryAllowed=256
```

Below are the explanations for these. You can alter these in the console at any time.

r.Shadow.DistanceScale
:	The value 4 set the shadow distance scale to 'epic' which makes sure shadows are not vanishing further away

r.MaxAnisotropy
:	Maximum anisotropy setting. Default in the game is 8, 16 is more appropriate

r.Tonemapper.Sharpen
:	Sets the sharpening of the in-game tonemapper. 0.7 is a slight adjustment to the default value as it's a bit blurry at times due to the TAA.

r.SceneColorFringeQuality
:	Setting this to 0 kills any CA the game adds

r.Streaming.LimitPoolSizeToVRAM
:	When set to 0 it allows to increase the pool size

r.Streaming.PoolSize
:	Bigger pool size for streaming, increases stream speed.

r.Streaming.MaxTempMemoryAllowed
:	By default this is 50. Setting it to 256 makes switching to e.g. 5K much faster: it won't have to stream in textures again at a low speed.

r.AmbientOcclusionMaxQuality
:	Setting this to 1 (default is 100) allows for better AO, which is by default non-existent.

r.AmbientOcclusionLevels
:	Having this set to 3 allows for more occlusion levels to be used, which increases AO quality

r.AmbientOcclusionRadiusScale
:	By default this is 1. Setting it to a low value, e.g. 0.08, makes AO much more profound. Lower values might look better
in some situations but overdo things a bit in other.

r.AmbientOcclusion.Compute
:	Having this set to 1 makes AO use compute shaders instead of pixel shaders. This increases AO quality.

## Useful Console Commands

### Gameplay / Screenshots

ToggleDebugCamera
:	Enables the UE4 free camera

TeleportToDebugCamera
:	Teleports your character to the current camera location  

slomo 0.5 / slomo 1.0
:	Slow motion / Normal game speed

### Rendering

r.DepthOfFieldQuality 0
:	Disables the in-game DoF

r.PostProcessAAQuality 2
:	Switches the TAA to FXAA. This is ideal when you paused the game and the TAA ruins the shot because some pixels are still in motion.
To get back to the proper TAA for gameplay, use `r.PostProcessAAQuality 6`

r.DefaultFeature.LensFlare 0
:	Disables the lensflare

r.BloomQuality 0
:	Disables the bloom

r.Fog 0
:	Disables the fog

##Tips and Tricks

The console has a history. Simply press arrow-up to get the list of last entered commands. This allows you to quickly switch between previously entered
commands like ToggleDebugCamera, r.PostProcessAAQuality 2 etc. It's advisable to switch off the HUD before enabling the debug camera, as sometimes some HUD
elements aren't hidden when the debug camera is enabled. 

There's no tilt in the Debug camera in Unreal Engine. Best way to control it is via the keyboard + mouse. Use mouse wheel to control the movement speed, WASD for
movement and Q + E to move up/down.

## Useful links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Darksiders_III)

