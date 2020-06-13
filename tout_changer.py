from glob import glob
from os.path import isdir,isfile
import base64
import webbrowser
def all_files(path,ext):
    r=[]
    for x in glob(path+"/*"):
        if x.endswith("."+ext) and isfile(x):
            r.append(x)
        elif isdir(x):
            r+=all_files(x,ext)
    return r
def search_balise(ctn,balise,class_):
    r=[]
    balise=balise.encode()
    class_=class_.encode()
    k=ctn.find(b"<"+balise)
    while k!=-1:
        start=k
        end=ctn.find(b">",start)
        balise=ctn[start:end]
        if class_==b"":
            r.append((start,end))
            k=ctn.find(b"<"+balise,k+1)
            continue
        class_pos=balise.find(b"class=\"")
        if class_pos!=-1:
            start=class_pos+7
            end=balise.find(b'"',start)
            if class_ in balise[start:end].split():
                r.append((start,end))
        k=ctn.find(b"<"+balise,k+1)
    return r
for x in all_files(".","html"):
    with open(x,"rb")as f:
        ctn=f.read()     
#titres en h1
    k=len(search_balise(ctn,"h1","")),len(search_balise(ctn,"h2",""))
    if k==(0,0):
        continue
    elif k==(0,1):
        title=search_balise(ctn,"h2","")
    else:
        title=search_balise(ctn,"h1","")
    [(start,end)]=title
    end=list(ctn[start:start+3])
    end.insert(1,47)
    end.append(62)
    end=bytes(end)
    end=ctn.find(end,start)+len(end)
    title=ctn[start:end]
    title=title[title.find(b">")+1:title.find(b"<",3)]
    title=b"<h1 class=\"uk-heading-large\">"+title+b"</h1>"
    title=list(title)
    ctn=list(ctn)
    ctn[start:end]=title
    ctn=bytes(ctn)
    with open(x,"wb")as f:
        f.write(ctn)
#actualit&eacute;s navbar mobile + normale
