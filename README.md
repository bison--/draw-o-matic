# draw-o-matic #

This tiny script generates fancy Images from ANY given file.


## REQUIREMENTS ##

* Python 2.7
* Python PIL
* Linux (works probably on other platforms ;)

## HOW TO USE ##

Open a terminal and go into the folder where this script is,

then just run:
>    python startTerminal if=mySuperFile.sh of=fancy_image_of_file.png

Sure, you can use any fullpath:
>    python startTerminal if=/home/mysuperuser/bigFile.iso of=/home/images/fancy_image_of_file.png

you can set the pixel size with:
>    python startTerminal if=mF.sh of=fancy.png pixelSize=25

if you want a LARGER Image, just use:
>    python startTerminal if=mF.sh of=fancy.png pixelSize=52 imageX=1080 imageY=1920

**WARNING** It will overwrite the image with the same name as the of= parameter says!
