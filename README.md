# draw-o-matic #

This tiny script generates fancy Images from ANY given file.


## REQUIREMENTS ##

* Python 2.7
* Python PIL
* Linux (works probably on other platforms ;)


## HOW TO USE ##

Open a terminal and go into the folder where this script is,

then just run:
>    python startTerminal.py if=mySuperFile.sh of=fancy_image_of_file.png

Sure, you can use any fullpath:
>    python startTerminal.py if=/home/mysuperuser/bigFile.iso of=/home/images/fancy_image_of_file.png

you can set the pixel size with:
>    python startTerminal.py if=mF.sh of=fancy.png pixelSize=25

if you want a LARGER Image, just use:
>    python startTerminal.py if=mF.sh of=fancy.png pixelSize=52 imageX=1080 imageY=1920

**WARNING** It will overwrite the image with the same name as the of= parameter says!


### PARAMETERS ###

* if=
  * input file, could be ANY file!
  * default input file is: *walk-dark-light-5.jpg*

* of=
  * output file
  * overwrites if already exist
  * default output will go to: *createdImages/tmp.png*

* pixelSize=
  * the size 3 bytes of the input file will be represented on the final Image
  * default is 10

* imageX= imageY=
  * the X and Y size/dimensions of the final Image
  * default is 255x255