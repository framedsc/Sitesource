![Mass Effect 1](\Images\masss_effect.png "Shot by erika.tschinkel")

[//]: #\Images\masss_effect.png

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

Getting Started: Ini Edits
==========================================================

Go to your `Documents/Bioware/Mass Effect/Config` folder and open the BIOInput.ini.

Add these settings under [BIOC_Base.BioPlayerInput]
```
Bindings=(Name="NumPadOne",InputMode=BIO_INPUT_MODE_NONE,Command="show scaleform",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadTwo",InputMode=BIO_INPUT_MODE_NONE,Command="FOV 0",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadThree",InputMode=BIO_INPUT_MODE_NONE,Command="FOV 70",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadSix",InputMode=BIO_INPUT_MODE_NONE,Command="set DOFAndBloomEffect bUseWorldSettings false",Control=False,Shift=False,Alt=False)
Bindings=(Name="F10",Command="set DOFAndBloomEffect bUseWorldSettings true")
Bindings=(Name="NumPadFour",InputMode=BIO_INPUT_MODE_NONE,Command="SloMo 0.5",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadFive",InputMode=BIO_INPUT_MODE_NONE,Command="SloMo 1",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadSeven",InputMode=BIO_INPUT_MODE_NONE,Command="ghost",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadEight",InputMode=BIO_INPUT_MODE_NONE,Command="walk",Control=False,Shift=False,Alt=False)
Bindings=(Name="NumPadNine",InputMode=BIO_INPUT_MODE_NONE,Command="ToggleFlyCam",Control=False,Shift=False,Alt=False)
Bindings=(Name="Multiply",Command="PlayersOnly")
```

An explanation for some of the less obvious commands:

The command “setDOFAndBloomEffect etc” is a command that tells the game whether or not to use the default post-processing settings or the ones meant for that particular scene. It is for use alongside a cheat table I will provide later on, that allows you to manipulate in-engine depth of field and tonemapping via keybinds. However, thanks to IDK, we now do not always need to tell the game to revert to default post-processing settings anymore in order to change the tonemapping and DoF. Sometimes that section of the cheat table does not work, though, so you have to use the old method.
What you do is: toggle “setDOFAndBloomEffect etc” to “false”, change the tonemapping and DoF (or whatever else) as you see fit, grab the shot, and then change it back to “true.” When you toggle it to “false,” you should see a pretty drastic change in the colors on the screen. Sometimes more than others. Note that it is also usually necessary to add regular movement commands to the cinematic and conversation modes, because these do not usually contain movement keys by default. Lastly "ShowScaleForm" is actually the HUD toggle for some UE3 games, this one included, and unlike in ME3, the HUD does not go off when you toggle the flycam. Also "show ScaleForm" is the HUD Toggle for this game.


Note: I also recommend adding ShadowDepthBias=0.100 in the BioEngine.ini to reduce shadow banding. You can search for this value in your text editor.


Part II: Custom Resolutions
==========================================================

Unreal Engine 3 has a very useful command, the setres command, which will change the resolution to whatever you tell it to. This can be bound to a key, which means that we can swap resolutions in ME3 from within the game. It’s extremely convenient for taking high resolution shots.
However, the only way this works for resolutions outside our screen resolution is if we use GeDoSaTo. GeDoSaTo allows you to run resolutions outside your screen resolution, downsampled to your screen resolution. This makes up for the fact that UE3 will not allow you to run outside your screen resolution. So what happens is that every time you hit the setres command, it tells the game to go to a resolution outside your screen, which GeDoSaTo allows, and then downsamples that so you can see the whole thing on the screen. Complicated, but very useful. Some of you may use this already for Skyrim.
Setting up the setres commands is a two part process. First you will need to add them to the coalesced file. The format is:
```
( Name="Key", Command="setres WidthxHeight” )
So mine look like this:
Bindings=(Name="L",InputMode=BIO_INPUT_MODE_NONE,Command="setres 4500x6000",Control=False,Shift=False,Alt=True)
Bindings=(Name="L",InputMode=BIO_INPUT_MODE_NONE,Command="setres 4320x7680",Control=False,Shift=False,Alt=False)
Bindings=(Name="Add",InputMode=BIO_INPUT_MODE_NONE,Command="setres 6000x4000",Control=False,Shift=False,Alt=False)
Bindings=(Name="K",InputMode=BIO_INPUT_MODE_NONE,Command="setres 4000x6000",Control=False,Shift=False,Alt=False)
Bindings=(Name="Subtract",InputMode=BIO_INPUT_MODE_NONE,Command="setres 7680x3840",Control=False,Shift=False,Alt=False)
Bindings=(Name="Home",InputMode=BIO_INPUT_MODE_NONE,Command="setres 5000x5000",Control=False,Shift=False,Alt=False)
Bindings=(Name="H",InputMode=BIO_INPUT_MODE_NONE,Command="setres 8000x3404",Control=False,Shift=False,Alt=False)
Bindings=(Name="End",InputMode=BIO_INPUT_MODE_NONE,Command="setres 9000x3000",Control=False,Shift=False,Alt=False)
Bindings=(Name="Equals",InputMode=BIO_INPUT_MODE_NONE,Command="setres 3840x2160",Control=False,Shift=False,Alt=False)
```

Note that these are kind of weird keybinds, but I found that this game really doesn't like certain commands to be bound to certain keys. I recommend, just to save yourself the hassle, that you use my exact keybinds for everything.

Next, we have to mirror those in the GeDoSaTo user.ini. Add your resolutions in the following format:

```
renderResolution 3840x2160@60 
```
The @60 is your refresh rate. Leave this the way it is if you do not know.

Then change your “present resolution,” which is the resolution you will downsample to, to your screen resolution:
presentWidth 3840 
presentHeight 2160 
presentHz 60 
In theory, you should now be able to run ME1 fullscreen, hit one of your setres keybinds, and watch the game re-render. In reality, GeDoSaTo is a really finicky program, and you may have to change the settings to get it to work. I now have to get GeDoSaTo to force borderless fullscreen, which is one of the settings you can toggle. I advise you to try stuff that sounds halfway reasonable until you figure it out. 


Part III: Cheat Table
==========================================================

You can download the Cheat Table (by Erika Tschinkel) <a href="..\CheatTables\MassEffectWIP4.CT">here</a>, and the keybinds are in the table.

To use tilt you must pause the game first, which you can do by typing "pause" in the console. Also, to change the FOV, you must use your FOV 70 bind first, and then when you're done you can reset it with your FOV 0 bind. The rest of the table is devoted to in-engine post-processing and DoF. You must first toggle the world settings (as I said above), using F6, and then use the “Post-Processing” script, which I’ve not bound to keys because reasons. So tickthe box (and you can leave this one on if you like) depending on what game mode you’re currently in, and then you can use the hotkeys on the table, or enter the numbers in manually if you would rather. 
Shadows, midtones, and highlights are fairly self-explanatory, as is desaturation. The DoF controls are less so. Near blur and far blur are different from “blur kernel.” You’ll see the degradation in quality when you lower the near or far blur down from 1. I advise, if you want a less strong DoF, to lower the blur kernel size. You can hit “shift” (I think, it might be “alt”) while you hit \ to lower it quickly, because it starts out quite high. Focus distance, self explanatory, but focus inner radius is the distance between near and far blur. It also makes a difference to how gentle the falloff is. Low focus inner radius means a very sharp falloff. Which is a bit different from falloff exponent, which only seems to act on the very end of the DoF. Bloom scale raises or lowers the amount of bloom, and you can use negative values. 


The Home Stretch: Mods
==========================================================
So these are just mods I consider essential for screenshotting this game. First of all <a href="https://www.nexusmods.com/masseffect/mods/83">ALOT</a> textures takes care of a very high quality base high resolution texture set. The other one that is essential to me is a new one that <a href="https://www.nexusmods.com/masseffect/mods/104">removes the vignette</a>.