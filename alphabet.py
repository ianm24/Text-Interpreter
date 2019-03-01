# Program Made By: Ian McDowell
# Started 30 December 2018
# English Alphabet Finished 3 January 2019

from PIL import Image
import glob, os, imageio

#make new image
def newImg(width,height,color,fileName):
	global img 
	img = Image.new("RGBA",(width, height),(color[0],color[1],color[2],color[3]))
	img.save(fileName + '.PNG')

#draw pixel
def draw(x,y,indentX,indentY,fontSize,fontColor):
	img.putpixel((int(fontSize*indentX)+x,int(fontSize*indentY)+y),(fontColor[0],fontColor[1],fontColor[2],fontColor[3]))

#save image file to .PNG
def save(letter,fileName):
	path = 'output'
	if(os.path.exists(path) == False):
		os.mkdir(path)
	file = fileName + '.PNG'
	img.save(path + "/" +file)
	print("'"+letter+"' has been printed")


#drawing letters
def a(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize: #first row
					if x >= fontSize and x < (4*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= 1*fontSize) or (y >= 3*fontSize): #sides except line
					if x < fontSize or x >=4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #line
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('A',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if (y < 2*fontSize and y >= 1*fontSize): # top
					if x >= fontSize and x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 4*fontSize and y >= 2*fontSize): # middle
					if (x < fontSize or x >= 3*fontSize and x < 4*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: # bottom
					if (x >= fontSize and x < (3*fontSize)) or (x >= 4*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('a',fileName)

def b(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or (y < 3*fontSize and y >= 2*fontSize) or (y >= 4*fontSize): # top, middle, and bottom lines
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= fontSize) or (y < 4*fontSize and y >= 3*fontSize): #other two lines
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('B',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize: #tale
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 3*fontSize and y >= 2*fontSize) or (y >= 4*fontSize): # bottom and middle lines
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: # other line
					if (x < fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('b',fileName)

def c(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: #first and last lines
					if x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= fontSize: #middle lines
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('C',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if (y < 2*fontSize and y >= fontSize) or y >= 4*fontSize: #first and last lines
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 2*fontSize: #middle lines
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('c',fileName)

def d(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: #first and last lines
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= fontSize: #middle lines
					if x < fontSize or x >=4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('D',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize: #tale
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 3*fontSize and y >= 2*fontSize) or (y >= 4*fontSize): # bottom and middle lines
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: # other line
					if (x < fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('d',fileName)

def e(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or (y < 3*fontSize and y >= 2*fontSize) or y >= 4*fontSize: #first, middle, and last lines
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= fontSize) or (y < 4*fontSize and y >= 3*fontSize): #middle lines
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('E',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize and y >= fontSize: #line 1
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #line 2
					if x < fontSize or (x < 3*fontSize and x >= 2*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #line 3
					if x < 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #line 4
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('e',fileName)

def f(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or (y < 3*fontSize and y >= 2*fontSize): #first, middle, and last lines
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= fontSize) or (y >= 3*fontSize): #middle lines
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('F',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize:
					if x < 4*fontSize and x >= fontSize: #top
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #line 2
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 3*fontSize and y >= 2*fontSize) or (y >= 4*fontSize): #line 3 and 5
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize:
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('f',fileName)

def g(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: #first and last lines
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 3*fontSize and y >= fontSize): #middle lines
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize:
					if x < fontSize or (x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('G',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize:
					if x < 4*fontSize and x >= 2*fontSize: #top
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #line 2
					if (x < 2*fontSize and x >= fontSize) or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 3*fontSize and y >= 2*fontSize): #line 3
					if x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #line 4
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #line 5
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('g',fileName)

def h(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize or y >= 3*fontSize: # vertical lines
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #other line
					draw(x,y,indentX,indentY,fontSize,fontColor)
		save('H',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize: #tale
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: # middle lines
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 3*fontSize: # bottom lines
					if (x < fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('h',fileName)

def i(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: # horizontal lines
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < 3*fontSize and x >= 2*fontSize: #other line
					draw(x,y,indentX,indentY,fontSize,fontColor)
		save('I',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 2*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('i',fileName)

def j(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize: # horizontal line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < 3*fontSize and x >= 2*fontSize: #vertical line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #left dot
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize:
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('J',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or (y < 4*fontSize and y >= 2*fontSize):
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize:
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize:
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('j',fileName)

def k(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if x < fontSize: # vertical line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < fontSize or y >= 4*fontSize: # top and bottom dots
					if x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= fontSize) or (y < 4*fontSize and y >= 3*fontSize): #middle dots
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle line
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('K',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= fontSize:
					if x < fontSize: # vertical line
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 3*fontSize and y >= fontSize) or y >= 4*fontSize: #dots
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #middle line
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('k',fileName)

def l(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if x < fontSize: # vertical line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #horizontal line
					draw(x,y,indentX,indentY,fontSize,fontColor)
		save('L',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if x < 3*fontSize and x >= 2*fontSize: #lowercase L
					draw(x,y,indentX,indentY,fontSize,fontColor)
		save('l',fileName)

def m(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if x < fontSize or x >= 4*fontSize: # vertical lines
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #second line dots
					if x < 2*fontSize or x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('M',fileName)
	# ~(-*-)~
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= fontSize: #left line
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #dots
					if x < 2*fontSize or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 3*fontSize: #other lines
					if (x < 3*fontSize and x >= 2*fontSize) or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('m',fileName)

def n(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if x < fontSize or x >= 4*fontSize: # vertical lines
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #second line dot
					if x < 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #fourth line dot
					if x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('N',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= fontSize: #left line
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle line
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 3*fontSize: #right line
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('n',fileName)

def o(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: #top and bottom
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize or x >= 4*fontSize: #sides
					if y < 4*fontSize and y >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('O',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if (y < 2*fontSize and y >= fontSize) or y >= 4*fontSize: #top and bottom
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize or (x < 4*fontSize and x >= 3*fontSize): #sides
					if y < 4*fontSize and y >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('o',fileName)	

def p(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or(y < 3*fontSize and y >= 2*fontSize): #top and middle lines
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize: #left line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #dot
					if x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('P',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= fontSize: #left line
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= fontSize) or (y < 4*fontSize and y >= 3*fontSize): # two lines
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #dot
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('p',fileName)

def q(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize: #top
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize: #left
					if y < 4*fontSize and y >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x >= 4*fontSize: #right
					if y < 3*fontSize and y >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #bottom
					if (x < 3*fontSize and x >= fontSize) or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize:
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('Q',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize:
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize:
					if x < fontSize or (x < 3*fontSize and x >= 2*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize:
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize:
					if x < 4*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)

		save('q',fileName)

def r(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or(y < 3*fontSize and y >= 2*fontSize): #top and middle lines
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize: #left line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #dot
					if x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 3*fontSize:
					if x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('R',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= fontSize: #left line
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle line
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #right line
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('r',fileName)

def s(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize: #first line
					if x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #left dot
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #right dot
					if x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle line
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #last line
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)				
		save('S',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize and y >= fontSize: #first line
					if x < 4*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #left dot
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #right dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #last line
					if x < 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)				
		save('s',fileName)

def t(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize: # horizontal line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < 3*fontSize and x >= 2*fontSize: #vertical line
					draw(x,y,indentX,indentY,fontSize,fontColor)
		save('T',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 4*fontSize: #vertical line
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #horizontal line
					if x < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #right dot
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('t',fileName)

def u(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= 4*fontSize: #bottom
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize or x >= 4*fontSize: #sides
					if y < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('U',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y >= 4*fontSize: #bottom
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize or (x < 4*fontSize and x >= 3*fontSize): #sides
					if y < 4*fontSize and y >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('u',fileName)

def v(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 4*fontSize and y >= 3*fontSize:#fourth row dots
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #bottom dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if x < fontSize or x >= 4*fontSize: #sides
					if y < 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('V',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 3*fontSize and y >= 2*fontSize: #top row
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #middle row
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #bottom dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('v',fileName)

def w(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 4*fontSize: #sides
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #horizontal line
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #top dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #bottom dots
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('W',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 4*fontSize and y >= 2*fontSize: #3 vertical lines
					if x < fontSize or (x < 3*fontSize and x >= 2*fontSize) or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #bottom dots
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('w',fileName)

def x(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: #outer corner dots
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if (y < 2*fontSize and y >= fontSize) or (y < 4*fontSize and y >= 3*fontSize): #middle corner dots
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #center dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('X',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if (y < 3*fontSize and y >= 2*fontSize) or y >= 4*fontSize: #corner dots
					if x < fontSize or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #center dots
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('x',fileName)

def y(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize: #top dots
					if x < fontSize or x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #middle dots
					if (x < 2*fontSize and x >= fontSize) or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 2*fontSize: #vertical line
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('Y',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 2*fontSize and y >= fontSize: #top dots
					if x < fontSize or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #horizontal line
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #bottom right dot
					if x < 4*fontSize and x >= 3*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize: #bottom line
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('y',fileName)

def z(capitalized,indentX,indentY,fontSize,fontColor,fileName):
	if capitalized == True:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize or y >= 4*fontSize: # horizontal lines
					draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize: #right dot
					if x >= 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #left dot
					if x < fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: #middle line
					if x < 4*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('Z',fileName)
	else:
		for y in range(5*fontSize):
			for x in range(5*fontSize):
				if (y < 2*fontSize and y >= fontSize) or y >= 4*fontSize: #horizontal lines
					if x < 4*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize: # top dot
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 4*fontSize and y >= 3*fontSize: #bottom dot
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
		save('z',fileName)

#symbols
def exclamation(indentX,indentY,fontSize,fontColor,fileName):
	for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 3*fontSize or y >= 4*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
	save('exclamation', fileName)

def qmark(indentX,indentY,fontSize,fontColor,fileName):
	for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < fontSize:
					if x < 3*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 2*fontSize and y >= fontSize:
					if x < fontSize or (x < 4*fontSize and x >= 3*fontSize):
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y < 3*fontSize and y >= 2*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
	save('questionmark',fileName)

def comma(indentX,indentY,fontSize,fontColor,fileName):
	for y in range(5*fontSize):
			for x in range(5*fontSize):
				if y < 4*fontSize and y >= 3*fontSize:
					if x < 2*fontSize and x >= fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
				if y >= 4*fontSize:
					if x < 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
	save('comma',fileName)
	
def colon(indentX,indentY,fontSize,fontColor,fileName):
	for y in range(5*fontSize):
			for x in range(5*fontSize):
				if (y >= fontSize and y < 2*fontSize) or y >= 4*fontSize:
					if x < 3*fontSize and x >= 2*fontSize:
						draw(x,y,indentX,indentY,fontSize,fontColor)
	save('colon',fileName)
