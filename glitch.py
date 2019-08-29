__author__ = 'bison'

import random, sys

class glitch:
	def glitchFile(self, inputFile, outputFile, glitchLevel = 100):
		fullFileBytes = open(inputFile, 'rb').read()
		newFileBytes = bytearray()

		if len(fullFileBytes) > 8024:
			glitchCount = 0
			glitchTypes = ['zero', 'random']
			for i in range(0, len(fullFileBytes)):
				if i <= 1024:
					newFileBytes.append(fullFileBytes[i])
				elif glitchLevel >= random.randint(0, 10000):
					chooseGlitch = random.choice(glitchTypes)
					print('glitching:', chooseGlitch)
					if chooseGlitch == 'zero':
						newFileBytes.append(0)
					elif chooseGlitch == 'random':
						rnd = random.randint(0, 255)
						# try to not set end of file
						if rnd != 0xd9:
							newFileBytes.append(rnd)
					elif chooseGlitch == 'remove':
						pass
					glitchCount += 1
				else:
					newFileBytes.append(fullFileBytes[i])

			print(glitchCount, 'glitches')

		open(outputFile, 'wb').write(newFileBytes)
