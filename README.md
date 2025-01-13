Projectile Motion Simulation with Air Resistance and GUI

This Python program simulates projectile motion with air resistance, allowing users to input parameters via a graphical user interface (GUI). The program visualizes the trajectory with key annotations and offers functionality to save the animation as a GIF.

Features

- Realistic Physics: Simulates projectile motion considering gravity and air resistance with adjustable drag coefficient.

- User-Friendly GUI:

- Accepts user inputs such as initial velocity, launch angle, projectile mass, and drag coefficient via pop-up dialogs.

- Offers an option to save the animation as a GIF.

Dynamic Animation:

- Visualizes the projectile's trajectory.

- Highlights key points such as the peak height and landing position.

- Interactive functionality with keyboard controls.

Keyboard Controls During Animation:

- p: Pause/Play the animation.

Requirements:

- Python 3.x

- Libraries:

- numpy

- matplotlib

- tkinter

Installation

Clone the repository:

git clone

Navigate to the project directory:

cd projectile-motion-simulation

Install the required libraries:

pip install numpy matplotlib

Usage

Run the script:

python projectile_motion.py

Input the required parameters through GUI dialogs:

Initial velocity (m/s): A positive number, e.g., 50.

Launch angle (degrees): Between 0 and 90, e.g., 45.

Mass of the projectile (kg): A positive number, e.g., 2.

Drag coefficient: A non-negative number, e.g., 0.1.

Watch the animation of the projectile's motion.

Save the animation as a GIF if desired.

Keyboard Controls

Pause/Play: Press p to toggle between pausing and playing the animation.

How It Works

The program uses numerical integration to compute the position and velocity of the projectile at each time step.

Gravity and air resistance (modeled as proportional to velocity) are included in the calculations.

A GUI powered by tkinter gathers user inputs and provides options for saving the animation.

The animation is created using matplotlib.animation.FuncAnimation.

Example

For an initial velocity of 50 m/s, a launch angle of 45 degrees, a mass of 2 kg, and a drag coefficient of 0.1, the program calculates and displays:

The projectile's trajectory.

The peak height and the horizontal distance traveled upon landing.

An option to save the animation as a GIF file.

Code Overview

projectile_motion_with_air_resistance:
Computes the projectile's motion under gravity and air resistance.

update:
Updates the plot for each animation frame.

toggle_pause:
Handles pause and play functionality.

get_user_input:
Collects user inputs using tkinter dialogs.

save_prompt:
Provides the option to save the animation as a GIF.

start_animation:
Initializes and displays the animation.

Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the program.

Acknowledgments

Physics principles used in the program are inspired by real-world projectile motion models.

Special thanks to the creators of matplotlib, numpy, and tkinter for their powerful tools.

