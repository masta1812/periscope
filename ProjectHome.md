[![](https://www.paypalobjects.com/WEBSCR-640-20110429-1/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=FJCSLVSUG75DJ&lc=BE&item_name=Periscope%20Development&item_number=periscope%2ddev&currency_code=EUR&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted)
<font size='3'><b>Help the development of periscope by making a donation using paypal.</b></font>

![http://a3.twimg.com/profile_images/79727517/ubuntu_logo_normal_bigger.gif](http://a3.twimg.com/profile_images/79727517/ubuntu_logo_normal_bigger.gif)
<font size='3'><b>Ubuntu users, please <a href='http://code.google.com/p/periscope/wiki/UbuntuRepository'>use the repository</a> so that updates will be pushed to you.</b></font>

# Presentation #
periscope is a subtitles searching module written in python that tries to find a **correct match** for a given video file. The goal behind periscope is that it will only return only correct subtitles so that you can simply relax and enjoy your video without having to double-check that the subtitles match your video before watching it.

This is done by using as much info as available from your file and on the websites. Some websites allow you to use hash of the files, the size/length of the video or the exact file name.

As a python module, periscope should be easily integrated in many projects that allow plugins to be written in python. The fact that the plugin is shared between all the applications means that separate application and their plugin (file browser, video player, media center application, ...) don't have to maintain the code to search, parse and download subtitles and the user preference about languages.

The subtitles websites are handled as plugins and currently support :
  * [OpenSubtitles.org](http://www.opensubtitles.org/en)
  * [SubtitleSource.org](http://www.subtitlesource.org/)
  * [Subscene.com](http://subscene.com)
  * [Subtitulos.es](http://www.subtitulos.es)
  * [Addic7ed.com](http://www.addic7ed.com)
  * [TheSubDB.com](http://thesubdb.com)
  * [BierDopje.com](http://bierdopje.com)

![http://static.opensubtitles.org/gfx/logo.gif](http://static.opensubtitles.org/gfx/logo.gif)
![http://periscope.googlecode.com/files/subtitlesource.org.jpg](http://periscope.googlecode.com/files/subtitlesource.org.jpg)
![http://subscene.com/themes/base/images/logo.gif](http://subscene.com/themes/base/images/logo.gif)
![http://www.subtitulos.es/images/subslogo.png](http://www.subtitulos.es/images/subslogo.png)
![http://periscope.googlecode.com/files/addic7ed.png](http://periscope.googlecode.com/files/addic7ed.png)
![http://thesubdb.com/subdb-logo.png](http://thesubdb.com/subdb-logo.png)

---

# Installation #
## Ubuntu ##
For Ubuntu users, you can add the repository for periscope in Synaptic.
All information are located on the Wiki:
http://code.google.com/p/periscope/wiki/UbuntuRepository

## Debian ##
I believe the Ubuntu package should be installable on Debian unstable.

## From source code ##
You can [checkout the code](http://code.google.com/p/periscope/source/checkout). The setup.py is included in SVN.

# Usage #
You can use the module with a CLI by doing

```
$ periscope </path/to/my/video> -l en
$ periscope </path/to/my/vidoe> -l en -l fr
```
to search subtitles in english, replace 'en' by 'fr', 'de' or whatever language you would like your subtitles in.
Note : Brazilian Portuguese is written as "pt-br", Argentinian Spanish is written as "es-ar".

You can also use periscope in [Nautilus by following the instructions on the wiki page](http://code.google.com/p/periscope/wiki/NautilusSupport)

# Requirements #
As of version 0.1.7
  * You will need Python (>= 2.6, < 3.0) to run periscope.
  * You will also need the python module [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/) to parse html pages.
  * An executable unrar command could be needed for some plugins

# Screenshot(s) #

## Nautilus Integration ##
A [Nautilus plugin](http://code.google.com/p/periscope/wiki/NautilusSupport) exists to integrate periscope in Nautilus:

![http://www.technobullshit.com/blog/wp-content/uploads/2007/12/subtitles.png](http://www.technobullshit.com/blog/wp-content/uploads/2007/12/subtitles.png)



## Changes ##

### 0.1.9 ###
```
Better error handling
Removing Podnapisi.net (temporary)
Added Addic7ed.com
Experimental support for TVSubtitles.net (not activated by default)
```

### 0.1.8.1 ###
```
 * Fixes the language from the config file
 * Fixes Podnapisi support
 * Various bugfixes
```

### 0.1.7 ###
```
 * support for subscene.com and subtitulos.es
 * CLI shows a report at the end
```