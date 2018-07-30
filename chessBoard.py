# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:01:30 2018

@author: wheat
"""

import tkinter as tk
import time
mark =0

#设置棋盘
def ChessBoardSet():
    number = int(entrySize.get())
    singlelength = 512//number
    for i in range(number):
        for j in range(number+1):
            cv.create_rectangle(10+j*singlelength,10+i*singlelength,10+singlelength,10+i*singlelength+singlelength)       
    cv.pack()
#设置特殊点    
def SpecialPointSet():
    number = int(entrySize.get())
    singlelength = 512//number
    prow = int(entryCd1.get())
    pcolumn = int(entryCd2.get())
    sprt = cv.create_rectangle(10+prow*singlelength,10+pcolumn*singlelength,10+singlelength+prow*singlelength,10+pcolumn*singlelength+singlelength)
    cv.itemconfig(sprt, fill="black")
    cv.pack()
    Arrange(0,0,prow,pcolumn,int(entrySize.get()))

def colorfill(prow,pcolumn,count):
    color = ['#FFB6C1','#A9A9A9','#DC143C','#FFF0F5','#800080',
             '#40E0D0','#4B0082','#F8F8FF','#0000FF','#D2B48C','#87CEEB',
             '#A52A2A','#40E0D0','#98FB98','#008000','#9ACD32',
             '#FFFFF0','#FFFF00','#FFD700','#F5DEB3','#FFEFD5',
             '#FF0000','#F5F5F5','#C0C0C0','#808080']
    select = int((count%10))
    #print(select,count)
    number = int(entrySize.get())
    singlelength = 512//number
    sprt = cv.create_rectangle(10+prow*singlelength,10+pcolumn*singlelength,10+singlelength+prow*singlelength,10+pcolumn*singlelength+singlelength)
    cv.itemconfig(sprt, fill=color[select])
    cv.pack()
    
#放入骨牌    
def Arrange(trow,tcolumn,prow,pcolumn,size):
    global mark
    mark +=1  
    count = mark 
    if size == 1: 
        return  
    half = size//2  
    ''' '''
    if prow<trow+half and pcolumn<tcolumn+half:
        Arrange(trow,tcolumn,prow,pcolumn,half) 
        #time.sleep(2)
    else:  
        #table[trow+half-1][tcolumn+half-1]=count 
        Arrange(trow,tcolumn,trow+half-1,tcolumn+half-1,half)  
        colorfill(trow+half-1,tcolumn+half-1,count)
    ''' '''
    if prow<trow+half and pcolumn>=tcolumn+half:  
        Arrange(trow,tcolumn+half,prow,pcolumn,half)  
    else:  
        #table[trow+half-1][tcolumn+half]=count 
        Arrange(trow,tcolumn+half,trow+half-1,tcolumn+half,half)  
        colorfill(trow+half-1,tcolumn+half,count)
    ''' '''
    if prow>=trow+half and pcolumn<tcolumn+half:  
        Arrange(trow+half,tcolumn,prow,pcolumn,half)  
    else:  
        #table[trow+half][tcolumn+half-1]=count  
        Arrange(trow+half,tcolumn,trow+half,tcolumn+half-1,half) 
        colorfill(trow+half,tcolumn+half-1,count)
    ''' '''
    if prow>=trow+half and pcolumn>=tcolumn+half:  
        Arrange(trow+half,tcolumn+half,prow,pcolumn,half)  
    else:  
        #table[trow+half][tcolumn+half] = count  
        Arrange(trow+half,tcolumn+half,trow+half,tcolumn+half,half)  
        colorfill(trow+half,tcolumn+half,count)  

window = tk.Tk()
window.title('Chess')
cv = tk.Canvas(window,bg = 'white',width = 522, height = 522)
#创建frame的框架，窗口window为这个框架的父容器
frame = tk.Frame(window)
frame.pack()

#控件设置
BoardSet = tk.Button(frame,text = 'SetBoard', command = ChessBoardSet)
Set = tk.Button(frame,text = 'Start', command = SpecialPointSet)
entrySize = tk.Entry(frame)
entryCd1 = tk.Entry(frame)
entryCd2 = tk.Entry(frame)

#控件布局
entrySize.grid(row = 500,column = 50)
BoardSet.grid(row = 500,column = 60)
entryCd1.grid(row = 500,column = 100)
entryCd2.grid(row = 500,column = 150)
Set.grid(row = 500,column = 200)
window.mainloop()


  





















