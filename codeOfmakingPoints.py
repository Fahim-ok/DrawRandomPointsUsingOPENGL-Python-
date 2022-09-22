import  random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *




def drawpoints():

    glBegin
    for p in range(50):
        glPointSize(5)
        a = random.randint(0, 600)
        b = random.randint(0, 600)
        glBegin(GL_POINTS)
        glVertex2f(a, b)
        glEnd()

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
    glColor3f(1.0, 0.5, 0.3)
    drawpoints()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Show Points")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()