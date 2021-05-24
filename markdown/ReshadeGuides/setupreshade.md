Setting up Reshade
============
 
Reshade is a powerful post-processing system with a lot of features. To get the most out of Reshade, it's key to set it up 
properly for the game you're using it with. This guide is written for Reshade v4.2. If you're using an older version, some
information might still apply, but that's not guaranteed. 
 
This guide is written for screenshotting. This means it doesn't really go into topics like performance mode as the game is likely
paused when you're going to set up your shot and the Reshade configuration you want to use for it. 
 
## Video
If you prefer video guidance, Framed member TheGordinho Ochinchin [made a video guiding you through the basic steps](https://www.youtube.com/watch?v=hYUiWfvyafQ) 
 
## Setting up Reshade for the game
To set up Reshade for a game, and not having the game running, we first have to [download it from the Reshade website](https://reshade.me/). 
After you've downloaded the .exe and started it, it will open a small program that will guide you through the process. Simply pick the game's .exe file as 
the first step. 
 
After that it should pick the right rendering API. If it fails to do so, simply pick DirectX 11 if it's a rather new game. The last step
is that it will ask you to download a set of shaders. If you're new to Reshade and don't have anything configured yet, it's best to download
all shaders [from the main repository on GitHub](https://github.com/crosire/reshade-shaders). If you decide not to download any shaders, at least download
the **DisplayDepth** shader as it helps with setting up Reshade properly.
 
After this, Reshade is ready to roll. Starting the game will show a banner at the top that Reshade is active. It also shows which key combination
to press to open the menu, which you'll need for the next section.
 
## Configuring Reshade
When Reshade is setup and running in the game, you can open its menu. Newer Reshade versions use the `HOME` key to open the menu. If you copied a 
Reshade configuration you might have to use `Shift-F2`. 
 
After opening the menu it might first show you the tutorial if you're new. The tutorial will set you up with a preset and tell you what all the parts 
are for. If you decided to download shaders when setting up Reshade you'll see all *techniques* these shaders contain listed in a nice order on the 
**Home** tab. You can assign hotkeys for each technique by right-clicking the name and clicking in the textbox next to *Toggle Key*. 
 
Pressing the toggle key will then activate/deactivate the technique. To activate/deactivate a technique, e.g. DisplayDepth, you can also check the checkbox in front of 
the technique name with the mouse. When a technique is active, its controls are listed at the bottom of the *Home* tab. You can drag the horizontal blue bar 
upwards to make some space. 
 
### Undock the menu
By default the menu is docked at the left side of the screen. This might be problematic if you want to look at a part that's covered by the menu. To be able to 
move the menu, you can drag a tab (like the **DX11** tab) off the menu and then add all other tabs to that tab to create a floating menu. Be sure not to dock a tab 
to the side of the screen. So when an icon appears to dock the tab to one side of the screen be sure to avoid dropping the tab on that icon. 
 
You can re-arrange the tabs in the floating menu by dragging the tab headers to the left or right. This way you can create a floating menu with the tabs in the order
you want. You can move the menu around by clicking anywhere in the menu and simply dragging it to some point.
 
When you now disable and enable the menu again, it will stay a floating menu and you can drag it around to any spot you want. 
 
### Order of execution
The techniques on the *Home* tab seem to be listed in a random order, but that's not the case. The order of execution is from top to bottom. This means that 
if you have the techniques CinematicDOF and LumaSharpen active and listed in that order from top to bottom, Reshade will first execute CinematicDOF and after that
LumaSharpen. This has the effect that the result of CinematicDOF will be used as input for LumaSharpen. 
 
What the right order is for you depends on your taste, however in general the rule of thumb is that any color oriented technique should be executed before
any lens oriented technique (like a Depth of Field shader, or a filmgrain or overlay shader). 
 
### Setting up global preprocessor definitions. 
Reshade uses a couple of global preprocessor definitions which have an impact on how techniques work. E.g. how the depth buffer looks like. You can 
edit these definitions by clicking the blue 'Edit global preprocessor definitions' button right at the top of the technique parameters on the *Home* tab. 
What these settings mean is explained in the section [Checking depth buffer access](#checking-depth-buffer-access).
 
### Reshade settings 
You can configure the various settings of Reshade on its Settings tab. For us screenshotters the *Screenshots* section is particularly important. 
The key to use shouldn't interfere with other overlays you're using, e.g. Steam, UPlay and the like, and you should pick a file format that works for you best,
e.g. png is lossless and you can upload it everywhere. It's fairly self-explainatory.
 
## Changing a technique's parameters
So you're all set, ready to rock but how to change a technique's settings? To do so, first activate the shader by either pressing the Toggle key you defined or 
by checking the checkbox in front of the technique's name on the *Home* tab. You'll see that Reshade will display all settings for a shader below the blue splitter bar
on the *Home* tab. 
 
When you see a slider, you can drag these by using your mouse. If you see a numeric textbox you can change that value also with the mouse, by simply clicking in the 
textbox, holding left-mousebutton and dragging the mouse either left or right. When you hold `shift` while dragging these sliders and dragboxes, the value will 
increase/decrease faster. When you hold `ctrl` and click, you'll get a textbox which allows you to type in the value. This can be beneficial if you want to 
specify a value that's higher or lower than the range set for the control. 
 
## Checking depth buffer access
To make sure you have setup the depth buffer properly, it's key to have the **DisplayDepth** shader installed. Activating the DisplayDepth shader will show you
a proper overview of how the depth buffer looks and whether or not you have picked the right preprocessor definition values. There's 
[a great tutorial over on the Reshade forums](https://reshade.me/forum/shader-discussion/4810-about-the-changes-in-displaydepth-fx) 
of how to use the DisplayDepth shader to setup the depth buffer properly, so it's recommended to read it and setup your
Reshade configuration properly. You have to do this only once per game. 
 
### Picking the right depth buffer
It might be the game uses multiple depth buffers that might be useful, or it switches depth buffers on the fly for the final image and therefore it looks like the
depth buffer isn't available. For DirectX11 Reshade contains an additional tab the **DX11** tab, which shows all currently active depth buffers. To see which one
you should select, first enable the *DisplayDepth* shader. You likely either see a white or a black screen. 
 
When you go to the DX11 tab in the Reshade menu you can then pick the right depth buffer by checking its checkbox (or by trying the 
*Copy depth before clearing* checkbox). If the screen becomes what it should be you picked the right depth buffer and you can use it with the techniques that depend on it. 
 
## Shader duplication
 
There are cases where you would want to use one shader more than once (CanvasFog and StageDepthPlus shaders are popular in that regard). With most shaders all you need to do is replace the technique name in the shader code to a different one, but some shaders will need to change the name of a `namespace` or a texture name, so be aware of that. Be sure to check the shaders code for comments regarding duplicating the shader.
 
## Depth buffer on online games
 
When the game is an online game or actively performs network access, the depth buffer is disabled. Access to the depth buffer is often required as a lot of effects use the depth buffer of the game. Reshade actively disables access to the depth buffer if it
detects the game to be an online game (so there's network traffic on a regular basis). If the depth buffer isn't available in the game, because of this, the shaders that depend on that will likely fail.
 
So if you are trying to use reshade in a game which uses the internet connection constantly (because of the DRM or because it's always online like The Division or Steep) you will have to use custom reshade .dlls builds to get depth buffer access, otherwise reshade will block it. You can find some of these .dlls [here](http://project7.rf.gd). Alternatively you can still use reshade without depth buffer access, but some shaders that use it like CinematicDof won't work.
 
Keep in mind that the official version of reshade is whitelisted by some games anti-cheat software, so by using a custom .dll you may get banned depending on the game, so do your research beforehand.
 
## Further information
 
* [Reshade website](https://reshade.me/)
* [Reshade forums](https://reshade.me/forum/index)
* [Easy troubleshooting guide](https://reshade.me/forum/troubleshooting/5227-introducing-easy-troubleshooting#33088)
* [PC Gaming wiki guide](https://www.pcgamingwiki.com/wiki/ReShade)
 
## Custom shader repositories
 
* [Fu-Bama's shaders](https://github.com/Fubaxiusz/fubax-shaders)
* [OtisFX](https://github.com/FransBouma/OtisFX)
* [qUINT](https://github.com/martymcmodding/qUINT)
* [Daodan's shaders](https://github.com/Daodan317081/reshade-shaders)
* [Brussell's shaders](https://github.com/brussell1/Shaders)
* [Luluco250's shaders](http://github.com/luluco250/FXShaders)