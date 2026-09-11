![The Screenshotter's Guide to ReShade](Images\tsgts_header.png){.shadowed .autosize}

**ReShade** is a generic post-processing injector for games developed by crosire. It allows you to add a variety of post-processing effects to almost every game, enhancing the visual experience in your favourite games. This is a beginner-intermediate with the goal of helping you to get the most out of your ReShade experience.

@alert neutral  
This guide was last updated for ReShade 5.4.2. *(November 2022)*
@end

---

## Basic installation & setup

[At the bottom of the ReShade home page](https://reshade.me/), there are two download buttons:

* **ReShade 5.4.2** - This is the standard ReShade installer, designed to work in all supported games. 
* **ReShade 5.4.2 with full add-on support** - This installer installs a version of ReShade with unrestricted add-on support. This version may cause bans in multiplayer games.

Run the installer and follow its instructions. A game's graphics API is typically listed on its store page, or can be easily found online. 

@alert info  
**Installing to Unreal Engine games**  
The file structure of an Unreal Engine game differs from other games, with a bootstrap EXE immediately visible in the game files and the actual game EXE found deeper in the files. You will want to install beside this game EXE in order for ReShade to hook. This EXE can be found in `~\[game folder]\[game name]\Binaries\Win64`, and is typically named `[game]-Win64-Shipping.exe`. For example, the path to *Stray*'s EXE looks like this: `~\Stray\Hk_project\Binaries\Win64\Stray-Win64-Shipping.exe`.  
*This information is only applicable when installing ReShade versions older than 5.4.2. Installers newer than that should be able to find the game EXE on its own.*
@end

After installing ReShade, your game directory should be populated with a few more files. `dxgi.dll` (`d3d9.dll` for DirectX 9 games, `opengl32.dll` for OpenGL games) is the most important of the files. The rest are for ReShade's use. *Vulkan games currently use a "global" ReShade install that is always active and will affect any game running on Vulkan.*

**This DLL should not be renamed**, as its file name is what tells a game to load ReShade on launch. In the cases where it conflicts with existing game / mod files, it is possible to rename it in certain circumstances or [inject it through entirely different methods](#alternative-installations).

#### Existing `dxgi.dll` file  

Some DX10+ games or their mods may come with a `dxgi.dll` file. A potential solution to this conflict is to rename ReShade's DLL to `d3d11.dll` (or the respective Direct3D version) - most games will recognise this file name as something to load on launch.

---

## Shader order of execution

A key but often misunderstood part of how ReShade operates is the shader order of execution. Shaders will and do affect each other depending on their order in the ReShade GUI. Shaders load *on top* of the shader listed *above* them in the GUI. 

This order of execution is especially important when it comes to using multiple depth shaders like ambient occlusion (MXAO, RTGI) with depth of field (CineDoF, Physical DoF).

[include WEBM example of organising shaders real-time]

As seen above, when `qUINT_rtgi.fx` was placed below `CinematicDOF.fx`, its effects were clearly visible through the depth of field. However, once it was sorted above `CinematicDOF.fx`, it was appropriately defocused by the depth of field shader. 

### Suggested order of shaders

This is a decent way to organise your shader list so that the effects of each shader don't conflict with one another.

1. Depth lighting shaders   
Anything that adds additional lighting/shadowing information to a scene, like AO or GI shaders, usually come first, as their impact to a scene is the greatest.  
2. Color shaders  
Shaders that modify scene color, like tonemappers, MLUTs, or color grading (ReGrade, qUINT Lightroom) shaders. This is best placed after depth lighting shaders so that their AO/GI information remains accurate to the original scene.  
3. DoF shaders  
Placing a DoF shader after color shaders minimises the presence of banding caused by gradients when they're colour-graded.  
4. AA shaders  
Anti-aliasing shaders go well after depth effects to smooth out any visible aliasing caused by the depth buffer. Sharpening shaders can also be used at this stage.  
5. Lens shaders  
Lens effects like bloom, lens flares, chromatic aberration, and so on, are best placed following the DoF shader so that their effects aren't defocused. Perspective-warping shaders are also best placed at this stage.
6. Finishing shaders  
Shaders that complete the look are best placed here, such as grain shaders.
7. Utility shaders  
Utility shaders that assist in shooting but aren't typically captured, like FreezeShot or composition shaders, go all the way at the bottom, so that they aren't disrupted by any of the shaders above.

This order can and is often argued about. For example, a "purist" approach might involve placing color shaders *after* finishing shaders, to get you a more "filmic" result involving colour-graded grain and lens effects. Furthermore, this suggested order can be entirely ignored if you have a good understanding of how each shader in your list affects one another. 

It's also best to experiment to see what kind of results you can achieve! [These are a couple videos](https://github.com/TheGordinho/MLUT#tips-and-tricks) of TheGordinho exploring different ways of how MLUT order can affect the colours of a scene.

---

## Shader organisation

These are some quick tips to help with the organisation of all your `reshade-shaders`.

### Installing shaders manually

If you've come across a new shader or simply want to update an existing shader on GitHub, navigate to the FX file page through GitHub's file explorer in your browser. Once you see all the code, look for the **Raw** button in the top right, next to *Blame* and the pencil. This should open a plain text version of the shader file in your browser. `CTRL+S` on the page to immediately save it as an FX.

### The Global Folder

Ditch individual `reshade-shaders` folders in every single game with this quick tutorial on setting up a global `reshade-shaders` for all your games to use! This heavily reduces time spent organising all your shaders for each and every game, and keeps all your favourite shaders available in all your games.

1. **Pick a home**  
Find a good place to store your `reshade-shaders`. It can be your desktop, Documents, wherever that's convenient. Copy over any one of your current installs to this new directory.  
2. **Pointing ReShade**  
ReShade now needs to know where its `Shaders` and `Textures` have gone! Navigate to a current ReShade install and open `ReShade.ini`. Edit `EffectSearchPaths=` and `TextureSearchPaths=` appropriately. *This can also be done in-game.* 
3. **Now point it again**  
This process has to be repeated for every ReShade install, but it is also possible to copy over the `ReShade.ini` file to different installs. This does mean you have to set up the depth buffer again (and redo any other customisations you might have done) for any existing installs.  
*Older versions of the ReShade installer allowed you to edit settings such as shader and texture search paths immediately after installation in the installer itself. pls bring that back crosire*
4. **Enjoy!**  
There are many minor benefits to a global folder than make the inconvenience of setting it up so worth it. You no longer have to keep track of every single ReShade install, updating a shader across all your games is as easy as replacing that one file, you can even swap out sets of shaders with different `Shaders` folders if you wish (a full fat folder with every effect under the sun, then a streamlined version with only basic utilities? more useful than you think!).

### Subfolders

Keep your `reshade-shaders` organised with subfolders to categorise your shaders by adding `\**` to the end of your Shaders search path. The `\**` serves as a wildcard and tells ReShade to search all subfolders as well.

### Duplicating shaders  

There are cases where you might want a duplicate of a shader, like more composition helpers or [if you're Natty](https://www.youtube.com/watch?v=3EdGL5eLpT0). The process isn't as simple as duplicating the shader in your file explorer, but that is the first step.

1. Duplicate the shader  
2. Open the duplicated shader file  
3. Navigate to the bottom  
Look for the `technique` line, this line tells ReShade how to list the shader.  
4. Edit it as necessary  
Add a "2" at the end or call it something else entirely, this just lets ReShade know to process it as another shader.

@alert info  
Some ReShade forks, like GShade, include features to easily duplicate shaders in the GUI itself.  
@end

---

## Alternative installations

These are some events where the standard ReShade installation may fail and how they can be worked around.

### Proxy library

ReShade tends to conflict with other graphical enhancement mods, namely SpecialK and ENB. This is usually circumvented by loading ReShade as a proxy library. This is only necessary for local versions of SpecialK, for which [the process is documented on their wiki](https://wiki.special-k.info/en/SpecialK/ReShade). 

ENB can be set to load ReShade as a proxy library by adding these lines to `enblocal.ini`:
```
[PROXY]
EnableProxyLibrary=true
InitProxyFunctions=true
ProxyLibrary=yourd3d11.dll
```
`ProxyLibrary=` is naturally the name of your ReShade DLL, which should be renamed to something like `Reshade64.dll` to stop conflicts with ENB.

[This great thread](https://reshade.me/forum/general-discussion/1267-using-additional-dll-files) on the ReShade forums covers all alternatives to loading ReShade as an additional library in older titles if the above doesn't work well.

### Injection

ReShade can also be manually injected into a game when it fails to be loaded on launch. The process is the same as covered in [our ReShade in UWP games guide](https://framedsc.com/ReshadeGuides/reshadeuwp.htm#how-to-inject-reshade-into-an-uwp-game).