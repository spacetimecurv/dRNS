This folder contains all the sequences, that were created with a modified version of the public RNS code (https://github.com/cgca/rns) implemented in the NR code BAM. This version can handle differentially rotating neutron stars, 
that are parametrized by the rotation parameter A, and the axis ratio rp/re. We created sequences in the ranges A=[0.05,1.0] in 0.05 steps and for axis ratios in the range rp/re=[0.35,0.95] in steps of 0.05. This makes in total 260 different models.
For a given pair of (A,rp/re) we have created the initial data using RNS at different central energy densities to find the maximum. To read in all the files, use the sequences.py file in the repo. The parameters in the file ordered by column are:

  - rho_c: central density
  - e_c: central energy density
  - M: baryonic mass
  - M_0: rest mass
  - R_e: equatorial radius
  - J: angular momentum
  - T/W: binding energy
  - Omega_c: angular frequency in the center
  - Omega_e: angular frequency at the equator
  - Omega_K: Kepler angular frequency
  - J/M^2: spin
  - rp/re: axis ratio
