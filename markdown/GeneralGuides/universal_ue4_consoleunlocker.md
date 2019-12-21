Universal Unreal Engine 4 Console Unlocker
=============

@alert Important
It's forbidden to host the Universal Unreal Engine 4 Console Unlocker binaries elsewhere, be it your own site or e.g. Nexus Mods. The only site the
unlocker binary is distributed on is this site. 
@end

For Unreal Engine 4 powered games, it's possible to re-create the in-game console that's usually stripped out when the game is build for shipping. To do so, 
you can use the Universal UE4 Console Unlocker / Dumper dll, in short **UUU**. It comes with its own injector, IGCSInjectorUI.exe, and is ready to use. See below what
you have to do to get started.

@alert important
The game's exe as well as the IGCSInjectorUI.exe have to be run as *administrator*. Right-click the exe's to run and select 'Run as Administrator' or create a shortcut to the 
exe on your desktop, right-click it, select *Properties* and on the *Shortcut* tab, select *Advanced...*, then check the 'Run as Administrator' checkbox and click OK. 
@end

## Downloading the unlocker

There are two versions at the moment: v1.0.16, which is a version with just the console enabler/dumper and which doesn't contain its own camera system, and v2.0.x which 
does contain its own camera system. v2.0.x requires Direct3D 11 at the moment, so if you're using a game that uses Direct3D 12, or fails to work with the camera system,
you could try v1.0.16 and the debug camera of Unreal Engine. 

* [Universal UE4 Unlocker v2.0.4](https://mega.nz/#!4B4gFAhb!J2_L4LgWBv_Y625E2AWJNl8PnOtDPSV3qQ8_TmM0qGE). See for the changelog [below](universal_ue4_consoleunlocker.htm#changelog).

* [Universal UE4 Unlocker v1.0.16](https://mega.nz/#!QVxCmIwQ!40fnUHK5Ai_rgXylzQZQ8yASpTOpGY3uCO2AVGhR3hg). (No built-in camera, only for console enabling)

## Setting up the injector
After downloading the zip linked below, unpack it in an empty folder. Now you first start the game and when the game has opened its main menu, 
you start the IGCSInjectorUI.exe application to inject the dll into the game's process. To do so, you click the `Select...` button and select the game's process. 
You then click the `Inject` button, as the dll has already been pre-configured, and the injector should successfully inject the dll into the game's process you
selected. 

### If the injector doesn't work
Some people on Windows 7 have reported issues with the IGCSInjector. If that happens, please try another dll injector, e.g. Extreme Injector. 

## After injecting the DLL
When you've successfully injected the dll, you'll get a notification in the top left corner of your game window which some info regarding who made the unlocker and
which version it is, as well as some notifications what it's doing. If everything went OK, you should see some notifications that the console has been created and 
the built-in camera has been found. 

### In-game menu
The UUU comes with its own menu. To open this menu, press `Ctrl-Ins`. It contains various tab pages, among them one where you can configure key bindings. The main 
tab is the first tab, the Settings tab. This tab allows you to configure camera specific values, which device you want to use for the camera etc. 

### Opening the in-game console
In-game, press the `~` key (it's the key above the `TAB` key on your keyboard). This should give a small line at the bottom of the 
game screen in which you can type commands. If you type the `~` again you'll get a larger console window which also shows the response of the game on your commands. 

To do useful things like toggle the debug camera, in a lot of games you first have to enable the cheats in the game. To do this, type `EnableCheats 1` in the console 
and hit <enter>. After that, type `toggledebugcamera` after you've loaded a level. This should give you the ability to move the camera around using your controller 
and WASD + mouse.

To go back to the game, type again `toggledebugcamera` in the console or simply press cursor UP to go to a previous command. There are many commands to choose from. Not all
of them work. E.g. `god` or `fly` might say they're activated but chances are they're not doing anything. Commands like `fov 50` (to set the FoV to 50 degrees, default is 
likely 80), `pause` (to toggle the pause of the game) and a lot of console variables do work. 

## What to do when the console doesn't open
It might be the `~` key doesn't do anything, even though the console was created successfully by the dll. This might be caused because the game unbound the `~` key
and therefore it's not possible to open the console. Additionally, you might be using a non-US keyboard, like an Azerty keyboard, and on those keyboards, the `~` key isn't
above the TAB key and the engine won't recognize it. 

To correct this, please open the UUU overlay menu by pressing `Ctrl-Ins` and on the settings tab you'll see a setting
"Key to open in-game console", which allows you to select from a small set of keys what to use to open the console. By default this is 'Tilde' (`~`). Please select
a key that's on your keyboard and which doesn't need Shift to be selected. E.g. on a French (Azerty) keyboard, the '$' key is a good choice, so choose in the 
overlay menu `Dollar ($)` as console key. 

@alert info
It might be you're running an EA Origin game and have the Origin overlay enabled. This too can block the console from appearing. To fix it, please disable
the Origin overlay in the EA Origin client. 
@end

#### Setting the console key in the game's ini files
Alternatively, you can add a custom console key to the game's ini file. This doesn't always work, but it's worth a try if you want to use another key than is available in
the menu. Follow these steps

* In explorer go to: `c:\users\<your username>\AppData\Local\<game name>\Saved\Config\WindowsNoEditor`
* open Input.ini
* Add (pay attention to the empty line, that has to be there):
```

[/Script/Engine.InputSettings]
ConsoleKey=Tilde
```
* Save and set the file to readonly. You can also set it to another key, e.g. K. 

## The Built-in free camera
The UUU has a built-in free camera, which you can enable at any time by pressing `Ins`. The camera is controlled by the device that you have selected in the overlay menu. 
See below for the default controls. You can configure the keyboard shortcuts in the overlay menu in the keybindings tab. 

### Controls

Key/button | Description 
--|--
Ctrl-Ins                              | Show / Hide Camera tools main window
Ctrl + Mouse wheel                    | Resize font
Ins                                   | Enable/Disable camera
HOME                                  | Lock/unlock camera movement
ALT + rotate/move                     | Faster rotate / move
Right-CTRL + rotate/move              | Slower rotate / move
Controller Y-button + l/r-stick       | Faster rotate / move
Controller X-button + l/r-stick       | Slower rotate / move
Arrow up/down or mouse or r-stick     | Rotate camera up/down
Arrow left/right or mouse or r-stick  | Rotate camera left/right
Numpad 8/Numpad 5 or l-stick          | Move camera forward/backward
Numpad 4/Numpad 6 or l-stick          | Move camera left / right
Numpad 7/Numpad 9 or l/r-trigger      | Move camera up / down
Numpad 1/Numpad 3 or d-pad left/right | Tilt camera left / right
Numpad +/- or d-pad up/down           | Increase / decrease FoV
Numpad * or controller B-button       | Reset FoV
Numpad .                              | Toggle block input to game for camera control device.

By default, when the free camera is enabled, the input to the game is blocked for the device that's controlling the camera. 

### Taking screenshots
The UUU comes with its own screenshot key, by default the Pause key. It writes the frame (including effects you might have applied with reshade) to a file with a name generated
from the date+time, to the folder you've specified in the overlay menu. 

It also offers two other screenshot types: Panorama shots and Lightfield shots. Each of these takes a multitude of shots; the panorama feature takes as much shots as needed
to satisfy the requirements set for panorama shots in the overlay menu and rotates the camera from left to right. You can stitch the shots together to a
single panorama with e.g. Microsoft Image Composition Editor or Photoshop.

The lightfield feature takes shots by stepping the camera
from left to right, moving it over a rail to to speak. You can then create a lightfield 'quilt' for e.g. Looking Glass 3D displays. 

To test the setup you have, press `Page Up`. To take all shots, press `Ctrl-PageUp`.

## Dumping names / object addresses
The unlocker has another feature up its sleeve: it can dump two text files in the game folder called UE4Tools_Names.txt and UE4Tools_Objects.txt. To do that, press `Ctrl-Numpad /`.
The Names file contains all names of all objects in the game. Most of them aren't really useful, but some are, e.g. if you open the file in a text editor and search for " sg." 
you find all settings variables for things you can also set in the game menu, only these accept higher values. Another one is " r." to find all render variables. 

The Objects text file shows all objects in the engine, and their addresses in memory. These memory addresses differ per level, so if you want to look up objects in-memory
after you've loaded a new level, you have to dump the files again. The Objects file is useful for people who create cheat tables. 

## Games that work with the unlocker
Although the name suggests it's a universal unlocker that always works with any Unreal Engine 4 game, the reality is that developers sometimes change the game engine's code
and the unlocker can't re-activate the console as essential functions aren't there anymore. The list below are games which are known to work with the unlocker. 

* 10 Miles to Safety
* 103
* A Knight`s Quest
* Agony
* Alice VR
* Ancestors Legacy
* Ancestors - The Humankind Odyssey
* Ancient Knowledge
* Another Sight Definitive Edition
* Apsulov: End of Gods
* Arise a Simple Story
* Assemblance: Oversight
* Ashes Of Oahu
* Bard's Tale IV: Barrows Deep
* The Beast Inside
* Bee Simulator
* The Blackout Club
* Blair Witch
* Borderlands 3
* Bright Memory
* Burning Daylight
* Call of Cthulhu
* Captain Starshot
* Chernobylite
* Close to the Sun
* Code Vein
* Conarium
* Creature in the Well
* Dark Future: Blood Red States
* Dark Deception
* Dark Occult
* Darksiders 3
* Darksiders Genesis
* Daymare: 1998
* Deep Rock Galactic
* Deliver Us The Moon
* Desolate
* Devil's Hunt
* Donensbourgh
* Draugen
* Dreamscaper
* Driftland
* Earth Defence Force: Iron Rain 
* Earthfall
* Echo
* Elea
* Everspace
* Explore Fushimi Inari
* Extinction
* Fade to silence
* Fear the Dark Unknown
* The Fidelio Incident
* Fighting Ex Layer
* Genesis Alpha One
* Gray Dawn
* Hellblade: Senua's Sacrifice
* Hollow
* Hunting Simulator
* Insomnia the Ark
* Intruders: Hide and Seek"
* Jumanji The Video Game
* Jump Force (limited)
* Killsquad
* Kine
* Koral
* Laser League
* Layers of Fear 2
* Liberty Prime
* Life is Strange 2
* Ling: a Road Alone 
* Little Brother Jim
* Lost Ember
* Man of Medan (The Dark Pictures Anthology)
* Marvel vs. Capcom: Infinite
* Mind: Path to Thalamus
* Monkey King: Hero Is Back
* Monster Jam Steel Titans
* Moons of Madness
* Morels: The Hunt
* Morphies Law Remorphed
* MotoGP 19
* Mutant Year Zero: Road to Eden
* My Hero One's Justice
* Narcos: Rise of the Cartels
* NBA 2K Playgrounds 2
* Nephise: Ascension
* Observer
* Only After
* Operencia: The Stolen Sun
* The Outer Worlds
* Overkill's The Walking Dead
* Pagui打鬼
* Paranormal Activity The Lost Soul
* Past Cure
* Planet Alpha
* Project Remedium
* Protocol
* Occupation
* Omen of Sorrow
* Omensight
* Quantum Replica
* Qube 2
* Race With Ryan
* RAD
* Redeemer
* Remnant: From the Ashes
* Remothered: Tormented Fathers
* Ruin 2
* Ruiner
* Shenmue 3
* ShockRods
* The Sinking City
* Session: Skateboarding Sim Game
* Shape of the World
* Silver Chains
* Sinner: Sacrifice for Redemption
* Skylar and Plux
* The Sojourn
* SolSeraph
* Song of Horror
* Sophont
* Soul Valley
* SOULCALIBUR VI
* Space Hulk: Deadwing Enhanced Edition
* Space Hulk Tactics
* Spacebourne
* Spyro Reignited Trilogy
* Star Wars Jedi: Fallen Order
* Stardrop
* Steel rats
* Stories: the Path of Destinies
* Styx 2
* Subdivision Infinity DX
* Supraland
* Tartarus
* Tetris Effect
* Tower of Fate
* Train Sim World
* Tropico 6
* Urban Trial Playground
* Uventa
* Vampyr
* Visage
* Wartile
* We Happy Few
* XING The Land Beyond
* ZED

## Built-in functionality

The following features are build-in (and enabled if the code can be found in the game). You can configure most shortcut keys in the overlay menu's keybindings section.
See the camera section above for the controls for the camera itself

Feature | Key 
--|--
Open in-game overlay menu | `Ctrl-Ins`
Toggle camera | `Ins`
Re-scan AOBs and re-try to create the console | `Ctrl-End`
Display help | `Ctrl`-`H`
Dump actual object addresses and names to text files | `Ctrl`-`Numpad /` 
Toggle widget based HUD / Menu elements | `Del`
Toggle game pause (Using UWorld::IsPaused) | `Numpad 0`
Toggle game pause (Using slomo 0) | `Page Down`
(In-game) Open the console | `~`
Controlling game speed | Overlay menu

## Console tricks
The Unreal Engine console supports copy / paste of text. This is a great help if you want to execute multiple commands and have to type them in every time. 
Additionally, it supports multiple commands on the same line, where you separate the commands with the `|` character. Combined with copy/paste you can
create long strings of commands in a text file and copy/paste them over to execute all the commands in one go. 

Examples:
```
showhud 0|fov 60|pause|toggledebugcamera|r.postprocessaaquality 2
```
This hides the hud, sets fov to 60, pauses the game, enables the debug camera and sets the AA to a lower quality so you don't have jitter blur. 

The console also remembers a history of commands, and keeps the line with multiple concatenated commands as one line. To show the history, press the arrow-up key
in the console. 

## Troubleshooting
You might get an error with older games that it can't find the EngineVersion key and it will fall back to the default version. 
When that happens, the unlocker will try to auto-detect which engine version is being used. If that fails, it's likely not going to work out however. 
If it succeeds, the console can be created most likely. 

If the game crashes when injecting the unlocker, try to inject it when a level is loaded. 

## Credits

Development: Otis_Inf  
Research: Otis_Inf and SunBeam  
Dumper code is based on the SDK generator by Kn4ck3r.  
Special thanks to Pino44io for testing.

&copy;2019 All rights reserved.

## Changelog

###v2.0.4:
- **ADDED**: Better compatibility with v4.20 based engines for the camera system.

###v2.0.3:
- **FIXED**: Corrects fix for UWorld::IsPaused on older engines as the offset used wasn't correct. 
- **FIXED**: Corrects a small issue with ctrl not working for slow movement with camera after introduction of fov-driven movement corrections. 
- **FIXED**: Fixes issue with numpad 0 not pausing the first time it was pressed.
- **ADDED**: Some new AOBs for constructs seen in newer engines (v4.22+)

###v2.0.2:
- **FIXED**: Camera intercept struct 2 wasn't marked as non-critical
- **FIXED**: Using UWorld::IsPaused pause + camera in a v4.15 game enables the in-game menu camera to activate, causing the built-in free camera to be locked in-place
- **FIXED**: The rotation slider in the overlay has a range that's way too wide for the values that are practical
- **IMPLEMENTED**: Make rotation/movement speed adjust themselves based on fov. 
- **IMPLEMENTED**: Switch default screenshot type to 'HorizontalPanorama' instead of 'Lightfield'
- **IMPLEMENTED**: Use the executable filename for screenshot filename prefix in single shot screenshots.

###v2.0.1: 
- First v2.0 release with IGCS camera system built-in.