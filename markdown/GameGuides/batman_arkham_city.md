![Batman: Arkham City](\Images\batman_ac.png "Shot by Originalnicodr")

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes, see note
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 9
 
## Tools

* [CE table by One3rd, Cielos and SunBeam](../CheatTables/BatmanACv0.5.2.CT)  
**Features**: Camera Control, Tilt, HUD Toggle, FoV, Tonemap, Bloom, Console Enabler, Cheats.

## Usage
Enable the camera when in-game so the script can grab the correct addresses and you should see the script expand with addresses populating when in-game. This is needed before going into the pause menu to actually control the camera. The free camera will only work when the game is paused!

## Controls
Key | Description
--|--
Page Down | Activate camera
Numpad 2/8 | Y coordinate
Numpad 4/6 | X coordinate
Numpad 3/9 | Z coordinate
Arrow keys | Rotate camera
Numpad +/- | Adjust FOV (see FOV section)
'-'/'=' | Tilt camera
F12 | Menu HUD Disable
Ctrl + F12 | Menu HUD Enable
Pause Button | Timestop
Hold CTRL | Move the camera position and orientation faster
Hold ALT | Move the camera position and orientation slower

FoV control: (requires you to force it with the UE3 FOV keybind command while in game first, do this before going into the Pause Menu for it to work. See FOV section below.)

## Timestop
Timestop is done using the Pause Menu (Main Menu), removal of the menu HUD and Pause Menu filter overlay. Press "ESC" to pause the game, F12 to clear the HUD and filter, and Keypad to move the camera around.


## FOV

To control the FOV you would need to edit a config file, so go to `..\Documents\WB Games\Batman Arkham City GOTY\BmGame\Config\` and open `UserInput.ini`.

Under the [Engine.PlayerInput] section add the FOV bindings at the tail end of that same section.

```
.Bindings=(Name="F4",Command="FOV 40", Control=False, Shift=False, Alt=False)
.Bindings=(Name="F5",Command="FOV 50", Control=False, Shift=False, Alt=False)
.Bindings=(Name="F6",Command="FOV 60", Control=False, Shift=False, Alt=False)
.Bindings=(Name="F7",Command="FOV 70", Control=False, Shift=False, Alt=False)
.Bindings=(Name="F8",Command="FOV 80", Control=False, Shift=False, Alt=False)
.Bindings=(Name="F9",Command="FOV 90", Control=False, Shift=False, Alt=False)
.Bindings=(Name="F10",Command="FOV 100", Control=False, Shift=False, Alt=False) 
```

You can of course choose the keys you want, but keep in mind before editing the FoV with the '-' and '+' keys you would need to change it once with one of the bindings you wrote in your `UserInput.ini`. You would probably need to do this again if you enter a new zone.

## Graphic tweaks

As with the previous game you can modify some engine values to get more quality in the game. Go to the file `..\Users\USERNAME\Documents\Square Enix\Batman Arkham Asylum GOTY\BmGame\Config\BmEngine.ini` and edit the following lines:

```
DepthOfField=False  
MaxAnisotropy=16
ShadowFilterQualityBias=0
MinShadowResolution=32
MaxShadowResolution=2048 
// change to '1024' for faster performance, '3072' or above for better quality
ShadowFadeResolution=5
ShadowFilterRadius=5.000000
SkeletalMeshLODBias=-1
ParticleLODBias=-1
```
These last two settings affects LoD (Level of Details) which reduces quality of meshes and particles 
the further the camera is from them. Something far away doesn't need to be as detailed as something which is 
right in front of the camera. This is made to improve performance, but can introduce some popping. The -1 settings disable LoD altogether, which is very performance hungry!

Press Ctrl+F and search for MemoryPools.
Under `[MemoryPools]` make the following changes:

```
FLightPrimitiveInteractionInitialBlockSize=1024
FModShadowPrimitiveInteractionInitialBlockSize=1024
```
You can use higher values than that but it will makes the loading screens longer, but will reduce textures and static shadow popping.
Remember to save the changes and set the file to read only so it doesn't get overridden.

## Cheats

The Cheat Table also provides some gameplay cheats to help you compositioning a scene.
In the table, expand Cheats -> Scripts -> Cheat Handler.

Key | Description
--|--
U/I/O | Slomo 0.01, 0.3, 1.0
M | PlayersOnly
, | Fly
. | Ghost
J | Unlimited Ammo
K | God
L | No Combo Reset


## Miscellaneous
The cheat table also provides a way to edit the engine DoF, but since its not very good (at least compared with the modern DoF aviable in ReShade) I recommend you to disable the game deapth of field all together. That is done in the Graphics tweaks section.

There are a couple more things the table can do, like enabling and disabling the Frost Overlay (F11 and Ctrl + F11 respectively) and editing the bloom and tonemap values, altho these last two dont have keys binded at the moment, you will need to make manual changes to these by double-clicking the value in the table, multiple values can be selected at once.

## Rendering Resolution

The game only seems to recognize your current desktop resolution. Change your desktop then set the ini file to the same resolution and start the game. Change the resolution in `..\Documents\WB Games\Batman Arkham City GOTY\BmGame\Config\UserEngine.ini` by setting the below lines to whatever your desktop resolution is currently set to. Different aspect ratios do work.
```
ResX=5120
ResY=2880
```

## Useful Links

- [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Batman:_Arkham_City)
- [HD textures mod](https://steamcommunity.com/sharedfiles/filedetails/?id=1188257825)
- [Unlock skins from the get go, force idle animations and more](https://steamcommunity.com/sharedfiles/filedetails/?id=1439618122)
- [Swap character meshes](https://steamcommunity.com/sharedfiles/filedetails/?id=649900424)
- [List of Console Codes](https://fearlessrevolution.com/viewtopic.php?t=1217)