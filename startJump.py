__author__ = 'bison'

import sys
import random

def copyfile(source, dest):
	open(dest, 'w').write(open(source, 'rb').read())

inputFile = 'walk-dark-light-5.jpg' #'source/house.jpg' #'walk-dark-light-5.jpg' #'house.jpg' #grumpyrainbow.jpeg
outputFile = 'createdImages/tmp_jump.jpg'

switchColors = 'jump'

jumpX = 1
jumpY = 0

for arg in sys.argv:
	if arg == '--help' or arg == '-h':
		#TODO: OWN README!
		print 'DEFAULT VALUES'
		print 'python startRotate.py if=walk-dark-light-5.jpg of=createdImages/tmp_coloring.jpg jumpX=1 jumpY=0'
		sys.exit()
	elif arg.startswith('if='):
		inputFile = arg.replace('if=', '')
	elif arg.startswith('of='):
		outputFile = arg.replace('of=', '')
	elif arg.startswith('jumpX='):
		switchColors = int(arg.replace('jumpX=', ''))
	elif arg.startswith('jumpY='):
		switchColors = int(arg.replace('jumpY=', ''))

copyfile(inputFile, outputFile)

from PIL import Image
im = Image.open(outputFile) #Can be many different formats.
pix = im.load()
width, height = im.size

if jumpX == 1:
	rowCount = 0
	for x in range(width):
		rowCount+=1
		for y in range(height):
			if x < width-31:
				pixIndex = [0, 1, 2]
				#random.shuffle(pixIndex)

				if rowCount >= 30:
					rowCount = 0

				if rowCount > 0 and rowCount < 30:
					oldPix = pix[x + rowCount, y]
					newPix = ( oldPix[pixIndex[0]], oldPix[pixIndex[1]], oldPix[pixIndex[2]] )
					pix[x, y] = newPix

if jumpY == 1:
	rowCount = 0
	for y in range(width):
		for x in range(height):
			rowCount+=1
			if x < height-31:
				pixIndex = [0, 1, 2]
				#random.shuffle(pixIndex)

				if rowCount >= 30:
					rowCount = 0

				if rowCount > 0 and rowCount < 30:
					oldPix = pix[y , x + rowCount]
					newPix = ( oldPix[pixIndex[0]], oldPix[pixIndex[1]], oldPix[pixIndex[2]] )
					pix[y, x] = newPix

im.save(outputFile)