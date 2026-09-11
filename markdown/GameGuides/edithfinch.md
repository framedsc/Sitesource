![What Remains of Edith Finch](Images\edithfinch.png "Shot by Originalnicodr"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes ([see notes](#hotsampling))
DSR | No
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
Graphics API | DirectX 11

@alert neutral  
This guide is for an Unreal Engine 4 game that can use the [Universal Unreal Unlocker](https://framedsc.com/GeneralGuides/universal_ue4_consoleunlocker.htm). Do keep in mind that only the 3.x version of the unlocker works (4.x crashes the game upon injection). Moreover, no free-camera functionality is available, only the timestop works.
@end
 
## Tools

* [Cheat Table by Smithfield01 and IDK31FC](..\CheatTables\FinchGame12_inter.CT)  
**Features**: Free Camera, FOV, DOF control, RGB editor, Custom Aspect Ratio, Blackbars remover

## Controls

- Move camera position:
    - Num 4: Left
    - Num 6: Right
    - Num 8: Forwards
    - Num 5: Backwards
    - Num 9: Upwards
    - Num 7: Downards
- Move camera position: Mouse
- FOV control:
    - +: Increase
    - -: Decrease
- Camera tilt:
    - Num 1: Tilt the camera left
    - Num 3: Tilt the camera right

Keep in mind that in order to use any of the buttons above, you will have to freeze said values so the games doesn't change them back. You will see a "fov stop","xy stop", etc. boxes in the cheat engine table that need to be ticked in order to change the values correctly with the controls. I would suggest making a hotkey with all "stop" boxes so you can activate them all at once (don't freeze rot stop or you won't be able to look around with the mouse).

If you need to move faster, you can edit the table or modify the values directly in the table.

## Disable chromatic aberration

Go to the configuration file(s) location (that is `%LOCALAPPDATA%\FinchGame\Saved\Config\WindowsNoEditor\` in windows and
`<Steam-folder>/steamapps/compatdata/501300/pfx/` in linux). Open the `Engine.ini` file and add the following lines:
```
[/Script/Engine.RendererSettings]
r.SceneColorFringe.Max=0
```

## Hotsampling

Hotsampling works with the game, the only problem comes after resizing the window and alt-tabing back to the game, which causes it to resize again to the previous resolution. For taking shots, I suggest using MSI Afterburner (and installing RivaTurner that comes with the installation) which will allow you to take photos without being focused on the game (be sure to configure the desired hotkey in MSI Afterburner).

## Custom Resolution

For custom resolutions you have to edit the file in the following location: `C:\Users\Username\AppData\Local\FinchGame\Saved\Config\WindowsNoEditor\GameUserSettings.ini`

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/What_Remains_of_Edith_Finch)