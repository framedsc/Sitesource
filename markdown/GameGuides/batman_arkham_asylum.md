![Batman Arkham Asylum GOTY](Images\batmanaa_header.jpg "Shot by One3rd"){.shadowed}

##Feature summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes, see note
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 9
 
##Tools
* [CE table - Camera by One3rd, Cheats by SunBeam](..\CheatTables\BatmanAA_One3rd_Camera_Merged.CT)  
**Features**: Camera Control, FoV, Tilt, HUD Toggle, Console Enabler, Cheats

##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Batman:_Arkham_Asylum)
* [HD Texture Pack + Full Game Tweaks Guide on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=1159691355) by GPUnity and EVERGREEN
* [List of Console Codes for Batman Arkham City](http://fearlessrevolution.com/viewtopic.php?t=1217) with some of these also working for the other Batman Arkham games.

##Additional Notes
* To use DSR resolutions you will need to set this in the ..\Users\USERNAME\Documents\Square Enix\Batman Arkham Asylum GOTY\BmGame\Config\BmEngine.ini file. Under the [SystemSettings] section change the resolution values to your desired DSR resolution such as:

        ResX=5120
        ResY=2880

    While there you can modifying the following settings (pulled from the Tweak Guide) to improve the graphics further.

        DepthOfField=False  
        MaxAnisotropy=16
        ShadowFilterQualityBias=0
        MinShadowResolution=32
        MaxShadowResolution=2048 
        // change to '1024' for faster performance, '3072' or above for better quality
        ShadowFadeResolution=5
        ShadowFilterRadius=5.000000
        SkeletalMeshLODBias=-1
        ParticleLODBias=-1
        // these last two settings affects LoD (Level of Details) which reduces quality of meshes and particles the further the camera is from them. Something far away doesn't need to be as detailed as something which is right in front of the camera. This is made to improve performance, but can introduce some popping. The -1 settings disable LoD altogether, which is very performance hungry!

        Press Ctrl+F and search for MemoryPools.
        Under [MemoryPools] make the following changes:

        FLightPrimitiveInteractionInitialBlockSize=1024
        FModShadowPrimitiveInteractionInitialBlockSize=1024
        // you can use higher values than that but it will makes the loading screens longer, but will reduce textures and static shadow popping.
    Remember to save the changes and set the file to read only so it doesn't get overridden. 

* For depth buffer access in Reshade you will need to use thalixte's dll. See [post #703 on Reshade.me](https://reshade.me/forum/general-discussion/4083-depth-buffer-detection-modification?start=700#32499) for details but you will need to install Reshade as normal and replace the .DLL with this new one. Make sure to set RESHADE_DEPTH_INPUT_IS_REVERSED=0 and tick the following settings under the DX9 menu.

        Preserve depth buffer from being cleared
        Auto preserve
        find best depthstencil based on vertices

* Useful keybinds can be added to ..\Users\USERNAME\Documents\Square Enix\Batman Arkham Asylum GOTY\BmGame\Config\BmInput.ini file at the end of the [Engine.PlayerInput] section. Set the file to read only.

        Bindings=(Name="F1",Command="God")
        Bindings=(Name="F1",Command="ToggleEnemiesCanAttack",Alt=True)
        Bindings=(Name="F2",Command="Fly")
        Bindings=(Name="F2",Command="Walk",Alt=True)
        Bindings=(Name="F3",Command="PlayersOnly")
        Bindings=(Name="F3",Command="Ghost",Alt=True)
        Bindings=(Name="F4",Command="ToggleDebugCamera")
        Bindings=(Name="F5",Command="Slomo 0.3")
        Bindings=(Name="F5",Command="Slomo 1",Alt=True)

* Cheat Table Notes
    1. Run the game till main menu, open up Cheat Engine, target ShippingPC-BmGame.exe game process.
    2. Activate [Console] item and the sub-section expands. Activate Fetch UE3 Pointers/Addresses script to fetch the required GNames and GObjects pointers. 
    3. Activate Enable Console script.
    4. Activate Set Hook & Emulate RCheatManager UObject script and leave it enabled.
    5. In-game, open up the console with Tilde key and type in a command (e.g.: fly). You'll see you can now fly around.
    6. The Debug Camera works in this one, just type in ToggleDebugCamera in the console. Once activated:

        Key | Command
        --|--
        I | ToggleLookInvert (changing mouse vertical orientation)
        Esc/Pause | to freeze/unfreeze game