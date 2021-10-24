from BitStringGAProblem import BitChromosome
from TSPGAProblem import TSPChromosome
import random

### mixin for crossover.

class Crossover :
    def crossover(self, c1, c2) :
        raise NotImplementedError


### single-point bitstring crossover.
class OnePointStringCrossover(Crossover) :
    def crossover(self, c1, c2) :
        locus = random.randint(0,len(c1.bitstring) - 1)
        child1 = BitChromosome(c1.bitstring[:locus] + c2.bitstring[locus:])
        child2 = BitChromosome(c2.bitstring[:locus] + c1.bitstring[locus:])
        return child1, child2


class TwoPointStringCrossover(Crossover) :
    def crossover(self, c1, c2) :

        l1 = random.randint(0,len(c1.bitstring) - 1)
        l2 = random.randint(0,len(c1.bitstring) - 1)
        if l1 > l2 :
            l1,l2 = l2,l1
        
        child1 = BitChromosome(c1.bitstring[:l1] + c2.bitstring[l1:l2] + c1.bitstring[l2:])
        child2 = BitChromosome(c2.bitstring[:l1] + c1.bitstring[l1:l2] + c2.bitstring[l2:])
        return child1, child2


### works with Permutation Chrmosomes
class PermutationCrossover(Crossover) :

    def crossover(self, c1, c2) :
        l1 = random.randint(0,len(c1.citylist) -1)
        c1list = c1.citylist[:l1]
        for item in c2.citylist :
            if item not in c1list :
                c1list.append(item)
        child1 = TSPChromosome(c1list)
        c2list = c2.citylist[:l1]
        for item in c1.citylist :
            if item not in c2list :
                c2list.append(item)
        child2 = TSPChromosome(c2list)
        return child1, child2

## works with TSP Chromosomes.
class GreedyCrossover(Crossover) :
    def crossover(self, c1, c2) :
### you do this one.
### The algorithm is as follows:
### Child1[0] == parent1[0]
### if parent1[1] is closer to Child1[0] than parent2[0], then Child1[1] = parent1[1]
### Otherwise, Child1[1] = parent2[1].
### If the chosen node is already in Child1, use the other.
### If both nodes are already in the child, select a random unused node.
### Repeat this for each subsequent node - for child[i], choose the closer parent node.
### Child2 starts with the first node of parent2 and proceeds similarly.

### To get distances, you will need a copy of the TSP graph. you can either attach it to the instance of the 
### mixin class after creating it, like so:
### class mySolver(GA.GA, Elitism.DeterministicElites, Crossover.GreedyCrossover, Selector.TournamentSelector) :
###      pass
### m = mySolver
### g = graph.Graph()
### g.makeTSPProblem(10)
### m.tspgraph = g
###
### or, you can write a method that attaches it.

        
        
        

