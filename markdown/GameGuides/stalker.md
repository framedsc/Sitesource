<!--![S.T.A.L.K.E.R - Call of Pripyat](Images\game_header.png "Shot by Author"){.shadowed}-->

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes (via WBG and Console Commands)
DSR | Yes
Custom Aspect Ratios | Yes (with Hotsampling)
Reshade | Yes (DX10/11)
Ansel | No
DirectX versions | DirectX 11 (i think)
 
## Tools

### Console

#### Setting up key bindings
Setting up the external cameras and first person camera binds with the following commands

* press `~` to open the console
* type in: 
```
bind cam_1 kF1
bind cam_2 kF2
bind cam_3 kF3
```

#### FOV Control

* [For Call of Pripyat](http://www.moddb.com/mods/console-controlled-fov)  
Type in `fov` followed by a number, like `80` to change the FOV on the fly. Example: `fov 80`
* [For Shadow of Chernobyl](https://community.pcgamingwiki.com/files/file/503-stalker-shadow-of-chernobyl-unofficial-patch-10008/)

#### Hud Toggle

For SoC: `hud_info on/off` or NumPad +/-  
For CoP: `hud_draw 0/1`  

`hud_crosshair 0/1` for both to toggle the crosshair.

#### How to use custom resolutions with the console

To do so run the game in the windowed mode which can be either done via switching in the menu or you type the following line into the console:

`rs_fullscreen 0` and apply the change with the commands `vid_restart`

For custom resolutions:
Setting up the scene in lower resolutions via the following command

`vid_mode [width]x[height]`. For example: `vid_mode 1920x810` for 21:9.
Type in `vid_restart` to apply the resolution

Set up your scene and to the same with a higher resolution. 
For example: `vid_mode 5120x2160`
confirm the resolution with `vid_restart`

#### Enter the Free-Camera

Type `demo_record x` [or whatever you want] in the console AFTER entering one of the prior bound cameras.
This will allow you to fly around.

Controls:
Forward/backward: with Mouse B1/2
Up/Down: W/S
Left/Right: S/D
Tilt: Num7/Num8

## Tips and Tricks

### Hide the weapon

Use the free rotatable external camera for the capture as your playermodel won't be in the way then.
+ this allows you to set up shots with your character.
Should be the camera bind to F3

##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/S.T.A.L.K.E.R.:_Call_of_Pripyat)