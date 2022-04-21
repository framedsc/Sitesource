![Limbo](Images\limbo_header.png "Shot by cHota gAbbar"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes (through Desktop)
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 9

## Workflow

By default, the game starts in fullscreen mode and uses a `1280x720` rendering resolution. It is however possible to force the game to render at higher resolutions but they may not look as crisp, since the game 'intentionally uses blurring and other image filtering methods combined with assets made for `720p` resolution'.

To do this (and many other things), you will need to modify the configuration file, i.e, `settings.txt` inside the game's root directory.

@alert tip
You may want to make a backup of this file before you start tweaking.
@end

### Entries to modify:-

* `backbufferheight`: By default, this is set to `720`. Change this value to force the game to render at resolutions greater than `720p`.

@alert Info
The game will cap out at your desktop resolution irrespective of how high a value you enter here. For example, if your desktop resolution is `1080p`, and you change the `backbufferheight` to `2160`, the game still will render at `1080p`.

You have to enable DSR and change your desktop resolution to `2160p`; only then will the game render at that resolution with `backbufferheight` set to `2160`.
@end

* `windowedmode`: By default, this is set to `false`. Changing this to `true` is necessary to be able to hotsample using SRWE. If you want to run the game in Borderless Windowed mode, you will have to use Special K and follow the guide [here](https://www.pcgamingwiki.com/wiki/Limbo#Borderless_fullscreen_windowed)

## Useful links

* [PC Gaming wiki](https://www.pcgamingwiki.com/wiki/Limbo)