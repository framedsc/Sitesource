## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No*
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | No
Rendering API | DX9

\* resolutions can be set to hotkeys which give an advantage similar to hotsampling

INI Edits
==========================================================
First you will need the [Wench Coalesced Editor](https://www.nexusmods.com/masseffect3/mods/76) in order to add settings and keybinds that you can use in-game. The settings file (coalesced file) is located in `Origin\Mass Effect 3\BIOGame\CookedPCConsole`. Back it up first. Find the bioinput.ini and then locate the sfxgame portion of it. I will list the settings you must add first, and then explain them later.

Add the following lines to SFXGameModeCinematic:

```
( Name="MouseX", Command="PC_LookX" )
( Name="MouseY", Command="PC_LookY" ) 
( Name="A", Command="PC_StrafeLeft" ) 
( Name="W", Command="PC_MoveForward" ) 
( Name="D", Command="PC_StrafeRight" ) 
( Name="S", Command="PC_MoveBackward" ) 
( Name="F12", Command="ToggleFlyCam" ) 
( Name="F11", Command="playersonly" ) 
( Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1" ) 
( Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false" ) 
( Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true" ) 
( Name="Semicolon", Command="set HeightFogComponent bEnabled False" ) ( Name="Period", Command="set HeightFogComponent bEnabled True" ) 
( Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)" ) 
( Name="Multiply", Command="FOV 70" )
( Name="Decimal", Command="FOV 0" )
```

Next go to SFXGameModeConversation and add the following lines there:

```
( Name="MouseX", Command="PC_LookX" )
( Name="MouseY", Command="PC_LookY" ) 
( Name="A", Command="PC_StrafeLeft" ) 
( Name="W", Command="PC_MoveForward" ) 
( Name="D", Command="PC_StrafeRight" ) 
( Name="S", Command="PC_MoveBackward" ) 
( Name="F12", Command="ToggleFlyCam" ) 
( Name="F11", Command="playersonly" ) 
( Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1" ) 
( Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false" ) 
( Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true" ) 
( Name="Semicolon", Command="set HeightFogComponent bEnabled False" ) 
( Name="Period", Command="set HeightFogComponent bEnabled True" ) 
( Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)" )
( Name="Multiply", Command="FOV 70" )
( Name="Decimal", Command="FOV 0" )
```

Now go to SFXGameModeDefault and add these lines:

```
( Name="Home", Command="set SFXPawn_Player bCombatPawn true| QuickSave | QuickLoad" )
( Name="End", Command="set SFXPawn_Player bCombatPawn false | QuickSave | QuickLoad" )
( Name="LBracket", Command="ghost" ) 
( Name="RBracket", Command="walk" ) 
( Name="F12", Command="ToggleFlyCam" ) 
( Name="F3", Command="God" ) 
( Name="F11", Command="playersonly" ) 
( Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1" )
( Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false" ) 
( Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true" ) 
( Name="Semicolon", Command="set HeightFogComponent bEnabled False" ) 
( Name="Period", Command="set HeightFogComponent bEnabled True" ) 
( Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)" ) 
( Name="Multiply", Command="FOV 70" )
( Name="Decimal", Command="FOV 0" )
```

Next go to SFXGameModeFlycam and add the following lines:

```
( Name="MouseX", Command="PC_LookX" )
( Name="MouseY", Command="PC_LookY" )
( Name="A", Command="PC_StrafeLeft" )
( Name="W", Command="PC_MoveForward" )
( Name="D", Command="PC_StrafeRight" )
( Name="S", Command="PC_MoveBackward" )
( Name="F12", Command="ToggleFlyCam" )  
( Name="F11", Command="playersonly" ) 
( Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1" )
( Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false" ) 
( Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true" ) 
( Name="Semicolon", Command="set HeightFogComponent bEnabled False" ) 
( Name="Period", Command="set HeightFogComponent bEnabled True" ) 
( Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)" ) 
( Name="Multiply", Command="FOV 70" )
( Name="Decimal", Command="FOV 0" )
```

Next go to SFXDreamSequence and add the following lines:

```
( Name="LBracket", Command="ghost" ) 
( Name="RBracket", Command="walk" ) 
( Name="F12", Command="ToggleFlyCam" ) 
( Name="F11", Command="playersonly" ) 
( Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1" )
( Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false" ) 
( Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true" ) 
( Name="Semicolon", Command="set HeightFogComponent bEnabled False" ) 
( Name="Period", Command="set HeightFogComponent bEnabled True" ) 
( Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)" ) 
( Name="Multiply", Command="FOV 70" )
( Name="Decimal", Command="FOV 0" )
```

Then go to SFXGameModeBase and add the following lines:

```
( Name="Multiply", Command="FOV 70" ) 
( Name="Decimal", Command="FOV 0" ) 
( Name="F6", Command="set DOFAndBloomEffect bUseWorldSettings false" ) 
( Name="F2", Command="set DOFAndBloomEffect bUseWorldSettings true" ) 
( Name="F7", Command="SloMo 0.3 |  OnRelease SloMo 1" )
( Name="Comma", Command="set UberPostProcessEffect SceneHighlights (x=1.0,y=1.0,z=1.0) | set UberPostProcessEffect SceneShadows (x=0.0,y=0.0,z=0.0 | set UberPostProcessEffect SceneMidtones (x=1.0,y=1.0,z=1.0)" ) 
( Name="Semicolon", Command="set HeightFogComponent bEnabled False" ) 
( Name="Period", Command="set HeightFogComponent bEnabled True" )
```

And if you’re a cheater like me, add this too:

```
( Name="F1", Command="initcredits 9999999" )
```

So, what does all this mean and why do I have to copy it so many times? Keybinding in ME3 is kinda weird. Some keybinds have to be repeated, others don’t, and it is important to put the right keybinds in the right game mode. For example, if you put ghost/walk in the Cinematic or Conversation mode, you will fall through the floor and die in a cutscene. (It has happened to me!) 

This game suffers from the same shadow banding that plagues most UE3 games. Try this tweak to fix it:

In `BioEngine.ini` add/change the following under `[SystemSettings]`
```
bEnableVSMShadows=True
bEnableBranchingPCFShadows=False
bAllowHardwareShadowFiltering=True
ShadowDepthBias=0.100
```

Custom Resolutions
==========================================================
Unreal Engine 3 has a very useful command, the setres command, which will change the resolution to whatever you tell it to. This can be bound to a key, which means that we can swap resolutions in ME3 from within the game. It’s extremely convenient for taking high resolution shots.

However, the only way this works for resolutions outside our screen resolution is if we use GeDoSaTo. GeDoSaTo allows you to run resolutions outside your screen resolution, downsampled to your screen resolution. This makes up for the fact that UE3 will not allow you to run outside your screen resolution. So what happens is that every time you hit the setres command, it tells the game to go to a resolution outside your screen, which GeDoSaTo allows, and then downsamples that so you can see the whole thing on the screen. Complicated, but very useful. Some of you may use this already for Skyrim.

Setting up the setres commands is a two part process. First you will need to add them to the coalesced file. The format is: `( Name="Key", Command="setres WidthxHeight" )`, so mine look like this:

```
( Name="NumPadEight", Command="setres 3840x2160",Alt=True ) 
( Name="NumPadThree", Command="setres 4000x6000",Alt=True ) 
( Name="NumPadFour", Command="setres 7680x3840",Alt=True ) 
( Name="NumPadFive", Command="setres 5000x5000",Alt=True ) 
( Name="NumPadSix", Command="setres 8000x3404",Alt=True )
( Name="NumPadSeven", Command="setres 9000x3000",Alt=True )
```

I tried to make all these keybinds not conflict, but you might want to change them. In any case, always make sure to add your native resolution as one of the keybinds, which is Num8 for me. Add these to Base, Default, Cinematic, Conversation, DreamSequence, and FlyCam game modes.

Next, we have to mirror those in the GeDoSaTo user.ini. Add your resolutions in the following format:

```
renderResolution 3840x2160@60 
```

The @60 is your refresh rate. Leave this the way it is if you do not know.

Then change your "present resolution," which is the resolution you will downsample to, to your screen resolution:
```
presentWidth 3840 
presentHeight 2160 
presentHz 60
```

In theory, you should now be able to run ME3 fullscreen, hit one of your setres keybinds, and watch the game re-render. In reality, GeDoSaTo is a really finicky program, and you may have to change the settings to get it to work. I now have to get GeDoSaTo to force borderless fullscreen, which is one of the settings you can toggle. I advise you to try stuff that sounds halfway reasonable until you figure it out. 


Mods
==========================================================
[High Res Textures](https://www.nexusmods.com/masseffect3/mods/363)  
[Removes the vignette](https://www.nexusmods.com/masseffect3/mods/523)

