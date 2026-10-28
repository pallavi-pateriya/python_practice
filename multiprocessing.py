# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
import multiprocessing
import time

def output():
  for i in range(1,10):
    print("printing square and cubes")
    print("Process 1", i**2)
    print(i**3)

def square(n):
  for i in range(1,50):
    print("Process 2",i**2)    

def cube(n):
  for i in range(1,n):
    print("Process 3",i**3)
    



if __name__ == '__main__':
  p1= multiprocessing.Process(target=output)
  p3= multiprocessing.Process(target=square,args=(10,))
  p2= multiprocessing.Process(target=cube, args=(10,))


  p1.start()
  p2.start()
  p3.start()
  
  
  p1.join()
  p3.join()
  p2.join()
  

  print("completed succesfully")