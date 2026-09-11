![Tom Clancy's Splinter Cell Blacklist](Images\SplinterCellBlacklist_header.png "Shot by One3rd"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes 
Custom Aspect Ratios | No 
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
 
## Tools
* [CE table by One3rd](..\CheatTables\Blacklist_DX11_v2.CT)  
**Features**: Camera control, FoV, Money cheat
* [HUD Toggle by One3rd](https://mega.nz/file/SNhWSCAL#f-DBWlBYhOChj2j36vF0J4QvXlBKOo6OG3AbyaIjT90)  
**Features**: Toggles main menu and game HUD, toggles cutscene DOF

## CE Table Notes
The table will only work with the game running in DX11 mode.  
Once the cheat table is loaded, enable the "Attach to game process" script or manually attach to "Blacklist_DX11_game.exe" process.

## Camera Control Notes

Key	| Command
--|--
`Num 0` | Toggle camera
`Num 8` / `Num 5` | Move camera forward / backward
`Num 4` / `Num 6` | Move camera left / right
`Num 7` / `Num 9` | Move camera up / down
`Num 8` / `Num 5` + `Num +` | Rotate camera up / down
`Num 4` / `Num 6` + `Num +` | Rotate camera left / right
`Num 1` / `Num 3` + `Num +` | Tilt camera left / right
`Num 2` + `Num +` | Reset Tilt
`Num 0` + `Num +` | Set Tilt to 90 degrees
`Num 7` / `Num 9` + `Num +` | Increase / decrease FoV
`Num *` | Reset FoV
Hold `CTRL` | Move the camera position and orientation faster
Hold `ALT` | Move the camera position and orientation slower

## Timestop
Timestop is accomplished by pressing ESC to enter the Main Menu which pauses the game. The HUD toggle is then used to remove the Main Menu HUD. 

## Cheats
Enable Money Script then go into upgrades menu to grab money pointer.

Key	| Command
--|--
`PgUp` | enables money script

Manually set Money value for loads of murder toy buying dosh (or pacifist toys if that's your thing).

## Hotsampling and Depth Buffer Notes
Game can hotsample using SRWE but it must be in windowed mode (select from the in-game menu or ALT+ENTER). If you change resolution while the game is paused, any in-game screens will be blacked out. Reshade might not grab the right depth buffer after a resolution change, you may need to select a different one.

## Useful Links
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Tom_Clancy%27s_Splinter_Cell:_Blacklist)