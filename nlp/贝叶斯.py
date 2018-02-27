import inspect

import sklearn

# https://www.cnblogs.com/pinard/p/6074222.html https://www.cnblogs.com/Scorpio989/p/4760281.html

import jieba

a = jieba.cut('你好吗')
#a.__next__()
for i in a:
    print(i)
#print(a.__next__())
print(jieba.cut.__defaults__())
jieba.cut.__doc__