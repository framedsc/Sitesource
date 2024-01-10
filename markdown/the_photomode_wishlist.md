<div class="figure">
<img src="Images/photomode_wishlist.jpg" alt="The Photomode Wishlist" title="The Photomode Wishlist" class="autosize shadowed" />
<p><i>Alan Wake II</i>, shot by seymourglass</p>
</div>

This article is aimed at developers who are curious about what the "perfect" photomode looks like to us users. We are aware that features cost resources so we will try to order the things we like to have when shooting games based on priority.

You will find that most of the suggestions below involve giving more freedom to the user regarding what and how they can change things. We, however, understand how such control can be overwhelming for some inexperienced users, especially if they have never come across similar things. And that's why we recommend checking out popular third-party tools such as [Otis_Inf's photomode mods](https://opm.fransbouma.com/) to see how these settings have evolved into pretty straightforward settings. More on that at the end.

# Essential
----
These are the features that we believe have to be in any photomode. Some of these would look obvious to you, but a lot of the current photomodes in games fail at these.

## Free Camera movement and orientation
The following aspects regarding camera movement and orientation are crucial:

- Maximum range as big as possible
: Maybe your game or engine is not prepared to deal with the camera being far away from the player, but we still encourage you to push this value as much as you can. Small range limits are one of the things that get modded first on PC, so players will certainly appreciate it. The studio may be worried about the players moving the camera around to find secrets or look at what comes next in the level. However, we feel this is to be a decision that comes from the player, and believe that the advantages outweigh the downsides.

- No orbital free cam
: Some popular console first-party titles like to have their photomodes centered around their characters, so they only let you move the camera around them. Not only is this less intuitive to control than a normal freecam, but it also emphasizes only a fraction of what the game has to offer visually with its characters, instead of letting the user move the camera across the environment itself to find beauty in it.

- Photomode availability in a cutscene 
: We are aware of how many tricks devs pull outside of the camera range on cutscenes, but being able to still use the photomode in them is crucial to have the most amount of variety when it comes to shooting scenes. Besides, players want to show how pretty your game is as much as you do, they won't focus on these imperfections happening around the scene.

- Camera Tilt
: It is often overlooked, but part of the complete movement of a free camera is being able to tilt it (also called roll depending on the bibliography). Such movement can help a lot in making compositions feel more dynamic or allow the users to shoot a vertical aspect ratio (although we would still very much prefer being able to [hotsample to the desired AR](basics.htm#composing-for-custom-aspect-ratios)).

- No camera clipping
: Having the camera be free to move through geometry can be very useful, as it allows the user to position the camera in those places where it makes the most sense for the shot instead of only in the areas where the photomode allows them to.

- PM settings toggle
: Pretty obvious considering we want to shoot the game itself without any menu getting in the way. Even tho if your game has a feature that automatically outputs the screenshot into a file, giving the user the possibility of taking a pic of the game with their preferred software would also be a nice perk. Additionally, please don't render any kind of watermark on the PM, they get in the way and end up being very distracting to the overall photo.

## Field of View control
Being able to control the "angle of the lens" of the camera is very important, but sometimes these have annoying quirks. We suggest pushing the minimum and maximum limits that the FoV control allows as far as possible, as well as allowing enough granularity in the user interface so the player can choose the right Field of View for their shot.

## Pausing the game / gamespeed control
Being able to pause the game at any given moment to catch the right frame or scene is the first step in setting up the perfect shot. Pausing the game alone isn't enough in most cases, however. Having the ability to skip frames after the game was paused is a welcome addition as well as having the ability to control the gamespeed/time dilation. 

For action shots the gamespeed/time dilation control can turn out to be crucial: having the action flow in slow motion gives the ability to the user to pause the game at the right moment. 


# Extremely nice to have
----
## Dynamic resolution on window mode
This is PC-specific, but being able to [hotsample](basics.htm#hotsampling) is very important for a lot of players to show games at their best. Rendering the shot at a higher resolution leads to a higher image quality and mitigates artifacts. For consoles rendering the final shot at a higher resolution might be a nice addition.

Don't forget to make sure that shaders such as bloom, ambient occlusion, and lightning scale well with bigger resolution and different aspect ratio changes.

## Time of Day Control
If your game has a dynamic time of day, it's most natural to give the user the ability to change the time of day for the shot so the sunlight is just right for the composition they have in mind. Just be sure to allow them to have as much granularity with it as they need.

## Weather Control
As well as with ToD control, if your game has a weather system, allowing the player to cycle between different weathers would give them even more control about the things they can do. Extra points if you add interpolation between different weathers.

Additionally, control over world variables such as wind and fog can also be incredibly helpful.

## Toggle shader effects
Even tho effects such as Vignettes can give a distinct look to your game, real-life photography often tries to get rid of them, so there is no reason for virtual photographers to have to deal with them, especially on a visually ideal medium as games are. So being able to toggle such effects off is very important to players.

Other effects that players tend to want to turn off (or have control over) are:

- Lens flare
- Grain
- Chromatic Aberration
- Depth of Field

Letting the player disable Depth of Field (that being from a cutscene or gameplay) can also be incredibly beneficial. More so if you let the player handle the DOF, but more on that later.

# Nice to have
----
## Light control
Letting the player spawn their own lights to re-illuminate the characters and scene can be a game changer. The controls and UI can be tricky to get right, but we suggest looking at what Insomniac has done with the Spider-Man games and Ratchet & Clank: Rift Apart. And, of course, what Frans has been doing with the [UUU](https://opm.fransbouma.com/uuuv5.htm#lights).

Besides letting the player spawn lights, it's almost equally important to let them turn off the in-game lights. That way they can start lighting the scene from scratch without having to deal with the other lights that don't benefit their composition. An example of what being able to turn off the in-game lights and relit a scene by yourself can achieve:

<div class="slider container" style="aspect-ratio: 4/5">
  <div class="slider__img slider__img-after">
    <p>Reilluminated</p>
    <img src="Images/PhotomodeWishlist/reilluminated.jpg" />
  </div>
  <div class="slider__img slider__img-before">
    <p>Vanilla lighting</p>
    <img src="Images/PhotomodeWishlist/vanilla.jpg" />
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p><i><a href="./GameGuides/re3.htm">Resident Evil 3</a></i>, reilluminated scene (<i>shkegulka</i>)</p></div>

As a side note, being able to modify the game exposure (and with that I mean the actual engine exposure, not rendering a black image on top of the game, yes that has happened) to tweak the impact of lights on the game can be a great addition as well.

## LOD increase
Given that, while we are inside the photomode the game is paused, we don't really engage with it in real-time, meaning that we can instead squish some more image quality out of it. Some games already change their settings to "quality" instead of "performance" when entering the photomode, but going a step further like increasing the Level of Detail of the scene or increasing shadow maps resolution can be of much use for the screenshotters.

## Post-processing control
Besides the effects we mentioned above that we would like to get rid of (or at least have control over), there are also other post-processing effects that we might not want to delete completely, such as bloom. Having control over engine-specific post-processing settings is also useful if the resources allow them.

## Aspect Ratio filters
A lot of users are not really familiar with the concept of Aspect Ratios, nor how a 16:9 screen is not a native AR on photography, and are therefore caged on what games have to offer. The consequence is they are stuck with this TV and computer AR without realizing that other Aspect Ratios such as 3:4 or 2:1 can be incredibly beneficial to what they are trying to achieve.

# Good but can live without them (or can be resource intensive)
----
## Poses and animations
Being able to make our characters more expressive can go a long way in improving portraits and making games feel more alive through shots. Full body poses or animation triggers and different facial expressions are of course welcome.

As always, more granularity and control are always good. So allowing the user to move the head of the character into a specific direction, or their eyes, is very useful to connect with the character better, or just allowing the user to set up their desired composition.

## Move characters/objects around
Setting up a scene is always a welcome addition, but such a system can be expensive resource-wise. Same as with spawning other characters.

## Saving camera positions
Sometimes (especially when tinkering with lights) we want to move the camera to a previous position, so having a way of saving the current position and orientation is a very welcome addition.

## Accumulation buffer based Depth of Field
A lot of real-time DOF solutions look great nowadays ([see Epic's Unreal Cinematic DOF for example](https://docs.unrealengine.com/5.0/en-US/cinematic-depth-of-field-in-unreal-engine/)). However, they come with limitations, like fake bleed of near plane objects, particles, and alpha effects not interacting with the blur correctly, or reflections just straight up not following physics.

Ideally, an accumulation buffer based DOF solution like the one on Forza Horizon 4 and 5 would be the best approach to handling all of the problems mentioned above, as shown in [here](ReshadeGuides/Addons/MSADOF.htm#advantages).

## Adjustable shutter speed for long exposure
Having the option to adjust the shutter speed, even in nonracing games, can be useful for many reasons, one of which is allowing the user to take long exposure photos (like trails of cars passing by). Keep in mind tho that you would also need an option to unpause the game while being inside the pm for this to make sense.

On another hand, decreasing shutter speed might have other benefits specific to games. Some of these can be read about in [here](ReshadeGuides/RealLongExposure.htm).

# Final notes and further reading
----
As you can see, the different mods and tools we use can be quite varied and complex, and getting the right control scheme and UI is definitely a challenge. That's why when it comes to controls, UI, and QoL we recommend checking out what Otis_Inf has been doing with his tools. They all share the same base system that Frans has been iterating on for years now, so it's a good idea to give them a look. For example, if you need a control scheme that is pretty much standardized nowadays I recommend following [the one Otis_Inf describes for his tools here](https://opm.fransbouma.com/generalconfiguration.htm#controls).

It is also worth mentioning that, depending on your game capabilities, you may come up with other cool features, such as [Lord of the Fallen 3D photo](https://youtu.be/TCdROP3U4yg?feature=shared&t=186) or change cosmetics inside the photomode. So don't be afraid to experiment!

Also consider facilitating stuff to modders when possible, like leaving the console or debug tools accessible without much tinkering. Altho we understand how the studio or publisher might not be very happy about such things.

Please take in mind that, even if you follow most of these suggestions, chances are users on PC will still mod the game to fit their screenshotting needs, and that doesn't mean you didn't make a good enough photomode. Things like godmode or being able to pause enemies mid-animation are just some of the things PC players like to use just to mention a few, and they are out of the scope of what a photomode should encapsulate.

If you have any questions about anything written here please reach out to any of the mods listed on the [main page](https://framedsc.com/). We would love to work with you to bring your photomode to the next level!
