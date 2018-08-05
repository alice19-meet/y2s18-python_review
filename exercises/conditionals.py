# Write your solution for 1.2 here!b=0
b=0
for i in range (101):
    if i%2==0:
        b=b+i
print (b)
i=0
while i<1000:
    if i%6==2 and i**3%5==3:
        print(i)
    i=i+1