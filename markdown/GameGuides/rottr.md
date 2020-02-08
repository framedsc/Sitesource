![Rise of the Tomb Raider](Images\rottr.png "Shot by Otis_Inf"){.shadowed}

##Feature summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 11
 
## Tools

* [Camera tools by Hattiwatti](http://s000.tinyupload.com/index.php?file_id=29974862871895437644)  
**Features**: Camera control, FoV. It also has timestop but it can be a little buggy. For timestop, see below. It helps to reconfigure the
speed for movement / rotation in the console menu opened by the tools. 
@alert warning
A recent update has broken the latest version of the tools. You will have to revert your version of the game in orde to continue using them. 
See [this guide](..\GeneralGuides\steam_update_guide.htm) for instructions.
@end
* [HUD/Menu toggle by Otis_Inf](https://mega.nz/#!9IwzQB5B!lfExc2g1nItGv2FFz_4DxEOWCvT_91-xa8dUaxCHLLs)  
Use [Caps Lock] to toggle the visibility of the HUD / menu text. See the enclosed readme how to install.

## Timestop
The tools by Hattiwatti don't come with a timestop/gamepause. To take a shot of a paused game or use the camera during cutscenes,
use the following steps:

* Pause the game so the menu comes up
* Press [Caps Lock] to hide the menu
* Press Ins to enable the camera.
* Press the key configured to block input

## Depth buffer access
Recent Reshade versions (3.4.3 and up) have solid depth buffer detection code but sometimes can still make the wrong choice. In Rise of the Tomb Raider especially
it can pick the depth buffer which is empty or has Lara without hair. To fix that, use the *DisplayDepth* shader that comes with reshade to display the depth 
buffer, go to the **DX11** menu in the Reshade overlay and pick a depth buffer that shows Lara with hair. This isn't always necessary but in some situations
it is.

##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Rise_of_the_Tomb_Raider)
