import numpy as np

arr = np.array([10,20,30,40,50,60,70,80])

#slicing
print("First 4 elements are ",arr[:4]) 
print("Elements from index 2 to 6",arr[2:7])

#Integer Indexing
print("Element at index 4 is ",arr[4])

#Boolean Indexing
print("Elements greater than 30",arr[arr>30])
