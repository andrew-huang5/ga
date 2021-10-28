import Elitism, Crossover,Selector, BitStringGAProblem, GA

def allOnes(chr):
    return len([x for x in chr.bitstring if x == '1'])

class MySolver(GA.GA, Elitism.DeterministicElites, Crossover.OnePointStringCrossover, Selector.TournamentSelector):
    pass


b = BitStringGAProblem.BitStringGAProblem(allOnes, 20)
m = MySolver(b)
m.run()