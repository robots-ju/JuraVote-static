from glob import glob
from os.path import isdir,isfile
def all_files(path,ext):
    r=[]
    for x in glob(path+"/*"):
        if x.endswith("."+ext) and isfile(x):
            r.append(x)
        elif isdir(x):
            r+=all_files(x,ext)
    return r
#lang="fr"
for x in all_files(".","html"):
    with open(x,"rb")as f:
        ctn=f.read()
    start=ctn.find(b"<html")
    end=ctn.find(b">",start)
    ctn_l=list(ctn)
    l=list(b'<html lang=\"fr\"')
    ctn_l[start:end]=l
    ctn=bytes(ctn_l)
    start=ctn.find(b"<html")
    end=ctn.find(b">",start)
    ctn_l=list(ctn)
    start=ctn.find(b"<html")
    end=ctn.find(b">",start)
    with open(x,"wb")as f:
        f.write(ctn)
#titres en h1
#actualit&eacute;s navbar mobile + normale
