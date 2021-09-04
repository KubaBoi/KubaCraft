#GENERATED FILE

execute as @s if entity @s[tag=ar0] if entity @e[tag=ar0,scores={random=0..50}] run summon minecraft:zombie ~ ~ ~ {Tags:["ar0_m"],Invulnerable:1,PersistenceRequired:1,HandItems:[{Count:1,id:"minecraft:netherite_axe"},{}],CustomName:"\"hitler\"",HandDropChances:[0.1f,0.0f]}
execute as @s if entity @s[tag=ar0] if entity @e[tag=ar0,scores={random=50..80}] run summon minecraft:cow ~ ~ ~ {Tags:["ar0_m"],}
execute as @s if entity @s[tag=ar0] if entity @e[tag=ar0,scores={random=80..100}] run summon minecraft:salmon ~ ~ ~ {Tags:["ar0_m"],}
