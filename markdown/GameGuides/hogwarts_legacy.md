![Hogwarts Legacy](Images\hogwarts_legacy.png "Shot by Dread"){.shadowed .autosize}
## Summary
Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes (use windowed fullscreen)
DSR | No
Custom Aspect Ratios | Yes  
Reshade | Yes
Ansel | Yes (full support)
Graphics API | DirectX 12
 
## Tools

* [Unreal Engine Unlocker](https://framedsc.com/GeneralGuides/universal_ue4_consoleunlocker.htm)  
**Free Features**: 
Free: Camera, HUD toggle, Hotsampling, console, timestop  
**Patreon Features**: Free features + Custom lights, post processing, camera paths, weather control, change seasons
* [Cheat Engine script by Sunbeam](..\CheatTables\HogwartsLegacy.CT)  
**Features**: Time of day  
Enable script, use [ ] keys to change time of day or hold ctrl for bigger changes (or set your own hotkeys)

## Tips and Tricks

### Hide white outlines

Using the console, hide outlines with:  
`r.customdepth 0`  
Show white outlines:  
`r.customdepth 3`  

### Tweaks
The tweaks below will likely harm performance in the game, so try to use only the ones that work well with your hardware. It's probably wise to create a
series of commands with the default values that the cvars have by default. To get these values, type in the cvar without a value on the console. Open the console's 
bigger view (press the open console key twice) to see the value. This might sound tedious but as you can concat all these cvars to one big line where you separate the cvars with `|` 
characters and you can copy/paste the line into the console, you have to this just once. This way you can flip back and forth between a set of values that work during gameplay 
and a set of values that make the game look really good but have a serious impact on performance. 

To make the game look the best it can be, use these:
```
r.maxanisotropy 16|r.Streaming.LimitPoolSizeToVRAM 0| r.Streaming.MaxTempMemoryAllowed 4096|r.SceneColorFringe.Max 0| r.StaticMeshLODDistanceScale 0.001 | foliage.LODDistanceScale 6 | r.LightFunctionQuality 2 | r.gbufferformat 5 | r.VolumetricFog.HistoryMissSupersampleCount 16 | r.RayTracing.Reflections.ScreenPercentage 70 | r.Shadow.DistanceScale 2 | r.tonemapper.sharpen 0.5 | r.MipMapLODBias -1 | r.RayTracing.Reflections.SamplesPerPixel 1| r.RayTracing.AmbientOcclusion.Intensity 1 |  r.RayTracing.Reflections.ScreenPercentage 70 | r.RayTracing.Reflections.MaxRoughness 1.0 | r.Reflections.Denoiser.ReconstructionSamples 8 | r.Reflections.Denoiser 2 | r.Shadow.WholeSceneShadowCacheMb 1024 | r.RayTracing.Shadows.Lights.Directional 1 | LightCullingRenderThread.MaxRTShadowedLights 32 | LightCullingRenderThread.MaxDynamicShadowedLights 32 | r.VT.MaxUploadsPerFrame 24 | r.VT.MaxContinuousUpdatesPerFrame 24 | r.Streaming.PoolSize 2500 | r.Streaming.PoolSizeForMeshes 1500 | r.NGX.DLSS.DenoiserMode 1 | r.RayTracing.Reflections.ExperimentalDeferred.SmoothBias 1 | r.RayTracing.Shadows.FarObjectsNormalBias 0
```

A lot of these tweak raytracing, and especially reflections, it's therefore key to enable raytracing in the game's settings. 

You don't have to look up all these cvars and switch back/forth for gameplay/shots. The biggest performance hogs are: `r.StaticMeshLODDistanceScale`, `foliage.LODDistanceScale`, `r.Shadow.DistanceScale`, `LightCullingRenderThread.MaxRTShadowedLights`, `LightCullingRenderThread.MaxDynamicShadowedLights`. 

To help with performance, the following tweaks can be used at any time to switch to a look that's more shot friendly but will likely run slow:

- Switch DLSS type: `r.NGX.DLSS.Quality <value>`, where `<value>` is e.g. `1` for `Quality` and `3` for `DLAA`. So to go from DLSS Quality (1) to native res, type `r.NGX.DLSS.Quality 3` and to go back to 
  DLSS Quality, type `r.NGX.DLSS.Quality 1`. `<value>` can also be `2` for `Ultra Quality` which is less good than `Quality`, `0` for `Performance` and `-1` for `Ultra performance`. 
- Switch on/off raytraced reflections: `r.RayTracing.Reflections 1` for on and `r.RayTracing.Reflections 0` for off. 

Additionally, for outdoor environments (you can try this indoors, but it'll look awful), you can switch on raytracing on the skylight (sun). To switch it on and calibrate the shadow darkness, use:
`r.RayTracing.Skylight 1 | r.SkylightIntensityMultiplier 0.3` and to switch back use: `r.RayTracing.Skylight 0 | r.SkylightIntensityMultiplier 1`. Try different values for the multiplier, the lower
the darker. 

### Change seasons without UUU

Download and install this mod (requires another mod to be installed first).
[https://www.nexusmods.com/hogwartslegacy/mods/57?tab=description](https://www.nexusmods.com/hogwartslegacy/mods/57?tab=description) 

Follow the installation instructions on the mod page how to install it, and setting it up. After properly installing the mod, you can 
use the normal console to use the weather commands.

```
HL_ChangeSeason spring
HL_ChangeSeason fall
HL_ChangeSeason winter
```

After entering the command, you'll need to fast travel for the textures to switch to the selected season.