![Sleeping Dogs: Definitive Edition](Images\SleepingDogsDE_header.png "Shot by One3rd")

##Feature summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | Yes
DSR | Yes 
Custom Aspect Ratios | Yes 
Reshade | Yes (see notes about depth buffer)
Ansel | No
DirectX versions | DirectX 11
 
## Tools
* [Camera Tools](https://mega.nz/file/vQgDRKxK#rWJDBAyjb_dXX5WowRPI43n8YKGOeLI9vyK_jmQbfuo)  
**Features**: Camera control (in-built HUD removal), FoV, Timestop, Time of Day, Weather Control, Sun Position, Lighting Control
* [CE table by One3rd](..\CheatTables\SDHDShip_Slomo_ChaseCam_v1.CT)  
**Features**: Features: Car Chase Camera, Timeflow, HUD toggle, Cheats

## Camera Tools Notes

Key	| Command
--|--
HOME | Toggle menu
INSERT | Toggle camera
DELETE | Freeze time
WASD / Left thumb | Move camera
Q / Left trigger | Move up
E / Right trigger | Move down
Arrow keys / Right thumb | Rotate camera
NUMPAD1 / Left shoulder | Roll left
NUMPAD3 / Right shoulder | Roll right
PAGE DOWN / Press LT | Zoom in
PAGE UP / Press RT | Zoom out

Hold roll left and right down for a second to reset roll  

Options for hi-def model spawning and camera based LOD. These work but after a while may cause model and level glitches. Can be fixed by disabling the options and restarting the level or game.

##  Time-of-day & Weather

To stop time-of-day from marching on, set the Game seconds per real second to 0.

## Pedestrians & Vehicles

Increasing cars and pedestrians excessively will have an equally excessive performance impact. At very large numbers cars and pedestrians go crazy, drivers will get frustrated at the massive crowds of people spilling onto the streets and will ram them or other cards to get away. Ambulances will then come to help those injured further blocking traffic and inducing road rage in more drivers resulting in even more carnage. 

To control pedestrian flow, there are pedestrian gates that will funnel pedestrians through choke points. Overflowing these gates with a flood of pedestrians will result in bottlenecks and large clumps of pedestrians on one corner or area and none anywhere else. Play with the Target pedestrian count and Pedestrians per square meter to see what works best in the area you are in. I've had good results with 500 pedestrians at 0.2 per square meter.

## Lights

Press the Spotlight or Omnilight buttons to spawn a light at the cameras current position. You can then enable/disable the lights from the list and edit settings.

When editing you can reposition the light to the cameras location by pressing Place at camera.

The types of lights available are spot, omni, direction, card, spot with lightshaft and area. Spot, omni, area and spot with lightshaft all seem to work with some fairly self explanatory settings once you start to play with them. Not sure what the direction or card lights do and it should be noted that changing a configured light from one type to card may result in a crash.

Many lights can be spawned and moved around the environment. Once you are done with them you can disable or delete them.

## Cheat Table Notes

Once the cheat table is loaded enable the Attach to game script or manually attach to game process. Use Cheat Engine to inject the camera tools by going to Memory View -> Tools -> Inject DLL, browse for and select `SDHDCamera.dll`.

## Timeflow
Timeflow can be used in conjunction with the Camera Tool TIMESTOP. For Slomo press F9, to disable press SHIFT + F9.

Key	| Command
--|--
F9 | activates script and sets time a mellow 0.3 
SHIFT + F9 | sets time back to default 1.0 normal time.
F5-F8 | almost stopped increasing to slow (useful for long exposure shots)

## Car Chase Camera and HUD Contol
This only works in vehicles and only when they are moving or have recently been moving.

Key	| Command
--|--
NUMPAD_0 | activates vehicle chase camera. This will disable the camera rotation and allow these to be manually set.
NUMPAD keys 4, 6, 8 and 5 | control pitch and yaw.
NUMPAD keys 7 and 9 | decrease/increase camera distance to vehicle.
NUMPAD_PLUS + 7 and NUMPAD_PLUS + 9 | decrease/increase camera FOV.  
[ | disable the game HUD 
] | re-enable the game HUD.

## Cheats

Manually enable Qi POWER AND HEAT script. Heat can be disabled by setting the NO HEAT value to 1 - currently not bound to a key.

Key	| Command
--|--
P | enables Qi power cheat
Shift+P | disables cheat

## Hotsampling and Depth Buffer Notes

Game can hotsample using SRWE but it must be in windowed mode (select from the in-game menu or ALT+ENTER. When changing the resolution you may need to do this twice for the actual internal render resolution to change. This also goes for when switching back to gameplay resolution, if playing fullscreen you may need to change to windowed and then back to fullscreen for the proper internal resulution to be applied.

Depth buffer may not load the correct one after a resolution change, check Reshade to see. You may need to select a different depth buffer. 

## Ground Fog
There is a glitch that can sometimes be used for more ground fog to be momentarily shown. This may only work at night and/or when in a vehicle. Pause game, wait awhile, un-pause game, pause again after required amount of fog generated in scene.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Sleeping_Dogs:_Definitive_Edition)