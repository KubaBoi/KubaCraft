#GENERATED FILE

#add one for every armorstand every time
execute as @e[tag=ar0] run scoreboard players add @s ars 1
execute as @e[scores={ars=50}] at @s positioned ^ ^ ^ run function ryba:spawner/shuffle

scoreboard players add @e[tag=ar0] random 1
execute as @e[tag=ar0,scores={random=100..}] run scoreboard players reset @e[tag=ar0] random
