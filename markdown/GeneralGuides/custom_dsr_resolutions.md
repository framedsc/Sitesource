How to get 10 custom resolutions in any aspect ratio you want
=============

You can now create any resolution you want by directly editing the Nvidia DSR registry settings, and you are not restricted to your native aspect ratio. Here is a guide on how to set that up.

Quick summary:

1. Export your Nvidia DSR registry settings (you should only ever need to do this once).
2. Use this tool to generate the registry data for up to 10 custom resolutions.
3. Swap that into your exported registry file and save. Double click that file to import your registry settings.
4. Use DevManView to toggle your display adapters so the new settings kick in. This saves you from having to do a restart and only takes about 10 seconds.
5. Enjoy your 10 custom resolutions in any aspect ratio you want.
 
##1. Export your registry settings

Open Regedit (open your start menu or press WIN+R and type "regedit"). Navigate here (Copy this line and paste it in the top line in RegEdit)

```
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\nvlddmkm\State\DisplayDatabase
```

And from there to your display name

You might have a bunch of different folders in there for your displays. For example, [this is what mine looks like](https://i.imgur.com/ZHav1Kf.png). The bottom 2 ended up being my monitors (I have 2). You'll know the folders correspond to a monitor when you see a populated "SmoothScalingData" parameter.

Right click that folder and click "export." Save the file somewhere you'll remember it. This file is handy as you simply need to double click it after a new driver install to restore your custom resolutions.

## 2. Run the DSR Calculator

The DSR Calculator is a tool I made that will allow you to type in 10 custom resolutions and will generate the required hex information for them. You simply need to copy that to your clipboard and be prepared to replace that section of the registry file you exported.

[Click here to download the DSR Calculator](https://web.archive.org/web/20180301201005/http://www.jim2point0.com/tools/dsr_hex/) (extract to a folder and open the index.html in your browser)

When you finish, you'll get some data that looks like this:

```
"SmoothScalingData"=hex:01,00,00,00,22,00,00,00,10,00,00,00,C7,38,00,00,41,36,00,00,00,00,00,00,22,44,00,00,61,51,00,00,00,00,00,00,7D,4F,00,00,82,6C,00,00,00,00,00,00,D8,5A,00,00,A2,87,00,00,00,00,00,00,11,22,00,00,41,36,00,00,00,00,00,00,C7,38,00,00,20,1B,00,00,00,00,00,00,7D,4F,00,00,61,51,00,00,00,00,00,00,D8,5A,00,00,82,6C,00,00,00,00,00,00,33,66,00,00,41,36,00,00,00,00,00,00,7C,23,00,00,61,51,00,00,00,00,00,00
```

## 3. Edit your exported registry file

Remember that file you exported? Open it in a text editor. We're interested in replacing the lines highlighted like in this picture (lines 5-10):

![Registry File Editing](https://i.imgur.com/r3KJVKY.png)

Highlight those lines and paste in the data you copied from the DSR tool. Save the file and then run it (double click). Say yes when it warns you about the potential damage you could be doing to your computer. 

If you get an error saying that you can not import the settings, you need to set permissions on that folder in the registry. Find your monitor in the registry settings like you did when you exported it. Right click -> permissions.

![Registry Permissions](https://i.imgur.com/tx8PgZp.png)

Click your relevant user\group and check "full control" under "allow." Or you can just set full control for everything.

Now you should just be able to double click registry files to import those settings again. 

## 4. Use DevManView OR Restart your computer

You can get this tool here and then create a BAT file that will toggle specific devices. For our purposes, this saves from having to do a complete restart every time you import new registry settings, which means you can instantly change out your DSR resolutions if you make a few copies of your original registry file (why have 10 resolutions when you can have 30?)

[Get the tool from here](http://www.nirsoft.net/utils/device_manager_view.html). The download link is all the way down a the bottom.

Extract that somewhere. I personally maintain a "utilities" folder for stuff like this.
Inside that same folder, create a new text file with the following line:

`devmanview /disable_enable "XXX"`

and save it as "toggle_gpu.bat" or... whatever you want to call it. Then, figure out the name of your display adapter and replace the "XXX" with that. You can find it listed in DevManView or your Device Manager. I have a Geforce 1080TI, so this is my toggle command:

`devmanview /disable_enable "NVIDIA GeForce GTX 1080 Ti"`

Double click that bat file and your monitor(s) will shut off for about 10 seconds (your Nvidia control panel does this when you enable DSR for the first time).

When your monitor(s) come back on, check your display settings and you should see your new custom resolutions ready to go. [Success?](http://i.imgur.com/QokCunW.png)

## 5. A little House Cleaning

Some games, not all, will require you to adjust your desktop size and position settings in the Nvidia control panel. You want want to make sure you perform scaling on the GPU and override the scaling mode set by games and programs.

![Control Panel Settings](https://i.imgur.com/aZKYJnL.png)

**Now go enjoy your resolutions!**

In the future, if you want to use 10 completely new custom resolutions, you simply type them into the tool and you'll be able to use them in 30 seconds.

If you have any questions or something isn't working, let me know. 

/End

