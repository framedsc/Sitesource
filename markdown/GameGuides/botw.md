![The Legend of Zelda: Breath of the Wild](Images\botw.png "Shot by ItsYFP"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes (CEMU Graphic Settings)
Reshade | Yes (OpenGL & Vulkan)
Ansel | No
DirectX versions | Unknown (what ever works with CEMU)
 
## Tools

* [TLoZ: Breath of the Wild Free Camera by etra0](https://github.com/etra0/botw-freecam/releases)  
**Features**: Free Camera, Tilt and FOV Control  
**Important**: Tested with Cemu 1.22.2 and Breath of the Wild v1.5.0 DLC Ver.3.0 (Support for other versions is not assured)
* [Stop Time and LOD Enhancement CE table by Postposterous](https://gamebanana.com/tools/7052)
**Features**: Timestop and improved LOD

## Controls

Key | Action
--|--
F2 / L2 + Circle / RT + B | Photo Mode Activation
WASD + Arrow keys / Sticks | Camera Movement
Q - E / Square - Triangle / X - Y | Camera Height
F5 - F6 / R2 - L2 / RT - LT | FoV Control
PgUp - PgDown / R1 - L1 / RB - LB | Camera Rotation
F3 - F4 / dpad left - dpad right | Change Camera movement Speed
Shift / X / A | Accelerates Camera movement temporarily



## Tips and Tricks

### Reshade

Install Reshade to the CEMU Main Folder where the CEMU.exe is located, OpenGL is preferred. 
Vulkan Support for CEMU is available but still experimental. 
Make sure to activate the Reshade Compatibility Modification in CEMU. 
Options > Graphic Packs > The Legend of Zelda: Breath of the Wild > Workarounds > Reshade Compatibility


### CEMU Graphic Improvements, High Resolution Screenshots and HUD

The Breath of the Wild Graphics Packs include various Enhancements you can/should use with the following Settings.
(Tested on i7-6700k / GTX 1070 / 16GB Ram)

**The HUD**
CEMU offers a few Options in the Mods Category but you can also go to the In-Game Options on the Main Menu, set the HUD Mode to PRO.
This disables already most of the annoying stuff on your screen.

**Category Mods:**
Enable Extended Memory.
Draw Distance, you are free to experiment with the settings here, if your Hardware is good enough you can likely set it to the highest available.
FPS++ should speak for itself, you need more Frames? Set it to the desired value. Available options from 20FPS to 240FPS.

**Category Workarounds: GPU Specific for OpenGL**
Enable the 2 available Workarounds for your Specific GPU Manufacturer (AMD or Nvidia)

**Category Workarounds:**
Enable all OpenGL Workarounds when using OpenGL.
Enable all Vulkan Workarounds when using Vulkan.

**Category Enhancements:**
CEMU offers a few things here, but mainly you want to disable the In-Game Depth of Field, enable Enhanced Reflections and set Anisotropic Filtering to Extrem (16x).

**Category Graphics:**
Set your desired Aspect Ratio, e.g 16:9, 21:9 etc.
Anti-Aliasing to NVIDIA FXAA or Normal FXAA (Default)
Shadows to Ultra (300%)
Resolution, depends how far you Hardware let you go here. In my case i can run and play the Game with stable 30FPS at 5K (5120x2880).

**Capturing High Resolution Screenshots**
The only way i was able to capture my Screenshots in the actual rendered Resolution, was by setting my Desktop Resolution with Nvidia DSR, to the same Resolution i had chosen in the CEMU Graphics Settings. Desktop 5K & In-Game 5K.
Additionally neither Reshade, MSI Afterburner or Print Screen are able to Capture and Save my Screenshots including all Reshade Effects.
If it does work for you, thats great! :) The last option in my case was/is the Snipping Tool from Windows.