# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(r"kernels.h5")
prediction.loadModel()

predictions, percentage_probabilities = prediction.predictImage(r"sample.jpeg", result_count=5)
for index in range(len(predictions)):
    print(predictions[index] , " : " , percentage_probabilities[index])