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
Game version | </font> <font face="Stores"> E </font> 4.12.5


## Tools

* [Cheat Table by Skall](..\CheatTables\AbzuGame-Win64-Shipping_Skall.CT)  
    **Features**: Camera control, FoV control.

    @alert tip
    If you want to take a stillshot, pause the game by pressing the `ESC` key and hide the HUD using the ShaderToggler as described below. Then press `INS` to enable freecam.
    @end
    
    @alert tip
    This Cheat Table allows you to toggle freecam without pausing the game. You can thus take long exposure shots with this tool.
    @end

    Function | Key
    --|--
    Toggle Freecam | Insert
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
    Pause the game (`ESC`) and hide the menu using the HUD toggle inside the table or the ShaderToggler as described below. Then take the shot.
    @end

    Function | Key
    --|--
    Camera movement | Num 9/8/7/6/5/4
    Pitch and Yaw controls | Arrow keys
    Increase/decrease FoV | Num +/-
    Camera Rotation | PageUp and PageDown

## Hide Hud

You may use the Shader Toggler Addon for Reshade to toggle the shaders the draw the HUD Elements. You may find the ShaderToggler.ini file of the game [here](../ShaderTogglers/abzû.ini) or in this [repository](../ReshadeGuides/Addons/shader_toggler_repository.md). Press the `Caps Lock` to hide/unhide the HUD.

## Hotsampling

Hotsampling works with the game, however there is an issue where alt-tabbing back to the game after hotsampling will reset it to its previous resolution. A workaround is to use MSI Afterburner / RTSS, which can capture the game without needing to alt-tab back.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Abz%C3%BB)