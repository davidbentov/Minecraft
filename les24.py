from mcpi.minecraft import Minecraft
import time

def connect_to_minecraft():
    try:
        mc = Minecraft.create()
        return mc
    except ConnectionRefusedError:
        print("Error: Could not connect to Minecraft. Please make sure:")
        print("1. Minecraft is running")
        print("2. You have the Minecraft Pi mod installed")
        print("3. You're running this script on the same computer as Minecraft")
        return None

# Try to connect to Minecraft
mc = connect_to_minecraft()

if mc is None:
    print("Exiting due to connection error")
    exit(1)

class Baschna:
    def __init__(self, x_p, y_p, z_p):
        self.x = x_p
        self.y = y_p
        self.z = z_p

    def firstfloor(self):
        x, y, z = self.x, self.y, self.z
        mc.setBlocks(x, y, z, x+6, y, z+5, 7)
        mc.setBlocks(x+1, y, z+1, x+5, y, z+4, 0)

    def secondfloor(self):
        x, y, z = self.x + 1, self.y + 1, self.z + 1  # Start one block in from the edges
        mc.setBlocks(x, y, z, x+4, y, z+3, 7)  # Make it 4x3 instead of 6x5
        mc.setBlocks(x+1, y, z+1, x+3, y, z+2, 0)  # Hollow interior

try:
    # Create and build both floors
    x, y, z = mc.player.getTilePos()
    bach = Baschna(x, y, z)
    bach.firstfloor()
    bach.secondfloor()
    print("Successfully built the house!")
except Exception as e:
    print(f"An error occurred while building: {e}")
