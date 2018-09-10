class Singleton:
<<<<<<< HEAD
   __instance = None
   @staticmethod
=======
   __instance = None       #1st design pattern program
   @staticmethod 
>>>>>>> 16b1c4b1f39524bc1ec9ef8ca8a063c7b0cecfb9
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
s = Singleton()
print s

s = Singleton.getInstance()
print s

s = Singleton.getInstance()
print s
