![Deadlight Director`s Cut](Images\deadlight_header.png "Shot by pino44io"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No
Reshade | Yes 
Ansel | No
Graphics API | DirectX 9
 
## Tools

* [Cheat Table by One3rd](..\CheatTables\deadlight.ct)  
**Features**: Camera control, FOV control.

@alert info
For Camera script to work you will need to pause the game and use the FOV keybinds.
@end

Go to `\Documents\my games\UnrealEngine3\LOTDGame\Config\LOTDInput.ini`, add the next lines under the [LOTDGame.LOTDPlayerInput] section:

```
Bindings=(Name="F1",Command="pause",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="F2",Command="FOV 70",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="F3",Command="FOV 45",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="F4",Command="togglehud",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
Bindings=(Name="F5",Command="SET MATERIALEFFECT bShowInGame FALSE | show camfrustums",Control=False,Shift=False,Alt=False,bIgnoreCtrl=False,bIgnoreShift=False,bIgnoreAlt=False)
```

Set this file to **Read-only** once done.

Key/button | Description
--|--
F1 | Toggles game pause
F2 | Changes FOV to 70 
F3 | Changes FOV to 45
F4 | Toggles HUD
F5 | Removes vignette


## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Deadlight:_Director%27s_Cut)


