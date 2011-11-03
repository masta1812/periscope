# -*- coding: utf-8 -*-

#   This file is part of periscope.
#   Copyright (c) 2008-2011 Patrick Dessalle <patrick@dessalle.be>
#
#    periscope is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public
#    License as published by the Free Software Foundation; either
#    version 2 of the License, or (at your option) any later version.
#
#    periscope is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with periscope; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import urllib2
import nautilus
import os
import threading
import gettext
import gio
import logging
import xdg.BaseDirectory as bd # required

gettext.textdomain('periscope-nautilus')

try:
    import pynotify
except ImportError:
    pass

import periscope

# i18n stuff
gettext.install('periscope-nautilus')

class DownloadSubtitles(nautilus.MenuProvider):
    ''' This class is to be used in Nautilus with the python-nautilus extension. 
    It provides a context menu on video file to download subtitles.'''
    def __init__(self):
        if pynotify:
            pynotify.init("periscope subtitles downloader")
        self.cache_folder = os.path.join(bd.xdg_config_home, "periscope")
    
    def menu_activate_cb(self, menu, files):
        #List the valid files
        videos = [f for f in files if not f.is_gone() and self.is_valid(f)]
        # Get the file paths from gvfs so we support non local file systems, yay!
        g = gio.vfs_get_default()
        videos = map(lambda f: g.get_file_for_uri(f.get_uri()).get_path(), videos)
        
        # Call the thread        
        invoker = PeriscopeInvoker(videos, self.notify, self.cache_folder)
        invoker.start()
                
        
    def get_file_items(self, window, files):
        # Keep only the files we want (right type and file)
        files = [ f for f in files if self.is_valid(f)]
        if len(files) == 0:
            return

        item = nautilus.MenuItem('Nautilus::download_subtitles',
                                 _('Find subtitles for this video'),
                                 _('Download subtitles for this video'),
                                 gtk.STOCK_FIND_AND_REPLACE)
        item.connect('activate', self.menu_activate_cb, files)
        return item,
        
    def is_valid(self, f):
        return f.get_mime_type() in periscope.SUPPORTED_FORMATS and (f.get_uri_scheme() == 'file' or f.get_uri_scheme() == 'smb')
        
    def notify(self, found, notfound):
        ''' Use pynotify to warn the user that subtitles have been downloaded'''
        if pynotify:
            title = "periscope found %s out of %s subtitles" %(len(found), len(found) + len(notfound))
            if len(notfound) > 0:
                msg = _("Could not find: \n")
                filenames = [os.path.basename(f["filename"]) for f in notfound]
                msg += "\n".join(filenames)
                msg += "\n"
                
            if len(found) > 0:
                msg = _("Found: \n")
                filenames = [os.path.basename(f["filename"]) + " ("+f['lang']+")" for f in found]
                msg += "\n".join(filenames)
                
            n = pynotify.Notification(title, msg, gtk.STOCK_FIND_AND_REPLACE)
            n.set_timeout(pynotify.EXPIRES_DEFAULT)
            n.show()
        else:
            pass
            
        
class PeriscopeInvoker(threading.Thread):
    ''' Thread that will call persicope in the background'''
    def __init__(self, filenames, callback, cache_folder):
        self.filenames = filenames
        self.callback = callback
        self.found = []
        self.notfound = []
        self.cache_folder = cache_folder
        threading.Thread.__init__(self)

    def run(self):
        subdl = periscope.Periscope(self.cache_folder)
        for filename in self.filenames:
            subtitle = subdl.downloadSubtitle(filename, subdl.preferedLanguages)
            if subtitle:
                self.found.append(subtitle)
            else:
                self.notfound.append({"filename": filename })
        self.callback(self.found, self.notfound)
