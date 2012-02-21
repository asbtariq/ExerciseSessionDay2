import os
import glob

def get_fnames(datadir):
    os.chdir(datadir)
    flist=glob.glob('*.txt')
    print flist

get_fnames('cleaneddata')


