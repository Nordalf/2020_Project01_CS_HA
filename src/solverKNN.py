#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:11:01 2020

@author: alexanderfalk
"""

import itertools
import time
import solution
import sys
import random

class KNearestNeightbour:


    def __init__(self, instance):
        self.instance = instance

    def construct(self, time_left):
        return self.algorithm(time_left)

    def algorithm(self, time_left, k=3):
        sol = solution.Solution(self.instance)
        t0 = time.process_time() # Starting time
        route = [0] # Our route
        capacity = 0 # Our capacity for each vehicle
        unvisited_nodes = list(self.instance.nodes[1:])
        current_node = self.instance.nodes[0] # Starting a depot 0
        distances = {}
        
        # While there are still nodes to visit, continue
        while unvisited_nodes:
            # Loop through the unvisited nodes
            for index, p in enumerate(unvisited_nodes):
                dist = sol.instance.distance(current_node['pt'], p['pt'])
                distances.update( { dist : p } )
                
            distances = {k : v for k, v in sorted(distances.items(), key=lambda item: item[0])}
            shortest_distances = dict(itertools.islice(distances.items(), k))
            
            randomly_picked_node = random.choice(list(shortest_distances.keys()))
            node = distances.get(randomly_picked_node)
            if capacity + node['rq'] <= self.instance.capacity:
                capacity += node['rq']
                route += [int(node['id']) - 1]
                current_node = node
                unvisited_nodes.remove(current_node)

            else:
                sol.routes += [route+[0]]
                route = [0]
                capacity = node['rq']

            if time.process_time() - t0 > time_left:
                sys.stdout.write("Time Expired")
                return sol

            distances = {}
            node = None
            randomly_picked_node = None            
            
        sol.routes += [route+[0]]
        return sol

