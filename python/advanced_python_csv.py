import csv
def write_emails(filein,fileout):
    f1=open(filein,'r')
    faclistcsv=csv.reader(f1)
    faclist=list(faclistcsv)
    f1.close()
    f2=open(fileout,'w')
    for fac in faclist[1:]:
        emailline=fac[3]+'\n' #Could add comma if needed
        f2.write(emailline)
    f2.close()