import csv
import re
def getlist(filename):
    f=open(filename,'r')
    faclistcsv=csv.reader(f)
    faclist=list(faclistcsv)
    f.close()
    return faclist


def make_fac_dict(faclist):
    #Make strings --allows searching with regex
    fac_dict={}
    names,degrees,titles,emails='','','',''
    for person in faclist[1:]:
        names+=person[0]+' '
        degrees+=person[1]+' '
        titles+=person[2]+' '
        emails+=person[3]+' '
    fac_dict['names'],fac_dict['degrees'],fac_dict['titles'],fac_dict['emails']=names,degrees,titles,emails
    return fac_dict
    
def Q1(fac_dict):
    degrees=fac_dict['degrees']
    ndegrees={}  
    uniqdegrees=set(re.findall('\w\.?\w\.?\w?\.?\w?\.?\s',degrees))
    for deg1 in uniqdegrees:
        #change periods to correct format for regex
        deg1mod=''
        for char in deg1:
            if char!='.':
                deg1mod+=char
            else:
                deg1mod+='\.'
        degreecount=re.findall(deg1mod,degrees)
        ndegrees[deg1]=len(degreecount)
    return ndegrees

def Q2(fac_dict):
    titles=fac_dict['titles']
    ntitles={}
    uniqtitles=set(re.findall('.{10}Professor',titles))
    for title in uniqtitles:
        titlecount=re.findall(title,titles)
        ntitles[title]=len(titlecount)
    return ntitles

def Q3(faclist):
    emaillist=[]
    for person in faclist[1:]:
        emaillist.append(person[3])
    return emaillist

def Q4(fac_dict):
    emails=fac_dict['emails']
    ndomains={}
    uniqdomains=set(re.findall('@.{0,15}\.edu',emails))
    for email in uniqdomains:
        emailcount=re.findall(email,emails)
        ndomains[email]=len(emailcount)
    return ndomains
        
    
    