# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:53:44 2020

@author: Suyash Singh
"""
from mido import MidiFile


dataset="../datasets/piano midi/"

mid=MidiFile(dataset+"albeniz/alb_esp2.mid",clip=True)

newtrack=MidiFile()

print(mid.tracks)
newtrack.tracks.append(mid.tracks[1])
newtrack.tracks.append(mid.tracks[2])

newtrack.save(dataset+"new.mid")



