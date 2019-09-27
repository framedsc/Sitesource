![ue4guide](Images\ue4_header.png)

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
`sg.PostProcessQuality` | `0` - `4` | changes post-processing quality
`sg.ShadowQuality` | `0` - `4` | changes shadow quality 
`sg.TextureQuality` | `0` - `4` | changes texture quality 
`sg.EffectsQuality` | `0` - `4` | changes effects quality 

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

### Setting custom scalability levels

As scalability groups are simply groups of render settings, you can make "custom profiles" by modifying them. This has many uses, from turning off certain post-processing effects completely, to changing Epic settings to include Cinematic-quality effects, and many more, all without the need of the console.

You will need access to your game's Scalability.ini, typically found through the path `~\AppData\Local\[GAME]\Saved\Config\WindowsNoEditor\Scalability.ini`. 

@alert important
Some games may limit modification of WindowsNoEditor .ini files, meaning your tweaks may not do anything. There is no way to bypass that limitation. 
@end

The file may be empty; that's fine. We'll be modifying it for our own use anyway.

Scalability groups correspond to their command names, without the `sg.` prefix. Each scalability group is denoted by a @ and their level, so the command `sg.PostProcessQuality 3` would look like `[PostProcessQuality@3]` in your file. The square brackets are important!

Here are a few examples of how the file can be modified:

**Removing bloom and motion blur**
```
[PostProcessQuality@3]
r.BloomQuality=0
r.MotionBlurQuality=0
```
This completely removes Bloom and Motion Blur when Post Processing is set to Epic. Quality levels of 0 mean that they are entirely disabled. 

**Cinematic shadows by default**
```
[ShadowQuality@3]
r.Shadow.MaxResolution=8196
r.Shadow.CSM.MaxCascades=16
r.Shadow.RadiusThreshold=0.01
```
This makes shadow maps render at a *very* intensive 8K resolution with much better quality when Shadows are set to Epic.

**"Epic" textures**
```
[TextureQuality@3]
r.Streaming.MipBias=2.5
r.MaxAnisotropy=0
r.Streaming.PoolSize=200
```
When textures are set to Epic, this makes them look the same as they would on Low settings. Why you would do this is beyond me, but it's an example all the same. 

@alert tip
For a full reference to what's capable, check the [Scalability Reference](https://docs.unrealengine.com/en-US/Engine/Performance/Scalability/ScalabilityReference/index.html). Note that these are default settings by Unreal developers, your game is likely to have these already changed.
@end 

**Scalability levels and groups have to be separated with an empty line!**  
With 5 scalability levels per group, you can have 5 different presets for Post-Processing, Shadows, Textures and Effects.

Once you're done, it's recommended to **set the file to Read-only** to prevent the game from changing it. You can do that by right-clicking on the file, enter Properties, tick Read-only under Attributes, and apply.

---

## Engine Renderer Settings

Modifying `Engine.ini` allows you to set render settings by default so that the console isn't needed to change them all the time. It can also be an alternative in the event where modifying `Scalability.ini` has no effects.  
Similar to scalability groups, modifying this file can be used to push the game's graphical limits or optimise it further. 

This file can be typically found through the path `~\AppData\Local\[GAME]\Saved\Config\WindowsNoEditor\Engine.ini`. 

@alert important
Like above, some games may limit edits to this file, causing tweaks to have no effects.
@end

The file needs to be started with `[/script/engine.renderersettings]`. All commands that follow typically have the `r.` prefix, as they relate to rendering properties.

Here's an example of how the file could look like:
```
[/script/engine.renderersettings]
r.ScreenPercentage=150
r.ViewDistanceScale=2
```
This forces the game to always render at 150% native resolution, with draw distance doubled from its native settings. You can also add the same `r.` commands from the scalability groups to enforce them by default.

For a full list of `r.` commands, [click here](https://digilander.libero.it/ZioYuri78/). 

@alert tip
Use the console to test out these commands and find the appropriate values in-game before adding them to the .ini. It'll save time!
@end

@alert important
These commands are meant for the developers. Most are likely to have zero effect as a result. Only a handful of commands meant for runtime (typically those you'd see in graphics settings) may work.
@end

Similar to Scalability.ini, it is recommended to change this file to **Read-only** once you're done.

---
*last updated 27th September 2019*  
*written by moyevka*