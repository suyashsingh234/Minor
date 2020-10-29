# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:35:21 2020

@author: Suyash Singh
"""
import os
from mido import MidiFile

def create_data():
    dataset="../datasets/good midi/"
    
    x_train=[]
    y_train=[]
    
    midFiles= [f for f in os.listdir(dataset) if f.endswith('.mid')]   
       
    for file in midFiles:
        pianoLeft=[]
        pianoRight=[]
        piano=[]
        mid=MidiFile(dataset+file)
        right=mid.tracks[1]
        left=mid.tracks[2]
        
        for msg in right:
            if str(msg).split(' ')[0]=='note_on' or str(msg).split(' ')[0]=='note_off':
                temp=[]
                for m in str(msg).split(' '):
                    if m=='note_on':
                        temp.append(1)
                    elif m=='note_off':
                        temp.append(0)
                    else:
                        temp.append(int(m.split('=')[1]))
                pianoRight.append(temp)
                
        for msg in left:
            if str(msg).split(' ')[0]=='note_on' or str(msg).split(' ')[0]=='note_off':
                temp=[]
                for m in str(msg).split(' '):
                    if m=='note_on':
                        temp.append(1)
                    elif m=='note_off':
                        temp.append(0)
                    else:
                        temp.append(int(m.split('=')[1]))
                pianoLeft.append(temp)
        
        piano=pianoLeft+pianoRight
        
        i=0
        while i<500:
            y_train.append(piano[i+1])
            cur_train=[]
            j=0
            while j<=i:
                cur_train.append(piano[j])
                j+=1
            while j<500:
                cur_train.append([0,0,0,0,0])
                j+=1
            x_train.append(cur_train)    
            i+=1
    return (x_train,y_train)

# =============================================================================
#         [[1,2,3,4,5],[0,0,0,0,0],[0,0,0,0,0]]
#         [[4,5,6,7,8]]
#         
#         [[1,2,3,4,5],[4,5,6,7,8],[0,0,0,0,0]]
#         [[10,11,12,13,14]]
#         
#         x_train=[ [[1,2,3,4,5],[0,0,0,0,0],[0,0,0,0,0]], [[1,2,3,4,5],[4,5,6,7,8],[0,0,0,0,0]] ]
#         y_train= [ [[4,5,6,7,8]], [[10,11,12,13,14]] ]
# =============================================================================

