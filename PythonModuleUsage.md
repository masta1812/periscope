# Introduction #

Periscope is a subtitle download module written in Python. It allows you to easily search for subtitles for a given file on your harddrive on multiple subtitle websites.

# Requirements #
Periscope is a 100% python module, the only requirements is BeautifulSoup with the current version from Ubuntu (3.1.0.1 as of August 2010).
If you've installed periscope through the PPA repository for Ubuntu, you should have BeautifulSoup installed.

# Download a subtitle for a file #

```
import periscope
subdl = periscope.Periscope()
filepath = '/home/user/myVideo.avi'
subtitle = subdl.downloadSubtitle(filepath, ['en']) # for english only
subtitle = subdl.downloadSubtitle(filepath, None) # for any language
subtitle = subdl.downloadSubtitle(filepath, ['de', 'en']) # subtitles in German, if none are found, search in English

if subtitle :
    print "Found a sub from %s in language %s, downloaded to %s" % ( subtitle['plugin'], subtitle['lang'], subtitle['subtitlepath']
```


# List subtitles in French or Spanish #
```
import periscope
subdl = periscope.Periscope()
filepath = '/home/user/myVideo.avi'
subs = subdl.listSubtitles(filepath, ['fr', 'es']) # subtitles in French, if none are found, search in Spanish

for sub in subs :
    print "Found a sub from %s in language %s, downloaded to %s" % ( subtitle['plugin'], subtitle['lang'], subtitle['subtitlepath']

# if you wish to download the second sub:
subdl.attemptDownloadSubtitle([sub[1]], None) # the method is named "attempt" because it may fail for some reason (no unrar capability for instance)

# if you've identified multiple good candidates (here the first three) and wish to attempt to donwload the first, if it fails, the second, if it fails the third :
subdl.attemptDownloadSubtitle([sub[0:2]], None)

```