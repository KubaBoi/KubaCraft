#GENERATED FILE

execute at @p run spreadplayers ~ ~ 10 75 false @e[type=minecraft:armor_stand]

execute as @s if entity @s[scores={mob_spawned=..3}] if entity @s[scores={ars=50..}] run function ryba:spawner/spawn_mob
execute as @s run scoreboard players set @s ars 0
function ryba:spawner/check_mobs
