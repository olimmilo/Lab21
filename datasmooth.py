import csv
#import numpy

"""
Experiment vars which could be input but are just written into the code are defined at the top in all caps

smoothing function was provided in the scipy numpy handbook and is not my own work
"""

##Experiment vars
DATALEN=180
INTERVALS=[1,1,10,10,10,10]
TRUELEN=[180,180,1800,1800,1800,1800]

##defines functions

def smooth(list,degree=6):
    """
    return(list)

    window=degree*2-1

    weight=numpy.array([1.0]*window)

    weightGauss=[]

    for i in range(window):
        i=i-degree+1
        frac=i/float(window)
        gauss=1/(numpy.exp((4*(frac))**2))
        weightGauss.append(gauss)

    weight=numpy.array(weightGauss)*weight
    smoothed=[0.0]*(len(list)-window)

    for i in range(len(smoothed)):
        smoothed[i]=sum(numpy.array(list[i:i+window])*weight)/sum(weight)

    return(smoothed)
    """
    return(list)


def sum(list):
    i = 0
    s = 0
    while i < len(list):
        s += list[i]
        i += 1
    return(s)


def mean(list):
    i = 0
    s = sum(list)
    mean = s/len(list)
    return(mean)


def LinReg(list,start,interval):
    y=list
    x=[]
    while len(x) < len(y):
        x.append((len(x)*interval)+start)
    xy=[n*m for n,m in zip(x,y)]
    x2=[j**2 for j in x]
    n=len(list)
    m=((n*sum(xy))-(sum(x)*sum(y)))/((n*sum(x2))-(sum(x)**2))
    b=((sum(y)*sum(x2))-(sum(x)*sum(xy)))/((n*sum(x2))-(sum(x)**2))
    ans=[m,b]
    return(ans)


def LineInt(lin1, lin2):
	m=lin1[0]
	b=lin1[1]
	n=lin2[0]
	c=lin2[1]
	y=((n*b)-(m*c))/(n-m)
	x=(y-c)/n
	intersect=[x,y]
	return(intersect)


def convert(iteration):
    name="trial"+str(iteration)+".txt"
    functrial=open(name).readlines()
    funclist=functrial
    return(funclist)

def average(set1,set2,iter1,iter2):
    int1=INTERVALS[iter1]
    int2=INTERVALS[iter2]
    truelen1=TRUELEN[iter1]
    truelen2=TRUELEN[iter2]
    finlen=180
    pre1=[]
    pre2=[]
    i=0
    while i < len(set1):
        n=0
        vallist=[]
        while n < (trulen1/finlen):
            setiter=i+n
            vallist.append(set1(setiter))
            n += 1
        value=mean(vallist)
        pre1.append(value)
        i += int1
    i=0
    while i < len(set2):
        n=0
        vallist=[]
        while n < (trulen2/finlen):
            setiter=i+n
            vallist.append(set2(setiter))
            n += 1
        value=mean(vallist)
        pre2.append(value)
        i += int1
    finset=[]
    i=0
    while i < finlen:
        value= (pre1[i]+pre2[2])/2
        finset.append(value)
        i += 1
    
    ##sets the data sets to thier given size, then averges the two
    return(finset)

def finish(m,table):
    i=0
    ##unite all three trials into one per row
    return(avglist)
##creates smoothed data sets

rawtrials=[]
    
i=0
while i < 6:
    it = i + 1
    rawtrials.append(convert(it))
    i += 1

smoothtrials=[]

i=0
while i < len(rawtrials):
    smoothtrials.append(smooth(rawtrials[i]))
    i += 1

##preforms calculations
avtable=[]

i=0
while i < 6:
    avtable.append(average(smoothtrials[i],smoothtrials[i+1],i,(i+1)))
    i += 2
i=0

    
fintable=[]

i=0
while i < DATALEN:
    fintable.append(finish(i,avtable))
    i += 1

i=0
i=0

with open('smoothedrec.csv','w') as printfile:
    writer = csv.writer(printfile)
    writer.writerows(fintable)
