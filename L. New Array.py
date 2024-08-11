def new_array(array1,array2):
    result=array2+array1
    return result    

n=int(input())
array1=list(map(int,input().split()))
array2=list(map(int,input().split()))
x=new_array(array1,array2)
print(' '.join(map(str,x)))