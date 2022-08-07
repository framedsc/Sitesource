![Batman Arkham Knight](Images\batman_ak_header.png "Shot by Otis_Inf"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 11

##Tools
* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**[Features](https://opm.fransbouma.com/Cameras/batmanak.htm)**: Camera control, FoV control, HUD toggle, timestop, depth blur removal.
* [Console unlocker by Sunbeam (mr. Jag video with DLL)](https://www.youtube.com/watch?v=NcvzZl5vXng)  
**Features**: Allows you to open the dev console using a command

@alert Important
The console unlocker dll available at the video above is outdated and contains an issue with smoke effects. If you have Nvidia enhanced smoke enabled in the gfx 
settings of the game, it might be the game crashes when these are on screen. A newer fixed dll is available on 
[Sunbeam's patreon](https://www.patreon.com/sunbeam906) which fixes this.
@end

## Resolutions
Using DSR fullscreen works ok. If you use an aspect ratio (AR) other than what the game natively support for your monitor (21:9 or 16:9), 
you might run into issues, e.g. there's a strange line down the left side in `3:4` AR.

#### Changing resolution while game is paused

Pause the game with `playersonly` (this is `F5` if you use the bindings below, see next section) then go into the graphics menu and change your resolution. 
Exit main menu and game should still be paused. Enable camera, take shot, disable camera then disable `playersonly`. Camera Tool 
pause and playersonly with stack so if you enable both, remember to disable both.

## Enabling console key and adding keybinds
This is what you need for adding a specific file for keybinds instead of editing any of the core game files. 

1. Create folder `<game installation folder>\DLC\356474\Content\BmGame\ScreenshootingBinds`
2. Create a textfile called `BmEngine.ini`, open it in notepad and copy the contents of the file listed below in notepad and save the file
3. Create a textfile called `BmInput.ini`, open it in notepad and copy the contents of the file listed below in notepad and save the file
4. If you made changes to the file `<game installation folder>\BmGame\Config\BmInput.ini`, remove them, as changes could conflict with the `BmInput.ini` file
we're creating
5. Start game and you should be able to access console (if using Sunbeam's d3d9.dll) with the [~] key and have access to the binds. Review the file for keys.
6. `F1` for some postprocessing, `F3/F4` for slomo, `F5` for playersonly. Other binds not confirmed.
7. when in debugcamera, using `toggledebugcamera` press `F2` to add a spotlight and `F3` to add a point light.

### BmEngine.ini
The following contents should be in the BmEngine.ini file created at step 2:

```ini
[Engine.Engine]
bPauseOnLossOfFocus=FALSE
```

This doesn't pause the game when you alt-tab

### BmInput.ini
The following contents should be in the BmInput.ini file created at step 3:

```ini
[Engine.Console]
ConsoleKey=Tilde
TypeKey=Backslash

[Engine.DebugCameraInput]
.Bindings=(Name="F2",Command="spawnscreenshotspotlight")
.Bindings=(Name="F3",Command="spawnscreenshotpointlight")

[Engine.PlayerInput]
.Bindings=(Name="F1",Command="set DOFAndBloomEffect bUseWorldSettings false",Alt=False)
.Bindings=(Name="F1",Command="set DOFAndBloomEffect bUseWorldSettings true",Alt=True)
.Bindings=(Name="F2",Command="exec console.txt")
.Bindings=(Name="F2",Command="exec console2.txt",Alt=True)
.Bindings=(Name="F3",Command="slomo 0.3")
.Bindings=(Name="F3",Command="slomo 0.001",Alt=True)
.Bindings=(Name="F4",Command="slomo 1")
.Bindings=(Name="F5",Command="set Engine.WorldInfo bPlayersOnly true")
.Bindings=(Name="F5",Command="set Engine.WorldInfo bPlayersOnly false",Alt=True)
.Bindings=(Name="F6", Command="set BmGame.RPersistentDebugData Debug_Combat_DisableStrikeTrails true | set BmGame.RPersistentDebugData Debug_Combat_DisableStunStars true | set BmGame.RPersistentDebugData Debug_Combat_DisableImpactVFX 1 | set BmGame.RVehicleBatmobileBase SatNavChallengeActive 0")
.Bindings=(Name="F6", Command="set BmGame.RPersistentDebugData Debug_Combat_DisableStrikeTrails false | set BmGame.RPersistentDebugData Debug_Combat_DisableStunStars false | set BmGame.RPersistentDebugData Debug_Combat_DisableImpactVFX 0 | set BmGame.RVehicleBatmobileBase SatNavChallengeActive 1",Alt=True)
.Bindings=(Name="F7", Command="set BmGame.RVehicleBatmobileBase CheatBatmobilePower 1")
.Bindings=(Name="F7", Command="set BmGame.RVehicleBatmobileBase CheatBatmobilePower 0",Alt=True)
.Bindings=(Name="F8", Command="set Engine.LocalPlayer IsMapViewEnabled true")
.Bindings=(Name="F8", Command="set Engine.LocalPlayer IsMapViewEnabled false",Alt=True)
.Bindings=(Name="F9", Command="set BmGame.MPawnPlayerHarleyQuinnBase bDebugHarleyMayhemMode 1")
.Bindings=(Name="F9", Command="set BmGame.MPawnPlayerHarleyQuinnBase bDebugHarleyMayhemMode 0",Alt=True)
.Bindings=(Name="F10", Command="set Engine.Material Wireframe true")
.Bindings=(Name="F10", Command="set Engine.Material Wireframe false",Alt=True)
.Bindings=(Name="F11", Command="set BmGame.RPersistentDebugData Debug_Combat_CanAlwaysTakedown 1")
.Bindings=(Name="F11", Command="set BmGame.RPersistentDebugData Debug_Combat_CanAlwaysTakedown 0",Alt=True)
.Bindings=(Name="F12", Command="set BmGame.RPawnVillain bShouldPreventFinalBlowCam 0")
.Bindings=(Name="F12", Command="set BmGame.RPawnVillain bShouldPreventFinalBlowCam 1",Alt=True)
```

##Running console commands from script with a keybind

If you want to use the exec console command to execute other console commands you will need to create text files under 
`<game installation folder>\Binaries` and add the commands you want to execute in those text files. 

Then add a keybind to `BMinput.ini` and press the keybind to execute in-game after you've started the game. 
This allows you to set aside a keybind for whatever console command you want without having to restart the game as you can change the text files
at runtime.

Example:
```ini
Bindings=(Name="F2",Command="exec console.txt")
Bindings=(Name="F2",Command="exec console2.txt",Alt=True)
```
These two lines are added to the BmInput.ini file and define `F2` and `Alt-F2` to exec the commands in `console.txt` and `console2.txt` respectively.

Sunbeam's Console unlocker is require to make all keybinds in the BMInput.ini `[Engine.PlayerInput]` section to actually work. Depending on what they 
are bound to and if that function works you may see strange behaviour.

The following commands are available:

Key / command | Description
--|--
`BACKSPACE` | debugcamera (Hides HUD and pauses game when enabled. Works in parrallel to Otis Camera Tool, both can be enabled at the same time.)
`B` |  spawn batmobile (it is floating but once you get in and drive it will be on the road...or blimp...where ever you happen to be.
`T` |  Teleport
`Y` |  ToggleGhost
`ENTER` |  When in debug camera this may step forward a couple frames
`RiddlerRevealItemsOnlyValid` | 
`God` | 
`Ghost` | 
`Walk` | 
`TriggerFearTakedown 99` |  enables isntant access to fear takedowns
`DebugGiveAllGadgets` | 
`UnlockAllUpgrades TRUE` | 
`spawnscreenshotspotlight` | go into debug camera then spawn light
`spawnscreenshotpointlight` |  go into debug camera then spawn light 
`spawnplayercar` | 
`ToggleEnemiesCanAttack` |  works, they run away.
`toggledebugcamera` | toggles the debug camera on/off. Same as pressing `BACKSPACE`
`DebugCamSingleFrameStep` | 
`set engine.RRainComponent ParticleCount 999999` |  Heavy Rain, value of 200000 is ALOT of rain. Rain bloom is exponentially amplified when time is stopped. (Must be entered in console and level restart level)
`set Engine.LocalPlayer IsThermalEnabled true` | Thermal vision enabled.
`set RPlayerController CapeGlideMinSpeed 99` |  allows camera to move around bats more while flying...and glide for longer?
`SuspendAI` | stops enemys from attacking. Can't turn off.
`SpecialMoveCheat` | enables instant access to special moves. Not sure what those moves are though, looked like just takedown?

More possible command functions, see: <https://fearlessrevolution.com/viewtopic.php?f=4&t=946>

##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Batman:_Arkham_Knight)
* [Mods on Nexus](https://www.nexusmods.com/batmanarkhamknight)