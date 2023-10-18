"""
Projectile Motion with Air Resistance Calculator

This python script calculates the horizontal distance traveled by a projectile considering air resistance.
"""

import argparse
# numpy library is removed from here as it is in requirements.txt.

# Constants
GRAVITY = 9.81  # Acceleration due to gravity (m/s^2)
AIR_RESISTANCE = 0.1   # Air resistance constant (kg/s)

# Function to calculate the distance
def calculate_horizontal_distance(x0, y0, v0, launch_angle_deg, m):
    """
    Calculate the horizontal distance traveled by a projectile with air resistance.

    Parameters:
    x0 (float): Initial horizontal position (m)
    y0 (float): Initial vertical position (m)
    v0 (float): Initial velocity (m/s)
    launch_angle_deg (float): Launch angle in degrees
    m (float): Mass of the projectile (kg)

    Returns:
    float: Horizontal distance traveled (meters)
    """
    # Convert launch angle to radians
    theta = np.radians(launch_angle_deg)

    # Time values
    t_max = 20  # Maximum simulation time (s)
    dt = 0.01   # Time step (s)
    t_values = np.arange(0, t_max, dt)

    # Use functional programming to update velocities over time
    vx_values = x0 + v0 * np.cos(theta) * t_values
    vy_values = y0 + v0 * np.sin(theta) * t_values - 0.5 * GRAVITY * t_values**2

    # Find the index when the projectile hits the ground (y = 0)
    ground_index = np.argmax(vy_values < 0)

    # Calculate the horizontal distance traveled
    x_final = vx_values[ground_index]

    return x_final

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Projectile Horizontal Distance Calculator")

    parser.add_argument("--x0", type=float, required=True, help="Initial horizontal position (m)")
    parser.add_argument("--y0", type=float, required=True, help="Initial vertical position (m)")
    parser.add_argument("--v0", type=float, required=True, help="Initial velocity (m/s)")
    parser.add_argument("--launch_angle_deg", type=float, required=True, help="Launch angle in deg")
    parser.add_argument("--m", type=float, required=True, help="Mass of the projectile (kg)")

    args = parser.parse_args()

    h_d = calculate_horizontal_distance(args.x0, args.y0, args.v0, args.launch_angle_deg, args.m)

    print(f"Horizontal distance traveled: {h_d:.2f} meters")
