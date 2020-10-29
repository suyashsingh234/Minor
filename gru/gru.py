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

x_train=x_train.astype("int")
y_train=y_train.astype("int")

x_train=x_train[:500]
y_train=y_train[:500]

model=keras.Sequential()
model.add(keras.Input(shape=(500,5)))
model.add(keras.layers.GRU(5,activation='linear'))
model.add(keras.layers.Dense(1*5))

model.compile(
        loss=keras.losses.MeanAbsoluteError(),
        optimizer=keras.optimizers.Adam(lr=0.001),
        metrics=["accuracy"]
    )

model.fit(x_train,y_train)

# song generation

mid = MidiFile()
track = MidiTrack()

currentNote=x_train[0].tolist()

i=0
while i<499:
    feed=[currentNote]
    feed=np.array(feed)
    output=model.predict(feed)
    output=np.absolute(output)
    output=output[0].astype("int").tolist()
    print(output)
    currentNote[i+1]=output
    i+=1 

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
