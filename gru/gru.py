# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:51:15 2020

@author: Suyash Singh
"""
import tensorflow as tf
from tensorflow import keras

import numpy as np

from data import create_data

(x_train,y_train)=create_data()

x_train=np.array(x_train)
y_train=np.array(y_train)

print(x_train.shape)
print(y_train.shape)

model=keras.Sequential()
model.add(keras.Input(shape=(500,5)))
model.add(keras.layers.GRU(5,activation='relu'))
model.add(keras.layers.Dense(1*5))

model.compile(
        loss=keras.losses.CategoricalCrossentropy(from_logits=True),
        optimizer=keras.optimizers.Adam(lr=0.001),
        metrics=["accuracy"]
    )

model.fit(x_train,y_train)


#model.evaluate(x_test,y_test)