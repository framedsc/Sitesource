![Risen 3](Images\risen3_header.png "Shot by Eggo"){.shadowed}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
DSR | Yes
Hotsampling | No
Custom Resolutions | Yes ([with tweaking](#defining-custom-resolutions))
Custom Aspect Ratios | Yes ([with tweaking](#defining-custom-resolutions))
FOV | No
Reshade | Yes (DX9)
Ansel | No
DirectX versions | DirectX 9
 
## Tools

* [Cheat Engine Table by sortajan (Steam)](https://fearlessrevolution.com/download/file.php?id=18937)  
**Features**: Debug Mode toggle (Freecam, HUD toggle, Pause, etc),  Various Player Cheats

[comment]: # (Link to thread: https://fearlessrevolution.com/viewtopic.php?t=10837)

## Controls 

[comment]: # (include this section if your guide references a cheat table / non-standard tools [Otis_Inf tools are all standardised], otherwise remove it)
Key	| Command
--|--
`PgUp` / `PgDown` | Toggle Debug mode on / off


Debug mode must be enabled for the following controls to work:

Key	| Command
--|--
`Ctrl` + `H` | Toggle HUD
`F2` | Toggle fullscreen / windowed 
`Ctrl` + `F2` |  Change to next [defined](#defining-custom-resolutions) resolution 
`Ctrl` + `Insert` | Toggle freefly camera
`Ctrl` + `Home` | Toggle fixed camera
`W` / `S` / `A` / `D` | Move camera
`Space` / `C` | Move camera up / down
Hold `Ctrl`| Speed up camera
`Ctrl` + `PgUp` | Move player to camera
`Pause` | Freeze game
`F6` / `F8` | Toggle slowmo / speedup
`Ctrl` + `K` | Beam player forward
`Alt` + `T` | Toggle autowalk

See: [remapping and deleting debug controls](#remapping-debug-controls)
<details>
  <summary>Full list of controls</summary>
  
  
Key	| Command
--|--
`F1` | Take Snapshot
`F2` | Toggle Fullscreen / Windowed
`F3` | Toggle Render Mode
`F4` | Cycle Indicators
`F6` | Toggle Slowmo
`F7` | Reset Player
`F8` | Toggle Speed Up
`F11` | Toggle Control Enabled
`F12` | Quit Application
`Alt` + `A` | Camera Flight Add
`Alt` + `C` | Camera Flight Pose Forward
`Alt` + `D` | Toggle Audio Emitter
`Alt` + `E` | End Cutscene
`Alt` + `H` | Toggle Statistics
`Alt` + `I` | Toggle Shadow Map Occlusion
`Alt` + `K` | Action Kill
`Alt` + `L` | Toggle Morpheme LiveLink
`Alt` + `M` | Toggle Movement Debug
`Alt` + `O` | Toggle Occlusion Culling
`Alt` + `P` | Toggle Render Portal
`Alt` + `Q` | Camera Flight Start
`Alt` + `R` | Camera Flight PoseRendering
`Alt` + `S` | Say SVM
`Alt` + `T` | Toggle Autowalk
`Alt` + `V` | Camera Flight PoseEnd
`Alt` + `W` | Camera Flight Stop
`Alt` + `X` | Camera Flight PoseBack
`Alt` + `Y` | Camera Flight PoseStart
`Ctrl` + `1` | Toggle Physics Opaque
`Ctrl` + `2` | Toggle Physics Wireframe
`Ctrl` + `3` | Toggle Physics Materials
`Ctrl` + `4` | Toggle Physics Shapes
`Ctrl` + `5` | Toggle Physics Meshes
`Ctrl` + `6` | Toggle Physics Controllers
`Ctrl` + `7` | Toggle Physics SpeedTrees
`Ctrl` + `AE` | Toggle Skinned Mesh LoD
`Ctrl` + `B` | Toggle Bounding Boxes
`Ctrl` + `E` | Toggle Entity Infos
`Ctrl` + `F` | Control Focus Entity
`Ctrl` + `F2` | Change to Next Resolution & Aspect Ratio
`Ctrl` + `F8` | Reset With Lift
`Ctrl` + `G` | Toggle State Graph Infos
`Ctrl` + `H` | Toggle HUD
`Ctrl` + `HOM` | Toggle Fixed Cam
`Ctrl` + `INS` | Toggle Free Fly Cam
`Ctrl` + `K` | Beam Forward
`Ctrl` + `L` | Toggle Levitate
`Ctrl` + `M` | Toggle Screen Messages
`Ctrl` + `N` | Toggle Navigation
`Ctrl` + `NUM_7` | Toggle Speed Tree Debug
`Ctrl` + `NUM_9` | Animation Toggle Transform Calculation
`Ctrl` + `O` | Toggle CBuffer Debug
`Ctrl` + `OE` | Toggle Cloth
`Ctrl` + `P` | Connect PhysX Debugger
`Ctrl` + `PG_UP` | Move Player To Camera
`Ctrl` + `Q` | Toggle Physics Render Debug
`Ctrl` + `T` | Toggle Speed Tree
`Ctrl` + `U` | Toggle Uneven Terrain
`Ctrl` + `UE` | Animation Skeleton
`Ctrl` + `V` | Toggle Vegetation
`Ctrl` + `X` | Action Down
`LSHF` + `Q` | Toggle Physics Native Debug
`LSHF` + `R` | Toggle Force Relaxed Processing
`NUM_1` | Toggle Melee Counter Parade On Attack
`NUM_2` | Toggle Melee Counter Parade On Parade
`NUM_3` | Toggle Melee Counter Attack
`NUM_4` | Toggle Shaky Cam
`PAUSE` | Freeze game
`RALT` + `F12` | Do Null Pointer Access
`RCtrl` + `D` | Toggle Drag Points Debug
`RCtrl` + `F` | Toggle FloatsDebug
`RCtrl` + `P` | Toggle DepthProbesDebug
`RCtrl` + `T` | Toggle PathDebug
`RShift` + `Q` | Toggle Physics NativeIgnoreZ

</details>
&nbsp;

## Tips and Tricks

### Defining custom resolutions

It is possible to define custom resolutions by editing  `<path to game>\Risen 3\data\ini\ConfigDefault.xml` and searching for `Resolutions`. It is advised to include your native resolution. In the example below you can see native 16:9 and 16:9 at 15 MP resolutions being used.
```html
      <Resolutions Test2="1920x1080xWindow" Test1="5162x2904xWindow">
      </Resolutions>
```
Pressing `Ctrl` + `F2` while debug mode is enabled will cycle to the next resolution, in this instance - back and forth. Custom aspect ratios are supported.

@alert tip
In some instances you will be required to use [SRWE](https://github.com/dtgDTGdtg/SRWE/releases) after swapping to a higher resolution because the game's window may appear stretched too far in one direction. Do note that capturing a stretched window with ReShade or Afterburner will output a perfectly viewable image with the correct resolution and aspect ratio.
@end

### Remapping debug controls

Debug controls can be remapped or deleted by editing `<path to game>\Risen 3\data\ini\ConfigDefault.xml` and searching for `DebugKeys`.

@alert tip
Visual enhancement mods may overwrite `ConfigDefault.xml` so save your own tweaks for the last.
@end

### Start the game in windowed mode

Navigate to  `%localappdata%\risen3\config\ConfigUser.xml` and edit `FullScreen="True"` to `FullScreen="False"`.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Risen_3:_Titan_Lords)
* [Neffo's Texture Mod](https://forum.worldofplayers.de/forum/threads/1444894-NeffO%C2%B4s-Texturmod-f%C3%BCr-Risen-3-Enhanced-Edition) (also includes a modded `ConfigDefault.xml`)




