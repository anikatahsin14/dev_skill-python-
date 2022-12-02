
a = []

x = int(input("Enter number of elements: "))

for i in range(0, x):
    list1 = int(input())
    a.append(list1)
print ("List: " + str(a)) 

position = int(input("Enter index no:"))
key = int(input("Enter key value:"))



a.insert(position,key)
print("\nUpdated list is: ",a)