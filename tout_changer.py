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
    ##########################################
    #### modifications de chaque page ici ####
    ##########################################
    if ctn.count(b"dataLayer")!=0:
        continue
    ctn=ctn.replace(b"</head>",b"""    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }

        gtag('js', new Date());

        gtag('config', 'UA-166072477-1');
    </script>
</head>""")
    with open(x,"wb")as f:
        f.write(ctn)
