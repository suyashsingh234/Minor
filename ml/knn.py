# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:53:44 2020

@author: Suyash Singh
"""

#note_on channel=0 note=81 velocity=60 time=240

from sklearn.neighbors import KNeighborsClassifier
from createData import create_data
import random
from mido import Message, MidiFile, MidiTrack

trainingData=create_data()
model = KNeighborsClassifier(n_neighbors=3)
model.fit(trainingData[0],trainingData[1])


mid = MidiFile()
track = MidiTrack()
i=0
while i<700:
    a=random.randint(0, 1)
    b=0
    c=random.randint(0,100)
    d=random.randint(0,127)
    e=random.randint(0, 2000)
    noteList=[[a,b,c,d,e]]
    predict=model.predict(noteList)
    if predict:
        i+=1
        if a:
            a='note_on'
        else:
            a='note_off'
        track.append(Message(a,channel=b,note=c,velocity=d,time=e))
    
mid.tracks.append(track)        
mid.save('new_song.mid')
        
        