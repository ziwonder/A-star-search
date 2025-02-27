import yaml
import argparse
import heapq


def load_problem(file_name):
    with open(file_name, 'r') as file:
        problem = yaml.safe_load(file)
    return problem   

def write_solution(file_name, data):
    with open(file_name, 'w') as file:
        yaml.dump(data, file)    

def uniform_cost_search(graph, start_node, goal):
    frontier = [(0,start_node)]
    explored_set = []
    visited_cost = {}
    path = {start_node: None}
    while True:
        if len(frontier) == 0:
            raise ValueError("Invalid problem.")
        current_cost, current_node = heapq.heappop(frontier)
        if current_node == goal:
            path_result = []
            while current_node:
                path_result.append(current_node)
                current_node = path[current_node]
            return current_cost, len(explored_set), list(reversed(path_result))

        if current_node not in explored_set:
            explored_set.append(current_node)
            visited_cost[current_node] = current_cost

        for child, cost in graph[current_node].items():
            total_cost = current_cost + float(cost)
            if (child not in visited_cost) or total_cost < visited_cost[child]: 
                path[child] = current_node
                heapq.heappush(frontier, (total_cost, child))
                visited_cost[child] = total_cost
                   
def search_with_simple_heuristic(graph, start_node, goal, heuristics_info):
    frontier = [(heuristics_info[start_node]['line_of_sight_distance'],0,start_node)]
    explored_set = []
    visited_cost = {}
    path = {start_node: None}

    while True:
        if len(frontier) == 0:
            raise ValueError("Invalid problem.")
        estimated_cost, current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path_result = []
            while current_node:
                path_result.append(current_node)
                current_node = path[current_node]
            return current_cost, len(explored_set), list(reversed(path_result))

        if current_node not in explored_set:
            explored_set.append(current_node)
            visited_cost[current_node] = estimated_cost

        for child, cost in graph[current_node].items():
            child_cost = current_cost + float(cost) 
            total_cost = child_cost + heuristics_info[child]['line_of_sight_distance']

            if (child not in visited_cost) or total_cost < visited_cost[child]:
                path[child] = current_node   
                visited_cost[child] = total_cost
                heapq.heappush(frontier, (total_cost,child_cost, child))


#Passing argument
if __name__ == "__main__": 
    parse = argparse.ArgumentParser()
    parse.add_argument("filename")
    args = parse.parse_args()

    problem_data = load_problem(args.filename)

#Creating a graph
    graph = {}
    problem = problem_data['problem']
    for key, value in problem.items():
        if key.startswith('city_') and key != 'city_start' and key != 'city_end':
            city_name = key.split('_')[1]
            connects_to = value.get('connects_to', {})
            graph[city_name] = {neighbor: float(cost) for neighbor, cost in connects_to.items()}

    start_node = problem['city_start']
    goal = problem['city_end']
    
#Heuristics
    heuristics_info = {}
    heuristics = problem_data['additional_information']
    for key, value in heuristics.items():
        city_name = key.split('_')[1]
        heuristics_info[city_name] = value     

#Aufgabe1-1
    cost, explored_nodes, path = uniform_cost_search(graph, start_node, goal)

    data_1 = {
        'solution' : {
            'cost': cost,
            'expanded_nodes': explored_nodes,
            'heuristic': {
                f'city_{i}' : 0.0 for i in heuristics_info.keys()
            },
            'path' : [i for i in path],
            
        }
    }

    write_solution('aufgabe1-1.yaml', data_1)

#Aufgabe1-2 
    cost, explored_nodes, path = search_with_simple_heuristic(graph, start_node, goal, heuristics_info)
    data_2 = {
        'solution' : {
            'cost': cost,
            'expanded_nodes': explored_nodes,
            'heuristic': {
                f'city_{i}' : heuristics_info[i]['line_of_sight_distance'] for i in heuristics_info.keys()
            },
            'path' : [i for i in path],
            
        }
    }
    write_solution('aufgabe1-2.yaml', data_2)

#Aufgabe1-3
    heuristics_info = {}
    heuristics = problem_data['additional_information']
    for key, value in heuristics.items():
        city_name = key.split('_')[1]
        total_heuristic = ((value['line_of_sight_distance'])**2 + (value['altitude_difference'])**2)**(1/2)
        heuristics_info[city_name] = {'line_of_sight_distance': total_heuristic}    

    cost, explored_nodes, path = search_with_simple_heuristic(graph, start_node, goal, heuristics_info)
    data_3 = {
        'solution' : {
            'cost': cost,
            'expanded_nodes': explored_nodes,
            'heuristic': {
                f'city_{i}' : heuristics_info[i]['line_of_sight_distance'] for i in heuristics_info.keys()
            },
            'path' : [i for i in path],
            
        }
    }
    write_solution('aufgabe1-3.yaml', data_3)


