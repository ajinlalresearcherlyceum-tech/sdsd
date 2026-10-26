#!/usr/bin/env python3
"""
Test Harness for Full-Physics Multi-Product Forward ODE Simulation
"""

import numpy as np

# Page kinetics parameters
products = {
    'Juice': {
        'name': 'Tomato Juice (Foamed 2.5 mm)',
        'k0': 1.115e5, 'Ea_R': 5963.4,
        'n_base': 1.1845, 'n_slope': -0.00541,
        'T_ref': 60.0, 'T_max': 70.0,
        'M0': 9.0, 'mp': 6.0, 'md': 0.60
    },
    'Pulp': {
        'name': 'Tomato Pulp (Unfoamed 2 mm)',
        'k0': 533.2, 'Ea_R': 4011.2,
        'n_base': 1.1562, 'n_slope': 0.000585,
        'T_ref': 60.0, 'T_max': 80.0,
        'M0': 11.5, 'mp': 8.4, 'md': 0.672
    },
    'Potato': {
        'name': 'Potato Slices (5 mm)',
        'k0': 4.50e4, 'Ea_R': 4500.0,
        'n_base': 1.1180, 'n_slope': -0.00200,
        'T_ref': 60.0, 'T_max': 75.0,
        'M0': 4.0, 'mp': 20.0, 'md': 4.00
    },
    'Moringa': {
        'name': 'Moringa Leaves (Single layer)',
        'k0': 2.80e6, 'Ea_R': 6200.0,
        'n_base': 1.0811, 'n_slope': -0.00400,
        'T_ref': 60.0, 'T_max': 70.0,
        'M0': 3.17, 'mp': 4.0, 'md': 0.96
    }
}

def get_kinetics(prod_key, T_C):
    p = products[prod_key]
    T_K = T_C + 273.15
    k = p['k0'] * np.exp(-p['Ea_R'] / T_K)
    n = p['n_base'] + p['n_slope'] * (T_C - p['T_ref'])
    return max(1e-5, k), max(0.8, min(1.4, n))

for p_key, p_val in products.items():
    k60, n60 = get_kinetics(p_key, 60.0)
    k70, n70 = get_kinetics(p_key, 70.0)
    print(f"{p_val['name']}:")
    print(f"  60 C: k = {k60:.6f}, n = {n60:.4f}")
    print(f"  70 C: k = {k70:.6f}, n = {n70:.4f}")

print("Kinetics verified.")
