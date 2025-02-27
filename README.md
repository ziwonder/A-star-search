# A* Search Algorithm for Route Planning  

## Overview  
This project implements the **A* search algorithm** in the **graph-search** variant to solve route-finding problems. The goal is to develop a **Python program** that reads problem descriptions from a YAML file, applies the A* algorithm, and outputs the solution in three YAML files, including cost, path, and expanded nodes.  

The implementation is designed to be **efficient**, solving problems with up to **10,000 locations** within **one minute**. Additionally, different heuristic functions are tested to improve search performance.  

## Features  
- Implements **A* search** to find optimal paths between locations.  
- Supports **heuristic-based optimization** using:  
  - **Uniform-Cost Search (h(n) = 0)** - first output file 
  - **Line-of-sight distance heuristic** - second output file
  - **Custom heuristics for improved efficiency** - third output file
- Reads problem definitions from **YAML files**.  
- Outputs the solution in **YAML format**, including:  
  - **Optimal path**  
  - **Total cost**  
  - **Expanded nodes**  
  - **Applied heuristic values**  

## Usage  
Execute the script with a YAML file containing the problem description:
```bash
python a_star.py <problem_file>.yaml
```
### Prerequisites  
Ensure you have **Python 3** installed along with the required libraries:  
```bash
pip install numpy pyyaml argparse
