# Requirements #

Periscope follows the package version from Ubuntu. In order to have similar settings, these are the requirements (as of February 2011)

**Microsoft Windows :)** Python 2.6 or 2.7 http://python.org/download/releases/
**SetupTools** BeautifulSoup 3.1 (the .tar.gz) http://www.crummy.com/software/BeautifulSoup/download/3.1.x/
**Periscope (the latest .tar.gz or from SVN) http://code.google.com/p/periscope/downloads/list** A file extracter to open .tar.gz files. 7Zip is a good choice http://www.7-zip.org/download.html


# Installation #

**Download the Python .exe file and install it by executing it.** Download BeautifulSoup .tar.gz and periscope .tar.gz and save it in a selected folder.


README from Ano:
1°) Install Python (set PATH env variable to Python install dir i.e. C:\Python26)
2°) setuptools-0.6c11 : python setup.py install
3°) BeautifulSoup-3.0.8.1 : python setup.py install
4°) periscope : python setup.py install
5°) Edit python path in menu.reg and execute the file

Regedit from Ano:

REGEDIT4

[HKEY\_CLASSES\_ROOT\**\shell]
[HKEY\_CLASSES\_ROOT\**\shell\Periscope]
[HKEY\_CLASSES\_ROOT\