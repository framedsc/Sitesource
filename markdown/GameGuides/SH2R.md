![Silent Hill 2 Remake](Images\SH2R.png "Shot by Iron Gauntlet"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (see notes)
DSR | Yes
Custom Aspect Ratios | Yes (see notes)
Reshade | Yes
Ansel | No
Graphics API | DirectX 11/12 (see notes)
Game version | 1.04

@alert neutral  
This guide is for an Unreal Engine 5 game that can use the [Universal Unreal Unlocker](https://opm.fransbouma.com/uuuv5.htm).  
@end

## Tools

* [Silent Hill 2 Remake Widescreen fix](https://github.com/RoseTheFlower/UltrawideIndex/releases/tag/silenthill2remake)  
**Features**: Fixes Hotsampling/Custom ARs (removes black bars with vertical ARs/cutscenes)

## UUUv5 cleaner preset

The following is a post-process effects toggle for the game using UUUv5 preset system. It gets rid of the DOF, CA, vignette, lens flares, and film grain. To use it, create a text file called `cleaner.preset` inside the `PostProcessPresets` folder in your UUU exe folder. Then, paste the following code block inside the file:

```
[General]
Name=cleaner
[Setting values]
24=2|0.00
31=2|0.00
40=2|0.00
47=2|0.00
60=2|0.00
97=2|0.00
104=2|0.00
```

You may need to restart UUU for it to read the new preset file.

## Tips and Tricks

### Removing artificial lighting on characters

To remove the artificial lighting on James/Maria, simply bring the freecam a few meters away from the characters and pause/unpause once.

### Taking shots in cutscenes

To shoot cutscenes, follow the given workflow:

1. Use the game pause (`Esc` by default).  
2. Hide the pause menu with the tool's HUD toggle (`Del` by default) then toggle the UUU cam.

### Using the correct DirectX version

The game will not launch properly on older cards/cards with less VRAM (like 1050ti/1650) by default. To fix this, add `~dx11` as a startup command in Steam's Game Properties section. This will also remove FSR3/Framegen toggles from the ingame options, only FSR1 is available for use with DX11.

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Silent_Hill_2)
