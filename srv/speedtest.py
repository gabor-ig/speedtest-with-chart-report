# speedtest.py uses matplotlib to generate graphical reports from speedtest logs

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


speedtest = pd.read_table("/var/log/speedtest/speedtest.txt", parse_dates=True, usecols=['download','upload','timestamp'])

speedtest["download(Mbps)"]=speedtest["download"]/(1024*1024)*8
download_Mbps=speedtest["download(Mbps)"]

speedtest["upload(Mbps)"]=speedtest["upload"]/(1024*1024)*8
upload_Mbps=speedtest["upload(Mbps)"]

speedtest2=speedtest.drop(['download', 'upload'], axis=1)

axs = speedtest2.plot.area(figsize=(12, 4), subplots=True)
plt.savefig("/srv/speedtest/speedtest.png")
