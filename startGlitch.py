__author__ = 'bison'
import glitch
import sys

inputFile = 'walk-dark-light-5.jpg'
outputFile = 'createdImages/glitched.jpg'
glitchLevel = 1

for arg in sys.argv:
	if arg.startswith('if='):
		inputFile = arg.replace('if=', '')
	elif arg.startswith('of='):
		outputFile = arg.replace('of=', '')
	elif arg.startswith('glitchLevel='):
		glitchLevel = int(arg.replace('glitchLevel=', ''))


gl = glitch.glitch()
gl.glitchFile(inputFile, outputFile, glitchLevel)