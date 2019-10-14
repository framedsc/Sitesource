![Mass Effect 1](\Images\mass_effect_3.png "Shot by erika.tschinkel")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No, but Setres
DSR | Yes
Custom Aspect Ratios | Yes and with tools
Reshade | Yes (d3d9.dll), but plays poorly with GeDoSaTo sometimes
Ansel | No
Rendering API | DX9

Getting Started: Coalesced Edits
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

An explanation for some of the less obvious commands:
The command "setDOFAndBloomEffect etc" is a command that tells the game whether or not to use the default post-processing settings or the ones meant for that particular scene. It is for use alongside a cheat table I will provide later on, that allows you to manipulate in-engine depth of field and tonemapping via keybinds. However, thanks to IDK31, we now do not always need to tell the game to revert to default post-processing settings anymore in order to change the tonemapping and DoF. Sometimes that section of the cheat table does not work, though, so you have to use the old method.

What you do is: toggle "setDOFAndBloomEffect etc" to "false", change the tonemapping and DoF (or whatever else) as you see fit, grab the shot, and then change it back to "true." When you toggle it to "false," you should see a pretty drastic change in the colors on the screen. Sometimes more than others. The comma key will reset the settings to default, in case you’ve gone a little off the rails.

Now, the "HeightFogComponent" commands toggle fog on and off, also for use with the cheat table. I honestly do not recommend messing around with fog, because getting back to the default settings is a bit difficult. But it can look cool, and you can use it for single color backgrounds for taking portraits by setting the density really high and changing the start distance to be right behind your character. (More on that below.)

Home and End effectively allow you to completely holster your weapon, but at a price. They switch your characters between combat and explore mode, and unfortunately that mode persists across saves and locations, so you’ll find yourself in explore mode when you want to fight, and combat mode on the Normandy, for example. Big pain in the ass. It doesn’t always last forever, but I recommend saving (hard save, not quick save) before you do it and just going back to your save afterwards.

Note: I also recommend adding ShadowDepthBias=0.100 in the BioEngine.ini to reduce shadow banding. You can search for this value in the editor.

Part II: Custom Resolutions
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

Yes, it gets worse: The Cheat Table
==========================================================
Okay, so now that your brain has fallen out, remember I mentioned a cheat table? This is a joint effort by three people: me (Erika Tschinkel), IDK31 (mentioned above) and One3rd. It is a bit messy, despite parts of it having an overhaul by a much neater (than me) IDK31.

You can download the silly thing [here](..\CheatTables\MassEffect3_complete.CT).

The hotkeys are listed on the table, but I’ll try to explain some of the nomenclature.

I made this table initially for two reasons: 1) camera tilt, and 2) modifying post-processing through hotkeys.

I’ll start with 1). There are two ways to do this, but one is generally more desirable. The original way of doing this was to pause the game (you can enter "pause" in the console to do this--it cannot be bound to a key for some reason) and then press "Page Up," and with the numpad you can use the camera, including tilt. This is still useful when you want to stop certain background effects in a certain place. The new way, however, thanks to IDK31, is to hit "Insert" and then you do not need to use the pause command in order to use the camera. 

This is useful for when you want to move very slightly, or of course for camera tilt. I should note that it seems that disabling the Freecam script crashes the game. So just keep it on. Additionally, in order to use the FOV controls, you must hit your FOV 70 bind first. Hit the FOV 0 bind to reset the FOV.

Now onto 2). This is significantly more complex. There is an old and a new way to do this as well. The old way is to toggle the world settings (as I said above), using F6, and then use the "Post-Processing" and "Post-Processing Cutscenes" scripts, which I’ve not bound to keys because reasons. So tick one or both of those boxes (and you can leave this one on if you like) depending on what game mode you’re currently in, and then you can use the hotkeys on the table, or enter the numbers in manually if you would rather. The new way is to start the "New PP" script and this will allow you to modify the colors on top of the world settings. These changes will revert upon loading a save or changing areas, in case you want to go back to default for that scene.

Shadows, midtones, and highlights are fairly self-explanatory, as is desaturation. The DoF controls are less so. Near blur and far blur are different from "blur kernel." You’ll see the degradation in quality when you lower the near or far blur down from 1. I advise, if you want a less strong DoF, to lower the blur kernel size. You can hit "shift" (I think, it might be "alt") while you hit \ to lower it quickly, because it starts out quite high. Focus distance, self explanatory, but focus inner radius is the distance between near and far blur. It also makes a difference to how gentle the falloff is. Low focus inner radius means a very sharp falloff. Which is a bit different from falloff exponent, which only seems to act on the very end of the DoF. Bloom scale raises or lowers the amount of bloom, and you can use negative values. 

When you’re in default game mode, using the "New PP" script, you can add DoF. However, you do not seem to be able to change DoF during cutscenes with this script. Which is unfortunate. And also the script often doesn’t work during cutscenes, which means you have to use the "Post-Processing Cutscenes" script along with the F6 key toggling to world settings. Sorry about this, I dunno if I’ll fix it because it’s a pain.

And there are fog controls. Height, density, and color are pretty self explanatory. Start distance is obviously how close the fog comes to the screen, and extinction distance alters how quickly it dissipates. A very low extinction distance and high density will make a kind of fog useful for backgrounds in portraits. But as I said, it can be a pain to alter the fog, because the settings are unique to each scene.

Another extremely useful script is the AR script (aspect ratio). This is for changing the resolution in cutscenes. Cutscenes will only render in 16:9 unless you hit "Alt-P" after you use the setres commands. Try it! It’s very cool.

Tint and Flares are fairly self-explanatory, but I have not bound them to keys, because I literally ran out of keys. But you can use these scripts to modify the overall tint of the scene or change the flares.

Render Flags is just a bunch of different stuff you can try out. I don’t find it too useful but you never know.

The Home Stretch: Mods
==========================================================
So these are just mods I consider essential for screenshotting this game. First of all [ALOT](https://www.nexusmods.com/masseffect3/mods/363) textures takes care of a very high quality base high resolution texture set. The other one that is essential to me is a new one that [removes the vignette](https://www.nexusmods.com/masseffect3/mods/523).

