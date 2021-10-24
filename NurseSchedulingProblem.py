from GAProblem import GAProblem, Chromosome
import random

### we can represent the nurse scheduling problem as a matrix, with nurses on 
### the rows and shifts on the columns. A one in a cell in the matrix indicates
### that the nurse is scheduled for that shift, and a 0 indicates he/she is 
### not. 

### for example:
###      s1    s2    s3
###  n1  0      1     1
###  n2  1      0     0
###  n3  0      1     0

### we can encode this as the bitstring 011101110 

### We can use the regular BitStringProblem class to represent Nurse Scheduling problems. We 
### just need a factory that can produce appropriate fitness functions, given a set of constraints. 

def NurseFactory(contraints) :
    def f(chr) :
        return sum([constraint(chr)
               for constraint in constraints])
    return f


### Now we just need to build constraints that let us describe different schedules. Here's a couple to get you started.
### Let's assume three shifts per day, seven days per week, and three nurses. 
### This means our biststring is of length 3 * 7 * 3=63
numNurses = 3
numShifts = 3
numDays = 7

### a constraint: each nurse should work exactly 1 shift. 
def oneShiftEach(bitstring) :
    total = 0
    for i in range(numNurses) :
        total += bitstring[i:i+21].count('1') -1
    return total

### There should be exactly one nurse working each shift.
def oneNursePerShift(bitstring) :
    ### convert the bitstring into a list of lists, one per shift, with 
    shiftlist = getShifts(bitstring)
    return -1 * sum([abs(sum(shift) -1) for shift in shiftlist])

### return a list of lists, one for each nurse's schedule
def getShifts(bitstring) :
    nlist = []
    for i in range(numShifts) :
        shift = []
        for j in range(numNurses) :
            shift.append(bitstring[(j*numShifts) +i])
        nlist.append(shift)
    return nlist

