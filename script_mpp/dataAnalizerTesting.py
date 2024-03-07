import numpy as np
import matplotlib.pyplot as plt
import pandas as plt

# Define the 3D points
points = np.array([[0.434, 0.083, -0.356], [0.449, 0.07, -0.328],[0.462, 0.07, -0.328],
                   [0.475, 0.07, -0.328],[0.417, 0.071, -0.332],[0.406, 0.072, -0.333],
                   [0.395, 0.073, -0.334],[0.494, 0.079, -0.139],[0.374, 0.084, -0.156],
                   [0.459, 0.104, -0.277],[0.416, 0.106, -0.287],[0.593, 0.175, -0.041],
                   [0.288, 0.179, -0.039],[0.635, 0.298, 0.079],[0.243, 0.308, 0.002],
                   [0.702, 0.407, 0.032],[0.178, 0.428, -0.11],[0.71, 0.446, 0.022],
                   [0.154, 0.463, -0.138],[0.713, 0.447, -0.058],[0.163, 0.465, -0.223],
                   [0.701, 0.434, 0.003],[0.181, 0.453, -0.149],[0.551, 0.426, 0.003],
                   [0.36, 0.43, -0.004],[0.565, 0.631, 0.083],[0.358, 0.638, -0.074],
                   [0.577, 0.801, 0.341],[0.364, 0.81, 0.2],[0.551, 0.822, 0.352],
                   [0.389, 0.826, 0.221],[0.649, 0.884, 0.172],[0.319, 0.897, 0.049]])

# Extract x, y, z coordinates
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Create the frontal projection (XY plane)
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(131)
ax.scatter(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Frontal Projection (XY plane)')

# Create the lateral projection (XZ plane)
ax = fig.add_subplot(132)
ax.scatter(x, z)
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title('Lateral Projection (XZ plane)')

# Create the top-down projection (YZ plane)
ax = fig.add_subplot(133)
ax.scatter(y, z)
ax.set_xlabel('Y')
ax.set_ylabel('Z')
ax.set_title('Top-down Projection (YZ plane)')

plt.tight_layout()
plt.show()
