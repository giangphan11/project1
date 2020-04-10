def GhiFile(path,data):
    try:
        file = open(path, 'a', encoding='utf-8')
        file.writelines(data)
        file.writelines("\n")
        file.close()
    except:
        pass

def DocFile(path):
    arrData=[]
    try:
        file=open(path,'r',encoding='utf-8')
        for line in file:
            data=line.strip()
            arr=data.split(";")
            arrData.append(arr)
    except:
        pass
    return arrData
