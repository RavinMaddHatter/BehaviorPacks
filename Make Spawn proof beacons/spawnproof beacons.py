import pprint
mobs={}
mobs["skeleton"]={"item":{"skull:0"}}
mobs["wither_skeleton"]={"item":"skull:1"}
mobs["creeper"]={"item":"skull:4"}}
mobs["zombie"]={"item":{"skull:2"}}
ticks="10"
payment=["netherite_ingot","netherite_ingot","netherite_ingot"]
ranges=[25,50,75]
mobNames=list(mobs.keys())

states={"default":{"transitions":[]}}

componentGroups={}
events={}
def makeInteraction(item,interactText,eventName):
    interaction={}
    interaction["hurt_item"]=0
    interaction["interact_text"]=interactText
    interaction["on_interact"]={"filters":{"all_of":[]}}
    filt={"test": "has_equipment","subject": "player","value": item}

    interaction["on_interact"]["filters"]["all_of"].append{filt}
    interaction["on_interact"]["event"]=eventName
    interaction["on_interact"]["target"]="self"
    interaction["on_interact"]["swing"]=True
    interaction["on_interact"]["use_item"]=True
    
    
componentGroups["waiting_activation"]={}

componentGroups["waiting_activation"]

for rangeI in range(len(ranges)):
    

for mobI in range(len(mobNames)):
    for rangeI in range(len(ranges)):
        stateName="{}_range_{}".format(mobNames[mobI],ranges[rangeI])
        transition="query.skin_id=={}&&query.variant=={}".format(mobI+1,rangeI+1)
        states["default"]["transitions"].append({stateName:transition})
        states[stateName]={}
        states[stateName]["transitions"]="math.mod(query.time_stamp,{})==1".format(ticks)
        states[stateName]["on_entry"]="/tp @e[name={},r={}] ~ -10 ~".format(mobNames[mobI],ranges[rangeI])

controller={}
controller["format_version"]="1.10.0"
controller["animation_controllers"]={}
controller["animation_controllers"]["controller.animation.despawner"]={}
controller["animation_controllers"]["controller.animation.despawner"]["initial_state"]= "default"
controller["animation_controllers"]["controller.animation.despawner"]["states"]=states




