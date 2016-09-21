# render a function using opengl
from pyglet.gl import *
import numpy as np

class Function:

    def __init__(self):
        self.step = 0.1
        self.y = self.x = np.arange(self.minx, self.maxx, self.step, dtype=np.float32)
        self.minx = -1
        self.maxx = 1

    def render(self):
        glColor3f(1, 0, 0)
        glBegin(GL_LINES)
        for i in range(1, self.x.size):
            glVertex2f(self.x[i - 1], self.y[i - 1])
            glVertex2f(self.x[i], self.y[i])
        glEnd()
        return self

    def compute(self, x):
        pass

# From here on, define your Functions to use SimAnnealing upon
# you just have to define the interval on which the Function is defined
# and how to compute it

class StrangeFun(Function):
    def __init__(self):
        self.step = 0.01
        self.minx = -10
        self.maxx = +10
        self.x = np.arange(self.minx, self.maxx, self.step, dtype=np.float32)
        self.y = self.compute(self.x)

    def compute(self, x):
        return np.cos(x) + np.cos(x*2 - 0.5) / 2 * np.sin(x*2)

class Sin(Function):
    def __init__(self):
        self.step = 0.01
        self.minx = -10
        self.maxx = +10
        self.x = np.arange(self.minx, self.maxx, self.step, dtype=np.float32)
        self.y = self.compute(self.x)

    def compute(self, x):
        return np.sin(x)

class Cos(Function):
    def __init__(self):
        self.step = 0.01
        self.minx = -10
        self.maxx = +10
        self.x = np.arange(self.minx, self.maxx, self.step, dtype=np.float32)
        self.y = self.compute(self.x)

    def compute(self, x):
        return np.cos(x)

class Pow2(Function):
    def __init__(self):
        self.step = 0.01
        self.minx = -10
        self.maxx = +10
        self.x = np.arange(self.minx, self.maxx, self.step, dtype=np.float32)
        self.y = self.compute(self.x)

    def compute(self, x):
        return np.power(x, 2)
