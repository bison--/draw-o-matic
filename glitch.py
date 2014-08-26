__author__ = 'bison'

import random

class glitch(object):
	def glitchFile(self, inputFile, outputFile, glitchLevel = 100):
		fullFileBytes = open(inputFile).read()
		newFileBytes = ''
		if len(fullFileBytes) > 1024:
			glitchCount = 0
			glitchTypes = ['zero', 'remove']
			for i in xrange(0, len(fullFileBytes)):
				if i <= 1024:
					newFileBytes += fullFileBytes[i]
				elif glitchLevel >= random.randint(0,1000):
					chooseGlitch = random.choice(glitchTypes)
					print 'glitching:', chooseGlitch
					if chooseGlitch == 'zero':
						newFileBytes += '0'
					elif chooseGlitch == 'remove':
						pass
					glitchCount += 1
				else:
					newFileBytes += fullFileBytes[i]

			print glitchCount, 'glitches'

		open(outputFile, 'w').write(newFileBytes)