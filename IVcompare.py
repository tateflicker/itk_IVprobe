import matplotlib.pyplot as plt

def main():
  #Sensor Data:
  V_bias_sensor = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
    
  sensor_I_microamps_68 = [1.2221,0.7915800000000001,0.8655200000000001,0.9708000000000001,1.0210000000000001,1.0390000000000001,1.0502,1.058,1.0639,1.0685,1.0721,1.0753000000000001,1.0780999999999998,1.0808000000000002,1.0838,1.0877999999999999,1.0969000000000002,1.1219000000000001,1.178,1.2782,1.4313,1.6424,1.9145999999999999,2.2503,2.6485000000000003,3.1173,3.6401,4.221100000000001,4.8589,5.552700000000001,6.297300000000001,7.0954,7.942800000000001,8.8282,9.756000000000002,10.712,11.721,12.784000000000002,13.869,0,0]
  sensor_I_nanoamps_68 = [i * 1000 for i in sensor_I_microamps_68]

  sensor_I_microamps_70 = [1.9283000000000003,1.2904000000000002,1.4061,1.4687000000000003,1.489,1.5008000000000001,1.5091,1.5158,1.5212999999999999,1.5261,1.5303,1.5342,1.538,1.5415,1.5448,1.5483,1.5517,1.5552000000000001,1.5587000000000002,1.5621,1.5656,1.5690000000000002,1.5724000000000002,1.5757000000000003,1.5792000000000002,1.5827000000000002,1.5860999999999998,1.5895000000000001,1.5928,1.5962,1.5994000000000002,1.6028000000000002,1.6062,1.6096,1.6129000000000002,1.6162,1.6195000000000002,1.6229000000000002,1.6262000000000003,1.6296,1.6329000000000002]
  sensor_I_nanoamps_70 = [j * 1000 for j in sensor_I_microamps_70]
  sensor_check_units_70 = [a / 10 for a in sensor_I_microamps_70]

  sensor_I_microamps_71 = [0.87987,0.68506,0.77588,0.8607600000000001,0.8819000000000001,0.8935299999999999,0.90123,0.9068900000000001,0.9112,0.9145599999999999,0.9174500000000001,0.9199600000000001,0.9223300000000001,0.9246900000000001,0.9268500000000001,0.9286900000000001,0.9304500000000001,0.9322000000000001,0.9339500000000001,0.93568,0.9373900000000001,0.9390000000000001,0.94049,0.94193,0.94337,0.94481,0.9462700000000001,0.9477500000000001,0.94925,0.9508400000000001,0.9524500000000001,0.9552000000000002,0.9567000000000001,0.9579,0.9592,0.9603999999999999,0.9616,0.9627999999999999,0.964,0.9653,0.9665]
  sensor_I_nanoamps_71 =[k * 1000 for k in sensor_I_microamps_71]
  sensor_check_units_71 = [b / 10 for b in sensor_I_microamps_71]

  sensor_I_microamps_72 = [0.8385000000000001,0.68365,0.7723200000000001,0.86555,0.88829,0.9017999999999999,0.90888,0.9149800000000001,0.9196500000000001,0.92329,0.9262000000000001,0.9288700000000001,0.9313500000000001,0.9338700000000001,0.9361100000000001,0.93801,0.9398400000000001,0.94165,0.94347,0.94529,0.9471200000000001,0.9488800000000001,0.9505,0.9533,0.9549,0.9564,0.9578,0.9594,0.9609,0.9626000000000001,0.9641,0.9656000000000001,0.967,0.9683000000000002,0.9697,0.9710000000000001,0.9722000000000002,0.9735,0.9747000000000001,0.9760000000000001,0.9772000000000002]
  sensor_I_nanoamps_72 = [m * 1000 for m in sensor_I_microamps_72]
  sensor_check_units_72 = [c / 10 for c in sensor_I_microamps_72]

  sensor_I_microamps_73 = [1.2288,0.77431,0.8467600000000001,0.9510000000000001,1.0029,1.0207,1.0316,1.0393,1.0451,1.0497,1.0533,1.0562000000000002,1.0590000000000002,1.0615999999999999,1.0644000000000002,1.0672000000000001,1.0698,1.0723,1.0747,1.0771,1.0793,1.0812000000000002,1.0831,1.0849000000000002,1.0867000000000002,1.0885,1.0903,1.0920999999999998,1.0938,1.0957000000000001,1.0976,1.0996000000000001,1.1016,1.1036,1.1054000000000002,1.1072000000000002,1.1088,1.1104000000000003,1.1120999999999999,1.1137000000000001,1.1153]
  sensor_I_nanoamps_73 = [n * 1000 for n in sensor_I_microamps_73]
  sensor_check_units_73 = [d / 10 for d in sensor_I_microamps_73]
  
  #Hybrid Data:
  
  hybrid_V_68 = [0,4.7,9.7,14.7,19.7,24.7,29.8,34.8,39.8,44.8,49.9,54.8,59.8,64.7,69.8,74.8,79.8,84.8,89.8,94.8,99.9,104.8,109.9,114.8,119.8,124.8,129.9,134.8,139.9,144.9,150,154.9,160,164.9,169.9,174.9,179.9,185,190,194.9,199.9]
  hybrid_I_microamps_68 = [0.015,0.0955,0.1285,0.1495,0.15,0.155,0.159,0.16,0.16,0.163,0.164,0.165,0.165,0.1695,0.1705,0.17500000000000002,0.18,0.185,0.19,0.199,0.20650000000000002,0.218,0.23,0.242,0.257,0.274,0.2895,0.3045,0.3245,0.34,0.358,0.3765,0.3955,0.40850000000000003,0.425,0.445,0.4645,0.485,0.504,0.523,0.541]
  I_error_68 = [0,0.004716990566028301,0.0032015621187164245,0.0015,0,0,0.002,0,0,0.002449489742783178,0.002,0,0,0.0015,0.0015,0,0,0,0,0.002,0.00229128784747792,0.002449489742783178,0,0.002449489742783178,0.002449489742783178,0.002,0.0015,0.0015,0.0015,0,0.002449489742783178,0.00229128784747792,0.0015,0.00229128784747792,0,0,0.0015,0,0.002,0.002449489742783178,0.002]

  hybrid_V_70 = [0,4.7,9.7,14.7,19.7,24.7,29.8,34.8,39.8,44.8,49.9,54.8,59.8,64.7,69.8,74.8,79.8,84.8,89.8,94.8,99.9,104.8,109.9,114.8,119.8,124.8,129.9,134.8,139.9,144.9,150,154.9,160,164.9,169.9,174.9,179.9,185,190,194.9,199.9]
  hybrid_I_microamps_70 = [0,0.08835,0.1425999999999999,0.16155,0.1635,0.1645,0.1655,0.1656,0.1660499999999999,0.16625,0.1665,0.16715,0.16715,0.1680499999999999,0.16855,0.1695,0.17015,0.1709,0.171,0.1715,0.1722999999999999,0.173,0.17315,0.1735,0.174,0.17445,0.1749,0.175,0.1755,0.176,0.176,0.1764999999999999,0.1767499999999999,0.177,0.17745,0.1775,0.178,0.1785,0.17855,0.179,0.17945]
  I_error_70 = [0,0.0007088723439378,0.0013190905958272,0.00015,0,2.775557561562892e-17,0,0.0002,0.00015,0.0006020797289396,0.0003162277660168,0.000502493781056,0.0003905124837953,0.00035,0.00015,0,0.0002291287847477,0.0002,0,0,0.0007483314773547,0.0002236067977499,0.0002291287847477,0,0,0.00015,0.0002,0,0,0,0,2.775557561562892e-17,0.00025,0,0.00015,0,0,2.775557561562892e-17,0.00015,0,0.00015]

  hybrid_V_71 = [0,4.7,9.7,14.7,19.7,24.7,29.8,34.8,39.8,44.8,49.9,54.8,59.8,64.7,69.8,74.8,79.8,84.8,89.8,94.8,99.9,104.8,109.9,114.8,119.8,124.8,129.9,134.8,139.9,144.9,150,154.9,160,164.9,169.9,174.9,179.9,185,190,194.9,199.9]
  hybrid_I_microamps_71 = [0,0.09985,0.1285,0.13745,0.1395,0.141,0.14225,0.1445,0.1457,0.1472,0.1485,0.1495,0.151,0.1519999999999999,0.153,0.1539999999999999,0.155,0.1557,0.1565,0.1575,0.1579999999999999,0.15875,0.1595,0.1599999999999999,0.1605,0.161,0.1615,0.1619499999999999,0.16245,0.163,0.1638,0.1642999999999999,0.16495,0.1655,0.1659999999999999,0.1665,0.167,0.1673,0.16755,0.1681,0.1685]
  I_error_71 = [0,0.0003201562118716,0,0.00015,0,0,0.0006800735254367,2.775557561562892e-17,0.0002449489742783,0.0006403124237432,2.775557561562892e-17,0,0,2.775557561562892e-17,0,2.775557561562892e-17,0,0.0002449489742783,2.775557561562892e-17,0,2.775557561562892e-17,0.00025,0,2.775557561562892e-17,2.775557561562892e-17,0,0,0.0002692582403567,0.00015,0,0.0002449489742783,0.0002449489742783,0.00015,0,2.775557561562892e-17,2.775557561562892e-17,0,0.0002449489742783,0.00015,0.0003,2.775557561562892e-17]

  hybrid_V_72 = [0,4.7,9.7,14.7,19.7,24.7,29.8,34.8,39.8,44.8,49.9,54.8,59.8,64.7,69.8,74.8,79.8,84.8,89.8,94.8,99.9,104.8,109.9,114.8,119.8,124.8,129.9,134.8,139.9,144.9,150,154.9,160,164.9,169.9,174.9,179.9,185,190,194.9,199.9]
  hybrid_I_microamps_72 = [0,0.08535,0.1185499999999999,0.136,0.1387,0.13995,0.141,0.1430499999999999,0.1447999999999999,0.14685,0.1479499999999999,0.14865,0.15095,0.1515,0.1525,0.1535,0.15375,0.155,0.1559999999999999,0.1567,0.1575,0.15805,0.1588999999999999,0.15935,0.1599,0.1605,0.161,0.1615,0.1619999999999999,0.16275,0.1632,0.1637,0.16435,0.1645,0.165,0.1655,0.1659999999999999,0.1664,0.1668,0.167,0.1675]
  I_error_72 = [0,0.0012854960132182,0.0004153311931459,0.0005477225575051,0.0002449489742783,0.0002692582403567,0.0002236067977499,0.00015,0.0004,0.00105,0.00015,0.0005937171043518,0.0011926860441876,0.0009486832980505,2.775557561562892e-17,0,0.0011672617529928,0,2.775557561562892e-17,0.0002449489742783,0,0.00015,0.0002,0.0002291287847477,0.0002,2.775557561562892e-17,0,0,2.775557561562892e-17,0.00025,0.0002449489742783,0.0002449489742783,0.0002291287847477,2.775557561562892e-17,0,0,2.775557561562892e-17,0.0002,0.0002449489742783,0,0]

  hybrid_V_73 = [0,4.7,9.7,14.7,19.7,24.7,29.8,34.8,39.8,44.8,49.9,54.8,59.8,64.7,69.8,74.8,79.8,84.8,89.8,94.8,99.9,104.8,109.9,114.8,119.8,124.8,129.9,134.8,139.9,144.9,150,154.9,160,164.9,169.9,174.9,179.9,185,190,194.9,199.9]
  hybrid_I_microamps_73 = [0.015,0.115,0.15,0.17200000000000001,0.17500000000000002,0.1785,0.18,0.18,0.18,0.1805,0.182,0.1845,0.185,0.185,0.185,0.185,0.186,0.19,0.19,0.19,0.19,0.19,0.19,0.1925,0.195,0.195,0.195,0.195,0.195,0.195,0.195,0.195,0.1975,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
  #no uncertainty data for BM 73
  
  IVcompare_68(V_bias_sensor, sensor_I_microamps_68, hybrid_V_68, hybrid_I_microamps_68, I_error_68)
  IVcompare_70(V_bias_sensor, sensor_I_microamps_70, hybrid_V_70, hybrid_I_microamps_70, I_error_70)
  IVcompare_71(V_bias_sensor, sensor_I_microamps_71, hybrid_V_71, hybrid_I_microamps_71, I_error_71)
  IVcompare_72(V_bias_sensor, sensor_I_microamps_72, hybrid_V_72, hybrid_I_microamps_72, I_error_72)
  IVcompare_73(V_bias_sensor, sensor_I_microamps_73, hybrid_V_73, hybrid_I_microamps_73)

  check_units_70(V_bias_sensor, sensor_check_units_70, hybrid_V_70, hybrid_I_microamps_70)
  check_units_71(V_bias_sensor, sensor_check_units_71, hybrid_V_71, hybrid_I_microamps_71)
  check_units_72(V_bias_sensor, sensor_check_units_72, hybrid_V_72, hybrid_I_microamps_72)
  check_units_73(V_bias_sensor, sensor_check_units_73, hybrid_V_73, hybrid_I_microamps_73)

  four_BMs(hybrid_V_70, hybrid_V_71, hybrid_V_72, hybrid_V_73, hybrid_I_microamps_70, hybrid_I_microamps_71, hybrid_I_microamps_72, hybrid_I_microamps_73, I_error_70, I_error_71, I_error_72)
  three_BMs(hybrid_V_70, hybrid_V_71, hybrid_V_72, hybrid_I_microamps_70, hybrid_I_microamps_71, hybrid_I_microamps_72, I_error_70, I_error_71, I_error_72)
  breakdown_comparison(hybrid_V_68, hybrid_V_70, hybrid_I_microamps_68, hybrid_I_microamps_70)

def IVcompare_68(V_bias_sensor, sensor_I_microamps_68, hybrid_V_68, hybrid_I_microamps_68, I_error_68):
  plt.scatter(V_bias_sensor, sensor_I_microamps_68, marker = "o", label = "Sensor Tile", color = "red")
  plt.errorbar(hybrid_V_68, hybrid_I_microamps_68, fmt = "o", label = "Hybrid", yerr = I_error_68, color = "blue")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("20UPGB42000068", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

def IVcompare_70(V_bias_sensor, sensor_I_microamps_70, hybrid_V_70, hybrid_I_microamps_70, I_error_70):
  plt.scatter(V_bias_sensor, sensor_I_microamps_70, marker = "o", label = "Sensor Tile", color = "red")
  plt.errorbar(hybrid_V_70, hybrid_I_microamps_70, fmt = "o", label = "Hybrid", yerr = I_error_70, color = "blue")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("20UPGB42000070", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()
  
def IVcompare_71(V_bias_sensor, sensor_I_microamps_71, hybrid_V_71, hybrid_I_microamps_71, I_error_71):  
  plt.scatter(V_bias_sensor, sensor_I_microamps_71, marker = "o", label = "Sensor Tile", color = "red")
  plt.errorbar(hybrid_V_71, hybrid_I_microamps_71, fmt = "o", label = "Hybrid", yerr = I_error_71, color = "blue")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("20UPGB42000071", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()
  
def IVcompare_72(V_bias_sensor, sensor_I_microamps_72, hybrid_V_72, hybrid_I_microamps_72, I_error_72):
  plt.scatter(V_bias_sensor, sensor_I_microamps_72, marker = "o", label = "Sensor Tile", color = "red")
  plt.errorbar(hybrid_V_72, hybrid_I_microamps_72, fmt = "o", label = "Hybrid", yerr = I_error_72, color = "blue")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("20UPGB42000072", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()
  
def IVcompare_73(V_bias_sensor, sensor_I_microamps_73, hybrid_V_73, hybrid_I_microamps_73):
  plt.scatter(V_bias_sensor, sensor_I_microamps_73, marker = "o", label = "Sensor Tile", color = "red")
  plt.scatter(hybrid_V_73, hybrid_I_microamps_73, marker = "o", label = "Hybrid", color = "blue")
  plt.xlabel("Bias Voltage (V)", fontsize = 16)
  plt.ylabel("Leakage Current (microA)", fontsize = 16)
  plt.title("20UPGB42000073", fontsize = 18)
  plt.legend(loc = "lower right", fontsize = 16)
  plt.show()

def check_units_70(V_bias_sensor, sensor_check_units_70, hybrid_V_70, hybrid_I_microamps_70):
  plt.scatter(V_bias_sensor, sensor_check_units_70, marker = "o", label = "Sensor Data / 10")
  plt.scatter(hybrid_V_70, hybrid_I_microamps_70, marker = "o", label = "Hybrid")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current - Checking Units", fontsize = 20)
  plt.title("BM 70 - Checking Wafer IV Units", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

def check_units_71(V_bias_sensor, sensor_check_units_71, hybrid_V_71, hybrid_I_microamps_71):
  plt.scatter(V_bias_sensor, sensor_check_units_71, marker = "o", label = "Sensor Data / 10")
  plt.scatter(hybrid_V_71, hybrid_I_microamps_71, marker = "o", label = "Hybrid")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current - Checking Units", fontsize = 20)
  plt.title("BM 71 - Checking Wafer IV Units", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

def check_units_72(V_bias_sensor, sensor_check_units_72, hybrid_V_72, hybrid_I_microamps_72):
  plt.scatter(V_bias_sensor, sensor_check_units_72, marker = "o", label = "Sensor Data / 10")
  plt.scatter(hybrid_V_72, hybrid_I_microamps_72, marker = "o", label = "Hybrid")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current - Checking Units", fontsize = 20)
  plt.title("BM 72 - Checking Wafer IV Units", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

def check_units_73(V_bias_sensor, sensor_check_units_73, hybrid_V_73, hybrid_I_microamps_73):
  plt.scatter(V_bias_sensor, sensor_check_units_73, marker = "o", label = "Sensor Data / 10")
  plt.scatter(hybrid_V_73, hybrid_I_microamps_73, marker = "o", label = "Hybrid")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current - Checking Units", fontsize = 20)
  plt.title("BM 73 - Checking Wafer IV Units", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()


def four_BMs(hybrid_V_70, hybrid_V_71, hybrid_V_72, hybrid_V_73, hybrid_I_microamps_70, hybrid_I_microamps_71, hybrid_I_microamps_72, hybrid_I_microamps_73, I_error_70, I_error_71, I_error_72):
  plt.errorbar(hybrid_V_70, hybrid_I_microamps_70, fmt = "o", label = "BM 70", yerr = I_error_70, color = "blue")
  plt.errorbar(hybrid_V_71, hybrid_I_microamps_71, fmt = "o", label = "BM 71", yerr = I_error_71, color = "green")
  plt.errorbar(hybrid_V_72, hybrid_I_microamps_72, fmt = "o", label = "BM 72", yerr = I_error_72, color = "red")
  plt.scatter(hybrid_V_73, hybrid_I_microamps_73, marker = "o", label = "BM 73", color = "orange")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("Comparing Four BMs", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

def three_BMs(hybrid_V_70, hybrid_V_71, hybrid_V_72, hybrid_I_microamps_70, hybrid_I_microamps_71, hybrid_I_microamps_72, I_error_70, I_error_71, I_error_72):
  plt.errorbar(hybrid_V_70, hybrid_I_microamps_70, fmt = "o", label = "BM 70", yerr = I_error_70, color = "blue")
  plt.errorbar(hybrid_V_71, hybrid_I_microamps_71, fmt = "o", label = "BM 71", yerr = I_error_71, color = "green")
  plt.errorbar(hybrid_V_72, hybrid_I_microamps_72, fmt = "o", label = "BM 72", yerr = I_error_72, color = "red")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("Comparing Three BMs", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

def breakdown_comparison(hybrid_V_68, hybrid_V_70, hybrid_I_microamps_68, hybrid_I_microamps_70):
  plt.scatter(hybrid_V_68, hybrid_I_microamps_68, marker = "o", label = "BM 68", color = "blue")
  plt.scatter(hybrid_V_70, hybrid_I_microamps_70, marker = "o", label = "BM 70", color = "red")
  plt.xlabel("Bias Voltage (V)", fontsize = 20)
  plt.ylabel("Leakage Current (microA)", fontsize = 20)
  plt.title("Breakdown vs No Breakdown", fontsize = 24)
  plt.legend(loc = "lower right", fontsize = 18)
  plt.show()

if __name__ == "__main__":
  main()
  
  
