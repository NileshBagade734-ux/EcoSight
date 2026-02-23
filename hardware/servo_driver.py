# Low-level interface for servo motors
# For now, we'll simulate with print statements.
# Replace with actual GPIO / servo code on real hardware.

class ServoDriver:
    def __init__(self):
        # Initialize hardware, e.g., GPIO setup
        print("[ServoDriver] Initialized (simulation)")

    def move_servo(self, bin_name: str):
        """
        Moves the servo for the specified bin.
        """
        # Real implementation: use PWM to rotate servo
        print(f"[ServoDriver] Moving servo for {bin_name}")
