class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return  "Rectangle(width={}, height={})".format(self.width, self.height)
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2*self.width + 2*self.height
  
  def get_diagonal(self):
    return pow(pow(self.width, 2) + pow(self.height, 2), .5)

  def get_picture(self):
    output = ""
    if self.height > 50 or self.width > 50:
      output = "Too big for picture."
      return output
    else:
      for i in range(0, self.height):
        for j in range(0, self.width):
          output += "*"
        output += "\n"
    return output      
  
  def get_amount_inside(self, shape):
    x = int(self.width/shape.width)
    y = int(self.height/shape.height)
    return x*y

class Square(Rectangle):
  def __init__(self, side_length):
    super().__init__(side_length, side_length)
  
  def __str__(self):
    return "Square(side={})".format(self.width)
  
  def set_side(self, side_length):
    super().set_width(side_length)
    super().set_height(side_length)