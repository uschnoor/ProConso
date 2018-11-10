import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class plotter:
    def __init__(self):
        plt.ion()

    def scatterplot_onevariable(self,xpoints,ypoints, title):
        self.xpoints = np.array(xpoints)
        self.ypoints = np.array(ypoints)
        plt.scatter(self.xpoints, self.ypoints)
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        raw_input()

    def scatterplot_3groups(self,list1x, list1y,list2x, list2y,list3x, list3y, groups):
        g1x= np.array(list1x)
        g1y= np.array(list1y)
        g2x= np.array(list2x)
        g2y= np.array(list2y)
        g3x= np.array(list3x)
        g3y= np.array(list1y)
        colors = ("red", "green", "blue")
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
        g1 = (g1x, g1y)
        g2 = (g2x, g2y)
        g3 = (g3x, g3y)
        print g1
        data = (g1,g2,g3)
        for data, color, group in zip(data, colors, groups):
            x, y = data
            print x
            print y
            ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
        plt.show()
        plt.legend(loc=2)
        raw_input()
        return

    def pandaplot_3groups(self,listx,listy,listz,title,xlabel):
        gx= np.array(listx)
        gy= np.array(listy)
        gz= np.array(listz)
        
        colors = ("red", "green", "blue")

        df = pd.DataFrame(dict(x=gx, y=gy, label=gz))
        groups = df.groupby('label')
        fig, ax = plt.subplots()
        ax.margins(0.05)
        for name, group in groups:
            ax.plot(group.x, group.y, marker = 'o', linestyle='', alpha=0.8, ms=12, label=name)
        ax.legend()
        ax.set_ylabel("consommation [kWh]")
        ax.set_xlabel(xlabel)
        plt.title(title)
        raw_input()
        return


        #
#import pandas as pd
#np.random.seed(1974)
#
## Generate Data
#num = 20
#x, y = np.random.random((2, num))
#labels = np.random.choice(['a', 'b', 'c'], num)
#df = pd.DataFrame(dict(x=x, y=y, label=labels))
#
#groups = df.groupby('label')
#
## Plot
#fig, ax = plt.subplots()
#ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
#for name, group in groups:
#    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, label=name)
#ax.legend()
#
#plt.show()


    
#
## Create data
#N = 60
#g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
#g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
#g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))
# 
#data = (g1, g2, g3)
#colors = ("red", "green", "blue")
#groups = ("coffee", "tea", "water") 
# 
## Create plot
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
# 
#for data, color, group in zip(data, colors, groups):
#    x, y = data
#    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
# 
#plt.title('Matplot scatter plot')
#plt.legend(loc=2)
#plt.show()
#
