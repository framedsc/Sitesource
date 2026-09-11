![Game Title](Images\brothers_in_arms_rth30.png "Shot by shkegulka"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes (see tips)
Custom Aspect Ratios | No
Reshade | Yes (see tips)
Ansel | No
Graphics API | DirectX 9
Game version | <font face="Stores"> S </font> 1.11
 
## Enabling Debug Tools

This game does not have any dedicated camera tools, so we will be using Unreal Engine 2 commands for our shots.

Find the `bia.ini` file in `%APPDATA%\Gearbox Software\Brothers In Arms\<Profile_Name>` and make the following changes:

* Replace `Consolekey=0` with `Consolekey=192`
* Replace `bEnableDebugConsoleAndMenu=False` with `bEnableDebugConsoleAndMenu=True`

Save the file. Now you have access to debug tools that let you control the camera, adjust the game speed, and much more.

## Hiding HUD

Once you have debug tools enabled, press `F1` during gameplay to bring up the Debug Menu with a list of options. Select `Show/Hide HUD` there and press `Enter` to remove the HUD overlay from the screen. Doing so again will revert the changes in case you want to go back to playing the game without restarting.

Debug Menu can be unresponsive to mouse navigation and still enable the first option regardless of your selection. If that happens, re-open it and use arrow keys to navigate the list instead.

## Using Console Commands

Most of the heavy lifting while setting up a shot is done by the console. Some commands are included in the Debug Menu, but we need more than that, so you will have to type them manually or use keybinds from the next block.

Open the console by pressing `~`, then enter one of the following commands:

Command	| Description
--|--
`god` | Makes you invincible.
`ghost` | Lets you fly and clip through objects freely.
`walk` | Disables `ghost`.
`fov <value>` | Adjusts in-game FOV. `63` is the default value.
`slomo <value>` | Controls game speed. `1` is the default value, `0.1` is the lowest that works.
`playersonly` | Toggles pause for NPCs and some objects. Does not affect ragdoll, grass, rain effects, etc.

## Binding Commands to Keys

Making keyboard shortcuts for certain console commands is heavily recommended. They save a lot of time and give you way better control over the scene.

Keybinds can be added by editing `User.ini` in `%APPDATA%\Gearbox Software\Brothers In Arms\<profile_name>`. Look for a block called `[Engine.Input]` there and add a command to any key you want to use. Save the file and test the inputs in-game.

Example:

```
1=slomo 0.3
2=slomo 1
3=slomo 3
[...]
J=ghost
K=walk
L=playersonly
```

Adding these inputs will let you toggle NPC pause by pressing `L`, go in and out of ghost mode with `J`/`K`, and control the game speed with `1`/`2`/`3`.

Alternatively, you can assign commands to keys through the console itself by entering `set input <key> <command>`. However, keybinds assigned that way will be lost as soon as you return to the main menu.

@alert warning
The game can randomly reset custom inputs back to default. To avoid that, make `User.ini` read-only.
@end

## Tips and Tricks

### Solving Crashes on Startup

In some cases, installing ReShade causes the game to crash during the intro movies. If that happens, simply skip them as soon as you can, or go to `<game_path>\Media` and rename/remove `LEGAL_EN.lte` and `Logos.bik`.

### Fixing Depth Buffer

By default, ReShade doesn't detect the depth buffer correctly in this game. Thankfully, all you have to do is go to the Add-ons tab in ReShade overlay and check the following boxes:

* Use aspect ratio heuristics
* Use extended aspect ratio heuristics
* Copy depth buffer before clear operations

### Making DSR Work

The game tends to crash at resolutions higher than native when ReShade is used. There are two potential workaround to this:

* Set desktop resolution to the desired one first, then match it in the game settings.
* During gameplay, open the console with `~` and enter `setres <width>x<height>f` to change the output resolution on the fly. You can also bind this command to a key as described above.

Unfortunately, neither method gets rid of the crashes completely. Some stability issues are still to be expected, so always have backups and stick to one resolution that works best for you.

### Hiding Player Weapons

There is no reliable way to remove your own gun from the screen, but you use `playersonly` mid-animation while swapping weapons (`TAB` by default) to achieve that. Make sure to use low `slomo` values to easily catch the right moment.

## Additional Notes

* Most of the guide applies to Brothers in Arms: Earned in Blood as well. You'll find the config file in a different folder (`%APPDATA%\Gearbox Software\Earned In Blood\`) under a different name (`eib.ini` rather than `bia.ini`), but the rest of it works exactly the same.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Brothers_in_Arms:_Road_to_Hill_30)
* [Rendroc's WarZone](https://www.moddb.com/mods/rendrocs-warzone/downloads/rendrocs-warzone-and-commandmod-v438-for-rth30) (ModDB) — a massive collection of gameplay enhancements that can also be used for shots. After installation, apply them from the main menu in Chapters - Mutators.
* [Brothers in Arms Cheats](https://brothersinarms.fandom.com/wiki/Cheats) (Fandom Wiki) — the full list of cheats for the game. Not all work as expected, but you may find some of them useful.
