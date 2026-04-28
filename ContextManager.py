class MyFileManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    
    def __enter__(self):
        print("Opening File...")
        self.file=open(self.filename,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc, tb):
        print("Closing File....")
        self.file.close()
        return False
    

with MyFileManager("context.txt","w") as f:
    f.write("Hello World!!!")
        