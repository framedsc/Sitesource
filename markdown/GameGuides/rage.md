![Game Title](Images\rage.png "Shot by pino44io"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
Game version | <font face="Stores"> S </font> 1.0.0.1. 
@alert important
Steam offers you two versions of the game to launch. Choose **RAGE 64-bit with Mods (unsupported)**
@end

## Useful Console Commands

Right-click the game icon in your Steam library and select Properties, then click on Set Launch Options and enter `+set com_allowconsole 1`. In-game press Tilde (`) to open up the console.

Command | Description
--|--
`toggle g_showhud` | Toggles the HUD
`toggle hands_show` | Togglles the protagonist's hands
`toggle g_stoptime 1 0 ` | Toggles timestop. The protagonist can still move around
`noclip` | Enables noclip mode
`pm_noclipspeed X` | Controls the noclip Mode speed, e.g. `pm_noclipspeed 150`
`g_fov X` | Controls the Field of View. Default is 80
`cvaradd g_fov 1` | Increases Field of View
`cvaradd g_fov -1` | Decreases Field of View
`cvaradd pm_thirdperson 1` | Enables third-person model
`cvaradd pm_thirdperson -1` | Disables third-person model
`cvaradd pm_thirdpersonrange 1` | Increases the camera range in third-person
`cvaradd pm_thirdpersonrange -1` | Decreases the camera range in third-person
`cvaradd pm_thirdpersonclip -1` | Removes the clipping of the third-person camera
`r_skipglare 1/0 ` | Disables post-processing effects. Default values is 0
`notarget` | Enables invisibility

@alert tip
You can bind the commands to specific keys. For example, `bind F1 "toggle g_showhud"`. Also, you can combine them, like `bind F1 "toggle g_showhud;toggle hands_show"`
@end

## Installing Reshade
Please be sure to inject the ***Rage Tool Kit (Rage64.exe)*** process.

## Hotsampling
The game needs to run in windowed mode in order to hotsample correctly to different aspect ratios. You can use [SRWE](https://github.com/dtgDTGdtg/SRWE) or [Universal Unreal Engine 4 Unlocker](https://www.patreon.com/Otis_Inf).

## Graphic tweaks
To increase texture buffer, right-click the game icon in your Steam library and select *Properties*, then click on Set Launch Options and enter the following:

```
*+fc maxcachememoryMB 1024 +vt_maxPPF "16" +vt_pageimagesizevmtr 16384 +vt_pageImageSizeUnique 16384 +vt_pageImageSizeUniqueDiffuseOnly 16384 +vt_pageImageSizeUniqueDiffuseOnly2 16384*
```
## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/RAGE)
* [Rage Wiki](https://rage.fandom.com/wiki/Tweaks)
