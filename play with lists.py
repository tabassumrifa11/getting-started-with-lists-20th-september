print('\033c')
l = [4, 5, 1 , 2, 9, 7, 10, 8]
print("Original Lists :", l)

count = 0

for i in l:
    count = count + i
    
avg = count/len(l)

print("sum = ", count) 
print("average = ", avg) 

l.sort()
print(l)

print("Smallest element is:", l[0])
print("Largest element is:", l[-1])