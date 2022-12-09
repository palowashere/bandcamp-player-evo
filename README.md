bandcamp-player-evo
============

streaming random music from bandcamp by specified genre & location on https://github.com/strizhechenko/bandcamp-player

Usage
=====

``bandcamp-player-evo ["genre"] ["location"]``

Genres can be found on the bandcamp homepage. Slashes spaces and &'s in the genre name should be replaced by dashes (hip-hop/rap becomes hip-hop-rap r&b/soul becomes r-b-soul, field recordings becomes field-recordings). Location can be found in ``locations.txt``.
MPV

check https://mpv.io/manual/master/ for keyboard controls of the mpv cli music player (eg arrows to scrub, ">" to go to next track)

Installation
============
install node and npm https://nodejs.org/en/download/, tutorial (https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac)

install python version 3.4 or above+

install mpv (https://mpv.io/installation/)

install bandcamp-fetch (https://github.com/patrickkfkan/bandcamp-fetch ) with

``npm i bandcamp-fetch --save``

make sure you are in the folder you downloaded from github

``cd bandcamp-player-evo``

install the package

``pip install -e .``

Description
===========

bandcamp-player is a small command-line app to stream audio from BandCamp.com. It requires the Python interpreter, version 3.4+.

You also need mpv installed.

You also need node installed (for scrape.js)

You also need https://github.com/patrickkfkan/bandcamp-fetch (for scrape.js)

