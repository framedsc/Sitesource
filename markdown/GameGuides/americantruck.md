![American Truck Simulator](Images\americantruck.png "Shot by tripps"){.shadowed .autosize}

* Note that everything in this guide applies to Euro Truck Simulator 2 aswell.

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (DX11)
Ansel | No
Graphics API | DirectX 11
Game version | 1.45
 
## Tools

* [Photo Mode Unlock by tripps](https://mega.nz/file/wNU0CbCb#UyrcytyubnV69z4FNCM93R8mVwKZXtl4OC-vmfVxJmQ)  
**Features**: Unlocks camera distance limitations, increases FOV distance, removes viewfinder overlay

## Photo Mode

The game has a built-in photo mode which also allows you to change the weather, time, FOV, DOF.

Key | Command
--|--|
W, A, S, D | Move Camera
Q, E | Up/Down
Z, C | Tilt Camera Left/Right 
Scroll Wheel | Change FOV
R | Reset Camera 
L | Lights Menu

@alert important
The Photo Mode export does not render Reshade shaders, use Reshade's built-in screenshot feature.
@end

## Tips and Tricks

@alert tip
It is highly recommended for **NVIDIA** graphics card users to not use the in-game AA, but setup NVIDIA's AA using the guide below in Useful Links. `This does not work for AMD card users`
@end

### Developer Console

To enable the developer console, go to: `\Documents\American Truck Simulator`, open "config.cfg" and change these values: `uset g_developer "1"` and `uset g_console "1"`

Useful commands
Command + Parameters | Effects
--|--|
g_bloom 'value' | Changes the bloom amount (Set it to 0 and forget about it).
g_set_time 'hour' | Changes/advances the game time.
g_set_weather 'weather' | Changes the game weather.
g_set_skybox 'id' | Changes the skybox (only 1-6).
g_traffic '0 or 1' | Disables or enables AI traffic.
goto 'x;y;z' or 'city name' | Enables free camera and teleports your camera to the specified location.
warp 'speed' | Changes the simulation speed of the game.
g_show_game_elements '0 or 1' | Disables or enables in-game elements like the gas station/repair icons and such.
g_minicon '0 or 1' | Turns on in-game mini console.


### Reshade

Note that the game uses an upside-down depth buffer. You will need to go to the global processor definitions and change `RESHADE_DEPTH_INPUT_IS_UPSIDE_DOWN` from 0 to 1. This is essential and otherwise depth shaders will not work properly.

@alert info
Your game may need to have the depth buffer set manually for depth shaders to work properly, it is done in Reshade's D3D11 tab (This has to be done everytime the resolution is changed).
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/American_Truck_Simulator)
* [Nvidia Profile Inspector AA setup guide](https://roextended.ro/forum/viewtopic.php?t=1000)