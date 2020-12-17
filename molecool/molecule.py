"""
Functions for analying/measuring molecules.
"""

import numpy as np
from .measure import calculate_distance
from .atom_data import atomic_weights

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

def calculate_molecular_mass(symbols):
   
    # Calculate the mass of a molecule.
    weight=[]
   
    for symbol in symbols:
        weight.append(atomic_weights[symbol])
   
    return sum(weight)

def calculate_center_of_mass(symbols, coordinates):
    
    # Calculate the center of mass of a molecule.
    
    total_mass = calculate_molecular_mass(symbols)
   
    mass_array = np.zeros([len(symbols), 1])
   
    for i in range(len(symbols)):
        mass_array[i] = atomic_weights[symbols[i]]
   
    center_of_mass = sum(coordinates * mass_array) / total_mass
   
    return center_of_mass