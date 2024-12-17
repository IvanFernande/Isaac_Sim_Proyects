import omni.ui as ui
from omni.isaac.dynamic_control import _dynamic_control
import numpy as np

# Function to move the robot's joints
def move_joint(joint_angles=None):
    """
    Moves the UR10 robot's joints to the target positions.

    Args:
        joint_angles (list or np.ndarray): List of desired positions for each joint in radians.
    """
    # Initialize the dynamic controller
    dc = _dynamic_control.acquire_dynamic_control_interface()

    # Path to the robot in the simulator
    robot_path = "/World/ur10_bin_stacking_long_conveyor/ur10"
    articulation = dc.get_articulation(robot_path)

    if not articulation:
        print(f"Robot not found at path: {robot_path}")
        return

    # Wake up the robot (if it was in sleep mode)
    dc.wake_up_articulation(articulation)

    # Count the degrees of freedom (DoF) of the robot
    dof_count = dc.get_articulation_dof_count(articulation)
    print(f"The robot has {dof_count} degrees of freedom.")

    # Apply the target positions to the joints
    print(f"Moving joints to: {joint_angles}")
    dc.set_articulation_dof_position_targets(articulation, joint_angles)

    # Get the current state of the joints
    joint_state = dc.get_articulation_dof_states(articulation, _dynamic_control.STATE_POS)
    print(f"Current joint states: {joint_state['pos']}")

# Create the UI window
window_name = "Robot Control"

# Create the main window
window = ui.Window(window_name, width=300, height=300)

# Create a main container
with window.frame:
    with ui.VStack():  # Organizes elements in a vertical column
        ui.Label("UR10 Robot Control", style={"font_size": 18, "color": "white"})
        
        # Buttons for predefined positions
        with ui.HStack():  # Organizes elements in a horizontal row
            ui.Label("Move to Positions:")
            ui.Button("Safe Position", clicked_fn=lambda: move_joint(
                joint_angles=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            ))
            ui.Button("Custom", clicked_fn=lambda: move_joint(
                joint_angles=[0.6, -1.0, 0.1, -0.1, 0.1, -0.1]
            ))
        
        # Sliders to move each joint individually
        sliders = []
        ui.Label("Manual Control:")
        for i in range(6):  # Assuming 6 DoFs for the UR10
            with ui.HStack():
                ui.Label(f"Joint {i+1}:")
                slider = ui.FloatSlider(min=-3.14, max=3.14)
                slider.model.set_value(0.0)  # Initial value
                sliders.append(slider)
        
        # Button to apply slider values
        def apply_sliders():
            joint_angles = [slider.model.get_value_as_float() for slider in sliders]
            move_joint(joint_angles=joint_angles)
        
        def clear_sliders():
            for i in range(6):
                sliders[i].model.set_value(0.0)
                
        
        ui.Button("Apply Sliders", clicked_fn=apply_sliders)
        ui.Button("Clear Sliders", clicked_fn=clear_sliders)
