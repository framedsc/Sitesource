![LUT Generation!](Images\lutg_header.png)

LUTs are a powerful tool that can completely change the look of any picture. This guide is geared towards generating LUTs for usage in ReShade, however, this guide remains useful if you're into photo editing and anything based around colours in general.

---

## Why would I want to use a LUT?

LUTs (Look-up Tables) are a cheap way of changing the colours of your game without having to rely on a huge stack of shaders that eats at your performance. You can use them to make in-game colours look more natural (colour correction), or give your game a certain stylised look (colour grading).

### How do I use a LUT?

You'll need one of these:

![This is a Neutral LUT](Images\lutguide\lut_neutral.png){.shadowed .autosize}

This is a LUT. More specifically, this is a **neutral** LUT. It does absolutely nothing, but is the starting point for *everything* you can do with LUTs.

@alert important
**This texture is incredibly important!** It is the LUT itself, after all. Make sure you have it! You can either download the above texture, or it can be found in the standard `reshade-shaders` Textures folder as `lut.png`. **Back it up** somewhere, you'll want copies of this texture.
@end

 ReShade uses the shader `LUT.fx` to load and apply this. Note that `LUT.fx` only handles **one** (1) LUT, and I highly recommend this single LUT to be your colour correction LUT. You can have multiple LUTs and switch through them with the `MultiLUT.fx` shader, which will be covered later on.

 ### What now?

 This guide is split into three parts (for now), covering generation of LUTs using Photoshop or Lightroom, and the usage of the `MultiLUT.fx` shader.

---
## Adobe Photoshop
What you'll need:  
- at least one screenshot from your game  
- Adobe Photoshop CS4 or newer *(requires Adjustment Layers)*

*I will be using Photoshop CC 2019. The game screenshot is from GreedFall.*

#### Step 0: Screenshot Collage
While not necessary, creating a collage of various screenshots will ensure that the effects of your LUT still look great in different scenes. They should cover various times of day and locations! This is important if you're making a corrective LUT.

#### Step 1: Adjustment Layers
With your screenshots loaded into Photoshop, it's time to get to work. I'll be focusing on colour grading the screenshot I have loaded. Start by adding an Adjustment Layer from the Adjustments tab.

![Photoshop Import](Images\lutguide\lutg_ps-adj1.png){.shadowed .autosize}

**Use as many adjustment layers as you want!** Don't hesitate to abuse them, as they all get baked down into a texture at the end. If you're going for style, go ahead and play with the weirder adjustments like Posterize and Threshold. 

Once you've had your fun, you should have a few extra layers on your right. 

![Photoshop Adjusted](Images\lutguide\lutg_ps-adj2.png){.shadowed .autosize}
*Curves for contrast, Vibrance for saturation, Color Balance for split-tones, H/S for selective colours (desaturated greens)*

@alert important
This is **not** a guide on editing images. If you'd like to learn how to use these adjustment layers, I recommend [this guide by How-To Geek](https://www.howtogeek.com/274714/what-are-adjustment-layers-in-photoshop/) as a quick introduction to them.
@end

You may have noticed the chain & white canvas next to your adjustment layer icons.  

![Masks!](Images\lutguide\mask.png){.shadowed .autosize}

**Ignore these.** These are masks for the adjustment layers. **Adjustment masking** (for obvious reasons) **will not transfer to your LUTs.**

#### Step 2: The LUT
Next, you want to load in the neutral LUT texture from earlier as a separate document. **Make sure that it's the neutral one.** If not, you'll end up with really weird colours once you're done.

All you need to to here is copy the adjustment layers from your screenshot document to the new LUT document. This can be done by the traditional Ctrl+C / Ctrl-V, or you can select all adjustment layers, right-click, `Duplicate Layers...` and choose the LUT document.

![Photoshop LUT](Images\lutguide\lutg_ps-lut.png){.shadowed .autosize}

Depending on the extent of your adjustments, the LUT may look weird. My LUT shown above starts to look really off towards the left of the image, but that's because I desaturated the greens completely. If you've done everything right, there should be no worry here.

#### Step 3: Exporting
The final step is to export the image as a **PNG**. Do **not** export it in a lossy format like JPG, you do not want compression artifacts in a LUT. Unless you're going for a weird corrupted effect. 

I would recommend exporting this file as `lut.png`, saving right into your Textures folder and replacing the previous `lut.png` that was in there. This makes it so you can use your LUT right away with `LUT.fx`.

#### Extra: .CUBE, .3DL and other 3DLUT formats
LUTs found online typically will not look like those that we're familiar with here, usually being in the form of .CUBE, .3DL, .CSP, .ICC, etc. They can be used by applying them with the Color Lookup adjustment layer to your neutral LUT document.

---

## Adobe Lightroom
What you'll need:  
- at least one screenshot from your game  
- Adobe Lightroom

*I will be using Lightroom CC 2019, not Lightroom Classic. Outside of a few UI differences, the overall steps are identical. The game screenshot is from Mass Effect: Andromeda.*

#### Step 0: Screenshot Collage
While not necessary, creating a collage of various screenshots will ensure that the effects of your LUT still look great in different scenes. They should cover various times of day and locations! This is important if you're making a corrective LUT.

#### Step 1: Making the Preset
Import your screenshot(s) into Lightroom. If you've never used Lightroom before, don't worry, it's pretty straightforward. You have all your tools on the right (they'll be under Develop in Lightroom Classic), just play around with them and see what results you get!

![Lightroom Import](Images\lutguide\lutg_lr-adj1.png){.shadowed .autosize}

@alert important
This is **not** a guide on editing images. *N.B.: I couldn't find any decent guides to wrangling Lightroom. Ghost, make one!*
@end

After a few minutes of messing around, this is my result.

![Lightroom Adjusted](Images\lutguide\lutg_lr-adj2.png){.shadowed .autosize}

Once you're happy with yours, save it as a preset.   
**Do NOT include Texture, Clarity, Dehaze, Vignette, Grain, Sharpening, Noise Reduction and any lens correction in your preset.** This will completely ruin your LUT.

#### Step 2: The LUT
Import the neutral LUT texture from earlier. **Make sure that it's the neutral one.** If not, you'll end up with really weird colours once you're done.

Apply your saved preset to the neutral LUT.

![Lightroom LUT](Images\lutguide\lutg_lr-lut.png){.shadowed .autosize}

Depending on how much you modified your image, the LUT may look weird. My LUT shown above is quite washed out and overexposed, due to the extent of the changes I made to it. I'm not concerned though, as these changes were intended.

#### Step 3: Exporting

The final step is to export the image as a **PNG**. Do **not** export it in a lossy format like JPG, you do not want compression artifacts in a LUT. Unless you're going for a weird corrupted effect. 

If you're *not* using Lightroom Classic, you have an additional step before you get to save as a PNG. You will need Photoshop for this. Under File, choose `Edit in Photoshop...`. This will automatically launch Photoshop with your LUT already loaded, ready to save. Export as PNG like you normally would.

I would recommend exporting this file as `lut.png`, saving right into your Textures folder and replacing the previous `lut.png` that was in there. This makes it so you can use your LUT right away with `LUT.fx`.

#### Extra: Lightroom presets
If you're an avid Lightroom user, chances are you already have presets made/downloaded. Just continue from Step 2 onwards, using the presets you have on hand.

---

## MultiLUT
`MultiLUT.fx` is a shader that allows you to load in multiple LUTs and switch between them, as the name would imply. It does this by collecting the LUTs in an atlas.

![MultiLUT Atlas](Images\lutguide\multilut.png){.shadowed .autosize}

This is the default MultiLUT atlas. You're this far down in the guide, you should know what a LUT looks like. So you should be able to tell that each row of this mess of boxes is a separate LUT. 

You can use this shader as is, or *you can modify it*.

Modification is simple enough, just replace each row of LUTs with one of the many you've surely made by now. I would recommend keeping the top LUT as is; it's a neutral LUT.

### Renaming the LUTs
You may not want your LUTs to be named `Color 1`, `Color 2`, `Color 3 (Blue oriented)` and so on, so this is how you can modify the shader file so that they're named the way you want.

@alert tip
Use the ReShade GUI whenever you are modifying a shader file (ReShade 4.0+, under the Statistics tab). With a key bound to reload ReShade, you can check what your modifications are doing on-the-fly. This is helpful to make sure your syntax is correct.
@end

After opening the shader file, look for Line 31:
```
ui_items="Neutral\0Color1\0Color2\0Color3 (Blue oriented)\0Color4 (Hollywood)\0Color5\0Color6\0Color7\0Color8\0Cool light\0Flat & green\0Red lift matte\0Cross process\0Azure Red Dual Tone\0Sepia\0\B&W mid constrast\0\B&W high contrast\0";
``` 
This is the line we want to edit to give our LUTs custom names. `\0` acts as the separator between the names, so don't remove that.

Let's say we added 4 of our own LUTs, replacing the second to fifth LUTs of that atlas (remember, first is neutral!). Now we want to give them names, I'll use the NATO alphabet for simplicity's sake: Alfa, Bravo, Charlie, Delta.

Line 31 should now look like this:
```
ui_items="Neutral\0Alfa\0Bravo\0Charlie\0Delta\0";
``` 
We've removed the excess names since we just want to use your LUTs. Don't worry, ReShade will ignore them with no issue. 

You can continue modifying the names to your own need. If you want to use quotes in your LUT names, don't use `"`. This ends the line and will cause errors. You'll want to use `'` instead.

### Adding more LUTs
The default atlas contains 17 LUTs, but if you have made more and would like to add them, the shader file once again needs to be modified to accommodate them. Once your atlas is fully compiled, you want to edit Line 20:
```
#define fLUT_LutAmount 17
```
Change 17 to the number of LUTs you now have.

### LUT variants and changing the atlas
Sometimes you may come across LUTs that have more tiles or have a different tile size, such as those generated using qUINT Lightroom with modified tiles. Or you may have found a different MultiLUT atlas that you'd like to use.  
```
#define fLUT_TextureName "MultiLut_Atlas.png"
```
Line 11 controls the name of the atlas file. If you have multiple atlases that you'd like to change to, just change the name of the PNG listed. Keep in mind that names obviously will not transfer.
```
#define fLUT_TileSizeXY 32
```
Line 14 controls the tile size, or the size of each box in a LUT. 32 refers to both width and height of each box, since they're squares. You may have to count pixels if the LUT you've found has a different tile size. (tip: use the height of your LUT, since height = width of each tile.)
```
#define fLUT_TileAmount 32
```
Line 17 controls how many tiles there are. This may differ if the LUT you found is meant to have higher precision (or lower). You will have to count the number of tiles (or divide width of the entire LUT by its height).

---
*last updated 12th October 2019*  
*written by moyevka*

