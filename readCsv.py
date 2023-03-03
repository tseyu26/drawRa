import csv
import matplotlib.pyplot as plt


fileName = input("Input the name of the file: ")
print("The name of the csv file is: " + fileName )

print("Reading...")

strLength = []
strHeight = []

try:
    with open(fileName) as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            strLength.append(row[0])
            strHeight.append(row[1])
        print("The data has been accessed!")
except Exception:
    print(fileName+" is not found!\n"+"Check the name of the file!")

# Change the Strings into Floats
floatLength = [float(i) for i in strLength]
floatHeight = [float(i) for i in strHeight]


plt.figure(figsize=(20, 10), dpi=100)
plt.title("Height change",  fontsize=30)
plt.xlabel("Length/Micrometer", fontsize=20)
plt.ylabel("Height/Angstrom", fontsize=20)


plt.plot(floatLength,floatHeight)

savePath = "./" + fileName[:-4] +".jpg"
plt.savefig(savePath)

plt.show()
print("The figure has been saved!")
