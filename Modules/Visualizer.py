import platform
import os
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import math
from datetime import datetime


class Visualizer:
    def __init__(self,filename):
        self.filename = filename
        self.filepath = os.path.abspath(os.path.join(os.getcwd(),r'risk_server',r'Data',filename))
        # self.filepath = os.path.abspath(os.path.join(os.getcwd(),r'Data',filename))
        plt.rcParams["font.family"] = 'NanumGothicCoding'
        mpl.rcParams['axes.unicode_minus'] = False
        
        self.data = pd.read_csv(self.filepath,index_col=0,encoding='cp949')
    
    def select_data(self, params):
        temp = self.data
        for idx in params.keys():
            dest = params[idx]
            # print(type(temp[idx][0]))
            if (pd.api.types.is_float_dtype(temp.dtypes[idx])):
                dest = float(dest)
            elif (pd.api.types.is_integer_dtype(temp.dtypes[idx])):
                dest = int(dest)
            else:
                dest = str(dest)
            temp = temp.loc[temp[idx] == dest]
        return temp
    
    def save_graph(self,pddata,xparam):
        temp = pddata[xparam].value_counts().sort_index().to_frame()
        temp.plot(kind='bar')
        plt.savefig(f'./risk_server/Data/temp.jpg', dpi=300)
        return

