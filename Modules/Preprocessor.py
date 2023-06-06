import platform
import configparser
from time import strftime
import os
from pathlib import Path
import pandas as pd
import sys
import json
from datetime import datetime

class Preprocessor:
    def __init__(self, cwd, jsonname = "params.json"):
        if(sys.argv[0] == "__main__.py") or ( cwd != os.getcwd()):
            self.data_path = os.path.abspath(os.path.join(cwd,r'Data'))
            self.result_path = os.path.abspath(os.path.join(cwd,r'Results'))
        else:
            self.data_path = os.path.abspath(os.path.join(cwd.split("Preprocessor")[0],r"Preprocessor",r'Data'))
            self.result_path = os.path.abspath(os.path.join(cwd.split("Preprocessor")[0],r"Preprocessor",r'Results'))
        self.jsonname = jsonname
        self.filename = ""
        self.data = ""
        self.resultdata = pd.DataFrame()
        self.jsondata = ""

        
        pd.set_option('max_colwidth', 4000)
        return

    def setFilename(self,data):
        self.filename = data

    def openFile(self,encode='cp949'):
        if(self.filename.split(".")[-1] == "csv"):
            self.data = pd.read_csv(os.path.join(self.data_path,self.filename), encoding=encode)
        with open(os.path.join(self.data_path,self.jsonname), "r") as st_json:
            self.jsondata = json.load(st_json, encoding=encode)
        
    def selectParams(self):
        column_list = list(self.jsondata.keys())
        self.data = self.data[self.data.columns.intersection(column_list)]

    def append_result(self,columnname):
        self.resultdata = pd.concat([self.resultdata,self.data[columnname]])


    def column_list_get(self,columnname,jsonparams):
        name = jsonparams['name']
        data = jsonparams['data']
        exchange = jsonparams['exchange']
        exchangekeys = list(exchange.keys())
        option = jsonparams['option']

        for idx, row in self.data.iterrows():
            checkdata = row[columnname]
            found = False
            for keyword in data:
                if keyword in checkdata:
                    self.resultdata.at[idx,name] = keyword
                    found = True
                    break
            if not found:
                for keyword in exchangekeys:
                    if keyword in checkdata:
                        self.resultdata.at[idx,name] = exchange[keyword]
                        found = True
                        break
            
            if option == "delete" and not found:
                self.resultdata.at[idx,name] = ""
            
    def column_date_get(self,columnname,jsonparams):
        name = jsonparams['name']
        param = jsonparams['data']
        dateformat = jsonparams['format']
        self.resultdata[name] = self.data[columnname]
        for idx, row in self.resultdata.iterrows():
            checkdata = row[name].strip()
            if param == "m":
                self.resultdata.at[idx,name] = datetime.strptime(checkdata, dateformat).month
            if param == "H":
                self.resultdata.at[idx,name] = datetime.strptime(checkdata, dateformat).hour

        # if param == "m":
        #     self.result[name] = self.data[columnname].dt.month
        # if param == "H":
        #     self.result[name] = self.data[columnname].dt.hour
        
        if not (jsonparams.get('exchange')) is None:
            exchange = jsonparams['exchange']
            exchangekeys = list(exchange.keys())
            for idx, row in self.resultdata.iterrows():
                checkdata = str(row[name])
                if checkdata in exchangekeys:
                    self.resultdata.at[idx,name] = exchange[checkdata]

    def handle_params(self):
        jsonlist = list(self.jsondata.keys())
        for param in jsonlist:
            param_key = list(self.jsondata[param].keys())[0]
            param_list = self.jsondata[param][param_key]
            if param_key == "list_get":
                for param_data in param_list:
                    self.column_list_get(param,param_data)
            if param_key == "date_get":
                for param_data in param_list:
                    self.column_date_get(param,param_data)


    def checkList(self, column):
        collist = []
        for idx, row in self.data.iterrows():
            data = row[column].split(" ")[0]
            if(not data in collist):
                collist.append(data)
        print(collist)

