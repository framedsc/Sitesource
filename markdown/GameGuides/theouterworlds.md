![The Outer Worlds](Images\theouterworlds_header.png "Shot by Otis_Inf"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | unknown
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | No
Graphics API | DirectX 11
 
## Tools

* [Universal Unreal Engine 4 Unlocker (UUU) by Otis_Inf](../GeneralGuides/universal_ue4_consoleunlocker.htm)  
**Features**: Camera, Pause Game, FOV Control, in-game console, hotsampling controls.

## Tips and Tricks

### Useful engine tweaks

The following set of commands can be used to tweak the engine to a high level and get rid of e.g. the CA in this game and other lens distortion. Copy the
string below as a whole and paste it in the in-game console once you've enabled the Universal Unreal Engine 4 Unlocker on it. You have to do this once.

```
sg.ShadowQuality 5| r.Shadow.DistanceScale 4 | r.AmbientOcclusionMaxQuality -100 | r.Shadow.SpotLightTransitionScale 1024 | r.Shadow.TransitionScale 1024 | sg.FoliageQuality 5|sg.ViewDistanceQuality 5|sg.PostProcessQuality 5|sg.EffectsQuality 5|sg.TextureQuality 5| r.Streaming.LimitPoolSizeToVRAM 0|r.Streaming.PoolSize 4096|r.Streaming.MaxTempMemoryAllowed 256|r.SSR.Quality 5 |r.MaxQualityMode 1|r.StaticMeshLODDistanceScale 0.001|r.maxanisotropy 16 | foliage.LODDistanceScale 50 |r.SkeletalMeshLODBias -1 | r.SceneColorFringeQuality 0 | r.lensflarequality 0 | r.motionblurquality 0| r.SSS.Checkerboard 0 | r.MipMapLODBias -2
```

### Toggle HUD

To toggle the HUD, open the in-game console and type: `showhud 0`. Type it again (or press cursor up to get the last command) to enable the HUD again. 
This works also when the game is paused with `Page Down` (The 'slomo' pause in the UUU). 

### Take shots of your character

To take shots of your character, you need to use the following steps (This works with the latest patch of the game):

- Pause the game with `Page Down`
- Press `Ins` to enable the camera
- Press `Esc` to bring up the menu
- Click 'Idle camera'
- You'll now see your character and you can take shots of it. If you press `Page Down` again, you can wait for a nice idle animation and
press `Page Down` to pause the game again. 

Once you press a key again when the UUU camera is disabled, the game will flip the model back to the two arms and gun model as used in regular gameplay. 


##Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/The_Outer_Worlds)
