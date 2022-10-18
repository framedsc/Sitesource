![Header](..\Images\MiscGuides\uwp_reshade_header.png){.shadowed .autosize}
 
This guide will help you to inject ReShade into most Universal Windows Platform games, i.e. Windows Store & PC Game Pass games. Please note that this won't work in every UWP game since some are protected (like *Forza Horizon 4*, which shuts down upon .dll injection).
 
## Tools
 
You will need [crosire's DLL injector](https://reshade.me/downloads/inject64.exe).

OR

You can use the [Reshade installer from the official site](https://reshade.me/).

### Using Reshade with Xbox App/Game Pass Installs
In the past getting Reshade and UWP to cooperate has required multiple steps of varying difficulty, however Microsoft has since changed their processes to allow direct access to game files for all users by default. As a result, the steps required to get Reshade working on Game Pass games is much less complicated.

The steps may vary slightly but the basics remain consistent:

1. Define your install path. You can set this by clicking on the profile icon in the top left of the xbox app> Settings > General, Under the section _Game Install Options_ you can set the game folder destination. Install as normal.
2. Depending on which method you intend to use, the next step will either be:
   * Manual Install - Place the files in the same folder as the game's .exe
   * Reshade Installer - launch the installer guide and browse to the game folders, from here you will need to locate ```gamelaunchhelper.exe``` as trying to use the game's own .exe will most likely produce an error.

Once you've successfully situated Reshade, launch the game and you should be able to use it as normal.

@alert warning
Be advised that there are some minor compatibility issues with Reshade on UWP games. The most notable is that inputs into the Reshade UI will duplicate (Clicks registering twice, typing into entry fields enters the value multiple times etc). These issues are minor and easily worked aroud, but they are known to occur.
@end

### ReshadeForUWP tool
Alternatively, [this tool with a GUI](https://github.com/MilkyDeveloper/ReshadeForUWP) can help to inject Reshade into UWP / PC Game Pass games with little manual intervention. It asks you for the package name (and the custom process name, if any) and gets the metadata of the game through the `appxmanifest.xml` file. It then generates a BAT file to inject Reshade into the game and then launch it. Optionally, it also bootstraps a working Reshade install by downloading / extracting all of the FX files and generates the Reshade.ini file.

@alert info
The content below may still be valid in certain instances but is largely considered out of date. We recommend you follow the instructions above when trying to configure Reshade for UWP games. We have left the guidance below in case an alternate method is required
@end.

## How to inject ReShade into an UWP game
 
* Extract the zip containing the UWP Injector in a folder on your desktop or drive (e.g.: ReShadeUWP).
* Start the game you would like to use ReShade in.
* Open Task Manager and check the process name used by the game (e.g.: `MoonMan-Win64-Shipping.exe` for *Deliver Us The Moon*).
* Close the game.
* Open a command prompt and navigate to the folder where the UWP Injector resides (you can write `cmd` in the address bar and it will open a command prompt there).
* Type `inject.exe name_of_the_process.exe`.
* Start the game.
 
ReShade should now be injected.
 
# Advanced UWP ReShade Injection
 
If you find the process above too tedious since you have to do it every time you launch a game, you can instead follow these steps to make a script that automatically launches the game and injects Reshade.
 
## Preparation
 
* Extract the zip containing the UWP Injector in a folder on your Desktop or drive (e.g.: ReShadeUWP).
* Create a new folder and name it like the game (e.g.: ReShade-DeliverUsTheMoon), copy the contents previously unzipped in that folder.
* If you previously installed ReShade in a Steam game you can copy the Shaders and Textures in a specific folders (see ReShade Repository for more)
 
## Find the game executable and Application ID
 
* Download the game via Windows Store or XBOX Game Pass App
* If a link is available on the desktop right click on it and note the Target (eg: WiredProductions.DeliverUsTheMoon...)
* In PowerShell, type `get-appxpackage > C:\Users\<Your UserName>\Desktop\UWP_Apps_List.txt`
* Open the file and search for the Target previously noted
* You should find this:
 
```
Name              : WiredProductions.DeliverUsTheMoonWin10
Publisher         : CN=5D8B0615-AEFA-4F14-AD65-C4F7D3A73F91
Architecture      : X64
ResourceId        : 
Version           : 1.4.44.0
PackageFullName   : WiredProductions.DeliverUsTheMoonWin10_1.4.44.0_x64__hxzk6evwjr6sy
InstallLocation   : C:\Program Files\WindowsApps\WiredProductions.DeliverUsTheMoonWin10_1.4.44.0_x64__hxzk6evwjr6sy
IsFramework       : False
PackageFamilyName : WiredProductions.DeliverUsTheMoonWin10_hxzk6evwjr6sy
PublisherId       : hxzk6evwjr6sy
IsResourcePackage : False
IsBundle          : False
IsDevelopmentMode : False
NonRemovable      : False
Dependencies      : {Microsoft.DirectXRuntime_9.29.952.0_x64__8wekyb3d8bbwe, Microsoft.VCLibs.140.00.UWPDesktop_14.0.29016.0_x64__8wekyb3d8bbwe}
IsPartiallyStaged : False
SignatureKind     : Store
Status            : Ok
```
 
* Note the PackageFamilyName. In this case: `WiredProductions.DeliverUsTheMoonWin10_hxzk6evwjr6sy`
* Go to the InstallLocation by copying and pasting it in Explorer (`C:\Program Files\WindowsApps\WiredProductions.DeliverUsTheMoonWin10_1.4.44.0_x64__hxzk6evwjr6sy`)
* Open the `appxmanifest.xml` and note the Application ID (Application Id="App")
* Go to the folder where the game executable resides. In this case: `C:\Program Files\WindowsApps\WiredProductions.DeliverUsTheMoonWin10_1.4.44.0_x64__hxzk6evwjr6sy\MoonMan\Binaries\Win64\`
* Note the exe -> MoonMan-Win64-Shipping.exe

@alert Important
If you encounter files with a padlock on them, you will not be able to use the injection process as the game is memory-protected.
@end

 
## Create your PowerShell injection script
 
* Start PowerShell ISE
* In the Script part start with `CD\` and press enter
* If the ReShade folder resides on a drive other than C:, write its drive letter and press enter
* Now write CD and the folder where the ReShade injector resides (`CD D:\ReShadeUWP`)
* Type `start-process -filepath inject.exe` followed the game executable name (`Start-Process -FilePath inject.exe MoonMan-Win64-Shipping.exe`)
* You will need to start another explorer process in order to start the game. So go on and type `Start-Process -filepath explorer.exe shell:appsFolder\PackageFamilyName!Application Id`
* Your injection and start script is ready
 
Your script should looks like this
 
```
Cd\ 
D:
Cd 'D:\ReShade-DeliverUsTheMoon\' 
Start-Process -FilePath inject.exe MoonMan-Win64-Shipping.exe
Start-Process -filepath explorer.exe shell:appsFolder\WiredProductions.DeliverUsTheMoonWin10_hxzk6evwjr6sy!App
```

* Save it somewhere safe

@alert info
To execute your script, right-click it and choose 'Run with PowerShell'
@end

## ReShade Repository

As you cannot install or copy files into a UWP game folder, here is how we managed to have all our Shaders and Texture in just one folder.

* First of all, if you copied the Shaders and Textures in a specific folder AND injected ReShade into an UWP game, a `reshade.ini` is created in the ReShade UWP folder (eg: `D:\ReShade-DeliverUsTheMoon\`)
* Open `reshade.ini` and modify the following lines to reflect your current setup

```
CurrentPresetPath=D:\ReShade UWP\Deliver Us The Moon.ini
EffectSearchPaths=.\,D:\ReShade UWP\Shaders,D:\ReShade UWP\Shaders\OtisFX
TextureSearchPaths=.\,D:\ReShade UWP\Textures
```

This is how it looks on my side. ![alt text](..\Images\MiscGuides\uwp_reshade_folder01.png){.shadowed .autosize}

@alert tip
To update the ReShade version, just download the installer from [reshade.me](https://reshade.me/).
Open the installer with WinRar then copy and replace the ReShade64.dll with the new one.
@end
