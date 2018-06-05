import os
import sys
os.chdir(r'D:\Users\Research\Research-WeiZhou\data\side view images\MouseA14_20140914_20-10-55_Front_J85')
#ext = sys.argv[0]
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.JPEG':
        ext = '.jpg'
        fname = file_name + ext
        #fk = file_name.split('-')
        print(fname)
        os.rename(f, fname)
