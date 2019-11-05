#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
	Draw a circle in BresenHam algorithm.
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawCircle(x0, y0, r):
	x, y, m = 0, r, 1-r
	K = []
	K.append((x, y))

	for x in range(int(r)):
		if m < 0:
			m = m + 2 * x + 3
		else:
			y -= 1
			m = m + 2 * x + 3 - 2 * y

		K.append((x, y))

		if x >= y: break

	W = K[:]
	for i in K:
		W.append((i[1], i[0]))

	K = W[:]
	for i in W:
		K.append((-i[0], i[1]))
		K.append((i[0], -i[1]))
		K.append((-i[0], -i[1]))

	W = []
	for i in K:
		W.append((x0+i[0], y0+i[1]))

	return W

def projection():
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0, 900, 0, 600)

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 1)
	

	glBegin(GL_POINTS)

	for i in drawCircle(500, 350, 200):
		glVertex2iv(i)

	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA|GLUT_RGB)
	glutInitWindowSize(900, 600)
	glutInitWindowPosition(50, 100)
	glutCreateWindow("Simple Point")
	projection()
	glutDisplayFunc(draw)
	glutMainLoop()

if __name__ == "__main__":
	main()
