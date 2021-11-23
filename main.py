import Elitism, Crossover,Selector, BitStringGAProblem, GA

def allOnes(chr):
    return len([x for x in chr.bitstring if x == '1'])

class MySolver(GA.GA, Elitism.DeterministicElites, Crossover.OnePointStringCrossover, Selector.RouletteSelector):
    pass
    #def __init__(self, problem, popsize=100, elitismRate=0.2, mutationRate=0.05, itersToRun=100):
    #GA.GA.__init__(self, problem, popsize=popsize, elitismRate=elitismRate, mutationRate=mutationRate, itersToRun=itersToRun)


# b = BitStringGAProblem.BitStringGAProblem(allOnes, 20)
# m = MySolver(b)
# m.run()

from NurseSchedulingProblem import oneShiftEach, oneNursePerShift
from NurseFactory import NurseFactory
import BitStringGAProblem

constraintList = [oneShiftEach, oneNursePerShift]
nurseProblem = NurseFactory(constraintList)
b = BitStringGAProblem.BitStringGAProblem(nurseProblem,25)
m = MySolver(b)
m.run()