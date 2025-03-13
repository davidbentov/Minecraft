import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x_derevna=319
y_derevna=66
z_derevna=239

x_plains=97
y_plains=67
z_plains=280


mc.postToChat("деревня")
mc.player.setTilePos(x_derevna,y_derevna,z_derevna)
mc.postToChat(str(x_derevna)+"/"+str(y_derevna)+"/"+str(z_derevna))
mc.postToChat("Деревня - в широком смысле - социально-территориальная общность, характеризующаяся небольшой по сравнению с городом концентрацией населения на локализованном пространстве, занятого преимущественно сельским хозяйством.")
time.sleep(15)

mc.postToChat("равнины")
mc.player.setTilePos(x_plains,y_plains,z_plains)
mc.postToChat(str(x_derevna)+"/"+str(y_derevna)+"/"+str(z_derevna))
mc.postToChat("Равнины обычно имеют плоский рельеф с небольшими холмами. Поверхность состоит из дёрна и покрыта травой. В этом биоме иногда можно найти небольшие водоёмы, лавовые озера и пещерные отверстия. Также редко встречаются дубы,")

mc.player.setTilePos(x_derevna,y_derevna,z_derevna)
mc.postToChat("конец экскусии")

