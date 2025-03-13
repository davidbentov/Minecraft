

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# x, y, z, height

class Parfenon:
    def __init__(self, x_p, y_p, z_p, h):
        self.x = x_p
        self.y = y_p
        self.z = z_p
        self.height = h

    def trunk(self):
        x, y, z = self.x, self.y, self.z
        mc.setBlocks(x, y, z, x, y+self.height, z, 155)

    def base(self):
        x, y, z = self.x, self.y, self.z
        mc.setBlocks(x-1, y, z-1, x+1, y, z+1, 155)
        mc.setBlock(x-1, y+1, z, 156, 0)
        mc.setBlock(x+1, y+1, z, 156, 1)
        mc.setBlock(x, y+1, z-1, 156, 2)
        mc.setBlock(x, y+1, z+1, 156, 3)

    def capital(self):
        x, y, z = self.x, self.y, self.z
        mc.setBlocks(x-1, y+self.height, z-1, x+1, y+self.height, z+1, 155)
        mc.setBlock(x-1, y-1+self.height, z, 156, 4)
        mc.setBlock(x+1, y-1+self.height, z, 156, 5)
        mc.setBlock(x, y-1+self.height, z-1, 156, 6)
        mc.setBlock(x, y-1+self.height, z+1, 156, 7)

    def build_column(self):
        self.base()
        self.trunk()
        self.capital()

    def build_all_column(self):
        start_x = self.x
        for i in range(10):
            self.build_column()
            self.x += 7
        self.x = start_x

    def build_parfenon(self):
        x, y, z = self.x, self.y, self.z
        self.build_all_column()
        self.z += 20
        self.build_all_column()
        self.z -= 20
        mc.setBlocks(x-1, y-1, z-1, x+64, y-1, z+21, 155)
        mc.setBlocks(x-1, y+self.height+1, z-1, x+64, y+self.height+1, z+21, 155)
        
        
class Geniral_clas:
    def __init_(self,n, x_p, y_p, z_p,):
       self.name = n
       self.x = x_p
       self.y = y_p
       self.z = z_p
        
    def info(self):
        mc.postTochat(self.name)
class Flowers(Geniral_class):
     def plant_flowers(self):
         x, y, z = self.x, self.y, self.z
         mc.setBlocks(x, y, z, x+70, y, z+25, 2)
         mc.setBlocks(x, y+1, z, x+70, y+1, z+25, 38)

class Fountai(Geniral_class):
    def __init__(self,n, x_p, y_p, z_p, h ):
        Geniral_class.__init_(self,n, x_p, y_p, z_p, h )
        self.height = h

    def one_fount(self):
        x, y, z, = self.x, self.y, self.z
        mc.setBlocks(x-2, y-1, z-2, x+2, y, z+2, 155)
        mc.setBlocks(x-1, y, z-1, x+1, y, z+1,0)
        mc.setBlocks(x, y, z, x, y+self.height, z, 155)
        mc.setBlock(x, y+self.height+1, z, 8)

    def row_fount(self, count):
        for i in range(count):
            self.one_fount()
            self.x += 10
        
x, y, z = mc.player.getTilePos()
x += 5
building = Parfenon(x, y, z, 20)
flowers1 = Flowers('Клумба слева', x, y-1, z-31)
flowers2 = Flowers('Клумба справа', x, y-1, z+26)
fountain1 = Fountain('Фонтаны слева', x, y, z-25, 6)
fountain2 = Fountain('Фонтаны справа', x, y, z+46, 6)

building.build_parfenon()
flowers1.plant_flowers()
flowers2.plant_flowers()
fountain1.row_fount(7)
fountain2.row_fount(7)



x, y, z = mc.player.getTilePos()
parf = Parfenon(x+5, y, z, 8)
parf.build_parfenon()