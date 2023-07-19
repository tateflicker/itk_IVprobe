import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def main():

    #Sensor Data:

    sensor_V_68 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
    sensor_I_microamps_68 = [1.2221,0.7915800000000001,0.8655200000000001,0.9708000000000001,1.0210000000000001,1.0390000000000001,1.0502,1.058,1.0639,1.0685,1.0721,1.0753000000000001,1.0780999999999998,1.0808000000000002,1.0838,1.0877999999999999,1.0969000000000002,1.1219000000000001,1.178,1.2782,1.4313,1.6424,1.9145999999999999,2.2503,2.6485000000000003,3.1173,3.6401,4.221100000000001,4.8589,5.552700000000001,6.297300000000001,7.0954,7.942800000000001,8.8282,9.756000000000002,10.712,11.721,12.784000000000002,13.869,0,0]
    sensor_I_nanoamps_68 = [i * 1000 for i in sensor_I_microamps_68]


    sensor_V_70= [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
    sensor_I_microamps_70 = [1.9283000000000003,1.2904000000000002,1.4061,1.4687000000000003,1.489,1.5008000000000001,1.5091,1.5158,1.5212999999999999,1.5261,1.5303,1.5342,1.538,1.5415,1.5448,1.5483,1.5517,1.5552000000000001,1.5587000000000002,1.5621,1.5656,1.5690000000000002,1.5724000000000002,1.5757000000000003,1.5792000000000002,1.5827000000000002,1.5860999999999998,1.5895000000000001,1.5928,1.5962,1.5994000000000002,1.6028000000000002,1.6062,1.6096,1.6129000000000002,1.6162,1.6195000000000002,1.6229000000000002,1.6262000000000003,1.6296,1.6329000000000002]
    sensor_I_nanoamps_70 = [j * 1000 for j in sensor_I_microamps_70]

    sensor_V_71 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
    sensor_I_microamps_71 = [0.87987,0.68506,0.77588,0.8607600000000001,0.8819000000000001,0.8935299999999999,0.90123,0.9068900000000001,0.9112,0.9145599999999999,0.9174500000000001,0.9199600000000001,0.9223300000000001,0.9246900000000001,0.9268500000000001,0.9286900000000001,0.9304500000000001,0.9322000000000001,0.9339500000000001,0.93568,0.9373900000000001,0.9390000000000001,0.94049,0.94193,0.94337,0.94481,0.9462700000000001,0.9477500000000001,0.94925,0.9508400000000001,0.9524500000000001,0.9552000000000002,0.9567000000000001,0.9579,0.9592,0.9603999999999999,0.9616,0.9627999999999999,0.964,0.9653,0.9665]
    sensor_I_nanoamps_71 =[k * 1000 for k in sensor_I_microamps_71]

    sensor_V_72 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
    sensor_I_microamps_72 = [0.8385000000000001,0.68365,0.7723200000000001,0.86555,0.88829,0.9017999999999999,0.90888,0.9149800000000001,0.9196500000000001,0.92329,0.9262000000000001,0.9288700000000001,0.9313500000000001,0.9338700000000001,0.9361100000000001,0.93801,0.9398400000000001,0.94165,0.94347,0.94529,0.9471200000000001,0.9488800000000001,0.9505,0.9533,0.9549,0.9564,0.9578,0.9594,0.9609,0.9626000000000001,0.9641,0.9656000000000001,0.967,0.9683000000000002,0.9697,0.9710000000000001,0.9722000000000002,0.9735,0.9747000000000001,0.9760000000000001,0.9772000000000002]
    sensor_I_nanoamps_72 = [m * 1000 for m in sensor_I_microamps_72]

    sensor_V_73 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200] 
    sensor_I_microamps_73 = [1.2288,0.77431,0.8467600000000001,0.9510000000000001,1.0029,1.0207,1.0316,1.0393,1.0451,1.0497,1.0533,1.0562000000000002,1.0590000000000002,1.0615999999999999,1.0644000000000002,1.0672000000000001,1.0698,1.0723,1.0747,1.0771,1.0793,1.0812000000000002,1.0831,1.0849000000000002,1.0867000000000002,1.0885,1.0903,1.0920999999999998,1.0938,1.0957000000000001,1.0976,1.0996000000000001,1.1016,1.1036,1.1054000000000002,1.1072000000000002,1.1088,1.1104000000000003,1.1120999999999999,1.1137000000000001,1.1153]
    sensor_I_nanoamps_73 = [n * 1000 for n in sensor_I_microamps_73]

    #Hybrid Data:

    df_70_lightsOff = pd.read_csv("20UPGB42000070_14BB3_20230714-095815_lightsOff.csv", skiprows = [0,1,2,3,4,5])
    hybrid_V_70_lightsOff = df_70_lightsOff["V_Bias (V)"]
    hybrid_I_70_lightsOff = df_70_lightsOff["I_leakage (nA)"]

    df_68 = pd.read_csv("20UPGB42000068_14B8D_20230714-120813.csv", skiprows= [0,1,2,3,4,5])
    hybrid_V_68 = df_68["V_Bias (V)"] 
    hybrid_I_68 = df_68["I_leakage (nA)"]

    df_70 = pd.read_csv("20UPGB42000070_14BB3_20230714-093611.csv", skiprows=[0,1,2,3,4,5])
    hybrid_V_70 = df_70["V_Bias (V)"] 
    hybrid_I_70 = df_70["I_leakage (nA)"]

    df_71 = pd.read_csv("20UPGB42000071_14BA2_20230712-204622.csv", skiprows=[0,1,2,3])
    hybrid_V_71 = df_71["V_Bias"] 
    hybrid_I_71 = df_71["I_leakage"]

    df_72 = pd.read_csv("20UPGB42000072_14BA9_20230712-201946.csv", skiprows=[0,1,2,3])
    hybrid_V_72 = df_72["V_Bias"] 
    hybrid_I_72 = df_72["I_leakage"]

    df_73 = pd.read_csv("20UPGB42000073_14B9B_20230712-194434.csv", skiprows=[0,1,2,3])
    hybrid_V_73 = df_73["V_Bias"] 
    hybrid_I_73 = df_73["I_leakage"]

    sensor_hybrid_compare(hybrid_V_68, hybrid_I_68, sensor_V_68, sensor_I_nanoamps_68, hybrid_V_70, hybrid_I_70, sensor_V_70, sensor_I_nanoamps_70, hybrid_V_71, hybrid_I_71, sensor_V_71, sensor_I_nanoamps_71, hybrid_V_72, hybrid_I_72, sensor_V_72, sensor_I_nanoamps_72, hybrid_V_73, hybrid_I_73, sensor_V_73, sensor_I_nanoamps_73)
    log_sensor_hybrid(hybrid_V_68, hybrid_I_68, sensor_V_68, sensor_I_nanoamps_68, hybrid_V_70, hybrid_I_70, sensor_V_70, sensor_I_nanoamps_70, hybrid_V_71, hybrid_I_71, sensor_V_71, sensor_I_nanoamps_71, hybrid_V_72, hybrid_I_72, sensor_V_72, sensor_I_nanoamps_72, hybrid_V_73, hybrid_I_73, sensor_V_73, sensor_I_nanoamps_73)
    all_five_BMs(hybrid_V_68, hybrid_I_68, hybrid_V_70, hybrid_I_70, hybrid_V_71, hybrid_I_71, hybrid_V_72, hybrid_I_72, hybrid_V_73, hybrid_I_73)
    lightsOn_lightsOff(hybrid_V_70, hybrid_I_70, hybrid_V_70_lightsOff, hybrid_I_70_lightsOff)


def sensor_hybrid_compare(hybrid_V_68, hybrid_I_68, sensor_V_68, sensor_I_nanoamps_68, hybrid_V_70, hybrid_I_70, sensor_V_70, sensor_I_nanoamps_70, hybrid_V_71, hybrid_I_71, sensor_V_71, sensor_I_nanoamps_71, hybrid_V_72, hybrid_I_72, sensor_V_72, sensor_I_nanoamps_72, hybrid_V_73, hybrid_I_73, sensor_V_73, sensor_I_nanoamps_73):
    fig, axs = plt.subplots(5)
    axs[0].scatter(hybrid_V_68, hybrid_I_68, label = "BM 0068", marker = ".")
    axs[0].scatter(sensor_V_68, sensor_I_nanoamps_68, label = "Sensor Tile", marker = ".")
    axs[0].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[0].set_ylabel("Leakage Current (nA)", fontsize = 12)
    axs[0].set_title("BM 0068 IV", fontsize = 16)
    axs[0].legend(fontsize = 12)

    axs[1].scatter(hybrid_V_70, hybrid_I_70, label = "BM 0070", marker = ".")
    axs[1].scatter(sensor_V_70, sensor_I_nanoamps_70, label = "Sensor Tile", marker = ".")
    axs[1].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[1].set_ylabel("Leakage Current (nA)", fontsize = 12)
    axs[1].set_title("BM 0070 IV", fontsize = 16)
    axs[1].legend(fontsize = 12)

    axs[2].scatter(hybrid_V_71, hybrid_I_71, label = "BM 0071", marker = ".")
    axs[2].scatter(sensor_V_71, sensor_I_nanoamps_71, label = "Sensor Tile", marker = ".")
    axs[2].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[2].set_ylabel("Leakage Current (nA)", fontsize = 12)
    axs[2].set_title("BM 0071 IV", fontsize = 16)
    axs[2].legend(fontsize = 12)

    axs[3].scatter(hybrid_V_72, hybrid_I_72, label = "BM 0072", marker = ".")
    axs[3].scatter(sensor_V_72, sensor_I_nanoamps_72, label = "Sensor Tile", marker = ".")
    axs[3].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[3].set_ylabel("Leakage Current (nA)", fontsize = 12)
    axs[3].set_title("BM 0072 IV", fontsize = 16)
    axs[3].legend(fontsize = 12)

    axs[4].scatter(hybrid_V_73, hybrid_I_73, label = "BM 0073", marker = ".")
    axs[4].scatter(sensor_V_73, sensor_I_nanoamps_73, label = "Sensor Tile", marker = ".")
    axs[4].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[4].set_ylabel("Leakage Current (nA)", fontsize = 12)
    axs[4].set_title("BM 0073 IV", fontsize = 16)
    axs[4].legend(fontsize = 12)

    fig.suptitle("Comparing Hybrid IV and Sensor IV", fontsize = 18)
    fig.tight_layout()
    fig.show()


def log_sensor_hybrid(hybrid_V_68, hybrid_I_68, sensor_V_68, sensor_I_nanoamps_68, hybrid_V_70, hybrid_I_70, sensor_V_70, sensor_I_nanoamps_70, hybrid_V_71, hybrid_I_71, sensor_V_71, sensor_I_nanoamps_71, hybrid_V_72, hybrid_I_72, sensor_V_72, sensor_I_nanoamps_72, hybrid_V_73, hybrid_I_73, sensor_V_73, sensor_I_nanoamps_73):
    fig, axs = plt.subplots(5)
    axs[0].scatter(hybrid_V_68, hybrid_I_68, label = "BM 0068", marker = ".")
    axs[0].scatter(sensor_V_68, sensor_I_nanoamps_68, label = "Sensor Tile", marker = ".")
    axs[0].set_yscale("log")
    axs[0].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[0].set_ylabel("Log [Leakage Current] (nA)", fontsize = 12)
    axs[0].set_title("BM 0068 IV - Logarithmic", fontsize = 16)
    axs[0].legend(fontsize = 12)

    axs[1].scatter(hybrid_V_70, hybrid_I_70, label = "BM 0070", marker = ".")
    axs[1].scatter(sensor_V_70, sensor_I_nanoamps_70, label = "Sensor Tile", marker = ".")
    axs[1].set_yscale("log")
    axs[1].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[1].set_ylabel("Log [Leakage Current] (nA)", fontsize = 12)
    axs[1].set_title("BM 0070 IV - Logarithmic", fontsize = 16)
    axs[1].legend(fontsize = 12)

    axs[0,2].scatter(hybrid_V_71, hybrid_I_71, label = "BM 0071", marker = ".")
    axs[0,2].scatter(sensor_V_71, sensor_I_nanoamps_71, label = "Sensor Tile", marker = ".")
    axs[0,2].set_yscale("log")
    axs[0,2].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[0,2].set_ylabel("Log [Leakage Current] (nA)", fontsize = 12)
    axs[0,2].set_title("BM 0071 IV - Logarithmic", fontsize = 16)
    axs[0,2].legend(fontsize = 12)

    axs[3].scatter(hybrid_V_72, hybrid_I_72, label = "BM 0072", marker = ".")
    axs[3].scatter(sensor_V_72, sensor_I_nanoamps_72, label = "Sensor Tile", marker = ".")
    axs[3].set_yscale("log")
    axs[3].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[3].set_ylabel("Log [Leakage Current] (nA)", fontsize = 12)
    axs[3].set_title("BM 0072 IV - Logarithmic", fontsize = 16)
    axs[3].legend(fontsize = 12)

    axs[4].scatter(hybrid_V_73, hybrid_I_73, label = "BM 0073", marker = ".")
    axs[4].scatter(sensor_V_73, sensor_I_nanoamps_73, label = "Sensor Tile", marker = ".")
    axs[4].set_yscale("log")
    axs[4].set_xlabel("Bias Voltage (V)", fontsize = 12)
    axs[4].set_ylabel("Log [Leakage Current] (nA)", fontsize = 12)
    axs[4].set_title("BM 0073 IV - Logarithmic", fontsize = 16)
    axs[4].legend(fontsize = 12)

    fig.suptitle("Comparing Hybrid and Sensor IV With a Logarithmic Scale", fontsize = 18)
    fig.tight_layout()
    fig.show()


def all_five_BMs(hybrid_V_68, hybrid_I_68, hybrid_V_70, hybrid_I_70, hybrid_V_71, hybrid_I_71, hybrid_V_72, hybrid_I_72, hybrid_V_73, hybrid_I_73): 
    plt.scatter(hybrid_V_68, hybrid_I_68, label="BM 0068", marker = ".")    
    plt.scatter(hybrid_V_70, hybrid_I_70, label="BM 0070", marker= ".")
    plt.scatter(hybrid_V_71, hybrid_I_71, label="BM 0071", marker = ".")    
    plt.scatter(hybrid_V_72, hybrid_I_72, label="BM 0072", marker= ".")
    plt.scatter(hybrid_V_73, hybrid_I_73, label="BM 0073", marker = ".")  

    plt.xlabel("Bias Voltage (V)", fontsize = 12)
    plt.ylabel("Leakage Current (nA)", fontsize = 12)
    plt.title("IV Curves for Five BMs", fontsize = 16)
    plt.legend(fontsize = 12)
    plt.show()


def lightsOn_lightsOff(hybrid_V_70, hybrid_I_70, hybrid_V_70_lightsOff, hybrid_I_70_lightsOff):
    plt.scatter(hybrid_V_70, hybrid_I_70, label="Lights On", marker=".")
    plt.scatter(hybrid_V_70_lightsOff, hybrid_I_70_lightsOff, label="Lights Off", marker=".")

    plt.xlabel("Bias Voltage (V)", fontsize = 12)
    plt.ylabel("Leakage Current (nA)", fontsize = 12)
    plt.title("20UPGB420070 Lights On vs. Lights Off", fontsize = 16)
    plt.legend(fontsize = 12)
    plt.show()


if __name__ == "__main__":
    main()















