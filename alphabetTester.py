# Program Made By: Ian McDowell
# Started and finished 3 January 2019
import alphabet

# values
color = [255,255,255,255]
fontColor = [0,0,0,255]
fileName = 'alphabet'

#makes the new image file
alphabet.newImg(850,250,color,fileName)

#print out of the alphabet with uppercase and lowercase letters
def alphabetTest():	
	#line 1
	alphabet.a(True,1,1,10,fontColor,fileName)
	alphabet.a(False,7,1,10,fontColor,fileName)
	alphabet.b(True,13,1,10,fontColor,fileName)
	alphabet.b(False,19,1,10,fontColor,fileName)
	alphabet.c(True,25,1,10,fontColor,fileName)
	alphabet.c(False,31,1,10,fontColor,fileName)
	alphabet.d(True,37,1,10,fontColor,fileName)
	alphabet.d(False,43,1,10,fontColor,fileName)
	alphabet.e(True,49,1,10,fontColor,fileName)
	alphabet.e(False,55,1,10,fontColor,fileName)
	alphabet.f(True,61,1,10,fontColor,fileName)
	alphabet.f(False,67,1,10,fontColor,fileName)
	alphabet.g(True,73,1,10,fontColor,fileName)
	alphabet.g(False,79,1,10,fontColor,fileName)
	#line 2
	alphabet.h(True,1,7,10,fontColor,fileName)
	alphabet.h(False,7,7,10,fontColor,fileName)
	alphabet.i(True,13,7,10,fontColor,fileName)
	alphabet.i(False,19,7,10,fontColor,fileName)
	alphabet.j(True,25,7,10,fontColor,fileName)
	alphabet.j(False,31,7,10,fontColor,fileName)
	alphabet.k(True,37,7,10,fontColor,fileName)
	alphabet.k(False,43,7,10,fontColor,fileName)
	# ~(-*-)~
	alphabet.l(True,49,7,10,fontColor,fileName)
	alphabet.l(False,55,7,10,fontColor,fileName)
	alphabet.m(True,61,7,10,fontColor,fileName)
	alphabet.m(False,67,7,10,fontColor,fileName)
	alphabet.n(True,73,7,10,fontColor,fileName)
	alphabet.n(False,79,7,10,fontColor,fileName)
	#line 3
	alphabet.o(True,1,13,10,fontColor,fileName)
	alphabet.o(False,7,13,10,fontColor,fileName)
	alphabet.p(True,13,13,10,fontColor,fileName)
	alphabet.p(False,19,13,10,fontColor,fileName)
	alphabet.q(True,25,13,10,fontColor,fileName)
	alphabet.q(False,31,13,10,fontColor,fileName)
	alphabet.r(True,37,13,10,fontColor,fileName)
	alphabet.r(False,43,13,10,fontColor,fileName)
	alphabet.s(True,49,13,10,fontColor,fileName)
	alphabet.s(False,55,13,10,fontColor,fileName)
	alphabet.t(True,61,13,10,fontColor,fileName)
	alphabet.t(False,67,13,10,fontColor,fileName)
	alphabet.u(True,73,13,10,fontColor,fileName)
	alphabet.u(False,79,13,10,fontColor,fileName)
	#line 4
	alphabet.v(True,1,19,10,fontColor,fileName)
	alphabet.v(False,7,19,10,fontColor,fileName)
	alphabet.w(True,13,19,10,fontColor,fileName)
	alphabet.w(False,19,19,10,fontColor,fileName)
	alphabet.x(True,25,19,10,fontColor,fileName)
	alphabet.x(False,31,19,10,fontColor,fileName)
	alphabet.y(True,37,19,10,fontColor,fileName)
	alphabet.y(False,43,19,10,fontColor,fileName)
	alphabet.z(True,49,19,10,fontColor,fileName)
	alphabet.z(False,55,19,10,fontColor,fileName)

alphabetTest()