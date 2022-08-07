![NieRAutomata](Images\nier-automata-header.png "Shot by Midhras"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (with tools)
DSR | Yes
Custom Aspect Ratios | Yes (with tools)
Reshade | Yes
Ansel | No
Graphics API | DirectX 11

@alert neutral
**This guide is fairly outdated.** *I tried to get things working again to middling success. The tools often conflicted and would not produce desired results. I'll write down how far I got, if you get further please do update the guide. - moyevka,  21/04/22.*  

The Otis camera tools are for the **Steam 15/07/2021 patch**. The CT is for game versions prior to that. 

**The FAR mod has been superseded by Special K** as a whole, but the latest versions of Special K conflict with Otis tools upon injection. I had luck with [Special K ver. 21.07.22](https://wiki.special-k.info/SpecialK/Tools#previous-versions-of-special-k).

Reshade 5.1.0+ seems to cooperate with Special K. Follow the [Special K Reshade setup guide](https://wiki.special-k.info/en/SpecialK/ReShade). As below, depth buffer access is only available with AA turned off.

For the most part, Otis tools work. The only thing that's unreliable is hotsampling. Sometimes it works fine, sometimes it just doesn't. I suspect it might be a Special K conflict, but I couldn't solve it. Occasionally, timestopping wouldn't work, but that seems to be location-specific.
@end
 
##Tools

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**[Features](https://opm.fransbouma.com/Cameras/nierautomata.htm)**: Camera control, FoV control, HUD toggle, timestop/gamespeed, hotsampling, post-processing toggles, invulnerability toggle
* [CE table by IDK31 and Smithfield](..\CheatTables\nier_automata_121.ct)  
**Features**: Camera control, FoV, Speed control, HUD/Vignette/Banding/Character halo removal, Tonemap

##Useful Links

* [Hi-res Textures Pack by GPUnity](https://www.nexusmods.com/nierautomata/mods/5)
* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Nier:_Automata)

##Additional Notes
* To change aspect ratio, set the game to windowed mode and use custom resolution or DSR [(Custom res guide here)](..\GeneralGuides\custom_dsr_resolutions.htm)
* Depth buffer inaccessible with in-game AA turned on, turn off AA to get depth
