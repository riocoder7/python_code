

class  student :
    def __init__(self,name,age ,sex,course):
      self.name=name
      self.age = age
      self.sex = sex
      self.course = course
      


    def rio(self):
     
      print("name is " + self.name)
      print("age is  is "+ self.age)
      print("sex is "+ self.sex)
      print("course is "+ self.course)


s1= student("rio","20","male","bscit")
s1.rio()



# class student:
#    def _init_(self,name, sex,course,result):
#     self.name=name
#     self.sex=sex
#     self.course=course
#     self.result=result
#    def display(self):
      
#       print (self.name)
#       print (self.sex)
#       print (self.course)
#       print (self.result)

      
# s1 = student("AshwinMehta","M",'B.Sc.(IT),'96')
# s1.display()


# print (s1.name)
# print (s1.sex)
# print (s1.course)
# print (s1.result)


# s1.display('AshwinMehta','M','B. Sc.(IT)','96.8%')

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("rio", 18)
p1.myfunc()


print("\n \n \n ")




# 7B
class shape():
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def area(self):
    a = self.x * self.y
    print(a)


class square(shape):
  def __init__(self, x):
    self.x = x

  def area(self):
    b = self.x * self.x
    print(b)


s1 = shape(12,34)
s1.area()

s2 = square(34)
s2.area()




# 7C
print(" 7 c is ")
class number :
  def __init__ (self,x,y):
    self.x = x
    self.y = y

  def add(self):
    a  = self.x + self.y
    print("\n \n addtion is ",a)

  def multiplay(self):
    b = self.x * self.y
    print("\n \n \n multiplication is ",b)


ab = number(5.7,9.3)
ab.add()
ab.multiplay()









    

