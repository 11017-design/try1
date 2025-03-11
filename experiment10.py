file1=open('sample1.txt','r')
file2=open('sample2.txt','w')

for line in file1:
    file2.write(line)
file2.write("\nCompleted")
print("\nSuccessfully written in file2.\n")

file1.close()
file2.close()

file2 = open('sample2.txt','r')
print("Content of file2:")
print(file2.read())
file2.close()