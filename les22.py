from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Parfenon:
    def __init__(self, p, h,):
        self.pos = p
        self.height = h

    def stvol(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z, x, y+self.height, z, 155)

    def base(self):
        x, y, z = self.pos
        mc.setBlocks(x-1, y, x+1, y, z+1, 155)
        mc.setBlock(x-1, y+1, z, 156 ,0)
        mc.setBlock(x+1, y+1, z, 156, 1)
        mc.setBlock(x, y+1, z-1, 156, 2)
        mc.setBlock(x, y+1, z+1, 156, 3)

    def capital(self):
        x, y, z = self.pos
        mc.setBlocks(x-1, y+self.height, x+1, y+self.height, z+1, 155)
        mc.setBlock(x-1, y+self.height-1, z, 156 ,4)
        mc.setBlock(x+1, y+self.height-1, z, 156, 5)
        mc.setBlock(x, y+self.height-1, z-1, 156, 6)
        mc.setBlock(x, y+self.height-1, z+1, 156, 7)

    def Biuld_colymn(self):
        self.base()
    self.stvol()
    self.capital()

    def Biuld_all_colymn(self):
        x, y, z, = self.pos
        for i in range(10):
            self.Biuld_colymn()
            x+=7
    self.pos = x, y, z-20,
    self.pos = x, y, z
    self.pos = x_start, y, z



    def build_parfenon(self):
        x, y, z = self.pos
        self.build_all_column()
        self.pos = x, y, z+20
        self.build_all_column()
        self.pos = x, y, z-20

        mc.setBlocks(x-1, y-1, z-1, x+64, y-1, z+21, 155)

        mc.setBlocks(x-1, y+1+self.height, z-1, x+64, y+1+self.height, z+21, 155)


x, y, z = mc.player.getTilePos()
parf = Parfenon((x, y, z), 6)
parf.capital()