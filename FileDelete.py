import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
        
    else:
        print("There no such file")
        return

def main():
    print("Enter the file name to Delete")
    Name = input()

    DeleteFile(Name)

if __name__ =="__main__":
    main()