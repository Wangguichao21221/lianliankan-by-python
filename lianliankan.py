# coding=GBK
import sys
import os
from time import time
import pygame
import random
import time
import tkinter as tk
from tkinter import messagebox
from pygame.locals import *
difficulties=[[4,4,2],[10,8,4],[18,12,8]]
import tkinter as tk
sidewidth=60
imgs=[]
for i in range(27):
    img=f"./res/{i}.png"
    imgs.append(pygame.transform.scale(pygame.image.load(img),(sidewidth,sidewidth)))
pygame.mixer.init()
sound=pygame.mixer.Sound("./BinggoSound.mp3")
def drawGrid(num):
    global xNum,yNum,sidewidth,imgs
    blocks=[]
    res=formnumers(num)
    for x in range(xNum):
        if x>=1 and x<xNum-1:
            blockx=[]
            for y in range(yNum):
                if y>=1 and y<yNum-1:
                    block=[res.pop(),x,y]
                    blockx.append(block)
                else:
                    block=[0,x,y]
                    blockx.append(block)
            blocks.append(blockx)
        else:
            blockx=[]
            for y in range(yNum):
                block=[0,x,y]
                blockx.append(block)
                
            blocks.append(blockx)
    return blocks
def drawline(window,rect:list):
    pygame.draw.rect(window,(100,100,255),(rect[0]*sidewidth-5,rect[1]*sidewidth-5,sidewidth+10,sidewidth+10),5)
def main(dif):
    global blocks,turns,xnum,ynum,numofsame,xNum,yNum,bg_color,colors
    xnum=difficulties[dif][0]
    ynum=difficulties[dif][1]
    numofsame=difficulties[dif][2]
    xNum=xnum+2 
    yNum=ynum+2 
    width=xnum*sidewidth
    height=ynum*sidewidth
    widthW=width+2*sidewidth
    heightW=height+2*sidewidth
    bg_color = (200,200,255)
    colors=[(200,200,255),
        (0,255,0),
        (255,0,0),
        (0,0,255),
        (100,200,0)]
    start=time.time()
    linecolor=(100,50,255)
    pygame.init()
    window=pygame.display.set_mode((widthW,heightW))
    pygame.display.set_caption("Lianliankan")
    clock=pygame.time.Clock()
    blocks=drawGrid(numofsame)
    start=[]
    end=[]
    turns=[]
    showingturns=[]
    imgtick=0
    ifshow=False
    showstart=[]
    showend=[]
    scores=0
    stime=time.time()
    while True:
        if scores==xnum*ynum:
            etime=time.time()
            timetaken=round((etime-stime),1)
            message_box("获胜!",f"总用时 : {timetaken}秒")
            pygame.quit()
            break
        clock.tick(60)
        window.fill((200,200,255))
        for blockx in blocks:
            for block in blockx:
                if block[0] >0:
                    window.blit(imgs[block[0]-1],(block[1]*sidewidth,block[2]*sidewidth))
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scores=0
                    blocks=drawGrid(numofsame)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    if len(start)==0:
                        pos=pygame.mouse.get_pos()
                        if (pos[0]>=sidewidth and pos[0]<=sidewidth+width) and (
                            pos[1]>=sidewidth and pos[1]<=sidewidth+width):
                            position=[pos[0],pos[1]]
                            start=[position[0]//sidewidth,position[1]//sidewidth]
                            if blocks[start[0]][start[1]][0]==0:
                                start=[]
                    else:
                        pos=pygame.mouse.get_pos()
                        if (pos[0]>=sidewidth and pos[0]<=sidewidth+width) and (
                            pos[1]>=sidewidth and pos[1]<=sidewidth+width):
                            position=[pos[0],pos[1]]
                            end=[position[0]//sidewidth,position[1]//sidewidth]
                            if blocks[end[0]][end[1]][0]==0:
                                end=[]
        if len(start)!=0:
            drawline(window,start)
            if len(end)!=0:
                drawline(window,end)
                if start!=end:
                    if blocks[start[0]][start[1]][0]==blocks[end[0]][end[1]][0]:
                        if zeroLineup(start,end):
                            blocks[start[0]][start[1]][0]=0
                            blocks[end[0]][end[1]][0]=0
                            ifshow=True
                            scores+=2
                            sound.play()
                        elif oneLineup(start,end) is not False:
                            blocks[start[0]][start[1]][0]=0
                            blocks[end[0]][end[1]][0]=0
                            ifshow=True
                            scores+=2
                            sound.play()
                        elif twoLineup(start,end) is not False:
                            blocks[start[0]][start[1]][0]=0
                            blocks[end[0]][end[1]][0]=0
                            ifshow=True
                            scores+=2
                            sound.play()
                        else:
                            start=end[:]
                            end=[]
                    else:
                        start=end[:]
                        end=[]
                else:
                    start,end =[],[]
        if ifshow :
            imgtick+=1
            if len(turns)>0:
                showingturns=turns[:]
                turns=[]
            if len(showstart)==0:
                showstart=[i*sidewidth+sidewidth//2 for i in start]
                showend=[i*sidewidth+sidewidth//2 for i in end]
                start,end =[],[]
            if len(showingturns)>0 :
                if len(showingturns)==1:
                    pygame.draw.lines(window,linecolor,False,
                                      [(showstart[0],showstart[1])
                                       ,(showingturns[0][0],showingturns[0][1])
                                       ,(showend[0],showend[1])],5)
                else:
                    pygame.draw.lines(window,linecolor,False,
                                      [(showstart[0],showstart[1]),
                                      (showingturns[0][0],showingturns[0][1]),
                                      (showingturns[1][0],showingturns[1][1]),
                                      (showend[0],showend[1])],5)
            else:
                pygame.draw.line(window,linecolor,(showstart[0],showstart[1]),(showend[0],showend[1]),5)
            if imgtick==10:
                imgtick=0
                showingturns=[]
                showstart=[]
                showend=[]
                ifshow=False
        pygame.display.update()
def zeroLineup(startpos:list,endpos:list):
    global blocks
    if startpos[0]==endpos[0]:
        x=startpos[0]
        start=min(startpos[1],endpos[1])
        end=max(startpos[1],endpos[1])
        start+=1
        while start<end:
            if blocks[x][start][0]==0:
                start+=1
            else:return False
        return True
    elif startpos[1]==endpos[1]:
        y=startpos[1]
        start=min(startpos[0],endpos[0])
        end=max(startpos[0],endpos[0])
        start+=1
        while start<end:
            if blocks[start][y][0]==0:
                start+=1
            else:return False
        return True
    else:
        return False
def oneLineup(startpos:list,endpos:list):
    global blocks,turns
    if startpos[0]==endpos[0] or startpos[1]==endpos[1]:return False
    if blocks[endpos[0]][startpos[1]][0]==0:
        if zeroLineup(startpos,[endpos[0],startpos[1]]) and zeroLineup(endpos,[endpos[0],startpos[1]]) :
            turns.append([endpos[0]*sidewidth+sidewidth//2,startpos[1]*sidewidth+sidewidth//2])
            return True
    if blocks[startpos[0]][endpos[1]][0]==0:
        if zeroLineup([startpos[0],endpos[1]],endpos) and zeroLineup([startpos[0],endpos[1]],startpos):
            turns.append([startpos[0]*sidewidth+sidewidth//2,endpos[1]*sidewidth+sidewidth//2])
            return True
    return False
def twoLineup(startpos:list,endpos:list):
    global blocks,turns
    x=startpos[0]
    y=startpos[1]
    x-=1
    while x>=0:
        if blocks[x][y][0]==0 and zeroLineup([x,y],startpos):
            if oneLineup([x,y],endpos) is not False:
                turns.insert(0,[x*sidewidth+sidewidth//2,y*sidewidth+sidewidth//2])
                return True
            x-=1
        else:
            x-=1
    x=startpos[0]
    y=startpos[1]
    x+=1
    while x<xNum:
        if blocks[x][y][0]==0 and zeroLineup([x,y],startpos) :
            if oneLineup([x,y],endpos) is not False:
                turns.insert(0,[x*sidewidth+sidewidth//2,y*sidewidth+sidewidth//2])
                return True
            x+=1
        else:
            x+=1
    x=startpos[0]
    y=startpos[1]
    y-=1
    while y>=0:
        if blocks[x][y][0]==0 and zeroLineup([x,y],startpos):
            if oneLineup([x,y],endpos) is not False:
                turns.insert(0,[x*sidewidth+sidewidth//2,y*sidewidth+sidewidth//2])
                return True
            y-=1
        else:
            y-=1
    x=startpos[0]
    y=startpos[1]
    y+=1
    while y<yNum:
        if blocks[x][y][0]==0 and zeroLineup([x,y],startpos):
            if oneLineup([x,y],endpos) is not False:
                turns.insert(0,[x*sidewidth+sidewidth//2,y*sidewidth+sidewidth//2])
                return True
            y+=1
        else:
            y+=1
    return False
def message_box(suject,content):
    root=tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(suject,content)
    try:
        root.destroy()
    except:pass
def formnumers(num):
    lis=[i for i in range(1,xnum*ynum//num+1)]
    res=[]
    for i in range(xnum*ynum):
        k=random.choice(lis)
        res.append(k)
        if res.count(k)==num:
            lis.remove(k)
    return res

window=tk.Tk()
window.title('连连看')
window.geometry('400x300')

l = tk.Label(window, 
    text='请选择一个难度!',   
    bg='white',    
    font=('Arial', 18),   
    width=40, height=4  
    )
l.pack()
var=tk.StringVar() 

b=tk.Button(window,text='简单',width=15,height=2,command=lambda:main(0))
c=tk.Button(window,text='中等',width=15,height=2,command=lambda:main(1))
d=tk.Button(window,text='困难',width=15,height=2,command=lambda:main(2))
b.pack()
c.pack()
d.pack()
window.mainloop()

xnum=4
ynum=4


