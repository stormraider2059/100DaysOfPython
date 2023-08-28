import os
class clearClutter:
    def __makeDir(self):
        if(not os.path.exists("./clutter")):
            os.mkdir("./clutter")
        else:
            print("Directory already exists")
    def __makeSubFolder(self):
        os.mkdir("./clutter/clutterFiles")
    def __makeFile(self):
        if(os.path.exists("./clutter/clutterFiles")):
            ext1="pdf"
            f=open(f"./clutter/clutterFiles/libra.{ext1}","w")
            f=open(f"./clutter/clutterFiles/virgo.{ext1}","w")
            f=open(f"./clutter/clutterFiles/leo.{ext1}","w")
            f=open(f"./clutter/clutterFiles/cancer.{ext1}","w")
            f=open(f"./clutter/clutterFiles/gemini.{ext1}","w")
            f=open(f"./clutter/clutterFiles/taurus.{ext1}","w")
            f=open(f"./clutter/clutterFiles/aries.{ext1}","w")
            f=open(f"./clutter/clutterFiles/pisces.{ext1}","w")
            f=open(f"./clutter/clutterFiles/aquarius.{ext1}","w")
            f=open(f"./clutter/clutterFiles/capricorn.{ext1}","w")
            f=open(f"./clutter/clutterFiles/sagittarius.{ext1}","w")
            f=open(f"./clutter/clutterFiles/scorpio.{ext1}","w")          
    def __getExtension(self,fileExt):   
        def __renameFiles():
            i=1 
            for fileName in os.listdir("./clutter/clutterFiles"):
                if fileName.endswith(fileExt):      
                    os.rename(f"./clutter/clutterFiles/{fileName}",f"./clutter/clutterFiles/{i}.{fileExt}")
                    i+=1               
        __renameFiles()
                  
clt=clearClutter()
clt._clearClutter__makeDir()
clt._clearClutter__makeSubFolder()
clt._clearClutter__makeFile()
clt._clearClutter__getExtension("pdf")