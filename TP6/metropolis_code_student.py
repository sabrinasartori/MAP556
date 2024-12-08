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
        proposal = current_x + np.random.normal(0, proposal_sd, size=dimx)
        # Compute acceptance probabilities
        curr_target = np.exp(-potential_function(current_x))
        prop_target = np.exp(-potential_function(proposal))
        accept_proba = min(1, prop_target/curr_target)
        # Accept proposals
        if np.random.rand() < accept_proba:
            acceptance[i+1] = 1
            current_x = proposal
        samples[i] = current_x

    acceptance_rate = acceptance[1:]
    return samples, acceptance_rate 


def independance_metropolis(num_samples, proposal_sd, x0):
    dimx = x0.shape[0]
    samples = np.zeros((num_samples, dimx))
    acceptance = np.zeros(num_samples+1)
    current_x = x0
    for i in range(num_samples):
        # Generate proposals
        proposal = np.random.normal(0, proposal_sd, size=dimx)
        # Compute acceptance probabilities
        curr_target = np.exp(-potential_function(current_x))
        prop_target = np.exp(-potential_function(proposal))
        curr_q = np.exp(-np.sum(current_x)**2/(2*proposal_sd))
        prop_q = np.exp(-np.sum(proposal)**2/(2*proposal_sd))
        accept_proba = min(1, prop_target/curr_target * curr_q/prop_q)
        # Accept proposals
        if np.random.rand() < accept_proba:
            acceptance[i+1] = 1
            current_x = proposal
        samples[i] = current_x
        
    acceptance_rate = acceptance[1:]
    return samples, acceptance_rate



