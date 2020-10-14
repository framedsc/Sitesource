![The Witcher 3:Wild Hunt](Images\witcher3_header.png "Shot by jim2point0"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Ansel | Yes
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
DirectX versions | DirectX 11

Essential mods
--
* Some mods touch the same files. The script merger detects conflicts and allows you to decide which mods have priority over others. It is absolutely essential.
[https://www.nexusmods.com/witcher3/mods/484](https://www.nexusmods.com/witcher3/mods/484)

* The game keels over if you install too many mods due to a weird internal mod limit. This mod removes that limit: [https://www.nexusmods.com/witcher3/mods/3643](https://www.nexusmods.com/witcher3/mods/3643)

Mods for Visuals: Jim2point0 Edition
--
* [Immersive Lighting (nudel edition)](https://www.nexusmods.com/witcher3/mods/3953)  
Lighting Mods will probably make the biggest visual difference, but they are very subjective as to what you'll like.
* [HD Reworked](https://www.nexusmods.com/witcher3/mods/1021/)
* [Monsters Reworked](https://www.nexusmods.com/witcher3/mods/3580)
* [Elysium Grass](https://drive.google.com/file/d/1lGsFSyc3_7LitGL3csqk8ZntbAbbLWUb/view)  
    Make sure your `mod.settings` file has the following
    ```
    [mod0Elysium]
    Enabled=1
    Priority=0
    ```
* [Tweaks](https://www.nexusmods.com/witcher3/mods/2658)  
    Lets you push the graphics higher than ultra, like grass distance, density, etc.
    ```
    Recommended grass settings:
    Grass density: 6000-8000
    Grass distance SCale: 2.3
    Grass Ring Size: 33554432
    Grass Efficienty: 0.001
    ```

**Extra odds and ends**

* Beautiful Rocks: [https://www.nexusmods.com/witcher3/mods/2691](https://www.nexusmods.com/witcher3/mods/2691)  
* Oaks: [https://www.nexusmods.com/witcher3/mods/3852](https://www.nexusmods.com/witcher3/mods/3852)  
* Haystacks: [https://www.nexusmods.com/witcher3/mods/1515](https://www.nexusmods.com/witcher3/mods/1515)  
* Volumetric Clouds Over Skellige: [https://www.nexusmods.com/witcher3/mods/1302](https://www.nexusmods.com/witcher3/mods/1302)  
* High quality faces: [https://www.nexusmods.com/witcher3/mods/1024](https://www.nexusmods.com/witcher3/mods/1024)  
* Ciri Eyes: [https://www.nexusmods.com/witcher3/mods/3215](https://www.nexusmods.com/witcher3/mods/3215)  
* Yen Eyes: [https://www.nexusmods.com/witcher3/mods/2565](https://www.nexusmods.com/witcher3/mods/2565)  
* Ultimate Clouds: [https://mega.nz/file/yqpziabQ#JwJdR_9ytETCHET3GtpthVgmAcE91X24caugHQHN1GM](https://mega.nz/file/yqpziabQ#JwJdR_9ytETCHET3GtpthVgmAcE91X24caugHQHN1GM)  
* Ultimate Water: [https://mega.nz/file/CrQC0KLS#lwajFoosXm4Y2yuhG6bvfzevGKf3b0CLG3NTyFLA7W4](https://mega.nz/file/CrQC0KLS#lwajFoosXm4Y2yuhG6bvfzevGKf3b0CLG3NTyFLA7W4)  
    ```
    Ultimate water gives you higher resolution water textures and enhanced reflections. 
    The clouds do come with a performance penalty on some rigs (or so I've heard) so keep that in mind if you have relatively low performance
    ```
For screenshots:
--
* [Freecam & console](https://www.nexusmods.com/witcher3/mods/3574)  
* [Photomode2inOne](https://www.nexusmods.com/witcher3/mods/190)  
* [AMM](https://www.nexusmods.com/witcher3/mods/780)    
    ```
    AMM lets you change your appearance (as well as Roach). It will ignore whatever you're wearing so you can still look cool while using items that have the stats you want.
    ```

Time of Day Control
--
* [CE table](../CheatTables/witcher3.CT)  
Enable the script. Use the [ ] keys to change the time of day.
Hold ALT to move the time faster.
Hold CTRL to move the time slower. 

    To make the time transition smoother, in Cheat Engine, go to Edit -> settings -> hotkeys  
    Decrease keypoll interval and delay to 25-50

High Resolution Screenshots
--
If you freeze the game with Photomode2inOne, you should still be able to access the menu by pressing escape. This will allow you to bump up your resolution with DSR or another means. 

## Tips and Tricks
* When using the freecam mod, you might notice that trees\bushes behind Geralt will disappear as you fly around. That's because, when you enable the freecamera, those trees exist outside of the current camera frustum. If you want those trees or objects to stick around, you need to trick the game into thinking the camera is looking at those trees. So before you enable the freecam, rotate the in-game camera to look behind Geralt. Then when you enable the camera, those trees/objects will not disappear.


## Useful links

* [Console command list](https://commands.gg/witcher3)
* [GeForce tweak guide](https://www.geforce.com/whats-new/guides/the-witcher-3-wild-hunt-graphics-performance-and-tweaking-guide)
* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/The_Witcher_3:_Wild_Hunt)