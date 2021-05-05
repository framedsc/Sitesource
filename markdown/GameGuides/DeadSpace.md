![Game Title](Images\DeadSpace_header.png "Shot by K-Putt"){.shadowed} 

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes 
Ansel | No
DirectX versions | 9

## Tools

* [Modified Cheat Table of jim2point0](../CheatTables/deadspace_AoB.CT) - FOV, Camera, Char Size. Supports every game version by AoB scan.
* [Original Cheat Table by jim2point0](../CheatTables/Archive/deadspace.CT)

### Text Description

The following is based on [original description by jim2point0](https://web.archive.org/web/20141021190640/flickr.com/groups/deadendthrills/discuss/72157631765632995/).

FOV: Field of View.

Cam Distance: How far back the camera sits from character. The further you go, the smaller he is. This is what the "widescreen fixer" app modifies as well.

Cam Move Distance: Same as above, but for when you're walking. 

Cam Height: when the camera is level or pointing up, there is a minimum height the camera is allowed to go. By increasing\decreasing this, the camera will move up and down. HOWEVER, this does not apply when looking down. To change height when looking up and down, you'll need to use distance.

Center Offset 1\2\3: 3 values the game uses to determine how far left\right the camera sits from Isaac. However, it's dependent on where you're looking. No matter where you look, these will always move the camera left\right. To make matters simple, hotkeys are setup to change all 3 at the same time.

Pivot Distance: The camera rotates around a pivot point. By default, that point is located wherever Isaac is. However, if you increase this value, the camera will rotate around a point in front of Isaac. Negative values for behind him. This is one of several ways to simply put the camera in front of Isaac and get him out of the shot. Has other uses too.

Chacacter Size.

@alert important  
Aiming and many other in-game events reset camera values. To prevent value from changing, freeze it: open cheat table window, click in the box leftside of it's name. Or navigate with keyboard arrows and press Space. 
@end

@alert tip  
To keep favourite values for further use, organize them in dropdown: right click on entry, click on gear, fill value:name.   
Change the value manually by pressing Enter or double clicking on value.  
@end


### Controls

The controls aren't exactly intuitive, but you can customize them to your liking by pressing Ctrl+H.
Hotkeys function even if game window is minimized, use with care.

Key | Function
--|--
Numpad -/+ | camera distance
Numpad 4\6 | left\right offset
Numpad 8\2 | camera height
Numpad 9\3 | pivot offset
F5| reset defaults*

*this sets distance to a value of 4 instead of the game's normal default of 2.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Dead_Space)

* [SweetFX Settings DB / Dead Space 1](https://sfx.thelazy.net/games/game/304/)

* [Free Camera on RPCS3 Debug Build](https://www.youtube.com/watch?v=cHHJBT4CjE4) (video tutorial)