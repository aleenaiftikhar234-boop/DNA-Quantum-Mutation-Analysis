import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, proton_mass, electron_volt, Boltzmann
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

class DNAQuantumMutationEngine:
    def __init__(self):
        # Physical constants
        self.m = proton_mass
        
        # Spatial grid (Angstroms to Meters)
        self.xmin = -1.5e-10
        self.xmax = 1.5e-10
        self.N = 2000 # Grid points
        self.x = np.linspace(self.xmin, self.xmax, self.N)
        self.dx = self.x[1] - self.x[0]

        # Potential parameters for G-C hydrogen bond
        self.a = 7e20 
        self.b = 0.35e-10 

    def potential(self):
        """Double-well potential representing the DNA hydrogen bond."""
        return self.a * (self.x**2 - self.b**2)**2

    def build_hamiltonian(self):
        """Constructs the Hamiltonian matrix using Finite Difference Method."""
        V = self.potential()
        kinetic_coeff = hbar**2 / (2 * self.m * self.dx**2)
        
        main_diag = 2 * kinetic_coeff + V
        off_diag = np.ones(self.N - 1) * (-kinetic_coeff)
        
        H = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format="csr")
        return H

    def solve(self, n_states=4):
        """Solves the Schrödinger Equation for the lowest energy states."""
        H = self.build_hamiltonian()
        energies, states = eigsh(H, k=n_states, which='SM')
        
        # Sort by energy
        idx = np.argsort(energies)
        return energies[idx], states[:, idx]

    def analyze(self):
        """Calculates tunneling frequency and mutation risk."""
        energies, _ = self.solve()
        delta_E = energies[1] - energies[0] # Energy splitting
        tau = hbar / delta_E               # Tunneling time scale
        freq = 1 / tau                     # Frequency in Hz
        
        if freq < 1e8: status = "Stable (Low Risk)"
        elif freq < 1e11: status = "Metastable (Medium Risk)"
        else: status = "Quantum Instability (High Mutation Risk)"
        
        return freq, status, energies

# --- EXECUTION ---
engine = DNAQuantumMutationEngine()
freq, status, energies = engine.analyze()
_, states = engine.solve()

# Print the Report
print("-" * 40)
print("🧬 DNA QUANTUM MUTATION ANALYSIS")
print("-" * 40)
print(f"Tunneling Frequency: {freq:.2e} Hz")
print(f"Mutation Risk:      {status}")
print(f"Ground State Energy: {energies[0]/electron_volt:.4f} eV")
print("-" * 40)

# Visualization
plt.figure(figsize=(10, 6))
V_plot = engine.potential() / electron_volt
plt.plot(engine.x * 1e10, V_plot, color='black', lw=2, label="DNA Potential Barrier")

for i in range(3):
    # Scale wavefunctions for visibility on the energy plot
    psi = states[:, i]
    psi_rescaled = (psi / np.max(np.abs(psi))) * 0.05 
    plt.plot(engine.x * 1e10, psi_rescaled + (energies[i]/electron_volt), 
             label=f"Quantum State ψ{i}")

plt.title("Proton Tunneling Simulation in DNA Base Pair")
plt.xlabel("Position (Ångströms)")
plt.ylabel("Energy (electron-Volts)")
plt.ylim(min(energies/electron_volt)-0.1, max(energies/electron_volt)+0.5)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
