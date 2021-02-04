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

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Camera control, FoV, timestop, hud toggle, higher LODs selector.

## Depth buffer access
Recent Reshade versions (3.4.3 and up) have solid depth buffer detection code but sometimes can still make the wrong choice. In Rise of the Tomb Raider especially
it can pick the depth buffer which is empty or has Lara without hair. To fix that, use the *DisplayDepth* shader that comes with reshade to display the depth 
buffer, go to the **DX11** menu in the Reshade overlay and pick a depth buffer that shows Lara with hair. This isn't always necessary but in some situations
it is.

##Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Rise_of_the_Tomb_Raider)
