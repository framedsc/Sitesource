![Using UUU for Motion Blur](Images\MiscGuides\uuu_motionblur_header.png "Shot by Antic Owl"){.shadowed .autosize}
 
## Tools

* [Universal Unreal 4 Unlocker by Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Camera control, FoV control, HUD toggle, timestop/gamespeed, hotsampling and camera path
* [ReShade by Crosire](https://reshade.me/)  
**Features**: Screen Capture, Addons, Shaders,...

## Controls 
Refer to the [UUU documentation](https://opm.fransbouma.com/uuuv4.htm) for a complete list of controls available to you and how to use them.

## Using UUU Camera Path for Motion Blur

Camera paths not only let you create in-game videos but they can also be used to create motion blur in still images with the help of 
ReShade and the Real Long Exposure shader. Below are the steps how to achieve this.

1. Once your game has started, launch the UUU client and inject it.
2. Find the scene you want to capture and pause the game by pressing `Page Down` or `NumPad 0`.
3. Hide the HUD by presssing `Delete`.
4. Enable the camera by pressing `Insert`.
5. Frame you scene (FoV, angle, etc).
6. Go back to the UUU client and change the game speed as slow as you can. Recommended would be 0.01
7. At the bottom of the window activate the *Show camera path control window* button.
8. To attach the camera to the player or player vehicle the following options will need to be set.
    * Set `Total play time` to a large number, suggested 50s or more depending on how long your exposue is going to be.
    * Enable `Playback is relative to the player character's location`
    * Enable `Playback has a constant speed`   
![CameraPath](Images\MiscGuides\CamPath01.png) 
9. Add a new camera path by clicking on the `+` next to *Current path*. 
10. Add 2 nodes at the same place by clicking twice on `+` next to `Current node in path`
11. Start the playback by pressing on the `Play` button or `F7` and move the player. The camera will follow.
12. Start long exposure between 1s, 2s or more. 
13. Take the screenshot.

### Examples 

Below are two examples with a Before and After shot

* [Example 1](https://imgsli.com/MTA3Nzgz)
* [Example 2](https://imgsli.com/MTA3Nzg5)