# 🧬 Q-Mutate: DNA Quantum Mutation Engine
### Investigating Proton Tunneling Dynamics in G-C Base Pairs Using Finite Difference TISE Solvers

**Author:** Aleena Baig  
**Affiliation:** Mallinson Girls' School, Srinagar, Jammu & Kashmir, India  
**Field:** Quantum Biology, Computational Physics  
**Language:** Python (NumPy, SciPy, Matplotlib)

---

## 🔬 Overview
**Q-Mutate** is a high-fidelity computational physics engine designed to simulate and analyze the quantum mechanical behavior of protons within the localized hydrogen bonds of DNA molecules. 

The project evaluates the **Löwdin Hypothesis**, which proposes that a proton sitting within a nucleotide base pair has a non-zero probability of tunneling across its classical potential barrier. If this translocation occurs immediately prior to or during the unwinding of the double helix for replication, the base pair undergoes a rare tautomeric shift (e.g., Guanine moving from its standard keto state to its rare enol form). This causes replication machinery to misread the template, driving spontaneous point mutations.

---

## 🌌 Scientific Background
In a purely classical model, a proton lacks the kinetic or thermal energy required to cross over the high electrostatic potential barrier separating the two nucleotide bases. However, by treating the proton as a quantum wavepacket, there is a non-zero transmission probability through the barrier.

### Key Engine Features:
* **Schrödinger Grid Solver:** Solves the 1D Time-Independent Schrödinger Equation (TISE) using numerical matrix discretization.
* **Quartic Double-Well Potential:** Models the precise structural configuration of the localized $N-H\cdots N$ hydrogen bond landscape.
* **Automated Calibration Loop:** Automatically optimizes double-well constraints to systematically isolate a precise energy splitting window ($\Delta E \approx 0.004 \text{ eV}$).
* **Frequency Analytics:** Converts spatial splitting margins into physical terahertz-scale tunneling rates to quantify background mutation mechanics.

---

## 🧮 Mathematical Architecture
The system establishes a discrete Hamiltonian matrix operator ($\hat{H}$) expressed via:

$$\hat{H} = -\frac{\hbar^2}{2m_p}\nabla^2 + V(x)$$

The electrostatic interaction landscape is modeled as a symmetric/asymmetric Quartic Double-Well Potential Surface:

$$V(x) = a(x^2 - b^2)^2$$

### Converged Structural Parameters:
Following numerical calibration constraints targeting stable spatial intervals, the optimization loop settles on:
* **$a$ (Barrier Stiffness Factor):** `2.887676` $\text{eV}/\text{Å}^4$
* **$b$ (Half-Distance of Hydrogen Bond Separation):** `0.470955` $\text{Å}$
* **$V_{\text{max}}$ (Calculated Central Barrier Height):** $\approx 0.142 \text{ eV}$

The continuous second-order spatial derivative is mapped across $N = 1400$ discrete grid sections utilizing a second-order central finite difference framework:

$$\frac{d^2\psi}{dx^2} \approx \frac{\psi(x + dx) - 2\psi(x) + \psi(x - dx)}{dx^2}$$

---

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/aleena-baig/q-mutate.git](https://github.com/aleena-baig/q-mutate.git)
cd q-mutate

