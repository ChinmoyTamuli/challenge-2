arr=[1,21,3,14,5,60,7,6]
value=27

for i,x in enumerate(arr[:-1]):
    val=value-x
    if val in arr[i+1:]:
        print("required value {} and {}:".format(x,val))
        break



