# 🧬 Q-Mutate: DNA Quantum Mutation Engine
### *Investigating Proton Tunneling in G-C Base Pairs*

[![Field: Quantum Biology](https://img.shields.io/badge/Field-Quantum%20Biology-blueviolet)](https://en.wikipedia.org/wiki/Quantum_biology)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue)](https://www.python.org/downloads/)
[![Project: Bal Puraskar 2026](https://img.shields.io/badge/Project-Bal%20Puraskar-gold)](#)

---

## 🌟 Overview
**Q-Mutate** is a computational physics engine designed to simulate the quantum behavior of protons within the hydrogen bonds of DNA. This project explores the **Löwdin Hypothesis**, which suggests that protons can "tunnel" across energy barriers, leading to tautomeric shifts and spontaneous genetic mutations.

---

## 🔬 Scientific Background
In a classical model, a proton lacks the energy to "jump" the potential barrier between DNA bases. However, through **Quantum Tunneling**, there is a non-zero probability of the proton passing through the barrier.

### Key Features:
* **Schrödinger Solver:** Solves the Time-Independent Schrödinger Equation (TISE) using the Finite Difference Method.
* **Quartic Double-Well Potential:** Accurately models the $N-H...N$ bond geometry.
* **Thermal Analysis:** Compares quantum tunneling rates against classical Boltzmann distributions at human body temperature (310K).
* **Risk Scoring:** Categorizes mutation probability based on calculated tunneling frequencies.

---

## 🧮 Mathematical Model
The engine utilizes a Hamiltonian matrix $\hat{H}$ defined as:

$$\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(x)$$

The potential $V(x)$ is modeled as a Quartic Double-Well:

$$V(x) = a(x^2 - b^2)^2$$

**Parameters:**
* **a**: Barrier stiffness (derived from Slocombe et al. 2021).
* **b**: Half-distance of the hydrogen bond separation ($\approx 0.35$ Å).

---

## 🚀 Installation & Usage
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/aleenaiftikhar234-boop/DNA-Quantum-Mutation-Analysis.git](https://github.com/aleenaiftikhar234-boop/DNA-Quantum-Mutation-Analysis.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install numpy scipy matplotlib
    ```
3.  **Run the analysis:**
    ```bash
    python dna_quantum_sim.py
    ```

---

## 📊 Results
The simulation identifies the energy splitting ($\Delta E$) between the ground state ($\psi_0$) and the first excited state ($\psi_1$). This splitting is directly used to calculate the **Tunneling Frequency**, providing a quantitative measure of mutation risk.

---

## 🎓 About the Author
**Aleena Baig**
* 📍 Srinagar, Jammu & Kashmir
* 🔍 Research Interests: Quantum Biology, Computational Neuroscience, and Theoretical Physics.

---

## 📜 References
* Löwdin, P. O. (1963). "Proton Tunneling in DNA and its Biological Implications."
* Slocombe, L., et al. (2021). "Quantum and classical effects in DNA point mutations." *Physical Chemistry Chemical Physics*.
