# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:52:36 2019

@author: mingyux
"""


import matplotlib.pyplot as plt
 
num_list = [ 5.9,2.19,2.3,0.6,4.1,3.9,0.7,2.2 ]
num_list2 = [5.4,0.7,0.7,0.3,0.8,0.8,0.6,0.6]
name = ['C-SIM','LCSS','EDR','IRD','Fréchet','Hausdorff','Euclidean','DTW' ]
x =list(range(len(num_list)))
total_width, n = 1,4
width = total_width / n
 
plt.bar(x, num_list, width=width, label='Original trajectory',fc = 'k')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list2, width=width, label='Reduced trajectory',tick_label = name,fc = '#DCDCDC')
plt.legend()
 
plt.show()
 
plt.savefig('E:/UEF/实验/barChart.png')