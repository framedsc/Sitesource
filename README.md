# Sitesource

The source files used to generate the official site. (c) 2019 All rights reserved. 

## How to generate the main site?

The site is based on Markdown and is generated with a tool called [DocNet](https://github.com/FransBouma/DocNet). DocNet is a static site
generator mainly meant for generating documentation and guide sites, and that's exactly what we're dealing with.

### Download DocNet
To get started, first download a recent [DocNet release](https://github.com/FransBouma/DocNet/releases), preferably v0.16.4 or higher. Simply
download the .zip file, unpack it and copy the files in the zip to a folder. It's convenient to add the folder you have copied the files to to 
your windows path, as DocNet is a command line tool.

### Clone this repository
After you've downloaded DocNet and made it available on the commandline, you can clone this repository to a folder using Github For Windows. However it's best to do that in your own fork. This requires you to create an account on Github, and when logged in, you can 
fork this repository to your own account (effectively creating a copy for yourself on Github) and clone *that* repository to your own
PC. Changes made to that repository then have to be merged through a pull request. Github has a [guide](https://guides.github.com/activities/forking/) for this which explains the whole process for you. You'll be up and running in no time!

The repository contains both a `Markdown` folder for source content and a `Site` folder which contains the generated site for testing. 

### Adding content
All site content goes into the `Markdown` folder. In the `Markdown` folder there are several sub folders, to group files together. Images
used in the markdown pages should be placed in the `Images` folder. The `Theme` folder is for the theme used in the pages. Changing something
there will affect all pages after generating the site. 

To add a page, place it in the folder inside `Markdown` and use a file with the `.md` suffix. If you don't know where to start, try copy/pasting
an existing file and change that till it's what you want. Just adding a file isn't enough however, you have to tell the generator where to 
place it in the table of contents. 

To make it show up in the site, you have to change the file `docnet.json` inside the `Markdown` folder. This file configures DocNet and defines the
site structure. Preferably, place game guides in alphabetical order so they're easy to find. Json can be a tricky format, if you get errors, you likely
forgot a quote or a comma somewhere. 

### Authoring content
To author content, you can use any text editor like notepad, but it's easier to use an editor which also has wysiwyg view. 
[Visual Studio Code](https://code.visualstudio.com), a free editor from Microsoft, offers that. When using Visual Studio Code, open a .md file using its
built-in file browser. This will give you a textual editor. If you right-click the tab of the file and select 'Split right' you get a second 
view on the text editor. Right-click the tab header of the newly created 2nd view and select 'Open preview'. This will show the markdown in wysiwyg overview
so you can write markdown and immediately see the result how it will look.

#### Markdown references
The following references can be used to learn more about Markdown:

* [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [DocNet's Markdown support](http://fransbouma.github.io/DocNet/WritingcontentusingMarkdown.htm)

### Generating the site
DocNet is very fast, it can generate the whole site in a second or so. To generate the site, open a command prompt or powershell prompt and navigate to the
folder which contains this repository. Then type on the commandline:

```
docnet -c markdown
```

This will generate the complete site in the `Site` folder, and first clean the folder so files which are no longer used are removed. You can now preview
the site by opening the index.htm file in the `Site` folder. If you want to make changes, simply edit the markdown file that needs changing, again run the 
docnet command as stated above, and refresh the page in the browser. 

When everything is OK, commit your changes to this repository and let us know so we can update the main repository. Or create a 
pull request on your own repository so we get notified automatically. If you go this route, you'll be editing on your own copy, and
it has to be kept up to date with the main repository so you get changes merged in when others make changes on this repository too. 
To get these changes, [follow this guide](https://help.github.com/en/articles/syncing-a-fork).

### Useful markdown info
Please check [the DocNet documentation site](http://fransbouma.github.io/DocNet/WritingcontentusingMarkdown.htm) to learn more about the markdown it supports.