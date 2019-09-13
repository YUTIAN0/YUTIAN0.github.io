# -*- coding: UTF-8 -*-

import time
import os

head="""---
layout: post                      
title:  " "
author: "YUTIAN0"           
date:  {}
excerpt:  " "  
categories:  []                
tags:  [ ] 
---            
""".format(time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime()))

f=os.listdir("./_posts")
name=time.strftime("%Y-%m-%d", time.localtime())+"-0%d.md" %(len(f)+1)

with open('./_posts/%s'%(name), 'x') as f:
     f.write(head)
f.close()


''''
---
layout: post                         ## 文章使用的模板
title:  ""          ## 文章的标题
author: ""                  ## 作者
date:       ## 发布时间
categories: []                   ## 文章所属的目录
tags: [ ]                 ##文章标签
mathjax:   ##文章中是否启用latex公式语法，建议打开
excerpt: ##摘要，和TOC一章的方法可以二选一，但是TOC中可以加入图片连接，因此建议使用第一种方法

---



f=os.listdir("./_posts")
for x in f:
    print(int(x.split(".")[0].split("-")[-1]))
'''


