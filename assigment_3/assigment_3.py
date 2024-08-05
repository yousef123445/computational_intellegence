# name : youssef mohamed mohamed ezzat 
# id : 20200688 
import random
import numpy as np
def initialize_pop(size,variables,maxx,minn):
    population=[]
    for i in range(size):
        temp=[]
        for j in range(variables):
            temp.append(random.random()*(maxx-minn) +minn)
        population.append(temp)
    return population


def elitism(chromosomes, fitness_scores):
      sorted_chromose = [chromosome for _, chromosome in sorted(zip(fitness_scores, chromosomes), reverse=True)]
      top_two =  sorted_chromose[:2]
      return top_two

def rank_fitness(population):
    fitness=[]
    for i in range(len(population)):
        fitness.append(8-(population[i][0]+0.0317)**2+population[i][1]**2)
    rank= np.array(fitness).argsort().argsort()+1
    sp=1+random.random()
    rank_fitness=[]
    for j in range(len(rank)):
        rank_fitness.append( (2-sp) + 2 * (sp - 1) * (rank[j]-1)/(len(fitness)-1) )
    return rank_fitness
def tournament_selcection(population,k,fitness):
    individuals = []
    selection = random.sample(population, k) 
    tournament_fitness = rank_fitness(selection)
    winner = elitism(selection ,tournament_fitness)
    individuals.append(winner)
    return individuals
def arithmetic_crossover(parent1, parent2, pcross):
    offspring_1 = []
    offspring_2= []
    if random.random() < pcross:
        for i, j in zip(parent1, parent2):
            beta = random.uniform(0, 1)
            offspring1 = beta * i + (1 - beta) * j
            offspring2 = (1 - beta) * i+ beta * j
            offspring_1.append(offspring1)
            offspring_2.append(offspring2)
    else:
        offspring_1= parent1
        offspring_2= parent2

    return offspring_1, offspring_2
def gaussian_mutation(individual, sigma, Pmut, Rmax, Rmin):
  mutated_individual = []
  for gene in individual:
        if random.random() < Pmut:
            mutation = random.gauss(0, sigma)
            mutated_gene = gene + mutation
            mutated_gene = max(min(mutated_gene, Rmax), Rmin) 
            mutated_individual.append(mutated_gene)
        else:
            mutated_individual.append(gene)
  return mutated_individual


  
    
def genetic_algorithm(runs, generations,  pcross, pmut,sigma,k):
    best_fitness_history = []
    avr_fitness_history = []

 
    for j in range(runs):
       print("run ",j+1)
    
       chromosomes = initialize_pop(100, 2,2,-2)
    
       max_fitness = []
       avr_fitness = []
     
       for i in range(generations):
         
           ran_fit=rank_fitness(chromosomes)
           max_fitness.append(max(ran_fit))
           avr_fitness.append(sum(ran_fit) / len(ran_fit))
           new_population = []
         
           while len(new_population) < len(chromosomes):
             selection = []
             selection =tournament_selcection(chromosomes,k,rank_fitness)
             offspring= arithmetic_crossover(selection[0][0],selection[0][1],pcross)
             new_population.append(gaussian_mutation(offspring[0],sigma,pmut,2,-2))
             new_population.append(gaussian_mutation(offspring[1],sigma,pmut,2,-2))
         
           new_population = new_population[0:98]# because you have 20 generation and you want to selcet the best individual 
           best=  elitism(chromosomes, ran_fit)         
           new_population.extend(best)
           chromosomes = new_population.copy()
         
  
   
       print(" final generation ",chromosomes, "\n")
       
       print("Best fitness history:\n", max_fitness, "\n")
       print("Average fitness history:\n", avr_fitness, "\n")
       print("\n")
      
print ("\t \t \t<< welcome to my application>> \n\n")    
print ("select 1 for intilize pop   :")
print("select 2 for gentic algorithm : ")


x=int(input("enter your choice : \n"))
if x==1:
   size=int(input("enter the size of your population "))
   variable=int(input("enter the number of variable "))
   r_max=int(input("enter r_max "))
   r_min=int(input("enter r_min"))
   pop = initialize_pop(size,variable,r_max,r_min)
   print("population: ",pop)  
   k=int(input("enter k :"))
   rank=rank_fitness(pop)
   select =tournament_selcection(pop,k,rank_fitness)
   print("tournment selection  : ",select)
   offspring=arithmetic_crossover(select[0][0],select[0][1],0.6)
   print(" arthimtic_crossover",offspring)
  
   sigma=float(input("enter your sigma "))
   pmut=float (input("enter yout pmut :"))
   print("gussian mutation : ")
   print("mutation for childrens : ",gaussian_mutation(select[0],sigma,pmut,2,-2))
if x==2:
     runs = int(input("Enter number of runs: "))
     generation=int(input("enter number of your generation : "))
     pCross = float(input("Enter pCross: "))
     pMut = float(input("Enter pMut: "))
     sigma=float(input("enter your sigma "))
     k=int(input("enter your k of tournment "))
     
     genetic_algorithm(runs, generation,pCross, pMut,sigma,k)
     
 

     
   
     

   
    
   


  
   





 







