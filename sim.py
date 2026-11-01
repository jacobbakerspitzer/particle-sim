# A tiny charged ball, like a proton, flies through space.
# A magnet is creating an invisible magnetic field around it. 
#  The field is a collection of invisible arrows that fill the space and point the same way. 
# Ours point straight up, out of the screen towards us.

# F: the push(force) on the ball
# q: how much charge the ball has. More charge means a stronger push.
# v: the ball's velocity, meaning its speed and direction
# B: the magnetic field, it's strength and direction
# x: the cross product, which takes 2 directions and gives the direction perpendicular to both. That's the sideways push.

# F = q(v x B)

# r = mv/ (qB), tells you how big the circle is.

# Faster ball means a wider circle,  A car going faster makes wider turns
# Heavier ball means a wider circle -> more inertia
# More charge -> tighter circle, stronger inward force during rotation

# I will use 1s to simulate accuracy, since the calculations are easy r = (1)(1) / ((1)(1)) = 1

# Load NumPy, a math library for arrays
import numpy as np
# Loads the plotting library, plt is the nickname
import matplotlib.pyplot as plt

# Declaring variables
q = 1.0
m = 1.0

# Creates a vector to do vector math with via the numpy library
B = np.array([0.0, 0.0, 1.0])

# How much time passes each frame
dt = 0.01

# # Of total frames 
steps = 20000


# position initially starts at the origin
pos = np.array([0.0, 0.0, 0.0])

# Moves in the +x direction at speed 1
vel = np.array([1.0, 0.0, 0.0])

# Create two empty lists to be filled as the ball moves.
# We will take data from this to plot later
xs, ys = [], []

# for every step, do 5 things:
# Find the push
# Turn into acceleration
# Nudge the vel
# Nudge the pos
# record position
for i in range(steps):

    # make the force calculation exerted on the ball by the field
    force = q * (np.cross(vel, B))

    # calculate the acceleration according to N2M
    a = force / m

    # Integrate the accelaration with intial and final conditions the old vel and new vel. 
    vel += a * dt

    # Do the same with vel and pos
    pos += vel * dt

    # Append the x and y position into the xs and ys lists to be plotted
    xs.append(pos[0])
    ys.append(pos[1])

# plotting the data
# Draws a line connecting all the recorded points
plt.plot(xs, ys)

# Make 1 unit on X same as 1 unit on Y
plt.axis('equal')

# Makes this the title
plt.title('charged particle in magnetic field')

# Labels x and y axis
plt.xlabel('x position')
plt.ylabel('y position')

# displays the plot
plt.show()