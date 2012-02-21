import os
import glob

def get_fnames(datadir):
    os.chdir(datadir)
    flist=glob.glob('*.txt')
    return flist

def isSexN(datafile):
    file=open(datafile)
    linelist=file.readlines()
    i=0
    while i < len(linelist):
        if linelist[i] == "Sex: N\n":
            print datafile+' has an N entry'
            return True
        i+=1
    return False
    
isSexN('cleaneddata/jamesm_data_475.txt')

'''
def chSexNM(datafile):
    file=open(datafile,'w')
    linelist=file.readlines()
    

    
     
files=get_fnames('cleaneddata')
'''
