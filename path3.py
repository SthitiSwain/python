'''
Created on 21-May-2017

@author: sbig
'''
'''
Created on 19-May-2017

@author: sbig
''''''
Created on 18-May-2017

@author: sbig
'''
'''
Created on 17-May-2017(1,1),

@author: sbig
'''
 #TODO: len should give the actual length covered by 
# the path
import numpy as np
from colorsys import hls_to_rgb
import matplotlib.pyplot as plt
import itertools
import random
import datetime



class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return "<POINT: x=%d, y=%d>"%(self.x,self.y)
    def __repr__(self):
        return  self.__str__()
    

no_of_points_in_set=input('no of points in set:')
c= range(no_of_points_in_set)
random.shuffle(c)
d= range(no_of_points_in_set)
random.shuffle(d)
set_of_points=set([Point(*i) for i in zip(c,d)])

class Path: 
    
    def __init__(self):
        self.points = []
    
    def add(self,*points):
        return self.points.extend(points)
        
    def travel(self):
        pass 
    
    def num_len(self):
        return len(self.points)

    def __len__(self):
        pass 

    

        
def Map(path):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    
    colors = []
    k=0
    for i in np.arange(0., 360., 360. / no_of_paths):
        h = i / 360.
        l = (50 + np.random.rand() * 10) / 100.
        s = (90 + np.random.rand() * 10) / 100.
        colors.append(hls_to_rgb(h, l, s))
    for pa in path:
        
            print (pa)
            print (path)
            print (colors[k])
            plt.plot([i.x for i in pa],[i.y for i in pa],
             color=colors[k],label='P'+str(k))
            print ('P'+str(k))
            k+=1
    plt.legend()
    plt.plot([j.x for j in set_of_points],
             [j.y for j in set_of_points],'ro')
            

    plt.axis([min([i.x for i in set_of_points]),
              max([i.x for i in set_of_points])+5,
              min([i.y for i in set_of_points]),
              max([i.y for i in set_of_points])+5])
    
    for xy in zip([j.x for j in set_of_points], [j.y for j in set_of_points]):
        ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
    plt.xticks(np.arange(min([i.x for i in set_of_points]), max([i.x for i in set_of_points])+1, 1.0))
    plt.yticks(np.arange(min([i.y for i in set_of_points]), max([i.y for i in set_of_points])+1, 1.0))
    #plt.show()
    fig.savefig('/home/sbig/workspace3/practice/pic/{}.png'.format(datetime.datetime.now()))
    plt.close(fig)
    print (fig)
    return fig
p1 = Path()
no_of_points=input('write no of points in a single path:')
no_of_paths=input('write no of paths:')


multiple_path_points=[]
for i in range(no_of_paths):
    single_path_points=random.sample(set_of_points,no_of_points)
    multiple_path_points.append(single_path_points)
print(multiple_path_points)


p1.add(*multiple_path_points)
print (p1.points)
Map(p1.points)


