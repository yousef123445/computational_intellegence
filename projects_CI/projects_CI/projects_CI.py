import random
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def generate(size,length,rmin,rmax):
    population=[]
    for i in range(size):
        x=[]
        for j in range(length):
            x.append(rmin[j]+random.random()*(rmax[j]-rmin[j]))
        x=constrain_solution(x)
        population.append(x)
        
    return population

def constrain_solution(x):
    total=[0]*10
    for j in range(10):
        for i in range(5):
            total[j]+=x[j*5+i]
    for j in range(10):
        if total[j] != 20:
            for i in range(5):
                x[j*5+i] = x[j*5+i] * (20 / total[j])  # Scale the vector to ensure the sum equals 20
    return x

def select_parents(population,target):
    selected=[]
    c=0
    while len(selected)!=3:
        x = random.randint(0,len(population)-1)
        if population[x] not in selected and population[x]!=target:
            selected.append(population[x])
        elif c>len(population):
            selected.append(population[x])
        c+=1
    return selected
def mutation(parents,F,rmax,rmin):
    mutated=F*(parents[0]-parents[1])+parents[2]
    for i in range(len(mutated)):
        if mutated[i]<rmin[i]:
            mutated[i]=rmin[i]
        elif mutated[i]>rmax[i]:
            mutated[i]=rmax[i]
    return mutated
def crossover(mutated,target,pcross,difinite_count):
    trail=[]
    definite_index=[]
    while len(definite_index)!=difinite_count:
        x = random.randint(0,len(mutated)-1)
        if x not in definite_index:
            #print(x)
            definite_index.append(x)
    for i in range(len(mutated)):
        trail.append(0.0)
        if i in definite_index or pcross > random.random():
            trail[i]=mutated[i]
        else:
            trail[i]=target[i]
    trail= constrain_solution(trail)
    return trail
def fitness(X,C):
    fitness=0
    for i in range(len(X)):
        fitness+=X[i]*C[i]
    #enter the function of X here
    return fitness
def best(trail,target,Cost,bestCost):
    
    if fitness(trail,Cost) < fitness(target,Cost): #less than if minimize
        bestCost=min(fitness(trail,Cost),bestCost)
        return trail,bestCost
    else:
        bestCost=min(fitness(target,Cost),bestCost)
        return target,bestCost
def defuzz(simulations,population,fuzzy):
    defuzzified= []
    fuzzy_values=[]
    for i in range(simulations):
        while True:
            for j in range(len(population[i])):
                x = population[i][j]
                u = fuzz.interp_membership(fuzzy.universe, fuzzy['fuzzy'].mf, x)
                alpha = np.random.uniform(0, 1)
                if alpha <= u:
                    fuzzy_values.append(u)
                    defuzzified.append(x)
                    break
            break
    return defuzzified,fuzzy_values

Best= float('inf')
mini=[0]*50
maxi = [20]*50
F= random.random()*2
pcross=0.5
definite_crossover=int(input("definite crossover count: "))
generations=500
population=generate(100,50,mini,maxi)
Xij=np.arange(0,21,1)
X_fuzzy = ctrl.Antecedent(Xij, 'Xij')
X_fuzzy['fuzzy']=fuzz.trimf(X_fuzzy.universe,[0,20,20])
print(X_fuzzy['fuzzy'].mf)
Cost=[38,18,29,24,21,12,27,32,30,10,38,32,25,15,20,11,20,30,38,11,31,19,24,29,35,15,10,25,30,32,40,21,26,31,23,17,18,17,15,38,37,23,28,29,21,21,34,29,34,40]
for j in range(generations):
    
    for i in range(len(population)):
        target=population[i]
        parents= select_parents(population,target)
        parents=np.array(parents)
        mutated= mutation(parents,F,maxi,mini)
        trial=crossover(mutated,target,pcross,definite_crossover)
        better,Best = best(trial,target,Cost,Best)
        population[i]=better
    if (j+1)%50==0 or j ==0 :
        print("genration ",j+1)
        for i in range(10):
            pop_temp=population[0][i*5:i*5+5]
            print('task[',i+1,'] = ', pop_temp)
        print("best cost = ",Best)
        defuzzy_values,fuzzy_values =defuzz(5,population,X_fuzzy)
        print('fuzzy= ',fuzzy_values)
        print(" 'defuzzified' X over 5 simulations:", defuzzy_values)
        average_defuzzified_X = np.mean(defuzzy_values)
        print("average 'defuzzified' X over 5 simulations:", average_defuzzified_X)
        