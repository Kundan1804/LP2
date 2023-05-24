def isSafe(arr,x,y,n):
    for i in range(x):
        if arr[i][y]==1:
            return False
    row=x
    col=y
    while row>=0 and col>=0:
        if arr[row][col]==1:
            return False
        row-=1
        col-=1
    row=x
    col=y
    while row>=0 and col<n:
        if arr[row][col]==1:
            return False
        row-=1
        col+=1
    return True

def nQueens(arr,x,n):
    if x>=n:
        return True
    for col in range(n):
        if isSafe(arr,x,col,n):
            arr[x][col]=1
            if nQueens(arr,x+1,n):
                return True
            arr[x][col] = 0
    return False

if __name__=="__main__":
    n = int(input("Enter number of Queens : "))
    arr = [[0]*n for i in range(n)]

    if nQueens(arr,0,n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j],end=" ")
            print()