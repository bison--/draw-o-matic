__author__ = 'bison'

import sys
import random

def copyfile(source, dest):
	open(dest, 'w').write(open(source, 'rb').read())

inputFile = 'walk-dark-light-5.jpg' #'source/house.jpg' #'walk-dark-light-5.jpg' #'house.jpg' #grumpyrainbow.jpeg
outputFile = 'createdImages/tmp_coloring.jpg'

switchColors = 'jump'

for arg in sys.argv:
	if arg == '--help' or arg == '-h':
		#TODO: OWN README!
		print 'DEFAULT VALUES'
		print 'python startRotate.py if=walk-dark-light-5.jpg of=createdImages/tmp_coloring.jpg switchColors=random'
		#f = open('README.md')
		#print f.read()
		#f.close()
		sys.exit()
	elif arg.startswith('if='):
		inputFile = arg.replace('if=', '')
	elif arg.startswith('of='):
		outputFile = arg.replace('of=', '')
	elif arg.startswith('switchColors='):
		switchColors = int(arg.replace('switchColors=', ''))


copyfile(inputFile, outputFile)

if switchColors == 'random':
	from PIL import Image
	im = Image.open(outputFile) #Can be many different formats.
	pix = im.load()
	width, height = im.size
	for y in range(width):
		for x in range(height):
			pixIndex = [0, 1, 2]
			random.shuffle(pixIndex)
			oldPix = pix[y, x]
			newPix = ( oldPix[pixIndex[0]], oldPix[pixIndex[1]], oldPix[pixIndex[2]] )
			pix[y, x] = newPix

	im.save(outputFile)

	#for row in im.si:
	#	print row
	#print im.size #Get the width and hight of the image for iterating over
	#print pix[10,10] #Get the RGBA Value of the a pixel of an image
	#pix[x,y] = value # Set the RGBA Value of the image (tuple)