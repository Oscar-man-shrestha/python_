#list
lis=["Apple","Orange",5,345.00,False,"Akash","Rohan"]
print(lis[0])
print(lis[1:4]) 
lis.reverse()
lis.pop(3)
lis.insert(1,"banana")

print(lis)

#tuple
a=("oscar","rohan",1,2,3)
# a[0]=1 #cant change
ok=a.count("oscar")
ok=a.index(2)
print(ok)