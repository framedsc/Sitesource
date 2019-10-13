![Mass Effect 1](\Images\masss_effect_2.png "Shot by erika.tschinkel")

[//]: #\Images\masss_effect_2.png

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No, but Setres
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (d3d9.dll), but plays poorly with GeDoSaTo sometimes
Ansel | No
Rendering API | DX9

Getting Started: Coalesced Edits
==========================================================
First you will need the <a href="https://www.nexusmods.com/masseffect2/mods/197"> Coalesced Editor</a> in order to add settings and keybinds that you can use in-game. The settings file (coalesced file) is located in `...\Mass Effect 2\BIOGame\CookedPCConsole`. Back it up first. Find the bioinput.ini and then locate the sfxgame portion of it. I will list the settings you must add first, and then explain them later.
___________________

Note that each time you must make a new entry called "Bindings" with this application, or you can also do them in batch.

___________________

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
(Name="F6",Command="set DOFandBloomEffect bUseWorldSettings false")
(Name="F2",Command="set DOFandBloomEffect bUseWorldSettings true")
```

________________________________________

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

________________________________________

Now go to SFXGameModeDefault and add these lines: 

```
(Name="F3",Command="God")
(Name="F8",Command="Ghost")
(Name="F4",Command="Walk")
```
__________________________________

An explanation for some of the less obvious commands:

The command “setDOFAndBloomEffect etc” is a command that tells the game whether or not to use the default post-processing settings or the ones meant for that particular scene. It is for use alongside a cheat table I will provide later on, that allows you to manipulate in-engine depth of field and tonemapping via keybinds. However, thanks to IDK, we now do not always need to tell the game to revert to default post-processing settings anymore in order to change the tonemapping and DoF. Sometimes that section of the cheat table does not work, though, so you have to use the old method.
What you do is: toggle “setDOFAndBloomEffect etc” to “false”, change the tonemapping and DoF (or whatever else) as you see fit, grab the shot, and then change it back to “true.” When you toggle it to “false,” you should see a pretty drastic change in the colors on the screen. Sometimes more than others. Note that it is also usually necessary to add regular movement commands to the cinematic and conversation modes, because these do not usually contain movement keys by default. Lastly "ShowScaleForm" is actually the HUD toggle for some UE3 games, this one included, and unlike in ME3, the HUD does not go off when you toggle the flycam.

_________________________

Note: I also recommend adding ShadowDepthBias=0.100 in the BioEngine.ini to reduce shadow banding. You can search for this value in the editor.


Part II: Custom Resolutions
==========================================================
Unreal Engine 3 has a very useful command, the setres command, which will change the resolution to whatever you tell it to. This can be bound to a key, which means that we can swap resolutions in ME3 from within the game. It’s extremely convenient for taking high resolution shots.
However, the only way this works for resolutions outside our screen resolution is if we use GeDoSaTo. GeDoSaTo allows you to run resolutions outside your screen resolution, downsampled to your screen resolution. This makes up for the fact that UE3 will not allow you to run outside your screen resolution. So what happens is that every time you hit the setres command, it tells the game to go to a resolution outside your screen, which GeDoSaTo allows, and then downsamples that so you can see the whole thing on the screen. Complicated, but very useful. Some of you may use this already for Skyrim.
Setting up the setres commands is a two part process. First you will need to add them to the coalesced file. The format is:
```
( Name="Key", Command="setres WidthxHeight” )
So mine look like this:
( Name="NumPadEight", Command="setres 3840x2160",Alt=True ) 
( Name="NumPadThree", Command="setres 4000x6000",Alt=True ) 
( Name="NumPadFour", Command="setres 7680x3840",Alt=True ) 
( Name="NumPadFive", Command="setres 5000x5000",Alt=True ) 
( Name="NumPadSix", Command="setres 8000x3404",Alt=True )
( Name="NumPadSeven", Command="setres 9000x3000",Alt=True )
```
I tried to make all these keybinds not conflict, but you might want to change them. In any case, always make sure to add your native resolution as one of the keybinds, which is Num8 for me.
Add these to Base game mode.

Next, we have to mirror those in the GeDoSaTo user.ini. Add your resolutions in the following format:
```
renderResolution 3840x2160@60 
```
The @60 is your refresh rate. Leave this the way it is if you do not know.

Then change your “present resolution,” which is the resolution you will downsample to, to your screen resolution:
```
presentWidth 3840 
presentHeight 2160 
presentHz 60 
```
In theory, you should now be able to run ME2 fullscreen, hit one of your setres keybinds, and watch the game re-render. In reality, GeDoSaTo is a really finicky program, and you may have to change the settings to get it to work. I now have to get GeDoSaTo to force borderless fullscreen, which is one of the settings you can toggle. I advise you to try stuff that sounds halfway reasonable until you figure it out. 

Part III: Cheat Table and Console
==========================================================

Enabling the Console: I have only ever managed to get the <a href="https://www.gamewatcher.com/mods/mass-effect-2-mod/better-me2-1-0-0-3#">BetterME2 mod</a> to enable the console, but the mod adds some pretty stupid changes. However, One3rd and I made the cheat table with this mod installed and it turns out that it does not work without it. Note that this cheat table is for the Origin version, which is much easier to use because the DLC situation on the Steam version is sort of complicated.

You can download the Cheat Table (by Erika Tschinkel and One3rd) <a href="..\CheatTables\MassEffect2_For_Origin.CT">here</a>, and the keybinds are in the table.

To use tilt you must pause the game first, which you can do by typing "pause" in the console. Also, to change the FOV, you must use your FOV 70 bind first, and then when you're done you can reset it with your FOV 0 bind. The rest of the table is devoted to in-engine post-processing and DoF. You must first toggle the world settings (as I said above), using F6, and then use the “Post-Processing” script, which I’ve not bound to keys because reasons. So tickthe box (and you can leave this one on if you like) depending on what game mode you’re currently in, and then you can use the hotkeys on the table, or enter the numbers in manually if you would rather. 
Shadows, midtones, and highlights are fairly self-explanatory, as is desaturation. The DoF controls are less so. Near blur and far blur are different from “blur kernel.” You’ll see the degradation in quality when you lower the near or far blur down from 1. I advise, if you want a less strong DoF, to lower the blur kernel size. You can hit “shift” (I think, it might be “alt”) while you hit \ to lower it quickly, because it starts out quite high. Focus distance, self explanatory, but focus inner radius is the distance between near and far blur. It also makes a difference to how gentle the falloff is. Low focus inner radius means a very sharp falloff. Which is a bit different from falloff exponent, which only seems to act on the very end of the DoF. Bloom scale raises or lowers the amount of bloom, and you can use negative values. 


The Home Stretch: Mods
==========================================================
So these are just mods I consider essential for screenshotting this game. First of all <a href="https://www.nexusmods.com/masseffect2/mods/68">ALOT</a> textures takes care of a very high quality base high resolution texture set. The other one that is essential to me is a new one that <a href="https://www.nexusmods.com/masseffect2/mods/148">removes the vignette</a>.