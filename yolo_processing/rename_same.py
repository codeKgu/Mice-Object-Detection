import os

if(len(sys.argv != 1))
    print("invalid number of arguements")
os.chdir(r'.')
#ext = sys.argv[0]
ext = "-001"
for f in os.listdir():
    file_name, file_ext = os.path.splittext(f)
    file_name = file_name + ext
    os.rename(f, file_name)
