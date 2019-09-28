#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : clean_bookmark_test.py
@time : 2019/09/28 16:31:50
@func : 
"""
#!/usr/bin/python

# -*- coding: UTF-8 -*-

list1=[] # 最终列表

b=None

with open(r"D:\test\test001\bookmark.html",'r',encoding='utf-8') as fh:
    for line in fh:
        print(line.strip())
        # print(type(line))
        # print(line.split())
        f=line.strip()
        a=f.split('>')
        if len(a) <3: # 切片后长度小于3就是普通标签直接添加，否则就是收藏夹要去重复
            list1.append(f)

        elif a[-2] != b:
            list1.append(f)
            b = a[-2]

            # print(b)



with open(r"D:\test\test001\new_html.html",'w',encoding='utf-8') as f:
    for i in list1:
        f.write(i)
        f.write('\n')