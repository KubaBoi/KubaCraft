#execute as @a[scores={dropItem=1..}] at @s positioned ^ ^ ^ run function ryba:portal/dropped

#execute as @e[type=item,nbt={Item:{id:"minecraft:stone"}}] at @s if block ~ ~ ~ water run scoreboard players add @s sunktime 1

#execute as @e[scores={sunktime=1..},nbt={Item:{id:"minecraft:stone"}}] at @s positioned ^ ^ ^ run function ryba:portal/dropped

execute as @p at @s if block ~ ~ ~ water run scoreboard players add @s sunktime 1

execute as @p[scores={sunktime=1..}] at @s positioned ^ ^ ^ run function ryba:portal/dropped

function ryba:spawner/timer
