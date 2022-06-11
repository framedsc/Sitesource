![Bayonetta](Images\bayonettaheader.jpg "Shot by One3rd"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes, see notes
Reshade | Yes
Ansel | No
Graphics API | DirectX 9
Game version | Steam

## Tools

* [Cheat Engine Table](..\CheatTables\Bayonetta_v2.CT)  
**Features**: Camera control, FOV control, Timeflow control, Vignette removal, Cheats  
* [Hud Removal Tool](https://mega.nz/file/qZI01b4b#Xs0WwnrIND4yah9Y2niF1Ux02KoRPyB3nVmeDEbfmqU)
**Features**: Pause menu HUD toggle using Reshade add-on ShaderToggler

## Controls 
[comment]: # (include this section if your guide references a cheat table / non-standard tools [Otis_Inf tools are all standardised], otherwise remove it)

Key	| Command
--|--
`Delete` | Toggle time control
`F1` | Toggle Photo Mode FOV control
`Num +` / `Num -` | Increase / decreas FOV
`F2` | Unlock aspect ratio
`F3` | Infinite Fuel / scraps
`F4` | Infinite health for Max 
`F5` | Timeflow = 0 (stop time)
`CTRL`+`F5` | Timeflow = 0.001 
`F6` | Timeflow = 0.01 
`CTRL`+`F6` | Timeflow = 0.1 
`F7` | Timeflow = 0.3
`CTRL`+`F7` | Timeflow = 1 (resume time)
`F8` | Toggle ingame HUD (this is the games default hud toggle)
`F9` | Enemy Timeflow = 0
`CTRL`+`F9` | Enemy Timeflow = 1
`F10` | Bayonetta Timeflow = 0
`CTRL`+`F10` | Bayonetta Timeflow = 1
`Caps Lock` | Toggle all HUD (Reshade add-on ShaderToggler)
`Num Decimal` | Toggle various screen effects (Reshade add-on ShaderToggler)
`PAGE DOWN` | Toggle free camera (controlled with numpad keys, see CAMERA > HOTKEYS section in table for specifics)
`PAGE UP` | Disable additional camera writes to help stabalize during some scenes/levels where the camera shakes
`Number row 0` | Disable vignette

@alert info
The in-game camera is this games most difficult boss...and this free camera is no exception to that jankiness. Expect stange camera behaviour in certain levels and no proper camera control during cutscenes or any time the camera control is taken away from the player.
@end

## Tips and Tricks

### Resolution

Hotsampling does not work but the resolution can be changed in the in-game settings to any DSR resolution while the game is paused.

### Aspect Ratio

The game supports different aspect ratios. Go to .\Bayonetta\aspect unlock folder and add the registry entry by double clicking `DisableAspectLock.reg` or right-click selecting merge. 

### VSync

The in-game VSync is horrendous. Disable that and enable it in your graphic cards control panel. In NVidia Control Panel set the game specific VSync setting to `FAST`.

### Reshade and MSAA

Reshade depth buffer works well in this game even with in-game MSAA enabled. 

Use below depth buffer values in Reshade 5.x 

* RESHADE_DEPTH_LINEARIZATION_FAR_PLANE=1000
* RESHADE_DEPTH_INPUT_IS_UPSIDE_DOWN=0
* RESHADE_DEPTH_INPUT_IS_REVERSED=0
* RESHADE_DEPTH_INPUT_IS_LOGARITHMIC=0

### Pause Menu Camera

When in the pause menu the camera position can be moved around the scene. This does not allow for camera rotation or FOV and can be visually buggy but it works any time an in-engine cutscene is playing. No need to enable anything just use the below keys.

Key	| Command
--|--
`I` | Up
`K` | Down
`J` | Left
`L` | Right

@alert info
Use `CTRL` and `SHIFT` keys as modifiers for movement speed. 
@end

### Bayonetta's Hair Costume

There are two scripts that disable the Wicked Weave model change.

Key	| Command
--|--
`N` | Model is always clothed
`M` | Model is clothed in hair costume

### Cheats

* Press `F11` to enable/disable infinite health
* There are two address values for the current magic and money values, these can be set manually.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Bayonetta)
* Credit: cheats by fantomas and Zachillios 
* Credit: lookat camera control script and LUA lifted from IDK31 & Smithfield's Nier Automata table