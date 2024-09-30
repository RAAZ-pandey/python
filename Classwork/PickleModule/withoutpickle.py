#### wap to save a python list in into a file and read that same file and recover original list


list = [1,2,3,4,5]


filepath = "data.txt"

with open(filepath, "w") as fileHandle:
    fileHandle.write(str(list))

with open(filepath,"r") as fileHandle:
    readData = fileHandle.read()
    readData =readData[1:len(readData)-1].replace(" ","").split(",")
    print(f"read data is{readData}\n its type is {type(readData)}")