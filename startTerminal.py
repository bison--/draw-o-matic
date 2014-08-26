__author__ = 'bison'

import sys

inputFile = 'walk-dark-light-5.jpg'
outputFile = 'createdImages/tmp.png'
imageX = 255
imageY = 255
pixelSize = 10
dpi = -1
for arg in sys.argv:
	if arg == '--help':
		f = open('README.md')
		print f.read()
		f.close()
		sys.exit()
	elif arg.startswith('if='):
		inputFile = arg.replace('if=', '')
	elif arg.startswith('of='):
		outputFile = arg.replace('of=', '')
	elif arg.startswith('imageX='):
		imageX = int(arg.replace('imageX=', ''))
	elif arg.startswith('imageY='):
		imageY = int(arg.replace('imageY=', ''))
	elif arg.startswith('pixelSize='):
		pixelSize = int(arg.replace('pixelSize=', ''))
	elif arg.startswith('dpi='):
		dpi = int(arg.replace('dpi=', ''))

import core

coreWorker = core.core(imageX, imageY, pixelSize, dpi)

coreWorker.fromFile(inputFile)
coreWorker.saveImage(outputFile)
