import os
folder="D:/sharex/Screenshots/2023-03/"
os.chdir(folder)



def rename():
    os.chdir(folder)

    #files gita sort kore
    files=[]
    for file in sorted(os.listdir(folder), key=os.path.getctime):
        files.append(file)
    
    i=0
    for file in files:
        # file.sort(key=os.path.getctime)
        # print(file)
        os.rename(file,f"{i}.png")
        i=i+1
print("process started")
rename()
print("process completed")