# UBM-4.6-EFT: Unified Buffer Model Verification

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18850771.svg)](https://doi.org/10.5281/zenodo.18850771)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the official numerical verification scripts and Monte Carlo simulations for the manuscript: **"Unified Buffer Model 4.6: A Degenerate Higher-Order Scalar-Tensor EFT for Gauge Unification and Flavor Topology"** (Submitted to *Physical Review D - Letters*).

## Overview
The Unified Buffer Model (UBM) 4.6 is a Class Ia DHOST Effective Field Theory that formally resolves the non-SUSY $SO(10)$ unification gap via a scalar-tensor threshold coupling ($\xi \approx -1.21 \times 10^{-12}$). This repository provides the exact Python code used to generate the manuscript's figures, proving the kinetic stability of the vacuum and forecasting a falsifiable spacecraft flyby anomaly.

## Key Predictables & Results
* **Strong Coupling:** Matches PDG 2024 boundary $\alpha_s(M_Z) = 0.1179$.
* **CP Violation:** Predicts a low-energy leptonic phase of $\delta_{CP} \approx 1.32\pi$.
* **JUICE Flyby Anomaly:** Predicts an asymmetric $+1.84 \times 10^{-8}$ Hz Ka-band Doppler blue-shift for the ESA JUICE Earth Gravity Assist-2 (September 29, 2026).

## Repository Structure & Code-to-Figure Mapping

### Visualizations (The Manuscript Figures)
* `fig1_unification.py`: Generates **Figure 1**. Simulates the 1-loop RGE flow with DHOST threshold corrections achieving exact $SO(10)$ convergence.
* `fig2_stability.py`: Generates **Figure 2**. Plots the $Q(X)$ eigenvalue, proving the kinetic density domain $X \in [0, M_P^4]$ is positive-definite and ghost-free.
* `fig3_cp_phase.py`: Generates **Figure 3**. Derives the $\delta_{CP}$ running from the topological winding boundary ($n=1$) down to the electroweak scale.
* `fig4_juice_forecast.py`: Generates **Figure 4**. Monte Carlo integration of the $A_3$ coupling predicting the JUICE spacecraft's anomalous Doppler residual.

### Ancillary Proofs
* `ancillary/01_DHOST_Stability.py`: A `SymPy` script that algebraically proves the ADM degeneracy condition ($4fA_4 + A_3^2 = 0$) holds true, eliminating the Ostrogradsky ghost.

## Installation and Usage

To reproduce the figures locally, ensure you have Python 3.8+ installed, then run:

```bash
# 1. Clone the repository
git clone [https://github.com/Bhasanpal-Thiru/ubm-4.6-physics.git](https://github.com/Bhasanpal-Thiru/ubm-4.6-physics.git)
cd ubm-4.6-physics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate a figure (e.g., Figure 4)
python fig4_juice_forecast.py
