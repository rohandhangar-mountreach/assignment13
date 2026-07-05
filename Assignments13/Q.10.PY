# Q10
import numpy as np

try:
    n = int(input("Enter number of values: "))
    a = np.random.randint(10,101,n)

    print("Array:", a)
    print("Mean:", np.mean(a))
    print("Median:", np.median(a))
    print("Std:", np.std(a))
    print("Min:", np.min(a))
    print("Max:", np.max(a))

    if n % 2 == 0:
        b = a.reshape(2, n//2)
        print("2D Array:\n", b)
        print("Row-wise Sum:", b.sum(axis=1))
    else:
        print("Cannot reshape into 2D equally.")

except ValueError:
    print("Invalid Input")