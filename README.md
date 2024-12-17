# My Isaac Sim Proyects

In this repository, I will be working on different projects of mine in isaac sim, to learn how to simulate robotics in different applications, combining it with different technologies.

---

# Isaac Sim - Development of Scripts in VSCode

## What is Isaac Sim?

**NVIDIA Isaac Sim** is an advanced simulation platform for robotics, part of the **NVIDIA Omniverse** ecosystem. It is designed for engineers and developers to:

- Simulate realistic environments for robotics testing.
- Safely test robotics and control algorithms without physical hardware.
- Implement and deploy artificial intelligence (AI) and reinforcement learning (RL) models.
- Seamlessly integrate with popular tools such as **ROS/ROS2** for real-world deployment.

Isaac Sim supports high-fidelity simulations that include accurate physics, realistic sensor data, and machine learning workflows. It allows developers to:

1. Test complex robotic behaviors like manipulation, locomotion, and perception.
2. Connect to real-world frameworks like **ROS2** for live simulation-to-hardware workflows.
3. Use **dynamic control APIs** for real-time articulation control.
4. Train AI models in simulated environments before deploying to physical robots, reducing the costs and risks associated with real-world testing.

Thanks to **NVIDIA Omniverse**, Isaac Sim integrates tools like USD (Universal Scene Description) for high-performance rendering and simulation, enabling realistic, scalable, and efficient robotic workflows.

---

## My Development Environment

For efficient script development in **Isaac Sim**, I use **Visual Studio Code (VSCode)**, leveraging a combination of tools and extensions for a seamless experience.

### VSCode Extensions
1. **Python** - For Python development and debugging.
2. **Omniverse Code Extension** - Official NVIDIA extension for integration with Omniverse applications like Isaac Sim.
3. **Jupyter** - Allows interactive execution and debugging of Python code.

### Isaac Sim Configuration
- **Omniverse Kit** - A modular development environment that supports Python scripting and USD workflows.
- **Dynamic Control API** - Provides real-time control over robot articulations, joints, and sensors.
- **ROS2 Integration** - I have implemented connections with **ROS2** to simulate real-world communication between robots and controllers, enabling advanced robotics workflows.

Using **VSCode** with the appropriate extensions allows me to:
- Write, debug, and execute scripts efficiently.
- Integrate Isaac Sim simulations with ROS2 frameworks for complex robotic tasks.
- Test AI-driven control systems and reinforcement learning pipelines directly within the Isaac Sim environment.

---

## Repository Overview

This repository includes example scripts and projects for:

- Controlling robots like the **UR10_bin_stacking_long_conveyor** model.
- Manipulating robot articulations using the **Dynamic Control API**.
- Building interactive interfaces with **omni.ui** for real-time control.
- Integrating **ROS2** for real-world communication between Isaac Sim and robotic controllers.

### How to Run a Script:
1. Clone this repository into your local environment:
   ```bash
   git clone https://github.com/your-username/isaac-sim-scripts.git
   cd isaac-sim-scripts
   ```
2. Open **Isaac Sim** and Visual Studio Code.
3. Ensure all required extensions are installed.
4. Run the script directly from **VSCode**:
   - Use the integrated terminal or the Jupyter interface for interactive execution.

---

## Example Script: UR10 Joint Control
Below is a simple script for controlling the joints of the UR10 robot using Isaac Sim's **Dynamic Control API**:

```python
from omni.isaac.dynamic_control import _dynamic_control

# Initialize the dynamic control interface
robot_path = "/World/ur10_bin_stacking_long_conveyor/ur10"
dc = _dynamic_control.acquire_dynamic_control_interface()
articulation = dc.get_articulation(robot_path)

# Move the joints to predefined positions
if articulation:
    dc.wake_up_articulation(articulation)
    target_positions = [0.0, -1.0, 0.1, -0.1, 0.1, -0.1]  # Example positions
    dc.set_articulation_dof_position_targets(articulation, target_positions)
    print("Joints moved to target positions.")
else:
    print("Robot not found in the specified path.")
```

---

## Requirements
- **NVIDIA Isaac Sim** (compatible version).
- **Python 3.7+**.
- **Visual Studio Code** with:
   - Python extension.
   - Omniverse extension.

---

## Next Steps
- **Advanced ROS2 Integration**: Simulate ROS2 control nodes and controllers.
- **Reinforcement Learning (RL)**: Train AI models to automate complex tasks like pick-and-place operations.
- **Trajectory Automation**: Develop scripts to generate smooth and collision-free robot trajectories.
- **Sensor Integration**: Implement additional sensors such as cameras, LiDAR, and IMUs for perception tasks.

---

If you have any questions, suggestions, or feedback, feel free to reach out! 🚀

#Robotics #IsaacSim #ROS2 #VSCode #Omniverse #Simulation #ReinforcementLearning

