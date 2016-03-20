# Introduction #

This wiki pages shows you the steps to add periscope support into Nautilus by simply doing a right-click "Download subtitles" on a video file.

**This wiki reflects details for the latest version of the package**

# Ubuntu user #

If you use Ubuntu, you may prefer to install the **periscope-gnome** package from the [repository](http://code.google.com/p/periscope/wiki/UbuntuRepository)

# Details #

  * Install python support in nautilus by installing python-nautilus and python-notify that shows notification on the bottom-right of your screen:
> For Ubuntu:
```
sudo aptitude install python-nautilus python-notify
```

  * Install periscope from the project home page: http://code.google.com/p/periscope/
    * Ubuntu/Debian users : Download the lastest debs (python-periscope and periscope-gnome) and double-click on it. That's it.

  * Copy the periscope-nautilus.py script into the ~/.nautilus/python-extensions
```
cd ~/.nautilus/python-extensions
wget http://periscope.googlecode.com/svn/trunk/bin/periscope-nautilus/periscope-nautilus.py
```

  * If you want to change the default languages, run periscope once, a file named "config" will be created under ~/.config/periscope. Update this file to reflect your prefered languages. They can be separated by comas, so:
```
lang = en 
or
lang = en,fr
```
are valid. The first one saying that you want to search subtitles in english, the second, in english and if not found, in french.

  * Restart nautilus otherwise it does not take into account the newly added scripts by typing in a terminal `nautilus -q`

  * Open nautilus and go to a location where you have video files. Right-click on a video and wait for the notification to see if a match was found.