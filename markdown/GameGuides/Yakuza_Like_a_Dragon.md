![Yakuza Like a Dragon](Images\yakuza_lad.png "Shot by ItsYFP"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (16:9)
DSR | Unknown
Custom Aspect Ratios | No
Reshade | Yes (DX11)
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [Yakuza Like a Dragon Free Cam by etra0](https://github.com/etra0/yakuza-freecam/releases)  
**Features**: Pause, Engine Speed Control, Free Camera, Tilt and FOV Control  
**Important**: Currently, you can ONLY use it with a Controller (no keyboard support!)

## Controls

Key | Action
--|--
R1 + R3 | Photo Mode Activation
Left/Right Arrow | Change Engine Speed
L2/R2 | Change FoV
L1/R1 | Tilt

Activating the camera disables the HUD.

## Tips and Tricks

### Reshade

Save yourself some trouble by deactivating the In-Game Depth of Field in Settings -> Graphic Settings -> Advanced Settings.

In Reshade edit the Global Preprocessor and set `RESHADE_DEPTH_INPUT_IS_REVERSED` to `1`.

@alert Important
**Reshade Depth Related Shaders**  
If you use the tools in cutscenes it is important to know, that by pressing E(or A on Controller) or clicking Left Mouse Button, 
you jump ahead in the cutscene conversation by default. You can not change this in the keyboard layout for the game. 

If you want to work with Reshade and being able to edit the current scene, tab out of the game, this way the game will pull up a pause screen, which you 
can't see because the tools also hide the HUD, but it is there. Tab back into the Game, by pressing ESC you will return to the 
game (leaving the Pause Screen). You have to set up any Depth Shader you want to use in the active Pause Screen, yet this way the 
Depth Buffer does not work.

It takes a bit more effort to set things up, but you'll get used to it.
@end

##Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Yakuza:_Like_a_Dragon)