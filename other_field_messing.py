
import galois
import time 

t_start = time.time()
GF2 = galois.GF(2)
t_end = time.time() 

print(t_end - t_start)

t_start = time.time()
x = 1
y = 1
z = 1
for _ in range(10000):
  z = x + y
  z %= 2
t_end = time.time() 
print(t_end - t_start)