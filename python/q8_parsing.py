"""
The football.csv file contains the results from the English Premier League. 
The columns labeled Goals and Goals Allowed contain the total number of 
goals scored for and against each team in that season (so Arsenal scored 79 goals 
against opponents, and had 36 goals scored against them). Write a program to read the file, 
then print the name of the team with the smallest difference in for and against goals.
"""
import csv
import sys
def make_diff_dict(filename):
    f=open(filename,'r')
    scorelist=csv.reader(f)
    rows=list(scorelist)
    f.close()
    #Make dictionary of teams and difference between for and against goals
    diff_dict={}
    for row in rows[1::]:
        diff_dict[int(row[5])-int(row[6])]=row[0]
    return diff_dict

def print_differences(filename):
    diff_dict=make_diff_dict(filename)
    print 'Most negative difference: '+diff_dict[min(diff_dict)]+', '+str(min(diff_dict))
    print 'Smallest absolute difference: ',
    abs_dict={}
    for key in diff_dict:
        abs_dict[abs(key)]=diff_dict[key]
    print abs_dict[min(abs_dict)]+', '+str(min(abs_dict))
    
