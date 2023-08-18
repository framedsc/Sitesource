![Baldur's Gate 3](Images\baldursgate3_header.png "Shot by ashcorpdev"){.shadowed .autosize}

## Summary

| Feature              | Supported             |
| -------------------- | --------------------- |
| Vanilla Photo Mode   | No                    |
| Hotsampling          | Yes                   |
| DSR                  | Unknown               |
| Custom Aspect Ratios | No                    |
| Reshade              | Yes\*                 |
| Ansel                | Yes                   |
| Graphics API         | DirectX 11/Vulkan\*\* |

\* _[ReShade v5.9.1 or above](https://reshade.me/#download) is required to avoid crashing the game._

\*\* _Vulkan works with ReShade, but does not have depth buffer support._

## In-game Controls

| Name       | Keybind |
| ---------- | ------- |
| Toggle HUD | F10     |

## Tools

- [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
  **[Features](https://opm.fransbouma.com/Cameras/bg3.htm)**: Camera control, FoV control, Camera paths, HUD toggle, Timestop/Game speed, Hotsampling, Frameskip, Higher LODs

## Tips and Tricks

### Depth Buffer

If you want to make use of the depth buffer, you need to make sure you do the following:

- Run the game using DX11 mode (Vulkan currently does not support depth buffer).
- Enable the option 'Copy depth buffer before clear operation' in the 'Generic Depth' ReShade add-on (Can be found in the Add-on tab of ReShade).

## Useful Links

- [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Baldur%27s_Gate_3)
- [Native Camera Tweaks Mod](https://www.nexusmods.com/baldursgate3/mods/945) (Nexus Mods)
  - Provides unlocked camera pitch, zoom, controller stick deadzone.
  - Requires [Native Mod Loader](https://www.nexusmods.com/baldursgate3/mods/944/) to work.
