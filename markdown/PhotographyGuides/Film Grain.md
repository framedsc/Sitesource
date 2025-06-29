![The Witcher 3](Images/By-Iron-TheWitcher3.jpg "Shot by Iron"){.shadowed .autosize}

@alert important
This is, like all other photography guides on this site, a guideline, not an absolute rule of 'do this or your shot will be bad'. In photography there are no rules, just guidelines which can help you avoid pitfalls. These guides are meant to explain why certain aspects work and once you know why these work, it's up to you to use them to achieve what you're after, or go against them if you want to achieve the opposite.
@end
## Grain and Noise
In photography, grain and noise are visual artifacts that result from how the image is captured/processed, grain refers to the optical effect caused by particles of silver halide crystals that forms during the development of analog (film) photographs, color film grain also has dye clouds (not just silver crystals)

These crystals are light sensitive and have a response curve to them, they vary by size and disturbution depending on the shooting medium (film stock) used, larger crystals lead to **coarser grain** and smaller leads to **softer grains**.

@alert info
Grain structure can also be influenced by the developer's chemistry and agitiation, not just crystal size. Some developers enhance grain (e.g., Rodinal), while others try to minimize it (e.g., fine grain developers like Kodak XTOL). Brief: A photographic developer is a chemical that makes images on a film or print visible.
@end


Saying that, some people see grain as a desirable feature to photos while some others see it as a problem that detracts from the image quality, however, grain is present in a lot of works and is almost unavoidable when shooting analog film and can also sometimes be added to digital works to achieve the film-like look. 

Grain in analog can vary based on light and dark parts in the image, usually there is almost no visible grain in bright spots, because the silver crystals are fully exposed to light, and there is less visible grain in black parts of the image, because there isn't enough light to illuminate the particles there, so grain is more promenint in the shades and tints of the image.


However, dark and light parts of the image can still have visible grain if the film is pushed or developed aggressively becuase that amplifies the signal in those areas, making the grain visible to the naked eye. (same with editing the image in software)

Also Something of note is the trade-off of **film speed (light sensitivity, also known as the film stocks ISO which is pre-determined by the manufacturer)** and **crystal size**, so the bigger the crystals, the more chances of it receiving enough light to go into a developable state, large crystals result in more sensitive film, but at the expense of being visibly grainier and less detailed, and smaller crystals (finer grain) better preserves detail, but requires more light.

@alert info
The amount of film grain can also depend on the definition at which it is observed, for example it can be more noticable in an over-enlarged film photograph. 
@end

On the other hand, **noise** in photography refers to random variatons of color information/brightness in digital camera photography, more so under low-light, high ISO, long exposure times, and heat.


Noise is often colored, it can come in random (R,G,B) dots and or luminance altered dots, that are often dislikable in photography, the noise pattern depends on the sensor, cheap sensors may show [banding](https://framedsc.com/GeneralGuides/how-to-fix-color-banding.htm) or fixed pattern noise, and higher end sensors tend to have more random noise (closer to film grain)

It also can be removed with denoising software without altering the overall look of the image much, but removing grain from analog based media is often invasive and involves altering the overall film look, although some photographers intentionally reduce grain for a cleaner scan.


@alert important
Its crucial to know when implementing grain into your pictures that putting a constant (even) texture like what **lightroom** does by default may not be accurate to how actual analog (film) looks like, we will dive more into getting closer to mimicing real grain later on in the guide.
@end





## Grain Vs Noise

Grain | Noise
--|--  
Film Cameras | Digital cameras
 Organic, textured | Pixel-level, harsh
random sized particles|Random or Patterened dots
Monochromatic or colored | Usually colored (R,G,B Dots)
Artistic/Vintage | Generally undesirable

@alert info
* Grain can be deliberately added for a vintage/film look
* Noise can sometimes be added to mimic film grain
@end

## Why Film Grain?
 #### There are a lot of reasons to use grain, for example, you could use grain to mimic more detail in low lod objects in some games, or try to reduce [banding](https://framedsc.com/GeneralGuides/how-to-fix-color-banding.htm) in the image, more uses for grain include mimicing the film look found in movies, or adding that layer of realism to a shot like it was taken from a real camera,
 Here's a quick comparison of grain vs no grain,
you can see the difference in how the overall image feels much less plasticy:
 <div class="slider container" style="aspect-ratio: 4/5">
  <div class="slider__img slider__img-after">
    <p>With grain</p>
    <img src="Images/After grain fp2.jpg" style="width: 120%; max-width: 600px;"/>
  </div>
  <div class="slider__img slider__img-before">
    <p>Without grain</p>
    <img src="Images/Before grain fp2.jpg" style="width: 120%; max-width: 600px;"/>
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Shot by Ray_st in Frostpunk 2</p></div>
Here's another example from mass effect andromeda:

<div class="figure">
<img src="Images/grain_example_-_grain.jpg" alt="Mass Effect Andromeda" title="Tooltip that appears when you hover" class="autosize shadowed" style="width: 100%; max-width: 400px;" />
<p>Shot by Originalnicodr</p>
</div>
You can see the mountains to the right appear to be have detail to them, Here's a zoomed in comparison with the vanilla shot:
<div class="slider container" style="aspect-ratio: 4/5">
  <div class="slider__img slider__img-after">
    <p>With grain</p>
    <img src="Images/grain_example_-_graincrop_.png" style="width: 120%; max-width: 600px;"/>
  </div>
  <div class="slider__img slider__img-before">
    <p>Without grain</p>
    <img src="Images/grain_example_-_vanillacrop.png" style="width: 120%; max-width: 600px;"/>
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Shot by Originalnicodr in Mass effect andromeda</p></div>


## How to add it to pictures
There are multiple ways to implement film grain into your pictures, we however recommend using [Reshade](https://reshade.me/) as the best way to implement it:

* [Shaderdeck](https://github.com/TreyM/SHADERDECK), actually the Filmdeck shader inside that pack by TreyM is great for emulating the film look. *(free version also available inside the reshade setup)*
* **PD8006_Film_Grain.fx** by prod80, within a shader pack called "Color effects by prod80" in the reshade setup.

* **MartysModsFILMGRAIN.fx** by Marty McFly within the shaderpack "METEOR by Marty McFly" also available in the reshade setup.

However if for any reason you cannot use Reshade to do it, there are other ways to mimic grain:
* Lightroom can actually mimic grain, however, you'd have to mask the highlights, midtones, and shadows of the image and adjust grain manually for each which can be tedious if you have a bunch of images to do, though there is a paid preset which should make this process easier [here](https://vmoldo.com/grain-in-lightroom/)

* Photoshop with a plugin called "Exposure" this plugin has a lot of film like presets which can serve as a starting point for custom edits, or just use them on their own. The plugin's grain implemetation lets you adjust the shadows, highlights and midtones of the grain without extra work which is super convinent for mimicing grain.

You can also add noise to "mimic grain" but this is way less accurate than the methods above. (Not recommended)
* For this you could use free image manupilation software called [Gimp](https://www.gimp.org/downloads/), after you install it from the offical website, drag and drop your desired image inside the editor, go to Filters/Noise then select the type of Noise you want to add, I recommend using HSV Noise, put dulling to 8 and saturation to 0, and play around with the value until you settle on something that looks right according to guidelines in the first section, also feel free to play around with other Noise types and values to see how it looks with it.

## How much grain do I apply?
This depends on your understanding of grain in film photography, for example, Images that appear to be taken at a higher ISO (film speed) should have coarser and bigger grains, while images that  are lower in ISO (film speed) should have finer grain.

This is just one of the aspects you should consider when mimicing real grain in an image, we'd suggest reading more into the first section of the guide to better understand how much or how little to apply if you haven't already.

@alert important
When taking shots in-game its important to turn off film grain until you are finished with everything else in the picture, grain should be added last in the picture (before you want to press the screenshot key) because when shooting it can disturb your clear view of the actual image without grain and lead you to make different decisions regarding the image.
@end
##
*Written by: [NotRay_st](https://x.com/NotRay_st)*

*Last updated on:* 2025/6/29
