# kamaka.py
# helper module to store common functions

from qiskit import *

import numpy as np

def cleanup_matrix(mx: list, norm: float) -> np.array:
    cleaned = np.array([[int(x.real / norm) for x in row] for row in mx])
    cleaned = str(cleaned).replace('\n', '').replace('   ', '  ').replace(']', ']\n')
    return np.array(cleaned)

def trim_matrix(mx: list, dim: int) -> np.array:
    """ Takes an nxn matrix and returns a reduced matrix of dimension dim x dim
    corresponding to the upper-left square of the original matrix"""
    trimmed = [[x for idx, x in enumerate(row) if idx < dim] for index, row in enumerate(mx) if index < dim]
    return np.array(trimmed)

def refresh(size: int, reg_name='q', circ_name='qc') -> (QuantumRegister, QuantumCircuit):
    reg = QuantumRegister(size, name=reg_name)
    circ = QuantumCircuit(reg, name=circ_name)
    
    return reg, circ