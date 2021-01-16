import pprint
import os
import json
import uuid
import block
debug=False
mobs={}
mobs["skeleton"]={"item":"skull:0","skin":"textures/entity/skeleton/skeleton","geo_file":"file","bone":"head"}
mobs["wither_skeleton"]={"item":"skull:1","skin":"textures/entity/skeleton/wither_skeleton"}
mobs["creeper"]={"item":"skull:4","skin":"textures/entity/creeper/creeper"}
mobs["zombie"]={"item":"skull:2","skin":"textures/entity/zombie/zombie"}
mobs["slime"]={"item":"slime","skin":"textures/entity/slime/slime"}
mobs["witch"]={"item":"glowstone_dust","skin":"textures/entity/witch"}

mobs["ghast"]={"item":"ghast_tear","skin":"textures/entity/ghast/ghast"}
mobs["hoglin"]={"item":"leather","skin":"textures/entity/hoglin/hoglin"}
mobs["vindicator"]={"item":"iron_axe","skin":"textures/entity/vindicator"}
mobs["pillager"]={"item":"crossbow","skin":"textures/entity/pillager"}
mobs["ravager"]={"item":"saddle","skin":"textures/entity/ravager"}
mobs["evocation_illager"]={"item":"totem","skin":"textures/entity/evoker"}
mobs["piglin"]={"item":"gold_block","skin":"textures/entity/piglin/piglin"}
mobs["zombie_pigman"]={"item":"golden_sword","skin":"textures/entity/piglin/zombie_piglin"}
mobs["magma_cube"]={"item":"magma_cream","skin":"textures/entity/slime/magma_cube"}
mobs["enderman"]={"item":"ender_pearl","skin":"textures/entity/enderman/enderman"}
mobs["blaze"]={"item":"blaze_rod","skin":"textures/entity/blaze"}
mobs["phantom"]={"item":"phantom_membrane","skin":"textures/entity/phantom"}
mobs["guardian"]={"item":"prismarine","skin":"textures/entity/guardian"}
mobs["drowned"]={"item":"trident","skin":"textures/entity/zombie/drowned"}
mobs["spider"]={"item":"web","skin":"textures/entity/spider/spider"}


fileName="pack_maker_def.json"
#os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(mobs,json_file,indent=2)

ticks="10"
payment="netherite_ingot"
ranges=[25,50,75]
mobNames=list(mobs.keys())

states={"default":{"transitions":[]}}

bp_pack_name="test_bp"
rp_pack_name="test_rp"
componentGroups={}
events={}
def makeInteraction(item,interactText,eventName):
    interaction={}
    interaction["hurt_item"]=0
    interaction["interact_text"]=interactText
    interaction["on_interact"]={"filters":{"all_of":[]}}

    filt={"test": "has_equipment","subject": "player","value": str(item)}
    
    interaction["on_interact"]["filters"]["all_of"].append(filt)

    interaction["on_interact"]["event"]=eventName

    interaction["on_interact"]["target"]="self"
    interaction["swing"]=True
    interaction["use_item"]=True

    return interaction

def makeManifest(bp_pack_name):
    manifest={}
    manifest["format_version"]=2
    manifest["header"]={}
    manifest["modules"]={}
    manifest["header"]["description"]="This pack makes a craftable block that spawn proofs a radius around the player, Created by FondUnicycle and RavinMaddHatter"
    manifest["header"]["name"]="Spawn Proofing Beacons"
    manifest["header"]["uuid"]= str(uuid.uuid4())
    manifest["header"]["version"]=[0,0,3]
    manifest["header"]["min_engine_version"]=[1,16,0]
    
    manifest["modules"]["description"]="Spawn Proofing Beacons"
    module={}
    module["uuid"]= str(uuid.uuid4())
    module["type"]="data"
    module["version"]=[1,0,0]
    manifest["modules"]=[module]
    fileName="{}/manifest.json".format(bp_pack_name)
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName,"w+") as json_file:
              json.dump(manifest,json_file,indent=2) 

eventName="set_range_{}".format(0)
componentGName="mpb:mob_defined_{}_range".format(0)
NextcomponentGName="mpb:mob_defined_{}_range".format(ranges[0])
componentGroups[componentGName]={}

nextEvent="set_range_{}".format(ranges[0])
componentGroups[componentGName]["minecraft:variant"]={"value":0}
events[eventName]={"add":{"component_groups":[componentGName]}}

for rangeI in range(len(ranges)-1):  
    eventName="set_range_{}".format(ranges[rangeI])
    nextEvent="set_range_{}".format(ranges[rangeI+1])
    PrevComponentGName=componentGName
    componentGName="mpb:mob_defined_{}_range".format(ranges[rangeI])
    componentGroups[componentGName]={}
    componentGroups[componentGName]["minecraft:variant"]={"value":rangeI+1}
    events[eventName]={"add":{"component_groups":[componentGName]}}
    events[eventName]["remove"]={"component_groups":[PrevComponentGName]}
    
PrevComponentGName=componentGName
componentGName="mpb:mob_defined_{}_range".format(ranges[-1])
componentGroups[componentGName]={}
componentGroups[componentGName]["minecraft:variant"]={"value":len(ranges)}
eventName="set_range_{}".format(ranges[-1])
events[eventName]={"add":{"component_groups":[componentGName]}}
events[eventName]["remove"]={"component_groups":[PrevComponentGName]}

staticComps={}
staticComps["minecraft:nameable"]={}
staticComps["minecraft:type_family"]={"family":["inanimate","beacon_base"]}
staticComps["minecraft:collision_box"]={"width":0.5,"height":1.5}
staticComps["minecraft:loot"]={"table":"loot_tables/empty"}
staticComps["minecraft:physics"]={"has_collision": False,"has_gravity": False}
staticComps["minecraft:pushable"]={"is_pushable":False,"is_pushable_by_piston":False}
staticComps["minecraft:interact"]={}
staticComps["minecraft:damage_sensor"]={"triggers": [{"cause": "all","deals_damage":False}]}
rp_render={"format_version": "1.8.0"}
rp_render["render_controllers"]={"controller.render.beacon_base":{"arrays":{"textures":{"Array.skins":["Texture.default"]}}}}
rp_render["render_controllers"]["controller.render.beacon_base"]["materials"]=[{"*": "Material.default"}]
rp_render["render_controllers"]["controller.render.beacon_base"]["geometry"]="query.skin_id== 0 ? Geometry.default : Geometry.head"
rp_render["render_controllers"]["controller.render.beacon_base"]["textures"]=["Array.skins[query.skin_id]"]
rp_entity={"format_version": "1.10.0"}
rp_entity["minecraft:client_entity"]={"description": {"identifier": "spb:beacon_base"}}
rp_entity["minecraft:client_entity"]["description"]["materials"]={"default": "entity_alphatest"}
rp_entity["minecraft:client_entity"]["description"]["textures"]={"default": "textures/items/nether_star"}
rp_entity["minecraft:client_entity"]["description"]["geometry"]={"default": "geometry.beacon_base.nether_star"}
rp_entity["minecraft:client_entity"]["description"]["geometry"]["head"]="geometry.beacon_base.head"
rp_entity["minecraft:client_entity"]["description"]["scripts"]={"animate": ["move"]}
rp_entity["minecraft:client_entity"]["description"]["animations"]={"move": "animation.beacon_base"}
rp_entity["minecraft:client_entity"]["description"]["render_controllers"]=["controller.render.beacon_base"]
mobset=[]
interactionSet=[]
componentGroups["mpb:mob_defined_empty"]={}
componentGroups["mpb:mob_defined_empty"]["minecraft:skin_id"]={"value":0}

componentGroups["mpb:mob_defined_empty"]["minecraft:interact"]={}
componentGroups["mpb:mob_defined_empty"]["minecraft:interact"]["interactions"]=[]
componentGroups["mpb:despawn"]= {"minecraft:instant_despawn": {}}
for mobI in range(len(mobNames)):
    componentGName="mpb:mob_defined_{}".format(mobNames[mobI])
    componentGroups[componentGName]={}
    item=mobs[mobNames[mobI]]["item"]
    interactText="Set Mob Type"

    eventName="set_{}".format(mobNames[mobI])
    componentGroups[componentGName]["minecraft:skin_id"]={"value":mobI+1}
    interaction=makeInteraction(item,interactText,eventName)
    componentGroups["mpb:mob_defined_empty"]["minecraft:interact"]["interactions"].append(interaction)
    events[eventName]={"add":{"component_groups":[componentGName]}}
    rp_render["render_controllers"]["controller.render.beacon_base"]["arrays"]["textures"]["Array.skins"].append("Texture.{}".format(mobNames[mobI]))
    events[eventName]["remove"]={"component_groups":["mpb:mob_defined_empty"]}
    rp_entity["minecraft:client_entity"]["description"]["textures"][mobNames[mobI]]=mobs[mobNames[mobI]]["skin"]
    for rangeI in range(len(ranges)):
        stateName="{}_range_{}".format(mobNames[mobI],ranges[rangeI])
        transition="query.skin_id=={}&&query.variant=={}".format(mobI+1,rangeI+1)
        states["default"]["transitions"].append({stateName:transition})
        states[stateName]={}
        states[stateName]["transitions"]=[{"default":"math.mod(query.time_stamp,{})==1".format(ticks)}]
        states[stateName]["on_entry"]=[]
        states[stateName]["on_entry"].append("/tp @e[type={},name=!save,r={}] ~ -10 ~".format(mobNames[mobI],ranges[rangeI]))
        if debug:
            states[stateName]["on_entry"].append("/say name={}r={}] ~ -100 ~".format(mobNames[mobI],ranges[rangeI]))
    
events["minecraft:entity_spawned"]={"add": {"component_groups": ["mpb:mob_defined_empty","mpb:mob_defined_0_range"]}}
events["despawn_entity"]={"add": {"component_groups": ["mpb:despawn"]}}		
#staticComps["minecraft:interact"]["interactions"]=interactionSet


controller={}
controller["format_version"]="1.10.0"
controller["animation_controllers"]={}
controller["animation_controllers"]["controller.animation.despawner"]={}
controller["animation_controllers"]["controller.animation.despawner"]["initial_state"]= "default"
controller["animation_controllers"]["controller.animation.despawner"]["states"]=states

entity={}
entity["format_version"]="1.13.0"
entity["minecraft:entity"]={}
entity["minecraft:entity"]["description"]={"identifier":"spb:beacon_base","is_spawnable":False}
entity["minecraft:entity"]["description"]["is_summonable"]=True
entity["minecraft:entity"]["description"]["is_experimental"]=False
entity["minecraft:entity"]["description"]["animations"]={"cntrl":"controller.animation.despawner"}
entity["minecraft:entity"]["description"]["scripts"]={"animate":["cntrl"]}
entity["minecraft:entity"]["component_groups"]=componentGroups
entity["minecraft:entity"]["components"]=staticComps
entity["minecraft:entity"]["events"]=events


fileName="{}/render_controllers/beacon_base.entity.render_controllers.json".format(rp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(rp_render,json_file,indent=2)
fileName="{}/entity/beacon_base.entity.rp.json".format(rp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(rp_entity,json_file,indent=2)
fileName="{}/recipes/beacon_base.block.json".format(bp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(block.recipe,json_file,indent=2)
fileName="{}/loot_tables/blocks/beacon_base.json".format(bp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(block.table,json_file,indent=2)
fileName="{}/blocks/beacon_base.block.json".format(bp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(block.beaconBaseBlock,json_file,indent=2)
fileName="{}/entities/beacon_base.json".format(bp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(entity,json_file,indent=2)
fileName="{}/animation_controllers/beacon_base.json".format(bp_pack_name)
os.makedirs(os.path.dirname(fileName), exist_ok=True)
with open(fileName,"w+") as json_file:
    json.dump(controller,json_file,indent=2)
makeManifest(bp_pack_name)
