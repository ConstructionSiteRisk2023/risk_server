import platform
import os
import pandas as pd
import numpy as np
import sys
# import ydata_profiling
import matplotlib.pyplot as plt
import math
from datetime import datetime

filename = '20221118_cid_nodrop.csv'
filepath = os.path.abspath(os.path.join(os.getcwd(),r'Results',filename))
plt.rc('font', family='Malgun Gothic')