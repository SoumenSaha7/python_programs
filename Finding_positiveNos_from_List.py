n = int(input("Enter the no. elements to be included in the list: "))
lst = list()
for i in range(n):
    lst.append(int(input()))  # input for list elements
new_lst = list()
for i in range(n):
    if lst[i] > 0:
        new_lst.append(lst[i])  # adding +ve nos. to the new_list
print("Output:")
print(*new_lst, sep=", ", end="")  # printing the +ve nos. separated by " ,"



"""
# OUTPUT
    #1
    Enter the no. elements to be included in the list: 5
    12
    -7
    5
    64
    -14
    Output:
    12, 5, 64
    
    #2
    Enter the no. elements to be included in the list: 4
    12
    14
    -95
    3
    Output:
    12, 14, 3
"""
