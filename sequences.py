###########################################
# Small script to read in the sequence    #
#     files, with small examples          #
###########################################

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import os

sequences = {}
sequences_intp = {}

# your path to the sequence files once downlaoded
parent_path = ""

for file in sorted(os.listdir(parent_path),reverse=True):
    key = file.split(sep=".")[0]
    A = key.split("A")[1].split("r")[0]
    r = key.split("A")[1].split("r")[1]

    # convert to better key format
    r = r[0] + "." + r[1:]
    if "0" == A[0]:
        A = A[0] + "." + A[1:]
    else:
        A = A[0] + ".0"

    # initialize nested dictionary
    if A not in sequences:
        sequences[A] = {}

    with open(f"/path/to/sequences/{key}.txt", "r") as file:
        stor_arr = []
        file.readline()
        for line in file:
            values = line.split()
            stor_arr.append([float(val) for val in values])
        sequences[A][r] = np.array(stor_arr)

# interpolate between the arrays to get the more accurate sequences - TAKES SOME TIME
rho_c_array = np.linspace(0.00005,0.005,200)
for key in sequences.keys():
    # same as before, initialize nested dictionary
    if key not in sequences_intp:
        sequences_intp[key] = {}

    # loop over the different axis ratios
    for keyr in sequences[key].keys():
        global_array = []
        for i in range(len(rho_c_array)):
            storing_array = []
            for j in range(len(sequences[key][keyr][0,:])):
                if j != 0:
                    f = interpolate.interp1d(sequences[key][keyr][:,0],sequences[key][keyr][:,j],kind="quadratic",fill_value="extrapolate")
                    storing_array.append(float(f(rho_c_array[i])))
                else:
                    storing_array.append(rho_c_array[i])

            global_array.append(storing_array)
        sequences_intp[key][keyr] = np.array(global_array)

# dictionary first key is the rotation parameter and the second the axis ratio
# Example: to get the sequence for A=1.0 and rp/re=0.35, type
print(sequences_intp["1.0"]["0.35"])

# What you will get is a 2D array where each column corresponds to the column in the sequence file.
# So here, we have: rho_c, e_c, M, M_0, R_e, J, T/W, Omega_c, Omega_e, Omega_K, J/M^2, rp/re.
# Example: To axis all the entries at various central energy densities of the mass, type
print(sequences_intp["1.0"]["0.35"][:,2])

# A sequence can be plotted in the rho_c-M plane with the following
plt.plot(sequences_intp["1.0"]["0.35"][:,0],sequences_intp["1.0"]["0.35"][:,2],color="red")
plt.xlabel(r"$\rho_c$",fontsize=12)
plt.ylabel(r"$M\ [M_{\odot}]$",fontsize=12)
plt.show()
