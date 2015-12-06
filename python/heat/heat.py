#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def initial_func(xx):
    length_xx = len(xx)
    y = np.zeros(length_xx)
    for i in range(length_xx):
        x = xx[i]

        if x <= -1 or x >= 1:
            y[i] = 0
        else:
            y[i] = np.exp(- 1 / (1 - x**2))
    return y

def laplacian(uu):
    length_uu = len(uu)
    y = np.zeros(length_uu)

    for i in range(length_uu):
        u = uu[i]
        left_u  = 0
        right_u = 0
        if i - 1 >= 0:
            left_u = uu[i - 1]
        if i + 1 < length_uu:
            right_u = uu[i + 1]

        y[i] = (left_u + right_u - 2*u) / 2;
    return y

class HeatEquation(object):
    def __init__(self):
        self.w  = 10 # half width of bar
        self.dx = 0.05
        self.dt = self.dx**2
        self.T  = 10 # total elapsed time [sec]

        self.n  = int(self.T/self.dt) # step num
        # sampling on x-axis
        self.xx = np.linspace(-self.w, self.w, int(2*self.w/self.dx))
        self.u  = None

        self.__setup()

    def solve(self):
        length_xx = len(self.xx)

        # solve heat equation by forward Euler method
        for step in range(self.n-1):
            t = self.dt * step # current time
            self.u[step + 1, :] = self.u[step, :] + laplacian(self.u[step, :])

    def show(self):
        plt.plot(self.xx, self.u[0,:], "r")
        plt.plot(self.xx, self.u[int(self.n/5),:], "b")
        plt.plot(self.xx, self.u[int(2*self.n/5),:], "k")
        plt.plot(self.xx, self.u[int(3*self.n/5),:], "g")
        plt.plot(self.xx, self.u[int(4*self.n/5),:], "y")
        plt.plot(self.xx, self.u[self.n-1,:], "m")
        plt.axis([-10, 10, 0, 0.4])
        plt.show()

    def __setup(self):
        length_xx = len(self.xx)

        # solutions at each time
        self.u = np.zeros([self.n, length_xx])
        # initial value
        self.u[0,:] = initial_func(self.xx)

################################################################################

heat = HeatEquation()
heat.solve()
heat.show()
