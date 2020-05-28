import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

#sensibilità
mtr_sens = [
    [86,29],
    [275, 438]
]

mtr_topic = [
    [7, 1, 0, 2, 0],
    [2, 133, 6, 15, 1],
    [0, 3, 22, 19, 0],
    [0, 1, 2, 65, 2],
    [47, 122, 66, 265, 46]
]

def plot_conf(mtr, lbl, path):
    df_cm = pd.DataFrame(mtr, lbl, lbl)
    sn.set(font_scale=1.4)
    sn.heatmap(df_cm, annot = True, annot_kws = {"size":8}, fmt = "g")
    plt.savefig(path)
    #plt.show()

server = pd.read_csv("server.csv", sep=';', skiprows = 1, names = ["ram", "time", "cpu"])
cpu_server = server.cpu.tolist()
ram_server = server.ram.tolist()
time_server = server.time.tolist()

cpu_client  = pd.read_csv("cpu.csv", sep=";", names = ["chrome","knoxly","scheda","totale"], usecols = ["totale"])
cpu_client = cpu_client.totale.tolist()

ram_client = pd.read_csv("memory.csv", sep=";", names = ["chrome","knoxly","scheda","totale"], usecols = ["totale"])
ram_client = ram_client.totale.tolist()

x = np.sort(cpu_server)
y = np.arange(1, len(cpu_server)+1 / float(len(cpu_server)))
_ = plt.plot(np.sort(cpu_server),y, marker = '|', linestyle = 'none')
_ = plt.plot(np.sort(ram_server),y, marker = '|', linestyle = 'none')
_ = plt.plot(np.sort(time_server),y, marker = '|', linestyle = 'none')

_ = plt.plot(np.sort(cpu_client),y, marker = '|', linestyle = 'none')
_ = plt.plot(np.sort(ram_client),y, marker = '|', linestyle = 'none')
_ = plt.xlabel('performance')
_ = plt.ylabel('# frasi esaminate')
plt.margins(0.02)
plt.show()
plt.savefig('cummultavie_graph.png')


plot_conf(mtr_sens, ["sensibile", "non sensibile"], "sens.png")
plot_conf(mtr_topic, ["politics", "health", "job", "travel", "general"], "topic.png")