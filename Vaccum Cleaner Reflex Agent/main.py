
#Goal State that the vacuum has to achieved
goal_state = {'A':0,'B':0,'C':0}

#Neighbors of all the Given Rooms
neighbors = {'A':{'Right': 'B','Left':None}, 'B':{'Right':'C','Left':'A'},'C':{'Right':None,'Left':'B'}}

#Taking Input on which Room Vacuum Currently is 
vacuum_location = input("Enter location of the Vacuum (A/B/C): ")

#Defining the current state of the Rooms 
current_state = {
    'A': int(input("Enter status of A (0/1): ")),
    'B': int(input("Enter status of B (0/1): ")),
    'C': int(input("Enter status of C (0/1): "))
}


#defining the Reflex Agent to clean the Rooms
def reflex_agent(initial,state,goal_state,neighbors):
    
    current_state = state.copy()
    
    #Cost for cleaning all rooms on the left 
    cost_r = 0 

    starting_state = initial
    
    #the last room that the vacuum clean on the right of the given room 
    global last_node

    #loop for cleaning all the rooms that are on the Right Side of the given Room
    for key in neighbors.keys():

        if starting_state == key:
            if starting_state is not None:

                if current_state[key] != 0:
                    current_state[key] = 0
                    cost_r += 1  
                else:
                    cost_r += 1
                starting_state = neighbors[key]['Right']

                if neighbors[key]['Right'] == None:
                    last_node = key 
                else:
                    last_node = neighbors[key]['Right']

    #cost for cleaning all rooms on the left of the last room vacuum clean 
    cost_l = 0 
    
    #loop for cleaning all the room that are on the left side of the last room vacuum clean 
    while True:

        if goal_state == current_state:
            break 
 
        for key in neighbors.keys():

            if last_node == key:
                if last_node is not None:

                    if current_state[key] != 0:

                        current_state[key] = 0
                        cost_l += 1 

                    else:
                        cost_l += 1    
                         
                    last_node = neighbors[key]['Left']

    #calculating the total cost
    cost = cost_l + cost_r

    #returning the total cost and the state of all room after cleaning 
    return current_state , cost 

#Calling the Reflex_Agent to clean the Room 
final_state , cost = reflex_agent(vacuum_location,current_state,goal_state,neighbors)

#Printing the Output 
print("Rooms State Before the Vacuum Cleans them: ", current_state)
print("Rooms State After Vacuum Cleans them: ", final_state)
print("Total Cost : ",cost)
