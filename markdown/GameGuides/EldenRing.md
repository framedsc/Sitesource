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


## Tips and Tricks

Game doesn't support [hotsampling](../basics.htm#hotsampling), but there are other ways to take high resolution shots in this game. 
You can activate the DSR (Dynamic Super Resolution) from the Nvidia Control Panel, but that will let you go up to 4x multiplier only and you will be limited when it comes to custom aspect ratios.

**I highly recommend** to go [here](../GeneralGuides/custom_dsr_resolutions.htm) to setup as many DSR resolutions you want to take high resolution shots in **different aspect ratios**. This is the best way, and its really everything you need to setup the resolutions and ratios of your [choice](https://i.imgur.com/gfPhRCN.png). This is for Nvidia cards.

For AMD card user, you might wanna tweak VSR (Virtual Super Resolution). I personally do not own the AMD card, but I will leave some useful links that can help you achieve this. [Activating VSR](https://www.amd.com/en/support/kb/faq/dh-010), and [AMD GPU Scaling](https://www.amd.com/en/support/kb/faq/dh2-019). You wanna go with Centered GPU scaling, because its description is similar to Nvidia's No Scaling, though you will have to crop since there is no VSR guide for different aspect ratios for next generation of AMD cards like the one above for Nvidia. So this guide will focus more on Nvidia, with the same idea for the AMD as well.

___
So after you setup everything, make sure to run the game in fullscreen mode and play. When you want to work on a shot, go to video settings and set it to high DSR resolution of your choice that you created with the tool (you don't need to set dekstop resolution to DSR one for this to work). 

Then what you wanna do is press `Alt`+`Enter` to enter the windowed mode which brings you to monitors native resolution. Then you can play with the ReShade, *compose* the shot, and when you are ready to take the high res shot, pressing the `Alt`+`Enter` will switch back to that DSR resolution you set before, and `Alt`+`Enter` again will return you to windowed mode. 

This method is good because you can see entire shot in that particular aspect ratio and even tweak FoV, or compose, however, the rest of the area will be surrounded with black bars, but fear not. Capturing the screenshot will not include those black bars thanks to Nvidia's No Scaling option which you set in Nvidia Control Panel previously. *(example bellow)*


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
<div class="figure"><p>Left: example of the composed ER 3:4 shot at resolution of 3037x4050 surrounded by the black bars on 16:10 monitor. Right: example in windows after the shot was taken. So you get nice crisp 3:4 image result, no black bars.</p></div>

@alert tip
You can access the video settings even if your game is paused, while the free cam is on! 
This can be really useful if you want to switch to different aspect ratio while not ruining your perfectly alligned action shot. Just you gotta do this with keyboard and mouse if the camera control device is set to `Gamepad` in tools. If its set to `KeyboardMouse`, then you can access the menu with controller. If its set to `Both` it will not work. Don't forget to turn the `HUD` back on otherwise you won't see the menu after pressing the esc.
@end

Let say that you are on 21:9, or 16:9, but you realised that 3:4 would suit better for this moment, or 1:1, or you just want to experiment, so you press esc, and navigate with a mouse (if the camera control device is set to `Gamepad` in tools) to video settings to pick the resolution of your choice and it will instantly switch to that DSR resolution! You can do this as many times as you want. Honestly I never experienced crashes while doing this countless of times in one play session of 4 hours.

Having the beefier card will make these things significantly more easier of course (you can even play the game in 5k), but as an example, to give you general idea, I have GTX 1060 6GB and I am still able to take high resolution shots from this game. Its a bit slower progress of course because sometimes, if not always, I tweak FoV while I am running the game at high DSR res, because if your monitor is 16:9 ratio, and you want to take the shot on 21:9, you will need to compose a bit on that DSR res and it can be quite laggy especially if you turned on Higher LODs from the tools. But I still do it, even up to 5760x2468 depends on the area, just with much lower fps then what would one have with the better card. 

In Lurnia Of The Lakes I struggle a bit with the fps on high settings, so there, I tone down my demands to 5040x2835 for 21:9, 2868x3825 for 3:4 and 3150x3150 for 1:1. So I recommend to test lots of DSR resolutions to find the best ones for your card.  
If you have RTX 4090, *don't think too much*.

## Useful Links

* [PC Gaming Wiki](https://www.pcgamingwiki.com/wiki/Elden_Ring)
* [Cheat Table](https://www.nexusmods.com/eldenring/mods/48?tab=files) Useful CT if you want to re-spawn certain bosses for shots etc.
* [Cheat Engine Tables Guide](../GeneralGuides/cheat_engine_tables.htm)
* [Skip the intro logos and remove white startup screen](https://www.nexusmods.com/eldenring/mods/421)
* [Elden Mod Loader](https://www.nexusmods.com/eldenring/mods/117) 
* [Metis Mod Launcher](https://www.nexusmods.com/eldenring/mods/117) 
* [Mod Engine 2](https://github.com/soulsmods/ModEngine2/releases)