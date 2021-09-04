tellraw @a {"text": "nacteno", "color": "#00FF00"}

scoreboard objectives remove dropItem
scoreboard objectives add dropItem minecraft.dropped:minecraft.stone

scoreboard objectives remove sunktime
scoreboard objectives add sunktime dummy

scoreboard objectives add dimOverworld dummy
scoreboard objectives add dimSuperCool dummy

#spawner
scoreboard objectives remove ars
scoreboard objectives add ars dummy
scoreboard objectives remove mob_spawned
scoreboard objectives add mob_spawned dummy

execute as @p run function ryba:spawner/spawn_ars


