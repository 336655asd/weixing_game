# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:50:21 2019

@author: cc
"""

import tkinter as tk
import numpy as np
import rules

win = tk.Tk()
win.title('Gen')
win.geometry('500x400')

population = rules.Population()

class Widget():
    def __init__(self, population, window):
        self.population = population
        self.code_num = self.population.population
        self.check_mate = [tk.IntVar() for i in range(self.code_num)]
        self.check_clone = [tk.IntVar() for i in range(self.code_num)]
        self.code = self.population.code
        self.frame_list = None
        self.individual_list = None
        self.check_button_mate = None
        self.check_button_clone = None
        self.mt_list = []
        self.clone_list = []
        self.flag = 0
        self.window = window
        self.main_frame = tk.Frame(window)
        self.main_frame.pack()
        self.button_list = []
        
    def gen_label(self, frame, color, text):
        return tk.Label(frame, text=text, bg=color, font=('Arial', 12), width=4, height=1)
    
    def gen_frame(self, window):
        frame = tk.Frame(window)
        return frame
    
    def gen_individual(self, window, code_idx, score=80, code_length=3):
        frame = self.gen_frame(window)
        color_list = ['white']*self.code.shape[1]
        grid_index = range(1,4)
        label_list = [self.gen_label(frame, color, text) for color,text in zip(color_list,self.code[code_idx]) ]
        map(lambda label, index: label.grid(row=0, column=index,padx=0, pady=1,ipadx=1, ipady=1), label_list, grid_index)
        check_button_mate = tk.Checkbutton(frame, text='score: '+str(self.population.score[code_idx]), variable=self.check_mate[code_idx], onvalue=1, offvalue=0)
        check_button_mate.grid(row=0, column=self.code.shape[1]+1, padx=2)
        check_button_clone = tk.Checkbutton(frame, text='if_clone', variable=self.check_clone[code_idx], onvalue=1, offvalue=0)
        check_button_clone.grid(row=0, column=self.code.shape[1]+2, padx=2)

        return [frame,label_list, check_button_mate, check_button_clone] 
            
    def gen_population(self, window):
        frame = tk.Frame(window)
        population_menu = [self.gen_individual(frame, index) for index in range(self.code_num)]
        grid_index = range(self.code_num)
        map(lambda frame_dic, index: frame_dic[0].grid(row=index, column=0),population_menu, grid_index)
        frame.pack()
        self.frame_list = [menu[0] for menu in population_menu]
        self.individual_list = [menu[1] for menu in population_menu]
        self.check_button_mate = [menu[2] for menu in population_menu]
        self.check_button_clone = [menu[3] for menu in population_menu]
        return population_menu, frame
    
    def click_mate(self):
        sum_mt_var = sum([x.get() for x in self.check_mate])
        if sum_mt_var == 2:        
            for i in range(self.code_num):
                if self.check_mate[i].get() == 1:
                    self.mt_list.append(i)
                    self.mt_list = list(set(self.mt_list))

            for i in self.mt_list:
                self.check_mate[i].set(0)
                self.check_button_mate[i].config(state = tk.DISABLED)
            print(self.mt_list)
            self.population.mate(self.mt_list[0], self.mt_list[1])
            self.mt_list = []
            self.flag += 1
            print('flag: ',self.flag)
        else:
            print("please select 2 individual")
            
    def click_clone(self):
        sum_cl_var = sum([x.get() for x in self.check_clone])
        print(sum_cl_var)
        if sum_cl_var == 5:
            for i in range(self.code_num):
                if self.check_clone[i].get() == 1:
                    self.clone_list.append(i)
                    self.population.clone(i)
                    self.check_clone[i].set(0)
                self.check_button_clone[i].config(state = tk.DISABLED)
            self.flag += 1    
            print('flag: ',self.flag)
            print("clone done")
        else:
            print("you must choose 5 individual")
        return
    
    def click_next(self):
        print(self.flag)
        if self.flag == 6:
            self.next_gen()
            self.flag = 0
        else:
            print("you must mate and clone first")
    
    def next_gen(self):
        self.population.next_gen()
        self.check_mate = [tk.IntVar() for i in range(self.code_num)]
        self.check_clone = [tk.IntVar() for i in range(self.code_num)]
        self.code = self.population.code
        self.frame_list = None
        self.individual_list = None
        self.check_button_mate = None
        self.check_button_clone = None
        self.mt_list = []
        self.clone_list = []
        self.main_frame.destroy()
        map(lambda x: x.destroy(), self.button_list)
        self.button_list = []
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack()
        self.build_win(self.main_frame)        
    
    
    def build_win(self, window):
        self.gen_population(window)
        button = tk.Button(win, text='mate',  font=('Arial', 12), width=10, height=1, command=self.click_mate)
        button.pack()
        self.button_list.append(button)
        button = tk.Button(win, text='clone',  font=('Arial', 12), width=10, height=1, command=self.click_clone)
        button.pack()
        self.button_list.append(button)
        button = tk.Button(win, text='next',  font=('Arial', 12), width=10, height=1, command=self.click_next)
        button.pack()
        self.button_list.append(button)
        
widget = Widget(population, win)    
widget.build_win(widget.main_frame)
