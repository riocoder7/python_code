#8 a
# import gemorty 
# def pointyShapeVolume(x, h, square):
#  if square:
#   base = geometry.squareArea(x)
#  else:
#      base = geometry.circleArea(x)

#  return h * base / 3.0

# print(dir(geometry))
# print (pointyShapeVolume(4, 2.6, True))
# print(pointyShapeVolume(4, 2.6, False))


import sys
randomList = ['a', 0, 2]
for entry in randomList:
  try:
     print("The entry is", entry)
     r = 1/int(entry)
     break
  except:
      print("Oops!",sys.exc_info()[0],"occured.")
      print("Next entry.")
      print()
print("The reciprocal of",entry,"is",r)