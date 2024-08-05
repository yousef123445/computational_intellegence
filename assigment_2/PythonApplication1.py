
'''name : youssef mohamed mohamed ezzat 
id : 20200688
'''

import random
from re import X
import numpy as np

def generate_chromosomes(num_chromosomes, chromosome_length):
    chromosomes = [''.join([str(random.randint(0, 1)) for _ in range(chromosome_length)]) 
                   for _ in range(num_chromosomes)]
    return chromosomes
def decode_pop(chromosomes,length):
    decoded_pop=[]
    for i in range(len(chromosomes)):
        varaiable =[]
        varaiable.append(decode(chromosomes[i][0:int(length/2)],length/2))# for decode x1 
        varaiable.append(decode(chromosomes[i][int(length/2):],length/2))# for decode  x2 
        decoded_pop.append(varaiable)# merge two decoded variable (x1 ,x2)
    return decoded_pop
def decode_pop_gray(chromosomes,length):
    decoded_pop=[]
    for i in range(len(chromosomes)):
        variable =[]
        variable.append(decode_gray(chromosomes[i][0:int(length/2)],length/2))
        variable.append(decode_gray(chromosomes[i][int(length/2):],length/2))
        decoded_pop.append(variable)
    return decoded_pop
def decode_gray(chromosome,percision):
    value = 0
    gray=""
    gray+=chromosome[0]
    for i in range(len(chromosome)-1):
        gray+=str(int(chromosome[i])^int(chromosome[i+1]))

    value = decode(gray,percision)
    return value
def decode(chromosome,percision):
    value = 0
    length=len(chromosome)
    for i in range(length):
        value+= 2**(length-i-1)*int(chromosome[i])
    decode= -2+(value/(2**(percision)-1))*4
    return decode
    
def rank_fitness(values):
    fitness=[]
    for i in range(len(values)):
        fitness.append(8-(values[i][0]+0.0317)*2+values[i][1]*2)
    rank= np.array(fitness).argsort().argsort()+1
    sp=1+random.random()
    rank_fitness=[]
    for j in range(len(rank)):
        rank_fitness.append( (2-sp) + 2 * (sp - 1) * (rank[j]-1)/(len(fitness)-1) )
    return fitness,rank,rank_fitness
    
# rank_fitness for constrian x1 +x2 =1 
def rank_fitness_part_2(values):
    fitness=[]
    for i in range(len(values)):
        fitness.append(8-(values[i][0]+0.0317)*2+(1-values[i][0])*2)
    rank= np.array(fitness).argsort().argsort()+1
    sp=1+random.random()
    rank_fitness=[]
    for j in range(len(rank)):
        rank_fitness.append( (2-sp) + 2 * (sp - 1) * (rank[j]-1)/(len(fitness)-1) )
    return fitness,rank,rank_fitness

    
def evaluate_fitness(chromosomes):
    fitness_scores = []
    target_chromosome = '11111'
    for chromosome in chromosomes:
        fitness = chromosome.count('1') 
        fitness_scores.append(fitness)
    return fitness_scores

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

def genetic_algorithm(runs, generations, ch_length, pcross, pmut,cross_over_point,gray,part_2):
    best_fitness_history = []
    avr_fitness_history = []
    var_values=[]
    
    for j in range(runs):
        print("run ",j+1)
       
        chromosomes = generate_chromosomes(100, ch_length)
        if gray == 1 : 
             var_values= decode_pop_gray(chromosomes,ch_length)
        else :
              var_values=decode_pop(chromosomes,ch_length)
        max_fitness = []
        avr_fitness = []
        
        for i in range(generations):
            if part_2==0:
               fit,r ,ran_fit=rank_fitness(var_values)
            else:
                fit,r ,ran_fit=rank_fitness_part_2(var_values)
            max_fitness.append(max(ran_fit))
            avr_fitness.append(sum(ran_fit) / len(ran_fit))
            probabilities = probability(ran_fit)
            cummulative_prob = cumulative(probabilities)
            new_population = []
            
            while len(new_population) < len(chromosomes):
                selection = []
        
                selection.append(select_byrouttle(chromosomes, cummulative_prob,False))
                selection.append(select_byrouttle(chromosomes, cummulative_prob,False))
                offspring = crossover(selection[0], selection[1], pcross, cross_over_point)
                new_population.append(mutation(offspring[0], pmut))
                new_population.append(mutation(offspring[1], pmut))
            
            new_population = new_population[0:98]# because you have 20 generation and you want to selcet the best individual 
            best=  elitism(chromosomes, ran_fit)         
            new_population.extend(best)
            chromosomes = new_population.copy()
            
     
      
        print(" final generation ",chromosomes, "\n")
      
        
       
        print("Best fitness history:\n", max_fitness, "\n")
        print("Average fitness history:\n", avr_fitness, "\n")
        print("\n")
       


     
print ("\t \t \t<< welcome to my application>> \n\n")    
print ("select 1 for decode pop and gray code  :")
print ("selcet 2 for test percision   :")
print ("select 3  genetic algorithm  ")

x=int(input("enter your choice : \n"))
if x==1:
      num_of_chromose=int(input("enter number of your chromose : "))
      length=int(input("enter your length of each chromsome "))
      chromose=generate_chromosomes  (num_of_chromose, length)
      print("all chromose are generated :",chromose)
      decodepop=decode_pop(chromose,length)
      print(decodepop)
      decodegray=decode_pop_gray(chromose,length)
      print("gray code for population : ",decodegray)
    
      fitness,rank,rank_fitness=rank_fitness(decodegray)
          
     
       
          
      for i in range(len (rank)):
     
          print("rank :", rank[i],"\t fitness : ", fitness[i],"\t rank_fitness : ",rank_fitness[i])
      

    
     
       
      
          
   

 
if x==2 :
     num_of_chromose=int(input("enter number of your chromose : "))
     precetion =int(input("enter the precesition of chromose"))
   
           
     chromose=generate_chromosomes(num_of_chromose,precetion)
     print(chromose)
     decodepop=decode_pop(chromose,precetion)
     print("decode pop after precetion : ",decodepop )
     decodegray=decode_pop_gray(chromose,precetion)
     print("gray code for population : ",decodegray)
     
     
     
     
     
   
     


if x==3 :
     runs = int(input("Enter number of runs: "))
     generation=int(input("enter number of your generation : "))
     ch_length = int(input("Enter length of chromosome: "))
     pCross = float(input("Enter pCross: "))
     cross_over_point=int(input("Enter cross over point : "))
     pMut = float(input("Enter pMut: "))
     gray=int (input("do you want gray code or not ( 1 / 0 )"))
     part_2=int(input("do you want part 2 or not ( 1 /0 )"))
     genetic_algorithm(runs, generation, ch_length, pCross, pMut,cross_over_point,gray,part_2)
     
 




    