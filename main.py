
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def point(x = 0, y = 0):
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def bintang(x= 0, y = 0):
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(27.2 + x, 19.8 + y)
    glVertex2f(28.8 + x, 18.2 + y)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(27.2 + x, 18.2 + y)
    glVertex2f(28.8 + x, 19.8 + y)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(27 + x, 19 + y)
    glVertex2f(29 + x, 19 + y)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(28 + x, 20 + y)
    glVertex2f(28 + x, 18 + y)
    glEnd()








def badan():
    glColor3ub(242, 184, 24)
    glBegin(GL_POLYGON)
    glVertex2f(15,18)
    glVertex2f(16,18)
    glVertex2f(16,19)
    glVertex2f(17,19)
    glVertex2f(17,20)
    glVertex2f(19,20)
    glVertex2f(19,19)
    glVertex2f(23,19)
    glVertex2f(24,18)
    glVertex2f(22,16)
    glVertex2f(22,14)
    glVertex2f(25,11)
    glVertex2f(24,10)
    glVertex2f(24,7)
    glVertex2f(20,3)
    glVertex2f(17,3)
    glVertex2f(16,2)
    glVertex2f(15,2)
    glVertex2f(14,3)
    glVertex2f(11,3)
    glVertex2f(7,7)
    glVertex2f(7,10)
    glVertex2f(6,11)
    glVertex2f(9,14)
    glVertex2f(9,16)
    glVertex2f(7,18)
    glVertex2f(8,19)
    glVertex2f(12,19)
    glVertex2f(12,20)
    glVertex2f(14,20)
    glVertex2f(14,19)
    glVertex2f(15,19)
    glVertex2f(15,18)
    glVertex2f(15,18)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3ub(100, 100, 100)
    glVertex2f(15,18)
    glVertex2f(16,18)
    glVertex2f(16,19)
    glVertex2f(17,19)
    glVertex2f(17,20)
    glVertex2f(19,20)
    glVertex2f(19,19)
    glVertex2f(23,19)
    glVertex2f(24,18)
    glVertex2f(22,16)
    glVertex2f(22,14)
    glVertex2f(25,11)
    glVertex2f(24,10)
    glVertex2f(24,7)
    glVertex2f(20,3)
    glVertex2f(17,3)
    glVertex2f(16,2)
    glVertex2f(15,2)
    glVertex2f(14,3)
    glVertex2f(11,3)
    glVertex2f(7,7)
    glVertex2f(7,10)
    glVertex2f(6,11)
    glVertex2f(9,14)
    glVertex2f(9,16)
    glVertex2f(7,18)
    glVertex2f(8,19)
    glVertex2f(12,19)
    glVertex2f(12,20)
    glVertex2f(14,20)
    glVertex2f(14,19)
    glVertex2f(15,19)
    glVertex2f(15,18)
    glVertex2f(15,18)
    glEnd()

def huruf():
    # F
    glColor3ub(54,54,54)
    glBegin(GL_POLYGON)
    glVertex2f(10,13)
    glVertex2f(10,9)
    glVertex2f(11,9)
    glVertex2f(11,13)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(10,11)
    glVertex2f(13,11)
    glVertex2f(13,10)
    glVertex2f(10,10)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(10,13)
    glVertex2f(13,13)
    glVertex2f(13,12)
    glVertex2f(10,12)
    glEnd()
    
    # glColor3ub(0,0,0)
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(10,13)
    # glVertex2f(13,13)
    # glVertex2f(13,12)
    # glVertex2f(11,12)
    # glVertex2f(11,11)
    # glVertex2f(13,11)
    # glVertex2f(13,10)
    # glVertex2f(11,10)
    # glVertex2f(11,9)
    # glVertex2f(10,9)
    # glVertex2f(10,13)
    # glEnd()
    
    # C
    glColor3ub(54,54,54)
    glBegin(GL_POLYGON)
    glVertex2f(14,13)
    glVertex2f(17,13)
    glVertex2f(17,12)
    glVertex2f(14,12)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(14,10)
    glVertex2f(17,10)
    glVertex2f(17,9)
    glVertex2f(14,9)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(14,13)
    glVertex2f(15,13)
    glVertex2f(15,9)
    glVertex2f(14,9)
    glEnd()

    # glColor3ub(0,0,0)
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(14,13)
    # glVertex2f(17,13)
    # glVertex2f(17,12)
    # glVertex2f(15,12)
    # glVertex2f(15,10)
    # glVertex2f(17,10)
    # glVertex2f(17,9)
    # glVertex2f(14,9)
    # glEnd()

    # B
    glColor3ub(54,54,54)
    glBegin(GL_POLYGON)
    glVertex2f(18,13)
    glVertex2f(21,13)
    glVertex2f(21,9)
    glVertex2f(18,9)
    glEnd()
    glColor3ub(242, 184, 24)
    glBegin(GL_POLYGON)
    glVertex2f(19,12)
    glVertex2f(20,12)
    glVertex2f(20,11.5)
    glVertex2f(19,11.5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(19,10.5)
    glVertex2f(20,10.5)
    glVertex2f(20,10)
    glVertex2f(19,10)
    glEnd()

def benderaBawah1():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(8,9)
    glVertex2f(8,7)
    glVertex2f(10,5)
    glVertex2f(10,9)
    glEnd()

def benderaBawah1OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(8,9)
    glVertex2f(8,7)
    glVertex2f(10,5)
    glVertex2f(10,9)
    glEnd()

def benderaBawah2():
    glBegin(GL_POLYGON)
    glColor3ub(222, 7, 0)
    glVertex2f(10,5)
    glVertex2f(11,4)
    glVertex2f(12,4)
    glVertex2f(12,9)
    glVertex2f(10,9)
    glEnd()

def benderaBawah2OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(10,5)
    glVertex2f(11,4)
    glVertex2f(12,4)
    glVertex2f(12,9)
    glVertex2f(10,9)
    glEnd()

def benderaBawah3():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(12,4)
    glVertex2f(14,4)
    glVertex2f(14,9)
    glVertex2f(12,9)
    glEnd()

def benderaBawah3OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(12,4)
    glVertex2f(14,4)
    glVertex2f(14,9)
    glVertex2f(12,9)
    glEnd()

def benderaBawah4():
    glBegin(GL_POLYGON)
    glColor3ub(222, 7, 0)
    glVertex2f(14,4)
    glVertex2f(17,4)
    glVertex2f(17,5)
    glVertex2f(14,5)
    glEnd()

def benderaBawah4OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(14,4)
    glVertex2f(17,4)
    glVertex2f(17,5)
    glVertex2f(14,5)
    glEnd()

def benderaBawah5():
    glBegin(GL_POLYGON)
    glColor3ub(222, 7, 0)
    glVertex2f(14,8)
    glVertex2f(17,8)
    glVertex2f(17,9)
    glVertex2f(14,9)
    glEnd()

def benderaBawah5OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(14,8)
    glVertex2f(17,8)
    glVertex2f(17,9)
    glVertex2f(14,9)
    glEnd()

def bola():
    glBegin(GL_POLYGON)
    glColor3ub(255, 234, 0)
    glVertex2f(14,5)
    glVertex2f(17,5)
    glVertex2f(17,8)
    glVertex2f(14,8)
    glEnd()

def bolaOTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(14,5)
    glVertex2f(17,5)
    glVertex2f(17,8)
    glVertex2f(14,8)
    glEnd()

def benderaBawah6():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(17,4)
    glVertex2f(19,4)
    glVertex2f(19,9)
    glVertex2f(17,9)
    glEnd()

def benderaBawah6OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(17,4)
    glVertex2f(19,4)
    glVertex2f(19,9)
    glVertex2f(17,9)
    glEnd()

def benderaBawah7():
    glBegin(GL_POLYGON)
    glColor3ub(222, 7, 0)
    glVertex2f(19,4)
    glVertex2f(20,4)
    glVertex2f(21,5)
    glVertex2f(21,9)
    glVertex2f(19,9)
    glEnd()

def benderaBawah7OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(19,4)
    glVertex2f(20,4)
    glVertex2f(21,5)
    glVertex2f(21,9)
    glVertex2f(19,9)
    glEnd()

def benderaBawah8():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(21,5)
    glVertex2f(23,7)
    glVertex2f(23,9)
    glVertex2f(21,9)
    glEnd()

def benderaBawah8OTL():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 255, 255)
    glVertex2f(21,5)
    glVertex2f(23,7)
    glVertex2f(23,9)
    glVertex2f(21,9)
    glEnd()
    
def benderaAtasKiri():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(8, 18)
    glVertex2f(15, 18)
    glVertex2f(15, 16)
    glVertex2f(10, 16)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(15, 16)
    glVertex2f(10, 16)
    glVertex2f(10, 14)
    glVertex2f(15, 14)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(10, 14)
    glVertex2f(9, 13)
    glVertex2f(15, 13)
    glVertex2f(15, 14)
    glEnd()
    glColor3ub(252, 3, 3)
    glBegin(GL_QUADS)
    glVertex2f(11.5, 18)
    glVertex2f(13.5, 18)
    glVertex2f(13.5, 13)
    glVertex2f(11.5, 13)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(15, 16)
    glVertex2f(15, 14)
    glVertex2f(10, 14)
    glVertex2f(10, 16)
    glEnd()

def benderaAtasKanan():
    glColor3ub(255, 221, 0)
    glBegin(GL_POLYGON)
    glVertex2f(16, 18)
    glVertex2f(23, 18)
    glVertex2f(21, 16)
    glVertex2f(21, 14)
    glVertex2f(22, 13)
    glVertex2f(16, 13)
    glEnd()
    glColor3ub(252, 3, 3)

    for i in range(0,3,2):
        glBegin(GL_QUADS)
        glVertex2f(17 + i, 18)
        glVertex2f(18 + i, 18)
        glVertex2f(18 + i, 13)
        glVertex2f(17 + i, 13)
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
    badan()
    huruf()
    bintang()
    bintang(-2, 10)
    bintang(-12, 10)
    bintang(-6, 6)
    bintang(-18, 6)
    bintang(-21, 10)
    bintang(-23, 0)
    point(5, 3)
    point(25, 3)
    point(15, 25)
    
    #bendera bawah
    benderaBawah1()
    benderaBawah1OTL()
    benderaBawah2()
    benderaBawah2OTL()
    benderaBawah3()
    benderaBawah3OTL()
    benderaBawah4()
    benderaBawah4OTL()
    benderaBawah5()
    benderaBawah5OTL()
    bola()
    bolaOTL()
    benderaBawah6()
    benderaBawah6OTL()
    benderaBawah7()
    benderaBawah7OTL()
    benderaBawah8()
    benderaBawah8OTL()
    benderaAtasKiri()
    benderaAtasKanan()
    glutSwapBuffers()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("Tugas Minggu 4")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

