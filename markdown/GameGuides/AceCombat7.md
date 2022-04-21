![Ace Combat 7](Images\ac7header.png "Shot by Ghostinthecamera"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes - See Tips
Custom Aspect Ratios | Yes (with tools)
Reshade | Yes
Ansel | No
Graphics API | DirectX 11

## Tips

@alert tip
**Using DSR**  
The game is quite picky whether it will detect DSR resolutions. If you have a 2560x1440 monitor, for example, and have a DSR resolution of 3840x2160 most games will detect this and allow you to select it in their options. As of the current patch AC7 won't detect this. Set your desktop resolution to the DSR resolution before starting the game and make sure you select full screen as the display type. DSR resolutions should display now.
@end

@alert tip
**Using DSR with borderless window**  
Follow the above instructions to get the game to recognise DSR resolutions. Set the resolution in full screen mode and then change to borderless. The selected resolution should remain as long as it is the same as the desktop DSR resolution.
@end
 
## Tools

* [Camera Tools by ghostinthecamera](https://github.com/ghostinthecamera/IGCS-GITC)  
**Features**: Camera control, FOV Control, Time Stop, Resolution Scaling, HUD Toggle, Time Skip.

@alert important
**HUD Toggle**  
As of v1.1 there is HUD toggle in the tools. However, if the HUD toggle is used after the game is paused, not all HUD elements may be removed. To prevent this, by default, the game will turn the HUD off when you press the game pause key. In order to do this, a small delay of 300ms is introduced to allow all HUD elements to be removed before the game is actually paused. 

This may make action shots a little more difficult due to the delay between pressing the game pause key and the game actually pausing. If you need the game pause to have no delay you have a couple of options:

1. Change the default behaviour of the game pause so that it does not toggle the HUD. You can find this in Misc options in the overlay. It is activated by default. You will then have to ensure the HUD is disabled manually prior to pausing the game.  

2. Use the 3dmigoto HUD toggle included in the package.

You can have the 3dmigoto HUD toggle installed and use the tools built in HUD toggle. They do not prevent each others functioning.
@end

## Useful links

* [PC Gaming Wiki](https://acecombat.fandom.com/wiki/Ace_Combat_7:_Skies_Unknown)