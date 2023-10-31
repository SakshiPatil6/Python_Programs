File=open('Saksha.txt','w+')
print("Name of file= ",File.name)
print("Opening mode of file= ",File.mode)
File.write( "My name is sakshi patil\n")
File.close()

File=open('Saksha.txt','r')
for i in File:
    print("Contents= ",i)
File.close()

#opening file in append mode
f=open('Saksha.txt','a')
f.write("I m from TY CSE")
f.close()

f=open('Saksha.txt','r')
print("Contents= ",f.read())
f.close()
