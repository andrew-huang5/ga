from GAProblem import GAProblem, Chromosome
import random

class TSPGAProblem(GAProblem) :

    def __init__(self, fitnessFn, ncities) :
        GAProblem.__init__(self, fitnessFn)
        self.ncities = ncities

    def makePopulation(self, popsize) :
        pop = []
        for i in range(popsize) :
            clist = range(self.ncities)
            random.shuffle(clist)
            pop.append(TSPChromosome(clist))
        return pop

    def evalFitness(self, pop) :
        for p in pop:
            p.fitness = self.fitnessFn(p)

    def solved(self,pop) :
        return False

    def mutate(self, c) :
        c1 = random.randint(0,len(c.citylist) -1)
        c2 = random.randint(0,len(c.citylist) -1)
        newc = []
        for i in range(len(c.citylist)) :
            if i == c1 :
                newc.append(c.citylist[c2])
            elif i == c2 :
                newc.append(c.citylist[c1])
            else :
                newc.append(c.citylist[i])
        c.citylist = newc

class TSPChromosome(Chromosome) :
    def __init__(self, citylist) :
        Chromosome.__init__(self)
        self.citylist = citylist

    def __repr__(self) :
        return "%s %d" % (self.citylist, self.fitness)



