# Introduction #

Ubuntu uses a powerful repository system to keep your software updated. This page tells you how to add the repository for periscope.


# Details #

Ubuntu 9.10 and after (Karmic Koala, Lucid Lynx) users, add the repository by typing in a terminal:
```
sudo add-apt-repository ppa:patrick-dessalle/ppa
```

Other Ubuntu users,
Open Synaptic (System > Administration > Synaptic Software Manager)
Go to Settings > Repositories
Click on the "Third-Party Software" tab and click on Add.
The apt-line to insert is:
```
deb http://ppa.launchpad.net/patrick-dessalle/ppa/ubuntu jaunty main
```

You can find more info on the PPA page:
https://launchpad.net/~patrick-dessalle/+archive/ppa