![Wolfenstein: The New Order](\Images\wolfenstein_the_new_order.png "Shot by Originalnicodr")
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes (desktop DSR)
Custom Aspect Ratios | No (see notes)
Reshade | Yes (see notes)
Ansel | No
Graphic API version | OpenGL
 
## Tools
 
* [CE Table by K-Putt & Jim2point0, merged with SunBeam's table](\CheatTables\wolfenstein_the_new_order.CT)  
**Features**: Freecam, Tilt.
* Plus some cfg edits and commands for pause, HUD toggle, gun and arms toggle, FoV control, DoF and film grain toggle.
 
## Setting up the game
 
### Activating the console
The CT have a script to open the console with the tilde key, if it isn't working try adding `+com_allowConsole 1` as a startup parameter in the game (through steam parameters or direct access properties), without the table script and only that parameter it will bind the console to tilde key + control.
 
### Modifying the wolfConfig file
 
Go to your wolfConfig.cfg (located in `C:\Users\User\Saved Games\MachineGames\Wolfenstein The New Order\base`) and add the following lines in the bindset 0 section:
 
```
bind "F5" "toggle g_showhud;toggle hands_show"
bind "F6" "cvarrandom g_stoptime 0 0"
bind "F7" "cvarrandom g_stoptime 1 1"
bind "F8" "g_fov 100"
bind "F9" "cvaradd g_fov -5"
bind "F10" "cvaradd g_fov 5"
```
 
Sometimes F5 and F9 don't work as intended so you would need to rebind them in the game every time. Open the console with the tilde key and copy these lines one by one:
 
```
cvaradd r_skippostprocess 1
bind F9 "cvaradd g_fov -5"
bind F5 "toggle g_showhud;toggle hands_show"
```
 
The first command turns off the engine DoF and filmgrain, but it also turns off other post processing effects like color correction, altho not all of them. If you only want to turn off the post processing effects for shooting you can instead add bindings to change the `r_skippostprocess` value to -1 and 1 to turn them on and off respectively.

If you want to remove the game's bloom you can use the console command `r_skipadaptiveglare 1` to do so.

Subtitles cant be turned off with F5, but you can dissabled them in the game options after composing a shot.
 
## Usage
 
Before shooting make sure to enter the command `r_multisamples 16` in the console to force the highest AA, altho it will freeze the game's depth buffer. To fix it just press `Esc` two times to open and close the menu. The same will probably happen if you want to go back to the old AA with `r_multisamples 2`.
 
 
If you followed the guide to the letter you will end up with the following bindings
 
Description | Key/button 
--|--
Pause | F6
Unpause | F7
Toggle Hud, arms and gun | F5
Increase/Decrease FOV | F9/F10
Activate/Disable CE movement | Numpad 0
Activate/Disable gravity | Numpad 0
Move camera position| WASD
Move camera position (CE movement) | Numpad 4, Numpad 6, Numpad 8, Numpad 2
Move camera orientation| Mouse
Move camera up/down | Space bar/Control
Move camera up/down (CE movement)| Numpad 9, Numpad 3
Activate tilt modification | `.`
Tilt left/right | `{` / `}`
Tilto to 0 degrees | `+`
Tilt to 90 degrees | `´`
Faster CE camera position movement | Alt + Numpad 4, 6, 8, 2
Slower CE camera position movement | Ctrl + Numpad 4, 6, 8, 2
Faster tilting | Alt + `{` / `}`
 
To use the freecam you will need to click the box in Cheat Engine that says "Enable 'god', 'noclip', 'notarget', console commands" so you can use the `noclip` command, which will be used as the freecam. Use the WASD keys to set up the shot and press Numpad 0 to activate the cheat engine movement (which only works with noclip enabled), allowing you to do fine adjustments with the numpad.
 
### Tilting
 
Once you get the position, before turning noclip off (enter the noclip command again in the console) turn off gravity (and CE camera position movement) if you haven't done so yet. After doing so and pressing the '.' key in the numpad you would be able to tilt with the keys stated above. 
 
Also take in mind that **tilting may result in your character taking damage tho putting blood in the screen because of collisions, making you unpause to get the blood out of the screen.**. If you find yourself with this problem try using the 'god' command.
 
 
 
 
## ReShade
 
There is a bug in OpenGL that doesn't let CineDOF compile properly (in Reshade 4.7 and probably previous releases). This has already been reported and (apparently) fixed in the next ReShade version, so use a version above 4.7 if you want to use this specific shader.
 
 
 
## Custom Aspect Ratios 
 
The game doesn't support vertical ARs (it stretches the image). Even tho wider AR seems to work, most of the time you will get hud elements at the side of the screen, but since this depends on the mission you may successfully use wide ARs.
 
## Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Wolfenstein:_The_New_Order)