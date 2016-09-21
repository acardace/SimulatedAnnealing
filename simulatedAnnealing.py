from pyglet.gl import *
import numpy as np

class SimulatedAnnealing:

    def __init__(self, function, tStart=15.0, tEnd=2.0,localMovement=False, dxMovement=1, scale=2.0):
        #xpos, ypos of current position
        self.scale = scale
        self.step = function.step
        self.xmin = function.minx
        self.xmax = function.maxx
        self.pos = [0, 0]
        self.pos[0] = np.random.randint(function.minx, function.maxx)
        self.pos[1] = function.compute(self.pos[0])
        self.evaluate = function.compute
        self.tmax = tStart
        self.t = tStart
        self.t_end = tEnd
        self.timer = 0.0
        self.p = 1.0
        self.local_movement = localMovement
        self.dx_interval = dxMovement
        self.run_time = tStart
        self.vline_len = 5.0
        self.y_max = np.max(function.y)
        self.y_min = np.min(function.y)

    def add_callback(self, f):
        self.callback = f

    def render(self):
        # render current solution
        glColor3f(0, 0, 0)
        glPointSize(10)
        glBegin(GL_POINTS)
        glVertex2f(self.pos[0], self.pos[1])
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(self.pos[0], self.pos[1] - self.vline_len)
        glVertex2f(self.pos[0], self.pos[1] + self.vline_len)
        glEnd()

    def decreaseT(self, dec):
        self.t -= dec

    # return next random move
    # pick is made from [xmin, xmax]
    def next_value_all_random(self):
        x = (self.xmax - self.xmin) * np.random.ranf() + self.xmin
        return x, self.evaluate(x)

    # return next random move
    # pick is made from [x-dx, x+dx]
    def next_value_int(self, dx):
        x = dx*2 * np.random.ranf() + self.pos[0]-dx
        return x, self.evaluate(x)

    # returns a value in [0,1]
    def schedule(self):
        return self.t/self.tmax

    def run(self, dt):
        self.timer += dt
        # time in seconds
        if self.timer >= 0.1:
            self.decreaseT(self.timer)
            self.run_time -= self.timer
            self.timer = 0.0
        # update T probability
        self.p = self.schedule()
        # check termination
        if self.run_time < 0:
            self.callback()
            print(self)
        else:
            # pick next move
            if(self.local_movement):
                x, y = self.next_value_int(self.dx_interval)
            else:
                x, y = self.next_value_all_random()
            # delta of energy
            # and normalization in [0,1]
            # then we scale (optional), scaling
            # helps avoiding large P(x) for minor bad moves
            d_energy = np.abs((y - self.pos[1]) /(self.y_max - self.y_min))*self.scale
            # find the minimum
            if y < self.pos[1]:
                self.pos = [x, y]
            # accept with probability e^(-(delta_energy)/temperature))
            elif self.t > self.t_end and np.exp(-(d_energy) / self.p) >= np.random.ranf():
                self.pos = [x, y]

    def __repr__(self):
        return "pos: [{x}, {y}]\nstep: {step}".format(x=self.pos[0], y=self.pos[1], step=self.step)

