![Devil May Cry 5](Images\dmc5_header.png "Shot by Langgi"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes (With tools)
Reshade | Yes (With DirectX11)
Ansel | No
Graphics API | DirectX 11, DirectX 12

 
## Tools

* [Camera tools by Otis_Inf, Jim2Point0, Hattiwatti and K-putt](https://www.patreon.com/Otis_Inf)  
**Features**: Camera control, Fov, timestop, Hud toggle, Aspect ratio selection, DoF removal, Vignette removal and Lens distortion removal. For more info refear to the [tool docs](https://opm.fransbouma.com/Cameras/dmc5.htm).
* [RELit by Originalnicodr and Otis_inf](https://github.com/originalnicodr/RELit)  
**Features**: Lighting Control, turn off scene lights, exposure control.  
Make sure to check out [the guide](GeneralGuides/relit.htm) on it.

## Contact Shadows

To improve gameplay shadows on character models go to `Devil May Cry 5` game folder:
 
* Open the file `dmc5config.ini`.
* Change the `ContactShadowSetting` value from `CUSTOM` to `ON`.
* Save your changes, right click on the file -> properties.
* Select the "Read only" box.

It should also be noted that forcing contact shadows on gameplay may result in some texture bugs e.g., the balloons in mission 2 may look weird, among other things.

## Tips and Tricks

In order to use ReShade, you'll need the game to boot in DX11. In your game's folder, open `dmc5config.ini` and change the following line:

```TargetPlatform=DirectX11```

## Useful links
* [Mod forum](https://infernalwarks.boards.net/)
* [Another mod forum ](https://residentevilmodding.boards.net/board/185/dmc-modification-releases)
* [Nexus mods](www.nexusmods.com/devilmaycry5/)
* [Helix mod](http://helixmod.blogspot.com/2019/03/devil-may-cry-5.html)
* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Devil_May_Cry_5)