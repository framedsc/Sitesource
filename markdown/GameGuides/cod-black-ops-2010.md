![Call of Duty- Black Ops (2010)](Images\cod_bo_2010.png "Shot by IronGauntlet"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Unknown
Custom Aspect Ratios | No
Reshade | Yes
Ansel | No
Graphics API | DirectX 9
Game version | 1.1
 
## Tools

* [Console Command Binds](https://callofduty.fandom.com/wiki/Developer_console#Call_of_Duty:_Modern_Warfare_2_and_Call_of_Duty:_Black_Ops) 

## How to set binds for commands 

Open the game directory, and open the `players` folder. Under this, open the `config.cfg` with Notepad. Locate `seta monkeytoy "1"` and set it to `seta monkeytoy "0"`. Go to the bottom of this text and type in `spu` (ignore if present). Now you can add command bindings. Type `bind (key name) "command name"` to add respective bindings.

Some useful commands:

Command | Description
--|--
`bind F3 "cg_drawGun 0"` | removes HUD
`bind F4 "cg_drawGun 1"` | returns HUD
`bind F5 "cg_fov 50"` | FOV 50
`bind F6 "cg_fov 60"` | FOV 60
`bind F7 "cg_fov 70"` | FOV 70
`bind F8 "cg_fov 80"` | FOV 80
`bind F9 "cg_fov 90"` | FOV 90
`bind F10 "cg_fov 100"` | FOV 100
`bind F11 "noclip"` | enables fly mode
`bind F12 "notarget"` | enables invisibility
`bind U "god"` | godmode/take no damage
`bind J "notarget"` | enemies will not target you

## Controls 

Hotkey | Description
--|--
`W/S` | Move camera forward / backward
`A/D` | Move camera left / right
`Q/E` | Move camera up / down

## Depth Buffer fix
You'll notice that the depth buffer might flicker a lot. To prevent this, simply disable Anti-Aliasing in the Options. Recheck the selected depth buffer if the issue persists.

@alert warning
You might experience severe stutters if you keep "Number of corpses" set to "Large". To avoid this, simply set it to "Tiny".
@end

## Useful Links

* [Original NOHUD guide by pino44io](https://nohud.fandom.com/wiki/Call_of_Duty:_Black_Ops_No_Hud)
* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Call_of_Duty:_Black_Ops)
