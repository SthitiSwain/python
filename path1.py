'''
Created on 18-May-2017

@author: sbig
'''
'''
Created on 17-May-2017(1,1),

@author: sbig
'''
 #TODO: len should give the actual length covered by 
# the path
import matplotlib.pyplot as plt
import itertools
import random
##from random import choices
#set_of_points=set((4,2),(10,9),(12,14),(1,1),(5,6),(10,13),(9,1))
class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return "<POINT: x=%d, y=%d>"%(self.x,self.y)
    def __repr__(self):
        return  self.__str__()
    
#def get_random_point(start,end):
#    rv = random.choices(range(start,end),k=2)
 #   return rv 
#print(get_random_point(10,15))
#set_of_points=set([Point(*i) for i in itertools.izip([random.shuffle(range(0,15))],[random.shuffle(range(0,12))])])
c= (range(0,15))
random.shuffle(c)
d= (range(0,15))
random.shuffle(d)
set_of_points=set([Point(*i) for i in zip(c,d)])
print (set_of_points)
#print ( i for i in itertools.izip([random.shuffle(range(0,15))],[random.shuffle(range(0,12))]))
#print (i for i in set_of_points)
#print (set_of_points)

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
  #  def __str__(self):
  #      return "sides ({}),{},{},{}".format ((i.x,i.y) for i in self.points)
    

        
def Map(path):
    
    plt.plot([i.x for i in path],[i.y for i in path],'b-',[j.x for j in set_of_points],[j.y for j in set_of_points],'ro')

# get maix x and y from points collection 
    plt.axis([min([i.x for i in set_of_points]),max([i.x for i in set_of_points])+5,min([i.y for i in set_of_points]),max([i.y for i in set_of_points])+5])
    plt.show()
p1 = Path()
#points=input('write points you want in path:')
points=random.sample(set_of_points,5)
print (points)
#list_of_point_obj = [Point(*i) for i in points]

p1.add(*points)
#print (p1.points)
Map(p1.points)

#print(p1.num_len)


# Two cases:
# 1.) p1.add(point)
# 2.) p1.add([point,point])