
from matplotlib import lines
import pandas as pd
import json
import os



intel_versions = ['I3', 'I5', 'I7', 'I9']
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
root_path = os.environ['CUSTOMPC_HOME']
filepath = root_path+"/jsonFiles/rawdata_processors.json"
df = pd.read_json(filepath, lines=True)
processorNames = df['processorName'].str.upper()
processorPrice = df['processorPrice'].str.upper()
sites = df['site'].str.upper()
index = 0
processorsDict = {}

skip_words = ["PENTIUM","GEFORCE","HDD"]

def populateProcessorDict(df, index, processorsDict, modelId,):
    site = df['site'][index]
    price = df['processorPrice'][index]
    priceList = [0,0,0,0,0]
    if modelId in processorsDict.keys():
        priceList = processorsDict[modelId]
    if site == "MDComputers":
        priceList[0] = price
    elif site == "PCShop":
        priceList[1] = price
    elif site == "ThinkPC":
        priceList[2] = price
    elif site == "Vedant":
        priceList[3] = price
    elif site == "TPSTech":
        priceList[4] = price
    
    processorsDict[modelId] = priceList
    return

def irregularData(index, code):
    name = processorNames[index]
    skip = False
    for word in skip_words:
        if word in name:
            skip= True
            break
    if not skip:
        print(code+" : "+sites[index]+" : "+name+" : "+processorPrice[index])
    pass



def cleanName(name):
    name = name.replace("-", " ")
    name = name.replace("CORES", "CORE")
    name = name.replace(" 10TH GEN","")
    name = name.replace(" 11TH GEN","")
    name = name.replace(" 12TH GEN","")
    name = ''.join([i if ord(i) < 128 else '' for i in name])
    # print(name)
    return name

for name in processorNames:
    price = df['processorPrice'][index]
    if "INTEL" in name:
        if name is not None and price is not None:
            name = cleanName(name)
            before_keyword, keyword, after_keyword = name.partition("INTEL CORE ")
            version = after_keyword.split(" ")[:2]
            if len(version) ==2 and version[0] in intel_versions:
                modelId = "Intel Core "+version[0]+"-"+version[1]
                populateProcessorDict(df, index, processorsDict, modelId)
            else:
                print(name)
                print(version)
                irregularData(index, "0")
                 
        else:
           irregularData(index)
    elif "AMD" in name:
        if name is not None and price is not None:
            name = cleanName(name)
            before_keyword, keyword, after_keyword = name.partition("AMD RYZEN ")
            version = after_keyword.split(" ")[:2]
            if len(version) ==2 :
                modelId = "AMD RYZEN "+version[0]+"-"+version[1]
                populateProcessorDict(df, index, processorsDict, modelId)
            else:
                irregularData(index, "1")
        else:
            irregularData(index, "2")
    else:
        irregularData(index, "3")
    index += 1


print('{:<30}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}'.format('Processor', 'MDComputers', 'PCShop', "ThinkPC","Vedant","TPSTech"))
for k, v in processorsDict.items():
    a, b, c, d , e= v
    print('{:<30}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}'.format(k,a, b , c, d, e))

# Serializing json 
json_object = json.dumps(processorsDict, indent = 4)
# Writing to sample.json
with open(root_path+"/jsonFiles/final_processors.json", "w+") as outfile:
    outfile.write(json_object)