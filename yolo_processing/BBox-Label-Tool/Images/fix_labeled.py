import os

os.chdir(r'D:\Users\Research\Research-WeiZhou\darknet\build\darknet\x64\data\obj')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.txt':
        print(f)
        file = open(r'D:/Users/Research/Research-WeiZhou/darknet/build/darknet/x64/data/obj/{}'.format(f), 'r')
        liness = file.read()
        lines = liness.split('\n')
        print(liness)
        if lines[1][0] == '1':
            lines[1] = '0{}'.format(lines[1][1:])
            lines = '\n'.join(lines)
            file_write = open(r'D:/Users/Research/Research-WeiZhou/darknet/build/darknet/x64/data/obj/{}'.format(f), 'w+')
            file_write.write(lines)
            file_write.close()
        file.close()
        print(lines)
