# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:28:34 2019

@author: cc
"""
from __future__ import division
import numpy as np

        
class Nature:
    def __init__(self):
        self.max_score = 1
        return
        
    def get_socre(self, code):
        score = code[0] - code[1] + 2*code[2]
        return score/self.max_score
        
        
class Population:
    def __init__(self):
        self.nature = Nature()
        self.population = 10
        self.code_length = 3
        self.code_range_min = 0
        self.code_range_max = 3
        self.code_shape = [self.population, self.code_length]
        self.code = np.random.randint(self.code_range_min,self.code_range_max,self.code_shape)
        self.son_list = []
        self.clone_list = []
        self.score = self.get_score()
        
    def get_score(self):
        self.score = [self.nature.get_socre(self.code[index]) for index in range(self.population)]                
        return self.score
        
    def mate(self, fa, mo):
        temp_son = (self.code[fa] + self.code[mo]) / 2
        self.son_list.append(temp_son)
        return temp_son

    def clone(self, index):
        temp_clone = self.code[index]
        self.clone_list.append(temp_clone)
        return temp_clone

    def variation(self, index, var_rate = 0.2, var_num = 2):
        temp_code = self.code[index]
        var_index = np.random.choice(self.population, var_num, False)
        var_rate_max = self.code_range_max / temp_code[var_index]
        var_rate_list = [np.random.ranf(1)*max_rate for max_rate in var_rate_max]
        rate_list = np.ones(self.population)
        rate_list[var_index] = var_rate_list
        temp_variation = temp_code * rate_list
        self.code[index] = temp_variation
        return temp_variation
        
    def next_gen(self):
        self.code = self.clone_list + self.son_list
        self.code = np.array(self.code)
        self.get_score()
        self.clone_list = []
        self.son_list = []
        return
    
    def gen_next(self):
        
        return


#population = Population()        