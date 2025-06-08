![Alan Wake 2](Images\AW2.png "Shot by IronGauntlet"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | Yes
Graphics API | DirectX 11/12
Game version | 1.2.8
 
## Tools

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**[Features](https://opm.fransbouma.com/Cameras/alanwake2.htm)**: Camera control, FoV control, HUD toggle, timestop/gamespeed, hotsampling

## How to get rid of ingame DOF/vignette/lens distortion effects

You can use the game's photomode to disable them separately for each shot. To disable them permanently, open Renderer.ini (located in %LOCALAPPDATA%\Remedy\AlanWake2) in Notepad and change the following settings to these values:

"m_bVignette": false,
"m_bDepthOfField": false,
"m_bLensDistortion": false,
"m_bUnlockAspectRatio": true

@alert tip
Clear out an area before taking shots, enemies can cause artifacts like blurring/lens distortion.
@end

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Alan_Wake_II)