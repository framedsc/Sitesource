Universal Unreal Engine 4 Unlocker
=============

![UUU Logo by Ichisake](Images\UUU\UUULogo.jpg){.shadowed }

**Engine versions supported**: Unreal Engine 4.15 - 4.24

@alert Important
It's forbidden to host the Universal Unreal Engine 4 Unlocker binaries elsewhere, be it your own site or e.g. Nexus Mods. 
The only site the unlocker binary is distributed on is this site. 
@end

For Unreal Engine 4 powered games, there's a universal way to add a free camera, add timestop, a hud toggle and re-create the in-game console (which is usually stripped out in released games): The Universal UE4 Unlocker, in short **UUU**. It comes with its own client exe, UuuClient.exe, and is ready to use. See below what you have to do to get started.

## Downloading the UUU

To download the UUU please use the link below. It's usable with all [the supported games in the list](universal_ue4_consoleunlocker.htm#games-that-work-with-the-unlocker). 

* [Universal UE4 Unlocker v3.0.0](https://mega.nz/#!MBw1wAiB!E6B_O5xamAi-XanX6cgf9m2zQo42jvTygtG8sgGCOnc). See for the changelog [below](universal_ue4_consoleunlocker.htm#changelog).

## Starting the UUU
After downloading the zip linked below, unpack it in an empty folder. 

### Injecting the DLL
Now you first start the game and when the game has opened its main menu, you start the UuuClient.exe application to inject the UniversalUE4Unlocker.dll into the game's process and control its features. To do so, on the *General* tab you click the **Select...** button and select the game's process. You can leave the 'DLL to inject' as-is as it should already refer to the `UniversalUE4Unlocker.dll`. 

![The general tab before selecting a game](Images\UUU\GeneralTab.jpg){.shadowed}

After you've select the game's process, you click the **Inject DLL** button. The UUU dll is now injected and the General tab switches to the following screen: here, the UUU is injected into the Darksiders III game process.

![The general tab after injecting](Images\UUU\GeneralTab2.jpg){.shadowed}

@alert tip
If you click **Select** and the game process isn't shown, even though you know it's running, it's likely the game runs as administator and you therefore have to run the UuuClient.exe also as administrator: right-click the UuuClient.exe and select 'Run as Administrator' or create a shortcut to the 
exe on your desktop, right-click it, select *Properties* and on the *Shortcut* tab, select *Advanced...*, then check the 'Run as Administrator' checkbox and click OK.
@end

### After injecting the DLL
After you've successfully injected the dll, you'll get a series of notification windows in the top left corner of your game window which some info regarding what the UUU is doing. You can now switch to the *Available features* tab to see which features of the UUU are available with the game you're using it with. 

![The available features tab](Images\UUU\AvailablefeaturesTab.jpg){.shadowed}

Here, with Darksiders III as example game, all features are available. 

The **Game speed** can be used with the *Slomo timestop* when it's active. The **Dump object info** button can be used to dump all active object names and the addresses in memory to a text file on disk. This feature is helpful for people who want to use cheat engine with the game at hand. See for more info [the object dumping section below](universal_ue4_consoleunlocker.htm#dumping-object-addresses).

## Configuration
The UUU has various settings you can configure, which you'll do on the *Configuration* tab. Additionally you can define the key-shortcuts for various functionality on the *Key bindings* tab. These are discussed below

### Configuration tab
![The configuration tab](Images\UUU\ConfigurationTab.jpg){.shadowed}

Most settings are for the built-in free camera and are self explanatory. The *Game control device* allows you to select which device to use for controlling the built-in free camera. By default it's both 'keyboard+mouse' and 'gamepad'. The device that's chosen is blocked by default to send its input to the game (as much as possible, sometimes this is unavoidable). 

#### Key selection for opening the in-game console
It might be the `~` key doesn't do anything, even though the console was created successfully by the dll. This might be caused because the game unbound the `~` key and therefore it's not possible to open the console. Additionally, you might be using a non-US keyboard, like an Azerty keyboard, and on those keyboards, the `~` key isn't above the TAB key and the engine won't recognize it. 

To correct this, on the *Configuration* tab, the setting **Key to open in-game console** allows you to select from a small set of keys what to use to open the console. By default this is 'Tilde' (`~`). Please select a key that's on your keyboard and which doesn't need Shift to be selected. E.g. on a French (Azerty) keyboard, the '$' key is a good choice, so choose in the drop down `Dollar ($)` as console key. 

### Keybindings tab
![The Keybindings tab](Images\UUU\KeybindingsTab.jpg){.shadowed}

To change a key binding, click in the textbox and press the key combination you want to use, then click the **OK** button that appeared next to the textbox when you clicked it. If you changed your mind, just click **Cancel**. You can use the same key combination for multiple features. This allows you to e.g. use `Insert` for enabling the free camera, stopping time and hiding the HUD at the same time. 

The UUU comes with its own menu. To open this menu, press `Ctrl-Ins`. It contains various tab pages, among them one where you can configure key bindings. The main 
tab is the first tab, the Settings tab. This tab allows you to configure camera specific values, which device you want to use for the camera etc. 

## Opening the in-game console
In-game, press the `~` key (it's the key above the `TAB` key on your keyboard). This should give a small line at the bottom of the 
game screen in which you can type commands. If you type the `~` again you'll get a larger console window which also shows the response of the game on your commands. 

To do useful things like starting the debug camera, in a lot of games you first have to enable the cheats in the game. To do this, type `EnableCheats 1` in the console and hit `enter`. After that, type `toggledebugcamera` after you've loaded a level. This should give you the ability to move the camera around using your controller and WASD + mouse. This can be a good alternative for when the built-in camera of the UUU isn't available.

To go back to the game, type again `toggledebugcamera` in the console or simply press cursor UP to go to a previous command. There are many commands to choose from. Not all of them work. E.g. `god` or `fly` might say they're activated but chances are they're not doing anything. Commands like `fov 50` (to set the FoV to 50 degrees, default is likely 80), `pause` (to toggle the pause of the game) and a lot of console variables do work. 

Please see the [Tweaking Unreal Engine 4 Games](../GeneralGuides/ue4guide.htm) guide elsewhere on this site for more info about what commands you could use to make the game look even better. 

### What to do when the console doesn't open
It might be the `~` key doesn't do anything, even though the console was created successfully by the dll. This might be caused because the game unbound the `~` key and therefore it's not possible to open the console. Additionally, you might be using a non-US keyboard, like an Azerty keyboard, and on those keyboards, the `~` key isn't above the TAB key and the engine won't recognize it. 

To correct this by choosing a different key to open the console, please see the [Configuration section above](universal_ue4_consoleunlocker.htm#configuration). 

#### Setting the console key in the game's ini files
Alternatively, you can add a custom console key to the game's ini file. This doesn't always work, but it's worth a try if you want to use another key than is available in the menu. Follow these steps

* In explorer go to: `c:\users\<your username>\AppData\Local\<game name>\Saved\Config\WindowsNoEditor`
* open Input.ini
* Add (pay attention to the empty line, that has to be there):

```

[/Script/Engine.InputSettings]
ConsoleKey=Tilde
```
* Save and set the file to readonly. You can also set it to another key, e.g. K. 

## The built-in free camera
The UUU has a sophisticated built-in free camera, which you can enable at any time by pressing `Insert` (or the key binding you've configured). The camera is controlled by the device that you have selected in the Configuration tab. See below for the default controls. You can configure the keyboard shortcuts in the *Key bindings* tab. 

### Controls

Key/button | Description 
--|--
Insert                                | Enable/Disable camera
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
The camera will move / rotate slower when you lower the fov.

## Hotsampling

For hotsampling, or better: dynamically resize the game window to a higher resolution, the usual tool to use is [SRWE](https://github.com/dtgDTGdtg/SRWE). 
The UUU has the same functionality SRWE offers now built-in and has a handy pre-selection of resolutions generated from your monitor's native resolution, using a variety of aspect ratios. 

![The hotsampling tab](Images\UUU\HotsamplingTab.jpg){.shadowed}

Unreal Engine 4 games by default support hotsampling, as long as you run the game in Windowed mode (in DX12, borderless might also help, but usually, it's
Windowed). If you run your game as full screen, hotsampling might just stretch the game window's content but not set the game's rendering resolution to a higher resolution. 

After you've select the resolution and aspect ratio you want to use, click the **Set** button to activate it. By default the UUU will switch focus back to the game window so you can immediately take the shot. To get back to your native play resolution, you can either select it from the tree or click the **Fake fullscreen** window. 

## Dumping object addresses
The UUU has another feature up its sleeve: it can dump the memory locations and names of all currently active engine objects a text file in the game folder, called `UUU_Objects.txt`. To do that, on the *Available features* tab, click the **Dump object info** button. The memory addresses listed in the file differ per level and every time you run the game, so if you want to look up objects in-memory after you've loaded a new level, you have to 
dump the file again. The Objects file is useful for people who create cheat tables. 

## Games that work with the unlocker
Although the name suggests it's a universal unlocker that always works with any Unreal Engine 4 game, the reality is that developers sometimes change the game engine's code and the unlocker can't re-activate the console as essential functions aren't there anymore, or activate other features offered by the UUU. The list below are games which are known to work with the unlocker. 

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
* Areia: Pathway to Dawn
* Arise a Simple Story
* Assemblance: Oversight
* Ashen
* Ashes Of Oahu
* Assetto Corsa Competizione
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
* Deliver us the moon
* Desolate
* Devil's Hunt
* Donensbourgh
* DRAGON BALL Z: KAKAROT
* Dragon Quest XI: Echoes of an Elusive Age
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
* GRIP: Combat Racing
* Hellblade: Senua's Sacrifice
* Hollow
* Hunting Simulator
* Infliction
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
* Offroad Racing Buggy X ATV X Moto
* Only After
* Operencia: The Stolen Sun
* The Outer Worlds
* Overkill's The Walking Dead
* Pagui打鬼
* Paranormal Activity The Lost Soul
* 港詭實錄ParanormalHK
* Past Cure
* Planet Alpha
* Praetorians HD Remaster
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
* Sword Art Online: Fatal Bullet
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
* The Works of Mercy
* XING The Land Beyond
* ZED

## Built-in functionality

The following features are build-in (and enabled if the code can be found in the game). You can configure most key bindings on the *Key bindings* tab.

See the camera section above for the controls for the camera itself

Feature | Key 
--|--
Toggle camera | `Insert`
Toggle widget based HUD / Menu elements | `Delete`
Toggle game pause (Using UWorld::IsPaused) | `Numpad 0`
Toggle game pause (Using slomo 0) | `Page Down`
(In-game) Open the console | `~`
Controlling game speed with slomo 0 game pause| Available features tab

### Multiple game pause/timestops
The UUU has two ways to pause the game: using the normal UWorld::IsPaused hack, (`Numpad 0`), and one using the slomo command code, (`Page down`).
You can use either one, if they're both available/found. `Numpad 0` is a hard-pause which could lead to TAA jitter in the scene. 

You can remove that by stepping down the AA a bit, using the following command on the in-game console: `r.postprocessaaquality 2` in the console. 
To set it back, use `r.postprocessaaquality 6`. The downside of that is that cutscenes might play on and the lower quality AA might remove some effects. 

The slomo based pause using `Page Down` doesn't suffer from TAA jitter, and can pause most, if not all, cutscenes as well (except audio in some
situations). In general, if the latter is supported, you should use the slomo based pause. 

If both don't work, you can try `pause` on the in-game console. `pause` isn't an official command but a lot of games support it in one way or the other.

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

## Credits

Development: Otis_Inf  
Research: Otis_Inf and SunBeam  
Logo: Ichisake  
Dumper code is based on the SDK generator by Kn4ck3r.  
Special thanks to Pino44io for testing.  

&copy;2019-2020 All rights reserved.

## Changelog

###v3.0.0: 
- **ADDED**: Added new user interface which offers hotsampling and doesn't rely on DirectX hooking for menu display.

###v2.0.6: 
- **ADDED**: Added support for UE4.23's new NamePool structure for object names. This adds support for UE4 4.23 and higher
- **FIXED**: Fixed an issue that could occur with some games where one of the camera write blocks in the engine uses a different register, causing the game to crash as
the UUU uses a single interception block for all camera write blocks. 

###v2.0.5:
- **FIXED**: Fixes issue with slomo interception where a slow motion action set by the game was resulting in a high game speed instead of a slow game speed. 

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