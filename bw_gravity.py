# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:42:35 2019

@author: cc
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

class Gmap:
    def __init__(self):
        self.black_list = np.random.randint(1,10,100)
        self.white_list = np.random.randint(-9,0,100)
        self.dic_b = {}
        self.dic_w = {}
        self.map = np.zeros([100,100])
        
        self.gravity_atto = 1
        
        self.arrange(self.black_list, self.dic_b)
        #self.arrange(self.white_list)        
        #plt.ion()
        self.fig, self.ax = plt.subplots()
        self.orbit, = plt.plot([],[], 'ro')
        
    def arrange(self, ball_list, ball_dic):
        def random_xy():
            x = np.random.randint(0,100,1)
            y = np.random.randint(0,100,1)    
            return int(x),int(y)
            
        for i in range(len(ball_list)):
            while True:
                xy = random_xy()
                if self.map[xy] == 0:
                    self.map[xy] = ball_list[i]
                    ball_dic[xy] = ball_list[i]
                    break
               
    def draw(self):
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.grid(False)
        
        sun_x = []
        sun_y = []
        sun_c = []
        for item in self.dic_b.items():
            sun_x.append(item[0][0])
            sun_y.append(item[0][1])
            sun_c.append(item[1])
            
        self.ax.scatter(sun_x, sun_y, s = np.array(sun_c)*10, c = sun_c)
        return 
    
    def draw_animation(self, step = 1):
        ax = self.ax
        ln = self.orbit
        xdata = []
        ydata = []
        
        def init():
            ax.set_xlim(0,100)
            return ln,
            
        def update(frame):
            xdata.append(frame)
            ydata.append(frame)
            ln.set_data(xdata, ydata)
            return ln,
            
        anim = FuncAnimation(self.fig, update, frames=np.linspace(0, 100, 50), interval=10,
                    init_func=init, blit=True)
        plt.show()

gmap = Gmap()
gmap.draw()
gmap.draw_animation()





