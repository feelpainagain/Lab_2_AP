import os
import cv2
import csv
import numpy as np
import pandas as pd

columns = ["Absolute path", "Relative path", "Class"]
data = []
rel_path1 = r'dataset\tiger'
rel_path2 = r'dataset\leopard'

name_list1 = os.listdir(rel_path1)
name_list2 = os.listdir(rel_path2)

for name in name_list1:
    data.append([os.path.abspath(rel_path1 + name), rel_path1 + name, "tiger"])
for name in name_list2:
    data.append([os.path.abspath(rel_path2 + name), rel_path2 + name, "leopard"])


df = pd.DataFrame(data, columns=columns)
df.to_csv('annotation.csv', sep=";")
