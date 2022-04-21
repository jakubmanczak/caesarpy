import math
chars = [
	'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
	'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'w', 'x', 'y', 'z'
]

file = open('file.txt', 'r')
text = file.read()
newtext = ''

print(text)
cdigit = int( input("Enter a four digit number for use as encryption key: ") )

digits = [
	math.floor( ( cdigit / 1000 ) % 10 ),
	math.floor( ( cdigit / 100 ) % 10 ),
	math.floor( ( cdigit / 10 ) % 10 ),
	math.floor( cdigit % 10 )
]
i = 0

for char in text:
	if char in char:
		index = chars.index(char)
		
		cdigit = digits[i]
		i += 1
		if i == 4:
			i = 0

		index += cdigit

		while index >= 32:
			index = index - 32
		while index <= -32:
			index = index + 32
		char = chars[index]
		newtext += char
print(newtext)

file = open('file.txt', 'w')
file.write(newtext)