![Warhammer 40000: Space Marine 2](Images\spacemarine2header.jpg "Shot by Otis_Inf"){.shadowed .autosize}

##Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Ansel | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes (with cheat table)
Reshade | Yes, see guide below
Graphics API | DirectX 12
 
## Tools

* [Cheat table for enhancing the in-game photomode](..\CheatTables\SM2_PM.CT) by Otis_Inf and Skall  
**Features**: Unlimited range in PM, higher details, no black bars in non-16:9 aspect ratio's and custom in-game FoV

@alert Important
The game has Easy Anti Cheat enabled. This means that if you want to use the cheat table, you have to disable the anti cheat. See below.
@end

@alert Important
When you run into trouble with Reshade, e.g. the game hangs or crashes, please go to the folder `<steam installation folder>\Space Marine 2\client_pc\root\bin\pc` and delete or rename
`GFSDK_Aftermath_Lib.x64.dll`. Reshade should then work normally in the game (if you disable Easy Anti Cheat of course, see below).
@end

If the guide refers to `<steam installation folder>` below, it refers to the root folder where your game's installation folder is located. 

## Disabling the Easy Anti Cheat

To be able to use the cheat table to alter the photomode behavior and tweak other things in the game, you have to disable the Easy Anti Cheat (EAC). This is straightforward but
has the consequence that you can't play online in PVP matches. 

To disable the EAC, please go to the folder `<steam installation folder>\Space Marine 2\client_pc\root\bin\pc` and create a new bat file, e.g. `rungame.bat` and open it in notepad. Paste the following
lines in the file and save it:

```
set SteamAppId=2183900
set SteamGameId=2183900
"Warhammer 40000 Space Marine 2 - Retail.exe"
```

When you want to run the game without EAC, start this bat file instead of running it from Steam. 

## Disabling barrel distortion / CA / letterboxing in cutscenes

To disable the barrel distortion in the game, as well as the chromatic aberration and the letterboxing that's applied to cutscenes, 
you have to add some text files to some folders. This is described below. 

### Disabling barrel distortion

To disable barrel distortion, go to the folder `<steam installation folder>\Space Marine 2\client_pc\root` and create the following folders: `local\presets\data\default_camera_effects`, 
then go to the folder `default_camera_effects` you just created so you're now in the folder `<steam installation folder>\Space Marine 2\client_pc\root\local\presets\data\default_camera_effects`.
Create a new file called `lense_distortion.s3dprs` and open it in notepad. Be sure it doesn't have a suffix `.txt`!

Paste the following:
```json
preset   =   {
   params   =   {
      enabled   =   False
      params   =   {
         floatParam00   =   0.01
         floatParam01   =   0
         floatParam02   =   1
         floatParam03   =   0
         floatParam04   =   2
         floatParam05   =   2
         floatParam06   =   1.2
      }
   }
   __type__   =   "screen_effect_13"
}
```
and save the file. 

### Disabling chromatic aberration

(If you already have disabled barrel distortion, you already have made this folder)
To disable chromatic aberration, go to the folder `<steam installation folder>\Space Marine 2\client_pc\root` and create the following folders: `local\presets\data\default_camera_effects`, 
then go to the folder `default_camera_effects` you just created so you're now in the folder `<steam installation folder>\Space Marine 2\client_pc\root\local\presets\data\default_camera_effects`.
Create a new file called `chromatic_aberration.s3dprs` and open it in notepad. Be sure it doesn't have a `.txt` suffix!

Paste the following:

```json
preset   =   {
   ChromaticAberration   =   {
      Enabled   =   False
      Scale   =   0.25
      floatParam01   =   1
      floatParam02   =   1.5
      floatParam03   =   2
   }
   __type__   =   "image_effects"
}
```
and save the file

### Disabling letterboxing in cutscenes

To disable letterboxing in cutscenes, you have to create two files. 
Go to the folder `<steam installation folder>\Space Marine 2\client_pc\root` and create the following folders: `local\presets\data\cinematic`, 
then go to the folder `cinematic` you just created so you're now in the folder `<steam installation folder>\Space Marine 2\client_pc\root\local\presets\data\cinematic`.
Create a new file called `letterbox.s3dprs` and open it in notepad. Be sure it doesn't have a `.txt` suffix!

Paste the following:
```json
preset   =   {
   params   =   {
      enabled   =   False
      priority   =   40
      params   =   {
         floatParam00   =   2.35
      }
   }
   __type__   =   "screen_effect_15"
}
```
and save the file.

Now create a new folder inside the `cinematic` folder called `magnus` and go into this folder, so you're now in the folder 
`<steam installation folder>\Space Marine 2\client_pc\root\local\presets\data\cinematic\magnus`

Create a new file called `letterbox_magnus.s3dprs` and open it in notepad. Be sure it doesn't have a `.txt` suffix!

Paste the following:
```json
preset   =   {
   params   =   {
      enabled   =   False
      params   =   {
         floatParam00   =   2.35
      }
   }
   __type__   =   "screen_effect_15"
}
```
and save the file. 

## Cheat table related information

- The cheat table offers a feature to enable an infinite range for the photomode. However enabling this during gameplay will cause issues. So disable the range unlocker
  option when you close the photomode. You can toggle the range unlocker by pressing Scroll lock. You can of course assign a different key to the entry in cheat engine.
- Enabling the pillar box remover will give a low FoV. To fix that enable the game fov override and specify a higher FoV, e.g. 80 or 90. 
- To get higher details further away you have to enable the entry in the table and then change the value manually. Ultra will use a value of 0.9, and a value of 0.1 gives 
  nice details in the distance. You can keep this enabled. To change the value, simply double click it in cheat engine. 


