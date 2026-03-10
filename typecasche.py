a="15" #here int 15 I gave as str
b="15.5" #here float 15.5 I gave as str
a=int(a) #here str change into integer
b=float(b) #here str change into float
print(type(a)) #here type checking and output showing string into integer
print(type(b)) #here type checking and output showing string into float
print(float(a+b))
print(type(a+b))