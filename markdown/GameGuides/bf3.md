![Battlefield 3](Images\bf3.png "Shot by Smithy"){.shadowed}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes
Ansel | No
DirectX versions | DirectX 10.1/11
 
## Tools
 
* [Camera by hattiwatti](https://www.mediafire.com/file/x5haebqei1rt7lq/CT_BF3_20180501-b0fdee.rar/file) Password is 'CinematicTools'  
**Features**: Freecam, Timestop, UI Toggle, FOV Control, Camera Movement Speed, Animated Camera Paths, Green Screen, DepthMap Toggle, Shadow Resolution Control 

### Installation & Use

For shooting the single-player campaign you'll want to use Hatti's camera tools (linked above). Extract the files to your BF3 Directory. Run `BF3 Cinematic Tools.exe` only while loaded into a level. **Make sure not to inject the tools while in the game's menus.** Unfortunately, the game will crash if you try to enable the camera after visiting the menus, loading a new level, or restarting from a checkpoint, so try not to die. 

Hatti's tools also work with multiplayer but you must only join servers that have Punkbuster DISABLED. **Failing to do so would result in you getting banned** and little chance to get unbanned by Punkbuster. 

## Hatti's Camera Tool Controls

Key | Function
--|--|
F5 | Toggle Camera Menu
INSERT | Enable/Disable Camera
W,A,S,D | Move Camera
ARROW KEYS | Rotate Camera
NUMPAD 1,3 | Camera Angle
LEFT CTRL, SPACEBAR | Camera Height
PAGE UP/DOWN | Increase/Decrease FOV
HOME | UI Toggle
END | Display Depth Map
DELETE | Timestop
F | Create Camera Track Point
G | Delete Last Track Point
P | Play/Stop Camera Animation
Q | Move Created Object
R | Remove Created Object
E | Rotate Created Object

@alert tip
Camera movement speeds can be changed in the Tool Menu (F5). Shadow Resolution, Depth Map Distance and Key Binding can be changed under the "Misc" Category in the menu. Green Screens can also be created from the Misc category under "Tools", although they might not work properly sometimes.
@end

## Tips and Tricks

### Custom Aspect Ratio

For custom aspect ratios, the game must be launched in windowed mode. SRWE has to be used to resize the window to the desired aspect ratio.

**Note:** The single player uses lens effects like dirt and flare on most of its levels, and these effects generally don't like resolutions higher than 1080p. This means hotsampling will cause them to repeat and appear smaller depending on the resolution.

### Reshade Support

You can use ReShade to add multiple different effects in single player. Since the game is quite old, some shaders can have unnatural-looking effects. 

Multiplayer supports ReShade as well, without the risk of getting banned. However, Depth based shaders are disabled due to ReShade's anti-cheat system. 

To counter these issues with SP & MP, just switch to the camera's depth map mode (END) and take another screenshot, then follow [this tutorial](https://framedsc.com/ReshadeGuides/depthguide.htm). If you have Photoshop or any other editing software, you can use depth maps to add blur and other depth based effects in post.

## Venice Unleashed

Venice Unleashed opens a whole new domain in this regard. You can edit lighting, environments, props and so much more to craft a shot that you like.

However it would be quite a lot to incorporate here, so you can use the two VU links below to get into it.

### Useful Links
 
* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Battlefield_3)
* [Venice Unleashed Modding Platform](https://veniceunleashed.net/)
* [Cinematic tools for Venice Unleashed](https://github.com/Powback/VEXT-CinematicTools)