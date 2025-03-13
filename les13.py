from mcpi.minecraft import Minecraft

from les102 import x_start

mc = Minecraft.create()

air = 0
grn = 133
yel = 19
blk = 49

pixel_art = [
    [air, air, air, air, air, air, air, air, air, air, air, air],
    [air, air, air, blk, blk, blk, blk, blk, blk, blk, blk, blk],
    [air, air, blk, yel, yel, yel, yel, yel, yel, yel, yel, blk],
    [air, air, blk, yel, yel, yel, yel, yel, yel, yel, yel, air, blk],
    [air, air, blk, yel, yel, yel, yel, yel, yel, air, yel, air, yel, blk],
    [air, air, blk, yel, yel, yel, yel, yel, yel, blk, yel, blk,yel, blk, blk, blk, blk],
    [air, air, blk, yel, yel, yel, yel, air, air, air, yel, yel, yel],
    [air, air, blk, yel, yel, yel, yel, air, air, air, air, yel, yel, blk, blk, blk, blk],
    [air, air, blk, yel, yel, yel, yel, yel, yel, yel, yel, yel, yel],
    [air, air, blk, blk, blk, blk, blk, blk, blk, blk, blk, blk, blk],
    [air, air, blk, grn, grn, grn, grn, grn, grn, grn, grn, grn],
    [air, air, blk, grn, grn, grn, grn, grn, grn, grn, grn, grn],
    [air, air, blk, blk, blk, blk, blk, blk, blk, blk, blk, blk, blk, blk],
    [air, air, air, blk, air, air, air, air, air, air, air, air],
    [air, air, air, blk, air, air, air, air, air, air, air, air],
    [air, air, air, air, air, air, air, air, air, air, air, air],
]

x, y, z = mc.Player.getTilePost()
x_start = x

for row in reversed(Pixel_art):
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    x = x_start
    y, += 1

