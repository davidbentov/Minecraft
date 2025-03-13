from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def basein(x,y, z ):
    mc.setBlocks(x-8,y-4,z-6, x, y, z,1)
    mc.setBlocks(x-6,y-3,z-5, x, y, z,9)


basein(x, y, z)
