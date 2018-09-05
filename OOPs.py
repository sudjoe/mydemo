# How to define Python classes
# Example file for working with classes
class myClass():
  def method1(self):
      print "Guru99"
        
  def method2(self,someString):    
      print "Software Testing:" + someString      
   
def main():           
  # exercise the class methods
  c = myClass ()
  c.method1()
  c.method2(" Testing is fun")
  
if __name__== "__main__":
  main()


#How Inheritance works
# Example file for working with classes
class myClass():
  def method1(self):
      print "Guru99"
        
      
class childClass(myClass):
  def method1(self):
        myClass.method1(self);
        print "childClass Method1" 
        
  def method2(self):
        print "childClass method2"     
         
def main():           
  # exercise the class methods
  c2 = childClass()
  c2.method1()
  c2.method2()

if __name__== "__main__":
  main()
