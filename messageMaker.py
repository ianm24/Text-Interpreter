# Program Made By: Ian McDowell
# Started 3 January 2019 
# Letters finished 3 January 2019
import alphabet

fontSize = int(raw_input("Enter a font size:"))
message = str(raw_input("Enter a message:"))

# values
color = [255,255,255,255]
fontColor = [0,0,0,255]
fileName = 'message_test'
width = ((5*fontSize) * len(message)) + (fontSize *(len(message)))
height = 7*fontSize
indentX = 1
defaultIndX = 6
oneLineIndX = 5
middleIndX = 4
indentY = 1

#new image
alphabet.newImg(width,height,color,fileName)

#interpret message
for x in range(len(message)):
	if message[x] == "A":
			alphabet.a(True,indentX,indentY,fontSize,fontColor,fileName)
			indentX = indentX + defaultIndX
	elif message[x] == "a":
		alphabet.a(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "B":
		alphabet.b(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "b":
		alphabet.b(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "C":
		alphabet.c(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "c":
		alphabet.c(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "D":
		alphabet.d(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "d":
		alphabet.d(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "E":
		alphabet.e(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "e":
		alphabet.e(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "F":
		alphabet.f(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "f":
		alphabet.f(False,indentX,indentY,fontSize,fontColor,fileName)
		# ~(-*-)~
		indentX = indentX + oneLineIndX
	elif message[x] == "G":
		alphabet.g(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "g":
		alphabet.g(False,indentX,indentY+1,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "H":
		alphabet.h(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "h":
		alphabet.h(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "I":
		alphabet.i(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "i":
		if indentX - 2 < 1:
			indentX = 1
		else:
			indentX = indentX - 2
		alphabet.i(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + middleIndX
	elif message[x] == "J":
		alphabet.j(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "j":
		alphabet.j(False,indentX,indentY+1,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "K":
		alphabet.k(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "k":
		alphabet.k(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "L":
		alphabet.l(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "l":
		if indentX - 2 < 1:
			indentX = 1
		else:
			indentX = indentX - 2
		alphabet.l(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + middleIndX
	elif message[x] == "M":
		alphabet.m(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "m":
		alphabet.m(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "N":
		alphabet.n(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "n":
		alphabet.n(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "O":
		alphabet.o(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "o":
		alphabet.o(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "P":
		alphabet.p(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "p":
		alphabet.p(False,indentX,indentY+1,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "Q":
		alphabet.q(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "q":
		alphabet.q(False,indentX,indentY+1,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "R":
		alphabet.r(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "r":
		alphabet.r(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "S":
		alphabet.s(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "s":
		alphabet.s(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "T":
		alphabet.t(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "t":
		alphabet.t(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "U":
		alphabet.u(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "u":
		alphabet.u(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "V":
		alphabet.v(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "v":
		alphabet.v(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "W":
		alphabet.w(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "w":
		alphabet.w(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "X":
		alphabet.x(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "x":
		alphabet.x(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "Y":
		alphabet.y(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "y":
		alphabet.y(False,indentX,indentY+1,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == "Z":
		alphabet.z(True,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + defaultIndX
	elif message[x] == "z":
		alphabet.z(False,indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == " ":
		indentX = indentX + middleIndX
	elif message[x] == "!":
		if indentX - 2 < 1:
			indentX = 1
		else:
			indentX = indentX - 2
		alphabet.exclamation(indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + middleIndX
	elif message[x] == "?":
		alphabet.qmark(indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + oneLineIndX
	elif message[x] == ",":
		alphabet.comma(indentX,indentY+1,fontSize,fontColor,fileName)
		indentX = indentX + 3
	elif message[x] == ":":
		if indentX - 2 < 1:
			indentX = 1
		else:
			indentX = indentX - 2
		alphabet.colon(indentX,indentY,fontSize,fontColor,fileName)
		indentX = indentX + middleIndX
