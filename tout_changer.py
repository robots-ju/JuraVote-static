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
for x in all_files(".","html"):
    with open(x,"rb")as f:
        ctn=f.read()     
#actualit&eacute;s navbar mobile + normale
    m_start=ctn.find(b"""<div id="menu-mobile" uk-offcanvas>""")
    if m_start==-1:
        continue
    end=ctn.find(b"</div>",ctn.find(b"</div>",m_start)+1)
    part=ctn[m_start:end]
    start=part.find(b"""07Instances/accueilI.html">Instances polit""")
    i=1
    while part[start-3*i]==46:
        i+=1
    i-=1
    start=part.find(b"</li>",start)
    start=part.find(b"\n",start)
    start+=1
    old=start
    start=part.find(b"\n",start)
    indent=b"\n"+part[old:start-1]
    new=b"""<li id="Actualites">
####    <a class="uk-button uk-button-text" href=\""""+b"../"*i+b"""09Actualites/Actualites.html">Actualit&eaccute;s politiques</a>
####</li>"""
    with open(x,"wb")as f:
        f.write(ctn[:m_start+start-1]+new.replace(b"####",indent)+ctn[m_start+start-1:])
