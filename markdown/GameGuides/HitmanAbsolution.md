<!-- ![Hitman: Absolution](Images\Hitman_Abs_header.jpg "Shot by unknown"){.shadowed}-->

##Feature summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11
 
##Tools
* [CE table - Camera by One3rd and ghostinthecamera](..\CheatTables\Hitman_Absolution.CT)  
**Features**: Camera Control, FoV, Tilt, Timestop

* [HUD Toggle by the_janitor and One3rd](https://mega.nz/#!3cxmkC4Y!LIKJv-H4V11h3t1si3kBJpLgxTsPi56bDhoR4AOlPNo)  
**Features**: Toggle for the in-game HUD and Pause Menu HUD

##Cheat table notes

1. The Rotation Camera can be enabled and disabled at any time with [Page Up] to enable the Rotation script (IMPORTANT) and then [Page Down]. The camera is controlled with the keypad keys as shown in the table. Be warned that this can be a bit wonky at times and difficult to control with the pitch, yaw and roll control with the numpad keys.
	* This camera can be used in the Pause Menu and during cutscenes.
	* If using the Timescale control below the script may at times not find the correct camera addresses, if this occurs just go into the Pause Menu as that will find the correct camera addresses.
	* The Enable Camera Script will block access to the Pause Menu. If [ESC] is pressed to bring up the Pause Menu while this script is active everything will stop. Perform the following steps if this occurs:
		1. Disable the Enable Camera script [Page Down]. If time is stopped the camera position will not change.
		2. Press [ESC] to go into the Pause Menu.
		3. Re-enable the Enable Camera script with [Page Down]
	* FOV changes will only take place after ALT-Tab back into the game. Change the FOV value with below keys and then ALT-Tab out and then back in to the game for changes to take effect.

2. If rotation is not working try enabling, disabling then re-enabling the Rotation Camera script.
	1. Enable the rotation script - [Page Up]
	2. Disable the rotation script - [Page Up]
	3. Enable the rotation script - [Page Up]
	4. Enable the camera script - [Page Down]

3. Enable  Timescale control with the following keys.

	Key | Command
	--|--
	ESC | Pause Menu
	P | Timestop with no mouse rotation
	Shift+P | Timestop with mouse rotation 
	[ | SloMo - Time set to 0.1
	Shift+[ | Unpause - Time set to 1.0

4. jim2point0's original Free Camera Script is supplied as well as it can also be used to control the camera but will using the mouse for rotation. This is much easier to use. Once the script is enabled the numpad keys control position.

	Key | Command
	--|--
	F2 | Enable/disable script
	F3/F4 | Timstop with mouse rotation
	F5 | Lock camera to current position so character can be moved into position

5. The Pause menu has a blur applied to it that can be removed by enabling the Main Menu Blur Script with [Insert] before pressing [ESC] to bring up the Pause Menu.

6. I've merged some cheat scripts by Blayde. These allow for stealth, instincts, health and ammo control. Make sure to disable these scripts before going to a new level or restarting the current level as it may cause the game to crash.


##HUD toggle notes

HUD Toggle was made by the_janitor using 3DMigoto. I've added a couple of shader removals to remove some extra HUD elements but the keys are the same.

	Key | Command
	--|--
	NUMPAD_ZERO | Toggle HUD
	H | Toggle Instinct wallhack outlines

##Reshade Depth Buffer

1. Set RESHADE_DEPTH_INPUT_IS_REVERSED to 0.
2. Set RESHADE_DEPTH_LINEARIZATION_FAR_PLANE to 10000 (default is 1000).


##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Hitman:_Absolution)