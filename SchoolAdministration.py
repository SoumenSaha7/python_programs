# A python program creating a information database for the students of a school.
# Information are: Roll_num, Name, email_ID, Grades, Address.
# with Roll_num as key and the other values as another dictionary.
# The program perform these operations with CHOICES as INPUT ***
# 1) Access email_ID of a particular roll
# 2) Sort the students according to Roll_Number
# 3) Sort the students according to Name
# 4) Insert a new student
# 5) Remove a student who has left the school.


num = int(input("Please, enter the total no. of students: "))
class1 = {}
stud_details = ["Name:", "Email id:", "Grade:", "Address:"]
for i in range(num):
    roll = input("Roll: ")
    class1[roll] = {}  # creates a nested dictionary.
    for entry in stud_details:
        class1[roll][entry] = input("Please, enter the " + entry + "- ")
        # stores the input as values of nested dictionary.
print(class1)
strg = "1) Access email_ID of a particular roll\n2) Sort the students according to Roll_Number\n3) Sort the students according to Name\n4) Insert a new student\n5) Remove a student who has left the school."
print(strg)
n = int(input("Enter choice: "))
if n == 1:
    rollno = input("Enter the roll no: ")
    for i in class1.keys():
        if i == rollno:
            print("Email id: " + class1[i]["Email id:"])
        else:
            print("Roll no " + rollno + " is not found.")
elif n == 2:
    print("Sorted according to Roll number: ")
    for i in sorted(class1.keys()):
        print(i, " ", class1[i])
elif n == 3:
    print("Sorted according to Name: ")
    result = sorted(class1.items(), key=lambda x: x[1]["Name:"])
    # names are sorted using sorted() and stored in a list containing sets and dictionary in it.
    print(result)
elif n == 4:
    rollno = input("Roll no: ")
    class1[rollno] = {}
    for entry in stud_details:
        class1[rollno][entry] = input("Please, enter the " + entry + "- ")
    print(class1)  # prints the dictionary without any user-defined format
elif n == 5:
    rollno = input("Roll no: ")
    del class1[rollno]  # deletes the item from the dictionary
    print(class1)
else:
    print("INVALID CHOICE!!!")


"""
#OUTPUT: 

Please, enter the total no. of students: 3
Roll: 101
Please, enter the Name:- Akash
Please, enter the Email id:- akash@gmail
Please, enter the Grade:- 92
Please, enter the Address:- Kolkata
Roll: 102
Please, enter the Name:- Simran
Please, enter the Email id:- sim@gmail.com
Please, enter the Grade:- 90
Please, enter the Address:- Delhi South
Roll: 103
Please, enter the Name:- Binny
Please, enter the Email id:- bin@gmail.com
Please, enter the Grade:- 100
Please, enter the Address:- Mumbai
{'101': {'Name:': 'Akash', 'Email id:': 'akash@gmail', 'Grade:': '92', 'Address:': 'Kolkata'}, '102': {'Name:': 'Simran', 'Email id:': 'sim@gmail.com', 'Grade:': '90', 'Address:': 'Delhi South'}, '103': {'Name:': 'Binny', 'Email id:': 'bin@gmail.com', 'Grade:': '100', 'Address:': 'Mumbai'}}
1) Access email_ID of a particular roll
2) Sort the students according to Roll_Number
3) Sort the students according to Name
4) Insert a new student
5) Remove a student who has left the school.
Enter choice: 3
Sorted according to Name: 
[('101', {'Name:': 'Akash', 'Email id:': 'akash@gmail', 'Grade:': '92', 'Address:': 'Kolkata'}), ('103', {'Name:': 'Binny', 'Email id:': 'bin@gmail.com', 'Grade:': '100', 'Address:': 'Mumbai'}), ('102', {'Name:': 'Simran', 'Email id:': 'sim@gmail.com', 'Grade:': '90', 'Address:': 'Delhi South'})]

"""
