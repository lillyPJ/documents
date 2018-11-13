import glob
import os

def GetFileNameList(file_folder, ext_list = ['*.jpg']):
    file_name_list = []
    for ext in ext_list:
        file_name_list.extend(glob.glob(os.path.join(file_folder, '*'.format(ext))))
    file_name_list = sorted(file_name_list)
    return file_name_list


file_dir = "/home/linli1/documents_github/documents/papers/"

file_list = GetFileNameList(file_dir, "*.md")

print(file_list)

for each_file in file_list:
    ori_file_name = os.path.basename(each_file)
    ori_file_split = ori_file_name.split(' ')
    new_file_name = "_".join(ori_file_split)
    print(ori_file_name, new_file_name)
    ori_file_path = os.path.join(file_dir, ori_file_name)
    new_file_path = os.path.join(file_dir, new_file_name)
    print(ori_file_path, new_file_path)
    print(os.path.exists(ori_file_path))
    os.rename(ori_file_path, new_file_path)
