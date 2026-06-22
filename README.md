# Computational Modeling of Proton Tunneling in an Asymmetric DNA Base Pair Potential

An exploratory one-dimensional quantum mechanical simulation solving the Time-Independent Schrödinger Equation (TISE) to analyze proton tunneling dynamics in a Guanine-Cytosine (G-C) DNA base pair using sparse finite-difference methods.

## 📌 Project Overview
This repository contains a Python-based physical model designed to simulate the quantum behavior of a hydrogen-bond proton along a 1D reaction coordinate between DNA bases. By moving past simple symmetric approximations and implementing an analytical asymmetric quartic surface, the solver computes the lowest-energy eigenstates ($\psi_0$ and $\psi_1$), their corresponding eigenvalues, spatial probability distribution dynamics, and the characteristic coherent oscillation frequency ($\nu$) of the isolated system. 

This model serves as an educational and exploratory framework for studying quantum effects in biological systems (quantum biology), specifically investigating the theoretical mechanisms of spontaneous tautomeric mutations originally proposed by Per-Olov Löwdin in 1963.

## 🚀 Features
* **Asymmetric Double-Well Potential:** Reflects a realistic G-C potential energy landscape by utilizing an analytical asymmetric quartic surface: $V(x) = a(x^2 - b^2)^2 + cx$.
* **High-Tolerance Sparse Matrix Solver:** Discretizes the spatial domain into $N = 1400$ grid points and uses a second-order central finite difference method to construct the Hamiltonian. Eigenvalues are solved via `scipy.sparse.linalg.eigsh` with a strict convergence tolerance (`tol=1e-10`).
* **Spatial Probability Diagnostics:** Computes continuous numerical integrals to determine the exact localization probability of the proton in both the left (canonical) and right (rare tautomer) wells.
* **Automated Convergence Testing:** Programmatically reviews solver stability across various grid setups ($N=1000, 1400, 1800$) to guarantee discretization safety limits.
* **Publication-Quality Plotting:** Automatically generates and saves an energy-scaled visualization of the wavefunctions superimposed onto the potential energy surface.

## 📊 Core Simulation Metrics
Using the exploratory model parameters ($a = 1.50, b = 0.35, c = 0.05$):

| Metric / Quantity | Numerical Value |
| :--- | :--- |
| Ground-state Energy ($E_0$) | 0.035248 eV |
| First Excited-state Energy ($E_1$) | 0.070790 eV |
| Energy Splitting ($\Delta E$) | 0.035542 eV |
| Coherent Frequency ($\nu$) | 8.594 THz ($8.594 \times 10^{12}$ Hz) |
| Ground State ($\psi_0$) Localization | Left Well: 99.69% \| Right Well: 0.31% |
| Excited State ($\psi_1$) Localization | Left Well: 0.31% \| Right Well: 99.69% |

## 🛡️ Numerical Stability & Verification
To ensure results are free of mathematical grid constraints, the framework automatically executes verification loops:

1. **Grid Discretization Convergence ($N=1000$ to $N=1800$):** Calculated eigenvalues ($\mathit{E}_0$, $\mathit{E}_1$) remain invariant up to six decimal places, ensuring that the model solutions are perfectly independent of grid resolution scales.
2. **Boundary Wall Leakage Verification:** Wavefunction amplitude traces evaluate to $< 10^{-12}$ at the domain limits ($\pm1.4$ Å), confirming that the infinite potential wall boundaries do not introduce artificial solution artifacts or clamp constraints.

## 🛠️ Prerequisites & Installation
Ensure you have Python 3.8+ installed along with the required scientific computing libraries:

```bash
pip install numpy scipy matplotlib

​🧬 Scientific Limitations
​As noted in the accompanying manuscript, this is an isolated, exploratory model with specific limits:
​Decoherence: The system simulates absolute zero in a vacuum. It does not factor in environmental coupling or open quantum system interactions at physiological temperatures (310 K), which would introduce rapid quantum decoherence.
​Coherent Frequency vs. Mutation Rates: The computed THz frequency describes rapid quantum fluctuations rather than a direct biological point mutation rate or biological probability over time.
​Static Geometry: The donor-acceptor length is kept fixed, neglecting helical breathing modes and environmental DNA backbone fluctuations.
​📄 License
​This project is open-source and available under the MIT License.
