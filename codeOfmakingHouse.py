from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0,0.5,0.3)
    drawpionts()
    drawLines()
    glutSwapBuffers()


def drawLines():
    glBegin(GL_LINES)

    glVertex2f(250,320)
    glVertex2f(210, 280)
    glVertex2f(210, 280)
    glVertex2f(290, 280)
    glVertex2f(290, 280)
    glVertex2f(250, 320)
    glVertex2f(210, 280)
    glVertex2f(210, 210)
    glVertex2f(290, 280)
    glVertex2f(290, 210)
    glVertex2f(210, 210)
    glVertex2f(290, 210)
    glVertex2f(230, 210)
    glVertex2f(270, 210)
    glVertex2f(240, 210)
    glVertex2f(240, 230)
    glVertex2f(260, 210)
    glVertex2f(260, 230)
    glVertex2f(240, 230)
    glVertex2f(260, 230)
    glVertex2f(220, 250)
    glVertex2f(220, 260)
    glVertex2f(220, 250)
    glVertex2f(230, 250)
    glVertex2f(230, 250)
    glVertex2f(230, 260)
    glVertex2f(230, 260)
    glVertex2f(220, 260)
    glVertex2f(280, 250)
    glVertex2f(270, 250)
    glVertex2f(270, 250)
    glVertex2f(270, 260)
    glVertex2f(280, 250)
    glVertex2f(280, 260)
    glVertex2f(270, 260)
    glVertex2f(280, 260)
    glEnd()

def drawpionts():
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(255, 215)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Show House")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()




