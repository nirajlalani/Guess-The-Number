# Guess-The-Number
The easiest guess the number game

```
arrx = [0,"B","D","C","B"]
arry = [0,"B","A","C","D","B"]
arr_num = [[0]*6]*5
arr_arrow = [[0]*6]*5



for i in range(5):
    for j in range(6):
        if i==0 or j==0:
            print("here1")
            arr_num[i][j] = 0
        elif arrx[i] == arry[j]:
            arr_num[i][j] = arr_num[i-1][j-1] +1
            arr_arrow[i][j] = "D"
        else:
            arr_num[i][j] == max((arr_num[i-1][j]),(arr_num[i][j-1]))
            if arr_num[i][j] == arr_num[j-1][j]:
                arr_arrow[i][j] = "L"
            if arr_num[i][j] == arr_num[i-1][j]:
                arr_arrow[i][j] = "U"


print(arr_num)


LCS = ""
i=4
j=5
while True:
    if arr_arrow[i][j] == "D":
        LCS += arrx[i]
        i -= 1
        j -= 1
    elif arr_arrow[i][j] == "L":
        j -= 1
    elif arr_arrow[i][j] == "U":
        i -= 1
    else:
        break


print(LCS)
```
