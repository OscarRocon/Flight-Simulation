import numpy as np
import matplotlib.pyplot as plt
from Electronics_calculations import calculate_rpm, calculate_thrust, calculate_acceleration

# Ask the user for input values
mass = float(input("Enter the mass of the airplane (in Kg): "))  # Input mass directly
KV = float(input("Enter the motor KV rating: "))
V_supply = float(input("Enter the supply voltage (in Volts): "))

# Constants
g = 9.81  # Gravity constant
Cd = 0.3  # Drag coefficient
rho = 1.225  # Air density (kg/m^3)
A = 0.1  # Cross-sectional area (m^2)
C_T = 1e-7  # Thrust constant for this example
CL_max = 1.2  # Maximum lift coefficient (assumed value)
S = 0.2  # Wing area in square meters (assumed value)
dt = 0.01  # Time step (s)
total_time = 10.0  # Total simulation time

# Calculate motor RPM
RPM = calculate_rpm(KV, V_supply)
print(f"Calculated RPM: {RPM} RPM")

# Calculate thrust force using the calculated RPM
thrust = calculate_thrust(RPM, C_T)
print(f"Calculated Thrust: {thrust} N")

# Calculate acceleration based on the calculated thrust and given mass
a = calculate_acceleration(thrust, mass)
print(f"Calculated Acceleration: {a} m/s^2")

# Calculate stall speed
Vs = np.sqrt((2 * mass * g) / (rho * S * CL_max))
print(f"Stall Speed (Vs): {Vs:.2f} m/s")

# Initializing variables for the simulation
time = np.arange(0, total_time, dt)
v = 0.0
velocity = []
acceleration = []
thrust_data = [thrust] * len(time)  # Thrust remains constant over time
stall_speed_data = [Vs] * len(time)  # Stall speed as a constant line for reference

# Simulation loop
for t in time:
    D = 0.5 * Cd * rho * A * v**2  # Drag force
    G = mass * g  # Gravity force
    F_net = thrust - D - G  # Net force
    a = F_net / mass  # Acceleration
    v += a * dt  # Update velocity
    velocity.append(v)
    acceleration.append(a)

# Create a figure with a black background and arrange subplots in 2x2
fig, axs = plt.subplots(2, 2, figsize=(12, 10), facecolor='black')
fig.subplots_adjust(hspace=0.4, wspace=0.3)  # Adjust space between plots
fig.suptitle('Stallion Flight Data Simulation', color='white', fontsize=16)  # Add overall title

# Plotting the velocity data with stall speed line
axs[0, 0].plot(time, velocity, color='blue', label='Velocity')
axs[0, 0].axhline(Vs, color='red', linestyle='--', label='Stall Speed')
axs[0, 0].set_title('RC Plane Velocity Vs. Time', color='white')
axs[0, 0].set_xlabel('Time (s)', color='white')
axs[0, 0].set_ylabel('Velocity (m/s)', color='white')
axs[0, 0].tick_params(axis='x', colors='white', labelsize=12)
axs[0, 0].tick_params(axis='y', colors='white', labelsize=12)
axs[0, 0].set_facecolor('black')
axs[0, 0].grid(True, color='gray')
axs[0, 0].legend(loc='upper right', facecolor='black', labelcolor='white')

# Plotting the acceleration data
axs[0, 1].plot(time, acceleration, color='blue')
axs[0, 1].set_title('RC Plane Acceleration Vs. Time', color='white')
axs[0, 1].set_xlabel('Time (s)', color='white')
axs[0, 1].set_ylabel('Acceleration (m/s²)', color='white')
axs[0, 1].tick_params(axis='x', colors='white', labelsize=12)
axs[0, 1].tick_params(axis='y', colors='white', labelsize=12)
axs[0, 1].set_facecolor('black')
axs[0, 1].grid(True, color='gray')

# Plotting the thrust data with stall speed line
axs[1, 0].plot(time, thrust_data, color='blue', label='Thrust')
axs[1, 0].axhline(Vs, color='red', linestyle='--', label='Stall Speed')
axs[1, 0].set_title('Thrust Vs. Time', color='white')
axs[1, 0].set_xlabel('Time (s)', color='white')
axs[1, 0].set_ylabel('Thrust (N)', color='white')
axs[1, 0].tick_params(axis='x', colors='white', labelsize=12)
axs[1, 0].tick_params(axis='y', colors='white', labelsize=12)
axs[1, 0].set_facecolor('black')
axs[1, 0].grid(True, color='gray')
axs[1, 0].legend(loc='upper right', facecolor='black', labelcolor='white')

# Plotting the stall speed data alone for reference
axs[1, 1].plot(time, stall_speed_data, color='red', linestyle='--', label='Stall Speed')
axs[1, 1].set_title('Stall Speed (Constant)', color='white')
axs[1, 1].set_xlabel('Time (s)', color='white')
axs[1, 1].set_ylabel('Speed (m/s)', color='white')
axs[1, 1].tick_params(axis='x', colors='white', labelsize=12)
axs[1, 1].tick_params(axis='y', colors='white', labelsize=12)
axs[1, 1].set_facecolor('black')
axs[1, 1].grid(True, color='gray')
axs[1, 1].legend(loc='upper right', facecolor='black', labelcolor='white')

# Show the plots
plt.show()
