from __future__ import division,print_function
from numpy import zeros, array, log

a = zeros([2, 3], float);
print(a)

b = array ([[1, 2, 3], [4, 5, 6]], int);
print(b[1,2]);

print(b + b);
print(b - b);
print(b*b);
print(log(b))
