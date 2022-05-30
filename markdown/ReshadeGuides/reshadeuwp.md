![Header](..\Images\MiscGuides\uwp_reshade_header.png){.shadowed .autosize}
 
# Injecting ReShade in UWP games (Universal Windows Platform aka. Windows Store and XBOX Game Pass PC)

This guide will help you to inject ReShade into UWP games. Please note that this won't work in every UWP game since some have protections (like forza horizon 4 which shutdown when you inject a .dll).
 
## Tools
 
You will need [crosire injector](https://reshade.me/downloads/inject64.exe).

### ReshadeForUWP tool
Alternatively, there's a GUI tool to inject Reshade into UWP / Xbox game Pass PC games, [located here](https://github.com/MilkyDeveloper/ReshadeForUWP) with little manual intervention. It asks you for the package name (and the custom process name, if any) and gets the metadata of the game through the ```appxmanifest.xml``` file. It then generates a BAT file to inject Reshade into the game and then launch it. Optionally, it also bootstraps a working Reshade install by downloading / extracting all of the FX files and generates the Reshade.ini file.
 
## How to inject ReShade into an UWP game
 
* Extract the zip containing the UWP Injector in a folder on your desktop or drive (eg:ReShadeUWP).
* Start the game you would like to use ReShade in.
* Open Task Manager and check the process name used by the game (eg: `MoonMan-Win64-Shipping.exe` for Deliver Us The Moon).
* Close the game.
* Open a command prompt and navigate to the folder where the UWP Injector resides (you can write `cmd` in the address bar and it will open a command prompt there).
* Type `inject.exe name_of_the_process.exe`.
* Start the game.
 
ReShade should now be injected.
 
# Advanced UWP ReShade Injection
 
If you find the process above too tiring for every time you want to play a game you can instead follow these steps to make a script that automatically launches the game and reshade.
 
## Preparation
 
* Extract the zip containing the UWP Injector in a folder on you Desktop or drive (eg:ReShadeUWP).
* Create a new folder and name it by the game name (eg: ReShade-DeliverUsTheMoon), copy the content previously unzipped in that folder.
* If you previously installed ReShade in a Steam game you can copy the Shaders and Textures in a specific folders (see ReShade Repository for more)
 
## Find the game executable and Application ID
 
*  Download the game via Windows Store or XBOX Game Pass App
* If a link is available on the desktop right click on it and note the Target (eg: WiredProductions.DeliverUsTheMoon...)
* In PowerShell type `get-appxpackage > C:\Users\<Your UserName>\Desktop\UWP_Apps_List.txt`
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
* Go to the folder where the game executable reside. In this case: `C:\Program Files\WindowsApps\WiredProductions.DeliverUsTheMoonWin10_1.4.44.0_x64__hxzk6evwjr6sy\MoonMan\Binaries\Win64\`
* Note the exe -> MoonMan-Win64-Shipping.exe

@alert Important
If you encounter files with padlock on them, you will not be able to use the injection process as the game is then mostly memory protected
@end

 
## Create your PowerShell injection script
 
* Start PowerShell ISE
* In the Script part start with `CD\` and press enter
* If the ReShade folder reside on a drive other than the C: write its drive letter and press enter
* Now write CD and the folder where ReShade injector resite (`CD D:\ReShadeUWP`)
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

* Save it on a safe place

@alert info
To execute your script, right-click it and choose 'Run with PowerShell'
@end

## ReShade Repository

As you cannot install or copy file into an UWP game folder here is how we managed to have all our Shaders and Texture in just one folder.

* First of all, if you copied the SHaders and Textures in a specific folder AND injected ReShade into an UWP game, a `reshade.ini` is created in the ReShade UWP folder (eg: `D:\ReShade-DeliverUsTheMoon\`)
* Open `reshade.ini` and modify the following lines to relflect your current setup

`CurrentPresetPath=D:\ReShade UWP\Deliver Us The Moon.ini
EffectSearchPaths=.\,D:\ReShade UWP\Shaders,D:\ReShade UWP\Shaders\OtisFX
TextureSearchPaths=.\,D:\ReShade UWP\Textures`

This is how it looks on my side ![alt text](..\Images\MiscGuides\uwp_reshade_folder01.png){.shadowed .autosize}

@alert tip
To update the ReShade version, just download the installer from [reshade.me](https://reshade.me/).
Open the installer with WinRar then copy and replace the ReShade64.dll with the new one
@end
