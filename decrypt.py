chars = [
	'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
	'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'w', 'x', 'y', 'z'
]

file = open('file.txt', 'r')
text = file.read()
newtext = ''

for char in chars:
	newtext = ''
	cdigit = -(chars.index(char))
	for char in text:
		index = chars.index(char)
		index += cdigit
		char = chars[index]
		newtext += char
	print(newtext)