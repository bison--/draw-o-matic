__author__ = 'bison'

import sys

inputFile = 'google_logo11w.png'
outputFile = 'tmp.png'
imageX = 255
imageY = 255
pixelSize = 10
for arg in sys.argv:
	if arg == '--help':
		print 'comming soon'
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

import core

coreWorker = core.core(imageX, imageY, pixelSize)

coreWorker.fromFile(inputFile)
coreWorker.saveImage(outputFile)
