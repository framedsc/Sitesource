![Remember Me](\Images\remember_me.png "Shot by Otis_Inf")

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
Go to your `Documents/My Games/UnrealEngine4/RememberMeGame` folder and open the ExampleInput.ini (yes it really is "ExampleInput"). 

Under [Engine.PlayerInput] add:
```
Bindings=(Name="F1",Command="Pause")
Bindings=(Name="N",Command="FOV 70",alt=true)
Bindings=(Name="F2",Command="set DOFEffect bUseWorldSettings true")
Bindings=(Name="F6",Command="set DOFEffect bUseWorldSettings false")
Bindings=(Name="F3",Command="PlayersOnly")
Bindings=(Name="F4",Command="Ghost")
Bindings=(Name="F5",Command="Walk")
Bindings=(Name="F7",Command="God")
Bindings=(Name="F8",Command="SloMo 1")
Bindings=(Name="F9",Command="SloMo 0.5")
Bindings=(Name="F12",Command="SloMo 0.1")
Bindings=(Name="Multiply",Command="ShowHUD")
Bindings=(Name="Decimal",Command="ToggleHUD")
```

An explanation for some of the less obvious commands:

The command "setDOFAndBloomEffect etc" is a command that tells the game whether or not to use the default post-processing settings or the ones meant for that particular scene. It is for use alongside a cheat table I will provide later on, that allows you to manipulate in-engine depth of field and tonemapping via keybinds. However, thanks to IDK, we now do not always need to tell the game to revert to default post-processing settings anymore in order to change the tonemapping and DoF. Sometimes that section of the cheat table does not work, though, so you have to use the old method.

What you do is: toggle "setDOFAndBloomEffect etc" to "false", change the tonemapping and DoF (or whatever else) as you see fit, grab the shot, and then change it back to "true." When you toggle it to "false," you should see a pretty drastic change in the colors on the screen. Sometimes more than others. Note that it is also usually necessary to add regular movement commands to the cinematic and conversation modes, because these do not usually contain movement keys by default. Lastly "ShowScaleForm" is actually the HUD toggle for some UE3 games, this one included, and unlike in ME3, the HUD does not go off when you toggle the flycam.

Part II: Custom Resolutions
==========================================================

Unreal Engine 3 has a very useful command, the setres command, which will change the resolution to whatever you tell it to. This can be bound to a key, which means that we can swap resolutions in ME3 from within the game. It’s extremely convenient for taking high resolution shots.

However, the only way this works for resolutions outside our screen resolution is if we use GeDoSaTo. GeDoSaTo allows you to run resolutions outside your screen resolution, downsampled to your screen resolution. This makes up for the fact that UE3 will not allow you to run outside your screen resolution. So what happens is that every time you hit the setres command, it tells the game to go to a resolution outside your screen, which GeDoSaTo allows, and then downsamples that so you can see the whole thing on the screen. Complicated, but very useful. Some of you may use this already for Skyrim.

Setting up the setres commands is a two part process. First you will need to add them to the coalesced file. The format is:
( Name="Key", Command="setres WidthxHeight" )
So mine look like this:

```
Bindings=(Name="P",Command="SetRes 4320x7680",ctrl=true)
Bindings=(Name="L",Command="SetRes 4500x6000",ctrl=true)
Bindings=(Name="M",Command="SetRes 7680x3840")
Bindings=(Name="O",Command="SetRes 5000x5000",ctrl=true)
Bindings=(Name="P",Command="SetRes 8000x3404",alt=true)
Bindings=(Name="L",Command="SetRes 9000x3000",alt=true)
Bindings=(Name="M",Command="SetRes 6000x4000",alt=true)
Bindings=(Name="K",Command="SetRes 3840x2160")
```

Note that these are kind of weird keybinds, but it's so they don't conflict with the cheat table.

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
In theory, you should now be able to run Remember Me fullscreen, hit one of your setres keybinds, and watch the game re-render. In reality, GeDoSaTo is a really finicky program, and you may have to change the settings to get it to work. 


Part III: Other tweaks
==========================================================
Textures LOD Streaming: I recommend adding "NumStreamedMips=0" to the end of each "TextureGroup" setting in the ExampleEngine.ini file under the "[SystemSettings]" section.

Additionally, these lighting settings helped me in the ExampleEngine.ini in order to alleviate shadow banding.
```
LightEnvironmentShadows=True
ShadowFilterQualityBias=8
MinShadowResolution=256
MaxShadowResolution=2048
ShadowFadeResolution=256
ShadowDepthBias=0.100
```
Removing the HUD During Combat: This is a bit tricky. You have to alternate between ghost and walk a couple of times to get it to go away. This does not work in boss fights, however, for the boss meter thing. But there is one advantage, which is that you can actually move Nilin after toggling PlayersOnly during combat, and maintain her pose. However, once you do this and then resume combat, Nilin won't be able to punch or kick anything. You'll have to shoot something first with the spammer, and it should be fine after that. I found that the HUD came back, also, so you won't be fighting blind or have any subsequent issues.

Part IV: Cheat table
==========================================================
[This table](..\CheatTables\RememberMeFinal3.CT) is by both me (Erika Tschinkel) and Jim2point0. Jim2point0 did the actual camera script, and I added UE3 DoF and post-processing tweaks to it. Hotkeys are in the table.

To use the post-processing and DOF you must first toggle the world settings (as I said above), using F6, and then use the "Post-Processing" script, which is toggled with PageDown. Shadows, midtones, and highlights are fairly self-explanatory, as is desaturation. The DoF controls are less so. Near blur and far blur are different from "blur kernel." You’ll see the degradation in quality when you lower the near or far blur down from 1. 

I advise, if you want a less strong DoF, to lower the blur kernel size. You can hit "shift" (I think, it might be "alt") while you hit X to lower it quickly, because it starts out quite high. Focus distance, self explanatory, but focus inner radius is the distance between near and far blur. It also makes a difference to how gentle the falloff is. Low focus inner radius means a very sharp falloff. Which is a bit different from falloff exponent, which only seems to act on the very end of the DoF. Bloom scale raises or lowers the amount of bloom, and you can use negative values. 

There are also some cheats in the table if you are as irritated by the game as I was, so go for that.

Another cheat table, with smooth rotating controls can be found [here](https://steamcommunity.com/sharedfiles/filedetails/?id=662482735), made by IDK31.
Please read the guide at that link for download and details about the controls and other features it has.


Home Stretch: Mods
==========================================================
High Res Nilin Textures: for the [starting outfit](https://www.nexusmods.com/rememberme/mods/1), and her 
[regular outfit](https://www.nexusmods.com/rememberme/mods/5). 

No Vignette: [this](http://www.mediafire.com/file/vj4jibkah9tuauv/RM_No_Vignette.7z/file) is a texmod that I (Erika Tschinkel) made for use with this game. 