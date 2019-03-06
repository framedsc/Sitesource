![Street Fighter V](Images\SFVAE-header.jpg "Shot by Langgli")

##Feature summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes, with tools 
Reshade | Yes
Ansel | Partial, no freecamera
DirectX versions | DirectX 11
 
##Tools

* [CE table by nepafu and DeadEndThrills](..\CheatTables\streetfighterv.ct)  
**Features**: Camera control, FoV, Speed control, HUD toggle, DOF, Disable Timer, CPU Opponent Difficulty, Disable background NPCs

##Useful Links

* [Aspect Ratio correction patch by Jackfuste](http://www.wsgf.org/forums/viewtopic.php?p=172340#p172340)

##Additional Notes
* The game has an anti-cheat measure, make sure to play the game offline and 'mask' Cheat Engine application name with lua script by pressing Alt+Ctrl+L in CE and paste the following script 

```
getApplication().Title = "NotCE" 
getMainForm().setCaption("NotCE")
```
