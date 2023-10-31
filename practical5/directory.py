import os

#getting cwd
print("String format= ",os.getcwd())
print("Byte format= ",os.getcwdb())

#create directory
os.mkdir("C:/study/TY/5thsem/python/p5/demo")


#list contents of directory
print("Files in current dir= ",os.listdir())

#rename dir
#listing files of cwd
os.rename('demo','new_demo')
print("Files in current dir after reanme= ",os.listdir(os.getcwd()))

#checking empty dir
dir_list=os.listdir()
if len(dir_list)==0:
    print("Empty directory")
else:
    print("Directory has contents: ",dir_list)


#os.rmdir("C:/study/TY/5thsem/python/p5/new_demo")
#print("Directory has contents: ",dir_list)