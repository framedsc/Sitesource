![Game Title](Images\assettoheader.png "Shot by tripps"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 10.1/11
 
## Essentials
* [Content Manager by Ilja Jusupov](https://acstuff.ru/app/)  
**Feature**: Custom launcher and content management app.
* [Custom Shaders Patch by Ilja Jusupov](https://acstuff.ru/patch/)  
**Features**: Graphical overhaul for the game, optimizations, dynamic lighting, Weather FX, etc.
* [Sol by Peter Boese](https://www.racedepartment.com/downloads/sol.24914/)  
**Features**: Full control over game weather, day and night cycle.

Note: CSP and Sol are meant to be used together.

## Tips and Tricks

### Photo Mode

The game has two free camera modes. F5 camera links the camera to the car, F7 camera is unlinked from the car. Both cameras have different controls.

Turn on the app in-game from right side GUI to be able to control FOV, DOF, aspect ratio, shutter speed, change time and sun angle, turn on/off lights, hide driver.

@alert important
Do not use Assetto's built-in camera mode, use CSP Photo Mode app.
@end

Screenshots must be taken in-game with Replay mode.

* Motion screenshots are not possible without Replay mode
* CSP graphic features do not work in AC Showroom

### Free camera controls

Action | F5 Camera | F7 Camera
--|--|--
Move Camera | W, A, S, D | Arrow Keys
Tilt Camera Left/Right | F, G | -
Tilt Camera Up/Down | B, V | -
Up/Down | Z, C | Page Up/Down
Speed | Shift/Tab | Ctrl/Shift
Focus Camera (focus on cursor) | Ctrl + Left Mouse / End Key | Ctrl + Left Mouse / End Key
Take Shot | F8 | F8

### Hotsampling

Possible with CSP Nice Screenshots extension. To enable set `Resolution Multiply` to a higher value under Accumulation AA in CSP Settings > Nice Screenshots extension.

@alert info
Checkerboarding effect visible with Resolution Multiply, any value over 2x will ruin your shot.
@end

### Nice Screenshots extension

In CSP Settings > Nice Screenshots, there is several things you can change on the fly while your game is open, and it will affect the game.
There is also 3 things that overlap each other, so here's what you want to do if you want to use Accumulation AA, Accumulation DOF and Accumulation motion blur:

In each effect, there's a "Iterations" setting, with different values
They all do the same effect: take multiple photos and stitch them together, to smooth the 3 effects (AA, DOF, motion blur)
Using all 3 of them at the highest values will either crash your game, or in the best case scenario, take 3 months to render.

@alert tip
You only need to have one "iteration" value active to have a good result, you can always just put "1" or deactivate the effect when you don't use it.
@end

* I want to take a static photo with no effects (no DOF or motion blur): AA iterations at 80 
* I want to take a photo with DOF and no motion blur: AA iterations at 1, DOF iterations at 1000 
* I want to take a photo with motion blur only: AA and DOF iterations at 1 (or deactivated), motion blur iterations at 400 
* I want to take a photo with everything: AA iterations at 1, either DOF or motion blur iterations at their normal value (1000 for DOF or 400 for motion blur), the other one will stay at 1

@alert info
You can use a lower iteration but you will end up with a worse quality DOF/AA/motion blur, try and see what you have, lower values will also take less time to render.
Play with the values, explore the settings and find out what can be useful for your shots, there is so much that can be done with the settings of Custom Shaders Patch!
@end

### Filter installation

Most Post Processing filters have support for drag & drop installation with Content Manager. For manual installation, go to your game's file directory and drag the files into:

`\assettocorsa\system\cfg\ppfilters`

Selecting filters is done from the CSP Photo Mode app or the separate Post Process Filter app.

### Game setup

From Content Manager in Assetto Corsa's System settings tick `Allow free camera`, untick `Orbit mode for F5 camera`, and select PNG in `Screenshots format`.

Note: For Sol and CSP installation use their provided guides.

@alert tip
It's highly recommended to have separate gameplay and screenshot setting presets for high FPS and high graphics. You can switch between both with a right click anywhere in Content Manager, a menu will appear with the settings you saved.
@end

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Assetto_Corsa)
* [Girellu Repository](https://github.com/archibaldmilton/Girellu)
* [How to use Assetto Corsa's hidden photo mode video](https://www.youtube.com/watch?v=FIitR0SCoxQ)