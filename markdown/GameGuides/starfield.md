![Starfield](Images\starfield_header.png "Shot by Soulsurrender"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes, with tools
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 12
Game version | 1.8.86

## Tools

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**[Features](https://opm.fransbouma.com/Cameras/starfield.htm)**: Camera control, camera paths support, game pause/unpause, frameskip, HUD toggle, hotsampling and more.

## Helpful mods for screenshotting

@alert warning
Using mods and console commands will disable achievements. Use one of the achievement enabling mods ie. [Baka Achievement Enabler (SFSE)](https://www.nexusmods.com/starfield/mods/658).
@end

* [Starfield Script Extender (SFSE)](https://www.nexusmods.com/starfield/mods/106): Required for many mods.
* [Starfield Hotkeys](https://www.nexusmods.com/starfield/mods/1578): Hotkey console commands.
* [Luma - Native HDR and more](https://www.nexusmods.com/starfield/mods/4821): Might reduse color banding.
* [Base LUTs](https://www.nexusmods.com/starfield/mods/1433): Custom base/neutral LUTs for color grading.
* [Neutral LUTs - No Color Filters](https://www.nexusmods.com/starfield/mods/323): Another neutral LUT mod. Removes the color filters from the game, making the colors more uniformly neutral with deeper blacks.
* [Screen Archer Menu Starfield](https://www.patreon.com/MaxieAlice): Lights, pose adjustments, positioning, eye control, face morphs and more.
* [Photo Mode Tweaks](https://www.nexusmods.com/starfield/mods/583): Removes photo mode boundaries, and enhances sliders.
* [CharGenMenu](https://www.nexusmods.com/starfield/mods/6850): Improves the vanilla CharGenMenu and you can save/load your own character presets.
* [Shadowy Shadows](https://www.nexusmods.com/starfield/mods/6410): A set of ini tweaks for lighting and shadows.

## Tips and tricks

### Useful console commands

@alert important
Save before you start messing around with console commands!
@end

Command	| Description
--|--
`tgm` | Toggle God Mode.
`tai` | Toggle AI. Freezes selected actor.
`tcai` | Toggle Combat AI. Makes all/selected actors passive.
`tcl` | No Clip. Allows you to move through walls and other objects, and reach heights normally inaccessable.
`modpos x/y/z <value>` | Select object/actor in console to move them into desired position. Also useful to hide unwanted objects/actors.
`modangle x/y/z <value>` | Select object/actor in console to rotate them.
`setscale <value>` | Sets the scale of your selected object/actor.
`passtime <value>` | Moves time forward. Useful if you want to capture certain time of day.
`Showlooksmenu Player 2` | Change your character's looks from anywhere.
`pt <ID>` | Place There. Spawn any object/actor where your mouse pointer is pointing.
`placeatme <ID>` | Place at Me. Spawn object/actor at your position.
`fw <ID>` | Changes the Weather.
`lf` | Toggle lens flare.

Useful commands if you don't have access to Otis_Inf camera tools:

Command	| Description
--|--
`tfc` | Toggles freefly camera.
`tfc 1` | Same as `tfc` but also stops time.
`tm` | Toggles the UI on and off.
`sucsm <value>` | Sets speed of freefly camera.

### Changing the weather

Use `fw <ID>` in the console.

<details><summary class=important>View list of weathers</summary>

Weather name | ID
--|--
DefaultWeatherSettings | 0000018A
UC04_Weather_BurningHaze_C1 | 000405FB
Weather_Clear_C0_Clear | 0002B07E
Weather_Clear_C0_HazyLight | 0002B085
Weather_Clear_C0_MistDense | 0002B084
Weather_Clear_C0_MistLight | 0002B087
Weather_ClearFrozen_CO_Clear | 001411C3
Weather_ClearFrozen_C0_HazyLight | 0028A874
Weather_ClearFrozen_CO_MistDense | 0028A875
Weather_ClearFrozen_C0_MistLight | 0028A871
Weather_Cloudy_C1_Clear | 0002B088
Weather_Cloudy_C1_HazyLight | 0002B094
Weather_Cloudy_C1_MistDense | 0002B093
Weather_Cloudy_C1_MistLight | 0002B095
Weather_Cloudy_C2_Clear | 0002B4FB
Weather_Cloudy_C2_HazyLight | 0002B503
Weather_Cloudy_C2_MistDense | 0002B4FF
Weather_Cloudy_C2_MistLight | 0002B507
Weather_Cloudy_C3_Clean | 0002B50B
Weather_Cloudy_C3_HazyLight | 0002B513
Weather_Cloudy_C3_MistDense | 0002B50F
Weather_Cloudy_C3_MistLight | 0002B517
Weather_CloudyFrozen_C1_Clear | 00141189
Weather_CloudyFrozen_C1_HazyLight | 001411CA
Weather_CloudyFrozen_C1_MistDense | 001411D8
Weather_CloudyFrozen_C1_MistLight | 001411C5
Weather_CloudyFrozen_C2_Clear | 00141184
Weather_CloudyFrozen_C2_HazyLight | 00141182
Weather_CloudyFrozen_C2_MistDense | 001411D7
Weather_CloudyFrozen_C2_MistLight | 001411C6
Weather_CloudyFrozen_C3_Clear | 001411CE
Weather_CloudyFrozen_C3_HazyLight | 001411BD
Weather_CloudyFrozen_C3_MistDense | 001411D6
Weather_CloudyFrozen_C3_MistLight | 001411C7
Weather_Fog_C1_Heavy | 0002B527
Weather_Fog_C1_Light | 0002B51F
Weather_Fog_C1_Medium | 0002B523
Weather_Fog_C1_VeryHeavy | 0004279B
Weather_Fog_C1_VeryLight | 0002B51B
Weather_Fog_C2_Heavy | 0002B538
Weather_Fog_C2_Light | 0002B530
Weather_Fog_C2_Medium | 0002B534
Weather_Fog_C2_VeryHeavy | 000C74C6
Weather_Fog_C2_VeryLight | 0002B52C
Weather_Overcast_C1 | 0002B53C
Weather_Overcast_C2 | 0002B540
Weather_OvercastFrozen_C1 | 0028A877
Weather_OvercastFrozen_C2 | 0028A878
Weather_PartlyCloudy_C1_Clear | 0002B544
Weather_PartlyCloudy_C1_HazyLight | 0002B54C
Weather_PartlyCloudy_C1_MistDense | 0002B548
Weather_PartlyCloudy_C1_MistLight | 0002B550
Weather_PartlyCloudy_C2_Clear | 0002B554
Weather_PartlyCloudy_C2_HazyLight | 0002B55D
Weather_PartlyCloudy_C2_MistDense | 0002B559
Weather_PartlyCloudy_C2_MistLight | 0002B561
Weather_PartlyCloudy_C3_Clear | 0002B565
Weather_PartlyCloudy_C3_HazyLight | 0002B56D
Weather_PartlyCloudy_C3_MistDense | 0002B569
Weather_PartlyCloudy_C3_MistLight | 000AE7D6
Weather_PartlyCloudy_C4_Clear | 000AE7D7
Weather_PartlyCloudy_C4_HazyLight | 000C3042
Weather_PartlyCloudy_C4_MistDense | 000C3041
Weather_PartlyCloudy_C4_MistLight | 000C3043
Weather_PartlyCloudy_C5_Clear | 000C3044
Weather_PartlyCloudy_C5_HazyLight | 000C3046
Weather_PartlyCloudy_C5_MistDense | 000C3045
Weather_PartlyCloudy_C5_MistLight | 000C3047
Weather_PartlyCloudyFrozen_C1_Clear | 001411BF
Weather_PartlyCloudyFrozen_C1_HazyLight | 001411D2
Weather_PartlyCloudyFrozen_C1_MistDense | 001411D5
Weather_PartlyCloudyFrozen_C1_MistLight | 001411BB
Weather_PartlyCloudyFrozen_C2_Clear | 001411CD
Weather_PartlyCloudyFrozen_C2_HazyLight | 001411D0
Weather_PartlyCloudyFrozen_C2_MistDense | 001411D4
Weather_PartlyCloudyFrozen_C2_MistLight | 001411BA
Weather_PartlyCloudyFrozen_C3_Clear | 001411CC
Weather_PartlyCloudyFrozen_C3_HazyLight | 001411CF
Weather_PartlyCloudyFrozen_C3_MistDense | 001411D3
Weather_PartlyCloudyFrozen_C3_MistLight | 001411DB
Weather_PartlyCloudyFrozen_C4_Clear | 001411CB
Weather_PartlyCloudyFrozen_C4_HazyLight | 001411C9
Weather_PartlyCloudyFrozen_C4_MistDense | 001411D1
Weather_PartlyCloudyFrozen_C4_MistLight | 001411DA
Weather_PartlyCloudyFrozen_C5_Clear | 001411B1
Weather_PartlyCloudyFrozen_C5_HazyLight | 001411C4
Weather_PartlyCloudyFrozen_C5_MistDense | 001411BC
Weather_PartlyCloudyFrozen_C5_MistLight | 001411D9
Weather_Rain_C1 | 000C3048
Weather_RainHeavy_C1 | 000C3049
Weather_Sandstorm_C1 | 000C304A
Weather_SandstormHeavy_C1 | 000C304B
WeatherSnowC01 | 000C304C
WeatherSnowHeavyC01 | 000C304D
WeatherThunderstormC01 | 000C304E
WeatherClearFrozenList | 001411C8
WeatherClearFrozenTemplate | 001411BE
WeatherClearList | 000405FC
WeatherClearTemplate | 000E8397
WeatherCloudyFrozenList | 001411C2
WeatherCloudyFrozenTemplate | 001411C0
WeatherCloudyList | 000405FE
WeatherCloudyTemplate | 000E8396
WeatherFogHeavyTemplate | 001AF3F8
WeatherFogList | 000405FF
WeatherFogTemplate | 000E8344
WeatherNone | 003D2491
WeatherNoneFrozen | 0000AC2F
WeatherOvercastFrozenList | 0028A87A
WeatherOvercastFrozenTemplate | 0028A879
WeatherOvercastList | 00040600
WeatherOvercastTemplate | 000E8381
WeatherPartlyCloudyFrozenList | 001411C1
WeatherPartlyCloudyFrozenTemplate | 001411B7
WeatherPartlyCloudyList | 00040601
WeatherPartlyCloudyTemplate | 000E838C
WeatherRainHeavyList | 00040603
WeatherRainHeavyTemplate | 001E86B2
WeatherRainList | 00040602
WeatherRainTemplate | 000E8368
WeatherSandstormC01H500D100 | 000E8325
WeatherSandstormHeavyList | 00040605
WeatherSandstormList | 00040604
WeatherSandstormTemplate | 000E8330
WeatherSnowC01H100D050 | 000E834B
WeatherSnowC01H500D075 | 000E8346
WeatherSnowC01H500D100 | 000E8345
WeatherSnowHeavyC01H500D100 | 002ACEA2
WeatherSnowHeavyList | 0003334F
WeatherSnowList | 00040606
WeatherSnowTemplate | 000E8350
WeatherThunderstormC01H050D075 | 000E8359
WeatherThunderstormC01H100D075 | 000E8356
WeatherThunderstormC01H500D075 | 000E8351
WeatherThunderstormList | 00040607
WeatherThunderstormTemplate | 000E835C
WeatherUniqueAkila_Clear_CO_Clear | 0031FC4B
WeatherUniqueAkila_Clear_CO_Unique | 0031FC4C
WeatherUniqueAkila_Cloudy_C3_Unique | 0031FC50
WeatherUniqueAkila_Fog_C1_Medium | 0031FC51
WeatherUniqueAkila_Partly Cloudy_C2_Unique | 0031FC4D
WeatherUniqueAkila_Partly Cloudy_C3_HazyLight | 0031FC4E
WeatherUniqueAkila_Rain_C1 | 0031FC52
WeatherUniqueCydonia_Clear_CO_MistLight | 0031FC53
WeatherUniqueCydonia_Clear_CO_Unique | 0031FC54
WeatherUniqueCydonia_Sandstorm_C1 | 0031FC55
WeatherUniqueEarth_Clear_CO_Unique | 0031FC49
WeatherUniqueEarth_ClearFrozen_CO_Unique | 00310DB8
WeatherUniqueGagarin_Clear_CO_HazyLight | 0031FC4A
WeatherUniqueGagarin_Fog_C1_Heavy | 00064D15
WeatherUniqueGagarin_Partly Cloudy_C3_Unique | 0031FC4C
WeatherUniqueHomestead_Partly Cloudy_C3_Unique | 001FA1BC
WeatherUniqueHomestead_Snow_C1 | 00235C70
WeatherUniqueHomestead_SnowHeavy_C1 | 00245214
WeatherUniqueKreet_Clear_CO_Clear | 000AA384
WeatherUniqueKreet_Partly Cloudy_C5_Unique | 000AA385
WeatherUniqueKreet_Sandstorm_C1 | 000AA383
WeatherUniqueLC135_ScorpiusPuzzle | 0008BDAB
WeatherUniqueLightingTestGI02 | 00031FEB
WeatherUniqueLondiniun_SnowHeavy_C1 | 0034E83F
WeatherUniqueMercury | 0010C494
WeatherUniqueNA_Clear_Hazy_Unique | 0009BC59
WeatherUniqueNA_Clear_Misty_Unique | 0022FB28
WeatherUniqueNA_Clear_Unique | 001034AB
WeatherUniqueNA_Cloudy_C1_Unique | 0009BC58
WeatherUniqueNA_Fog_C1_Unique | 001034AC
WeatherUniqueNA_Partly Cloudy_C2_Unique | 0009BC5A
WeatherUniqueNeon_Rain_C1_Unique | 00325297
WeatherUniqueNiira_Fog_C1_UniqueHeavy | 0024FD3B
WeatherUniqueNiira_Fog_C2_Unique | 000CCBF8
WeatherUniqueNiira_Partly Cloudy_C5_Unique | 000CCBF7
WeatherUniqueNiira_Rain_C1_Unique | 000CCBF9
WeatherUniqueNiira_Thunderstorm_C1_Unique | 001443D7
WeatherUniqueParadiso_Clear_HazyLight | 003319E1
WeatherUniqueParadiso_Partly Cloudy_C3_Clear | 003319E0
WeatherUniquePluto | 0010C495
WeatherUniqueRed Mile_Partly Cloudy_C5_Unique | 0002139D
WeatherUniqueTitan_Overcast_C2 | 00031987
WeatherUniqueVectera_Partly Cloudy_C3_Unique | 0009EAA2
WeatherUniqueVenus_Fog_C1 | 00051800
</details>

### How to exit your ship in space

While in your cockpit and not flying the ship open the console and enter:

`player.setpos x 10`  
`setgravityscale 0`

To deactivate you can use your scanner to teleport back to the ship and then enter `setgravityscale 1` in the console.

### Access unlimited storage from anywhere

This is useful when you don't want to always carry around all your gear just for screenshots. 

Entering `00266e81.Activate Player` in the console will open the unlimited storage container in the Lodge bedroom, and can easily be accessed with a hotkey - [Starfield Hotkeys](https://www.nexusmods.com/starfield/mods/1578).

*Source and additional info* [here](https://www.nexusmods.com/starfield/mods/1537).

### Spawning objects and actors

To spawn an object or actor you first need to know the ID. Then use the `placeatme <ID>` or `pt <ID>` command.

@alert tip
Example: How to spawn an Aceles:
1. Enter `help aceles 4` in the console to find the ID.
2. Take note of the ID and enter: `placeatme <ID>` or `pt <ID>`
@end

It's also possible to spawn a decorator, which has the same functions as the decorater panel in any of your apartments.

`player.placeatme 00024DC7 1`

### Misc .ini Tweaks

Add to your StarfieldCustom.ini

<b>No dialogue light:</b>

```
[Dialogue]
bEnableDialogueLight=0
```

<b>Full resolution clouds</b>

```
[Display]
bHalfResClouds=0
bHalfResolutionCorrection=0
```

<b>No bloom</b>

```
[Display]
bEnableNewBloom=0.0
fBloomGaussianKernelMinScale=0.0
fBloomGaussianKernelPower=0.0
fBloomUpsampleBlendFactor=0.0
fLegacyBloomAmountScale=0.0
fNewBloomAmountScale=0.0
```

<b>Flora density</b>

```
[ProcGen]
fObjectMapMinPct=-5
fProcGenFootprintDitheringScale=0.115
```

*Source:* [Reddit](https://www.reddit.com/r/Starfield/comments/17v5quo/psa_you_can_edit_some_ini_settings_for_flora/)

## Useful links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Starfield)
* [Starfield Nexus Mods](https://www.nexusmods.com/starfield)
* [MODDING STARFIELD (PC) - A Quick Guide - by Gopher](https://www.youtube.com/watch?v=t-itv604IMQ)
* [Starfield console commands](https://www.shacknews.com/article/136971/starfield-console-commands)
* [Starfield Default Values for All Known Valid INI Settings](https://stepmodifications.org/forum/topic/19019-starfield-default-values-for-all-known-valid-ini-settings/)