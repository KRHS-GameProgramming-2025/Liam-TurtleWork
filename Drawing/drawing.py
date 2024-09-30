from shapes_new import *

def house (t, size = 10, color=None):
  square(t, size*7, 0, None, color)
  
  move(t,1*size,0*size)
  door(t,size, "tan")
  move(t,-1*size,0*size)
  
  move(t,4*size,1*size)
  window(t,size,)
  move(t,-4*size,-1*size)
  
  move(t,4*size,4*size)
  window(t,size,)
  move(t,-4*size,-4*size)
  
  move(t,1*size,4*size)
  window(t,size,)
  move(t,-1*size,-4*size)
  
  move(t,-1*size,7*size)
  roof(t,size)
  move(t,1*size,-7*size)
  
  move(t,-7*size,0*size)
  garage(t,size, color)
  move(t,-7*size,0*size)
    
 
def garage(t,size =10, color=None):
     rect(t, size*7, size*4, 0, None, color)
     
     move(t,size*0, size*4)
     right_tri(t,size*7, size*2, 0, None, "gray")
     move(t,size*0, size*-4)
     
     move(t,size*1, 0)
     garage_door(t,size)
     move(t,size*1, 0)
 
def garage_door(t,size =10, color=None):
    rect(t,size*5, size*1, 0, None, color)
    
    rect(t,size*5, size*1, 0, None, "light gray")
    move(t,0*size,size*1)
    rect(t,size*5, size*1, 0, None, "light gray")
    move(t,0*size,size*1)
    rect(t,size*5, size*1, 0, None, "light gray")
    move(t,0*size,size*1)
    
    move(t,size*0, -3)
    
 
def door(t, size =10, color=None):
  rect(t, size*1, size*2, 0, None, color)
  
  move(t,size*.8,size*1)
  arc(t,size*.1,360,0,None, "gray")
  move(t,size*-.8,size*-1)

def roof(t,size=10):
    move(t,6*size,1*size)
    chimney(t,size)
    move(t,-6*size,-1*size)
    
    sss_tri(t,9*size,6*size,6*size, 0, None, "gray")
    
def chimney(t,size=10):
    rect(t,size*1,size*3, 0, None, "tan")
    
def window(t,size=10):
    square(t,size*1, 0, None, "white")
    move(t,1*size,0)
    square(t,size*1, 0, None, "white")
    move(t,-1*size,1*size)
    square(t,size*1, 0, None, "white")
    move(t,1*size,0)
    square(t,size*1, 0, None, "white")
    move(t,-1*size,-1*size)
