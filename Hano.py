# -*- coding: utf-8 -*-
i=1
def move(n,fr,to):
    global i
    print 'no.',i,':move',n,'disk,from',fr,'--->',to
    i+=1
def hanno(n,init,tmp,dest):
    if n==1:move(1,init,dest)
    else:
        hanno(n-1,init,dest,tmp)        #把前n-1个盘子从初始塔放到中转塔
        move(n,init,dest)               #把最下方的盘子从初始塔放到目标塔
        hanno(n-1,tmp,init,dest)        #把前n-1个盘子从中转塔放到目标塔
hanno(3,'left','mid','right')