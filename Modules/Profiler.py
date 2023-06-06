import pandas as pd
# import pandas_profiling
import ydata_profiling
import os
from pathlib import Path

class Profiler:
    def __init__(self,dir = "", filename = ""):
        self.dir = dir
        self.resultdir = ""
        self.filename = filename
        if (self.dir == ""):
            self.dir = os.getcwd()
            if(self.dir[-12:] == "Preprocessor"):
                self.dir = os.path.abspath(os.path.join(self.dir,"Data"))
                self.resultdir = "Results"
            elif(self.dir[-7:] == "Modules"):
                self.dir = os.path.abspath(os.path.join(self.dir,"..","Data"))
                self.resultdir = os.path.abspath(os.path.join("..","Results"))
        

    def set_file(self,filename):
        self.filename = filename
    
    def profile(self,resultname, filename = ""):
        if(filename == ""):
            if(self.filename == ""):
                return
            filename = self.filename
            print(filename)

        pddata = pd.read_csv(os.path.join(self.dir,filename),encoding='cp949')
        pr = pddata.profile_report()

        if(resultname == "same"):
            resultname = filename.split('.')[0].replace(" ","") + ".html"
            # print(resultname)
        pr.to_file(os.path.join(self.resultdir,resultname))
        # pr.to_file("Results/report.html")

