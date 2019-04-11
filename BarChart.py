# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:52:36 2019

@author: mingyux
"""


import matplotlib.pyplot as plt
 
#num_list = [ 5.9,2.19,2.3,0.6,4.1,3.9,0.7,2.2 ]
#num_list2 = [5.4,0.7,0.7,0.3,0.8,0.8,0.6,0.6]
#name = ['C-SIM','LCSS','EDR','IRD','Fréchet','Hausdorff','Euclidean','DTW' ]
num_list = [ 3.77,31.55,87.55,169.67]
num_list2=[1.09,5.20,13.33,25.47]
name = ['10','30','50','70' ]
x =list(range(len(num_list)))
total_width, n = 1,4
width = total_width / n
 
#plt.bar(x, num_list, width=width, label='Reduced trajectory (Level 1)',fc = 'k')
plt.bar(x, num_list, width=width, label='Serial computing',fc = '#DCDCDC')
for i in range(len(x)):
    x[i] = x[i] + width
#plt.bar(x, num_list2, width=width, label='Reduced trajectory (Level 3)',tick_label = name,fc ='#DCDCDC' )
plt.bar(x, num_list2, width=width, label='Parallel computing',tick_label = name,fc ='k' )
plt.legend()
#plt.xlabel('Distance method')
#plt.ylabel('Time cost (ms)') 
#plt.title('Comparing time efficiency on different methods')
plt.xlabel('Number of trajectories')
plt.ylabel('Time cost (ms)') 
plt.title('Comparing time efficiency on Parallel and Serial computing')
plt.show()
 
plt.savefig('E:/UEF/实验/barChart.png')