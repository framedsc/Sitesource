The Basics of Taking Screenshots
=========

## Hotsampling
 
The term refers to running a game in higher resolutions than your monitor supports, and in doing so being able to get screenshots at bigger definitions  (not desirable while playing since you will only see a portion of the window and, probably, with very low FPS).
 
It is also often referred to when talking about a game running in aspect ratios that aren't supported by monitors, like `4:3` or `2:1`.
 
To properly hotsample you would need to use programs like [SRWE](https://github.com/dtgDTGdtg/SRWE) or
 [WindowedBorderlessGaming](https://westechsolutions.net/sites/WindowedBorderlessGaming/). Please take in mind not every game supports this feature, 
 so before attempting to hotsample check if the game is capable of doing so in the games [guide](https://framedsc.github.io/GameGuides/index.htm) if it has one. Some games might have a mod or cheat engine table that unlocks hotsampling or custom ARs, and there have been reports of games hotsampling in borderless windows instead of windowed mode (which should be tried by default).
 
Another technique used to achieve high resolution screenshots is [DSR](https://framedsc.github.io/GeneralGuides/basics.htm#dynamic-super-resolution---dsr). The advantage of hotsampling over DSR is that you can play at your regular definition, go to a higher one to get a screenshot, and come back to your gameplay definition when you are done, where DSR makes you play with the same definition as the one you use while shooting, which can be quite demanding depending on the PC and the game.
 
### How to hotsample
 
Below you can find some guides on how to hotsample using SRWE:
 
- [Markdown guide in SRWE repostery](https://github.com/dtgDTGdtg/SRWE/blob/master/README.md)
- [Dom steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1119283512)
 
### Historical background
 
The original SRWE was intentionally made for running skyrim in a smaller window to save memory, but in 2012 the user midhras used it for doing the opposite and asked the developer to build a generic tool that would allow the same in other windowed games, which he later did.
Because that was being used more and more, a name was needed. Duncan Harris and midhras were talking about what to call using SRWE (or similar tools) to resize the game window, allowing for higher resolutions. The name shotsampling came out, but then Duncan called it hotsampling, which stayed.
 
### External links
- [Midhras nexus guide](https://www.nexusmods.com/fallout3/articles/49/?)
- [Hotsampling helper shader for ReShade](https://github.com/Daodan317081/reshade-shaders/blob/master/Shaders/HotsamplingHelper.fx)
- [Video showing SRWE in action](https://youtu.be/gNyQB7jPwEA)
- [Another guide](https://pcgamingexperience.com/resolutions/)
- [Yet another guide](https://bsn.boards.net/post/552340)
 
## Ansel
Referred to as the Nvidia tool that allows the player to move the camera freely (with restrictions depending on the game), taking screenshots with high definition by stitching various shots, taking 360° shots, applying filters, etc. Named after the famous landscape photographer Ansel Adams.
 
### Controls
 
Description|Key/Jotstick button
-|-
Open Ansel | Alt + F2
Move the camera orientation | Mouse / Right analog
Move the camera position forwards,left, backguards, right  | W,A,S,D / Left analog
Move the camera up, down | Z,X / 
Tilt the camera | Q,E / Left and Right D-pads
Fast movement | (While moving) Shift / 
Slow movement | /
FoV | / 
Ins | Hide/show the Ansel GUI
 
 
### Limitations
It's often overlook since it comes with some limitations:

- You can't use ReShade with Ansel enabled, instead you have to use the Nvidia alternative [Freestyle](https://www.geforce.com/es_ES/gfecnt/whats-new/articles/nvidia-freestyle-ansel-enhancements-geforce-experience-article) (which works with most reshade shaders).
- You can't hotsample with Ansel enabled.
- The camera often has limitations such as a range limit or clipping.
 
That last one can sometimes be overcome with mods or cheat engine tables, so make sure to look them up.
 
### List of Games
You can find the full list of games that support Ansel [here](https://www.nvidia.com/es-la/geforce/geforce-experience/games/), but the list also includes games that lack one or more Ansel features, so be aware that not all of the games listed there have a freecam available using Ansel.

Be sure to check the "enable experimental features" in GeForce Experience, since some games support isnt released yet.
 
### External links
 
- [Trick for pumping up the max super resolution](https://www.techradar.com/how-to/nvidia-ansel-how-to-get-it-and-how-to-use-it)
- [Extended Ansel modification settings](https://www.ubergizmo.com/how-to/use-nvidia-ansel/)
- [System Requirements](https://www.nvidia.com/en-us/geforce/geforce-experience/system-requirements)
 
## Dynamic Super Resolution - DSR
Dynamic Super Resolution (DSR for short) is a feature available in the Nvidia GPUs that allows games to render at a higher resolutions that your monitor supports. To be able to play using DSR the image gets downscaled so it fits your monitor, but the screenshots you take using it will be at the definition that the game renders.
 
To add new resolutions (with custom aspect ratios) see the [custom dsr resolutions guide](custom_dsr_resolutions.htm).
 
Bear in mind that not all games support this feature, so if you can't find the resolution in the game options after adding a new DSR resolution to your system then it probably doesn't support DSR. However, on some games while they do support DSR, the definition wont show up in the games video settings and you will need to set the DSR definition as your desktop definition.
 
### External links
 
- [Nvidia DSR page](https://www.nvidia.com/en-us/geforce/technologies/dsr/technology/)
- [DSR neogaf tutorial](https://www.neogaf.com/threads/downsampling-a-simple-method-for-making-your-pc-games-look-better.509076/)
- [AMD alternative neogaf tutorial](https://www.neogaf.com/threads/downsampling-for-amd-cards-is-now-possible.472941/)
 
## ReShade
 
ReShade is a post-processing injector for games, which means that it allows you to apply post-processing effects in real time. More links and information can be found in the  [Setting up Reshade guide](https://framedsc.github.io/ReshadeGuides/setupreshade.htm).
 
### External links
 
- [ReShade official page](https://reshade.me/)
- [List of repositories](https://www.pcgamingwiki.com/wiki/ReShade#List_of_known_shader_repositories)
- [Game compatibility list](https://www.pcgamingwiki.com/wiki/ReShade#Game_compatibility)
- [How To fix most of your problems with ReShade](https://www.youtube.com/watch?v=hYUiWfvyafQ)
- [How to Fix a Misaligned Depth Buffer on ReShade](https://www.youtube.com/watch?v=1z3VyU_4GQY)
 
## How to capture a screenshot of a game
 
There are a number of ways to take screenshots from games, here are a few of the most commonly used programs.
 
- **Steam** (Make sure to select in Steam screenshot parameters the option to save a lossless .png)
- **ReShade** (In some reshade builds the built-in screenshot function does not behave well with certain graphic APIs)
- **Windows Gaming Bar** (Windows key + Alt + Prnt Screen)
- **MSI Afterburner** (Key is configurable)
- **Nvidia Overlay** (Alt-F1)
 
Steam, ReShade and Afterburner have been proven to work well while hotsampling, but if you run into difficulties with any try switching up.
 
## Further reading

- [VP Guide by ILikeDetectives](https://ilikedetectives.com/virtual-photography-101)
