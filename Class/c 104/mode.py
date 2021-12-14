import csv
from collections import Counter
with open('height_weght.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

data=Counter(new_data) 
mode_data_for_range={
                     "50-60":0,
                     "60-70":0,
                     "70-80":0
                   }

for height,occurunce in data.items():
    if 50<float(height)<60:
        mode_data_for_range["50-60"]+=occurunce
    elif 60<float(height)<70:
        mode_data_for_range["60-70"]+=occurunce   
    elif 70<float(height)<80:
        mode_data_for_range["70-80"]+=occurunce  

mode_range,mode_occurunce=0,0
for range,occurunce in mode_data_for_range.items():
    if occurunce>mode_occurunce:
        mode_range,mode_occurunce=[int(range.split("-")[0]),int(range.split("-")[1])],occurunce
mode=float((mode_range[0] +mode_range[1] )/2)   
print(f"mode is:{mode:2f}")       

