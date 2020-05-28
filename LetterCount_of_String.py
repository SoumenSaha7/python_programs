

def most_frequent(str1):
    lst1 = list(set(str1))  # Discrete characters of the string are stored in a list
    lst2 = [0 for i in range(len(str1))]
    dict1 = dict(zip(lst1, lst2))  # Two lists are merged in a dictionary using zip()
    for i in str1:
        dict1[i] += 1  # Taking the count of each character
    lst3 = sorted(dict1, key=dict1.get, reverse=True)
    # The dictionary values are sorted in descending order and stored in a list using in-built function
    for i in lst3:
        print(i + " = " + str(dict1[i]))


str1 = input("Please, enter a string: ").lower()
most_frequent(str1)  # call of function: most_frequent()


"""
OUTPUT:
    #1
    Please, enter a string: Mississippi
    s = 4
    i = 4
    p = 2
    m = 1
    
    #2
    Please, enter a string: Assassination
    s = 4
    a = 3
    i = 2
    n = 2
    o = 1
    t = 1
"""
