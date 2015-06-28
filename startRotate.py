import sys
import Image

def copyfile(source, dest):
    open(dest, 'w').write(open(source, 'rb').read())

inputFile = 'walk-dark-light-5.jpg' #'house.jpg'
outputFile = 'createdImages/tmp_rotate.jpg'

rotations = 0
quality = 23
degrees = 90
for arg in sys.argv:
	if arg == '--help':
		#TODO: OWN README!
		print 'DEFAULT VALUES'
		print 'python startRotate.py if=house.jpg of=createdImages/tmp_rotate.jpg rotations=100 quality=23 degrees=90'
		#f = open('README.md')
		#print f.read()
		#f.close()
		#sys.exit()
	elif arg.startswith('if='):
		inputFile = arg.replace('if=', '')
	elif arg.startswith('of='):
		outputFile = arg.replace('of=', '')
	elif arg.startswith('rotations='):
		rotations = int(arg.replace('rotations=', ''))
	elif arg.startswith('quality='):
		quality = int(arg.replace('quality=', ''))
	elif arg.startswith('degrees='):
		quality = int(arg.replace('degrees=', ''))
		
copyfile(inputFile, outputFile)

for i in range(rotations):
	# open an image file (.bmp,.jpg,.png,.gif)
	# change image filename to something you have in the working folder
	im1 = Image.open(outputFile)
	im1 = im1.rotate(degrees)
	im1.save(outputFile, quality=quality)

#im1 = Image.open(outputFile)
#im1.save(outputFile, quality=1)


