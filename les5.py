from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z= mc.player.getTilePos()

block=mc.getBlock(x, y, z)
in_water = (block== 8)
print(in_water)
           