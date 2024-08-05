 #myname : youssef mohamed mohmed ezzat
#id : 20200688
from hmac import new
import random
import numpy as np
#generate_population

def generate_chromosomes(num_chromosomes, chromosome_length):
    chromosomes = [''.join([str(random.randint(0, 1)) for _ in range(chromosome_length)]) 
                   for _ in range(num_chromosomes)]
    return chromosomes
#evalute fitness 
def evaluate_fitness(chromosomes):
    fitness_scores = []
    target_chromosome = '11111'
    for chromosome in chromosomes:
        fitness = chromosome.count('1') 
        fitness_scores.append(fitness)
    return fitness_scores


# evalute probabality 
def probability(fitness):
    total_fitness = sum(fitness)
    probabilities = [float(fitness[i]) / total_fitness for i in range(len(fitness))]
    return probabilities
#evalute commulative 
def cumulative(probabilities):
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    return cumulative_probabilities
#select bt routtle by cummaltive porobabilties and switch for printing random or not 

def select_byrouttle(chromosomes, cumulative_probabilities,switch):
  
    random_routtle= random.random()
    if switch==True:
         print(random_routtle)
 
    for i in range(len(cumulative_probabilities)):
        if random_routtle <= cumulative_probabilities[i]:
            return chromosomes[i]
      

# making cross_over by any point by crosspoint for two individual
def crossover(parent1, parent2, pCross, crossover_point):
    if random.random() < pCross:
        child_1 = parent1[:crossover_point] + parent2[crossover_point:]
        child_2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        child_1 = parent1
        child_2 = parent2
    return child_1, child_2
#make mutation 

def mutation(chromosome, pMut):
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < pMut:
            mutated_bit = '0' if bit == '1' else '1'
            mutated_chromosome += mutated_bit
        else:
            mutated_chromosome += bit
    return mutated_chromosome
#fucntion that return best indivdual 

def elitism(chromosomes, fitness_scores):
      sorted_chromose = [chromosome for _, chromosome in sorted(zip(fitness_scores, chromosomes), reverse=True)]
      top_two =  sorted_chromose[:2]
      return top_two

# function of genetic algorithm
def genetic_algorithm(runs, generations, ch_length, pcross, pmut,cross_over_point):
    best_fitness_history = []
    avr_fitness_history = []
    
    for j in range(runs):
       
        chromosomes = generate_chromosomes(20, ch_length)
        max_fitness = []
        avr_fitness = []
        
        for i in range(generations):
           
            fitnesses = evaluate_fitness(chromosomes)
            max_fitness.append(max(fitnesses))
            avr_fitness.append(sum(fitnesses) / len(fitnesses))
            probabilities = probability(fitnesses)
            cummulative_prob = cumulative(probabilities)
            new_population = []
            
            while len(new_population) < len(chromosomes):
                selection = []
        
                selection.append(select_byrouttle(chromosomes, cummulative_prob,False))
                selection.append(select_byrouttle(chromosomes, cummulative_prob,False))
                offspring = crossover(selection[0], selection[1], pcross, cross_over_point)
                new_population.append(mutation(offspring[0], pmut))
                new_population.append(mutation(offspring[1], pmut))
            
            new_population = new_population[0:18]# because you have 20 generation and you want to selcet the best individual 
            best=  elitism(chromosomes, fitnesses)         
            new_population.extend(best)
            chromosomes = new_population.copy()
            
     
      
        print(" final generation ",chromosomes, "\n")
      
        
       
        print("Best fitness history:\n", max_fitness, "\n")
        print("Average fitness history:\n", avr_fitness, "\n")
        print("\n")
       


 
        

# Input parameters
# switch case for gentic with selection , gentic with etlisim , test code 
while True:        
 print ("\t \t \t<< welcome to my application>> \n\n")    
 print ("select 1 for test all function of genentic algortithm  code :")
 print ("selcet 2 for evalute genetic algortihm  :")
 print ("select 3 for document of this code ")
 print("select 4 for stop :\n\n")
 x=int(input("enter your choice : \n"))
 if x==1:
     num_of_chromose=int(input("enter number of your chromose : "))
     length=int(input("enter your length of each chromsome "))
     chromose=generate_chromosomes  (num_of_chromose, length)
     print("all chromose are generated :",chromose)
     fitness =evaluate_fitness(chromose) 
     print(" fitnsess of each fitness : " ,evaluate_fitness(chromose)  )
     probality =probability(fitness)
     print (" all probablity of each chromose : ",probability(fitness))
     print ( "all cummulative of each chromose : ",cumulative( probality))
     cumulatives =cumulative( probality)
     selection=[]
     for i in range(2):
       selection.append(select_byrouttle(chromose,cumulatives,True))

       print ("  parent ",i+1 ," for making mutation and cross over ",selection[i])
     eltisim=elitism(chromose,fitness)
     print(" you can found the best indivdual : ",eltisim)
     print (" now we can make cross over and mutation ")
     crosspoint=int(input(" enter cross over point :"))
     pcross=float(input("enter pcross")) 
     offspring_2=crossover(eltisim[0],eltisim[1],pcross,crosspoint)
     print("two childern from the best indivdula : ",offspring_2)
     offspring = crossover(selection[0], selection[1], pcross, crosspoint)
     print(" two childern from selection routlle : ",offspring)
     pMut=float(input("enter your Pmut "))
     print (" muattion of childern 1 from  best indivdula (etlism) : ",mutation(offspring_2[0], pMut))
     print("mutation of childern 2 from best indivdula (etlism) : ", mutation(offspring_2[1],pMut))
     print (" muattion of childern 1 from selection routtle : ",mutation(offspring[0], pMut))
     print("mutation of childern 2 from selection routtle  : ", mutation(offspring[1],pMut))
   

 
 if x==2 :
     runs = int(input("Enter number of runs: "))
     generation=int(input("enter number of your generation : "))
     ch_length = int(input("Enter length of chromosome: "))
     pCross = float(input("Enter pCross: "))
     cross_over_point=int(input("Enter cross over point : "))
     pMut = float(input("Enter pMut: "))
     

# Run the genetic algorithm
     genetic_algorithm(runs, generation, ch_length, pCross, pMut,cross_over_point)
 if x==3 :
     print("\t \t \t the steps of genetic algorithm : ")
     print("1:generate N number of chromosomes with length L")
     print("2:compute the fitness for all chromosomes according to the number of 1s") 
     print("3:cumpute their relative fitness and cumulative relative fitness")
     print("4:generate 2 random numbers to select 2 chromosomes to become parents according to their cumulative relative fitness")
     print("5:generate their offspring using one point crossover with crossover point and pcross")
     print("6:use mutation on the offspring bits using pmut")
     print("7:add the 2 offsprings to the new population")
     print("8: use elitism to choose best 2 individuals to keep them on next population ")
     print("9:-repeat numbers of runs  from step 2 for M generations\n\n\n ")
    
 if x==4:
      break

    
     
            

  
     
