![Red Dead Redemption 2](Images\rdr2_header.png "Shot by Otis_Inf"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes, [see notes](#hotsampling)
DSR | Yes
Custom Aspect Ratios | Yes, [with tools](https://framedsc.com/basics.htm#composing-for-custom-aspect-ratios)
Reshade | Yes (v4.4+)
Ansel | No
Graphics API | DirectX 12/Vulkan
 
## Tools
* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)   
**[Features](https://opm.fransbouma.com/Cameras/rdr2.htm)**: Camera control (also in cutscenes), FoV control, HUD toggle, DOF toggle (through ShaderToggler), timestop/gamespeed control, frameskip, camera paths, black bar removal, higher LODs, time of day control, weather control (including mixing weathers)
* [Photomode enhancements by Otis_Inf](..\CheatTables\RDR2_PhotomodeEnhancements_Otis.CT): An alternative to Otis camera tools, altho not as good (e.g. no camera in cutscenes).   
**Features**: Range/limit removal of photomode, removal of black bars in cutscenes and photomode, FoV control, Hotsampling support (DX12 only), Weather control, HUD toggle, Pause/Unpause (also in photomode), Time of day (hour) support
* [jedijosh920's RDR2Trainer](http://discord.gg/wdNC5hn)
* [Rampage Trainer](https://www.nexusmods.com/reddeadredemption2/mods/233)
* [RDR2 Outfit Changer](https://www.rdr2mods.com/downloads/rdr2/scripts/12-rdr-2-outfit-changer/)
* [Photo Mode Enhancer](https://www.rdr2mods.com/downloads/rdr2/scripts/8-photo-mode-enhancer/), if you choose not to use the Photomode Otis_Inf's Camera tools or enhancements CE table
* [Cutscene Freecam](https://www.nexusmods.com/reddeadredemption2/mods/1209)

## Essentials
* [ScripthookRDR2](https://www.nexusmods.com/reddeadredemption2/mods/1472)  
*The [original source](https://www.dev-c.com/rdr2/scripthookrdr2/) might be outdated. The Nexus Mods variant is likely more recent.*
* [Lenny's Mod Loader](https://www.rdr2mods.com/downloads/rdr2/tools/76-lennys-mod-loader-rdr/)

## Texture/Graphic Mods
* [Weapon Texture Upscale](https://www.nexusmods.com/reddeadredemption2/mods/928)  
**Feature**: Upscaled gun textures. (*Vulkan only*)
* [Terrain Textures Overhaul](https://www.nexusmods.com/reddeadredemption2/mods/2189)  
**Feature**: Overhauls most of story mode location terrain textures (*Vulkan only*)
* [Gun Metal Rework](https://www.nexusmods.com/reddeadredemption2/mods/648)  
**Feature**: Updates the look of the in-game guns' metal finishes.
* [Higher Resolution Vegetation](https://www.nexusmods.com/reddeadredemption2/mods/1553)  
**Feature**: Uses unused 1024x1024 resolution textures for some of the game's vegetation. (*Vulkan only*)
* [WhyEm's Particles](https://www.nexusmods.com/reddeadredemption2/mods/1526)  
**Feature**: Increases particle counts for various aspects of the game world, and increases their quality.
* [Visual Redemption](https://discord.gg/ADfQxWSv6J)  
**Feature**: Slight graphics overhaul that doesn't change too much of the original game's visuals.
* [Vignette Disabler](https://www.nexusmods.com/reddeadredemption2/mods/1569)  
**Feature**: Disables the vignette visible in-game.
* [The Perfect TAA](https://www.nexusmods.com/reddeadredemption2/mods/1222)  
**Feature**: Attempts to fix ugly TAA blurring. Good for 1080p, however hotsampling to 4K and higher defeats its purpose.
* [DLSSTweaks for RDR2](https://www.nexusmods.com/reddeadredemption2/mods/2072)
**Feature**: Allows forcing DLAA, changing the presets used for each DLSS level, and swapping of the DLSS DLL.

### Hotsampling
While it's possible to hotsample with Vulkan, it can be unstable compared to DX12. [SRWE](https://framedsc.com/basics.htm#hotsampling) often loses track of which window to handle as well. This can be fixed by `Refreshing` the `Window Tree`, which will allow you to select the game and edit the resolution again. This problem does not occur with Otis_Inf's tools.

@alert info
The game hotsamples with Otis_Inf's tools & SRWE problem-free when running in DX12.
@end

@alert important
Hotsampling to a 32:9 aspect ratio and going back to your original one will break every trainer menu, with some losing the text, and some having the text way off the screen.
@end

### Vulkan or DX12?
If you're using Windows 7 or 8.x, the only option you have is Vulkan. If you use Windows 10/11, you can use DX12 as well. There are reports of higher performance under Vulkan, but also lower-res textures and overall worse fidelity (though marginal). The cheat table and tools should work with either graphic API. Regardless of API, the game is highly unstable, and you have to prepare for crashes during your gameplay session.

@alert important
Most texture mods do not work in DX12, making it a trade-off if you are willing to modify the game textures.
@end

## Tweaks & tips

It is possible to adjust elements of the visuals beyond what is available through the in-game settings. Be aware that adjusting these can be taxing on your system, and that the LOD tweak is not necessary when using Otis_Inf's tools due to the built-in LOD toggle.

In the file `My Documents\Rockstar Games\Red Dead Redemption 2\Settings\system.xml`:

- Search for `<lodScale value="...." />` and `<pedLodBias value="...." />`, and set these to 1.0, by default they're set to 0.0
- search for `<deepsurfaceQuality>...</deepsurfaceQuality>`, set the value to kSettingLevel_Ultra.

@alert info
As of the Blood Money (Version 1.25. July 13th, 2021) update, some graphics settings revert back to their default values. The graphics settings are: "Resolution Scaling" `off`, "TAA" `high`, "MSAA" `off`. It is currently not possible for them to stay changed.
@end

@alert info
If you have visual artifacts that look similar to GPU VRAM artifacts (green, purple, white noise) in the game (usually noticed in the main menu), turn `off` "Triple Buffering".
@end

@alert neutral
Bypassing the in-game VRAM limit can only be done by changing the values through the `system.xml` file.
@end

### ReShade

@alert warning
Reshade is known to cause issues with this game. DX12 is especially unstable with ReShade installed, while Vulkan can run better with it. A potential mitigation for this is to run no shaders during the menu/loading process, and enable shaders only once you have loaded into the world. This is not a guaranteed fix!
@end

The installation folder for this game may be marked as 'Read-only' which can block ReShade from writing to config files. 
To fix this, the folder needs to be set to have write access for the system user.

To do this, open Command Prompt and first type in `takeown /f "<Game Directory Path>" /r` followed by `attrib -r "<Game Directory Path" /s`
This intends to enable write privileges for the system user, allowing Reshade to work properly, as well as any mods that may be potentially affected.

*Source:* [Reddit](https://www.reddit.com/r/techsupport/comments/oejd98/why_in_the_holy_f_can_i_not_turn_readonly_off_on/)

### CT Weather control

Both Otis_Inf's camera tools and the cheat table offer two ways to control the weather: one option is to set the weather type, and another is to define a combination between two weathers. 
In the camera tools, these weathers are found in the 'Image adjustments' tab with drop-down menus for each of the weathers you wish to mix.
The cheat table requires you to adjust some values to change and blend the weathers. Below is a guide on how to do this.

#### Different weather types

Weathers are defined using a number. -1 (or in hexadecimal: `FFFFFFFF`) means that no weather is set and the default weather is used. 

<details><summary>List of weather types</summary>

Value | Weather name
--|--
0 | High pressure
1 | Sunny
2 | Misty
3 | Fog
4 | Clouds
5 | Overcast
6 | Overcast dark
7 | Drizzle
8 | Rain
9 | Thunder
10| Thunderstorm
11| Hurricane
12| Shower
13| Hail
14| Sleet
15| Snow clearing
16| Snow light
17| Snow
18| Blizzard
19| Ground blizzard
20| Whiteout
21| Sandstorm

</details>

#### How to set the weather
To set the active weather, enable the 'Weather control' entry in the table by clicking the check box in front of it. Then, double-click the value in the 'Weather type' entry on the right. By default, it'll show 'FFFFFFFF'. Double-clicking it allows you to type a new weather, e.g. 4 for cloudy weather. The weather change will be instant and also works in photomode.

@alert neutral
In-game trainers can also be used to change the weather.
@end

#### How to set a combination of two weather types
If you want to create your own unique weather, you can create a combination of two weather types. 
After you've enabled 'Weather control', you can then check 'Enable weather interpolation'. After that, you double-click the value in the 'From weather' entry and type a value, e.g. 4 for cloudy weather. Then you double-click the value in the 'To weather' column and also specify a value, e.g. 14 for thick snow. 

You can then define the amount of how much of one or the other should be used using the 'Interpolation factor'. Double-click the value of that entry to specify a value between 0 and 1, e.g. 0.3. If you e.g. specify 0.3 it means the weather is 70% the 'From weather' weather and 30% the 'To weather'. 

To go back to the other weather option, simply disable the 'Enable weather interpolation' entry.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Red_Dead_Redemption_2)
* [How to install and use Lenny's Mod Loader](https://www.youtube.com/watch?v=E-OIFFcIKDs) (YouTube)
* [Using Cheat Engine Tables](../GeneralGuides/cheat_engine_tables.htm)
* [system.xml Settings Parser](https://rdr2.forceflow.be/)
