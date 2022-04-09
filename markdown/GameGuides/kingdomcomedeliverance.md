![Kingdom Come: Deliverance](Images\kdc_header.png "Shot by Otis_Inf"){.shadowed}
## Summary
Feature | Supported
--|--
Vanilla Photo Mode | No
Hotsampling | No
DSR | Yes
Custom Aspect Ratios | No  
Reshade | Yes (DX11)
Ansel | Yes
DirectX versions | DirectX 11
 
## Tools

* [Camera tools by Otis_Inf](https://patreon.com/Otis_Inf)  
**Features**: Camera control (FoV Control, free unlimited camera movement), Ansel also in conversations, No-clip check anymore for ansel/freecamera,
makes all cvars writable.

## Tweaks
The game has its console enabled, so you can tweak the game through console commands. If you use the ansel enhancement tools linked above, you
can change any cvar in the game's engine. The engine is a modified CryEngine so you can use the custom cfg files and keybinds to enhance the graphics
and other game aspects. See below how to do that.

### Custom config files
In the game's folder, first of all create a file called `user.cfg`. There's already a system.cfg file, leave that alone. Your
own `user.cfg` file should have the following enhancements:

```
sys_MaxFPS=60
r_TexturesStreamingMipBias -4
r_FogShadows 1
r_ssdo=1
r_ssdoAmountAmbient=1.4
r_ssdoAmountDirect=2
r_ssdoAmountReflection=4
r_ssdoHalfRes=2
r_ssdoRadius=0.04
r_ssdoRadiusMin=0.07
r_ssdoRadiusMax=0.1
e_svoTI_ResScaleBase=0
e_svoTI_LowSpecMode=1
e_svoTI_ConeMaxLength=8
e_svoTI_DiffuseConeWidth=24
e_svoTI_SSAOAmount=1.545
e_svoTI_SpecularAmplifier=0.82
e_svoTI_TemporalFilteringBase=1
e_svoTI_MinReflectance=0.19
e_svoTI_DiffuseAmplifier=1.12
e_VolumetricFog=1
e_TessellationMaxDistance=100
e_ViewDistMin=15
e_ViewDistRatio=200
e_ViewDistRatioCustom=250
e_ViewDistRatioDetail=200
e_ViewDistRatioLights=250
e_ViewDistRatioPortals=250
e_ViewDistRatioVegetation=250
q_shaderWater=3
r_DetailDistance=20
r_TextureLodDistanceRatio=0
e_shadowsmaxtexres=2048
e_shadowspoolsize=8192
e_LodFaceAreaTargetSize=0.0008
e_UberlodDistanceRatio=4.0
e_MergedMeshesViewDistRatio=150
e_vegetationUseTerrainColorDistance=150
e_TerrainDetailMaterialsViewDistZ=300
e_ShadowsPerObject=1
wh_pl_showfirecursor=1
r_Rain 0  -- if you don't want the rain drops to be visible keep this command, otherwise remove it.
```

The following lines are **examples** how to bind a command to a key. You can add these to your custom `user.cfg` file as well:
```
-- when f2 is pressed it will run the commands in 'n.cfg'
bind f2 exec n.cfg
Bind f3 exec 4k.cfg
-- when 8 is pressed it will hide the hud
Bind 8 g_showHUD 0
-- when 9 is pressed it will show the hud
Bind 9 g_showHud 1
```

The files `n.cfg` and `4k.cfg` above, are custom text files you create, the same as `user.cfg`. The files have the following contents:

n.cfg:
```
r_width=1920
r_height=1200
```

4k.cfg:
```
r_width=3840
r_height=2400
```

If you're playing at 1920x1200, you can then switch between your normal play resolution and 4K by pressing f3 (to switch to 4K) and f2 (to switch
back to your normal resolution). 

### Console commands
The game's console (and all cvars, if you run the tools) are freely available and you can use it at any time. To search for variables and 
commands, use `?<string>`, like `?dof`. This will list all cvars and commands containing the string following `?`, here in the example `dof`. 
Typing the cvar without a value will give its current value. If you want to have a cvar always set to a given value, add it to your user.cfg file. 

## Essential mods
There are various mods available over at [NexusMods](https://www.nexusmods.com/kingdomcomedeliverance). Not all of them are really great nor necessary,
however a couple of them really make life a lot easier. One note for mods: check in the installation instructions if they try to overwrite/change 
your user.cfg file. If anything make a copy of your user.cfg file before installing mods. 

The mods which are essential:

- [No Helmet Vision](https://www.nexusmods.com/kingdomcomedeliverance/mods/28)
- [Unlimited Saving](https://www.nexusmods.com/kingdomcomedeliverance/mods/1)
- [No Vignettes](https://www.nexusmods.com/kingdomcomedeliverance/mods/78)
- [No Stamina effect](https://www.nexusmods.com/kingdomcomedeliverance/mods/10)
- [No Blood on Screen](https://www.nexusmods.com/kingdomcomedeliverance/mods/58)
- [No Gross Eating Sounds](https://www.nexusmods.com/kingdomcomedeliverance/mods/807). This one is perhaps up for debate, but really, the sounds
this game uses when you eat something are so disgusting that you really want these to be muted/removed.
- [Volumetric Fog Shadows](https://www.nexusmods.com/kingdomcomedeliverance/mods/800)
- [Inventoried](https://www.nexusmods.com/kingdomcomedeliverance/mods/797)
- [Bushes - collision remover](https://www.nexusmods.com/kingdomcomedeliverance/mods/591)

## Useful Links

* [PC Gaming Wiki](https://pcgamingwiki.com/wiki/Kingdom_Come:_Deliverance)