import os

os.chdir(r'D:/Users/Research/Research-WeiZhou/data/pipe_images/Training_images/labels_converted/')
# ext = sys.argv[0]
for f in os.listdir():
    file = open(r'D:/Users/Research/Research-WeiZhou/data/pipe_images/Training_images/labels_converted/{}'.format(f), 'r')
    liness = file.read()
    lines = liness.split('\n')
    # print(lines)
    if lines[1][0] == '1':
        lines[1] = '0{}'.format(lines[1][1:])
        lines = '\n'.join(lines)
        print(lines)
        file_write = open(r'D:/Users/Research/Research-WeiZhou/data/pipe_images/Training_images/labels_converted/{}'.format(f), 'w+')
        file_write.write(lines)
        file_write.close()
    file.close()
# file_name = file_name + ext
# os.rename(f, file_name)
