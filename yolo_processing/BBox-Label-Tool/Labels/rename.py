import os
import sys

ext = 'A12'
os.chdir(r'D:\Users\Research\Research-WeiZhou\darknet\build\darknet\x64\data')
#ext = sys.argv[0]
train = open('train.txt', 'r')
test = open('test.txt', 'r')

train_text = train.read().split('\n')
test_text = test.read().split('\n')
print(train_text)
print(len(test_text))
#file_name = file_name + "-" + ext + file_ext
# print(file_name)
#os.rename(f, file_name)
