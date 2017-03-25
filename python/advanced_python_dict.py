import csv
import re
def get_list(filename):
    f=open(filename,'r')
    faclistcsv=csv.reader(f)
    faclist=list(faclistcsv)
    f.close()
    return faclist

def get_last_name(fullname):
    #Finds last name in a full name string
    matchobject=re.search('\w+$',fullname)
    lastname=fullname[matchobject.start():matchobject.end()]
    return lastname

def get_first_name(fullname):
    matchobject=re.search('^\w+',fullname)
    firstname=fullname[matchobject.start():matchobject.end()]
    return firstname

def get_info(person):
    info=[]
    fulltitle=person[2]
    fulldegrees=person[1]
    email=person[3]
    degrees=''
    #Get number of degrees: count whitespace
    sloplist=re.findall('[A-Z][a-z]?\.?[A-Z]\.?[A-Z]?[a-z]?\.?',fulldegrees)
    for slop in sloplist:
        #Build string with periods
        match=re.search('[A-Z][a-z]?\.?',slop)
        abbrev=slop[match.start():match.end()]
        if abbrev[-1]!='.':
            abbrev+='.'
        match2=re.search('[A-Z]\.?',slop[match.end():])
        abbrev2=slop[match2.start()+match.end():match2.end()+match.end()]
        if abbrev2[-1]!='.':
            abbrev2+='.'
        match3=re.search('[A-Z][a-z]?\.?',slop[match2.end():])
        abbrev3=slop[match3.start()+match.end()+match2.end():match3.end()+match.end()+match2.end()]
        if abbrev3!='':    
            if abbrev3[-1]!='.':
                abbrev3+='.'
        degree=abbrev+abbrev2+abbrev3
        if degrees=='':
            degrees+=degree
        else:
            degrees+=', '+degree
    titleobject=re.search('\w*\s?Professor',fulltitle)
    title=fulltitle[titleobject.start():titleobject.end()]
    info.append(degrees)
    info.append(title)
    info.append(email)
    return info

def Q6(faclist):
    fac_dict={}
    for person in faclist[1:]:
        lastname=get_last_name(person[0])
        info=get_info(person)
        if lastname in fac_dict:
            fac_dict[lastname].append(info)
        else:
            fac_dict[lastname]=[info]
    return fac_dict

def Q7(faclist):
    fac_dict={}
    for person in faclist[1:]:
        firstname=get_first_name(person[0])
        lastname=get_last_name(person[0])
        info=get_info(person)
        key=(firstname,lastname)
        if key in fac_dict:
            fac_dict[key].append(info)
        else:
            fac_dict[key]=[info]
    return fac_dict

def Q8(faclist):
    fac_dict={}
    for person in faclist[1:]:
        firstname=get_first_name(person[0])
        lastname=get_last_name(person[0])
        info=get_info(person)
        key=(lastname,firstname)
        if key in fac_dict:
            fac_dict[key].append(info)
        else:
            fac_dict[key]=[info]
    return fac_dict