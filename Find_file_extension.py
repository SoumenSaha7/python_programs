# To find the file extension of a given filename


def extension(str2):  # in case the file type is not known, extension will be returned through this function
    for i in range(0, len(str2)):
        if "." == str2[i]:
            i = i + 1  # i gets the index of the letter after "."
            break
    new_str = str2[i:]  # gets the substring after "."
    return new_str


filename = input("Input the Filename: ")
str1 = "The extension of the file is : "
if ".py" in filename:
    print(str1 + "'python'")
elif ".txt" in filename:
    print(str1 + "'text file'")
elif ".c" in filename:
    print(str1 + "'C'")
elif ".jar" in filename:
    print(str1 + "'java'")
elif ".cpp" in filename:
    print(str1 + "'C++'")
elif ".apk" in filename:
    print(str1 + "'Android App'")
elif ".jpeg" in filename:
    print(str1 + "'image'")
elif ".mp3" in filename:
    print(str1 + "'music'")
elif ".mp4" in filename:
    print(str1 + "'video'")
else:
    print(str1 + "'" + extension(filename) + "'")   # since the format given in app includes single quote('')


"""
OUTPUT :
    # 1
    Input the Filename: abc.py
    The extension of the file is : 'python'

    # 2
    Input the Filename: pqr.exe
    The extension of the file is : 'exe'
"""
