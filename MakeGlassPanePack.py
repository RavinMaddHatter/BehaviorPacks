import json

dyes={}

dyes["black"]=[16,0]
dyes["blue"]=[18,4]
dyes["brown"]=[3,17]
dyes["cyan"]=[6]
dyes["grey"]=[8]
dyes["green"]=[2]
dyes["lightBlue"]=[12]
dyes["lightGrey"]=[7]
dyes["lime"]=[10]
dyes["magenta"]=[13]
dyes["orange"]=[14]
dyes["pink"]=[9]
dyes["purple"]=[5]
dyes["red"]=[1]
dyes["white"]=[15,19]
dyes["yellow"]=[11]


terracotta={}
terracotta["black"]=15
terracotta["cyan"]=9
terracotta["blue"]=11
terracotta["brown"]=12
terracotta["grey"]=7
terracotta["green"]=13
terracotta["lightBlue"]=3
terracotta["lightGrey"]=8
terracotta["lime"]=5
terracotta["magenta"]=2
terracotta["orange"]=1
terracotta["pink"]=6
terracotta["purple"]=10
terracotta["red"]=14
terracotta["white"]=0
terracotta["yellow"]=4

Priority=1
format_version="1.12"


def makeTerracotta(color,dyeNum,terracottaNum):
    recp={}
    recp["format_version"]=format_version
    recp["minecraft:recipe_shaped"]={}
    recp["minecraft:recipe_shaped"]["description"]={}
    recp["minecraft:recipe_shaped"]["description"]["identifier"]="minecraft:{}_glass_pane_from_dye{}".format(color,dyeNum)
    recp["minecraft:recipe_shaped"]["tags"]=[ "crafting_table" ]
    recp["minecraft:recipe_shaped"]["group"]="stained_glass"
    recp["minecraft:recipe_shaped"]["priority"]=Priority
    recp["minecraft:recipe_shaped"]["pattern"]=["###","#X#","###"]
    recp["minecraft:recipe_shaped"]["key"]={}
    recp["minecraft:recipe_shaped"]["key"]["#"]={}
    recp["minecraft:recipe_shaped"]["key"]["#"]["item"]="minecraft:stained_glass_pane"
    recp["minecraft:recipe_shaped"]["key"]["X"]={}
    recp["minecraft:recipe_shaped"]["key"]["X"]["item"]="minecraft:dye"
    recp["minecraft:recipe_shaped"]["key"]["X"]["data"]=dyeNum
    recp["minecraft:recipe_shaped"]["result"]={}
    recp["minecraft:recipe_shaped"]["result"]["item"]="minecraft:stained_glass_pane"
    recp["minecraft:recipe_shaped"]["result"]["data"]=terracottaNum
    recp["minecraft:recipe_shaped"]["result"]["count"]=8
    with open("{}_glass_Pane_from_dye{}.json".format(color,dyeNum),"w+") as json_file:
              json.dump(recp,json_file,indent=2)




for dyeKey in dyes.keys():
    for dyeNum in dyes[dyeKey]:
        makeTerracotta(dyeKey,dyeNum,terracotta[dyeKey])
