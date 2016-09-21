# SimulatedAnnealing
## Description
This is just a simple implementation of the Simulated Annealing algorithm in Python with a bit of OpenGL for the graphics bits.

Being a demonstration code the only thing you have to do is:
```bash
$ ./main.py
```

## Parameters
There are few tunable parameters when calling the function SimulatedAnnealing():
* **localMovement**: if True the next move will be chosen among the position next to the current one (like Hill climbing);
* **dxMovement**:  movement offset;
* **tStart, tEnd**;

## Input function
You can choose between different functions as input to the algorithm: Sine, Cosine, StrangeFun.
```python
def main():
    fun = StrangeFun()
    ...
```
## Define your functions
Moreover you can create your own functions by subclassing the Function class and defining the interval on which the Function is defined and how to compute it.
```python
class Sin(Function):
    def __init__(self):
        self.step = 0.01
        self.minx = -10
        self.maxx = +10
        self.x = np.arange(self.minx, self.maxx, self.step, dtype=np.float32)
        self.y = self.compute(self.x)

    def compute(self, x):
        return np.sin(x)
```
------------------------------------------------------------

Copyright **Antonio Cardace** 2016, antonio@cardace.it
