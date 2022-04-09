![ue4guide](Images\ue4_header.png){.shadowed}

Games using Unreal Engine 4 can be tweaked in many ways to better your experience in-game or while shooting. This guide covers the basics of what you can do, with or without UUU and the console.

---

## Console Commands

Command | Arguments| Description
-- | -- | --
`EnableCheats` | `0` - `1` | enables cheats (needed for most games)
`toggledebugcamera` | - | enables freecam (WASD + mouselook)
`fov` | `1` - `180` | changes field of view (in degrees)
`pause` | - | toggles game timestop
`r.ScreenPercentage` | `10` - ?? | sets resolution scale (in %)
`r.ViewDistanceScale` | `0.0` - ?? | sets draw distance
`r.PostProcessAAQuality` | `0` - `6` | changes AA quality (FXAA / TAA)
`r.Depthoffieldquality` | `0` - `6` | changes the depth of field quality (from 0: off to 6: max)
`r.SceneColorFringeQuality` | `0` - `1` | toggles CA off (0) or on (1).
`r.Motionblurquality` | `0` - `4` | changes the motion blur quality (from 0: off to 4: max)
`sg.PostProcessQuality` | `0` - `4` | changes post-processing quality
`sg.ShadowQuality` | `0` - `4` | changes shadow quality 
`sg.TextureQuality` | `0` - `4` | changes texture quality 
`sg.EffectsQuality` | `0` - `4` | changes effects quality 
`r.customdepth 0` | `0` - `3` | changes the visibility of outlines, other elements like focus circles

*Commands are not case-sensitive!*

Commands that have `??` upper limits listed technically have none.  
`r.ScreenPercentage` is render scale based  on your current resolution in %; values above 200 should not be necessary.  
`r.ViewDistanceScale` is a multiplier based on draw distance values set by developers. Unless the default maximum draw distance is very low, a value above 2 should not be necessary.

@alert important
**These commands require the console to be used.** You will most likely need the [Universal UE4 Console Unlocker](https://framedsc.github.io/GeneralGuides/universal_ue4_consoleunlocker.htm) to access the console.
@end

Commands unrelated to screenshotting are not included.

### Chaining commands

The console supports copy-pasting and commands can be chained with `|`.   
For example, if you wanted the game to:

1. Pause
2. Enable the debug camera
3. Set FoV to 50

all at the same time, you would just need to paste `pause | toggledebugcamera | fov 50` into the console.

---

## Scalability Groups

Some commands above start with the prefix `sg.` - these are scalability groups. Scalability groups come in levels that correspond to Low / Medium / High / Epic, as you'd find in a graphics settings menu. In-game settings usually display Level 0 (Low quality) up to Level 3 (Epic quality). You can force it up to Level 4 (Cinematic quality) through the console, at the obvious cost of performance.

*Games may occasionally include a Level 5 Scalability Group, you can go to that for maximum settings.   
Or you can continue to read to learn how to make your own **Super** Cinematic scalability group.*

### Setting custom scalability levels

As scalability groups are simply groups of render settings, you can make "custom profiles" by modifying them. This has many uses, from turning off certain post-processing effects completely, to changing Epic settings to include Cinematic-quality effects, and many more, all without the need of the console.

You will need access to your game's Scalability.ini, typically found through the path `~\AppData\Local\[GAME]\Saved\Config\WindowsNoEditor\Scalability.ini`. 

@alert warning
Some games may limit modification of WindowsNoEditor .ini files, meaning your tweaks may not do anything. There is no way to bypass that limitation. 
@end

The file may be empty; that's fine. We'll be modifying it for our own use anyway.

Scalability groups correspond to their command names, without the `sg.` prefix. Each scalability group is denoted by a @ and their level, so the command `sg.PostProcessQuality 3` would look like `[PostProcessQuality@3]` in your file. The square brackets are important!

Here are a few examples of how the file can be modified:

@tabs
@tab Removing bloom and motion blur
```ini
[PostProcessQuality@3]
r.BloomQuality=0
r.MotionBlurQuality=0

```
This completely removes Bloom and Motion Blur when Post Processing is set to Epic. Quality levels of 0 mean that they are entirely disabled. 
@end
@tab Cinematic shadows by default
```ini
[ShadowQuality@3]
r.Shadow.MaxResolution=8196
r.Shadow.CSM.MaxCascades=16
r.Shadow.RadiusThreshold=0.01

```
This makes shadow maps render at a *very* intensive 8K resolution with much better quality when Shadows are set to Epic.
@end
@tab "Epic" textures
```ini
[TextureQuality@3]
r.Streaming.MipBias=2.5
r.MaxAnisotropy=0
r.Streaming.PoolSize=200

```
When textures are set to Epic, this makes them look the same as they would on Low settings. Why you would do this is beyond me, but it's an example all the same. 
@end
@endtabs 

@alert info
For a full reference to what's capable, check the [Scalability Reference](https://docs.unrealengine.com/4.27/en-US/TestingAndOptimization/PerformanceAndProfiling/Scalability/ScalabilityReference/). Note that these are default settings by Unreal developers, your game is likely to have these already changed.
@end 

**Scalability levels and groups have to be separated with an empty line!**  
With 5 scalability levels per group, you can have 5 different presets for Post-Processing, Shadows, Textures and Effects.

Once you're done, it's recommended to **set the file to Read-only** to prevent the game from changing it. You can do that by right-clicking on the file, enter Properties, tick Read-only under Attributes, and apply.

## Engine Renderer Settings

Modifying `Engine.ini` allows you to set render settings by default so that the console isn't needed to change them all the time. It can also be an alternative in the event where modifying `Scalability.ini` has no effects.  
Similar to scalability groups, modifying this file can be used to push the game's graphical limits or optimise it further. 

This file can be typically found through the path `~\AppData\Local\[GAME]\Saved\Config\WindowsNoEditor\Engine.ini`. 

@alert warning
Like above, some games may limit edits to this file, causing tweaks to have no effects.
@end

The file needs to be started with `[/script/engine.renderersettings]`. All commands that follow typically have the `r.` prefix, as they relate to rendering properties.

Here's an example of how the file could look like:
```ini
[/script/engine.renderersettings]
r.ScreenPercentage=150
r.ViewDistanceScale=2
```

This forces the game to always render at 150% native resolution, with draw distance doubled from its native settings. You can also add the same `r.` commands from the scalability groups to enforce them by default.

## All UE4 console commands and variables

To know more about which commands are available and which variables you can set through the console you can use the following search engine: [https://digilander.libero.it/ZioYuri78/](https://digilander.libero.it/ZioYuri78/). 

This search engine allows you to search on both description and command/variable so it's easy to find the command or variable you're after. The engine gives the variables of the
latest public UE4 build, so it might be the game you're using the UUU with is of an earlier version and doesn't support the variable.

@alert tip
Use the console to test out these commands and find the appropriate values in-game before adding them to the .ini. It'll save time!
@end    

@alert info
These commands are meant for the developers. Most are likely to have zero effect as a result. Only a handful of commands meant for runtime (typically those you'd see in graphics settings) may work.
@end

Similar to Scalability.ini, it is recommended to change this file to **Read-only** once you're done.

## Examples

The following examples are ready to use. You can just copy / paste the contents of each tab into the console using ctrl-C / ctrl-V and hit enter. 

@tabs
@tab High end gameplay
sg.ShadowQuality 5 | sg.FoliageQuality 5 | sg.ViewDistanceQuality 5 | sg.PostProcessQuality 5 | sg.EffectsQuality 5 | sg.TextureQuality 5 | r.DepthOfFieldQuality 5 | r.motionblurquality 0 | r.Shadow.DistanceScale 4 | r.Streaming.LimitPoolSizeToVRAM 0 | r.Streaming.PoolSize 4096 | r.Streaming.MaxTempMemoryAllowed 256 | r.SSR.Quality 4 | r.MaxQualityMode 1 | r.StaticMeshLODDistanceScale 0.001 | r.maxanisotropy 16 | foliage.LODDistanceScale 100 | r.MipMapLODBias -15 | r.AmbientOcclusionMaxQuality -100 | r.Shadow.SpotLightTransitionScale 4096 | r.SkeletalMeshLODBias -1 | r.Shadow.TransitionScale 4096
@end
@tab Normal gameplay
sg.ShadowQuality 4 | sg.FoliageQuality 4 | sg.ViewDistanceQuality 4 | sg.PostProcessQuality 4 | sg.EffectsQuality 4 | sg.TextureQuality 4 | r.DepthOfFieldQuality 5 | r.motionblurquality 0 | r.Shadow.DistanceScale 1 | r.Streaming.LimitPoolSizeToVRAM 0 | r.Streaming.PoolSize 4096 | r.Streaming.MaxTempMemoryAllowed 256 | r.SSR.Quality 4 | r.StaticMeshLODDistanceScale 0.001 | r.maxanisotropy 8 | foliage.LODDistanceScale 1 | r.MipMapLODBias 0 | r.AmbientOcclusionMaxQuality 1 | r.Shadow.SpotLightTransitionScale 60 | r.SkeletalMeshLODBias 20 | r.Shadow.TransitionScale 20
@end
@tab High end screenshots
sg.ShadowQuality 5 | sg.FoliageQuality 5 | sg.ViewDistanceQuality 5 | sg.PostProcessQuality 5 | sg.EffectsQuality 5 | sg.TextureQuality 5 | r.DepthOfFieldQuality 0 | r.motionblurquality 0 | r.Shadow.DistanceScale 4 | r.Streaming.LimitPoolSizeToVRAM 0 | r.Streaming.PoolSize 4096 | r.Streaming.MaxTempMemoryAllowed 256 | r.SSR.Quality 4 | r.MaxQualityMode 1 | r.StaticMeshLODDistanceScale 0.001 | r.maxanisotropy 16 | foliage.LODDistanceScale 100 | r.MipMapLODBias -15 | r.AmbientOcclusionMaxQuality -100 | r.Shadow.SpotLightTransitionScale 4096 | r.SkeletalMeshLODBias -1 | r.Shadow.TransitionScale 4096 | r.Shadow.MaxResolution 8192 | r.Shadow.MaxCSMResolution 8192
@end
@endtabs

There are some per-scene tweaks recommended, especially for screenshots. These are listed below

CVar | Value | Effect
--|--
r.Shadow.SpotLightTransitionScale | 60 (default) | Large areas have a low amount of shadows from far away lights. Reflected highlights look more pronounced
r.Shadow.SpotLightTransitionScale | 512 | More shadows are cast by lights further away, shadows near the camera are more pronounced
r.Shadow.SpotLightTransitionScale | 4096 | Most lights cast shadows everywhere. 
r.Shadow.MaxResolution | 2048 | Blurry shadows but high performance
r.Shadow.MaxResolution | 4096 | Sharper shadows, lower performance. Can still show banding on objects near the camera
r.Shadow.MaxResolution | 8192 | High quality shadows, no banding on near-camera objects
r.Shadow.MaxResolution | 16384 | Your game will crash

## Fixing issues

### Shadow striping with low fov
You can sometimes run into shadow striping with low FoV. To fix this, you have to set the Depth Bias for the light that causes this. This can be a pointlight, directional light or spotlight. The commands to try are:

* `r.Shadow.PointLightDepthBias`
* `r.Shadow.CSMDepthBias`
* `r.Shadow.PerObjectDirectionalDepthBias`
* `r.Shadow.SpotLightDepthBias`

Usually, a value of around 0.15 should fix it.

![Shadow banding and fix](Images\MiscGuides\ue4_shadowbanding.png){.shadowed}
