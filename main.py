# python3
# author: Aloneme

import os

# path = os.getcwd()
# print(os.listdir(path))
# path = input("file path >>: ")
path = r'C:\Users\94533\Desktop\文档\Note\Linux服务器开发 - 副本'
md_list = os.listdir(path) # 获取目录下的md文件
for i in range(len(md_list)-1):
    for j in range(len(md_list)-i-1):
        if int(md_list[j].split('.')[0]) > int(md_list[j+1].split('.')[0]):
            md_list[j], md_list[j+1] = md_list[j+1], md_list[j]
print(md_list)

# 合并文件
contents = []
for md in md_list:
    # if md != 'cpmd.py':
    mdfile = str(path) + '\\' + md
    # print(mdfile)
    with open(mdfile, 'r', encoding='utf-8') as f:
        contents.append(f.read() + "\n")
        # print(contents)
# result = input("file save name >>: ")
print(contents)
with open('第六卷.md', "w", encoding='utf-8') as f:
    f.writelines(contents)
print("task done!")
