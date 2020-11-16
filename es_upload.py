import os
from elasticsearch import Elasticsearch,helpers
import pandas as pd
import csv
import numpy as np
es=Elasticsearch([{'host':'localhost','port':9200}])
location='../../archive/TelevisionNews/'
for file1 in os.listdir(location):
    with open(location, encoding='utf8') as f:
        df = pd.read_csv(location)
        filename=file1.replace('.','')
        print(filename)
        for i in range(len(df)):
            print(i)
            for key in df.iloc[i].keys():
                #print(type(key))
                if pd.isnull(df.iloc[i][key]):
                    df.iloc[i][key]=''
            x=dict(df.iloc[i])
            x['doc_name']=filename
            x['row_no']=i
            es.index(index='archive',doc_type='snippet',id=filename+"_"+str(i),body=x)