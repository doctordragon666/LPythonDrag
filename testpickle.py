# -*- coding:utf-8 -*-
# 时间：
# 功能：
# 目的：
# 需求分析：
#
import pickle
import json

dic = {'this': "data", 'that': "algorithm"}
with open('file.pickle', 'wb') as f:
    pickle.dump(dic, f)
with open('file.pickle', 'rb') as f:
    dic_read = pickle.load(f)
    print(dic_read)

result = json.dumps(dic)
print(result)

# 运行结果
