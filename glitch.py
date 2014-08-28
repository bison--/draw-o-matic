__author__ = 'bison'

import random

class glitch(object):
	def glitchFile(self, inputFile, outputFile, glitchLevel = 100):
		fullFileBytes = open(inputFile).read()
		newFileBytes = ''
		if len(fullFileBytes) > 1024:
			glitchCount = 0
			glitchTypes = ['zero', 'remove', 'random']
			for i in xrange(0, len(fullFileBytes)):
				if i <= 1024:
					newFileBytes += fullFileBytes[i]
				elif glitchLevel >= random.randint(0, 10000):
					chooseGlitch = random.choice(glitchTypes)
					print 'glitching:', chooseGlitch
					if chooseGlitch == 'zero':
						newFileBytes += '0'
					elif chooseGlitch == 'random':
						newFileBytes += chr(random.randint(0, 255))
					elif chooseGlitch == 'remove':
						pass
					glitchCount += 1
				else:
					newFileBytes += fullFileBytes[i]

			print glitchCount, 'glitches'

		open(outputFile, 'w').write(newFileBytes)
