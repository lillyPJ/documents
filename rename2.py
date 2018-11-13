# _*_coding:utf-8_*_
import sys
import os

def cur_file_dir():
    # 获取当前文件路径
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def rename(path):
    # print("当前目录:",path)
    file_list = os.listdir(path)
    # print(file_list)  
    for file in file_list:
        # print(file)         
        old_dir = os.path.join(path,file)          
        filename = os.path.splitext(file)[0]
        # print(filename)
        filetype = os.path.splitext(file)[1]
        # print(filetype)
        old_name = filename + filetype
        print("old name is:", old_name)
        new_filename = filename.replace(" ", "_")    # 这里替换的是重点
        new_name = new_filename.replace(" ", "_")     # 如果无法一次替换成功，可以进行多次替换
        print("new name is:", new_name)
        new_dir = os.path.join(path, new_name + filetype)  # 新的文件路径
        os.rename(old_dir, new_dir)                 # 重命名
        # print("DONE")     
        if os.path.isdir(new_dir):
            rename(new_dir)                     # 注意这里是重点，这里使用了递归

if __name__ == "__main__": 
    rename("./papers/")
    print("ALL DONE!!!")

