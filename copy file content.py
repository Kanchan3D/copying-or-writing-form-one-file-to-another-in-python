OldFile="file.txt"
NewFile="new.txt"
def copyFile(OldFile,NewFile):
    f1=open(OldFile,"r")
    f2=open(NewFile,"w")
    while True:
        text=f1.read(50)
        if text=="":
            break
        f2.write(text)
        f1.close()
        f2.close()