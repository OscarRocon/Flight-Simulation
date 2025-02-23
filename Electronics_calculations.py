def calculate_rpm(KV, V_supply):
    """
    Calculate the motor's RPM based on KV rating and supplied voltage.
    
    Parameters:
    KV (float): Motor KV rating (RPM per volt)
    V_supply (float): Voltage supplied to the motor (in volts)
    
    Returns:
    float: Motor RPM
    """
    return KV * V_supply

def calculate_thrust(RPM, C_T=1e-7):
    """
    Calculate the thrust force generated by the propeller.
    
    Parameters:
    RPM (float): Motor RPM
    C_T (float): Thrust coefficient based on propeller characteristics (default is 1e-7)
    
    Returns:
    float: Thrust force in Newtons
    """
    return C_T * (RPM ** 2)

def calculate_acceleration(thrust, mass):
    """
    Calculate the acceleration of the plane based on thrust and mass.
    
    Parameters:
    thrust (float): Thrust force in Newtons
    mass (float): Mass of the airplane in kg
    
    Returns:
    float: Acceleration in m/s^2
    """
    return thrust / mass

