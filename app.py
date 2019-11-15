import os
path = '/opt/code'
code= raw_input("Hello Tass choose your code:")

if code=="CPP":
 path_cpp = '/opt/code/CPP'
 if not os.path.exists(path_cpp):
     os.mkdir(path)
     os.mkdir(path_cpp)
     f = open("/opt/code/CPP/runme.cpp", "a")
     f.write(" Please enter your CPP code. ")
     f.close()
     print("Directory " , path_cpp ,  " Created ")
 else:
     print("Directory " , path_cpp ,  " already exists")

elif code =="GO":
 path_go = '/opt/code/GO'
 if not os.path.exists(path_go):
     os.mkdir(path)
     os.mkdir(path_go)
     f = open("/opt/code/GO/runme.go", "a")
     f.write("Please enter your GO code.")
     f.close()
     print("Directory " , path_go ,  " Created ")
 else:
     print("Directory " , path_go ,  " already exists")
else:
     print("Please choose either CPP or GO")
