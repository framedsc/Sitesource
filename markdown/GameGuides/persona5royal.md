![Persona 5 Royal](Images\persona5royal_header.png "Shot by ofseaandstars"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes (with tools)*
Reshade | Yes (DX11)
Ansel | No
Graphics API | DirectX 11
Game Version | 1.03B <font face="Stores"> S </font>

\* *Custom Aspect Ratios can be set in the mod menu, but may not rescale the image correctly.*

## Tools

- [Persona5ScriptHook](https://github.com/Zolika1351/Persona5ScriptHook/releases/)
- [ZMenu](https://zolika1351.pages.dev/mods/persona5menu)

@alert warning
Development on the mod menu has finished according to the author; as such, the guide may become outdated following a game update. If so, as an alternative, you can roll back to a previous version of the game following [this guide](../GeneralGuides/steam_update_guide.htm).
@end
## Requirements for Depth Buffer support

@alert important
The game writes HUD and menu data to the depth buffer. 

Disabling the HUD is **required** for the depth buffer to work. See [Scripts Functions](#script-functions) section for how to disable the HUD.
@end

For depth buffer support, set the following pre-processor definitions:

- `RESHADE_DEPTH_LINEARIZATION_FAR_PLANE` to `100.0`
- `RESHADE_DEPTH_INPUT_IS_UPSIDE_DOWN` to `0`
- `RESHADE_DEPTH_INPUT_IS_REVERSED` to `0`
- `RESHADE_DEPTH_INPUT_IS_LOGARITHMIC` to `1`

Select the following options for the 'Generic Depth' add-on:
- `Copy before clears` to `1`.

## Mod Menu - Navigation

Bindings can be adjusted in the `ZMenuP5R.ini` file in the root directory of the game.

### Default Bindings

Key | Description | KeyCode
--|--|--
Numpad 8 | Menu Up | 104
Numpad 2 | Menu Down | 98
Numpad 4 | Menu Left | 100
Numpad 6 | Menu Right | 102
Numpad 5 | Menu Enter | 101
Numpad 0 | Menu Back | 96
F7 | Menu Toggle | 118

### Recommended Bindings

Especially helpful for those without a numpad. 

Key | Description | KeyCode
--|--|--
Up Arrow | Menu Up | 38
Down Arrow | Menu Down | 40
Left Arrow | Menu Left | 37
Right Arrow | Menu Right | 39
Enter | Menu Enter | 13
Backspace | Menu Back | 8
F7 | Menu Toggle | 118

## Mod Menu - Free Camera

1. Navigate to `Options > Game Tweaks` and ensure that `Disable Keyboard Input` and `Disable Mouse Input` are enabled.
2. Navigate to `Options > Camera Options > Custom Cameras > Freecam` and set `Enabled` to `On`.
3. Set `Custom Mouse Rotation` to `On`.
4. Move camera with `WASD` and the mouse.

## Script Functions

To change these values, you'll need to open the mod menu (Default: `F7`) and navigate to `Experimental > Script Functions`. 

Select `Search` and type in `DISP`. Select `Search` from that menu and hit `Enter` and you should see a selection of functions. 

Once you've done so, select one of the functions from the table below. Go back to the previous menu (`Experimental > Scription Functions`) and you'll be prompted with some parameters that can be edited by pressing left or right on the values that say `<0>`.

Simply change the values based on the guides below and then select `Execute` to trigger them.

Function | Description | Parameters | Notes
--|--|--|--
`DATE_DISP` | Toggles the date/time indicator in top-left of HUD. | `P1`: `0` is hidden, `1` is shown. | **Must be hidden for depth buffer to work correctly.**
`FLD_PANEL_DISP` | Toggles the main controls HUD/Minimap etc. | `P1`: `0` is hidden, `1` is shown. | **Must be hidden for depth buffer to work correctly.**
`FLD_NPC_UNDISP` | Toggles NPC visibility. | `P1`: Leave at `0`. `P2`: `0` is hidden, `1` is shown. | *Optional.*
`FLD_NPC_TALKICON_FORCEDISP_FBNID` | Toggles the NPC 'chat' bubble icons above their heads. | `P1`: Leave at `0`. `P2`: `0` is hidden, `1` is shown. | *Optional.*

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Persona_5_Royal)
