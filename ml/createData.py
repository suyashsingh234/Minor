# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:08:33 2020

@author: Suyash Singh
"""
import os
from mido import MidiFile

def create_data():
    dataset="../datasets/good midi/"
    badDataset="../datasets/bad midi/"
    
    pianoLeft=[]
    pianoRight=[]
    piano=[]
    play=[]
    
    midFiles= [f for f in os.listdir(dataset) if f.endswith('.mid')]   
       
    for file in midFiles:
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
         
        midFiles= [f for f in os.listdir(badDataset) if f.endswith('.mid')]     
        badPiano=[]
        for file in midFiles:
            mid=MidiFile(badDataset+file)
            for msg in mid.tracks[0]:
                if str(msg).split(' ')[0]=='note_on' or str(msg).split(' ')[0]=='note_off':
                    temp=[]
                    for m in str(msg).split(' '):
                        if m=='note_on':
                            temp.append(1)
                        elif m=='note_off':
                            temp.append(0)
                        else:
                            temp.append(int(m.split('=')[1]))
                    badPiano.append(temp)
    
    piano=pianoLeft+pianoRight
    
    for i in range(len(piano)):
        play.append(1)
    
    piano=piano+badPiano
    
    for i in range(len(badPiano)):
        play.append(0)
    return [piano,play]
