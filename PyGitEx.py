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
        print 'on line ',i
        if linelist[i] == "Sex: N\n":
            print 'This file has an N entry'
            return True
        i+=1
    print 'No N found'
    return False

def chSexNM(datafile):
    filetext = open(datafile).read()
    print 'Changing N to M in '+datafile
    filetext=filetext.replace(': N',': M')
    chdatafile = open(datafile,'w')
    chdatafile.write(filetext)
    chdatafile.close()
    print 'done!'

datadir='cleaneddata'
filelist = get_fnames(datadir)
nch=0
for f in filelist:
    print 'in '+f
    if isSexN(f): 
        chSexNM(f)
        nch+=1
print 'Finished: made '+str(nch)+' changes!'

