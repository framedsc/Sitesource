A game screenshot can look right in your editor and startlingly different in a shared copy. Before adjusting saturation, check what color space the pixels were recorded in. This workflow starts with an SDR image whose source profile is known. An HDR capture needs a tone-mapping decision before an SDR export.

## Identify the source before changing it

Keep the original file and open a copy in GIMP. If GIMP offers to convert the embedded profile on opening, choose Keep so you can inspect it first. Open Image → Image Properties and look at Color Profile. If the source is already ordinary sRGB, skip straight to export. If you know the source is wider, such as Adobe RGB (1998), keep that profile attached for the next step.

For an untagged file, look up the color space used by the capture or export tool. If you can identify it, use Image → Color Management → Assign Color Profile to supply the missing source profile. Guessing from the grass or the sky is unreliable. GIMP can show a default sRGB profile for untagged pixels, so the profile displayed in the editor alone cannot establish how the capture was made.

## Convert the working copy

Open Image → Color Management → Convert to Color Profile. Check that Current Color Profile names the source you identified. For a conventional 8-bit SDR PNG, choose the built-in sRGB profile for nonlinear RGB in the destination list. For the example below, the settings were Relative colorimetric with black point compensation enabled. Confirm the conversion.

A three-patch test card shows what the command changes. In GIMP 3.0.4, a green patch in an 8-bit PNG tagged with an Adobe RGB (1998)-compatible profile started at RGB (108, 160, 122). Assigning sRGB on one copy left those three numbers untouched. Converting a second copy to sRGB produced (74, 161, 121). Both exports carried an sRGB profile. That is why checking the label on the final file cannot tell you whether the pixels were converted correctly.

## Check the file you will share

Use File → Export As and give the copy a new .png name. Enable the option to save the color profile in the PNG export settings. Reopen the exported file in the same color-managed editor and compare it with the original at the same zoom. Check recognizable details such as a muted wall and a brightly colored sign. Colors outside sRGB may lose saturation in the conversion. If the whole scene shifts unexpectedly, revisit the source profile before changing the image by eye.

The GIMP manual documents [profile assignment](https://docs.gimp.org/3.0/en/gimp-image-color-profile-assign.html), [profile conversion](https://docs.gimp.org/3.0/en/gimp-image-color-profile-convert.html) and [PNG export](https://docs.gimp.org/3.0/en/file-png-export.html).

Prepared by the ARTCORE editorial team with AI assistance.
