class sagar:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def G(self):
    print("HELLO DEMO")

class Tg:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def G(self):
    print("HELLO WORLD")

class tgmec:
  def __init__(self, c, d):
    self.c = c
    self.d = d

  def G(self):
    print("HELLO SAGAR")

sagar1 = sagar("hello", "sagar")    
tg1 = Tg("x", "demo") 
tgmec1 = tgmec("tg", "123456")    

for x in (sagar1, tg1, tgmec1):
  x.G()
