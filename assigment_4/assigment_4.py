'''
 Name : youssef mohamed mohamed ezzat 
 id : 20200688
 '''

import math
import numpy as np
import random
#calculte distance between two city ('ecuplirain)
def distance_between_twonodes(node_1, node_2):
    return math.sqrt((node_2[0] - node_1[0])**2 + (node_2[1] - node_1[1])**2) 

# select next node 

def choose_next_node(current_node, visited, pheromone, eta ,num_nodes,alpha,beta):
    probabilities = []
    not_visited=[]
    for i in range(num_nodes):
        if i not in visited:
            not_visited.append(i)

    for i in range(num_nodes):
        if i not in visited:
            probabilities.append(pheromone[current_node][i]*alpha * eta[current_node][i]*beta)
    probabilities = probabilities / sum(probabilities)
    next_node_index = np.random.choice(range(len(not_visited)), p=probabilities)
    
    return not_visited[next_node_index]
#calculate tour length_nearset_neighbor

def tour_length_nearest_neighbor(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities  
    start_city = 0  
    current_node = start_city
    length_tour = 0

    for i in range(num_cities - 1):  
        nearest_node = None
        min_distance = float('inf')

        for next_city in range(num_cities):
            if next_city != current_node and not visited[next_city]:
                distance = distance_matrix[current_node][next_city]
                if distance < min_distance:
                    min_distance = distance
                    nearest_node = next_city

        length_tour += distance_matrix[current_node][nearest_node]
        visited[current_node] = True
        current_node= nearest_node

    
    length_tour += distance_matrix[current_node][start_city]

    return length_tour

city_coordinates = []
with open('TSPDATA.txt', 'r') as file:
    first_colum = 1
    for l in file:
        coordinates = list(map(float, l.split()))
        coordinates.remove(first_colum)
        first_colum += 1
        city_coordinates.append(coordinates)

nodes = first_colum - 1
# calculate distance matrix 
distance_matrix = [[distance_between_twonodes(city1, city2) for city2 in city_coordinates] for city1 in city_coordinates]
#calculate eta matrix 
eta_matrix = [[1/distance if distance != 0 else 0 for distance in row] for row in distance_matrix]
# calculate lnn
lnn = tour_length_nearest_neighbor(distance_matrix)
# calculte toa it.'s same tao = 1/ nodes 
tao = np.ones((nodes, nodes)) / (nodes * lnn)
alpha = 1.0
beta = 2.0
best_distance = float('inf')
num_ants=nodes
evaporation_rate=0.5
num_iterations=int(input("enter the number off ur iteration : "))
best_tour = []
for iteration in range(num_iterations):
    for ant in range(num_ants):
       
        tour=[]
        tour.append(ant)
        start_point=0
        distance = 0.0
        while len(tour) < nodes:
            next_node = choose_next_node(tour[start_point],tour,tao,eta_matrix,nodes,alpha,beta)
            tour.append(next_node)
           
            distance += distance_matrix[tour[start_point]][next_node] 
            start_point+=1
        distance += distance_matrix[tour[start_point]][tour[0]] 
        tour.append(tour[0])
        if distance < best_distance and distance!=0:
            best_distance = distance
            best_tour = tour
    tao *= (1 - evaporation_rate)
    for i in range(len(best_tour) - 1):
        tao[best_tour[i]][best_tour[i+1]] += 1.0 / best_distance
        
print(f"Best tour: {best_tour}")
print(f"Best distance: {best_distance}")



