# ╭━━╮╱╱╱╱╱ ╭━━━╮╱╱╱╭━╮╭━╮
# ┃╭╮┃╱╱╱╱╱ ┃╭━╮┃╱╱╱┃╭╯┃╭╯
# ┃╰╯╰┳╮╱╭╮ ┃╰━╯┣━━┳╯╰┳╯╰╮
# ┃╭━╮┃┃╱┃┃ ╰━━╮┃╭╮┣╮╭┻╮╭╯
# ┃╰━╯┃╰━╯┃ ╭━━╯┃╰╯┃┃┃╱┃┃
# ╰━━━┻━╮╭╯ ╰━━━┻━━╯╰╯╱╰╯
# ╱╱╱╱╱╭━╯┃
# ╱╱╱╱╱╰━━╯

'''
(43, 14, 0) = +
(45,5,0) = -
(46, 23, 0) = .
(60, 31, 0) = <
(62, 76, 0) = >
(42, 14, 0) = *
(44, 4, 28) = ,
'''

from PIL import Image
import sys
from termcolor import colored

text = ''
memory = [0] * 1024
pointer = 0

try:
	if '.png' in sys.argv[1]:
		img = Image.open(sys.argv[1])
		width, height = img.size

		try:
			for i in range(width):
				px = img.getpixel((i,0))
				text += chr(px[0])
				# print(px)
				if text[i] == '+':
					memory[pointer] += 1
				elif text[i] == '-':
					memory[pointer] -= 1
				elif text[i] == '<':
					pointer -= 1
				elif text[i] == '>':
					pointer += 1
				elif text[i] == '*':
					memory[pointer] = 32
				elif text[i] == '.':
					print(chr(memory[pointer]), end='')
				elif text[i] == ',':
					memory[pointer] = int(input()) 
			print()
		except ValueError:
			print(colored('You enter not number!','red'))
		# print(text)
	else:
		print(colored("This img isnt .png!", 'red')); exit(1)
except IndexError:
	print(colored("You doesnt enter file name!", 'red'))
