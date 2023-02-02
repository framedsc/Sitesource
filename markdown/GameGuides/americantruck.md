![American Truck Simulator](Images\americantruck.png "Shot by tripps"){.shadowed .autosize}

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
Game version | 1.46

@alert neutral
Everything in this guide applies to *Euro Truck Simulator 2* as well!
@end
 
## Tools

* [Photo Mode Unlock by tripps](https://mega.nz/file/cAMQwSxR#CJGqIOVh3BoJE7dzSU9Vpft6RWwFji8ElBOUK4O82bg)  
**Features**: Unlocks camera distance limitations, increases FOV distance, removes viewfinder overlay (included HUD toggle version)

## Photo Mode

The game has a built-in photo mode which also allows you to change the weather, time, FOV, DOF.

Key | Command
--|--|
W, A, S, D | Move Camera
Q, E | Up/Down
Z, C | Roll Camera Left/Right 
Scroll Wheel | Change FOV
Space | Photo Settings
H | Hide HUD
R | Reset Camera 
M | Gallery

@alert important
The Photo Mode export does not render Reshade shaders, use Reshade's built-in screenshot feature.
@end

## Tips and Tricks

@alert tip
It is highly recommended for **NVIDIA** graphics card users to not use the in-game AA, but setup NVIDIA's AA using the guide below in [Useful Links](#useful-links). *This does not work for AMD card users.*
@end

### Console commands

To enable the developer console, go to: `\Documents\American Truck Simulator`, open "config.cfg" and change these values: `uset g_developer "1"` and `uset g_console "1"`

Command | Arguments | Description
-- | -- | --
`g_bloom` | `<value>` | Changes the bloom amount. (set to 0 and forget about it)
`g_set_time` | `<hours> <minutes>` | Changes in-game time.
`g_set_weather` | `1` / `2` | `1` for rain, `2` for clear weather.
`g_set_skybox` | `1` - `6` | Changes the skybox.
`g_traffic` | `0` - `1` | Disables or enables AI traffic.
`goto` | `x;y;z` or `<city_name>` | Enables free camera and teleports it to the specified location.
`warp` | `<speed>` | Changes the simulation speed of the game.
`g_show_game_elements` | `0` - `1` | Disables or enables in-game elements like the gas station/repair icons and such.
`g_minicon` | `0` - `1` | Turns on in-game mini console.

### Reshade

Note that the game uses an upside-down depth buffer. You will need to go to the global processor definitions and change `RESHADE_DEPTH_INPUT_IS_UPSIDE_DOWN` from 0 to 1. This is essential and otherwise depth shaders will not work properly.

@alert info
Your game may need to have the depth buffer picked manually for depth shaders to work properly, this is done in the D3D11 (ReShade 4.0 and below) / Add-ons (ReShade 5+) tab. This has to be done everytime the resolution is changed.
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/American_Truck_Simulator)
* [Nvidia Profile Inspector AA setup guide](https://roextended.ro/forum/viewtopic.php?t=1000)
