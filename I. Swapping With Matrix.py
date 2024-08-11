def swap_row_column(a,b,c,matrix):
    a-=1  #Convert X and Y from 1-based to 0-based indexing
    b-=1

    matrix[a], matrix[b] = matrix[b], matrix[a]    # Swap rows a and b

    for row in matrix:
        row[a], row[b] = row[b], row[a]      #Swap columns a and b in each row
    
    for row in matrix:
        print(' '.join(map(str, row)))



import sys 
input=sys.stdin.read  #"4 3 1\n1 2 3 -5\n-5 4 0 3\n7 7 1 2\n40 6 5 11\n"
n=input().split()     #["4", "3", "1", "1", "2", "3", "-5", "-5", "4", "0", "3", "7", "7", "1", "2", "40", "6", "5", "11"]
'''
4 3 1
1 2 3 -5
-5 4 0 3
7 7 1 2
40 6 5 11

'''

a=int(n[0])   #a = int(data[0]) converts "4" to 4  
b=int(n[1])   #b = int(data[1]) converts "3" to 3
c=int(n[2])   #c = int(data[2]) converts "1" to 1

matrix=[]
index=3
for i in range(a):
    row=list(map(int,n[index:index+a]))  #n[index:index + a] → n[3:7] → ["1", "2", "3", "-5"]
    matrix.append(row)
    index+=a    #Update index → index = 7

swap_row_column(n, a, b, matrix)