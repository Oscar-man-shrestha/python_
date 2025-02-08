name="oscar"
# new_name=name[3]
# print(f"new name {new_name}")


# nameshort=len(name)
# print(nameshort)

nameshort=name[:5]  #is samas [0:5]
print(nameshort)
nameshort=name[1:]  #is samas [1:5]
print(nameshort)
nameshort=name[1:5]  #is samas [1:]
print(nameshort)

a="0123456789"
new_short=a[1:9:4]
print(new_short)

#function of strings

name="oscar man"
new_name=len(name)
print(new_name)

print(name.endswith("ar"))

print(name.startswith("os"))

print(name.capitalize()) #pahilo character lai capital garxa