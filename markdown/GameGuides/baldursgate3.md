![Baldur's Gate 3](Images\baldursgate3_header.png "Shot by ofseaandstars"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode   | No                   
Hotsampling          | Yes                  
DSR                  | Unknown              
Custom Aspect Ratios | Yes (with tools)
Reshade              | Yes\*                
Ansel                | No
Graphics API         | DirectX 11/Vulkan\*\*

\* _[ReShade v5.9.1 or above](https://reshade.me/#download) is required to avoid crashing the game._

\*\* _Vulkan depth buffer support requires [ReShade v5.9.2 and above](https://reshade.me/#download)._

## In-game Controls

Name | Keybind
--|--
Toggle HUD | F10

## Tools

- [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
  **[Features](https://opm.fransbouma.com/Cameras/bg3.htm)**: Camera control, FoV control, Camera paths, HUD toggle, Timestop/Game speed, Hotsampling, Frameskip, Higher LODs

## Tips and Tricks

### Depth Buffer

If you want to make use of the depth buffer, you need to make sure you do the following:

- Run the game using DX11 mode.
  - Vulkan currently does not support depth buffer.
- Enable 'Copy depth buffer before clear operation' in the 'Generic Depth' ReShade add-on.
  - Can be found in the 'Add-on' tab of ReShade.
  - If using AMD FidelityFX™ Super Resolution (FSR), this does not need to be enabled.
- Set the global preprocessor definition `RESHADE_DEPTH_INPUT_IS_REVERSED` to `1`.
  - Can be found in the 'Home' tab of ReShade underneath the effects list.

## Useful Links

- [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Baldur%27s_Gate_3)
- [Native Camera Tweaks Mod](https://www.nexusmods.com/baldursgate3/mods/945) (Nexus Mods)
  - Provides unlocked camera pitch, zoom, controller stick deadzone.
  - Requires [Native Mod Loader](https://www.nexusmods.com/baldursgate3/mods/944/) to work.
