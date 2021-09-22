array= [-7,-5,-3,-1,3,6,9]
sorted_array = [sorted_array for sorted_array in range(len(array))] #create array using list comprehension 
i = 0;
k = len(array)-1
j = len(array)-1
while(i<=j):
    if (abs(array[i]) > abs(array[j])):
        sorted_array[k] = array[i]
        i+=1
    else:
        sorted_array[k] = array[j]
        j-=1
    k-=1
print(sorted_array)
