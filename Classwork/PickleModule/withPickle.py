import pickle


list = [1,2,3,4,5]


filepath = "data.txt"

with open(filepath, "w") as fileHandle:
    fileHandle.write(str(list))

with open(filepath,"r") as fileHandle:
    readData = fileHandle.read()
    readData =readData[1:len(readData)-1].replace(" ","").split(",")
    print(f"read data is{readData}\n its type is {type(readData)}")

with open("readData.pickle","wb")as file:
    pickle.dump(readData,  file)

print("Data has been serialized and saved to  readData.pickle")

with open("readData.pickle", "rb") as file:
    loaded_data = pickle.load(file)

print("Deserialized data : ", loaded_data)