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

Other stuff (not 100% tested):

`r_lodforce 0`  
(Max lod)

`r_texturelodbias -8`  
Sharper textures

##Useful Links

* [DOOM Eternal DevConsole Thread](https://fearlessrevolution.com/viewtopic.php?f=4&t=11889)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Doom_Eternal)