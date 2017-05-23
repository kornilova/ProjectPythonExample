import os

file=open('C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\test1.txt')
content=file.read()
print(content)
file.close()

file1=open('C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\testLine.txt')
content=file1.readlines()
print(content)
file1.close()

file2=open('C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\testWrite.txt','w')
file2.write('hello3')
file2.close()
file2=open('C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\testWrite.txt')
content=file2.read()
file2.close()
print(content)
