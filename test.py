print("hello")

import numpy as np

a = np.array([1,2])

print(a)

print("ver2")

print("use git clone for working with another computer")

print("2nd computer(directory)  add something  to   test git pull")

import asyncio
import time

async def add(a, b):
    print("1과 2의 덧셈을 계산하고 결과를 반환하는 함수입니다")
    await asyncio.sleep(10)
    return a+b

async def print_add(a, b):
    result = await add(a, b)    
    print('print_add: {0} + {1} = {2}'.format(a, b, result))

now = time.time()
loop = asyncio.get_event_loop()           
loop.run_until_complete(print_add(1, 2))    
loop.close()   
end = time.time()
print(f"시작은 {now}이고 끝은 {end}입니다")