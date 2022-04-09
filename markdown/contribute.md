<div class="figure">
<img src="Images/contribute_header.png" alt="Contribute to the site!" title="Help us out!" class="autosize" />
<p><i>Industria</i>, <a href="https://framedsc.com/HallOfFramed/?imageId=1633772229" target="_blank">shot</a> by nyxikri</p>
</div>

<center> <b><font size=+3 face="Galano Grotesque Alt">We're looking for authors!</font></b> <br>
<i>Don't know what to write? Check our</i> <a href="https://github.com/framedsc/Sitesource/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+author%22" target="_blank"><b>issue tracker</b></a> <i>for anything you could help out with.</i> </center>

[framedsc.com](https://framedsc.com/) is an open-collaboration project, written and maintained by a community of volunteers. We welcome anyone willing to contribute their own knowledge and expertise on anything relevant, be it to [our game guides](./Gameguides.htm), a [cool technique you know of](./GeneralGuides/tinyplanetsguide.htm), or anything you think could be useful to someone!

---

## Writing guides

If you're interested in writing a guide for the site, please [download this template](https://mega.nz/file/vBlhxTrL#f91WEfYmJMOXS5nDOyQtd7MKEWQ6fWorOMTVoTOcNl4). It contains everything you need to get started - a Markdown template for a game guide and a .PSD + font file to generate a header.

We recommend writing with [Visual Studio Code](https://vscode.dev/) as it has a Markdown preview similar to how the site looks. The site is built with DocNet, however, which includes Markdown extensions not found in the VS Code preview. Learn more about DocNet's additional features [**here**](http://fransbouma.github.io/DocNet/WritingcontentusingMarkdown.htm).

The site also supports HTML in Markdown if you want the formatting of your guides to be a little fancier. The centred text above was written in the .MD like so:

```HTML
<center> <b><font size=+3 face="Galano Grotesque Alt">We're looking for authors!</font></b> <br>
<i>Don't know what to write? Check our</i> <a href="LINK" target="_blank"><b>issue tracker</b></a> <i>for anything you could help out with.</i> </center>
```

### Making headers

When making a header for your guide, you may use any shot from the game, including your own. We recommend picking one that allows for good readability of text.

Here are two examples of great headers. The text lies wholly in the dark left side of the shot, contrasting and reading well.  
![good header eg1](Images\alienisolation_header.png){.shadowed .autosize}
![good header eg2](Images\nioh2_header.png){.shadowed .autosize}

After you've picked your shot, place it above the Base layer and ensure it's clipped to it. If it isn't, alt-click on the divider between the two layers. You should see a small down-arrow appear. Arrange the shot as you see fit.

Once the shot has been arranged, duplicate it by alt-clicking and dragging the layer below the Base layer. You can also `Ctrl + J` to duplicate and move it below. Go up to `Filter > Blur > Gaussian Blur...` and add a 26.3 radius blur to this duplicated layer to create the blurred border.

Your Photoshop layers should look like so:  
![photoshop layers](Images\contribute_pslayers.png){.shadowed .autosize}

Export it as a .PNG and rename appropriately.

The header template includes a network of guides that can be enabled and disabled with `Ctrl + ;`. These can be used to help you compose a header or as safety margins. In the rare case that a game title is so long it doesn't fit in the header, decrease the font size until it fits in the rightmost margin.

![long game title](Images\contribute_nnk2header.png "Font size had to be reduced to 31"){.shadowed}

### Images

If your guide has images, use this line to embed them:
```Markdown
![title](Images\image.png "subtitle"){.shadowed .autosize}
```
Images will be sorted into the Images folder by the site admins. You may place them in a subfolder if you'd like to organise them.  
You can also use HTML to embed them instead, if you want a bit more formatting.

```HTML
<div class="figure">
<img src="Images/image.png" alt="title" title="Tooltip that appears when you hover" class="autosize" />
<p>subtitle</p>
</div>
```

#### Accepted images

Images on the site should be in a .PNG / high-quality .JPG format, under 1MB. While there are no current size limits, images on the site are resized to 896px width (with the .autosize tag, which should be added to all images). They don't have to be resized to that width, but we would prefer it if you kept image sizes reasonable.

For excessively large images (say you want to include a full-res screenshot for some reason), they may be hosted externally. Use a trusted, reliable imagehost like [Imgur](https://imgur.com/upload).

### Hosting files

We don't host any tools or utilities in the repository itself. If you would like to contribute any tool or utility, we recommend using a filehost like [mega.nz](https://mega.nz). If the tool is hosted publicly on say a modding site or forum, please link to the post instead.

An exception to this is cheat tables. We prefer to archive those internally, provided that you are the author or have been given permission by the author to have them archived on the site. Include them alongside your submitted files.

### Controller buttons

The site supports display of controller buttons through a font. You can use these to embellish a controls table like so:

Gamepad | Command
--|--
<font face="Controller">{ / }</font> | Move camera up / down
<font face="Controller">[ / ]</font> | Tilt camera left / right
<font face="Controller">W / X</font> | Zoom in / out

The syntax for this is a little messy as it involves wrapping the specific glyphs in HTML:
```Markdown
<font face="Controller">{ / }</font> | Move camera up / down
<font face="Controller">[ / ]</font> | Tilt camera left / right
<font face="Controller">W / X</font> | Zoom in / out
```

This feature is unique to the site and not supported by Markdown previews. You may generate previews of the site following our [readme](https://github.com/framedsc/Sitesource) if you'd like to see how they look.

Input | Output
-- | --
`7 8 9` <br> `4 5 6` <br> `1 2 3` | <font face="Controller">7 8 9 <br> 4 5 6 <br> 1 2 3</font>
`< >` | <font face="Controller">< ></font>
`Q W E` <br> `A S D` <br> `Z X C` | <font face="Controller">Q W E <br> A S D <br> Z X C</font>
`x y` <br> `a b` | <font face="Controller">x y <br> a b </font>
`[ ]` <br> `{ }` | <font face="Controller">[ ] <br> { }</font>
`v g m` | <font face="Controller">v g m</font>

*Inputs are **case-sensitive**!*  
*Controller Font by [Dean Tersigni](http://www.thealmightyguru.com/Wiki/index.php?title=Controller_Font)*

### Updating guides

If you notice an error in a guide or you simply want to extend an existing guide, you may access the site source [**here**](https://github.com/framedsc/Sitesource). From there, open the markdown folder and navigate to the .md file of the guide you wish to edit. 

### Etiquette

We're generally not too concerned with how you write and format a guide, so long as the information is coherent and presentable. A site admin will help to clean up any incorrect syntax before publishing.

When it comes to updating game guides, headers will not be updated.

Unless all download pages are dead and the author is uncontactable, we will not rehost files without the author's permission.

#### Crediting yourself

You may credit yourself at the end of your non-game guides if you feel like it. Game guides don't have credits, but more often than not the headers used are from the guide authors themselves.

---

## Publishing guides

Once you're done writing a guide, you may contact one of the site admins (listed on the [homepage](./index.htm)) to get it added. Please zip up your guide and all relevant assets into one compressed folder. Alternatively, you may submit a [pull request](https://github.com/framedsc/Sitesource/pulls) to the GitHub repository. 

Once sent over, a site admin will look through your submission to ensure everything'll look good on the site before we put it up.

Thanks for contributing to FRAMED!