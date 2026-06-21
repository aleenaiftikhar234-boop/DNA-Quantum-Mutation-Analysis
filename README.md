# Computational Modeling of Proton Tunneling in an Asymmetric DNA Base Pair Potential

**Author:** Aleena Baig  
**Project Type:** Exploratory Computational Research  
**Language:** Python

An exploratory computational physics project that numerically solves the **one-dimensional Time-Independent Schrödinger Equation (TISE)** to investigate proton tunneling in an idealized **Guanine–Cytosine (G-C) DNA hydrogen bond** using finite-difference methods.

---

## 📌 Project Overview

Quantum mechanical proton tunneling has long been proposed as a possible mechanism contributing to rare tautomeric states in DNA. This project explores that idea through a simplified one-dimensional numerical model.

The simulation represents proton motion along a single reaction coordinate within an **idealized asymmetric quartic double-well potential**. By solving the Schrödinger equation, it computes the lowest-energy eigenstates, their corresponding energies, spatial probability distributions, and the characteristic coherent oscillation frequency of the isolated system.

This repository is intended as an educational and exploratory demonstration of computational quantum mechanics and should **not** be interpreted as a quantitatively predictive model of biological DNA.

---

## 🚀 Features

- ✅ Numerical solution of the **1D Time-Independent Schrödinger Equation**
- ✅ Asymmetric quartic double-well potential:
  \[
  V(x)=a(x^2-b^2)^2+cx
  \]
- ✅ Sparse finite-difference Hamiltonian construction
- ✅ Computation of the two lowest quantum eigenstates
- ✅ Energy splitting (\(\Delta E\)) calculation
- ✅ Characteristic coherent oscillation frequency estimation
- ✅ Left/right spatial probability diagnostics
- ✅ Automatic generation of publication-quality figures

---

## 📊 Example Simulation Output

Using the default illustrative parameters:

- **Barrier parameter:** `a = 1.50`
- **Well separation parameter:** `b = 0.35`
- **Asymmetry parameter:** `c = 0.05`

| Quantity | Example Value |
|----------|--------------:|
| Ground-state Energy (\(E_0\)) | 0.035248 eV |
| First Excited-state Energy (\(E_1\)) | 0.070790 eV |
| Energy Splitting (\(\Delta E\)) | 0.035542 eV |
| Characteristic Frequency (\(\nu\)) | \(8.594 \times 10^{12}\) Hz (8.594 THz) |
| Ground-state Left Probability | 99.69% |
| Ground-state Right Probability | 0.31% |
| Excited-state Left Probability | 0.31% |
| Excited-state Right Probability | 99.69% |

*These values correspond to the default illustrative parameter set and may change if the model parameters are modified.*

---

## 🧮 Mathematical Model

The proton is modeled by solving

\[
\left(
-\frac{\hbar^2}{2m}
\frac{d^2}{dx^2}
+
V(x)
\right)\psi(x)
=
E\psi(x)
\]

where

\[
V(x)=a(x^2-b^2)^2+cx
\]

- **a** controls the barrier height.
- **b** controls the approximate separation of the wells.
- **c** introduces asymmetry between the two wells.

The Hamiltonian is discretized using a second-order central finite-difference approximation and diagonalized using SciPy's sparse eigensolver.

---

## 📈 Output

Running the simulation computes:

- Ground-state energy
- First excited-state energy
- Energy splitting
- Characteristic coherent oscillation frequency
- Left/right spatial probability distributions

It also generates a figure (`q_mutate_publication_figure.png`) displaying:

- The asymmetric potential energy surface
- The lowest two quantum eigenstates
- Their corresponding energy levels

---

## 📂 Repository Structure

```text
.
├── q_mutate_core.py
├── README.md
├── q_mutate_publication_figure.png
└── paper.pdf   (optional)
```

---

## 🛠️ Installation

Install the required dependencies:

```bash
pip install numpy scipy matplotlib
```

Python 3.8 or later is recommended.

---

## ▶️ Running the Simulation

Execute:

```bash
python q_mutate_core.py
```

The program will:

1. Construct the finite-difference Hamiltonian.
2. Compute the two lowest eigenstates.
3. Calculate energies and localization probabilities.
4. Estimate the characteristic oscillation frequency.
5. Generate and save the visualization figure.

---

## ⚠️ Scientific Scope and Limitations

This project is an **exploratory educational model** and intentionally makes several simplifying assumptions.

Specifically, it:

- Uses a **one-dimensional** reaction coordinate.
- Employs an **analytical asymmetric quartic potential** rather than one derived from density functional theory (DFT) or other ab initio calculations.
- Treats the surrounding molecular framework as static.
- Does **not** include solvent effects, thermal fluctuations, or quantum decoherence.
- Does **not** simulate DNA polymerase interactions or DNA replication.
- Does **not** predict biological mutation rates.

Accordingly, the calculated coherent oscillation frequencies should **not** be interpreted as mutation frequencies or direct biological observables.

---

## 🎓 Educational Purpose

This repository demonstrates concepts from:

- Quantum mechanics
- Computational physics
- Numerical methods
- Sparse linear algebra
- Finite-difference discretization
- Scientific computing with Python

It is intended as a learning resource and exploratory research tool for students interested in quantum modeling and quantum biology.

---

## 📚 References

The project draws inspiration from foundational work on proton tunneling and quantum biology, including studies by:

- Per-Olov Löwdin
- Watson & Crick
- Lambert et al.
- Slocombe, Sacchi & Al-Khalili
- Brovarets' & Hovorun
- Villani

Please consult the accompanying manuscript for the complete bibliography.

---

## 📄 License

This project may be released under the **MIT License**, allowing use, modification, and distribution with appropriate attribution.

---

## 📢 Disclaimer

This software is intended for **educational and exploratory research purposes only**. The underlying model is highly simplified and is not intended to provide a quantitatively accurate description of proton dynamics in biological DNA or evidence for specific mutation mechanisms under physiological conditions.
