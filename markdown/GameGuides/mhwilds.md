![Monster Hunter Wilds](Images\mhwilds.jpg "Shot by Originalnicodr"){.shadowed .autosize}
 
## Summary
 
Feature | Supported
--|--
Vanilla Photo Mode | Yes (lol)
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes (with mods)
Reshade | Yes
Ansel | No
Graphics API | DirectX 12
 
## Tools
 
* [REFramework](https://github.com/praydog/REFramework)  
**Features**: Script and plugin loader (among other things) needed to use with all mods.
* [Otis_inf camera tools](https://opm.fransbouma.com/Cameras/monsterhunterwilds.htm) (Not free, only available on Patreon)  
**[Features](https://opm.fransbouma.com/Cameras/monsterhunterwilds.htm)**: Camera control, pause/timestop, hotsampling, post processing, Cutscene DOF removal, Higher resolution shadows, barrel distortion removal, Higher LODs, near-camera geometry dithering removal, etc. Hud toggle is also included to be used with [ShaderToggler](../ReshadeGuides/Addons/shader_toggler_repository.htm).
* [aspect_ratio_fit](https://www.nexusmods.com/monsterhunterrise/mods/40)  
**Features**: Allows hotsampling at custome ARs.
* [RELit](https://github.com/originalnicodr/RELit)  
**Features**: Lighting Control, turn off scene lights, exposure control.  
Make sure to check out [the guide](../GeneralGuides/relit.htm) on it.
* [Time Skip](https://www.nexusmods.com/monsterhunterwilds/mods/1143)  
**Features**: Advance the in-world time by x minutes. Closest we have to ToD control.
* [EMV Engine (compatible with MH Wilds)](https://github.com/SilverEzredes/EMV-Engine-SILVER)  
**Features**: Console, Enemy Spawner, Character Poser, Gravity Gun, and more.
Make sure to check out the [guide](../GeneralGuides/emv_engine.htm) on it (notice that there are some differences between the version being shared here and the one from the guide)
* [Fake Player Light Remover](https://www.nexusmods.com/monsterhunterwilds/mods/1745)  
**Features**: Remove the light that is ever present on the player, for more realistic lighting.
* [Persistent Buff Glow Removal](https://www.nexusmods.com/monsterhunterwilds/mods/141)  
**Features**: Remove some player and weapon effects.
* [HD textures](https://www.nexusmods.com/monsterhunterwilds/mods/3214)  
**Features**: An HD texture pack that runs better than the one offered by the game, and has better resolutions on armors.
* [Disable Post Processing Effects](https://www.nexusmods.com/monsterhunterwilds/mods/22)  
**Features**: Useful for a variety of things, like disabling AA on the go if you want to render a scene with IGCSDOF for a sharper image.

* (Optional) [Fluffy mod manager](https://www.fluffyquack.com/)  
**Features**: Mod manager, lets you easily install, disable and enable mods. 


## Installation
First, install REFramework by dropping its files into the game folder, or installing via the [Fluffy mod manager](https://www.fluffyquack.com/). Most mods are installed inside the `reframework` folder; however, if in doubt, you can use the linked mod manager.

## Controls
You can find the freecam hotkeys and controls over [here](https://opm.fransbouma.com/Cameras/monsterhunterwilds.htm#controls). Then, when it comes to opening the REFramework menu, you can do so by pressing the Insert key.

## Custom Aspect Ratios
The game doesn't support custom aspect ratios out of the box, so you will need to use the [aspect_ratio_fit](https://www.nexusmods.com/monsterhunterrise/mods/40) mod linked above.

## Time of day control
The main usage of the [Time Skip](https://www.nexusmods.com/monsterhunterwilds/mods/1143) mod is to advance the in-world timer to get resources refreshed and new monsters, but we can also use it to only advance the day/night cycle. To do so, disable the "Environment" and the "Forecast" checkboxes in the mods menu, and advance the time either by pressing the button in REFramework UI or assigning a hotkey to do so.

Be careful of using this in a lobby with more people tho, as it's said to affect them all at once and could bring Capcom's attention.

## Rendering fur and hair
As it's usual with modern games, fur and hair shaders have a temporal aspect to them that makes them flicker. So, in order for those to look better, we should use a shader that accumulates samples, like [IGCSDOF](https://opm.fransbouma.com/igcsdof.htm) or [RealLongExposure](../ReshadeGuides/RealLongExposure.htm).

Also, for both methods, if the game happens to have TAA, it will make the rendered shot blurrier. Therefore, we should turn that off before starting our session (these methods already fix aliasing on their own). Fortunately for us, we can disable TAA (and change a lot of graphics options) on the fly with [Disable Post Processing Effects](https://www.nexusmods.com/monsterhunterwilds/mods/22) without needing to stop our screenshotting session and do so from the game's menu.

@alert tip
The tools' pause isn't perfect, and some weapons move a bit over time while paused, but we can use that to our advantage and render motion blur on them that way!
@end

## Taking shots in cutscenes

Unfortunately, neither the tools nor REFramework pause and time dilation options let you pause the cutscenes, so if you want to shoot them, you would need to pause them in-game with the X button. Just be careful not unpausing by accident if you activate the game-input passthrough to interact with REFramework.

@alert tip
If you want to reilluminate a scene in a cutscene, you would be interested in the vanilla lights that pop up at the top of the list in RELit, as those are specific scene lights and are probably the ones you are looking for to turn off manually.
@end

## Vanilla photomode options
The vanilla photomode does offer a couple of useful options that we can use:

- Handler and palico toggles
- Hunter's bird mount toggle
- Scoutfly effects (those green particles you see in places in the environment you can interact with)
- Hunter lighting, talisman, and outline effects

@alert tip
If you need to use any of these, my recommendation would be to pause the game, pause the player animation from REFramework, unpause, go to the game's menu, open the photomode, and then disable these. And after that, start the freecam to find your composition.
@end

If there are some effects that are still not disabled with this menu, or you can't use it for whatever reason, give the [Persistent Buff Glow Removal](https://www.nexusmods.com/monsterhunterwilds/mods/141) mod a try. It adds UI options on REFramework to disable these, although it doesn't cover all of them from my testing.

## EMV usage
The EMV mod comes with a lot of things, most of which are documented on our [EMV guide](../GeneralGuides/emv_engine.htm). However, the version of the mod we are using is a fork that was made compatible with MH Wilds, which comes with some difference with the original mod. Particularly the "Collection" part, which we will tackle below, but you should read the original guide for full context on what it does and what it is used for.

In Monster Hunter Wilds, your character is being referenced as `MasterPlayer`. If you go to the Collections section inside the Script Generated UI in REFramework UI, click on SearchSettings, enable the "Search for objects with any of thesekeywords", write `MasterPlayer` in the input field below that, and click the Search button at the top, you should get a reference to your player in the "Collected GameObjects" section.

In there, you can click on the "Animations" tree element and click on the pause button to pause your character. You can also manually select the exact frame of the animation that is currently playing (we still haven't found a way to play other animations tho).

Another thing that you can do from this Collection part is move the player itself by going to the "via.Transform" tree element and move the values of the first vector, called "_UniversalPosition". For rotation, you can edit the "_EulerAngler" vector.

Another thing that these mods allow is posing your character. By going to the "Posing" tree element, you can move your character's bones around, even using helpful UI elements like in-game gizmos. This feature also allows you to save and load poses. Here are some that people have made and shared:

- [Ikemen Model Poses - Confidence](https://www.nexusmods.com/monsterhunterwilds/mods/3369)
- [Ikemen Model Poses - On the Edge](https://www.nexusmods.com/monsterhunterwilds/mods/2957)
- [Ikemen Weapon Poses - Longsword Set 01](https://www.nexusmods.com/monsterhunterwilds/mods/3415)

To install them, you can easily do so with the Fluffy mod manager. They will pop up on the "JSON file" dropdown, and if the mod includes more than one pose, you should be able to select them on the "Pose" dropdown.

If any of this is confusing, you can follow [this](https://youtu.be/QQXXX4VIkAY?si=ze97S0Adqm9qRNDk) and [this](https://youtu.be/qSbf0180aII?si=qXHaswDNGoSL6_Yt) tutorials to get some visual references.

If you make some yourself, don't forget to share them online!

### Using EMV with monsters

Everything detailed above is also relevant to monsters themselves. However, instead of searching them with the Collections mod, we will use the console.

To do so, go to the Console settings inside the Script Generated UI section, and click on Spawn Console. After doing so, you can look up the monster by writing `/{monster_id}` and clicking on the Enter button. You should now get a tree element above the input field with the results. Oftentimes, you would get two found game objects, one whose name ends with "StageResidentHolder" and one that doesn't. You will want to interact with the one that doesn't. Once opened the right GameObject on the UI, you should be able to interact with it in a similar fashion that we did with the player.

You can find the Monsters' IDs [here](http://github.com/dtlnor/MonsterHunterWildsModding/wiki/Monster-IDs) (although monsters that were added through updates are probably missing from that list).

@alert tip
For action scenes my usual flow is to pause the game in a specific attack animation I like from the monster, then look it up with the console if I haven't done so yet, freeze its animation and maybe manually selecting a specific frame (altho I would be careful with doing so since they could get moved to other parts of the map while attempting to change that). Then I unpause the game, position my character in the right spot, do a cool pose with an attack or one of the social in-game poses, and pause the game again. And finally, I work on a composition and spawn the necessary lights with RELit (and maybe disable other vanilla ones).
@end


## Tips and tricks
- REFramework, for some reason, isn't blocking game inputs when interacting with its menu.
- The black bars when using custom aspect ratios in cutscenes can be taken out by turning the HUD off.
- The game's contrast is very low; we recommend tweaking the values. The ones I use are 3 for black values, 18 for white values, and 9 for brightness. Having said that, I would still suggest using Reshade to bring some more contrast.
- The game supports HDR! So if you have a screen with HDR support, you can take HDR screenshots with Reshade to get more color information to edit in post-processing in Photoshop or Lightroom.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Monster_Hunter_Wilds)
