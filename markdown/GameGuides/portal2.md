![Portal 2](Images\portal2_header.png "Shot by EchoSmoker"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes¹
Custom Aspect Ratios | Yes²
Reshade | Yes
Ansel | No
DirectX versions | DirectX 9, Vulkan

*¹ - Changing resolutions too often can cause a game hang, recommended to play at your shooting resolution  
² - Aspect Ratio might have to be tweaked to see all your custom resolutions*

## Console commands

Since Valve games allow access to the console, no tools are needed.  
Going to the Options menu > Keyboard/Mouse, enable Allow Developer Console. You can now open the console with the `/~ key.  

Command | Arguments | Description
-- | -- | --
`sv_cheats` | `0` / `1` | enables cheats (needed for most of these)
`cl_drawhud` | `0` / `1` | hides HUD
`noclip` | `0` / `1` | toggles noclip (freecam)
`r_drawviewmodel` | `0` / `1` | toggles viewmodel (portal gun visibility)¹
`host_timescale` | - | controls gamespeed (multiplier)
`mat_postprocess_enable` | `0` / `1` | toggles post-processing (bloom, sharpening, LUTs)
`mat_fastspecular` | `0` / `1` | toggles quality of specular highlights, set to 0 for better quality
`r_waterforcereflectentities` | `0` / `1` | force water to reflect everything
`fog_override` | `0` / `1` | override the default fog settings (required for the fog commands below)
`fog_enable` | `0` / `1` | toggles fog in the level
`fog_skyboxenable` | `0` / `1` | toggles fog in the skybox
`cl_fov` | `value` | change FoV
`r_portal_use_dlights` | `0`/`1` | toggles a dynamic lighting effect around portals
`portal_draw_ghosting` | `0`/`1` | toggles portal outlines that are visible through walls 
`map` | [ID list](https://theportalwiki.com/wiki/List_of_Portal_2_chambers#List_of_map_names_.28in_alphabetical_order.29) | change levels
`thirdperson` | - | enable third person camera²
`thirdperson_mayamode` | - | enables rotational camera around the player model (hold alt + click - move the camera, left click - rotate camera, right click - zoom camera)
`firstperson` | - | enable first person camera (the default)

*¹ - Hiding the viewmodel also hides any object the portal gun is holding   
² - Enable `thirdperson` before using `thirdperson_mayamode`, use `firstperson` to reset*

## Tips and Tricks

### Binding commands & autoexec.cfg

The above commands can be bound to hotkeys with the use of `bind <key> <command>` / `bindToggle <key> <command>` (latter is best for 0 / 1 commands) so the console doesn't have to be opened all the time. 

These `bind` commands can be written to an `autoexec.cfg` file created in `~\Portal 2\portal2\cfg` folder. [This guide](https://steamcommunity.com/sharedfiles/filedetails/?id=381795162) goes into more detail regarding console commands and `autoexec.cfg`. While it is focused on L4D2, a lot of the same principles apply since they share the same engine.

### Notes

MSAA needs to be disabled in the video settings for the depth buffer to work. Use ReShade AA methods and DSR.

Environments seen through portals are not detected by the depth buffer.

Chell will look in the direction she shot portals.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Portal_2)
* [List of all commands](https://developer.valvesoftware.com/wiki/List_of_Portal_2_console_commands_and_variables)