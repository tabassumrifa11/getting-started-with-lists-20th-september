print('\033c')
def sq(l):
    square = []
    for i in l:
        square.append(i*i)
        
        
    return square

li = [4, 3, 6, 7, 5, 9, 8, 10, 2]
print(f"Original Lists  : {li}")
res = sq(li)

print(res)