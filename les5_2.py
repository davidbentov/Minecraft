from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z=mc.player.getTilePos()
block_up=mc.getBlock(x,y+2, z)
block_under=mc.getBlock(x, y, z)

in_tunnel= block_up != 0 and block_up != 8 and block_under != 0 and block_under != 8
print(in_tunnel)
