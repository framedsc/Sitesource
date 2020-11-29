Using RTTI info in a game exe
==============================

(Information distilled from an excellent video by Hatti.)

The first action is to search for `.?AV` as string in the game exe using cheat engine. Do a search on the .exe alone, by selecting
the exe in the combobox in Memory Scan options. Set Scan type to string, Writable and CopyOnWrite set to a filled checkbox. If you find more than
a 1000 entries, it's usable and types of the game are in RTTI info in the exe. If you find just a few hundred, forget it. 

After you've found all entries, select them all in the top pane of CE and click the red arrow to add them all to the table area. Select them all, press 
`alt-enter` and increase the width of the screen type to e.g. 50 or more. 

Then select `Table->Show Cheat Table Lua Script`, and run the following Lua:

```lua
local al = getAddressList()
local vals = {}
for i=0, al.Count-1 do
    vals[#vals+1] = al[i].Value
end
writeToClipboard(table.concat(vals, '\n'))
```

This will copy all string values to the clipboard. Open notepad++ and press `ctrl-v` to paste the contents. You now have all the type names
available through RTTI, and can start finding the types one by one using the steps described below.

## Using the type names
After you've ran the script and pasted the info into notepad, you can search for a given type, e.g. everything with 'Camera' in it. We'll use the 
example of Rise of the Tomb Raider. After using the steps above, we find a lot of names and one of them is `.?AVCameraComponent@@`. Searching again
on the .exe with the same settings we find just 1 entry. Clear the table area and add the one entry we found. The entry we found is at address 
`0x140f3D218`.

Bring up the windows calculator, set it to 'programmer' as you can then work with hexadecimal values. The type descriptor for the CameraComponent here
starts at the address 0x10 earlier, so `0x140f3D218 - 0x10` which is `0x140f3D208`.

### Object locator
To find the object locator we have to take the address we calculated, `0x140f3D208`, and substract the module start address, which is the start address
of the exe in memory. Here that's `0x140000000`, so we can just keep `0xf3d208`.
Scan for that, in the exe, 4 Bytes hex scan, and from the entries you find, pick the one ending with `0xC`. Now, that address, subtract `0xC` from that
which is just changing the end C with 0. Here however the address isn't ending with a C, but with a 4: `0x140DF8D14`. 

### Finding the VTable and instances
We substract C from that, which will give us `0x140DF8D08`. We do a new scan, this time for 8 bytes hex, and scan for that value, `0x140DF8D08`. This 
gives us 1 address, which is the VTable of the type we searched for, which in this case is located at `0x140CDF4D8`. With the VTable we can find all
instances of the type we searched for, as the instances point to the vtable in memory. To do that, add `0x8` to the address of the start of the VTable
which results here in `0x140CDF4E0` and we scan for this, 8 byte hex, in the complete memory, so not only inside the game exe. We'll end up with a couple
of instances and we can now browse the memory of these and look inside them to see if they contain any values we can use. 