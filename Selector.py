import random

## more mixin here

class Selector :
    
    ### given a population, choose two parents
    def selectChromosomes(self, pop) :
        raise NotImplementedError


class TournamentSelector(Selector) :
    def selectChromosomes(self, pop) :
        fit1, ch1 = pop[random.randint(0, len(pop) - 1)]
        fit2, ch2 = pop[random.randint(0, len(pop) - 1)]

        return ch1 if fit1 > fit2 else ch2
### You do this part. The method should return two potential parents.
### For each parent, choose two potential parents and compare their
### fitnesses. The more fit parent is retained.

### choose two parents via roulette selection

class RouletteSelector(Selector) :
    def selectChromosomes(self, pop) :
        total = sum([x.fitness for x in pop])
        rval = random.randint(0,total)
        i = 0
        counter = pop[0].fitness
        while counter < rval and i < len(pop) -1 :
            counter += pop[i].fitness
            i += 1
        c1 = pop[i]
        rval = random.randint(0,total)
        i = 0
        counter = pop[0].fitness
        while counter < rval and i < len(pop) - 1 :
            counter += pop[i].fitness
            i += 1
        c2 = pop[i]
        return c1,c2
