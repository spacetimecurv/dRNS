import numpy as np
from scipy import interpolate

sequences = {}
sequences_intp = {}

# your path to the sequence files once downloaded
parent_path = ""

# read in the files
for file in sorted(os.listdir(parent_path),reverse=True):
  key = file.split(sep=".")[0]
  with open(f"/Users/oliversteppohn/Desktop/BAM/scripts/plot/seq/{key}.txt", "r") as file:
    stor_arr = []
    file.readline()
    for line in file:
      values = line.split()
      stor_arr.append([float(val) for val in values])
    sequences[key] = np.array(stor_arr)

# interpolate between the arrays to get the more accurate sequences and find the maximum
rho_c_array = np.linspace(0.00005,0.005,200)
for key in sequences.keys():
  global_array = []
  for i in range(len(rho_c_array)):
    storing_array = []
    for j in range(len(sequences[key][0,:])):
      if j != 0:
        f = interpolate.interp1d(sequences[key][:,0],sequences[key][:,j],kind="quadratic",fill_value="extrapolate")
        storing_array.append(float(f(rho_c_array[i])))
      else:
        storing_array.append(rho_c_array[i])

    global_array.append(storing_array)
  sequences_intp[key] = np.array(global_array)

# returns a dictionary where the keys are the filenames
