import Elitism, Crossover,Selector, BitStringGAProblem, GA

# def allOnes(chr):
    #return len([x for x in chr.bitstring if x == '1'])

class MySolver(GA.GA, Elitism.DeterministicElites, Crossover.OnePointStringCrossover, Selector.RouletteSelector):
    pass


#b = BitStringGAProblem.BitStringGAProblem(allOnes, 20)
#m = MySolver(b)
#m.run()

from NurseSchedulingProblem import oneShiftEach, oneNursePerShift
from NurseFactory import NurseFactory
import BitStringGAProblem

constraintList = [oneShiftEach, oneNursePerShift]
nurseProblem = NurseFactory(constraintList)
b = BitStringGAProblem.BitStringGAProblem(nurseProblem,25)
m = MySolver(b)
m.run()