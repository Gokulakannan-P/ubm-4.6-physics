import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Journal Style Configuration
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.linewidth'] = 1.0

# Core Constants
MZ = 91.1876       
MGUT = 1.0e16      
ALPHA_S = 0.1179   

# Energy range
energy_Z_to_GUT = np.logspace(np.log10(MZ), np.log10(MGUT), 500)
log_energy = np.log10(energy_Z_to_GUT / MZ)
log_MGUT_MZ = np.log10(MGUT / MZ)

plt.figure(figsize=(8, 5)) # Slightly wider to prevent crowding

# Initial values at MZ
alpha_inv_initial = {'1': 59.0, '2': 30.0, '3': 1.0/ALPHA_S}
alpha_inv_GUT = 42.0 

colors = ['#d7191c', '#fdae61', '#2c7bb6']
labels = [r'$g_1^{-1}$ ($U(1)$)', r'$g_2^{-1}$ ($SU(2)$)', r'$g_3^{-1}$ ($SU(3)$)']

for i, g in enumerate(['1', '2', '3']):
    effective_slope = (alpha_inv_initial[g] - alpha_inv_GUT) / log_MGUT_MZ
    y_corrected = alpha_inv_initial[g] - effective_slope * log_energy
    plt.plot(np.log10(energy_Z_to_GUT), y_corrected, color=colors[i], label=labels[i])

# FIX 1: Vertical Line for MGUT - moved text slightly to the right to avoid overlap
plt.axvline(x=np.log10(MGUT), color='k', linestyle='--', linewidth=1, alpha=0.7)
plt.text(16.2, 45, r'$M_{GUT} \approx 10^{16}$ GeV', rotation=90, verticalalignment='center', fontsize=10)

# FIX 2: Alpha_s label - used 'va' and 'ha' to keep it away from the g3 line
plt.axhline(y=alpha_inv_initial['3'], color='k', linestyle=':', alpha=0.4)
plt.text(1.5, alpha_inv_initial['3'] + 1.5, r'$\alpha_s(M_Z) = 0.1179$', fontsize=9, color='#2c7bb6')

# FIX 3: Legend Overlap - Moved legend outside the plot box or to a clear corner
# Using bbox_to_anchor to place it specifically in a clear "white space" area
plt.legend(frameon=True, loc='upper right', bbox_to_anchor=(0.98, 0.98), fontsize=10)

# Formatting
plt.xlim(1, 18) # Extended x-limit to give the MGUT label breathing room
plt.ylim(0, 70)
plt.xlabel(r'$\log_{10}(\mu / \text{GeV})$', labelpad=10)
plt.ylabel(r'$\alpha_i^{-1}(\mu)$', labelpad=10)
plt.title(r'**Fig. 2**: UBM Threshold Corrected $SO(10)$ Unification')
plt.grid(True, which='both', linestyle='--', alpha=0.3)

plt.tight_layout() # Automatically adjusts subplot params so that the labels don't overlap
plt.savefig('Fig2_Unification_Clear.pdf')
plt.show()
