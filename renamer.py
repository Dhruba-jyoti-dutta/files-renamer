import os
folder="F:/python/not so imp/renamer/renamer data/"
os.chdir(folder)
# files=[]
# for file in sorted(os.listdir(folder), key=os.path.getctime):
#     files.append(file)
# print(files)
# above line will be same as os.chdir("F:/python/not so imp/renamer/renamer data/")
# i=0
# for file in files:
#     # file.sort(key=os.path.getctime)
#     # print(file)
#     os.rename(file,f"{i}.png")
#     i=i+1


def rename():
    os.chdir(folder)
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