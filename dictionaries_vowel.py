var1 = input("enter a statement : ")
print(var1)

var2 = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}

for i in var1:
    if i in var2:
        var2[i] += 1

print(var2)        
