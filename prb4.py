list = [5, 20, 15, 20, 25, 50, 20]

n = 20


print ("Given list:")
print (list)

i=0 
length = len(list) 
while(i<length):
	if(list[i]==n):
		list.remove (list[i])
			
		length = length -1  
		
		continue
	i = i+1


print ("\nNew list after removing 20:")
print (list)