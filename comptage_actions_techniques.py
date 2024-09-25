"""
Count AT

This script displays data from a .npz files

Usage :
    `comptage_actions_techniques.py filename`

Parameter
---------
filename : string
    path to the .npz file containing the data to count AT 
"""

import numpy as np
import cv2
import sys
from scipy.signal import find_peaks

# Script
if __name__ == "__main__":
	# Load data form file
	data = np.load(sys.argv[1])['arr_0']
	nb_frames = data.shape[0]
    
	# Normalize data to display
	data = data / np.max(data)
    
	# Compute differences
	differences = np.abs(data[1:nb_frames] - data[0:nb_frames-1])
	differences = np.reshape(differences, (differences.shape[0], differences.shape[1]*differences.shape[2]*differences.shape[3]))
	differences = np.sum(differences, axis=1).astype(int)
		
	peaks_indices = find_peaks(differences, distance=10)
	peaks_indices = peaks_indices[0]
	filtered_peaks_indices = [item for item in peaks_indices if differences[item] > np.quantile(differences, 0.75)]
	
	nb_actions = len(filtered_peaks_indices)
	print(f"{nb_actions} actions techniques répertoriées")
    #np.savetxt('diff2.txt',differences, fmt='%d')

