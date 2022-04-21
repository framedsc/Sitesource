![Bulletstorm: Full Clip Edition](Images/bulletstorm.png "Shot by Originalnicodr"){.shadowed .autosize}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes
Ansel | Yes
Graphics API | DirectX 11
 
## Tools
 
* [Camera tools by Otis_Inf](https://www.patreon.com/Otis_Inf)  
**Features**: Freecam and FoV control

## Usage

Run the game, start IGCSInjector.exe, both as administrator. You should get a console window with the text above. It'll report errors if it runs into it. Start the injector slightly later than the game so hooking into the XInput (for controller blocking) is picked up.

Before using the cam tools make sure to do the ini edits explained below.

## Ini edits
The tools does not provide a timestop. The closer we have to one would be the "Players only" unreal engine command that freeze enemies and npcs. To create a binding for it go to `My Documents\My Games\Bulletstorm Full Clip Edition\StormGame\Config\StormInput.ini` and add the following lines below `[StormGame.BSPlayerInput]`:

```
[StormGame.BSPlayerInput]
Bindings=(Name="Delete",Command="set Engine.WorldInfo bPlayersOnly true",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="Delete",Command="set Engine.WorldInfo bPlayersOnly false",Control=False,Shift=False,Alt=True,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
```

Even tho the game lacks hotsampling we can use the setres UE3 command to easily change between DSR resolutions with a press of a button. All you need to do is add these lines to the same file you edited above:

```
Bindings=(Name="F5",Command="setres 3840x2160",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="F6",Command="setres 1920x1080",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="F7",Command="setres 5760x3240",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
```

With those lines you can change to 4K by pressing F5, 1080 with F6 and 3k? with F7. Feel free to change those lineas with whatever resolution you want to use (and whatever button).

You can also modify the `StormSystemSettings.ini` file to push graphics, but this being a remake for new generation consoles most stuff are already maxed out. For reference to what to edit check other UE3 game guides or look up [in here](https://web.archive.org/web/20180101115845/http://deadendthrills.com/forum/discussion/248/ue3-engine-tweak-questions).

## Controls

Description | Keyboard Key - Joystick
--|--
Enable/Disable freecamera | Insert
Lock/unlock camera movement | Home
Timestop (Players only) | Delete
Continue | Alt + Delete 
Rotate camera up/down | Arrow up/down or mouse - Right stick     
Rotate camera left/right | Arrow left/right or mouse - Right stick
Move camera forward/backward | Numpad 8/Numpad 5 - Left stick          
Move camera left/right | Numpad 4/Numpad 6 - Left stick          
Move camera up/down | Numpad 7/Numpad 9 - Left/Right trigger      
Tilt camera left/right | Numpad 1/Numpad 3 - D-pad left/right
Increase/decrease FoV (w/ freecam) | Numpad `+`/`-` - D-pad up/down           
Reset FoV (w/ freecam) | Numpad `*` - B-button
Toggle Y look direction (for when the world coordinates change) | Numpad `/`
Toggle input to game | Numpad `.` - Right Bumper   
Faster rotate/move | Alt + rotate/move - Y-button + left/right-stick 
Slower rotate/move | Right-Ctrl + rotate/move - X-button + left/right-stick      

The camera, when enabled, disables bloom/dof. You should re-add these through reshade if you want them back. This is done to get rid of the near plane blur for the weapon and the atrocious bloom is ruining every shot.

In some levels (the ones on the city) the world is weirdly positioned so when trying to move the camera's orientation in those the controls would be unintuitive, so pointing upwards would point the camera down and vise versa for example. When that happens press the `/` key to invert the Y axis.


## Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Bulletstorm:_Full_Clip_Edition)