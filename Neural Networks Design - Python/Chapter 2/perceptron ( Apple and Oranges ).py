# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:02:41 2017

@author: Chris Amirani
"""

import numpy as np
inputs= ([-1,1,1],[-1,-1,1],[1,1,-1],[1,-1,-1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,-1],
         [-1,-1,-1],[1,1,1],[1,-1,1],[1,1,1],[1,1,1],[-1,-1,1],[-1,1,1],[1,-1,1],[1,1,1],
         [1,-1,1],[1,-1,1],[-1,-1,1],[1,1,1],[1,1,1],[-1,1,1],[1,1,-1],[1,1,1],[-1,1,1],
         [1,1,1],[1,1,-1],[-1,1,1],[1,-1,1],[-1,1,-1],[-1,1,1],[1,1,1],[1,-1,-1],[-1,1,1],
         [1,1,1],[1,-1,1],[1,1,-1],[1,1,1],[1,1,-1],[1,1,1],[-1,1,1],[1,1,1],[1,1,1],[1,1,-1],
         [1,1,-1],[-1,1,1],[1,-1,1],[1,1,1],[1,1,1],[1,-1,-1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],
         [1,-1,1],[1,-1,1],[1,-1,1],[1,-1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,-1],[1,1,1],[1,1,1],
         [1,-1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[1,1,-1],[1,1,1],[1,-1,1],[1,1,1],[1,1,1],[1,-1,1],
         [1,1,1],[1,1,1],[-1,1,1],[1,1,1],[1,1,-1],[1,1,1],[1,1,-1],[-1,-1,-1],[-1,1,1],[1,-1,-1],
         [1,1,-1],[-1,1,1],[1,1,1],[1,-1,-1],[-1,1,1],[1,1,1],[-1,1,1],[1,1,1],[1,1,-1],[1,1,1],
         [-1,1,1],[1,1,1],[1,1,1],[1,-1,-1],[1,1,1],[1,1,1])

#we want the output to be 1 for apples and -1 for oranges. The weight calculation will be covered in 
#later snippets
for i in range(len(inputs)):
    output = np.dot([0,1,0],inputs[i]) + 0
    if output == 1:
        print 'Apple', output
    else:
        print 'Orange', output