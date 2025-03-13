from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# индекс:   0   1   2   3   4
my_items = [57, 46, 20, 41, 1]

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, my_items[0])
mc.setBlock(x, y+1, z, my_items[1])
mc.setBlock(x, y+2, z, my_items[2])
mc.setBlock(x, y+3, z, my_items[3])
mc.setBlock(x, y+4, z, my_items[4])


my_items = [57, 46, 20, 41, 1]
print(my_items)
my_items.append(100)
print(my_items)



my_items = [20, 46, 20, 41, 1]
print(my_items)
my_items.remove(20)
print(my_items)