# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:51:43 2020

@author: cvsan
"""


'''Aum'''


import random

#print(random.randint(0,7))

# Goal=5 2 4 6 0 3 1 7

# create a list with 8 number. numbers range from 0 to 7 shud be unique


queen_list=[]*8
target_chromosome=[5, 2 ,4 ,6 ,0 ,3 ,1, 7]
#print(queen_list)#
fitness_value=0
initial_population=[]
generation=0
INIT_POP=100
offspring_population=[]
sequence_found=False
sequence_identified=[]

class chromosome():
    def __init__(self,random_chromosome):
        self.single_chromosome=random_chromosome
        self.fitness=self.chromosome_fitness(random_chromosome)
        
    
       

    
    def chromosome_fitness(self,chromosome):
        fitness_value=0
        #fitness_population=[]
    
        # for i in range(len(initial_population)):
        #     #print(initial_population[i])
        fitness_value=0 # reset fitness for every chromosome
        for j in range(len(chromosome)):
            
            #print(chromosome[j])
            #print(target_chromosome[j])
            
            if chromosome[j] ==target_chromosome[j]:
                # Goal=5 2 4 6 0 3 1 7  
                if j ==0:
                    fitness_value += 10000000
                elif j ==1:
                    fitness_value += 1000000
                elif j ==2:
                    fitness_value += 100000
                elif j ==3:
                    fitness_value += 10000
                elif j ==4:
                    fitness_value += 1000
                elif j ==5:
                    fitness_value += 100
                elif j ==6:
                    fitness_value += 10
                elif j ==7:
                    fitness_value += 1
            
            #fitness_population[initial_population[i]]=fitness_value
                    
            #print(initial_population[i])
            #print(fitness_value)
            # temp=[]
            # temp.append(initial_population[i])
            # temp.append(fitness_value)
            # fitness_population.append(temp)
        return fitness_value





def chromosome_create():
               
        chromosome=[]
        #counter=0    
        found_8_gene=False
    
        while not found_8_gene:
        
            gene=random.randint(0,7)#as its 8 queen
            if gene not in chromosome:
                chromosome.append(gene)
        
            if len(chromosome)==8:
                found_8_gene=True
        
        #print(chromosome)
        return chromosome;
    
def initialise_population_func(INIT_POP):
    random_chromosome=[]
    for i in range(INIT_POP):
        
        random_chromosome=chromosome_create()
        individual_chromosome=chromosome(random_chromosome)# object 
        
        #single_chromosome=individual_chromosome.chromosome_create()#attribute
        #fitness=individual_chromosome.chromosome_fitness(single_chromosome)#attribute
        
        temp=[]
        temp.append(individual_chromosome.single_chromosome)
        temp.append(individual_chromosome.fitness)
        initial_population.append(temp)
    
        #print(initial_population)
        #print(len(initial_population))

    return initial_population


def shuffle_sort_population(initial_population):
    #print(initial_population)
    return(initial_population[1])

 

def parent_crossover(P1,P2,):
    offspring=[]
    #print("P1: {}".format(P1))
    #print("P2: {}".format(P2))
    
     
    offspring=P1[0:4] + P2[4:6] + P1[6:8]
     
    recount_number=0
    
    #print("P1: {}".format(P1))
    #print("P2: {}".format(P2))
    #print("offspring after MERGER: {}".format(offspring))
    temp=[]
    for i in range(len(offspring)):
        recount_number=offspring.count(offspring[i])
        if recount_number >1:
            recount_number =offspring.count(offspring[i])
            #print("i={},offspring[i]: {} , recount_number: {}, offspring:{}". format (i,offspring[i],recount_number,offspring) )
            temp=[]# reset
            for j in range(len(offspring)):  
                #print ("ALLL HERE, offspring[j]:{},offspring[i]:{}".format(offspring[j],offspring[i]))
                if offspring[j]==offspring[i]:
                    temp.append(j)
                    #print ("j:{}, temp:{}".format(j,temp))
                    
         
            temp=sorted(temp,reverse=True)
            #print ("temp:{}".format(temp))
            #print("range(len(temp)-1):{} temp:{} ".format(range(len(temp)-1), temp))
            for k in range(len(temp)-1):
                #print("offspring:{} before popup:{}".format(offspring,temp[k]))
                offspring.pop(temp[k])
                #print("offspring:{} after popup:{}".format(offspring,temp[k]))
            
    
        while len(offspring) !=8:
        
            gene_random=random.randint(0,7)
        
            if gene_random not in offspring:
                offspring.insert(temp[k],gene_random)
                                   
                #print("offspring:{}".format(offspring))
    return offspring



def sequence_found_func(initial_population):
    sequence_not_found=True  
    offspring_population=[]
    generation=0
    sequence_identified=[]
    MAX_GENERATION=1000
    #res=[]
    #print("before res:{}".format(initial_population))
    #sub --> [[5, 6, 4, 2, 7, 1, 3, 0], 10100000]
    #res = list(set((sorted(sub)) for sub in initial_population)) 
    
    
    while sequence_not_found and generation <=MAX_GENERATION:
        #print(initial_population)
        #print (type(set_population))
        
        for i in range(len(((initial_population)))):
            
            #select 2 parents for crossover to create offsprings, randomly from top 50 individuals
            
            parent_chromosome1_num=random.randint(0,50)
            parent_chromosome2_num=random.randint(0,50)
            
            # if parent_chromosome2_num==parent_chromosome1_num:
            #     parent_chromosome2_num=random.randint(0,50)
                
            parent_chromosome1=initial_population[parent_chromosome1_num]
            parent_chromosome2=initial_population[parent_chromosome2_num]
            
            if parent_chromosome2 ==parent_chromosome1:
                #print("Both parents are same, need to generate new random sequence")
                #print("parent_chromosome2:{},parent_chromosome1:{}".format(parent_chromosome2,parent_chromosome1))
                offspring=[]
                offspring=chromosome_create()
                offspring_chromosome=chromosome(offspring)#obj
                temp=[]
                temp.append(offspring_chromosome.single_chromosome)
                temp.append(offspring_chromosome.fitness)
                parent_chromosome2=temp
                #print("AFTER RANDOM,parent_chromosome2:{},parent_chromosome1:{}".format(parent_chromosome2,parent_chromosome1))
               
                
            temp=[]
            temp.append(parent_chromosome1)
            temp.append(parent_chromosome2)
            temp=sorted(temp,key=shuffle_sort_population,reverse=True)
            #print("temp before crossover:{}".format(temp))
            
             
            parent_chromosome1=temp[0][0]
            parent_chromosome2=temp[1][0]
            
                
              
            #print("parent_chromosome1:{}, parent_chromosome2:{}".format(parent_chromosome1,parent_chromosome2))
            offspring=parent_crossover(parent_chromosome1,parent_chromosome2)
            
            #print("offspring={}".format(offspring))
            #calculare offspring fitness
            offspring_chromosome=chromosome(offspring)#obj
            
            #single_chromosome=offspring_chromosome.chromosome_create()#attribute
            #fitness=offspring_chromosome.chromosome_fitness(offspring)#attribute
            
            #single_chromosome=individual_chromosome.chromosome_create()#attribute
            #fitness=individual_chromosome.chromosome_fitness(single_chromosome)#attribute
        
            temp=[]
            temp.append(offspring_chromosome.single_chromosome)
            temp.append(offspring_chromosome.fitness)
            offspring_population.append(temp)
        
            
        #print("offspring population: {} ".format(offspring_population))
        #print("length of offspring population after crossover: {}".format(len(offspring_population)))
            
            
        #merge parent initial and offspring and then remove top 100
        
        initial_population=offspring_population + initial_population 
        offspring_population=[]
        
      
        initial_population=sorted(initial_population,key=shuffle_sort_population,reverse=True)
        #print("initial population: {} ".format(initial_population))
        #print("length of initial population after merger with offspring: {}".format(len(initial_population)))
        #print("length of offspring population after merge with parent: {}".format(len(offspring_population)))
        
        #Allow top 100 only
        initial_population=initial_population[0:100]
        
        #print("Top 100 individual from population: {} ".format(initial_population))
        #print("length of initial population after [0:100]: {}".format(len(initial_population)))
        
        #remove duplicate parents from generation as offsprign will be same
        
        for i in range(len(initial_population)):
            #remove_dups(initial_population)
            pass
            
            
        generation +=1
        #print("generation:{}".format(generation))
        for i in range(len(initial_population)):
            #[[7, 5, 0, 2, 1, 3, 4, 6], 100]'
            #print("initial chromosome:{}, target chromosome:{}".format(initial_population[i][0],target_chromosome) )
            if initial_population[i][0]==target_chromosome:
            #if initial_population[i][1]==11111111:#5 2 4 6 0 3 1 7 
                sequence_not_found=False
                #print("initial_population[i][0]:{}, i={},generation={}, fitness={}".format(initial_population[i][0],i,generation,initial_population[i][1]))
                sequence_identified=initial_population[i][0]
                break
               
        if sequence_not_found==False: # so, we got sequence
            sequence_identified_text=" ".join([str(elem) for elem in sequence_identified]) 
            #print ("Sequence found:{},string:{} ".format(sequence_identified,sequence_identified_text))
        else:
            pass
            #print("Target chromosome not found, need to loop again and do crossover!")    
        
            
    return sequence_identified_text
            
        
if __name__ == '__main__':
    initial_population=[]
    generation=0
    INIT_POP=100
    offspring_population=[]
    sequence_found=False
    sequence_identified=[]
    #print("Initialise the population for {} individuals and also calculate fitness".format(INIT_POP))
    initial_population=initialise_population_func(INIT_POP)
    #print("Sort and shuffle the initial population")
    initial_population=sorted(initial_population,key=shuffle_sort_population,reverse=True)
    #print("initial population: {} ".format(initial_population))
    #print("length of initial population at startup: {}".format(len(initial_population)))
    

    #initial_population=remove_dups(initial_population)
    #print("AFTER Remove duplicates, FITNESS IS GONE: {}".format((initial_population)))
    #print("AFTER Remove duplicates, FITNESS IS GONE: {}".format(len(initial_population)))
    
    #print("Lets find sequence!")
    #print("Disaled for now")
    sequence_identified_text=sequence_found_func(initial_population)
    print(sequence_identified_text)
