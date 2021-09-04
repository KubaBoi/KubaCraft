#checks if armorstands mob is alive - if no spawns one and add
tellraw @a "spawn mob"
execute as @s run scoreboard players add @s mob_spawned 1
execute as @s run scoreboard players set @s ars 0
execute as @s run function ryba:spawner/biomes/locate_biomes
execute as @s run function ryba:spawner/biomes/spawn_mob_biome
