from mcpi.minecraft import Minecraft

#mc = Minecraft.create()
mc = Minecraft.create(address="localhost", port=25565)

x=168
y=76
z=226
x, y, z = mc.player.getTilePos()
print(x, y, z)





