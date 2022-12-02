a = []

x = int(input("Enter number of elements: "))

for i in range(0, x):
    list1 = int(input())
    a.append(list1)
print ("List: " + str(a))  


print("Reverse list:", a[::-1])