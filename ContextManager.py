# class MyFileManager:
#     def __init__(self,filename,mode):
#         self.filename=filename
#         self.mode=mode
#         self.file=None
    
#     def __enter__(self):
#         print("Opening File...")
#         self.file=open(self.filename,self.mode)
#         return self.file
    
#     def __exit__(self, exc_type, exc, tb):
#         print("Closing File....")
#         self.file.close()
#         return False
    

# with MyFileManager("context.txt","w") as f:
#     f.write("Hello World!!!")

# with open("test.txt","r") as f:
#     content= f.read()
#     print(content)

class MyFileManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    
    def __enter__(self):
        print("Opening the File")
        self.file=open(self.filename,self.mode)
        return self.file
    #exc_type->type of exception, exc_val->Exception text,exc_tb->Traceback info,If no error then it is none
    def __exit__(self, exc_type, exc, tb):
        print("Closing File")
        self.file.close()
        return False
    
with MyFileManager("test.txt","r") as f:
    content=f.read()
    print(content)

        