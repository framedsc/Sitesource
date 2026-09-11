![Reverting Steam Updates](Images\steamupdates_header.png){.shadowed .autosize}

## 1. Install or open Steam Console
Install steamcmd.exe from [here](https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip) and login to your Steam account with 
`login {username} {password}` 
if you're using Steam Guard, you'll be prompted to enter that as well.

Alternatively, you can access Steam console from client or internet browser by typing 
`steam://nav/console`
or adding `-console` to Steam target address shortcut. 

Another alternative is to use [this](https://github.com/mmvanheusden/SteamDepotDownloaderGUI) tool with some friendly UI. You can find a written and a video tutorial in the programs repository.

## 2. Get AppID. 
Go to [Steamdb.info](http://www.steamdb.info) and type the name of the game into search bar on top left.
After searching the name of the game, look at the search result and find your game. Record its appID.

## 3. Get DepotID.
After that, you need to find the content you want to download by take a look at 'Depot' list. The easiest way to find the depot you need is by comparing files on SteamDB with your local files, if [they're identical](https://i.imgur.com/unz9j4i.jpg), or at least similar, that's most likely the depot you want to download. Record its DepotID.

## 4. Get ManifestID
Every specific version of the content you want to download are listed on 'Manifests' tab. They're marked by timestamp and ManifestID. Pick the one you want and record its ManifestID.

## 5. Download the package
Once you have AppID, DepotID and ManifestID type this into Steam console:

`download_depot <appid> <depotid> <manifestid>`

## 6. Retrieve the package & overwrite your files
If you're installing SteamCMD somewhere in your PC, the downloaded package will be on the same folder as your steamcmd.exe. If you're opening Steam Console via client or browser, the downloaded package will be on this folder
`...\Steam\steamapps\content\<depotid number>`

After that, it's just a matter of replacing new, updated game files with the older one you just downloaded.

## Additional Notes
You can do the same for Steam Workshop or any User Generated Content files provided you know the ID number, simply type this into Steam Console command `workshop_download_item <AppID> <WorkshopID>`

## Useful Links
* [Steam Developer documentation on SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD)