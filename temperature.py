import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create the temperature input variable
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')

# Define membership functions for the temperature variable
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['comfortable'] = fuzz.trimf(temperature.universe, [20, 50, 80])
temperature['hot'] = fuzz.trimf(temperature.universe, [50, 100, 100])

# Create the control output variable
compressor_speed = ctrl.Consequent(np.arange(0, 101, 1), 'compressor_speed')

# Define membership functions for the compressor speed variable
compressor_speed['low'] = fuzz.trimf(compressor_speed.universe, [0, 0, 50])
compressor_speed['medium'] = fuzz.trimf(compressor_speed.universe, [20, 50, 80])
compressor_speed['high'] = fuzz.trimf(compressor_speed.universe, [50, 100, 100])

# Create the fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], compressor_speed['high'])
rule2 = ctrl.Rule(temperature['comfortable'], compressor_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], compressor_speed['low'])

# Create the fuzzy control system
air_conditioner_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create the simulation
air_conditioner_sim = ctrl.ControlSystemSimulation(air_conditioner_ctrl)

# Set the input temperature
air_conditioner_sim.input['temperature'] = 75

# Compute the result
air_conditioner_sim.compute()

# Print the output compressor speed
print("Output Compressor Speed:", air_conditioner_sim.output['compressor_speed'])

# Plot the membership functions and the result
temperature.view()
compressor_speed.view()
