def DP_MED(str1, str2, m,n):
    #making a table
    list1 = [[0 for x in range(n+1)] for x in range(m+1)] #columns X rows

    for i in range(m+1):
        for j in range(n+1):

            if i==0:
                list1[i][j] = j

            elif j==0:
                list1[i][j] = i

            
            elif str1[i-1] == str2[j-1]: #if last character are same
                list1[i][j] = list1[i-1][j-1]

            else: #take into consideration all possible moves
                list1[i][j] = 1 + min(list1[i][j-1], list1[i-1][j], list1[i-1][j-1])
                    #as it was our formula of 1+min(a,b,c)

    return list1[m][n]

str1 = "sunday"
str2 = "saturday"
#last three remain same, t is inserted, a is added, n is deleted
print(DP_MED(str1, str2, len(str1), len(str2)))
 
