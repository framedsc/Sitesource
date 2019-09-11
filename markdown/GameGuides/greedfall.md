![Control](..\Images\greedfall.png "Shot by Jim2point0")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11

## Tools

* [CE Table by Jim2point0](..\CheatTables\GreedFall_AOB.CT)  
**Features**: Camera Coordinates, FOV, Timestop, Time of Day, Hud Toggle, and fog

## Using The CE Table 

[Read the general Cheat Engine guide](https://framedsc.github.io/GeneralGuides/cheat_engine_tables.htm) if you have't already to learn how to use cheat engine tables (don't worry, it's easy).

First, enable the main script and keep it running in the background. There's an arrow pointed at it that says "check this box." That's the only script you should have to enable manually.

If you want to use the hud toggle, open and close the menu after checking this box, which will allow the script to get the address for the HUD. **The HUD toggle requires that subtitles be enabled,** since that's the address I'm hooking for the script.

The hotkeys were tuned for smoother movement. In Cheat Engine, go to `Edit -> Settings -> Hotkeys` and change:  
Keypoll interval - 50  
Delay between activating hotkeys - 50  

* **Free Camera & FOV** - **`F1`**  
This gives you control over the coordinates, though it will not be normal WASD camera movement. The hotkeys display when you enable the script.  
Hold **`ALT`** for faster camera movement. 
* **Freeze Game** - **`Numpad 0`**  
While the game is frozen, you can still access the menu to change options. You can also change the time of day (see below). **`Numpad .`** to resume the game.
* **Toggle Hud** - **`F3/F4`**  
Press ESC twice to force the changes. This can be done while the game is frozen.
* **Time of Day** - **`[ ]`** or **`PG Up\Down`**  
Time of day is based on a 24 hour cycle. When you increase the time beyond 24, it resets back to 0. But you can decrease it below 0, which will break the lighting. Keep an eye on the table (on another monitor maybe) to make sure you aren't going below 0. 

## Some notes

This is an early version of the table. I'm going to try and improve the HUD toggle as it's very janky right now. 