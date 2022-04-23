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
Graphics API | DX9

\* resolutions can be set to hotkeys which give an advantage similar to hotsampling

INI Edits
==========================================================

Find your `Documents/Bioware/Mass Effect/Config` folder and open `BIOInput.ini`.

Add these settings under [BIOC_Base.BioPlayerInput]
```
Bindings=(Name="NumPadOne",Command="show scaleform")
Bindings=(Name="NumPadTwo",Command="FOV 0")
Bindings=(Name="NumPadThree",Command="FOV 70")
Bindings=(Name="NumPadFour",Command="SloMo 0.5")
Bindings=(Name="NumPadFive",Command="SloMo 1")
Bindings=(Name="NumPadSeven",Command="ghost")
Bindings=(Name="NumPadEight",Command="walk")
Bindings=(Name="NumPadNine",Command="ToggleFlyCam")
Bindings=(Name="Multiply",Command="PlayersOnly")
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

Unreal Engine has a command called `setres` that can be used to bind hotkeys to specific resolutions. In order to achieve resolutions are higher than your monitor supports, you can use DSR (see our guide for custom DSR resolutions). If for whatever reason DSR doesn't work, you can also do this in a program called GeDoSaTo.

However, the only way this works for resolutions outside our screen resolution is if we use GeDoSaTo. GeDoSaTo allows you to run resolutions outside your screen resolution, downsampled to your screen resolution. This makes up for the fact that UE3 will not allow you to run outside your screen resolution. So what happens is that every time you hit the setres command, it tells the game to go to a resolution outside your screen, which GeDoSaTo allows, and then downsamples that so you can see the whole thing on the screen. Complicated, but very useful. Some of you may use this already for Skyrim.

Setting up the setres commands is a two part process. First you will need to add them to the coalesced file. The format is: `( Name="Key", Command="setres WidthxHeight" )`, so mine look like this:

Hotkeys are just examples. Please feel free to choose your own. In these examples, I swap between a resolution that will fit on a 1440p screen, then use the same hotkey + ALT to switch to a higher resolution in the same aspect ratio.
```
Bindings=(Name="F1",Command="setres 2560x1440")
Bindings=(Name="F1",Command="setres 7680x4320")
Bindings=(Name="F2",Command="setres 1080x1440")
Bindings=(Name="F2",Command="setres 4800x6300")
Bindings=(Name="F3",Command="setres 3440x1440")
Bindings=(Name="F3",Command="setres 6880x2880")
```

Sometimes the game will not allow certain keys to be bound to commands. So experiment to find what works.

If you need to use GeDoSaTo, here's how you can configure the resolutions above to work in the GeDoSaTo config file.

```
#16:9
renderResolution 7680x4320@60

#3:4
renderResolution 1080x1440@60
renderResolution 4800x6400@60

#21:9
renderResolution 3440x1440@60
renderResolution 6880x2880@60
```


Mods
==========================================================
[High quality textures](https://www.nexusmods.com/masseffect/mods/83)  
[Vignette Removal](https://www.nexusmods.com/masseffect/mods/104)