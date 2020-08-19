![DmC: Devil May Cry](Images\dmc.png "Shot by White Harpy")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (read hotsampling section)
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | No
DirectX versions | DirectX 9
 
## Tools

* [CE table by IDK31](..\CheatTables\DMC_freecam0.02.CT)  
**Features**: Free Camera, FOV, Time control, HUD toggle, DOF control, Bloom, Color and more

## Controls
- Enable/Disable freecam: Pagedown
- Move camera position:
    - Num 4: Left
    - Num 6: Right
    - Num 8: Forwards
    - Num 5: Backwards
    - Num 9: Upwards
    - Num 7: Downards
- Move camera orientation:
    - '+' + Num 4: Left
    - '+' + Num 6: Right
    - '+' + Num 8: Up
    - '+' + Num 2: Down
- FOV control:
    - '+' + Num 9: Increase
    - '+' + Num 7: Decrease
- Camera tilt:
    - '+' + Num 1: Tilt the camera left
    - '+' + Num 3: Tilt the camera right
    - '+' + Num 2: Reset camera tilt
- Speed modifiers (maintain one of the followings pressed while you move the camera position or direction to do it faster or slower):
    - C: Slow
    - F: Fast
    - T: Very Fast

The rest of the table doesn't have hotkeys, so you can either add or use the edits stayed in the section below.

Editing the config file
=========================================================

Locate the DmC config files in `\Documents\My Games\UnrealEngine3\DevilGame\Config\`.

Open `Devilinput.ini` and add custom binds under `[Engine.PlayerInput]`.

```
Bindings=(Name="F8",Command="ToggleNTHUD")
Bindings=(Name="F9",Command="Pause")
Bindings=(Name="F12",Command="playersonly")
```

More commands that will come handy:

```
Bindings=(Name="F1",Command="setres 2560x1440",Control=False)
Bindings=(Name="F1",Command="setres 7680x4320",Control=True)
Bindings=(Name="F2",Command="setres 2560x1280",Control=False)
Bindings=(Name="F2",Command="setres 8000x4000",Control=True)
Bindings=(Name="F3",Command="setres 2560x1080",Control=False)
Bindings=(Name="F3",Command="setres 8640x3645",Control=True)
Bindings=(Name="F4",Command="setres 1080x1440",Control=False)
Bindings=(Name="F4",Command="setres 4800x6400",Control=True)
Bindings=(Name="F5",Command="setres 1400x1400",Control=False)
Bindings=(Name="F5",Command="setres 5500x5500",Control=True)

Bindings=(Name="F6",Command="Slomo 0.3", Alt=False)
Bindings=(Name="F6",Command="Slomo 1.0", Alt=True)
Bindings=(Name="F7",Command="Peace", Alt=False)
Bindings=(Name="F7",Command="War", Alt=True)
Bindings=(Name="F10",Command="NTKillAll")
Bindings=(Name="NumPadOne",Command="FOV 10",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadTwo",Command="FOV 20",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadThree",Command="FOV 30",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadFour",Command="FOV 40",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadFive",Command="FOV 50",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadSix",Command="FOV 60",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadSeven",Command="FOV 80",Control=True,Shift=False,Alt=False)
Bindings=(Name="NumPadEight",Command="FOV 90",Control=True,Shift=False,Alt=False)

Bindings=(Name="Four",Command="set DOFEffect bUseWorldSettings false",Alt=False)
Bindings=(Name="Four",Command="set DOFEffect bUseWorldSettings true",Alt=True)
```

In the code above the keys are setted to do the following:

- F1 = native 16:9
- Alt + F1 = dowsampled 16:9 ... same for F3, F4, F5
- F6 = Slow motion
- F7 = Enemies Ignore you
- F8 = Toggle Hud
- F9 = Pauses the game (required for camera - alt-tabbing unpauses)
- F10 = Kills all currently spawned enemies
- F12 = PlayersOnly (pauses the game - stays frozen while alt-tabbing)
- Control + Numpad 1-8 = Force FOV

The setres commands to change resolution need to be used with GeDoSato, more of that explained in the Hotsampling section.

The last two lines are required if you use the [alternative CE table made by one3rd](..\CheatTables\DMC-DevilMayCry-Merged-DOF--Tonemap-v0.2.CT) altough is recommended to use a DOF shader with reshade for shooting.

Keep in mind that you can use the combination of keys that fits you best.

In addition you can also change the default anisotropic filtering (4) up to 16 & Default smoothing (HD AA) in the config file `devilengine.ini` or use the antialising from the nvidia panel.

Hotsampling
=========================================================

For Hotsampling with the bindings above you will have to use them alongside GeDoSaTo.

You need to have matching resolutions in your GeDoSaTo config file (and have the program open while running the game); For example:

```
#16:9
renderResolution 7680x4320@60

#3:4
renderResolution 1080x1440@60
renderResolution 4800x6400@60

#2:1
renderResolution 2560x1280@60
renderResolution 8000x4000@60

#21:9
renderResolution 2560x1080@60
renderResolution 8640x3645@60
```

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/DmC:_Devil_May_Cry)