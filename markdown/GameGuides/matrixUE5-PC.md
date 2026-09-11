![City Sample](Images\matrixUE5-PC_header.png "Shot by barkar-b"){.shadowed .autosize}

## Summary

Feature | Supported
--|--
Vanilla Photo Mode | Yes
Hotsampling | Yes
DSR | Yes
Custom Aspect Ratios | Yes
Reshade | Yes (DX12)
Ansel | No
Graphics API | DirectX 12

@alert neutral  
This guide covers the compiled [City Sample project](https://unrealengine.com/marketplace/en-US/learn/city-sample) for PC, not the released demo for consoles.  
@end

@alert important  
**The [Universal Unreal Unlocker](../GeneralGuides/universal_ue4_consoleunlocker.htm) does not currently support UE5.** It's also not necessary here, as the available console provides access to a simple freecam and timestop.  
@end

## Console commands

The console is available by default, bound to `~`. If `~` isn't working for you, your keyboard might have to be switched to an English layout.

These are some useful commands that can be typed in via the console, or set in `Scalability.ini` and `Engine.ini`. Both are located in `~\CitySample\Saved\Config\Windows`. In case of emergency, refer to [our UE4 guide](../GeneralGuides/ue4guide.htm). Note that not all the info in that guide is applicable here, as this is a new version of UE.

Command | Arguments | Description
-- | -- | --
`toggledebugcamera` | - | Toggles the free camera, surprisingly. Note that you won't be able to access the Photo Mode or World Setting options when in this mode.
`pause` | - | You won't believe this, but this pauses the game. Type `pause` again to unpause. If you want to fly around when paused, type `toggledebugcamera` after you've paused the game.
`fov` | `0` - `180` | Sets the field of view. Use this if you find the Focal Length option in Photo Mode too limiting. `0` resets FoV so Focal Length works again.
`ScaleCrowdCount` | - | Multiplies number of NPCs (including cars) in the scene.
`MassTraffic.SpeedLimitScale` | - | Setting this to `0` stops all traffic.
`r.ScreenPercentage.MaxResolution` | - | Sets maximum resolution before [TSR](https://videocardz.com/newz/unreal-engine-5-early-access-features-temporal-super-resolution-upscaling-technology) kicks in. Set this to `-1` to disable TSR entirely.
`r.Streaming.LimitPoolSizeToVRAM` | `0` / `1` | If `1`, texture pool size will be limited to how much GPU memory is available.
`r.MipMapLODBias` | `-15` - `15` | Applies additional mipmap bias for all textures. Changes texture detail in the distance.
`r.Tonemapper.Sharpen` | `0.1` - `10` | Sharpens the image, useful against blurry TAA.
`sg.PostProcessQuality` | `0` - `5` | Setting this to `0` removes the vignette and colour fringing.
`DisableAllScreenMessages` | - | Gets rid of those annoying warnings about your GPU being close to dying.

#### FULL BORE!
Paste this in if you want your computer to burn:  
```
r.Streaming.LimitPoolSizeToVRAM 0 | r.MipMapLODBias -15 | r.DepthOfFieldQuality 5 | r.motionblurquality 0 | sg.PostProcessQuality 0 | r.ScreenPercentage.MaxResolution -1 | r.ToneMapper.Sharpen 1
```

Equivalent to the *High end screenshots* set of commands in the UE4 guide. The other commands don't appear to do much for this.

## Capturing high-res screenshots

Using `HighResShot` is not recommended as it causes artifacts when zoomed in. Try [hotsampling](..\basics.htm#hotsampling) with SRWE (with TSR disabled for native target resolutions) to capture high-res shots.

MSI Afterburner is unstable with DX12 titles, causing the demo to crash on startup. If MSI Afterburner is your preferred method of capture, you may launch it after you've launched the demo.