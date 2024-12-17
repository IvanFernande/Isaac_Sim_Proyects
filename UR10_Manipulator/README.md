![Captura desde 2024-12-17 10-21-44](https://github.com/user-attachments/assets/64b06d64-1a8a-4902-88bb-e1c738ca5c83)
# UR10 Projects in Isaac Sim

This folder contains a collection of projects and scripts developed for the **UR10** robot model within NVIDIA Isaac Sim. Each project focuses on different robotic tasks, control techniques, and integrations, leveraging the powerful capabilities of Isaac Sim for high-fidelity simulation and real-world application testing.

---

## About the UR10

The **UR10** is a collaborative industrial robotic arm designed for tasks such as pick-and-place, palletizing, assembly, and more. In this folder, the UR10 is simulated and controlled in Isaac Sim, allowing for:
- Accurate physics-based simulation.
- Real-time manipulation of joints and end-effectors.
- Integration with external frameworks like **ROS2**.
- Testing and optimization of control algorithms in a safe, virtual environment.

Isaac Sim enables developers to experiment with the UR10's kinematics, trajectory planning, and AI-based control solutions without the need for physical hardware.

---

## Projects Overview

### 1. **Joint Controller UI**
- **Description**: A basic script that provides an interactive user interface (UI) to control the joints of the UR10 robot in real time. This is achieved using Isaac Sim's **Dynamic Control API** and the **omni.ui** module.
- **Features**:
   - Predefined buttons for moving the robot to "Safe Position" and "Custom Position".
   - Sliders for manual adjustment of each joint's position.
   - Real-time feedback of joint states.
- **Script**: `ui.py`
- **Usage**:
   - Launch Isaac Sim and load the `ur10_bin_stacking_long_conveyor` model or the scene on `joint_controllers_ui/enviroment/scene.usd`.
   - Run the on `joint_controllers_ui/scripts/ui.py` with the Isaac Sim extension
   - Use the UI window to interact with the robot:
     - Move joints to predefined positions with buttons.
     - Adjust individual joints using sliders and apply the changes in real time.

---

## How to Run the Project

1. **Prerequisites**:
   - NVIDIA Isaac Sim installed and configured.
   - Python 3.7+ installed on your system.
   - Visual Studio Code with the **Isaac Sim VS Code** extension and **VS Code Integration** enabled.

2. **Steps**:
   - Clone this repository:
   - Open **Isaac Sim** and **Visual Studio Code**.
   - Ensure the `ur10_bin_stacking_long_conveyor` model is loaded in Isaac Sim or open the scene on `joint_controllers_ui/enviroment/scene.usd`.
   - Run the script using the Isaac Sim extension:

3. **Using the UI**:
   - A window will appear with controls to interact with the robot.
   - Use sliders to control each joint's position manually.
   - Use buttons to move the robot to predefined positions.

---

## Next Steps
- Add real-time visualization of joint velocities and torques.
- Integrate trajectory planning for smooth, automated movements.
- Implement ROS2 communication for external control.
- Extend the UI to include control for the end-effector.

---

## Feedback and Contributions
If you find this project useful or have suggestions for improvements, feel free to open an issue or submit a pull request.

Happy coding!
