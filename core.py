__author__ = 'bison'
from PIL import Image, ImageDraw


class core:

	def __init__(self, imageX, imageY, pixelSize, fileType, dpi):
		self.imageX = imageX
		self.imageY = imageY
		self.pixelSize = pixelSize
		self.img = Image.new('RGB', (imageX, imageY), "black")  # create a new black image
		self.pixels = self.img.load()  # create the pixel map
		self.fileType = fileType
		self.dpi = dpi

	def getColorTupleFromBytes(self, bytes3):
		color = (bytes3[0], bytes3[1], bytes3[2])
		return color

	def rainbow(self):
		for i in range(self.img.size[0]):  # for every pixel:
			for j in range(self.img.size[1]):
				self.pixels[i, j] = (i, j, 100)  # set the colour accordingly

	def fromFile(self, filePath):
		drawer = ImageDraw.Draw(self.img)
		f = open(filePath, 'rb')
		canDraw = True
		currentPositionX = 0
		currentPositionY = 0
		while canDraw:
			print('Current position:', currentPositionX, currentPositionY, '/', self.imageX, self.imageY)
			bytes3 = f.read(3)
			if len(bytes3) == 3:
				drawer.rectangle(
					(
						currentPositionX, currentPositionY,
						currentPositionX + self.pixelSize, currentPositionY + self.pixelSize
					),
					self.getColorTupleFromBytes(bytes3)
				)

				currentPositionX += self.pixelSize
				if currentPositionX >= self.imageX:
					currentPositionX = 0
					currentPositionY += self.pixelSize

				if currentPositionY >= self.imageY:
					canDraw = False
			else:
				canDraw = False

		f.close()

	def saveImage(self, savePath=''):
		if not savePath.lower().endswith('.' + self.fileType):
			savePath += '.' + self.fileType

		# fix sub-path
		if '/' not in savePath and '\\' not in savePath:
			savePath = 'createdImages/' + savePath

		# 72 is probably the default value?!
		if self.dpi > 0:
			self.img.save(savePath, self.fileType, dpi=(self.dpi, self.dpi))
		else:
			self.img.save(savePath, self.fileType)