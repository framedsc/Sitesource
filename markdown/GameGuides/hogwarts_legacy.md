![Hogwarts Legacy](Images\hogwarts_legacy.png "Shot by Dread"){.shadowed .autosize}
## Summary
Feature | Supported
--|--
Vanilla Photo Mode | No
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

### Change seasons without UUU

Download and install this mod (requires another mod to be installed first).
[https://www.nexusmods.com/hogwartslegacy/mods/57?tab=description](https://www.nexusmods.com/hogwartslegacy/mods/57?tab=description) 

Installing is easy, just drag some files to a folder for both mods. Follow the instructions to enable the mod in-game. After entering "UETools" into the mod window in-game, you never have to do that again. 

Now you can use the normal console to use the weather commands.

```
HL_ChangeSeason spring
HL_ChangeSeason fall
HL_ChangeSeason winter
```

After entering the command, you'll need to fast travel for the textures to switch to the selected season.