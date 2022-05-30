Universal Unreal Engine 4 Unlocker
=============

![UUU Logo by Ichisake](Images\UUU\UUULogo.jpg){.shadowed .autosize}

**Engine versions supported**: Unreal Engine 4.15 - 4.26 

@alert Info
This page is for the UUU v3.0.x. This is the free version and won't be updated anymore. If you're looking for the UUU v4.x with camera paths and other
additional features, please visit [Otis_Inf's Patreon page](https://patreon.com/Otis_Inf): the UUU v4.x is part of Tier 1.
@end

@alert Important
It's forbidden to host the Universal Unreal Engine 4 Unlocker binaries elsewhere, be it your own site or e.g. Nexus Mods. 
The only site the unlocker binary is distributed on is this site. 
@end

For Unreal Engine 4 powered games, there's a universal way to add a free camera, add timestop, a hud toggle and re-create the in-game console (which is usually stripped out in released games): The Universal UE4 Unlocker, in short **UUU**. It comes with its own client exe, UuuClient.exe, and is ready to use. See below what you have to do to get started.

## Downloading the UUU

To download the UUU please use the link below. It's usable with all [the supported games in the list](universal_ue4_consoleunlocker.htm#games-that-work-with-the-unlocker). See for the changelog [below](universal_ue4_consoleunlocker.htm#changelog).

* [Universal UE4 Unlocker v3.0.21](https://mega.nz/file/MUhUlaqa#PI0ubSy_sQc4GouDPnZbulNSgQRUNIJeXNwLb2LnKhk). 
* [Universal UE4 Unlocker v3.0.14](https://mega.nz/file/8Y50GRCS#Sg3A_v5rLeCiI6a4Xppi0RI1gwWDkoU4qjEwV3_g9Eg). Use this version if v3.0.20 gives problems


## Starting the UUU
After downloading the zip linked below, unpack it in an empty folder. 

### Injecting the DLL
Now you first start the game and when the game has opened its main menu, you start the UuuClient.exe application to inject the UniversalUE4Unlocker.dll into the game's process and control its features. To do so, on the *General* tab you click the **Select...** button and select the game's process. You can leave the 'DLL to inject' as-is as it should already refer to the `UniversalUE4Unlocker.dll`. 

![The general tab before selecting a game](Images\UUU\GeneralTab.jpg){.shadowed .autosize}

After you've select the game's process, you click the **Inject DLL** button. The UUU dll is now injected and the General tab switches to the following screen: here, the UUU is injected into the Darksiders III game process.

![The general tab after injecting](Images\UUU\GeneralTab2.jpg){.shadowed .autosize}

@alert tip
If you click **Select** and the game process isn't shown, even though you know it's running, it's likely the game runs as administator and you therefore have to run the UuuClient.exe also as administrator: right-click the UuuClient.exe and select 'Run as Administrator' or create a shortcut to the 
exe on your desktop, right-click it, select *Properties* and on the *Shortcut* tab, select *Advanced...*, then check the 'Run as Administrator' checkbox and click OK.
@end

### After injecting the DLL
After you've successfully injected the dll, you'll get a series of notification windows in the top left corner of your game window which some info regarding what the UUU is doing. You can now switch to the *Available features* tab to see which features of the UUU are available with the game you're using it with. 

![The available features tab](Images\UUU\AvailablefeaturesTab.jpg){.shadowed .autosize}

Here, with Darksiders III as example game, all features are available. 

The **Game speed** can be used with the *Slomo timestop* when it's active. The **Dump object info** button can be used to dump all active object names and the addresses in memory to a text file on disk. This feature is helpful for people who want to use cheat engine with the game at hand. See for more info [the object dumping section below](universal_ue4_consoleunlocker.htm#dumping-object-addresses).

@alert Info
It might be the UUU reports some elements aren't found while the game should be fully supported. This might be caused by assembly mismatches or the timing you injected the dll into the game process. If this
happens try to inject the DLL at moment after you've loaded the level or after the game's menu has fully loaded. 
@end

## Configuration
The UUU has various settings you can configure, which you'll do on the *Configuration* tab. Additionally you can define the key-shortcuts for various functionality on the *Key bindings* tab. These are discussed below

### Configuration tab
![The configuration tab](Images\UUU\ConfigurationTab.jpg){.shadowed .autosize}

Most settings are for the built-in free camera and are self explanatory. The *Game control device* allows you to select which device to use for controlling the built-in free camera. By default it's both 'keyboard+mouse' and 'gamepad'. The device that's chosen is blocked by default to send its input to the game (as much as possible, sometimes this is unavoidable). 

#### Key selection for opening the in-game console
It might be the `~` key doesn't do anything, even though the console was created successfully by the dll. This might be caused because the game unbound the `~` key and therefore it's not possible to open the console. Additionally, you might be using a non-US keyboard, like an Azerty keyboard, and on those keyboards, the `~` key isn't above the TAB key and the engine won't recognize it. 

To correct this, on the *Configuration* tab, the setting **Key to open in-game console** allows you to select from a small set of keys what to use to open the console. By default this is 'Tilde' (`~`). Please select a key that's on your keyboard and which doesn't need Shift to be selected. E.g. on a French (Azerty) keyboard, the '$' key is a good choice, so choose in the drop down `Dollar ($)` as console key. 

### Keybindings tab
![The Keybindings tab](Images\UUU\KeybindingsTab.jpg){.shadowed .autosize}

To change a key binding, click in the textbox and press the key combination you want to use, then click the **OK** button that appeared next to the textbox when you clicked it. If you changed your mind, just click **Cancel**. You can use the same key combination for multiple features. This allows you to e.g. use `Insert` for enabling the free camera, stopping time and hiding the HUD at the same time. 

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
Insert                                    | Enable/Disable camera
HOME                                      | Lock/unlock camera movement
ALT + rotate/move                         | Faster rotate / move
Right-CTRL + rotate/move                  | Slower rotate / move
Controller Y-button + l/r-stick           | Faster rotate / move
Controller X-button + l/r-stick           | Slower rotate / move
Arrow up/down or mouse or r-stick         | Rotate camera up/down
Arrow left/right or mouse or r-stick      | Rotate camera left/right
LMB + mouse forward / backward            | Move camera up / down
RMB + mouse forward/backward              | Move camera forward / backward
LMB or RMB + mouse left / right           | Move camera left / right
LMB + RMB + mouse left / right            | Tilt camera left / right
Mousewheel                                | Increase / Decrease FoV
Numpad 8/Numpad 5 or l-stick              | Move camera forward/backward
Numpad 4/Numpad 6 or l-stick              | Move camera left / right
Numpad 7/Numpad 9 or l/r-trigger          | Move camera up / down
Numpad 1/Numpad 3 or d-pad left/right     | Tilt camera left / right
Numpad +/- or d-pad up/down               | Increase / decrease FoV
Numpad * or controller B-button           | Reset FoV
Numpad .                                  | Toggle block input to game for camera control device.

By default, when the free camera is enabled, the input to the game is blocked for the device that's controlling the camera. 
The camera will move / rotate slower when you lower the fov.

## Hotsampling

For hotsampling, or better: dynamically resize the game window to a higher resolution, the usual tool to use is [SRWE](https://github.com/dtgDTGdtg/SRWE). 
The UUU has the same functionality SRWE offers now built-in and has a handy pre-selection of resolutions generated from your monitor's native resolution, using a variety of aspect ratios. 

![The hotsampling tab](Images\UUU\HotsamplingTab.jpg){.shadowed .autosize}

Unreal Engine 4 games by default support hotsampling, as long as you run the game in Windowed mode (in DX12, borderless might also help, but usually, it's
Windowed). If you run your game as full screen, hotsampling might just stretch the game window's content but not set the game's rendering resolution to a higher resolution. 

After you've select the resolution and aspect ratio you want to use, click the **Set** button to activate it. By default the UUU will switch focus back to the game window so you can immediately take the shot. To get back to your native play resolution, you can either select it from the tree or click the **Fake fullscreen** window. 

If you want to check portions of the window that's outside your monitor, you can use the *Alignment controls* buttons, which allow you to move the window around so you can check whether all parts of the window you're about to take a shot of are properly rendered. 

## Dumping object addresses
The UUU has another feature up its sleeve: it can dump the memory locations and names of all currently active engine objects a text file in the game folder, called `UUU_Objects.txt`. To do that, on the *Available features* tab, click the **Dump object info** button. The memory addresses listed in the file differ per level and every time you run the game, so if you want to look up objects in-memory after you've loaded a new level, you have to 
dump the file again. The Objects file is useful for people who create cheat tables. 

## Games that work with the unlocker
Although the name suggests it's a universal unlocker that always works with any Unreal Engine 4 game, the reality is that developers sometimes change the game engine's code and the unlocker can't re-activate the console as essential functions aren't there anymore, or activate other features offered by the UUU. The list below are games which are known to work with the unlocker. 

@alert Info
With the release of the UUU v4, this list has been frozen. A new list of games that work with the UUU v4 is maintained [**here**](https://opm.fransbouma.com/uuuv4.htm#games-that-work-with-the-uuu). *Games on that list are not guaranteed to work with the UUU v3*.
@end

Title| Notes
--|--
9 Monkeys of Shaolin | 
10 Miles to Safety | 
103 | 
A Knight`s Quest | 
Adam - Lost Memories | 
Aefen Fall | 
Agony | 
Alan Sharp | 
Alice VR | 
Alien: Fireteam Elite | 
Amid Evil | 
Ancestors Legacy | 
Ancestors - The Humankind Odyssey | 
Ancient Knowledge | 
Another Sight Definitive Edition | 
Apsulov: End of Gods | 
Aquanox Deep Descent | 
Arboria | 
Areia: Pathway to Dawn | 
Arid | 
Arise a Simple Story | 
Armoured Onslaught | 
Aron's Adventure | Console isn't available
The Ascent | Rebind Enable camera and UWorld Pause keys to different keys than `Numpad 0` and `Insert` as the game opens the menu with these. 
Ashen | 
Ashes Of Oahu | 
Assemblance: Oversight | 
Assetto Corsa Competizione | 
Astroneer | Console isn't available
AWAY: The Survival Series | 
Azur Lane Crosswave | 
Backbone | 
Bad Boys at School | 
Bard's Tale IV: Barrows Deep | 
Bastide | 
The Battle of Visby | 
The Beast Inside | 
Bee Simulator | 
Beyond a Steel Sky | 
The Blackout Club | 
Black Legend | 
Blade of Arena | 
Blair Witch | 
Borderlands 3 | 
BPM: Bullets per minute | 
Bright Memory | Also works with the RTX tech demo
Britannic: Patroness of the Mediterranean | 
Burning Daylight | 
Call of Cthulhu | 
Call of the Sea | 
Captain Starshot | 
Castle Rock Beach, West Australia | 
Chernobylite | 
Cions of Vega | 
Close to the Sun | 
Code Vein | 
Colony Ship | 
Comanche | 
Conarium | 
Corruption 2029 | 
Crash Bandicoot 4: It's About Time | 
Creature in the Well | 
Curse of Anabelle | 
DaemonYesMachina  | 
Dark Future: Blood Red States | 
Dark Deception | 
Dark Occult | 
Dark Space Ex Machina | 
Darksiders 3 | 
Darksiders Genesis | 
Daymare: 1998 | 
Days Gone | No custom console keys
Deep Rock Galactic | Console not available
Deliver us the moon | 
Demon Skin | 
Destroy all humans | Tested on demo
Desolate | 
Devil's Hunt | 
Devolverland Expo | 
Do you copy? | 
Die young | 
Disaster Report 4: Summer Memories |  Also works with the demo
Disintegration | 
Donensbourgh | 
DRAGON BALL Z: KAKAROT | HUD toggle doesn't hide some parts of the HUD.
Dragon Quest XI: Echoes of an Elusive Age | 
Drake Hollow | 
Draugen | 
DreadOut 2 | 
Dreamo | 
Dreamscaper | Also works in Dreamscaper Prologue
Driftland | 
Drug Dealer Simulator | 
Dungeon Defenders: Awakened | 
Dwarrows | 
Earth Defence Force: Iron Rain  | 
Earthfall | 
Echo | 
Effie | 
Elea | 
Elli | 
Estranged Act II | 
Everspace | 
Everspace 2 | Tested on demo
Eximius: Seize the Frontline | 
Explore Fushimi Inari | 
Extinction | 
Fortnite | Only versions below 1.9.1 are compatible.
Fade to silence | 
Fear the Dark Unknown | 
The Fidelio Incident | 
Fighting Ex Layer |
Filament | 
Finding the Soul Orb |  
The Forgotten City | 
Freud Gate | 
Frozenheim | 
Gal Gun 2 | 
Gamedec | 
Genesis Alpha One | 
Genesis Noir | 
Ghostrunner | requires UUU 3.0.12+
Giraffe and Annika | 
Godfall | Inject the UUU at launch, before the game starts. No console.
Grand Guilds | 
Gray Dawn | 
GRIP: Combat Racing | 
Grounded | Tested on demo
Gu Lady 蛊婆 | 
Guilty Gear Strive | Pause the game before moving the camera, otherwise the characters move too.
Halflight | 
Hazel Sky | Tested on demo
Hellblade: Senua's Sacrifice | 
Hellbound | 
Hello Guest | Tested on Alpha build.
Hello Neighbor 2 | 
Hollow |
Human or Virus | 
Hunter's Arena: Legends | 
Hunting Simulator | 
Hunting Simulator 2 | 
Hypercharge Unboxed | 
Industries of Titan | 
Infliction | 
Insomnia the Ark | 
Insurgency Sandstorm | 
Intruders: Hide and Seek" | 
Iron Survival | 
Journey to the Savage Planet | 
Jumanji The Video Game | 
Jump Force (limited) | 
Kari | 
Keep Out | 
Kena: Bridge of Spirits | Use v3.0.21+
Kid a mnesia exhibition | 
Killsquad | 
Kine | 
Koral | 
Laser League | 
The Last Show of Mr. Chardish | 
Layers of Fear 2 | 
Liberty Prime | 
Life is Strange: True Colors | 
Life is Strange 2 | 
Light Tracer 2 | 
The Line | The K148 Game Studio game 'The Line'
Ling: a Road Alone  | 
Little Brother Jim | 
Little Hope | No console, camera only (v3.0.12 or lower)
Little Nightmares 2 | Console only, no camera. Use `toggledebugcamera` for camera
Lost Ember | 
Mahoe Arms | 
ManEater | HUD toggle doesn't hide the entire HUD. Console not available.
Man of Medan (The Dark Pictures Anthology) | 
Marie's Room | Built-in camera doesn't work. Use `toggledebugcamera` for camera
Marvel vs. Capcom: Infinite | 
Metamorphosis | 
Medieval Dynasty | No hud toggle
The Medium | Camera doesn't work in split-screen scenes
Mind: Path to Thalamus | 
Minecraft Dungeons | 
Monkey King: Hero Is Back | 
Monster Energy Supercross: The Official Videogame 3 | 
Monster Jam Steel Titans | 
Moons of Madness | 
Morels: The Hunt | 
Morphies Law Remorphed | 
Mortal Shell | 
MotoGP 19 | 
MotoGP 20 | 
MotoGP 21 | 
My Hero One's Justice | 
My Hero One's Justice 2 | 
Mýrdalssandur, Iceland | 
Mysteria Occult Shadows | 
Narcos: Rise of the Cartels | 
NBA 2K Playgrounds 2 | 
Necromunda Underhive Wars | No hud toggle 
Nemezis - Mysterious Journey III | 
Nephise: Ascension | 
Nero | 
Nigate Tale | 
Night of the Dead | 
No Straight Roads | 
Observer | Built-in camera isn't available.
Offroad Racing BuggyYesATVYesMoto | 
Only After | 
Operencia: The Stolen Sun | 
The Outer Worlds | HUD toggle doesn't hide the entire HUD. Use `showhud 0`
Overkill's The Walking Dead | 
Override: Mech City Brawl | 
Pagui打鬼 | 
Paper Dolls Original | 
Paradise Killer | 
Paradise Lost | 
Paranormal Activity The Lost Soul | 
港詭實錄ParanormalHK | 
Partisans 1941 | 
Past Cure | 
Pathless | No timestop/pause. Use ESC + hud toggle.
Planet Alpha | 
The Pit: Infinity | 
Pluviophile | 
Praetorians HD Remaster | 
Project Remedium | 
Project Wingman | 
Protocol | 
Psychonauts 2 | Not with Gamepass / MS Store version
Observer System Redux | Tested on demo.
Occupation | 
OCTOPATH TRAVELER | 
Omen of Sorrow | 
Omensight | 
Omno | Tested on demo
Open Country | 
Orcs Must Die 3 | 
The Otterman Empire | 
Pacer | 
Quantum Replica | 
Qube 2 | 
The Quiet Man | 
Race With Ryan | 
RAD | 
Raji: An Ancient Epic Prologue | 
Redeemer | 
Redout | 
Redout: Space Assault | 
Relicta | 
Remnant: From the Ashes | 
Remothered: Broken Porcelain | 
Remothered: Tormented Fathers | 
Ride 4 | 
Roboquest | 
Robin Hood - Sherwood Builders | 
Rock of Ages 3: Make and Break | 
Ruin 2 | 
Ruiner | 
Samurai Jack Battle Through Time | No console/timestop. Use menu + hud toggle for pause.
Samurai Showdown | No aspect ratio correction
Satisfactory | 
Scarlet Nexus | No slomo (PgDn) pause
SCUM | 
Session: Skateboarding Sim Game | 
Shadows of Larth | 
Shape of the World | 
Shenmue 3 | 
ShockRods | 
Silver Chains | 
The Sinking City | 
Sinner: Sacrifice for Redemption | 
Skylar and Plux | 
Skully | 
The Sojourn | 
SolSeraph | 
Someday You Will Return | 
Song of Horror | 
Song of Iron | 
Sophont | 
Sorrowvirus A Faceless Short Story | 
Soul Valley | 
SOULCALIBUR VI | 
Space Hulk: Deadwing Enhanced Edition | 
Space Hulk Tactics | 
Spacebourne | 
Sponge Bob Bikini Bottom Rehydrated | 
Spyro Reignited Trilogy | 
Star Wars Jedi: Fallen Order | 
Stardrop | 
Steel rats | 
Stela | 
Stories: the Path of Destinies | 
Styx 2 | 
Subdivision Infinity DX | 
Subverse | 
Succubus | 
The Suicide of Rachel Foster | 
Supraland |
Sword and Fairy 7 | 
Sword Art Online: Fatal Bullet | 
Tales of Arise | 
Tartarus | 
TASOMACHI Behind The Twilight | 
Tell Me Why | (Also with xbox gamepass version)
Terminator Resistance | 
Tetris Effect | 
Torchlight 3 | 
Tower of Fate | 
Train Sim World | 
Transient | Tested on demo
Travis Strikes Again: No More Heroes Complete Edition | 
Trials of Mana | Also works with the demo
Tribes of Midgard | 
Tropico 6 | 
Twin Mirror | 
Urban Trial Playground | 
Uventa | 
Vampyr | 
Venineth | 
Visage | 
Wartile | 
We Happy Few | Built-in camera isn't available.
We Went Back | HUD toggle doesn't toggle crosshair. Use `showhud 0`
Weakless | 
Werewolf The Apocalypse Earthblood | 
Withstand: Survival | 
What Happened | 
The Works of Mercy | 
WWE Battlegrounds | 
XING The Land Beyond | 
Xuan-Yuan Sword VII | 
ZED | 

Additionally, most [UE4 games on Itch.io](https://itch.io/games/newest/made-with-unreal-engine) are usable with the UUU. 

## Built-in functionality

The following features are build-in (and enabled if the code can be found in the game). You can configure most key bindings on the *Key bindings* tab.

See the camera section above for the controls for the camera itself

Feature | Key 
--|--
Toggle camera | `Insert`
Toggle widget based HUD / Menu elements | `Delete`
Toggle game pause (Using UWorld::IsPaused) | `Numpad 0`
Toggle game pause (Using slomo 0) | `Page Down`
Skip frames when the game is paused | `Page Up`
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

&copy;2019-2021 All rights reserved.

## Changelog

###v3.0.21:
- **FIXED**: The HUD toggle didn't always work as it matched with the wrong piece of code in some games. 

###v3.0.20:
- **FIXED**: In some engine builds the offsets of the three Aspect Ratio correction blocks were different, causing the game to show a distorted image due to the wrong offsets being used

###v3.0.19:
- **FIXED**: In newer engines pillar/letterbox black bars would still appear even though the UUU should have removed them
- **FIXED**: It could be you received an error that a named pipe couldn't be created. 

###v3.0.18:
- **CHANGED**: Rewritten AOB scanner, 10%/20% faster and won't crash the game the cases the previous scanner would. It also now shouldn't miss any AOBs anymore.

###v3.0.17:
- **FIXED**: In some cases the new AOB scanner could run into memory it shouldn't end up in and crash the game. 

###v3.0.16:
- **CHANGED**: Implemented a better AOB scanner so it should match the blocks it has to find better. 

###v3.0.15:
- **ADDED**: Special cases added for Unreal Engine v4.11 for Days Gone
- **ADDED**: Toggle on the Log tab to suppress notifications.

###v3.0.14: 
- **ADDED**: Support for Unreal Engine v4.26
- **FIXED**: Custom console keys now work again after it was broken for newer engine versions. 

###v3.0.13:
- **FIXED**: The `SET` command was readded using code which assumed a fixed length of the check block, but in some games this was a different length, causing crashes when a command was specified on the console.

###v3.0.12:
- **FIXED**: The checks for Engine Version for select v4.25 games failed, this has been corrected. 
- **CHANGED**: The AOB for the ObjectsStore could fail in some situations, it has been made less strict
- **ADDED**: The UUU now re-enables the `set` command, which is disabled in every UE4 shipped game. The `set` command allows you to set any property on any object. 

###v3.0.11:
- **FIXED**: The Engine Version checks had one wrong address marker for v4.21 like engines which could lead to the wrong version being chosen
- **ADDED**: Logging of all activity to a .log file (UniversalUE4Unlocker.dll.log) for easier debugging when things go wrong.

###v3.0.10:
- **ADDED**: Another pattern added to find the engine version in 4.24+ games. 
- **CHANGED**: Default fall-back version has been bumped from 4.16 to 4.23.

###v3.0.9:
- **ADDED**: Some v4.21 games had different instructions after the engine version write which resulted in the wrong engine version being chosen. 

###v3.0.8:
- **FIXED**: Fixed a bug where in some games the HUD toggle was found but went unnoticed so it was reported as not working
- **ADDED**: Additional AOBs to detect some v4.24 based games. 

###v3.0.7:
- **FIXED**: Fixed a crash introduced in 3.0.6 when the object store wasn't found as well as the engine version and version auto-detect assumed they were.
- **ADDED**: Additional AOBs for UE4 4.25 for object store (console support), engine version and HUD toggle.

###v3.0.6:
- **FIXED**: Added a way to intercept LockFOV in recent UE4 releases so the FOV control works again in recent games like Remnant from the Ashes. 
- **CHANGED**: The engine version is now always reported, if found. Previously this was only reported when the console was also activated. 

###v3.0.5:
- **FIXED**: Added a more solid filter for v4.25, the one added in 3.0.4 could miss a couple of variants. 

###v3.0.4:
- **FIXED**: Added better version checking so games using UE4 v4.25 are better detected.

###v3.0.3:
- **FIXED**: Fixed an issue with duplicate resolutions showing up in the hotsampling list. 

###v3.0.2: 
- **ADDED**: Mouse-based camera movement / fov control (using left/right mouse button and mousewheel)
- **ADDED**: Frameskip feature for when the game is paused (default PageUp)
- **FIXED**: A checkbox control didn't send its changed state to the dll if the state changed to 'unchecked'. 

###v3.0.1:
- **ADDED**: Added alignment buttons for the window to the Hotsampling tab, so you can examine the window contents if it's larger than your monitor
- **FIXED**: Some games matched their Objectsstore AOB with the wrong location so an alternative, better one was added.

###v3.0.0: 
- **ADDED**: Added new user interface which offers hotsampling and doesn't rely on DirectX hooking for menu display.
