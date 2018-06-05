import os


os.chdir(r'D:\Users\Research WeiZhe\Data\mice data\annotations\converted\converted_same_name')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    title, _ = file_name.split('.')
    os.rename(f, title + file_ext)
