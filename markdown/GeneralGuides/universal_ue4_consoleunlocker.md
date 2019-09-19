Universal Unreal Engine 4 Console Unlocker
=============

For Unreal Engine 4 powered games, it's possible to re-create the in-game console that's usually stripped out when the game is build for shipping. To do so, 
you can use the Universal UE4 Console Unlocker / Dumper dll (comes with injector exe and readme). After adjusting the .ini file for the right exe to inject the 
dll in, it should show a console window that it has found all offsets and the console object has been created as well as that cheats have been enabled. 

@alert important
The game's exe as well as the IGCSInjector.exe have to be run as *administrator*. Right-click the exe's to run and select 'Run as Administrator' or create a shortcut to the 
exe on your desktop, right-click it, select *Properties* and on the *Shortcut* tab, select *Advanced...*, then check the 'Run as Administrator' checkbox and click OK. 
@end

## Setting up the injector
After downloading the zip linked below, unpack it in an empty folder and copy the contents of the folder to the folder of the game you want to use it with. Open the included
IGCSInjector.ini in notepad and change `YOURGAME-Win64-Shipping.exe` on the line with `Process=YOURGAME-Win64-Shipping.exe` to the .exe of the game you're running. 
To determine which exe to specify, please run the game, then open Windows Task Explorer (ctrl-shift-esc) and on the 'details' tab look for the exe of your game. 

### Example: Darksiders 3
So as an example we'll use Darksiders 3. The executable you're starting of Darksiders 3 is called 'darksiders3.exe', but the exe of the game is called 
`Darksiders3-Win64-Shipping.exe`. You can see that in Windows Task Explorer as that's the exe which has a high CPU / GPU usage. So in my ini file I'll then fill in the name
of the second process and it all becomes:

```ini
[InjectionData]
Process=Darksiders3-Win64-Shipping.exe
Dll=UniversalUE4UnlockerDumper.dll
```

### If the injector doesn't work
Some people on Windows 7 have reported issues with the IGCSInjector. If that happens, please try another dll injector, e.g. Extreme Injector. 

## After injecting the DLL
When you've successfully injected the dll, you'll get a console window which says, if everything went OK, that the cheats have been enabled and the console object
has been created. Go back to the game and press the `~` key (it's the key above the `TAB` key on your keyboard). This should give a small line at the bottom of the 
game screen in which you can type commands. If you type the `~` again you'll get a larger console window which also shows the response of the game on your commands. 

To do useful things like toggle the debug camera, you first have to enable the cheats in the game. To do this, type `EnableCheats 1` in the console and hit <enter>. After 
that, type `toggledebugcamera` after you've loaded a level. This should give you the ability to move the camera around using your controller and WASD + mouse.

To go back to the game, type again `toggledebugcamera` in the console or simply press cursor UP to go to a previous command. There are many commands to choose from. Not all
of them work. E.g. `god` or `fly` might say they're activated but chances are they're not doing anything. Commands like `fov 50` (to set the FoV to 50 degrees, default is 
likely 80), `pause` (to toggle the pause of the game) and a lot of console variables do work. 

## What to do when the console doesn't open
It might be the `~` key doesn't do anything, even though the console was created successfully by the dll. This might be caused because the game unbound the `~` key
and therefore it's not possible to open the console. However it's easy to correct this. Follow these steps

* In explorer go to: `c:\users\<your username>\AppData\Local\<game name>\Saved\Config\WindowsNoEditor`
* open Input.ini
* Add (pay attention to the empty line, that has to be there):
```

[/Script/Engine.InputSettings]
ConsoleKey=Tilde
```
* Save and set the file to readonly. You can also set it to another key, e.g. K. 

## Dumping names / object addresses
The unlocker has another feature up its sleeve: it can dump two text files in the game folder called UE4Tools_Names.txt and UE4Tools_Objects.txt. To do that, press **Numpad /**.
The Names file contains all names of all objects in the game. Most of them aren't really useful, but some are, e.g. if you open the file in a text editor and search for " sg." 
you find all settings variables for things you can also set in the game menu, only these accept higher values. Another one is " r." to find all render variables. 

The Objects text file shows all objects in the engine, and their addresses in memory. These memory addresses differ per level, so if you want to look up objects in-memory
after you've loaded a new level, you have to dump the files again. The Objects file is useful for people who create cheat tables. 

## Games that work with the unlocker
Although the name suggests it's a universal unlocker that always works with any Unreal Engine 4 game, the reality is that developers sometimes change the game engine's code
and the unlocker can't re-activate the console as essential functions aren't there anymore. The list below are games which are known to work with the unlocker. 

* Agony
* Alice VR
* Ancestors Legacy
* Ancestors - The Humankind Odyssey
* Another Sight Definitive Edition
* Apsulov: End of Gods
* Asemblance: Oversight
* Ashes Of Oahu
* Bard's Tale IV: Barrows Deep
* The Blackout Club
* Blair Witch
* Borderlands 3
* Bright Memory
* Burning Daylight
* Call of Cthulhu
* Captain Starshot
* Close to the Sun
* Conarium
* Creature in the Well
* Dark Future: Blood Red States
* Dark Deception
* Dark Occult
* Darksiders 3
* Deep Rock Galactic
* Deliver Us The Moon
* Desolate
* Devil's Hunt
* Donensbourgh
* Draugen
* Dreamscaper
* Driftland
* Earthfall
* Echo
* Elea
* Extinction
* Fade to silence
* The Fidelio Incident
* Fighting Ex Layer
* Genesis Alpha One
* Gray Dawn
* Hellblade: Senua's Sacrifice
* Hollow
* Hunting Simulator
* Insomnia the Ark
* Jump Force (limited)
* Killsquad
* Koral
* Laser League
* Layers of Fear 2
* Ling: a Road Alone 
* Man of Medan (The Dark Pictures Anthology)
* Marvel vs. Capcom: Infinite
* Monster Jam Steel Titans
* Morphies Law Remorphed
* MotoGP 19
* Mutant Year Zero: Road to Eden
* NBA 2K Playgrounds 2
* Nephise: Ascension
* Observer
* Operencia: The Stolen Sun
* Overkill's The Walking Dead
* Paranormal Activity The Lost Soul
* Past Cure
* Planet Alpha
* Project Remedium
* Protocol
* Occupation
* Omen of Sorrow
* Omensight
* Quantum Replica
* RAD
* Redeemer
* Remnant: From the Ashes
* Remothered: Tormented Fathers
* Ruiner
* The Sinking City
* Session: Skateboarding Sim Game
* Shape of the World
* Silver Chains
* Sinner: Sacrifice for Redemption
* Skylar and Plux
* SolSeraph
* Sophont
* Soul Valley
* Space Hulk: Deadwing Enhanced Edition
* Space Hulk Tactics
* Spyro Reignited Trilogy
* Stardrop
* Steel rats
* Stories: the Path of Destinies
* Styx 2
* Subdivision Infinity DX
* Supraland
* Tartarus
* Tower of Fate
* Train Sim World
* Tropico 6
* Urban Trial Playground
* Uventa
* Visage
* Wartile
* XING The Land Beyond
* ZED

## Downloading the unlocker

* [Universal UE4 Unlocker v1.0.13](https://mega.nz/#!xExGzIpJ!BAEOjKWiC4VkK1JR2rtXqylgbjwfDpo_xSzEa4BtdF8)

## Troubleshooting
You might get an error with older games that it can't find the EngineVersion key and it will fall back to the default version. 
When that happens, the unlocker will try to auto-detect which engine version is being used. If that fails, it's likely not going to work out however. 
If it succeeds, the console can be created most likely. 

If you get AOB errors when injecting the dll, it might be the engine's code hasn't been fully initialized yet and AOB scanning can't
find it. Simply load a level and try again by pressing `CTRL+END`. 

If the game crashes when injecting the unlocker, try to inject it when a level is loaded. 

## Credits

The Universal Unreal Engine 4 Unlocker / dumper was created by Otis_Inf and SunBeam. Dumper code is based on the SDK generator by Kn4ck3r. 
Special thanks to Pino44io for testing.