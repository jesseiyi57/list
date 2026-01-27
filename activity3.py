L = [6,7,5,8,9,5,7]
print("original list", L)

count = 0

for i in L:
    count += i
avg = count/len(L)
print("sum is equal to", L)
print(avg)
L.sort()
print("smallest element is:", L[0])
print("largest element is:", L[-1])