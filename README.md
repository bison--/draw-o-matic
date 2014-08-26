# draw-o-matic #

**startFileDrawer.py** generates fancy Images from ANY given file.

**startGlitch.py** glitches ANY file, but if you wanna see something, you have to use an **JPG** ;)


## REQUIREMENTS ##

* Python 2.7
* Python PIL (sudo apt-get install python-imaging)
* Linux (works probably on other platforms ;)


## HOW TO USE ##


### startFileDrawer ###

Open a terminal and go into the folder where this script is,

then just run:
>    python startFileDrawer.py if=mySuperFile.sh of=fancy_image_of_file.png

sure, you can use any fullpath:
>    python startFileDrawer.py if=/home/mysuperuser/bigFile.iso of=/home/images/fancy_image_of_file.png

you can set the pixel size with:
>    python startFileDrawer.py if=mF.sh of=fancy.png pixelSize=25

if you want a LARGER Image, just use:
>    python startFileDrawer.py if=mF.sh of=fancy.png pixelSize=52 imageX=1080 imageY=1920

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

* dpi=
  * set the dpi
  * default is -1 for unset

* mode=
  * glitch
    * glitches the final image (works best with jpg ;)


### startGlitch ###

Open a terminal and go into the folder where this script is,

then just run:
>    python startGlitch.py if=someimagetoglitch.jpg of=fancy_glitch.jpg

you can configure the glitch-level:
>    python startGlitch.py if=someimagetoglitch.jpg of=fancy_glitch.jpg glitchLevel=10

**WARNING** It will overwrite the image with the same name as the of= parameter says!

### PARAMETERS ###

* if=
  * input file, should be a **JPG**
  * default input file is: *walk-dark-light-5.jpg*

* of=
  * output file
  * overwrites if already exist
  * default output will go to: *createdImages/glitched.jpg*

* glitchLevel=
  * X out of 1000 bytes will be glitched
  * default is 1 out of 1000 (trust me, its enough for default ;)