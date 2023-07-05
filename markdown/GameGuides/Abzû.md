![Abzû](Images\abzû_header.png "Shot by SammirLlm"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (see notes)
DSR | No
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 11

@alert neutral  
This guide is for an Unreal Engine 4 game that can use the [Universal Unreal Unlocker](https://framedsc.com/GeneralGuides/universal_ue4_consoleunlocker.htm).  
@end

## Tools

* [Cheat Table by Skall](..\CheatTables\AbzuGame-Win64-Shipping_Skall.CT)  
    **Features**: Camera control, FoV control.
    
    @alert tip
    This Cheat Table allows you to toggle freecam without pausing the game. You can thus take long exposure shots with this tool
    @end

    Function | Key
    --|--
    Camera Movement (X axis) | Num 4 / Num 6
    Camera Movement (Y axis) | Num 7 / Num 9
    Camera Movement (Z axis) | Num 5 / Num 8
    Pitch | Up Arrow / Down Arrow
    Yaw | Left Arrow / Right Arrow
    Roll | Num 1 / Num 2
    Field of View | Num - / Num +

* [Cheat Table by pvp](..\CheatTables\AbzuGame-Win64-Shipping.CT)  
    **Features**: Camera control, FoV control, Hide Menu.

    @alert tip
    For Timestop, pause the game (`ESC`) and hide the menu using the HUD toggle inside the table.
    @end

    Function | Key
    --|--
    Camera movement | Num 9/8/7/6/5/4
    Pitch and Yaw controls | Arrow keys
    Increase/decrease FoV | Num +/-
    Camera Rotation | PageUp and PageDown

## Pause Game and Hide Hud

You may also use the Shader Toggler Addon for Reshade to toggle the shaders the draw the HUD Elements. This way, you can pause the game by pressing `ESC` and toggle off the shader group to hide the HUD. You may find the ShaderToggler.ini file of the game in this [repository](../ReshadeGuides/Addons/shader_toggler_repository.md).

## Hotsampling

Hotsampling works with the game, however there is an issue where alt-tabbing back to the game after hotsampling will reset it to its previous resolution. A workaround is to use MSI Afterburner / RTSS, which can capture the game without needing to alt-tab back.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Abz%C3%BB)