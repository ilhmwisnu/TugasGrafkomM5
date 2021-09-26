from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def segiTiga():
    glColor3ub(100,100,100)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100,100)
    glVertex2f(200,100)
    glVertex2f(150,300)
    glEnd()

def kubus():
    glColor3ub(100,100,100)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(300,300)
    glVertex2f(500,300)
    glVertex2f(500,500)
    glVertex2f(300,500)
    glEnd()
    # glPointSize(100.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(300,500)
    glVertex2f(360,520)
    glVertex2f(560,520)
    glVertex2f(500,500)
    glEnd()
    # glPointSize(100.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(500,500)
    glVertex2f(560,520)
    glVertex2f(560,320)
    glVertex2f(500,300)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 750, 0.0, 750, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(2, 0.3, 2)
    segiTiga()
    kubus()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("Tugas Minggu 4")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
