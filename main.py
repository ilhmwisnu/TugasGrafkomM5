from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def benderaAtas():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(8, 18)
    glVertex2f(10, 16)
    glVertex2f(10, 14)
    glVertex2f(9, 13)
    glEnd()
    glColor3ub(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(8, 18)
    glVertex2f(15, 18)
    glVertex2f(15, 13)
    glVertex2f(9, 13)
    glVertex2f(10, 14)
    glVertex2f(10, 16)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 30, 0.0, 30, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(2, 0.3, 2)
    benderaAtas()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("Tugas Minggu 4")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
