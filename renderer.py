import pyglet
from pyglet.gl import *

class Renderer(pyglet.window.Window):


    def __init__(self, w=800, h=800, samples=4, distance=5, updateFun=None, updateTime=0.1):
        self.w = w
        self.h = h
        self.conf = pyglet.gl.Config(double_buffer=True, depth_size=24, sample_buffers=1, samples=samples)
        super(Renderer, self).__init__(resizable=True, width=self.w, height=self.h, config=self.conf)
        # view parameters
        self.eyeDistance = distance
        self.xAngle = 0
        self.yAngle = 0
        self.do_step = updateFun
        self.step_dt = updateTime
        # things to render
        self.toRender = []
        #label

    def addToRender(self, obj):
        self.toRender.append(obj)

    def render(self):
        for obj in self.toRender:
            obj.render()

    def on_draw(self):
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLineWidth(2.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, self.w / self.h, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, self.eyeDistance, 0, 0, 0, 0, 1, 0)
        glRotatef(self.xAngle, 0, 1, 0)
        glRotatef(-self.yAngle, 1, 0, 0)
        self.renderAxis()
        self.render()
        super().flip()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & pyglet.window.mouse.LEFT:
            self.xAngle += dx
            self.yAngle += dy

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.eyeDistance += scroll_y

    def renderAxis(self):
        len = 100
        glBegin(GL_LINES)
        # X axis
        glColor3f(0, 1, 0)
        glVertex2f(-len, 0)
        glVertex2f(len, 0)
        # Y axis
        glColor3f(0, 0, 1)
        glVertex2f(0, -len)
        glVertex2f(0, len)
        glEnd()

    def on_activate(self):
        self.on_draw()

    def unschedule(self):
        if not self.do_step is None:
            pyglet.clock.unschedule(self.do_step)

    def run(self):
        if not self.do_step is None:
            pyglet.clock.schedule_interval(self.do_step, self.step_dt)
        pyglet.app.run()
