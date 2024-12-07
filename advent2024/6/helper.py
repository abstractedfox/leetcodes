import re
#get input
def gi():
    lines = open("input.txt", "r").readlines()
    for i in range(0, len(lines)):
        if lines[i][-1] == "\n":
            lines[i]=lines[i][0:-1]
    if lines[-1] == '\n' or lines[-1]=='' or lines[-1]==[]:
        lines=lines[0:-1]
   
    return lines

#rowcol
def rc(arr, r, c):
    return arr[r][c]

#join a list of characters into a string
def jn2str(arr):
    out=""
    for c in arr:
        out+=c
    return out

#inline documentation!!! let's make sure the reverse one works i don't think it does
def diag(arr, startrow, startcol, l, r=0):
    out=[]
    if r==1:
        for i in range(0, l):
            out.append(arr[startrow+l+i][startcol+l+i])
    for i in range(0, l):
        out.append(arr[startrow+i][startcol+i])
    if type(arr[0]) == type("a"):
        out=jn2str(out)
    return out

def do(collection, func):
    out=[x for x in collection]
    for i in rg(out):
        out[i]=func(out[i])
    return out

def every(collection, func):
    for i in collection:
        if not func(i):
            return False

def repl(string,char,num):
    return string[0:num]+char+string[num+1:]

#deep copy
def dcp(arr): 
    out = []
    for x in arr:
        if type(x) == type([]):
            out.append(dcp(x))
        else:
            out.append(x)
    return out

#'get columns' (formatted as rows)
def gcols(arr, split = None):
    out = []
    if split is None:
        for i in range(0, len(arr[0])):
            out.append([x[i] for x in arr])
    else:
        if type(split) == str:
            for i in range(0, len(arr[0].split(split))):
                out.append([x.split(split)[i] for x in arr])
        else: 
            for i in range(0, len(arr[0].split())):
                out.append([x.split()[i] for x in arr])
    return out

#cast an entire array to int
def toint(arr):
    return [int(x) for x in arr]

#ordinal boundary
#by default, behaves as 'return only numbers from the input'
    #spt = split using default behavior
    #jn = join subsequent numbers (ie "1234 5 6" should be [1234, 5, 6] not [1, 2, 3, 4, 5, 6])
    #toi = cast result to int list
def ordb(string: str, kws:list, s = ord("0"), e=ord("9")):
    out = []
    if spt in kws:
        out = string.split()
    elif jn in kws:
        joined = ""
        for c in string:
            if ord(c) >= s and ord(c) <= e:
                joined += c
            else:
                joined += " "
        out = joined.split()
    else:
        out = [x for x in string if ord(x) >= s and ord(x) <= e]
    if toi in kws:
        out = [int(x) for x in out]
    return out
    

def rg(arr):
    return range(0, len(arr))

#for posterity:
    #we will assume every line of input is represented as a string in an array
toi = 0 #to int
spt = 1 #split
jn = 2 #join
class Array:
    #cspt = custom split delineator if needed other than the default one
    def __init__(self, kws =  [], cspt = None, inp = None):
        if inp is not None:
            self.inp = inp 
        else:
            self.inp = gi()
    
    def parse_kws(self):
        #processing order:
            #split, cast
        if toi in kws:
            #take only numbers from this line
            pass

    def __getitem__(self, key):
        return self.inp[key]

    #get column
    def gcol(self, col, mkstr = True):
        out = []
        for r in self.inp:
            out.append(r[col])
        if mkstr:
            outstr = ""
            for c in out:
                outstr += c
            return outstr

        return out

    #set an entire column
    def scol(self, newcontents, col):
        for i in range(0, len(newcontents)):
            self.inp[i] = self.inp[i][0:col] + newcontents[i] + self.inp[i][col + 1:]

    #set an individual cell, overflow will overwrite next cells
    #unless insert, then 'val' inserted AT 'col' with current value of 'col' and subsequent vals pushed after it
    def scel(self, val, row, col, insert = False):
        if not insert:
            self.inp[row] = self.inp[row][0:col] + val + self.inp[row][col+len(val):]

        else:
            self.inp[row] = self.inp[row][0:col] + val + self.inp[row][col:]

    def __len__(self):
        return self.inp.__len__()

def strtoarr(string):
    return [x for x in string]

#generate a dictionary where keys are items in 'arr' and default values are 'dval', if 'ct' then vals are number of occurrences  
def gendict(arr, dval = None, ct = False):
    out = {}
    for val in arr:
        if ct:
            if val not in out:
                out[val] = 1
            else:
                out[val] += 1
            continue
        out[val] = dval

    return out
        
