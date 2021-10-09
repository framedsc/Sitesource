Ansel
=============

Ansel is Nvidia's implementation of a photomode into a large number of games through its GeForce Experience overlay. It allows the player to move the camera freely to take "super-resolution" tiled/AI-upscaled, 360°, HDR and stereoscopic screenshots. Named after famous landscape photographer Ansel Adams, it's one of the common camera tools used for screenshotting. It does come with (quite) a few limitations though.

### Controls
 
Description | Key / Gamepad bind
-|-
Open Ansel | `Alt + F2`
Camera Orientation | Mouse (while holding left click) / Right analog
Camera Movement | `WASD` / Left analog
Up/Down Movement | `Z`, `X` /  L2, L2
Camera Rotation | `Q`, `E` / L1, R1
Fast movement |  `Shift` (While moving) / R3
Slow movement | `Ctrl` (While moving)
FoV | In Ansel GUI (Camera section) 
Hide/Show Ansel GUI | `Ins` / In Ansel GUI
 
## Configuring Ansel

Ansel can be configured through an EXE found in `C:\Program Files\NVIDIA Corporation\Ansel\NvCameraConfiguration.exe` or `C:\Program Files\NVIDIA Corporation\Ansel\Tools\NvCameraConfiguration.exe`. You can use it for things such as changing the output format to `Lossless Output Image Format (PNG)`. More configuration settings can be found [here](https://www.ubergizmo.com/how-to/use-nvidia-ansel/).

If the folder doesn't exist, create the folder and download the EXE [here](https://nvidia.custhelp.com/app/answers/detail/a_id/4932/~/my-game-ready-driver-no-longer-has-program-files%5Cnvidia-corporation%5Cansel).

## Freestyle

Freestyle is Nvidia's implementation of post-processing filters. Because Reshade overlays on top of Ansel, captures with Ansel won't include Reshade effects. Freestyle effects do work with Ansel captures though. 

Freestyle is essentially a port of Reshade, so it is possible to install and use most Reshade effects in Freestyle as well. Just add the Reshade FXs of your choice to `C:\Program Files\NVIDIA Corporation\Ansel\`.

## Limitations

Ansel use is often discouraged because it can be quite limiting, especially when proper community-made camera tools exist.
 
- You cannot use Reshade with Ansel enabled.
- You cannot hotsample with Ansel enabled.
- The free camera often has range and clipping limits.
 
For some games where Ansel has been the only option, Cheat Engine tables or mods can exist that bypass these camera limits and give you a camera with more freedom. If these hacks exist, our [game guides](../Gameguides.htm) normally do mention them.
 
## Supported games

A full list of all the games Ansel is currently implemented in can be found [here](https://www.nvidia.com/en-us/geforce/geforce-experience/games/). Do note that this list includes all games in which Ansel supports, but not which Ansel features have been implemented. 

Be sure *Enable experimental features* is checked in your GeForce Experience settings, since support for some games hasn't been made official yet.
 
## More links
 
- [How to override Nvidia Ansel’s Super Resolution limits](https://www.techradar.com/how-to/nvidia-ansel-how-to-get-it-and-how-to-use-it) (TechRadar, last section of the article)
- [System Requirements](https://www.nvidia.com/en-us/geforce/geforce-experience/system-requirements) (Nvidia)