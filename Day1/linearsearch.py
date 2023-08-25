def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        
    return -1


arr = [20,45,47,55,67,75,88,90]
print("this is your index no", linearSearch(arr,55))
#time complexity 0(n)
#space complexity constant