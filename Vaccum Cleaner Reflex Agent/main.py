# Define actions
CLEAN = 0
DIRTY = 1

# Define states and goal state
STATES = ['A', 'B', 'C']
GOAL_STATE = {'A': 0, 'B': 0, 'C': 0}

# Define transition model
TRANSITION_MODEL = {
    'A': {'right': 'B', 'clean': 0},
    'B': {'left': 'A', 'right': 'C', 'clean': 0},
    'C': {'left': 'B', 'clean': 0}
}

# Define goal test
def is_goal_state(state):
    return state == GOAL_STATE

# Define path cost function
def path_cost(action):
    return 1

# Define reflex agent function
def reflex_agent(location, status, environment):
    if status == DIRTY:
        return CLEAN
    elif location == 'A':
        return 'right'
    elif location == 'B':
        if environment['A'] == DIRTY:
            return 'left'
        else:
            return 'right'
    elif location == 'C':
        return 'left'

# Define function to run agent for given inputs
def run_agent(location, status, environment):
    state = {location: status}
    path = []
    while not is_goal_state(state):
        action = reflex_agent(location, status, environment)
        path.append(action)
        if action == CLEAN:
            state[location] = CLEAN
            status = CLEAN
        elif action == 'left':
            location = TRANSITION_MODEL[location]['left']
            status = environment[location]
        elif action == 'right':
            location = TRANSITION_MODEL[location]['right']
            status = environment[location]
    return path, len(path)

# Example usage
location = input("Enter location (A/B/C): ")
status = int(input("Enter status of current location (0/1): "))
environment = {
    'A': int(input("Enter status of A (0/1): ")),
    'B': int(input("Enter status of B (0/1): ")),
    'C': int(input("Enter status of C (0/1): "))
}
path, cost = run_agent(location, status, environment)
print("Path: ", path)
print("Cost: ", cost)
