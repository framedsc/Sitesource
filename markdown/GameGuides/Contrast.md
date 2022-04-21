![Contrast](Images\contrast.png "Shot by Antic Owl"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 9
 
## Tools

Go to `C:\Users\<Username>\Documents\My Games\Contrast\ContrastGame\Config\`
Edit the file called `ContrastInput.ini` and add the following lines at the end of the `[Engine.PlayerInput]` section.
Save the file.

```
Bindings=(Name="Divide",Command="ToggleHUD")
Bindings=(Name="Add",Command="Pause")
Bindings=(Name="Subtract",Command="PlayersOnly")
Bindings=(Name="Home",Command="Toggledebugcamera")
Bindings=(Name="F2",Command="show camfrustums")
Bindings=(Name="Decimal",Command="Ghost")
Bindings=(Name="Decimal",Command="Walk",Control=False,Shift=False,Alt=True)
Bindings=(Name="NumPadOne",Command="FOV 10",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadTwo",Command="FOV 20",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadThree",Command="FOV 30",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadFour",Command="FOV 40",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadFive",Command="FOV 50",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadSix",Command="FOV 60",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadSeven",Command="FOV 70",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadEight",Command="FOV 75",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="NumPadNine",Command="FOV 0",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
```


## Controls

### Free Cam controls (keyboard and mouse / joystcik)

Key | Action
--|--
Substract (-) | Freeze everything but the player
Add (+) | Pause Game
Divide (/) | Toggle HUD
Home | Toggle the Debug Camera
F2| Toggle camfrustums
Numpad 1 - 9 | Change FOV (default FOV - Numpad 9)
Decimal (.) | Enable Noclip
Alt+Decimal (Alt+.) | Disable Noclip


@alert important
To hide the camfrustums (in-game camera lines), you need to press F2 before pausing the game and/or activating the camera.
@end

@alert important
The FOV needs to be changed before pausing the game and/or activating the camera.
@end

@alert important
To exit the debug camera, you need to press RS twice.
@end

### NOTES
To disable the in-game DoF, change `DepthOfField=True` to `False` in `ContrastEngine.ini`.
It is located in the same folder as `ContrastInput.ini`.
Camera rotation is not available in debug camera.
Heavily modifying the `ContrastEngine.ini` could lead to crash when playing

## Reshade

If using DSR the correct depth buffer needs to be selected.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Contrast)
