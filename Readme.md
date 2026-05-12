​🌟 Overview
​BioQuantum-TunnelSim is a computational physics engine designed to simulate the quantum behavior of protons within the hydrogen bonds of DNA (specifically the Guanine-Cytosine pair).
​This project explores the Löwdin Hypothesis, which suggests that protons can "tunnel" across the energy barrier of a hydrogen bond, leading to tautomeric shifts. If DNA replication occurs while a proton is in this "wrong" position, it results in a permanent genetic mutation.
​🔬 Scientific Background
​In a classical world, a proton lacks the energy to jump the potential barrier between DNA bases. However, due to Quantum Tunneling, there is a non-zero probability that the proton will pass through the barrier.
​Key Features:
​Schrödinger Solver: Solves the Time-Independent Schrödinger Equation (TISE) using the Finite Difference Method.
​Quartic Double-Well Potential: Models the specific geometry of the N-H...N bond.
​Thermal Analysis: Compares quantum tunneling rates against classical Boltzmann distribution "jumps" at human body temperature (310K).
​Risk Assessment: Categorizes mutation probability based on calculated tunneling frequencies.
​🧮 Mathematical Model
​The engine utilizes a Hamiltonian matrix \hat{H} defined as:
\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(x)Where the potential V(x) is modeled as:
V(x)=a(x²-b²)²
​a: Barrier stiffness (derived from Slocombe et al. 2021).
​b: Half-distance of the hydrogen bond separation (\approx 0.35 Å).
​📊 Sample Output
​The simulation generates a visualization showing:
​The Potential Energy Barrier (Black line).
​The Ground State (\psi_0) and First Excited State (\psi_1) wavefunctions.
​The Energy Splitting (\Delta E), which determines the tunneling frequency.
​🎓 About the Author
​Aleena baig
​📍 Srinagar, Jammu & Kashmir
​
​🔍 Research Interests: Quantum Biology, Computational Neuroscience, and Theoretical Physics.
​📜 References
​Löwdin, P. O. (1963). "Proton Tunneling in DNA and its Biological Implications."
​Slocombe, L., et al. (2021). "Quantum and classical effects in DNA point mutations." Physical Chemistry Chemical Physics.