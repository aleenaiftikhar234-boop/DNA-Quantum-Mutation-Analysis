# Computational Modeling of Proton Tunneling in an Asymmetric DNA Base Pair Potential

An exploratory one-dimensional quantum mechanical simulation solving the Time-Independent Schrödinger Equation (TISE) to analyze proton tunneling dynamics in a Guanine-Cytosine (G-C) DNA base pair using finite-difference methods.

## 📌 Project Overview
This project models the quantum behavior of a hydrogen-bond proton along a 1D reaction coordinate. By introducing a physically realistic asymmetric quartic potential, the solver computes the lowest-energy eigenstates ($\psi_0$ and $\psi_1$), their corresponding eigenvalues, spatial probabilities, and the characteristic coherent oscillation frequency ($\nu$) of the isolated system. 

This model serves as an educational and exploratory framework for studying quantum effects in biological systems (quantum biology), specifically looking at the theoretical background of spontaneous tautomeric mutations as proposed by Per-Olov Löwdin.

## 🚀 Features
* **Asymmetric Double-Well Potential:** Moves beyond simple symmetric approximations by implementing an analytical asymmetric quartic surface: $V(x) = a(x^2 - b^2)^2 + cx$.
* **Sparse Matrix Numerical Solver:** Discretizes the spatial domain into $N = 1400$ grid points and uses a second-order central finite difference method to construct the Hamiltonian.
* **Spatial Diagnostics:** Computes high-fidelity continuous integrals to determine the localization probability of the proton in both the left (canonical) and right (rare tautomer) wells.
* **Publication-Quality Plotting:** Automatically generates and saves an energy-scaled visualization of the wavefunctions superimposed onto the potential energy surface.

## 📊 Core Simulation Metrics
Using the default exploratory parameters ($a = 1.50, b = 0.35, c = 0.05$):

| Metric / Quantity | Value |
| :--- | :--- |
| Ground-state Energy ($E_0$) | 0.035248 eV |
| First Excited-state Energy ($E_1$) | 0.070790 eV |
| Energy Splitting ($\Delta E$) | 0.035542 eV |
| Coherent Frequency ($\nu$) | 8.594 THz ($8.594 \times 10^{12}$ Hz) |
| Ground State ($\psi_0$) Localization | Left Well: 99.69% | Right Well: 0.31% |
| Excited State ($\psi_1$) Localization | Left Well: 0.31% | Right Well: 99.69% |

## 🛠️ Prerequisites & Installation
Ensure you have Python 3.8+ installed along with the required scientific computing libraries:

```bash
pip install numpy scipy matplotlib
