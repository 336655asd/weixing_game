# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:28:34 2019

@author: cc
"""

import numpy as np

        
class Nature:
    def __init__(self):
        self.max_score = 100
        return
        
    def rule(self, code):
        score = code[0] - code[1] + 2*code[2]
        return score
        
        
class Population:
    def __init__(self):
        nature = Nature()
        self.code = np.random.randint(3,10)

    def mate(self):
        return

    def clone(self):
        return

    def variation(self):
        return 

    def eliminate(self):
        return


population = Population()        