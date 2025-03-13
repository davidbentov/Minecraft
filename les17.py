from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def roof(x, y, z, h, block):
    for i in range(h):
        mc.setBlocks(x-i, y-i, z-i, x+i, y-i, z+i, block)
x, y, z = mc.player.getTilePos()
def base(x, y, z, h, block):
    mc.setBlocks(x, y, z, x+h,y+h, z+h, block)
    mc.setBlocks(x+1, y+1, z+1, x+h-1, y+h-1, z+h-1, 0)

def build_house(x, y, z):
    base(x, y, z, 6, 1)
    roof(x+3, y+6+5, z+3, 5, 5)
x, y, z = mc.player .getTilePos()
build_house(x, y, z)