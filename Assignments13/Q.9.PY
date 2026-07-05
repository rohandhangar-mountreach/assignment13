# Q9
import numpy as np

a = np.random.randint(1,51,20)
b = a.reshape(4,5)

print(b)
print("Sum:", b.sum())
print("Mean:", b.mean())
print("Std:", b.std())
print("Row Max:", b.max(axis=1))