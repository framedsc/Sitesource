@alert neutral  
**This guide is being considered for deletion.**  
*"The Mass Effect games have more or less been superseded by Mass Effect Legendary Edition. We'd like to see these guides [replaced by a MELE guide](https://github.com/framedsc/Sitesource/issues/92)."*  
@end

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
First you will need the [Coalesced Editor](https://www.nexusmods.com/masseffect2/mods/197) in order to add settings and keybinds that you can use in-game. The settings file (coalesced file) is located in `...\Mass Effect 2\BIOGame\CookedPCConsole`. Back it up first. Find the bioinput.ini and then locate the sfxgame portion of it. I will list the settings you must add first, and then explain them later.

Note that each time you must make a new entry called "Bindings" with this application, or you can also do them in batch.

First go to SFXGameModeBase and add the following lines:

```
(Name="F12",Command="Show Scaleform")
(Name="F11",Command="PlayersOnly")
(Name="F10",Command="ToggleFlyCam")
(Name="Insert",Command="InitCredits 500000 | InitPalladium 500000 | InitIridium 500000 | InitEezo 500000 | InitPlatinum 500000")
(Name="O",Command="set materialeffect bshowingame false")
(Name="U",Command="set materialeffect bshowingame true")
(Name="i",Command="FOV 70")
(Name="l",Command="FOV 0")
```

Next add the following lines to SFXGameModeCinematic:

```
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
(Name="Multiply", Command="SloMo 1" )
(Name="Subtract", Command="SloMo 0.5" )
(Name="Add", Command="SloMo 0.01" )
```
________________________________________

Next go to SFXGameModeConversation and add the following lines there: 

```
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
(Name="Multiply", Command="SloMo 1" )
(Name="Subtract", Command="SloMo 0.5" )
(Name="Add", Command="SloMo 0.01" )
```

Now go to SFXGameModeDefault and add these lines: 

```
(Name="F3",Command="God")
(Name="F8",Command="Ghost")
(Name="F4",Command="Walk")
```

Explanation:

`ShowScaleForm` toggles the HUD

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

I tried to make all these keybinds not conflict, but you might want to change them. In any case, always make sure to add your native resolution as one of the keybinds, which is Num8 for me. Add these to Base game mode.

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
In theory, you should now be able to run ME2 fullscreen, hit one of your setres keybinds, and watch the game re-render. In reality, GeDoSaTo is a really finicky program, and you may have to change the settings to get it to work. I now have to get GeDoSaTo to force borderless fullscreen, which is one of the settings you can toggle. I advise you to try stuff that sounds halfway reasonable until you figure it out. 

Mods
==========================================================
So these are just mods I consider essential for screenshotting this game. [ALOT](https://www.nexusmods.com/masseffect2/mods/68) textures takes care of a very high quality base high resolution texture set. The other one that is essential to me is a new one that [removes the vignette](https://www.nexusmods.com/masseffect2/mods/148).