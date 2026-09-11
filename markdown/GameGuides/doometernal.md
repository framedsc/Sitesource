![DOOM Eternal](Images\doometernal_header.png "Shot by ItsYFP"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes 
DSR | Unknown
Custom Aspect Ratios | Yes
Reshade | Yes (Vulkan)
Ansel | No
Graphics API | Vulkan
 
## Tools

* [Dev Console cheat table by SunBeam]( ..\CheatTables\DOOMEternalx64vk.CT )  
**Features**: Developer Console/Commands (mainly for early Photomode in our case). 
See [https://fearlessrevolution.com/viewtopic.php?f=4&t=11889](https://fearlessrevolution.com/viewtopic.php?f=4&t=11889) for details.


## Tips and Tricks

### Console Commands/Hotsampling Info

DOOM Eternal does support Hotsampling with Limits. While every Horizontal AR (16:9, 21:9 etc) seems to work, Vertical AR gets squinched.

Open console with tilde, you can copy and paste commands into the console.

`g_allowphotomode 1`  
Enable photomode before finishing a level

`photomode_freecamleashdistance -1`  
Disable the range limiter

`photomode_freecammovementtype 2`  
Disable the camera collision

### Other Interesting Commands for Better Images ###

```
r_antialiasing 0 - 0 = Disabled, 1 = Temporal SSAA (32x), 2 = Nvidia DLSS
g_showPlayerShadow 1 - enables shadow of player model
r_shadowPlayerLOD 0 - shadow lod level for player/weapon shadow
r_shadowAtlasHeight 16384 - Shadow map size in height, 8192 ( default ) 
r_shadowAtlasWidth 16384 - Shadow map size in width, 8192 ( default ) 
r_shadowAtlasTileSize 5200 - Shadow size. Default is "2048".
r_shadowLodForceValue 0 - Force a specific lod level for shadow rendering of dynamic models. -1: Use the same LoD as opaque.
r_cloudsQuality 3 - 0: low, 1: medium, 2: high, 3: very high
r_cloudsQualityUseJitter 0 - 1: use jitter, 0: no jitter ( needs higher quality r_cloudsQuality cvar value )
r_lodScale 1.5 - Scale for LODs (use smaller value to switch lods more aggressively)
r_lodForce -1 - render a specific lod only
r_lodRender -1 - renderer uses lods 
r_filmGrainRatio -1 - Film grain - allow overriding art settings
r_dlssTextureLodBias -5 - DLSS texture LOD epsilon bias
r_dofHalfRes 0 - 0 = full res, 1 = half res ( default )
r_texturelodbias -8 - Set custom lod bias for textures (sharpness)
```
@alert neutral
Do not switch the `r_antialiasing` from 0 to 1 or 2 as it will make the game hanging and unresponsive.
About the `r_shadowAtlasTileSize`, you can use 4096 if you leave the default for `r_shadowAtlasWidth`.
the film grain is still noticeable even if set at 0. For this, setting `r_filmGrainRatio` to -1 will disable it completely.
If you have a GPU that support DLSS, it would help more to set the AA to it and play with the `r_dlssTextureLodBias`.
@end

##Useful Links

* [DOOM Eternal DevConsole Thread](https://fearlessrevolution.com/viewtopic.php?f=4&t=11889)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Doom_Eternal)
