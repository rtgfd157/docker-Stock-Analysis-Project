import time
import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

A = [1,2,3,4,5,6,7]
B = A[:len(A)//2]
C = A[len(A)//2:]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

if __name__ == "__main__":
    B, C = split_list(A)
    print("b ",B)
    print("C ",C)

  #asyncio.run(main())