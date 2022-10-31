![Monster Hunter Rise](Images\mhrise.png "Shot by Originalnicodr"){.shadowed .autosize}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | No
Custom Aspect Ratios | Yes*
Reshade | Yes*
Ansel | No
Graphics API | DirectX 12
 
## Tools
 
* [REFramework (script and plugin loader among other things)](https://github.com/praydog/REFramework)  
**Features**: Freecam and Time scale (pause)
* [FoV editor](https://www.nexusmods.com/monsterhunterrise/mods/84)  
**Features**: FoV control
* [aspect_ratio_fit and resolution_scale](https://www.nexusmods.com/monsterhunterrise/mods/40)  
**Features**: Custome AR and resolution scale (for cutscenes).
* [RELit by Originalnicodr and Otis_inf](https://github.com/originalnicodr/RELit)  
**Features**: Lighting Control, turn off scene lights, exposure control.  
Make sure to check out [the guide](../GeneralGuides/relit.htm) on it.

## Installation
First, install REFramework by dropping its files into the game folder. Then, to install the other mods drop their files into the new `reframework\autorun` folder.

Below I will leave you my settings. These are not necessary but you can copy and paste them into your `re2_fw_config.txt` file (created automatically when running the game with REFramework for the first time):

```
FreeCam_DisableMoveKey=-1
FreeCam_DisableMovement=false
FreeCam_Enabled=false
FreeCam_LockKey=-1
FreeCam_LockPosition=false
FreeCam_MoveDownKey=29
FreeCam_MoveUpKey=57
FreeCam_RotationSpeed=0.017000
FreeCam_Speed=0.100000
FreeCam_SpeedModifier=4.000000
FreeCam_SpeedModifierFast=42
FreeCam_SpeedModifierSlow=56
FreeCam_ToggleKey=211
Scene_TimeScale=0.000001
Scene_TimeScaleContinuousKey=-1
Scene_TimeScaleEnabled=false
Scene_TimeScaleToggleKey=199
```

## Custom Aspect Ratios

The game doesn't support custom aspect ratios out of the box, so you will need to use the plugin linked above.

## HUD toggle
To turn off the HUD you will need to execute the following script. Create a .txt file, put code in the code-block below on it, save it and change the file extension to `.lua`. Then in the game, open the REFramework menu, click on `Run script` and select the file you created.

Turn off HUD
```
re.on_pre_gui_draw_element(function(element, context)
    return false
end)
```

To turn the HUD on again click the button that says `Reset scripts`. Take in mind this will unpause the game and reset the fov.

## Time Scale
Using a time scale of 0 would totally freeze the time in the game, but it won't allow you to move the camera around. So instead select a value of `0.001`. You can however edit the `re2_fw_config.txt` file and put the value `0.000001` manually. If you used my file from above you already have it done for you.

## Controls

Take in mind these are the controls if you copied my `re2_fw_config.txt` values from above. You can of course change some of these keys in the REFramework menu.

Description | Keyboard and Mouse / Joystick
--|--
REFramework menu | Ins
Toggle Freecam | Del
Toggle Timestop | Home
Point camera | Mouse / Right stick
Move camera forward, backward, left and right | W, S, A, D / Left stick
Move the camera upwards | Space
Move the camera downwards | Ctrl

To edit the FoV open the REFramework menu, go at the bottom, and open the "Djevv's FoV" menu. Edit it from there.

## Reshade
At the time of writing the last version of reshade, 5.0.2 (addon version) crashes the game, so stick with 4.9.2 for now.

## Tips
- REFramework for some reason isn't blocking game inputs when interacting with its menu.
- If you change to a vertical AR the FOV value will change, so change the fov after deciding on an aspect ratio.
- If the game happens to crash while hotsampling and running it back again takes a long time (or just never gets to the title screen), deleting your `re2_fw_config.txt` seems to make it work again.
- The FoV editor doesnt work in cutscenes.
- The black bars when using custom aspect ratios in cutscenes can be taken out by turning the hud off.

## Useful Links

* [Disabling color gradig LUT](https://www.nexusmods.com/monsterhunterrise/mods/31)
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Bulletstorm:_Full_Clip_Edition)
