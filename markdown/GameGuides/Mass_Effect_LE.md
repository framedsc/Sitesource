![Mass Effect Legendary Edition](Images\mass_effect_le.png "Shot by Sonozaki"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (DX11)
Ansel | No
Graphics API | DirectX 11
Game version | 
 
## Tools

* [Photo Mode Range Unlocker by Otis_Inf](https://github.com/FransBouma/InjectableGenericCameraSystem/blob/master/MiscCheatTables/MassEffectLE.CT)  
**Features**: Free Camera Control within the Photomode
* [ME3 Tweaks Mod Manager](https://www.nexusmods.com/masseffectlegendaryedition/mods/2?tab=files&file_id=4619)  
**Features**: Unlocks the Command-Console, allows to unpack/pack coalesced files, HUD-Toggle via Console  
* [Wench Coalesced Editor](https://www.nexusmods.com/masseffect3/mods/76)  
**Features**: Allowing you to edit ME's Coalesced File without unpacking it to access the BIOInput.ini

We will be using the photomode for gameplay shots and the FlyCam/DebugCam for cutscene shots.

## Controls 
You can set keybinds in the Cheat Table for the no boundaries functionality.

## Access to the ingame console and Editing .ini + Coalesced Files
If you want to use additional keybinds, you need to unpack - edit - repack the Coalesced Files for Mass Effect 2 and Mass Effect 3. The following information is taken from a older source which isn't available anymore.

## Enabling the Console
To gain access to the console within the game, download the ME3 Tweaks Mod Manager. Starting the game through the mod manager should enable the in-game console in all three games.

To change the keybind, go to the `Tools` section in the Mod Manager and choose 
`Console Key Keybinder`. Set the bind to your likeing. 

Additional Information can be found here: 
- [List of console commands](http://www.nightsolo.net/games/mele/cheats.html) (Nightsolo)
- [ME3Tweaks Mod Manager](https://www.nexusmods.com/masseffectlegendaryedition/mods/2?tab=description) (Nexus Mods)
- [ME3Tweaks Mod Manager Source](https://github.com/ME3Tweaks/ME3TweaksModManager) (Github)

## Custom Resolutions
Through the console, it is possible to change the game resolution on the fly with the `setres` command. 

Typing in `setres 2560x1440` will set the game to the desired resolution. 

These commands can also be added to the BioInput to change between resolutions even quicker.

Example:

```
Bindings=(Name="U",Command="setres 5120x2880",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
```

By using the `Ctrl` / `Alt` / `Shift` modifiers, you can set multiple resolutions to one key: 

```
Bindings=(Name="U",Command="setres 1920x1080",Control=False,Shift=False,Alt=True,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
```

It is important that the resolutions that you want to use are either supported by your default and/or custom DSR settings. It's also possible to use the outdated downsample & post-processing tool GeDoSato for the same matter.

Either way, the resolution you bind via key or type into the console need to be mirrored in your DSR settings or GeDoSaTo config.

## Hud Removal
1. To remove the hud you can either disable it completely within the Photomode. 
2. If you use the command `toggledebugcamera` to enter the freecam during cutscenes, etc. type the following command into the console: `TOGGLEUI`
3. During gameplay you can disable the HUD by typing in `show scaleform`. You may choose to bind it to specific key as well. 


## Mass Effect 1
To get the FlyCam working you need need the `ME3TweaksManager`and perform the following steps:  

1. Locate the `Coalesced_INT.bin` file under `ME1/BioGame/CookedPCConsole` and create backup. Copy it over somewhere else to work with a seperate copy.
2. Drag the `Coalesced_INT.bin` into the `ME3TweaksManager`and head to the location of the `Coalesced_INT.bin`
3. Open up the folder `Coalesced_INT` and locate the `BIOInput.ini
4. Perform the following edits:
 Above the line `[SFXGame.SFXGameModeDefault]` add the following lines
 ```
 [SFXGame.SFXGameModeFlycam]
Bindings=(Name="Add",Command="PlayersOnly | ToggleFlycam | Show Scaleform" )
Bindings=(Name="MoveUp",Command="Axis aUp Speed=0.2")
Bindings=(Name="MoveDown",Command="Axis aUp Speed=-0.2")
Bindings=(Name="MoveForward",Command="Axis aBaseY Speed=0.2")
Bindings=(Name="MoveBackward",Command="Axis aBaseY Speed=-0.2")
Bindings=(Name="StrafeLeft",Command="Axis aStrafe Speed=-1.0")
Bindings=(Name="StrafeRight",Command="Axis aStrafe Speed=+1.0")
Bindings=(Name="Q",Command="MoveDown")
Bindings=(Name="E",Command="MoveUp")
Bindings=(Name="W",Command="MoveForward")
Bindings=(Name="S",Command="MoveBackward")
Bindings=(Name="S",Command="MoveBackward")
Bindings=(Name="A",Command="StrafeLeft")
Bindings=(Name="D",Command="StrafeRight")
Bindings=(Name="MouseX",Command="Count bXAxis | Axis aMouseX")
Bindings=(Name="MouseY",Command="Count bYAxis | Axis aMouseY")
```
Inside `[SFXGame.SFXGameModeDefault]` place the lines
```
Bindings=(Name="Add",Command="PlayersOnly | ToggleFlycam | Show Scaleform" )
Bindings=(Name="MoveUp",Command="Axis aUp Speed=0.2")
Bindings=(Name="MoveDown",Command="Axis aUp Speed=-0.2")
Bindings=(Name="MoveForward",Command="Axis aBaseY Speed=0.2")
Bindings=(Name="MoveBackward",Command="Axis aBaseY Speed=-0.2")
Bindings=(Name="StrafeLeft",Command="Axis aStrafe Speed=-1.0")
Bindings=(Name="StrafeRight",Command="Axis aStrafe Speed=+1.0")
Bindings=(Name="Q",Command="MoveDown")
Bindings=(Name="E",Command="MoveUp")
Bindings=(Name="W",Command="MoveForward")
Bindings=(Name="S",Command="MoveBackward")
Bindings=(Name="S",Command="MoveBackward")
Bindings=(Name="A",Command="StrafeLeft")
Bindings=(Name="D",Command="StrafeRight")
Bindings=(Name="MouseX",Command="Count bXAxis | Axis aMouseX")
Bindings=(Name="MouseY",Command="Count bYAxis | Axis aMouseY")
```
Inside `[SFXGame.SFXGameModeVehicle]` place the lines
```
Bindings=(Name="Add",Command="PlayersOnly | ToggleFlycam | Show Scaleform" )
```
Within the section `[SFXGame.SFXGameModeConversation]` add
```
Bindings=(Name="Add",Command="PlayersOnly | ToggleFlycam | Show Scaleform" )
Bindings=(Name="MoveUp",Command="Axis aUp Speed=0.2")
Bindings=(Name="MoveDown",Command="Axis aUp Speed=-0.2")
Bindings=(Name="MoveForward",Command="Axis aBaseY Speed=0.2")
Bindings=(Name="MoveBackward",Command="Axis aBaseY Speed=-0.2")
Bindings=(Name="StrafeLeft",Command="Axis aStrafe Speed=-1.0")
Bindings=(Name="StrafeRight",Command="Axis aStrafe Speed=+1.0")
Bindings=(Name="Q",Command="MoveDown")
Bindings=(Name="E",Command="MoveUp")
Bindings=(Name="W",Command="MoveForward")
Bindings=(Name="S",Command="MoveBackward")
Bindings=(Name="S",Command="MoveBackward")
Bindings=(Name="A",Command="StrafeLeft")
Bindings=(Name="D",Command="StrafeRight")
Bindings=(Name="MouseX",Command="Count bXAxis | Axis aMouseX")
Bindings=(Name="MouseY",Command="Count bYAxis | Axis aMouseY")
```
5. Save the file `BIOInput.ini` and drag the file `mele.extractedbin` within the `Coalesced_INT` folder back into the `ME3TweaksManager`
6. Place the newly created `Coalesced_INT.bin` under `ME1/BioGame/CookedPCConsole`. If asked replace the existing file.

The FlyCam should work now. Method by munchyfly found here: [https://hackmd.io/@munchyfly/ByiK4X5dc]

## Mass Effect 2
This is where things will get a bit more tricky, but thanks to the updated Mod Manager, the process has become a lot easier. 

To unpack the Mass Effect 2 Coalesced, go to the folder `Mass Effect 2\BIOGame\CookedPCConsole` in your installation location of ME 2. 

Search for `Coalesced_Language.bin` or simply choose `Coalesced_INT.bin` - **Do a back-up!**

Drag the file into the ME3TweaksModManager, in the left bottom are of the program window you'll get the following message: "Decompiled Coalesced file"

If you head into the location of your choosen Coalesced File, there will be a folder called the same name. Within that folder search for `BIOInput.ini`. Within that ini you need to perform multiple edits.

```
[SFXGameModeBase]
(Name="F12",Command="Show Scaleform")
(Name="F11",Command="PlayersOnly")
(Name="F10",Command="ToggleFlyCam")
(Name="Insert",Command="InitCredits 500000 | InitPalladium 500000 | InitIridium 500000 | InitEezo 500000 | InitPlatinum 500000")
(Name="O",Command="set materialeffect bshowingame false")
(Name="U",Command="set materialeffect bshowingame true")
(Name="i",Command="FOV 70")
(Name="l",Command="FOV 0")

[SFXGameModeCinematic]
(Name="MoveUp",Command="Axis aUp Speed=0.2")
(Name="MoveDown",Command="Axis aUp Speed=0.2")
(Name="MoveForward",Command="Axis aBaseY Speed=0.2")
(Name="MoveBackward",Command="Axis aBaseY Speed=-0.2")
(Name="TurnLeft",Command="Axis aBaseX Speed=-30.0 AbsoluteAxis=100")
(Name="TurnRight",Command="Axis aBaseX Speed=+30.0 AbsoluteAxis=100")
(Name="StrafeLeft",Command="Axis aStrafe Speed=-1.0")
(Name="StrafeRight",Command="Axis aStrafe Speed=+1.0")
(Name="Q",Command="MoveDown")
(Name="E",Command="MoveUp")
(Name="W",Command="MoveForward")
(Name="S",Command="MoveBackward")
(Name="S",Command="MoveBackward")
(Name="A",Command="StrafeLeft")
(Name="D",Command="StrafeRight")
(Name="MouseX",Command="Count bXAxis | Axis aMouseX")
(Name="MouseY",Command="Count bYAxis | Axis aMouseY")
(Name="Left",Command="TurnLeft")
(Name="Right",Command="TurnRight")
(Name="LeftShift",Command="MoreSpeed | OnRelease NormalSpeed",Control=False,Shift=False,Alt=False)
(Name="Multiply", Command="SloMo 1")
(Name="Subtract", Command="SloMo 0.5")
(Name="Add", Command="SloMo 0.01")

[SFXGameModeConversation]
(Name="MoveUp",Command="Axis aUp Speed=0.2")
(Name="MoveDown",Command="Axis aUp Speed=0.2")
(Name="MoveForward",Command="Axis aBaseY Speed=0.2")
(Name="MoveBackward",Command="Axis aBaseY Speed=-0.2")
(Name="TurnLeft",Command="Axis aBaseX Speed=-30.0 AbsoluteAxis=100")
(Name="TurnRight",Command="Axis aBaseX Speed=+30.0 AbsoluteAxis=100")
(Name="StrafeLeft",Command="Axis aStrafe Speed=-1.0")
(Name="StrafeRight",Command="Axis aStrafe Speed=+1.0")
(Name="Q",Command="MoveDown")
(Name="E",Command="MoveUp")
(Name="W",Command="MoveForward")
(Name="S",Command="MoveBackward")
(Name="A",Command="StrafeLeft")
(Name="D",Command="StrafeRight")
(Name="MouseX",Command="Count bXAxis | Axis aMouseX")
(Name="MouseY",Command="Count bYAxis | Axis aMouseY")
(Name="Left",Command="TurnLeft")
(Name="Right",Command="TurnRight")
(Name="LeftShift",Command="MoreSpeed | OnRelease NormalSpeed",Control=False,Shift=False,Alt=False)
(Name="Multiply", Command="SloMo 1")
(Name="Subtract", Command="SloMo 0.5")
(Name="Add", Command="SloMo 0.01")

[SFXGameModeDefault]
(Name="F3",Command="God")
(Name="F8",Command="Ghost")
(Name="F4",Command="Walk")
```


When you finished adding the commands, save the file and close it. Now, search within the previously mentioned folder (where you grabbed the .ini from) and locate the following file: `mele.extractedbin`. Drag that file into the ME3TweaksModManager and in the bottom left, the following message should appear [Compiled Coalesced File]. Within the folder you should find the new Coalesced. Drag this one into the `Mass Effect 2\BIOGame\CookedPCConsole`.

## Mass Effect 3

For Mass Effect 3, the process is a bit more straightforward, however it's up to you if you want to perform the edits by hand in Notepad etc. according to the previously mentioned process for ME2 or if you want to use the Wenched Coalesced Editor which allows you to directly edit the file without unpacking it first.

Either way, the initial steps are the same.

1. Navigate to `Mass Effect 3\BIOGame\CookedPCConsole`
2. Locate the `Coalesced.bin` file

Perform the unpacking steps mentioned above, or open up the file with the Coalesced Editor.
If you choose the Editor: start it and then load the file `Bioinput.ini` and within that file go to the `SFXGAME` tab.

Add the following commands under each named section:

```
[SFXGameModeCinematic]
(Name="MouseX", Command="PC_LookX")
(Name="MouseY", Command="PC_LookY") 
(Name="A", Command="PC_StrafeLeft") 
(Name="W", Command="PC_MoveForward") 
(Name="D", Command="PC_StrafeRight") 
(Name="S", Command="PC_MoveBackward") 
(Name="F12", Command="ToggleFlyCam") 
(Name="F11", Command="playersonly") 
(Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1") 
(Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false") 
(Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true") 
(Name="Semicolon", Command="set HeightFogComponent bEnabled False") ( Name="Period", Command="set HeightFogComponent bEnabled True") 
(Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)") 
(Name="Multiply", Command="FOV 70")
( Name="Decimal", Command="FOV 0")

[SFXGameModeConversation]
(Name="MouseX", Command="PC_LookX")
(Name="MouseY", Command="PC_LookY") 
(Name="A", Command="PC_StrafeLeft") 
(Name="W", Command="PC_MoveForward") 
(Name="D", Command="PC_StrafeRight") 
(Name="S", Command="PC_MoveBackward") 
(Name="F12", Command="ToggleFlyCam") 
(Name="F11", Command="playersonly") 
(Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1") 
(Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false") 
(Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true") 
(Name="Semicolon", Command="set HeightFogComponent bEnabled False") 
(Name="Period", Command="set HeightFogComponent bEnabled True") 
(Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)")
(Name="Multiply", Command="FOV 70")
(Name="Decimal", Command="FOV 0")

[SFXGameModeDefault]
(Name="Home", Command="set SFXPawn_Player bCombatPawn true| QuickSave | QuickLoad")
(Name="End", Command="set SFXPawn_Player bCombatPawn false | QuickSave | QuickLoad")
(Name="LBracket", Command="ghost") 
(Name="RBracket", Command="walk") 
(Name="F12", Command="ToggleFlyCam"  
(Name="F3", Command="God") 
(Name="F11", Command="playersonly") 
(Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1")
(Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false") 
(Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true") 
(Name="Semicolon", Command="set HeightFogComponent bEnabled False") 
(Name="Period", Command="set HeightFogComponent bEnabled True") 
(Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)") 
(Name="Multiply", Command="FOV 70")
(Name="Decimal", Command="FOV 0")

[SFXGameModeFlycam]
(Name="MouseX", Command="PC_LookX")
(Name="MouseY", Command="PC_LookY")
(Name="A", Command="PC_StrafeLeft")
(Name="W", Command="PC_MoveForward")
(Name="D", Command="PC_StrafeRight")
(Name="S", Command="PC_MoveBackward")
(Name="F12", Command="ToggleFlyCam")  
(Name="F11", Command="playersonly") 
(Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1")
(Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false") 
(Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true") 
(Name="Semicolon", Command="set HeightFogComponent bEnabled False") 
(Name="Period", Command="set HeightFogComponent bEnabled True") 
(Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)") 
(Name="Multiply", Command="FOV 70")
(Name="Decimal", Command="FOV 0")

[SFXDreamSequence]
(Name="LBracket", Command="ghost") 
(Name="RBracket", Command="walk") 
(Name="F12", Command="ToggleFlyCam") 
(Name="F11", Command="playersonly") 
(Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1")
(Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false") 
(Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true") 
(Name="Semicolon", Command="set HeightFogComponent bEnabled False") 
(Name="Period", Command="set HeightFogComponent bEnabled True") 
(Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)") 
(Name="Multiply", Command="FOV 70")
(Name="Decimal", Command="FOV 0")

[SFXGameModeBase]
(Name="Multiply", Command="FOV 70") 
(Name="Decimal", Command="FOV 0") 
(Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false") 
(Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true") 
(Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1")
(Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)") 
(Name="Semicolon", Command="set HeightFogComponent bEnabled False") 
(Name="Period", Command="set HeightFogComponent bEnabled True")
(Name="F1", Command="initcredits 9999999")
```

## Fix Shadow Banding in the Trilogy
In `BioEngine.ini` locate `SystemSettings` and add or change the following lines:
```
bEnableVSMShadows=True
bEnableBranchingPCFShadows=False
bAllowHardwareShadowFiltering=True
ShadowDepthBias=0.100
```

## Tips and Tricks
Obviously, you can change the keys for the above mentioned keys to your liking, but keep in mind that they need to look the same under every section.
It's also possible to use the majority - if not all - of the binds via the console. 

### Additional-Commands
Command | Description
--|--
`Viewmode 1` | Use Default Game Scene and Rendering
`Viewmode LITLIGHTMAPDENSITY` | Turn off Weather Effects on Planets
`Viewmode TEXTUREDENSITY` | Turn off Surface Rendering / Disables AO/Bloom etc
`teleport` |
`ghost`|
`TOGGLEUI` | Hides the DebugCamera overlay

You can find more commands in the [UE3 Console Commands List](https://docs.unrealengine.com/udk/Three/ConsoleCommands.html).

### Combination of Console Commands

For even more freedom, you can combine the command ghost with teleport. By using that "trick", you can access areas locked behind cutscenes.
*Shoutout to my man ItsYFP for digging this one up.*

## Alternative to Cheat Table useage: Photomode Enhancement Mods
Check the mods on Nexus for further installing instructions.
* [Photomode Enhancement MOD for LE1](https://www.nexusmods.com/masseffectlegendaryedition/mods/421?tab=description)
* [Photomode Enhancement MOD for LE2](https://www.nexusmods.com/masseffectlegendaryedition/mods/332?tab=description)
* [Photomode Enhancement MOD for LE3](https://www.nexusmods.com/masseffectlegendaryedition/mods/424?tab=description)

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Mass_Effect_Legendary_Edition)
* [ALOT-Textures](https://www.nexusmods.com/masseffectlegendaryedition/mods/363?tab=description) (Nexus Mods)
* [ALOT-Videos](https://www.nexusmods.com/masseffectlegendaryedition/mods/3)
* [Trilogy-Save-Editor](https://www.nexusmods.com/masseffectlegendaryedition/mods/20)
* [One-Probe-Mod](https://www.nexusmods.com/masseffectlegendaryedition/mods/149)
* [Community-Patch](https://www.nexusmods.com/masseffectlegendaryedition/mods/13)
* [ME2-No-Weapon-Restrictions](https://www.nexusmods.com/masseffectlegendaryedition/mods/41)
* [Cool-Armor](https://www.nexusmods.com/masseffectlegendaryedition/mods/1371)

