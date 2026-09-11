![Assassin's Creed: Rogue](Images\ac_rogue.png "Shot by Originalnicodr"){.shadowed .autosize}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
 
## Tools
 
* [Combined CE tables by Jim2Point0, Zanzer, SunBeam and STN](..\CheatTables\ac_rogue_merged.ct)  
**Features**: HUD toggle, freecam, fov control, time of day control, cheats
 
 
## Usage

In order to use the cheat engine table you have to first inject the table in the menu and click on the boxes `[DebugMenu]` and `pBase` inside cheat engine. After loading a level from a save click on the `pContext`, `Cheat Handler`, `[Cheats]`, `[Cheats] (0 - locked; 1 - unlocked)` boxes in cheat engine to be able to use the HUD toggle (and the cheats).

Before freezing or changing the time of day you will need to turn on the script (click on the `Time of Day` box in cheat engine).

## Controls

Description | Key
--|--
Toggle HUD | Numpad 8
Toggle free cam | Insert
Move Left and Right | 'G' and 'J'
Move Forward and Backward | 'Y' and 'H'
Move Up and Down | 'T' and 'U'
Increase and decrease the fov | '+' and '-'
Advance and go back the time of day | '[' and ']'
Freeze time of day | ';'
Camera orientation | Mouse

The hotkeys move the camera alongside the coordinates, so “left,right,forward and backwards” aren't relative to the camera orientation.

You can move the camera faster or slower by pressing 'Alt' and 'Ctrl' while moving. 

Hotkeys can be changed inside the cheat engine table, as well as the value "moved" by each hotkey.

## Increase textures quality and draw distance

Go to `User\Documents\Assassin's Creed Rogue` and open the file `AssassinRogue.ini`. Change the following settings:

```
EnvironmentQuality=4
TextureQuality=2
```
Save and set the file to Read only.

## Tips

- Since the camera orientation is controlled like in gameplay you will have some restrictions when changing its orientation.

- The FOV control is different for when you are on your ship.

- Opening the menu with the free cam enabled may crash the game.

- In some missions you can't change the time of day and the game will crash when you turn on the script. Other times if you change it and the time value reaches a certain hour (19 for example) it will also crash.
 
## Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Assassin%27s_Creed_Rogue)