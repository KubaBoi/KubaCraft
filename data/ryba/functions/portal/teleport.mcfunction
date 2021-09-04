#summon minecraft:item_frame ^ ^ ^ {Invisible:1b,Tags:["frame1"],Item:{id:"minecraft:crafting_table",Count:1b}}
#summon minecraft:item_frame ^-1 ^ ^ {Invisible:1b,Tags:["frame2"],Item:{id:"minecraft:crafting_table",Count:1b}}
#summon minecraft:item_frame ^-1 ^-1 ^ {Invisible:1b,Tags:["frame3"],Item:{id:"minecraft:crafting_table",Count:1b}}
#summon minecraft:item_frame ^ ^-1 ^ {Invisible:1b,Tags:["frame4"],Item:{id:"minecraft:",Count:1b}}

execute as @p at @s if entity @s[nbt={Dimension:"minecraft:overworld"}] run scoreboard players add @s dimOverworld 1
execute as @p at @s if entity @s[nbt={Dimension:"ryba:supercool_dimension"}] run scoreboard players add @s dimSuperCool 1

#overworld to supercool
execute as @p[scores={dimOverworld=1..}] as @s in ryba:supercool_dimension run tp @s ~2 ~2 ~2
execute as @p[scores={dimOverworld=1..}] run function ryba:spawner/spawn_ars
#supercool to overworld
execute as @p[scores={dimSuperCool=1..}] as @s in minecraft:overworld run tp @s ~2 ~2 ~2 

scoreboard players reset @a sunktime
scoreboard players reset @a dimOverworld
scoreboard players reset @a dimSuperCool