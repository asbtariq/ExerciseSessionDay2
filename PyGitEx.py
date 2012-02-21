import os
import glob

def get_fnames(datadir):
    os.chdir(datadir)
    flist=glob.glob('*.txt')
    return flist

files=get_fnames('cleaneddata')

def getSexData(datafile):
    os.system('grep Sex '+datafile)
     
'''
for fname in files:
    getSexData('THOMAS_0464.txt')
    os.system('grep -c N *')
'''
