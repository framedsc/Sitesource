![Red Dead Redemption 2](Images\rdr2_header.png "Shot by Otis_Inf"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes (with tools, dx12 only)
DSR | Yes
Custom Aspect Ratios | Yes (with tools)
Reshade | Yes (v4.4+)
Ansel | No
Graphics API | DirectX 12
Vulkan | Yes
 
## Tools
* [Photomode enhancements by Otis_Inf](..\CheatTables\RDR2_PhotomodeEnhancements_Otis.CT)  
**Features**: Range/limit removal of photomode, removal of black bars in cutscenes and photomode, FoV control, Hotsampling support (dx12 only),
Weather control, HUD toggle, Pause/Unpause (also in photomode), Time of day (hour) support
* [jedijosh920's RDR2Trainer](http://discord.gg/wdNC5hn)
* [Rampage Trainer](https://www.nexusmods.com/reddeadredemption2/mods/233)
* [RDR2 Outfit Changer](https://www.rdr2mods.com/downloads/rdr2/scripts/12-rdr-2-outfit-changer/)
* [Photo Mode Enhancer](https://www.rdr2mods.com/downloads/rdr2/scripts/8-photo-mode-enhancer/) if you choose not to use the CE table
* [Cutscene Freecam](https://www.nexusmods.com/reddeadredemption2/mods/1209)

## Essentials
* [ScripthookRDR2](https://www.nexusmods.com/reddeadredemption2/mods/1472) The original source is: <https://www.dev-c.com/rdr2/scripthookrdr2/>
however this version might be outdated. The nexus mods variant is likely more recent.
* [Lenny's Mod Loader](https://www.rdr2mods.com/downloads/rdr2/tools/76-lennys-mod-loader-rdr/)

## Texture/Graphic Mods
* [Weapon Texture Upscale](https://www.nexusmods.com/reddeadredemption2/mods/928)
* [Gun Metal Rework](https://www.nexusmods.com/reddeadredemption2/mods/648)
* [Visual Redemption](https://discord.gg/ADfQxWSv6J)
* [Vignette Disabler](https://www.nexusmods.com/reddeadredemption2/mods/1569)
* [The Perfect TAA](https://www.nexusmods.com/reddeadredemption2/mods/1222) 
**Feature**: Attempts to fix ugly TAA blurring, (Good for 1080p, however hotsampling to 4K and up defeats its' purpose).

### Vulkan or DX12?
If you're using Windows 7 or 8.x, the only option you have is Vulkan. If you use Windows 10, you can use DX12 as well. There are reports
of higher performance under Vulkan, but also lower-res textures and less stability. The cheat table should work with both. Regardless, the 
game is highly unstable, and you have to prepare for crashes during your gameplay session.

### Weather control
The cheat table offers two ways to control the weather: one option is to set the weather type, another is to define a combination
between two weathers. 

#### Different weather types
Weathers are defined using a number. -1 (or in hexadecimal: `FFFFFFFF`) means that no weather is set and the default weather is used. 

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
10|Thunderstorm
11|Hurricane
12|Shower
13|Hail
14|Sleet
15|Snow clearing
16|Snow light
17|Snow
18|Blizzard
19|Ground blizzard
20|Whiteout
21|Sandstorm

#### How to set the weather
To set the active weather, first enable the 'Weather control' entry in the table by clicking the check box in front of it. Then double click the 
value in the 'Weather type' entry on the right. By default it'll show 'FFFFFFFF'. Double clicking it allows you to type a new weather, e.g. 4 for cloudy
weather. The weather change will be instantly, also in photomode.

#### How to set a combination of two weather types
If you want to create your own unique weather, you can create a combination of two weather types. 
After you've enabled 'Weather control' you also have to enable 'Enable weather interpolation'. After that, you double click the value in the 
'From weather' entry and type a value, e.g. 4 for cloudy weather. Then you double click the value in the 'To weather' column and also specify
a value, e.g. 14 for thick snow. 

You can then define the amount of how much of one or the other should be used using the 'Interpolation factor'. 
Double click the value of that entry to specify a value between 0 and 1, e.g. 0.3. If you e.g. specify 0.3 it means the weather is 70% the 'From weather'
weather and 30% the 'To weather'. 

To go back to the other weather option, simply disable the 'Enable weather interpolation' entry.

## Tweaks

In the file `My Documents\Rockstar Games\Red Dead Redemption 2\Settings\system.xml`:

- search for `<lodScale value="...." />` and `<pedLodBias value="...." />`, set these to 1.0, by default they're set to 0.0
- search for `<deepsurfaceQuality>...</deepsurfaceQuality>`, set the value to kSettingLevel_Ultra.

### Hotsampling
While it's possible to hotsample with Vulkan, it is very unstable and has a crash rate of about 70% and the tool used for hotsampling loses track of which window to handle (To fix you have to Refresh Window Tree and you will be able to edit the resolution again)
* DirectX 12 API hotsamples with the tool without any problems

@alert info
Hotsampling to a 32:9 aspect ratio and going back to the original one will break every trainer menu, with some losing the text, and some having the text way off the screen.
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Red_Dead_Redemption_2)
* [How to install and use Lenny's Mod Loader](https://www.youtube.com/watch?v=E-OIFFcIKDs)
