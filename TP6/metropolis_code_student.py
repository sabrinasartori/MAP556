import numpy as np 
import matplotlib.pyplot as plt




def potential_function(x):
    return 0.2 * np.sum(x**2) + 0.5*np.sum(np.log(1+(x**2-2)**2))


def random_walk_metropolis(num_samples, proposal_sd, x0):
    dimx = x0.shape[0]
    samples = np.zeros((num_samples, dimx))
    acceptance = np.zeros(num_samples+1)
    current_x = x0
    for i in range(num_samples):
        # Generate proposals
        
        # Compute acceptance probabilities
        
        # Accept proposals
        

    acceptance_rate = acceptance[1:]
    return samples, acceptance_rate 


def independance_metropolis(num_samples, proposal_sd, x0):
    dimx = x0.shape[0]
    samples = np.zeros((num_samples, dimx))
    acceptance = np.zeros(num_samples+1)
    current_x = x0
    for i in range(num_samples):
        # Generate proposals
        
        # Compute acceptance probabilities
        
        # Accept proposals
        
        
    acceptance_rate = acceptance[1:]
    return samples, acceptance_rate



