from threading import Thread

def learning(input):
  for i in range(20):
    print(f"learning {input}")


def practice(n):
  for i in range(n):
    print("hello")

def func(m):
  for i in range(m):
    print("Hi monika")

def stud(n):
  for i in range(1,n):
    print(i**2)

t1=Thread(target=learning, args=('python',))
t2=Thread(target=practice, args=(50,))
t3=Thread(target=func, args=(20,))
t4=Thread(target=stud, args=(40,))

t4.start()
t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
t4.join()


print("all executed succesfully")




# #asyncio


import asyncio


async def download(file):
    print(f"downloading {file}")
    await asyncio.sleep(2)
    print(f"downloaded {file}")

async def main():
      await asyncio.gather(
            download("file1"),
            download("file2"),
            download("file3")
        )
asyncio.run(main())    
