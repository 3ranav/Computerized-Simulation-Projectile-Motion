import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring, askfloat
from tkinter import filedialog

# Parameters
g = 9.81
paused = False
current_frame = 0

# Function to calculate projectile motion with air resistance
def projectile_motion_with_air_resistance(v0, angle, m, b, delta_t, total_time):
    angle_rad = np.radians(angle)

    v_x = v0 * np.cos(angle_rad)
    v_y = v0 * np.sin(angle_rad)

    x_vals = [0]
    y_vals = [0]
    v_x_vals = [v_x]
    v_y_vals = [v_y]

    # Simulation loop
    for _ in np.arange(0, total_time, delta_t):
        v_x = v_x_vals[-1]
        v_y = v_y_vals[-1]

        a_x = - (b / m) * v_x
        a_y = -g - (b / m) * v_y

        v_x_next = v_x + a_x * delta_t
        v_y_next = v_y + a_y * delta_t

        x_next = x_vals[-1] + v_x * delta_t + 0.5 * a_x * delta_t ** 2
        y_next = y_vals[-1] + v_y * delta_t + 0.5 * a_y * delta_t ** 2

        if y_next < 0:
            break

        x_vals.append(x_next)
        y_vals.append(y_next)
        v_x_vals.append(v_x_next)
        v_y_vals.append(v_y_next)

    return x_vals, y_vals

# animation update function
def update(frame):
    plt.clf()  
    plt.xlim(0, max(x_vals) * 1.1)
    plt.ylim(0, max(y_vals) * 1.1)
    plt.axhline(0, color='black', lw=1)

    plt.plot(x_vals[:frame], y_vals[:frame], color='blue')

    plt.scatter(x_vals[0], y_vals[0], color='green', zorder=5)  
    plt.scatter(x_vals[frame-1], y_vals[frame-1], color='red', zorder=5)  

    peak_index = np.argmax(y_vals)
    if frame >= peak_index:
        plt.scatter(x_vals[peak_index], y_vals[peak_index], color='orange', zorder=5)
        plt.annotate(f"Peak: ({x_vals[peak_index]:.2f}, {y_vals[peak_index]:.2f})",
                     xy=(x_vals[peak_index], y_vals[peak_index]), textcoords="offset points", 
                     xytext=(0,10), ha='center', fontsize=10)

    plt.title(f'Projectile Motion: v0={initial_velocity} m/s, angle={launch_angle}°, mass={mass} kg')

    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.grid()

# Pause and play functionality
def toggle_pause(event):
    global paused, ani
    if event.key == 'p':  
        if paused:
            ani.event_source.start()
        else:
            ani.event_source.stop()
        paused = not paused

# GUI to get user input
def get_user_input():
    global initial_velocity, launch_angle, mass, b, delta_t, total_time

    initial_velocity = askfloat("Input", "Enter the initial velocity (m/s):", minvalue=0)
    launch_angle = askfloat("Input", "Enter the launch angle (degrees):", minvalue=0, maxvalue=90)
    mass = askfloat("Input", "Enter the mass of the projectile (kg):", minvalue=0)
    b = askfloat("Input", "Enter the drag coefficient:", minvalue=0)

    time_without_resistance = 2 * initial_velocity * np.sin(np.radians(launch_angle)) / g
    air_resistance_factor = 1 + (b / mass)
    total_time = time_without_resistance * air_resistance_factor
    delta_t = 0.01  # time increment being used (delta t)

    # Calculate trajectory with air resistance
    global x_vals, y_vals
    x_vals, y_vals = projectile_motion_with_air_resistance(initial_velocity, launch_angle, mass, b, delta_t, total_time)

    start_animation()

def start_animation():
    global ani

    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', toggle_pause)

    def animate(i):
        global current_frame
        if not paused and current_frame < len(x_vals):
            current_frame += 1
        update(current_frame)

    ani = FuncAnimation(fig, animate, frames=len(x_vals), interval=20, repeat=False) # change interval for faster/slower animation
    plt.show()

    save_prompt()

def save_prompt():
    save = messagebox.askyesno("Save Animation", "Do you want to save the animation as a GIF?")
    if save:
        file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
        if file_path:
            ani.save(file_path, writer='imagemagick', fps=30)
            messagebox.showinfo("Success", f"Animation saved to {file_path}")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  

    get_user_input()  
