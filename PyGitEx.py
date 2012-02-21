import os
import glob

datadir='cleaneddata'
def get_fnames(datadir):
    os.chdir(datadir)
    flist=glob.glob('*.txt')
    print flist
