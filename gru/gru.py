# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:51:15 2020

@author: Suyash Singh
"""
import tensorflow as tf
from tensorflow import keras

import numpy as np
import random
from mido import Message, MidiFile, MidiTrack

from data import create_data

(x_train,y_train)=create_data()

x_train=np.array(x_train)
y_train=np.array(y_train)

x_train=x_train.astype("float32")
y_train=y_train.astype("float32")

x_train=x_train[:500]
y_train=y_train[:500]

def normalize(list):
    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            list[i][j]=(list[i][j][0]/1,list[i][j][1]/15,list[i][j][2]/127,list[i][j][3]/127,list[i][j][4]/1000)
    return list

def normalizeY(list):
    for i in range(0,len(list)):
        list[i]=(list[i][0]/1,list[i][1]/15,list[i][2]/127,list[i][3]/127,list[i][4]/1000)
    return list
    
x_train=normalize(x_train)
y_train=normalizeY(y_train)

model=keras.Sequential()
model.add(keras.Input(shape=(16,5)))
model.add(keras.layers.GRU(5,activation='linear'))
model.add(keras.layers.Dense(1*5))

model.compile(
        loss=keras.losses.MeanSquaredError(),
        optimizer=keras.optimizers.Adam(lr=0.001),
        metrics=["accuracy"]
    )

model.fit(x_train,y_train)

# song generation
mid = MidiFile()
track = MidiTrack()

currentNote=x_train[0].tolist()
Note=[]
for note in currentNote:
    Note.append(note)
i=0
while i<499:
    feed=[currentNote]
    feed=np.array(feed)
    output=model.predict(feed)
    output=np.absolute(output)
    output=output[0].tolist()
    for j in range(1,16):
        currentNote[j-1]=currentNote[j]
    currentNote[15]=output
    Note.append(output)
    i+=1 

for note in Note:
    print(note)
# =============================================================================
# for note in currentNote:
#     print(note)
#     (a,b,c,d,e)=note
#     if a:
#         a='note_on'
#     else:
#         a='note_off'
#     track.append(Message(a,channel=b,note=c,velocity=d,time=e))
# 
# mid.tracks.append(track)        
# mid.save('song_gru.mid')
# =============================================================================
# =============================================================================
# test=np.array([x_train[1]])
# 
# print( model.predict(test) )
# =============================================================================
