a =[0,1,2,3,4,5,6,7,8,9]
b =(0,1,2,3,4,5,6,7,8,9)
c ='0123456789'

# slice(start, stop, step)
x = slice(0,5)

print(x)

print(a[x])

print(a[0:5]) #this a short notation for doing slice
#a[start:end] this item start through end-1
#a[start:] this item start through the rest of the array
#a[:] a copy of the whole array
#a[start:end:step] start through not past end, by step

print(b[0:5])
print(c[0:5])

print(a[0::2])

#  P Y T H O N
#  0 1 2 3 4 5 -- positive index
# -6-5-4-3-2-1 -- negative index

a[::-1] #give everything in reverse order


