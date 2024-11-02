
import numpy as np
import galois
# Initialize GF(2) and a random matrix to serve as an example
M,N = 7, 4
GF2 = galois.GF(3)
x = GF2(1)
y = GF2(1)
print(x + y)