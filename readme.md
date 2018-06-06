# Retrospect - Public GIT Repository #

This repository holds the main code for Retrospect. For more information of bug reporting please visit https://bitbucket.org/basrieter/xbmc-online-tv or https://www.rieter.net/content/.

# Installing Retrospect #
There are a couple of ways to install and/or update Retrospect using this GIT repository:

## 1 - Installation of Retrospect the 'Easy way' ##
If a `net.rieter.xot-x.x.x.zip` is available from the download section, this zip can be installed using Kodi's _Install from ZIP_ feature. Keep in mind that you these zip files may not always be up-to-date.

This method can also be used to install new versions of Retrospect and thus upgrading older installs.  

## 2 - Installation of Retrospect the 'Advanced way' ##
The installation comes down to putting the folders from the GIT repo (either via a _'GIT Clone'_ or _'Full Zip Download'_)in the Kodi add-on folder (very often: /home/<user>/.kodi/addons or c:\users\<user>\AppData\Roaming\Kodi\addons). The result should be that the *addons* folder now contains at least these folders:

```
 net.rieter.xot
 net.rieter.xot.channel.be
 net.rieter.xot.channel.mtg
 net.rieter.xot.channel.mtv
 net.rieter.xot.channel.nick
 net.rieter.xot.channel.no
 net.rieter.xot.channel.nos
 net.rieter.xot.channel.regionalnl
 net.rieter.xot.channel.rtlnl
 net.rieter.xot.channel.sbsnl
 net.rieter.xot.channel.se
 net.rieter.xot.channel.streams
 net.rieter.xot.channel.uk
 net.rieter.xot.channel.videos
```

### 2.A - ....via 'GIT Clone' ###
Clone the Nightly GIT repository into a folder of your choice:

```
git clone https://bitbucket.org/basrieter/xbmc-online-tv.git
```

The cloned GIT repository should contain the folders mentioned above. Now either `copy` or `symlink` (`junction` on Windows) each those folders into the Kodi Add-ons folder. I would suggest using symlinks or junctions so changes from a `git pull` are automatically available in Kodi. 

### 2.B - ....via 'Full Zip Download' ###
Download the complete GIT repo and extract it into the Kodi Add-on folder.

## 3 - Updating Retrospect ##

### 3.A - ....via 'GIT Clone' ###
Pull latest changes into your clone (located in the Kodi Add-on folder). After that remove all existing `*.pyc` and `*.pyo` files within the Retrospect folders (**don't skip this**).

### 3.B - ....via 'Full Zip Download' ###
Download the complete GIT repo. Remove all existing Retrospect folders (**don't skip this**) and extract the new ones it into the Kodi Add-on folder.

### Finalizing the update ###
In both situation run Retrospect at least once before accessing the Retrospect add-on settings. The initial run might take longer than usual, as Retrospect is initialising some stuff and downloads artwork.

# ! Be advised ! #
Retrospect will NOT auto-upate. So new version need to be installed manually. 

# Copyrights and Licenses #
*See also: http://www.rieter.net/content/xot/license/.*

## Retrospect (Dual) License ##
Retrospect Framework by Bas Rieter is licensed under a Creative Commons Attribution-Non-Commercial-No Derivative Works 3.0 Unported License. Files that belong to the Retrospect Framework have a disclaimer stating that they are licensed under the Creative Commons Attribution-Non-Commercial-No Derivative Works 3.0 Unported License.

All channels, skins and config.py (further called Retrospect Additions) are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation. Retrospect Additions are distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with Retrospect Additions. If not, see [1]. Kodi Add-on packages containing modified code must be given a different add-on identification to prevent confusion with the official packages.
Distributing Retrospect

The official add-on packages that are currently available within the official Retrospect Repository may not be distributed via other channels than the official Retrospect Repository. Only the official Retrospect Respository (net.rieter.xot.respository) package itself may be distributed and/or included within other Kodi (super) repositories.

## Disclaimer ##
Retrospect or Rieter.net are not connected to or in any other way affiliated with Kodi, Team Kodi, or the Kodi Foundation. Furthermore, any software, addons, or products offered by Retrospect or Rieter.net will receive no support in official Kodi channels, including the Kodi forums and various social networks.

## Rules & Terms ##
As more and more people are starting to make channels for the Retrospect Framework, we want to lay out some rules and terms for the channels that we will host on this site. Please stick to them before asking us to post or link to them on the site:

 1. We, the Retrospect Framework team, are not responsible for any content that is displayed using the Retrospect Framework.
 1. We, the Retrospect Framework team, do not support any kind of Adult content for the Retrospect Framework nor will we host it on our servers.

