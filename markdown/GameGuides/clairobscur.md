![Clair Obscur: Expedition 33](Images\clairobscurheader.jpg "Shot by Otis_Inf"){.shadowed .autosize}
## Summary
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (use windowed mode)
DSR | Yes
Custom Aspect Ratios | Yes  
Reshade | Yes
Ansel | No
Graphics API | DirectX 12
 
## Tools

* [Unreal Engine Unlocker v5.4.11 or higher](https://opm.fransbouma.com/uuuv5.htm) (Not free, only available on Patreon)  
**Features**: Camera control, custom lights, dev console, game speed, pause/timestop, black bar removal, hud toggle, post processing, camera paths, pose tools, animation control on selected actors
* [Lyall's Clair Obscur fix](https://codeberg.org/Lyall/ClairObscurFix) (Free)  
**Features**: Dev console, skip intro logos, black  bar removal, dev console. 

## Tips and Tricks

### Tweaks

The following tweaks will make the game look much better: Paste the following block on the dev console. 

```
r.maxanisotropy 16 | r.Streaming.LimitPoolSizeToVRAM 0| r.Streaming.MaxTempMemoryAllowed 4096|r.SceneColorFringe.Max 0| r.StaticMeshLODDistanceScale 0.001 | foliage.LODDistanceScale 6 | r.SkeletalMeshLODBias -1 | r.viewdistancescale 10 | r.depthoffieldquality 0 | Grass.Densityscale 2 | r.Shadow.NaniteLODBias 0 | r.DynamicRes.MinScreenPercentage 100 | r.tonemapper.sharpen 0.5 | r.SSFS.VolumetricFogILSIntensity 0.1 | r.Lumen.Reflections.DownsampleFactor 0.0 | r.postprocessing.disablematerials 1
```

It will lower the fog scattering and remove the sharpening due to materials. It will also increase LODs on some elements. 

To fully get rid of the upscaling, use: 

```
r.SecondaryScreenPercentage.GameViewport 100
```

Additionally to that, be sure to use TSR and *Custom 100%* for upscaling in the game's menu. 

### Animations and posing

With the UUU v5 you can select a character (not in cutscenes) and set animations using the overlay: press `Ctrl-Insert` to open the UUU overlay and, after enabling the camera, 
click a character. On the *Actor selction and manipulation* tab go to the *Experimental options* and click it open. For Component you can select the CharacterMesh or the Face_1 component
Selecting a component offers different Skeletal Meshes (skins) and animations. This way you can set an animation on the body (CharacterMesh0) and a different one on the head (Face_1). 

By stopping the animation and then increasing the play position using the mouse (click & drag) you can select the right frame, creating unique poses!

If you want to have fully control over your pose, click the *Show pose editor* button to bring up the bone tree window. Here you can change every bone's size, location and orientation
to fully setup your character's pose. 

### To be aware of

- After spawning a custom light, make sure to select the Light channel 3 for having a light affect a character. To do this, click on the Pencil icon of the light in the UUU's 
light list and in the light editor that pops up, at the bottom you can select the light channels. 

- When you're done with the lights, be sure to remove them, as it can be the game will crash if you go to another location. 

## Useful Links

- [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Clair_Obscur:_Expedition_33)