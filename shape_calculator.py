import math
class Rectangle:
   def __init__(self,width,height):
      self.width=width
      self.height=height
     
   def set_width(self,width):
      self.width=width
      
   def set_height(self,height):
      self.height=height
     
   def get_area(self):
      return self.width*self.height
     
   def get_perimeter(self):
      return 2*(self.width+self.height)
     
   def get_diagonal(self):
      return ((self.width ** 2 + self.height ** 2) ** .5)
     
   def get_picture(self):
      output=""
      if self.width>50 or self.height>50:
          return "Too big for picture."
      else:
          for i in range(0,self.height):
                 output+="*"*self.width+"\n"
          return output
        
   def __str__(self):
       return f'Rectangle(width={self.width}, height={self.height})'
      
   def get_amount_inside(self, Rectangle):
       area_fitting=self.get_area()
       area_tobefitted=Rectangle.get_area()
       no_of_fitting= area_fitting/area_tobefitted
       if no_of_fitting<0:
           return 0
       else:
         return math.trunc(no_of_fitting)
       
      
        
class Square(Rectangle):
   def __init__(self,side):
        self.side=self.width=self.height=side
     
   def set_side(self,side):
       self.side=self.width=self.height=side
     
   def set_width(self,width):
      self.side=self.width=self.height=width
      
   def set_height(self,height):
      self.side=self.width=self.height=height
     
   def __str__(self):
       return f'Square(side={self.side})'
