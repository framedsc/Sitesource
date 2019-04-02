![The Witcher 3:Wild Hunt](Images\witcher3_header.png "Shot by Otis_Inf"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes
Ansel | Yes
DirectX versions | DirectX 11

## Versions
The latest build of The Witcher 3 is v1.32. However most mods work with v1.31 or v1.31A. Version 1.32 only brings 
some Chinese translation fixes but no new functionality/fixes however the version number will break a lot of mods.
It's therefore highly recommended to roll back your game to v1.31A or v1.31. 

On GoG you can do that in the GoG Galaxy client
by clicking 'More' on the game's page in your library, then selecting 'Settings'. Scrolling down you can select the version 
you want. You should also disable auto-updates to avoid having to do it all over again later on. 

For Steam, please use [the guide to rollback to a previous version of a game on steam](../GeneralGuides/steam_update_guide.htm).

### Alternative using a mod
There's also [a mod which can revert the version](https://www.nexusmods.com/witcher3/mods/3374). It might work, it might not work, with all
mods. The rollback to a previous version through the store clients is a proven method.

## Essential mods and tools

* [Debug Console Enabler](https://www.nexusmods.com/witcher3/mods/1555). This mod gives you the free camera using F1 and a console, opened with `~`
 that allows you to specify all kinds of commands. It's highly recommended to use a controller with the free camera offered by this mod, as the camera moves
way too fast when used with keyboard/mouse.
* [Photomode2in1](https://www.nexusmods.com/witcher3/mods/190). This mods adds a handy timestop and weather control, as well as other commands that 
could help you setup the perfect shot.
* [The Witcher Script Merger](https://www.nexusmods.com/witcher3/mods/484). To work with mods, you will run into conflicts, things that need to be 
loaded before the other etc. The easiest to solve this is via this tool
* [Unification patch for 1.32 - 1.31 - 1.31GOTY - 1.31A](https://www.nexusmods.com/witcher3/mods/2134). This mod makes sure other mods work with your
install no matter the version they were made for.
* [Merged Free DLC mod limit fix](https://www.nexusmods.com/witcher3/mods/3334). The engine used for The Witcher 3 has a mod limit: if you have more
mods than the limit, it simply stops loading. While there's no direct fix for this, there's a way to free up a lot of 'slots' by merging all the free DLC mods
for e.g. Ciri, Triss and Yennefer into a single mod. This mod offers all those DLC files into one single mod.

For more mods, and to completely configure the game to your liking, please visit [The Witcher 3 on Nexus](https://www.nexusmods.com/witcher3). 

## Tricks and tips 

### How to get a high resolution shot
To get a high resolution shot using a DSR resolution higher than the one you use during normal gameplay, use the following steps:

* Open the console with the `~` key
* Type `testpause`. This pauses the game.
* Unpause the game with the Photomode2in1 key (Default is numpad0). This keeps the game paused, but will allow you to access the in-game menus
* Go into the in-game menu and select a different resolution
* Setup and create your shot
* When done, go into the in-game menus again, go back to the resolution you want to play the game in
* Open the console again with `~` and type `testunpause` to resume gameplay.

@alert Important
If you start the free camera with F1 and setup a shot, you won't be able to type commands in the console. so enter `testpause` and `testunpause` before setting up a 
shot so you can scroll through previous commands with the up arrow in the console.
@end

## Helpful cheat tables

* [Time Of Day / Camera position / Unit anim speed control](..\CheatTables\witcher3.ct). This cheat table by Jim2Point0 offers control over time of day by the keyboard, 
can adjust the camera distance and height and allows you to control speed of animations of NPCs and Geralt. 

## Useful links

* [Console command list](https://commands.gg/witcher3)
* [GeForce tweak guide](https://www.geforce.com/whats-new/guides/the-witcher-3-wild-hunt-graphics-performance-and-tweaking-guide)
* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/The_Witcher_3:_Wild_Hunt)