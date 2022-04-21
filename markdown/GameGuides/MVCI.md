![Marvel vs. Capcom: Infinite](Images\MVCI.png "Shot by One3rd"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 11
 
##Tools
* [CE table - Camera by One3rd](..\CheatTables\MVCI_One3rd.CT)  
**Features**: Camera Control, FoV, Tilt, Timestop
* [HUD Toggle](https://mega.nz/#!qMIQUQwC!RwVOwzeF_XRPmmo5OO-XUEq8S6PlLRGQb6XFow0VJqQ)  
**Features**: HUD Toggle, Effects Toggle

##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Marvel_vs._Capcom:_Infinite)

##Additional Notes

* To remove Chromatic Aberration add the following to the end of the Engine.ini file located at ..\Steam\steamapps\common\MARVEL VS. CAPCOM INFINITE\MVCI\Saved\Config\WindowsNoEditor
    ```
    [SystemSettings]
    r.SceneColorFringe.Max=0
    r.SceneColorFringeQuality=0
    r.VSync=0
    ```
* Cheat Table Notes
    1. The anti cheat shuts down the game when Cheat Engine is opened. To get around this you can use a hex editor (such as [HxD](https://mh-nexus.de/en/hxd/)) to change any references to "Cheat Engine" in the application. Open "cheatengine-x86_64.exe" in HxD, search and replace for "Cheat Engine" replacing it with "i like cats!". There should be around 128 occurrences replaced. Save to a new filename such as "ilikecats.exe" and use this instead of the normal Cheat Engine application.
    2. When using this to attach the table to the game there may be two choices for MVCI.exe in the process list. Select one and if the "static z" addresses in the table show a value instead of ?? then that is the correct process, if not try the other one.
    3. Camera can be enable and disabled at any time with [Page Down]. Controlled with the keypad keys as shown in the table.
    4. You can use the main pause menu as timestop and then remove the HUD with the HUD toggle key [NUMPAD DECIMAL] or use the Pause script with [P]. Pause now works in cutscenes.
          Key | Command
        --|--
        P | Pause / Unpause
    5. You can use Cheat Engines speedhack to slow down the game. Go to Edit > Settings > Hotkeys and assign values and keys to Speedhack speed1, Speedhack speed2, etc...

* HUD Toggle Notes
    1. HUD toggle is disabled using 3DMigoto. Extract the HUD Toggle files and copy everything into the games ..\Steam\SteamApps\common\MARVEL VS. CAPCOM INFINITE\MVCI\Binaries\Win64 folder.
    2. The HUD Toggle freezes what looks to be the AO shader so when using this you will notice the AO doesn't update when the camera moves. To fix this just enable the HUD and then disable again once you have setup your shot. This will do the same thing on a window resize so if using SRWE for resolution changes you will need to enable then disable the HUD again otherwise the characters will be dark.


        Key | Command
        --|--
        NUMPAD DECIMAL | Toggle Main Pause Menu and in-game HUD elements
        1, 2, 3 | Toggle specific effects