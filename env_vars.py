"""
Variaveis de Ambiente
"""
import os
stage = os.environ['STAGE'].upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "PERIGO !!! " + output
    
print(output)