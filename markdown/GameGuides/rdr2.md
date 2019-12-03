![Red Dead Redemption 2](Images\rdr2_header.jpg "Shot by Otis_Inf"){.shadowed}

##Feature summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes (with tools, dx12 only)
DSR | Yes
Custom Aspect Ratios | Yes (with tools)
Reshade | Yes (v4.4+)
Ansel | No
DirectX versions | DirectX 12
Vulkan | Yes
 
##Tools

* [Photomode enhancements by Otis_Inf](..\CheatTables\RDR2_PhotomodeEnhancements_Otis.CT)  
**Features**: Range/limit removal of photomode, removal of black bars in cutscenes and photomode, FoV control, Hotsampling support (dx12 only),
Weather control, HUD toggle, Pause/Unpause (also in photomode), Time of day (hour) support

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

##Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Red_Dead_Redemption_2)