![Devil May Cry 5](Images\dmc5_header.png "Shot by Langgi"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes (With tools)
Reshade | Yes (With DirectX11)
Ansel | No
DirectX versions | DirectX 11, DirectX 12

 
## Tools

* [Camera tools by Otis_Inf, Jim2Point0, Hattiwatti and K-putt](https://github.com/FransBouma/InjectableGenericCameraSystem/tree/master/Cameras/DMC5)  
**Features**: Camera control, Fov, timestop, Hud toggle, Aspect ratio selection, DoF removal.
@alert Important
These tools work with DirectX 11 *only*. So if you use these tools, be sure to switch back to DirectX 11 in the config file of the game, see
*Tips and Tricks* below.
@end
* [Vignette / Barrel distortion fix](https://mega.nz/#!pNgE2aSB!MRoFLYYNvLnL4ptz447rpBShPoaA7wrxNowD5A7hYhA)  
**Features**: Removes the barrel distortion and vignette.  
**Instructions**: Extract files to EXE folder. 

## Tips and Tricks

In order to use ReShade, you'll need the game to boot in DX11. In your game's folder, open `dmc5config.ini` and change the following line:

```TargetPlatform=DirectX11```

## Useful links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Devil_May_Cry_5)