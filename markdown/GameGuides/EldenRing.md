![Elden Ring](Images\eldenring_header.png "Shot by StephenCalic"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | Yes (with tools)
Reshade | Yes
Ansel | No
Graphics API | DirectX 12
Game version | 1.10.1
 
## Tools

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**[Features](https://opm.fransbouma.com/Cameras/eldenring.htm)**: Camera control(Also in cut scenes), FoV control, HUD toggle, timestop/gamespeed, Pillarbox/letterbox removal in custom aspect ratios (UW support), Higher LODs

### Support
* [Cheat Table](https://www.nexusmods.com/eldenring/mods/48?tab=files) Useful CT if you want to re-spawn certain bosses for shots etc.
* [Cheat Engine Tables Guide](../GeneralGuides/cheat_engine_tables.htm)
* [WeMod Trainer](https://www.wemod.com/cheats/elden-ring-trainers) Features Day Time +1 hour, Freeze Day Time, Freeze Enemies Position and more.
* [Internal](https://github.com/NightFyre/ELDENRING-INTERNAL)

## Tips and Tricks

Game doesn't support [hotsampling](../basics.htm#hotsampling), but there are other ways to take high resolution shots in this game. 
You can activate the DSR (Dynamic Super Resolution) from the Nvidia Control Panel, but that will let you go up to 4x multiplier only and you will be limited when it comes to custom aspect ratios.

**I highly recommend** going [here](../GeneralGuides/custom_dsr_resolutions.htm) to setup as many DSR resolutions as you want to take high resolution shots in **different aspect ratios**. This is the best way, and it's really everything you need to setup the resolutions and ratios of your [choice](https://i.imgur.com/gfPhRCN.png). This is for Nvidia cards.

For AMD card users, you might want to tweak VSR (Virtual Super Resolution). I do not own an AMD card, but I will leave some useful links that can help you achieve this. [Activating VSR](https://www.amd.com/en/support/kb/faq/dh-010), and [AMD GPU Scaling](https://www.amd.com/en/support/kb/faq/dh2-019). You wanna go with Centered GPU scaling, because its description is similar to Nvidia's No Scaling. However, you will have to crop since there is no VSR guide for different aspect ratios for next generation of AMD cards like the one above for Nvidia. So this guide will focus more on Nvidia, with the same idea for the AMD as well.

___
### First Method
So after you set up everything, make sure to run the game in fullscreen mode and play. When you want to work on a shot, head over to video settings and set it to the high DSR resolution of your choice that you created with the tool (you don't need to set your desktop resolution to DSR one for this to work). 

Then what you wanna do is press `Alt`+`Enter` to enter the windowed mode which brings you to monitor's native resolution. Then you can play with the ReShade, *compose* the shot, and when you are ready to take the high-res shot, press the `Alt`+`Enter` to switch back to previously set DSR resolution. 
Press `Alt`+`Enter` again to return to windowed mode. 

This method is good because you can see the entire shot in that particular aspect ratio and even tweak FoV, or compose, however, the rest of the area will be surrounded with black bars, but fear not. Capturing the screenshot will not include those black bars thanks to Nvidia's No Scaling option that you had previously set in Nvidia Control Panel. *(example bellow)*


<div class="slider container" style="aspect-ratio: 16/9">
  <div class="slider__img slider__img-after">
    <p>IN WINDOWS WITHOUT BLACK BARS</p>
    <img src="../Images/EldenRingGuide/EldenRingWindowsPhotoView.jpg" />
  </div>
  <div class="slider__img slider__img-before">
    <p>IN GAME WITH BLACK BARS</p>
    <img src="../Images/EldenRingGuide/EldenRingBlackBars.jpg" />
  </div>
  <input type="range" min="0" max="100" value="50" step="0.01" 
    id="slider" class="slider__input" 
    autocomplete="off" onwheel="this.blur()" 
  />
</div>
<div class="figure"><p>Left: example of the composed ER 3:4 shot at resolution of 3037x4050 surrounded by the black bars in 16:10 monitor. Right: example in windows after the shot was taken. So you get a nice crisp 3:4 image result, no black bars.</p></div>

This method comes with a penalty though, which is needing to compose a shot on high-resolution. For instance, if you align your shot in 16:10 and then switch back to 3:4, you will need to make some adjustments in the 3:4 aspect ratio.

Having the beefier card will make these things significantly much easier of course (you can even play the game in 5k), but as an example, to give you a general idea, I have GTX 1060 6GB and I am still able to take high-resolution shots from this game. 

Its a bit slower progress of course with the first method because sometimes, if not always, I tweak FoV while I am running the game at high DSR res because if your monitor has a 16:9 ratio, and you want to take the shot in 21:9, you will need to compose a bit on that DSR res and if you turned on Higher LODs from the tools along with ReShade it can be quite laggy. But there is also the other way of taking the high-res shots in this game.

### Fullscreen Way
@alert tip
You can access the video settings even if your game is paused, while the free cam is on! This can be useful if you want to switch to different aspect ratios in fullscreen mode while not ruining your perfectly aligned shot. You just gotta do this with a keyboard and mouse if the camera control device is set to `Gamepad` in tools. If it's set to `KeyboardMouse`, then you can access the menu with the controller. If it's set to `Both` it will not work. Don't forget to turn the `HUD` back on otherwise you won't see the menu after pressing the `ESC`.
@end

Let's say that you are in 21:9, or 16:9, but you realised that 3:4 would suit you better for this moment, or 1:1, or you just want to experiment, so you press `ESC`, and navigate with a mouse (if the camera control device is set to `Gamepad` in tools) to video settings to pick the resolution of your choice and it will instantly switch to that DSR resolution! You can do this as many times as you want. Honestly, I never experienced crashes while doing this countless of times in one play session of 4 hours.

It's really rare to happen, but keep in mind that this method sometimes won't work if you press the `Alt`+`Enter` or the `Windows` key for some reason or by accident. You will see the menu, but you won't be able to access it. So pay attention to that if you want to use this method straight away, or reset to refresh if the menu bug out, combine. But like I said it's rare, and it will only happen if you `Alt`+`Tab` too much while you are in a custom aspect ratio.

## Resembling Hotsampling

If you are dedicated, you can generate lower custom DSR resolutions with the tool only for composing, then do the [fullscreen](../GameGuides/EldenRing.htm#fullscreen-way) menu trick to go to much higher res in that aspect ratio to take the shot and also the same way to return to lower one. Avoid setting custom DSR resolutions too low, because it will crash your game. Generated resolutions shouldn't have lower width/height than your monitor's native one. In my case, I went with x1.5 for 21:9, and x2.25 for 3:4. Any lower caused my game to crash.

Another helpful tip is to check other [tools](https://i.imgur.com/dRk02S8.png) that support hotsampling. This way, you can find aspect ratio resolutions offered for your monitor that can be used with the DSR tool.

I recommend testing lots of custom DSR resolutions to find the best ones for your card.

If you have RTX 4090, *don't think too much*.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Elden_Ring)
* [Skip the intro logos and remove white startup screen](https://www.nexusmods.com/eldenring/mods/421)
* [Elden Mod Loader](https://www.nexusmods.com/eldenring/mods/117)
* [Metis Mod Launcher](https://www.nexusmods.com/eldenring/mods/117) 
* [Mod Engine 2](https://github.com/soulsmods/ModEngine2/releases)
* [More Armors](https://www.patreon.com/MaxTheMiracle)
* [More Mounts](https://www.nexusmods.com/eldenring/mods/991) You can also type **Mount** in nexus search bar to check for more mounts.
* [New Idle Animations](https://www.nexusmods.com/eldenring/mods/2397)
* [Dynamic Shadows](https://www.nexusmods.com/eldenring/mods/991) 
