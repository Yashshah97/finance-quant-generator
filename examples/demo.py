"""Demo for Finance Quant Synthetic Data Generator."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import finance_quant_generator

print("Finance Quant Synthetic Data Generator", "v" + finance_quant_generator.__version__)
print("modules:", [m for m in dir(finance_quant_generator) if not m.startswith('_')])
