import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#sensor_V_68 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
#sensor_I_microamps_68 = [1.2221,0.7915800000000001,0.8655200000000001,0.9708000000000001,1.0210000000000001,1.0390000000000001,1.0502,1.058,1.0639,1.0685,1.0721,1.0753000000000001,1.0780999999999998,1.0808000000000002,1.0838,1.0877999999999999,1.0969000000000002,1.1219000000000001,1.178,1.2782,1.4313,1.6424,1.9145999999999999,2.2503,2.6485000000000003,3.1173,3.6401,4.221100000000001,4.8589,5.552700000000001,6.297300000000001,7.0954,7.942800000000001,8.8282,9.756000000000002,10.712,11.721,12.784000000000002,13.869,0,0]
#sensor_I_nanoamps_68 = [i * 1000 for i in sensor_I_microamps_68]


#sensor_V_70= [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
#sensor_I_microamps_70 = [1.9283000000000003,1.2904000000000002,1.4061,1.4687000000000003,1.489,1.5008000000000001,1.5091,1.5158,1.5212999999999999,1.5261,1.5303,1.5342,1.538,1.5415,1.5448,1.5483,1.5517,1.5552000000000001,1.5587000000000002,1.5621,1.5656,1.5690000000000002,1.5724000000000002,1.5757000000000003,1.5792000000000002,1.5827000000000002,1.5860999999999998,1.5895000000000001,1.5928,1.5962,1.5994000000000002,1.6028000000000002,1.6062,1.6096,1.6129000000000002,1.6162,1.6195000000000002,1.6229000000000002,1.6262000000000003,1.6296,1.6329000000000002]
#sensor_I_nanoamps_70 = [j * 1000 for j in sensor_I_microamps_70]

#sensor_V_71 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
#sensor_I_microamps_71 = [0.87987,0.68506,0.77588,0.8607600000000001,0.8819000000000001,0.8935299999999999,0.90123,0.9068900000000001,0.9112,0.9145599999999999,0.9174500000000001,0.9199600000000001,0.9223300000000001,0.9246900000000001,0.9268500000000001,0.9286900000000001,0.9304500000000001,0.9322000000000001,0.9339500000000001,0.93568,0.9373900000000001,0.9390000000000001,0.94049,0.94193,0.94337,0.94481,0.9462700000000001,0.9477500000000001,0.94925,0.9508400000000001,0.9524500000000001,0.9552000000000002,0.9567000000000001,0.9579,0.9592,0.9603999999999999,0.9616,0.9627999999999999,0.964,0.9653,0.9665]
#sensor_I_nanoamps_71 =[k * 1000 for k in sensor_I_microamps_71]

#sensor_V_72 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
#sensor_I_microamps_72 = [0.8385000000000001,0.68365,0.7723200000000001,0.86555,0.88829,0.9017999999999999,0.90888,0.9149800000000001,0.9196500000000001,0.92329,0.9262000000000001,0.9288700000000001,0.9313500000000001,0.9338700000000001,0.9361100000000001,0.93801,0.9398400000000001,0.94165,0.94347,0.94529,0.9471200000000001,0.9488800000000001,0.9505,0.9533,0.9549,0.9564,0.9578,0.9594,0.9609,0.9626000000000001,0.9641,0.9656000000000001,0.967,0.9683000000000002,0.9697,0.9710000000000001,0.9722000000000002,0.9735,0.9747000000000001,0.9760000000000001,0.9772000000000002]
#sensor_I_nanoamps_72 = [m * 1000 for m in sensor_I_microamps_72]

#sensor_V_73 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200] 
#sensor_I_microamps_73 = [1.2288,0.77431,0.8467600000000001,0.9510000000000001,1.0029,1.0207,1.0316,1.0393,1.0451,1.0497,1.0533,1.0562000000000002,1.0590000000000002,1.0615999999999999,1.0644000000000002,1.0672000000000001,1.0698,1.0723,1.0747,1.0771,1.0793,1.0812000000000002,1.0831,1.0849000000000002,1.0867000000000002,1.0885,1.0903,1.0920999999999998,1.0938,1.0957000000000001,1.0976,1.0996000000000001,1.1016,1.1036,1.1054000000000002,1.1072000000000002,1.1088,1.1104000000000003,1.1120999999999999,1.1137000000000001,1.1153]
#sensor_I_nanoamps_73 = [n * 1000 for n in sensor_I_microamps_73]



df_1 = pd.read_csv(".csv", skiprows=[])  #put in name of csv file and number of rows to skip to get to V and I columns
#df_2 = pd.read_csv(".csv", on_bad_lines='skip')    This option does not work as well as skiprows
print(df_1)
#print(df_2)


hybrid_V = df_1[")"] #put in column names
hybrid_I = df_1[""]

plt.scatter(hybrid_V, hybrid_I, label="Hybrid IV", marker = ".")    
plt.scatter(sensor_V_, sensor_I_nanoamps_, label="Sensor Tile IV", marker = ".")    #add correct numbers at end of sensor variables
#plt.yscale("log")
plt.xlabel("Bias Voltage (V)")
plt.ylabel("Leakage Current (nA)")
#plt.ylabel("Log [Leakage Current (nA)]")
plt.title("")   #include serial no, lights on/off, etc.
plt.show()

#temporary script for plotting












