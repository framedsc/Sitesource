![MSADOF](../../Images/MSADOF/MSADOF_header.png){.shadowed .autosize}

**Multi-sampled Accumulated Depth of Field** (**MSADOF**) is an advanced DOF add-on developed by murchalloo. It allows users to render bokeh without the use of a depth buffer, greatly increasing the possibilities of defocused captures. This is an advanced guide that aims to cover the usage of MSADOF, as well as its setup process for you and other users.

@alert important
MSADOF requires **ReShade 5.2+ with full add-on support** and supported [Otis_Inf camera tools](https://patreon.com/Otis_Inf). *All cameras newer than the 31st of May 2022 should have support for MSADOF, look for "interpolation factors" in the camera changelogs.*
@end

@alert neutral
The add-on is currently in closed beta and is unavailable for public download.
@end

---

## Advantages

MSADOF works by manipulating the game camera around a certain plane in space and progressively blending the result to produce a defocused image that's depth-accurate. This results in:

<div class="slider container" style="aspect-ratio: 43/18">
  <div class="slider__img slider__img-after">
    <p>MSADOF</p>
    <img src="../../Images/MSADOF/comp_nearplane_MSADOF.jpg" />
  </div>
  <div class="slider__img slider__img-before">
    <p>Traditional depth-based DOF</p>
    <img src="../../Images/MSADOF/comp_nearplane_CineDOF.jpg" />
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Accurate near-plane bleed.</p></div>

<div class="slider container" style="aspect-ratio: 43/18">
  <div class="slider__img slider__img-after">
    <p>MSADOF</p>
    <img src="../../Images/MSADOF/comp_refl_MSADOF.jpg" />
  </div>
  <div class="slider__img slider__img-before">
    <p>Traditional depth-based DOF</p>
    <img src="../../Images/MSADOF/comp_refl_CineDOF.jpg" />
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Depth-accurate reflections.</p></div>

<div class="slider container" style="aspect-ratio: 3/2">
  <div class="slider__img slider__img-after">
    <p>MSADOF</p>
    <img src="../../Images/MSADOF/comp_trefl_MSADOF.jpg" />
  </div>
  <div class="slider__img slider__img-before">
    <p>Traditional depth-based DOF</p>
    <img src="../../Images/MSADOF/comp_trefl_CineDOF.jpg" />
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Complex defocusing of transparent reflections.</p></div>

<div class="slider container" style="aspect-ratio: 3/2">
  <div class="slider__img slider__img-after">
    <p>MSADOF</p>
    <img src="../../Images/MSADOF/comp_hair_MSADOF.jpg" />
  </div>
  <div class="slider__img slider__img-before">
    <p>Traditional depth-based DOF</p>
    <img src="../../Images/MSADOF/comp_hair_CineDOF.jpg" />
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Alpha hair in DOF!</p></div>

---

## Installation

MSADOF comprises of two files, `IgcsConnector.addon` and `MSADOF.fx`. The first of which is a ReShade add-on, and the second a ReShade shader. The ADDON file is installed in the same directory as your game EXE, while the FX file is installed to your reshade-shaders\Shaders folder.

Once installed, upon opening the ReShade GUI, you will now see a new window. This is where you will control the bulk of MSADOF. You must also enable `MSADOF_ADDON` and drag it all the way to the bottom of your shaders list.

### Initial Setup

For the add-on to function as intended, it's typically necessary to enable v-sync in your game. Motion blur should also be disabled.
Below, in the table, you will find the MSADOF values for games that have been tested. 

These values have to be added in the `Tweaking Mode` part of the addon. 
For this, when loaded, click on `Switch Mode`. Scroll down, expand `Game Adjustements` and add the values. You may also have to change some in the `DOF Setting`
Keep in mind that the `Skip Frame` value may differ on your system. 

![Example DOF Settings and Game Adjustements](../../Images/MSADOF/MSADOF_Addon_tweakingMode_01.png){.shadowed .autosize}

### List of values

| Game                          | Near Plane         | FOV | Variable</br> Near Plane |Skip</br>Frame | Camera</br>Multiplier | Flip X/Y |Comments|
|-------------------------------|----------------------------------|-----|---------------------|--------------------------|-------------------|----------|--------|
| Ace Combat 7                  | 1                                | 180 | Y                   | 2                        | 0.1               | X        ||
| Alien: Fireteam Elite         | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| Assassin's Creed Odyssey      | 0.0995                           | 180 | N                   | 2                        | 0.001             | X        ||
| Assassin's Creed Origins      | 0.0995                           | 180 | N                   | 2                        | 0.001             | X        ||
| Batman: Arkham Knight         | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| Beyond a Steel Sky            | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| Borderlands 3                 | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| Blind Fate: Edo no Yami       | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| Code Vein                     | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| Cyberpunk 2077                | 0.02                             | 180 | N                   | 4                        | 0.001             | X        ||
| Days Gone                     | 9.95                             | 320 | N                   | 1                        | 0.1               | X        |Might require raytracing / a low framerate under vsync targets.|
| Draugen                       | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| ECHO                          | 0.56                             | 180 | N                   | 2                        | 0.1               | X        |No custom AR possible|
| Elden Ring					| 0.0500						   | 180 | N				   | 2						  | 0.001 - 0.01	  | X        |In some areas the camera multiplier may have to be changed|
| Hellblade                     | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| Kena: Bridge of Spirits       | 9.9965                           | 180 | Y                   | 4                        | 0.1               | X        ||
| Life is Strange: True Colors  | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| Mortal Shell                  | 9.9965                           | 180 | Y                   | 4                        | 0.1               | X        ||
| MotoGP 19                     | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||
| Resident Evil 2			    | 0.01                             | 180 | Y                   | 1                        | 0.001             | X        ||
| Resident Evil 3			    | 0.01                             | 180 | Y                   | 1                        | 0.001             | X        ||
| Scarlet Nexus                 | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| Star Wars - Jedi Fallen Order | 9.9995                           | 180 | Y                   | 1                        | 0.1               | X        ||
| Stray						    | 0.5625                           | 180 | N                   | 1                        | 0.1               | X        ||
| Tell Me Why                   | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| The Ascent                    | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| The Medium                    | 2                                | 180 | Y                   | 3                        | 0.1               | X        ||
| The Shore                     | 9.9965                           | 180 | Y                   | 1                        | 0.1               | X        ||
| The Witcher 3 : Wild Hunt     | gameplay : 0.2 - Cutscene : 0.4  | 180 | N                   | 0                        | 0.001             | X        ||
| Twin Mirror                   | 9.9965                           | 180 | Y                   | 2                        | 0.1               | X        ||


If you have to adjust for your game, follow the [advanced setup section](#adjusting-for-a-new-game) further below.

---

## Usage

Once the add-on is configured, press `Ctrl+B` to begin the render. The final image is automatically saved to the same folder where your game EXE is located.

The add-on also supports hotsampling! Simply start the render after hotsampling.

### DOF Settings

This is the category you'll most likely be configuring the most, as it's where you'll be adjusting your focus distance.

**Shape size**  
This controls how large your bokeh will be. 

**Focus distance**  
This sets the focal plane. The arrows on the right change the step size of the slider.

**Increase focus precise at close range**  
This changes the scaling of the focus distance slider. Higher values mean that the focus distance slider can operate in even smaller steps.

**HDR Log Whitepoint**  
Affects how bright pixels stack atop each other during the accumulation process.

**Frames to skip**  
Skips camera movement of every few frames to make accumulation more consistent. Depending on the performance of your game, this value might have to be changed. If you notice that the add-on is drawing rings/donuts on your focus plane, this value likely has to be changed.

**Frames to wait**  
Similar to above, this value should only be changed if you notice that the focus plane isn't properly sharp.

**Show focus plane**  
Overlays a plane on screen. Where the plane intersects the scene is where your focus distance is.

**Show rendering progress**  
Displays a progress bar.

**Save 32-bit EXR**  
As the accumulation process can introduce banding, this option stacks the accumulated frames into a higher-precision buffer, alleviating the banding. The saved EXR requires further post-processing to produce the intended result.

### Shape settings

These controls configure the shape of the bokeh circles.

**Preview size**  
Changes the scale of each point only in the preview window above it.

**Number of rings**  
Changes the number of rings in each bokeh circle. This value affects render time. Increase it if you notice undersampling (each point is clearly visible), decrease it if render times are taking too long.

**Points on first ring**  
This sets the density of the points on each ring. Similarly, this affects render time.

**Anamorphic scale**  
Stretches/squashes the bokeh circle. Useful for replicating oval bokeh characteristic of anamorphic lenses.

**Offset value / Offset type**  
Affects the alignment of every point relative to the previous ring. Typically unnecessary to modify.

**Swirl scale**  
Introduces swirl to bokeh, useful for Helios-style swirly bokeh.

**Fringing scale**  
Modifies how much the inner rings are darkened to introduce fringing to the bokeh.

**Fringing power**  
Modifies the falloff of the darkening to sharpen the fringing.

@alert info
Fringing and swirling require their respective boxes to be ticked in the MSADOF shader (*not add-on!*) settings.
@end

### Additional info

This category displays useful as well as debug information. 

### Game Adjustments

This category is to be left alone, as it is for first time configuration of a new game.

---

## Adjusting for a new game

If you're playing a game that does not have an `MSADOF.ini` yet, this is the process of setting up the *Game Adjustments* tab.

#### 1. Checking X and Y

Before adjusting anything, do a quick render to judge the shape of the bokeh. You may have to adjust *Camera movement multiplier* and/or bring up *Focus distance* if the shape size is too dramatic.

If the shape of the rendered bokeh is not perfectly circular, the **Flip X** and **Flip Y** checkboxes have to be configured. Mess around with them until the rendered result is circular.

#### 2. Calibrating the focus plane

This step requires quite a bit of trial & error, as it involves messing with *Focus distance* until the focus plane is found. 

If you're struggling to find an area in focus, you might have to configure *Frames to skip*. The add-on drawing rings/donuts is usually a tell-tale sign of this.

![ringing example](../../Images/MSADOF/ringing.png){.shadowed .autosize}

Once you've managed to find the focus plane, adjust **Camera near plane** with *Show focus plane* ticked until the focus helper plane aligns with the actual focus plane. 

#### 3. Max FOV Value

This value typically does not have to be changed from 180. For Unreal Engine games, the value should be 320 instead.

#### Done!

This process acts as calibration of the focus helper plane to the actual focus plane, so it can be used to help you set a focus point.


---

## Tips & Tricks

### Preview bokeh size  
You can perform a quick preview of how large your bokeh shape size will be by doing a render with a very low *Number of rings*.

### Best-case scenario

To get the best possible result out of this add-on, it's best to find a game that can perfectly timestop with no significant jitter, foliage sway, or anything that could interrupt the render. 

Raytracing / specular highlight noise is often the cause of 'dirty' bokeh circles.

### Undersampling

A DOF shader can be used as a blurring pass before rendering to help and smooth out undersampling artifacts. Simply align the DOF shader's focus point to that of the add-on's and make the DOF strength very subtle. **Do not** use autofocus here, as the autofocus point will slip due to the camera movements.

### Overexposed pixels

Because of how the add-on stacks bright pixels to boost highlights, this can result in severely overbright highlights. This can be diminished by using a Levels shader beforehand to bring down the whitepoint slightly, affecting the stacking process.

### Antialiasing & image sharpness

The camera-based nature of the shader means it does its own antialiasing! AA can be entirely disabled in your game to get a sharper image. 

In titles where TAA is integral to shading (Cyberpunk 2077 and its hair, for example), it can be left enabled at the cost of a slightly softer image. 

It is **not** recommended to have a sharpening pass prior to the render. Sharpening halos may become exaggerated and/or show up in the accumulation process.

### Have fun with shaders!

This add-on works great with ReShade shaders too! In fact, using a LUT prior to the render and saving the result in EXR can reduce colour banding, thanks to the stacking process. 

---

## Processing saved EXRs

The saved EXRs require gamma correction to look as they did on your screen, instead of a washed-out image. This is easiest done with Adobe Photoshop, however any editor that can open EXRs and perform gamma correction would also work.

The EXRs are saved in linear gamma (gamma 1.0), so a simple gamma correction of 0.454545... (repeating) returns an image at the proper sRGB gamma of 2.2.

This can be done with *Image* > *Adjustments* > *Exposure...* / the Exposure adjusment layer in Photoshop.