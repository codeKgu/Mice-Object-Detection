import os
os.chdir(r'D:\Users\Research\Research-WeiZhou\data\pipe images\Training_images\Images')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_name[-3:] == 'jpg':
        os.rename(f, file_name[:-3] + '.jpg')
