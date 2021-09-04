import json

count = 1
pref = "ar"
path = "data/ryba/functions/spawner/"
freq = 50
radius = 10
dist = 5
max_mobs = 2

biomes = [
    ("blue_cold", "blue_cold", "minecraft:pig"),
    ("blue_cold_m", "blue_cold_mountain", "minecraft:chicken"),
    ("dry_forrest", "dry_forrest", "minecraft:zombie"),
    ("mushroom_jun", "mushroom_jungle", "minecraft:salmon"),
    ("obsidian_plane", "obsidian_plane", "minecraft:cow")
]

if (count > 100): count = 100

#spawn
with open(path + "spawn_ars.mcfunction", "w") as f:
    f.write("#GENERATED FILE\n\n")
    for i in range(100):
        cmd = "execute as @e[tag=" + pref + str(i) + "] run kill\n"
        f.write(cmd)
    
    f.write("\n")

    for i in range(count):
        cmd = "execute at @p run summon armor_stand ~ ~ ~ {Tags:[\"" + pref + str(i) + "\"],Invisible:1b,Invulnerable:1}\n"
        f.write(cmd)
        cmd = "scoreboard objectives remove random\n"
        f.write(cmd)
        cmd = "scoreboard objectives add random dummy\n"
        f.write(cmd)

    f.write("\n")

    for i in biomes:
        cmd = "scoreboard objectives remove " + i[0] + "\n"
        f.write(cmd)
        cmd = "scoreboard objectives add " + i[0] + " dummy\n"
        f.write(cmd)

#timer
with open(path + "timer.mcfunction", "w") as f:
    f.write("#GENERATED FILE\n\n")
    f.write("#add one for every armorstand every time\n")
    for i in range(count):
        cmd = "execute as @e[tag=" + pref + str(i) + "] run scoreboard players add @s ars 1\n"
        f.write(cmd)

    f.write("execute as @e[scores={ars=" + str(freq) + "}] at @s positioned ^ ^ ^ run function ryba:spawner/shuffle\n\n")
    f.write("scoreboard players add @e[tag=ar0] random 1\n")
    f.write("execute as @e[tag=ar0,scores={random=100..}] run scoreboard players reset @e[tag=ar0] random\n")

#shuffle
with open(path + "shuffle.mcfunction", "w") as f:
    f.write("#GENERATED FILE\n\n")
    f.write(f"execute at @p run spreadplayers ~ ~ {dist} {radius} false @e[type=minecraft:armor_stand]\n\n")
    f.write("execute as @s if entity @s[scores={mob_spawned=.." + str(max_mobs) + "}] if entity @s[scores={ars=" + str(freq) + "..}] run function ryba:spawner/spawn_mob\n")
    f.write("execute as @s run scoreboard players set @s ars 0\n")
    f.write("function ryba:spawner/check_mobs\n")

#check mobs
with open(path + "check_mobs.mcfunction", "w") as f:
    f.write("#GENERATED FILE\n\n")
    f.write("#checks if mobs are alive\n")
    for i in range(count):
        cmd = "execute as @e[tag=" + pref + str(i) + "] unless entity @e[tag=" + pref + str(i) + "_m] run scoreboard players set @s mob_spawned 0\n"
        f.write(cmd)

#locate biomes
with open(path + "biomes/locate_biomes.mcfunction", "w") as f:
    f.write("#GENERATED FILE\n\n")
    f.write("#locates nearest biom\n")
    for i in biomes:
        cmd = "execute as @s at @s store result score @s " + i[0] + " run locatebiome ryba:" + i[1] + "\n"
        f.write(cmd)

#spawn mob biome
with open(path + "biomes/spawn_mob_biome.mcfunction", "w") as f:
    f.write("#GENERATED FILE\n\n")
    f.write("#choose the biom\n")
    for i in biomes:
        cmd = "execute as @s if entity @s[scores={" + i[0] + "=..5}] at @s run function ryba:spawner/biomes/biome_files/biome_" + i[1] + "\n"
        f.write(cmd)

#biom files
for b in biomes:
    with open(path + "biomes/biome_files/biome_" + b[1] + ".mcfunction", "w") as f:
        f.write("#GENERATED FILE\n\n")
        for i in range(count):
            with open(path + f"biomes/biomes_data/{b[1]}.json", "r") as js:
                data = json.load(js)
                for entity in data["entities"]:

                    cmd = ("execute as @s if entity @s[tag=" + pref + str(i) + "] if entity @e[tag=ar0,scores={random=" +
                     str(entity["floor"]) + ".." + str(entity["ceil"]) + "}] run summon " +
                     entity["name"] + " ~ ~ ~ {Tags:[\"" + pref + str(i) + "_m\"]," + entity["tags"] + "}\n")

                    f.write(cmd)



