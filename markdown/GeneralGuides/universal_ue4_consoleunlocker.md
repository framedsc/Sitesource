Universal Unreal Engine 4 Unlocker
=============

![UUU Logo by Ichisake](Images\UUU\UUULogo.jpg){.shadowed }

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

* [Universal UE4 Unlocker v3.0.19](https://mega.nz/file/JQgmmTDQ#JicdedqwrbiCwj-DzfOIgJUD-HiKphSlO8Ppvkvqwfc). 
* [Universal UE4 Unlocker v3.0.14](https://mega.nz/file/8Y50GRCS#Sg3A_v5rLeCiI6a4Xppi0RI1gwWDkoU4qjEwV3_g9Eg). Use this version if v3.0.19 gives problems


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

@alert Info
It might be the UUU reports some elements aren't found while the game should be fully supported. This might be caused by assembly mismatches or the timing you injected the dll into the game process. If this
happens try to inject the DLL at moment after you've loaded the level or after the game's menu has fully loaded. 
@end

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

![The hotsampling tab](Images\UUU\HotsamplingTab.jpg){.shadowed}

Unreal Engine 4 games by default support hotsampling, as long as you run the game in Windowed mode (in DX12, borderless might also help, but usually, it's
Windowed). If you run your game as full screen, hotsampling might just stretch the game window's content but not set the game's rendering resolution to a higher resolution. 

After you've select the resolution and aspect ratio you want to use, click the **Set** button to activate it. By default the UUU will switch focus back to the game window so you can immediately take the shot. To get back to your native play resolution, you can either select it from the tree or click the **Fake fullscreen** window. 

If you want to check portions of the window that's outside your monitor, you can use the *Alignment controls* buttons, which allow you to move the window around so you can check whether all parts of the window you're about to take a shot of are properly rendered. 

## Dumping object addresses
The UUU has another feature up its sleeve: it can dump the memory locations and names of all currently active engine objects a text file in the game folder, called `UUU_Objects.txt`. To do that, on the *Available features* tab, click the **Dump object info** button. The memory addresses listed in the file differ per level and every time you run the game, so if you want to look up objects in-memory after you've loaded a new level, you have to 
dump the file again. The Objects file is useful for people who create cheat tables. 

## Games that work with the unlocker
Although the name suggests it's a universal unlocker that always works with any Unreal Engine 4 game, the reality is that developers sometimes change the game engine's code and the unlocker can't re-activate the console as essential functions aren't there anymore, or activate other features offered by the UUU. The list below are games which are known to work with the unlocker. 

Title| UUU v3| UUU v4 | Notes
--|--
10 Miles to Safety | X | X | 
103 | X | X | 
A Knight`s Quest | X | X | 
Adam - Lost Memories | X | X | 
Aefen Fall | X | X | 
Agony | X | X | 
Alan Sharp | X | X | 
Alice VR | X | X | 
Alien: Fireteam Elite | X | X | 
Amid Evil | X | X | 
Ancestors Legacy | X | X | 
Ancestors - The Humankind Odyssey | X | X | 
Ancient Knowledge | X | X | 
Another Sight Definitive Edition | X | X | 
Apsulov: End of Gods | X | X | 
Aquanox Deep Descent | X | X | 
Arboria | X | X | 
Areia: Pathway to Dawn | X | X | 
Arid | X | X | 
Arise a Simple Story | X | X | 
Armoured Onslaught | X | X | 
Aron's Adventure | X | X | Console isn't available
The Ascent | X | X | Rebind Enable camera and UWorld Pause keys to different keys than `Numpad 0` and `Insert` as the game opens the menu with these. 
Ashen | X | X | 
Ashes Of Oahu | X | X | 
Assemblance: Oversight | X | X | 
Assetto Corsa Competizione | X | X | 
Astroneer | X | X | Console isn't available
Azur Lane Crosswave | X | X | 
Backbone | X | X | 
Bad Boys at School | X | X | 
Bard's Tale IV: Barrows Deep | X | X | 
Bastide | X | X | 
The Battle of Visby | X | X | 
The Beast Inside | X | X | 
Bee Simulator | X | X | 
Beyond a Steel Sky | X | X | 
The Blackout Club | X | X | 
Black Legend | X | X | 
Blade of Arena | X | X | 
Blair Witch | X | X | 
Borderlands 3 | X | X | 
BPM: Bullets per minute | X | X | 
Bright Memory | X | X | Also works with the RTX tech demo
Britannic: Patroness of the Mediterranean | X | X | 
Burning Daylight | X | X | 
Call of Cthulhu | X | X | 
Call of the Sea | X | X | 
Captain Starshot | X | X | 
Castle Rock Beach, West Australia | X | X | 
Chernobylite | X | X | 
Cions of Vega | X | X | 
Close to the Sun | X | X | 
Code Vein | X | X | 
Colony Ship | X | X | 
Comanche | X | X | 
Conarium | X | X | 
Corruption 2029 | X | X | 
Crash Bandicoot 4: It's About Time | X | X | 
Creature in the Well | X | X | 
Curse of Anabelle | X | X | 
Daemon X Machina  | X | X | 
Dark Future: Blood Red States | X | X | 
Dark Deception | X | X | 
Dark Occult | X | X | 
Dark Space Ex Machina | X | X | 
Darksiders 3 | X | X | 
Darksiders Genesis | X | X | 
Daymare: 1998 | X | X | 
Days Gone | X | X | No custom console keys
Deep Rock Galactic | X | X | 
Deliver us the moon | X | X | 
Destroy all humans | X | X | Tested on demo
Desolate | X | X | 
Devil's Hunt | X | X | 
Devolverland Expo | X | X | 
Do you copy? | X | X | 
Die young | X | X | 
Disaster Report 4: Summer Memories | X | X |  Also works with the demo
Disintegration | X | X | 
Donensbourgh | X | X | 
DRAGON BALL Z: KAKAROT | X | X | HUD toggle doesn't hide some parts of the HUD.
Dragon Quest XI: Echoes of an Elusive Age | X | X | 
Drake Hollow | X | X | 
Draugen | X | X | 
DreadOut 2 | X | X | 
Dreamo | X | X | 
Dreamscaper | X | X | Also works in Dreamscaper Prologue
Driftland | X | X | 
Drug Dealer Simulator | X | X | 
Dungeon Defenders: Awakened | X | X | 
Dwarrows | X | X | 
Earth Defence Force: Iron Rain  | X | X | 
Earthfall | X | X | 
Echo | X | X | 
Effie | X | X | 
Elea | X | X | 
Elli | X | X | 
Estranged Act II | X | X | 
Everspace | X | X | 
Everspace 2 | X | X | Tested on demo
Eximius: Seize the Frontline | X | X | 
Explore Fushimi Inari | X | X | 
Extinction | X | X | 
Fortnite | X | X | Only versions below 1.9.1 are compatible.
Fade to silence | X | X | 
Fear the Dark Unknown | X | X | 
The Fidelio Incident | X | X | 
Fighting Ex Layer |
Filament | X | X | 
Finding the Soul Orb | X | X |  
The Forgotten City | X | X | 
Freud Gate | X | X | 
Frozenheim | X | X | 
Gal Gun 2 | X | X | 
Genesis Alpha One | X | X | 
Genesis Noir | X | X | 
Ghostrunner | X | X | requires UUU 3.0.12+
Giraffe and Annika | X | X | 
Godfall | X | X | Inject the UUU at launch, before the game starts. No console.
Grand Guilds | X | X | 
Gray Dawn | X | X | 
GRIP: Combat Racing | X | X | 
Grounded | X | X | Tested on demo
Gu Lady 蛊婆 | X | X | 
Guilty Gear Strive | X | X | Pause the game before moving the camera, otherwise the characters move too.
Halflight | X | X | 
Hazel Sky | X | X | Tested on demo
Hellblade: Senua's Sacrifice | X | X | 
Hellbound | X | X | 
Hello Guest | X | X | Tested on Alpha build.
Hello Neighbor 2 | X | X | 
Hollow |
Human or Virus | X | X | 
Hunter's Arena: Legends | X | X | 
Hunting Simulator | X | X | 
Hunting Simulator 2 | X | X | 
Hypercharge Unboxed | X | X | 
Industries of Titan | X | X | 
Infliction | X | X | 
Insomnia the Ark | X | X | 
Insurgency Sandstorm | X | X | 
Intruders: Hide and Seek" | X | X | 
Iron Survival | X | X | 
Journey to the Savage Planet | X | X | 
Jumanji The Video Game | X | X | 
Jump Force (limited) | X | X | 
Kari | X | X | 
Keep Out | X | X | 
Killsquad | X | X | 
Kine | X | X | 
Koral | X | X | 
Laser League | X | X | 
The Last Show of Mr. Chardish | X | X | 
Layers of Fear 2 | X | X | 
Liberty Prime | X | X | 
Life is Strange 2 | X | X | 
Light Tracer 2 | X | X | 
The Line | X | X | The K148 Game Studio game 'The Line'
Ling: a Road Alone  | X | X | 
Little Brother Jim | X | X | 
Little Hope | X | X | No console, camera only (v3.0.12 or lower)
Little Nightmares 2 | X | X | Console only, no camera. Use `toggledebugcamera` for camera
Lost Ember | X | X | 
Mahoe Arms | X | X | 
Man Eater | X | X | HUD toggle doesn't hide the entire HUD. Use `showhud 0`
Man of Medan (The Dark Pictures Anthology) | X | X | 
Marie's Room | X | X | Built-in camera doesn't work. Use `toggledebugcamera` for camera
Marvel vs. Capcom: Infinite | X | X | 
Metamorphosis | X | X | 
Medieval Dynasty | X | X | No hud toggle
The Medium | X | X | Camera doesn't work in split-screen scenes
Mind: Path to Thalamus | X | X | 
Minecraft Dungeons | X | X | 
MotoGP 20 | X | X | 
Monkey King: Hero Is Back | X | X | 
Monster Energy Supercross: The Official Videogame 3 | X | X | 
Monster Jam Steel Titans | X | X | 
Moons of Madness | X | X | 
Morels: The Hunt | X | X | 
Morphies Law Remorphed | X | X | 
Mortal Shell | X | X | Tested on beta
MotoGP 19 | X | X | 
My Hero One's Justice | X | X | 
My Hero One's Justice 2 | X | X | 
Mýrdalssandur, Iceland | X | X | 
Mysteria Occult Shadows | X | X | 
Narcos: Rise of the Cartels | X | X | 
NBA 2K Playgrounds 2 |
Necromunda Underhive Wars | X | X | No hud toggle 
Nemezis - Mysterious Journey III | X | X | 
Nephise: Ascension | X | X | 
Nigate Tale | X | X | 
Night of the Dead | X | X | 
No Straight Roads | X | X | 
Observer | X | X | Built-in camera isn't available.
Offroad Racing Buggy X ATV X Moto | X | X | 
Only After | X | X | 
Operencia: The Stolen Sun | X | X | 
The Outer Worlds | X | X | HUD toggle doesn't hide the entire HUD. Use `showhud 0`
Overkill's The Walking Dead | X | X | 
Override: Mech City Brawl | X | X | 
Pagui打鬼 | X | X | 
Paper Dolls Original | X | X | 
Paradise Killer | X | X | 
Paradise Lost | X | X | 
Paranormal Activity The Lost Soul | X | X | 
港詭實錄ParanormalHK | X | X | 
Partisans 1941 | X | X | 
Past Cure | X | X | 
Pathless | X | X | No timestop/pause. Use ESC + hud toggle.
Planet Alpha | X | X | 
The Pit: Infinity | X | X | 
Pluviophile | X | X | 
Praetorians HD Remaster | X | X | 
Project Remedium | X | X | 
Project Wingman | X | X | 
Protocol | X | X | 
Psychonauts 2 | X | X | 
Observer System Redux | X | X | Tested on demo.
Occupation | X | X | 
OCTOPATH TRAVELER | X | X | 
Omen of Sorrow | X | X | 
Omensight | X | X | 
Omno | X | X | Tested on demo
Open Country | X | X | 
Orcs Must Die 3 | X | X | 
The Otterman Empire | X | X | 
Pacer | X | X | 
Quantum Replica | X | X | 
Qube 2 | X | X | 
The Quiet Man | X | X | 
Race With Ryan | X | X | 
RAD | X | X | 
Raji: An Ancient Epic Prologue | X | X | 
Redeemer | X | X | 
Redout | X | X | 
Redout: Space Assault | X | X | 
Relicta | X | X | 
Remnant: From the Ashes | X | X | 
Remothered: Broken Porcelain | X | X | 
Remothered: Tormented Fathers |
Ride 4 | X | X | 
Roboquest | X | X | 
Rock of Ages 3: Make and Break | X | X | 
Ruin 2 | X | X | 
Ruiner | X | X | 
Samurai Jack Battle Through Time | X | X | No console/timestop. Use menu + hud toggle for pause.
Samurai Showdown | X | X | No aspect ratio correction
Satisfactory | X | X | 
Scarlet Nexus | X | X | No slomo (PgDn) pause
SCUM | X | X | 
Session: Skateboarding Sim Game | X | X | 
Shadows of Larth | X | X | 
Shape of the World | X | X | 
Shenmue 3 | X | X | 
ShockRods | X | X | 
Silver Chains | X | X | 
The Sinking City | X | X | 
Sinner: Sacrifice for Redemption | X | X | 
Skylar and Plux | X | X | 
Skully | X | X | 
The Sojourn | X | X | 
SolSeraph | X | X | 
Someday You Will Return | X | X | 
Song of Horror | X | X | 
Sophont | X | X | 
Sorrowvirus A Faceless Short Story | X | X | 
Soul Valley | X | X | 
SOULCALIBUR VI | X | X | 
Space Hulk: Deadwing Enhanced Edition | X | X | 
Space Hulk Tactics | X | X | 
Spacebourne | X | X | 
Sponge Bob Bikni Bottom Rehydrated | X | X | 
Spyro Reignited Trilogy | X | X | 
Star Wars Jedi: Fallen Order | X | X | 
Stardrop | X | X | 
Steel rats | X | X | 
Stela | X | X | 
Stories: the Path of Destinies | X | X | 
Styx 2 | X | X | 
Subdivision Infinity DX | X | X | 
Subverse | X | X | 
The Suicide of Rachel Foster | X | X | 
Supraland | X | X | 
Sword Art Online: Fatal Bullet | X | X | 
Tartarus | X | X | 
TASOMACHI Behind The Twilight | X | X | 
Tell Me Why | X | X | (Also with xbox gamepass version)
Terminator Resistance | X | X | 
Tetris Effect | X | X | 
Torchlight 3 | X | X | 
Tower of Fate | X | X | 
Train Sim World | X | X | 
Transient | X | X | Tested on demo
Travis Strikes Again: No More Heroes Complete Edition | X | X | 
Trials of Mana | X | X | Also works with the demo
Tribes of Midgard | X | X | 
Tropico 6 | X | X | 
Twin Mirror | X | X | 
Urban Trial Playground | X | X | 
Uventa | X | X | 
Vampyr | X | X | 
Venineth | X | X | 
Visage | X | X | 
Wartile | X | X | 
We Happy Few | X | X | Built-in camera isn't available.
We Went Back | X | X | HUD toggle doesn't toggle crosshair. Use `showhud 0`
Weakless | X | X | 
Werewolf The Apocalypse Earthblood | X | X | 
Withstand: Survival | X | X | 
What Happened | X | X | 
The Works of Mercy | X | X | 
WWE Battlegrounds | X | X | 
XING The Land Beyond | X | X | 
Xuan-Yuan Sword VII | X | X | 
ZED | X | X | 

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
