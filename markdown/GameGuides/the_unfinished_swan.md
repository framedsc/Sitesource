![Inside](Images\unfinished_swan_header.png "Shot by cHota gAbbar"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes (through Desktop)
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
Game version | </font> <font face="Stores"> S </font> 1.0.0.1

## Workflow

You need to use [ShaderToggler](https://github.com/FransBouma/ShaderToggler) addon for Reshade to hide the UI elements. The UI elements that may be on your screen at a time are:-

  1. Dot crosshair in the center of the screen.
  2. Balloon Radar at the bottom left of the screen (provided you have unlocked the Toy).

The game uses a handful of vertex and pixel shaders. Create a ShaderGroup and add the two pixel shaders corresponding to the aforementioned two UI elements. Toggle them off and take the shot.

@alert info
The game uses MSAA and thus has no depth-buffer access.
@end

## Notes

The in-game resolution settings caps out at your desktop resolution. If you want to play at higher resolutions (like 4K), set your desktop resolution to the corresponding value; only then the in-game settings show the higher resolutions.

## Useful links

* [PC Gaming wiki](https://www.pcgamingwiki.com/wiki/The_Unfinished_Swan)