a = []

x = int(input("Enter number of elements for first list: "))

for i in range(0, x):
    list1 = int(input())
    a.append(list1)
print ("List 1 : " + str(a))   
  
b = []

y = int(input("Enter number of elements for second list: "))


for j in range(0, y):
    list2 = int(input())
    b.append(list2)   
print ("List 2 : " + str(b))

output_list = []
for k in range(0, len(a)):
    output_list.append(a[k] + b[k])
   
print ("\nOutput : " + str(output_list))


   