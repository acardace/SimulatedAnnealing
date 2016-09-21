#!/usr/bin/env python3.5
from simulatedAnnealing import *
from functions import *
import renderer


def main():
    fun = StrangeFun()
    simAnnealing = SimulatedAnnealing(fun, localMovement=False, dxMovement=0.1, tStart=15.0, tEnd=3.0)
    ren = renderer.Renderer(w=800, h=800, samples=8, distance=(fun.maxx - fun.minx),
                            updateFun=simAnnealing.run, updateTime=0.01)
    simAnnealing.add_callback(ren.unschedule)
    ren.addToRender(simAnnealing)
    ren.addToRender(fun)
    ren.run()

if __name__ == '__main__':
    main()
