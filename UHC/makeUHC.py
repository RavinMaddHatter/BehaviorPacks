import json
import math
import numpy as np
import os
import uuid
import player
import health
from tkinter import StringVar,IntVar, Button,Label,Entry,Tk,DoubleVar, Toplevel,messagebox, ttk
from zipfile import ZipFile
from shutil import copyfile
import os
from os import listdir
from os.path import isfile, join
from os import walk
import glob

def makeStand(packName,name,animations,componetGroups,components,events):
    stand={"format_version": "1.10.0","minecraft:entity": {}}
    
    stand["minecraft:entity"]["description"]={}
    stand["minecraft:entity"]["description"]["identifier"]="uhc:{}".format(name)
    stand["minecraft:entity"]["description"]["is_summonable"]=True
    stand["minecraft:entity"]["description"]["is_spawnable"]=True
    stand["minecraft:entity"]["description"]["is_experimental"]=False
    stand["minecraft:entity"]["description"]["scripts"]={"animate": []}
    stand["minecraft:entity"]["description"]["animations"]= {}
    stand["minecraft:entity"]["spawn_egg"]={"base_color": "#949493","overlay_color": "#651818"}
    if type(animations)is dict:
        for ani in  animations.keys():
            stand["minecraft:entity"]["description"]["scripts"]["animate"].append(animations[ani]["name"])
            stand["minecraft:entity"]["description"]["animations"][animations[ani]["name"]]=animations[ani]["handle"]
    
    if type(componetGroups) is dict:
        stand["minecraft:entity"]["component_groups"]=componetGroups
    if type(components) is dict:
        stand["minecraft:entity"]["components"]=components
    if type(events) is dict:
        stand["minecraft:entity"]["events"]=events
    os.makedirs(os.path.dirname("{}/entities/uhc/{}.json".format(packName,name)), exist_ok=True)
    with open("{}/entities/uhc/{}.json".format(packName,name),"w+") as json_file:
              json.dump(stand,json_file,indent=2)
    

def standComponents(family="hatter_controller"):
    components={}
    components["minecraft:nameable"]={}
    components["minecraft:type_family"]= {"family": [family]}
    components["minecraft:navigation.generic"]={"can_sink": False}
    components["minecraft:damage_sensor"]= {"triggers":{"cause": "all","deals_damage": False}}
    components["minecraft:collision_box"]={"width": 0.6,"height": 1.9}
#    components["minecraft:health"]={"value": 6,"max": 6}
    components["minecraft:persistent"]={}
#    components["minecraft:physics"]={"has_gravity": False,"has_collision": False}
    components["minecraft:pushable"]={"is_pushable": False,"is_pushable_by_piston": True}
#    components["minecraft:fire_immune"]=True
    return components
def gameControllerParts(packName,roundTime,totalGameTime,safeTime,startR,stopR):
    contractingTime=totalGameTime-safeTime
    timeSteps=np.arange(0,contractingTime,roundTime)
    rSteps=np.flip(np.arange(stopR,startR,(startR-stopR)/timeSteps.size)).astype(int)
    numRounds=timeSteps.size
    componentGroups={}
    events={}
    states={}
    states["default"]={"transitions":[]}
    states["default"]["on_entry"]=["/function lock_inventory"]
    states["default"]["transitions"].append({"start":"query.variant==70"})
    states["default"]["transitions"].append({"pvp_start":"query.variant==71"})
    states["start"]={}
    states["start"]["on_entry"]=["/title @a[rm={}] actionbar Next Game step you must be closer than {} from 0,0 you will take damage here".format(rSteps[1],rSteps[1])]
    states["start"]["on_entry"].append("/scoreboard players set @e[name=zero] detect_health {}".format(rSteps[0]))
    states["start"]["on_entry"].append("/effect @a[rm={}] wither 2 1".format(rSteps[0]))
    
    
    states["start"]["transitions"]=[{"default": "math.mod(query.time_stamp,10)==1"}]
    states["pvp_start"]={}
    states["pvp_start"]["on_entry"]=["/title @a[rm={}] actionbar Next Game step you must be closer than {} from 0,0 you will take damage here".format(rSteps[1],rSteps[1])]
    states["pvp_start"]["on_entry"].append("/scoreboard players set @e[name=zero] detect_health {}".format(rSteps[0]))
    states["pvp_start"]["on_entry"].append("/effect @a[rm={}] wither 2 1".format(rSteps[0]))
    states["pvp_start"]["on_entry"].append("/gamerule pvp true")
    states["pvp_start"]["on_entry"].append("/title @a actionbar PVP is now enabled. Enjoy!")
    states["pvp_start"]["transitions"]=[{"default": "math.mod(query.time_stamp,10)==1"}]
    
    events["minecraft:entity_spawned"]={"add": {"component_groups":["uhc:start"]}}
    currentRound="uhc:start"
    nextRound="uhc:pvp_start"
    componentGroups[currentRound]={}
    componentGroups[currentRound]["minecraft:is_baby"]={}
    componentGroups[currentRound]["minecraft:scale"]={"value": 1/(numRounds+3)}
    componentGroups[currentRound]["minecraft:variant"]={"value": 70}
    componentGroups[currentRound]["minecraft:ageable"]={}
    componentGroups[currentRound]["minecraft:ageable"]["duration"]=safeTime
    componentGroups[currentRound]["minecraft:ageable"]["feed_items"]="wheat"
    componentGroups[currentRound]["minecraft:ageable"]["grow_up"]={}
    componentGroups[currentRound]["minecraft:ageable"]["grow_up"]["event"]="uhc:to_pvp_start"
    componentGroups[currentRound]["minecraft:ageable"]["grow_up"]["target"]="self"
    events["uhc:to_pvp_start"]={"add": {"component_groups":[nextRound]},"remove": {"component_groups": [currentRound]}}
    
    currentRound=nextRound
    nextRound="uhc:round0"
    componentGroups[currentRound]={}
    componentGroups[currentRound]["minecraft:is_baby"]={}
    componentGroups[currentRound]["minecraft:scale"]={"value": 2/(numRounds+3)}
    componentGroups[currentRound]["minecraft:variant"]={"value": 71}
    componentGroups[currentRound]["minecraft:ageable"]={}
    componentGroups[currentRound]["minecraft:ageable"]["duration"]=2
    componentGroups[currentRound]["minecraft:ageable"]["feed_items"]="wheat"
    componentGroups[currentRound]["minecraft:ageable"]["grow_up"]={}
    componentGroups[currentRound]["minecraft:ageable"]["grow_up"]["event"]="uhc:to_round0"
    componentGroups[currentRound]["minecraft:ageable"]["grow_up"]["target"]="self"
    events["uhc:to_round0"]={"add": {"component_groups":[nextRound]},"remove": {"component_groups": [currentRound]}}   
    
    for i in range(numRounds-1):
        
        commands=["/title @a[rm={}] actionbar Next Game step you must be closer than {} from 0,0 you will take damage here".format(rSteps[i+1],rSteps[i+1])]
        
        commands.append("/scoreboard players set @e[name=zero] detect_health {}".format(rSteps[i]))
        commands.append("/effect @a[rm={}] wither 2 1".format(rSteps[i]))
        
        nextEventName="uhc:to_round{}".format(i+1)
        currentRound="uhc:round{}".format(i)
        stateName="round{}".format(i)
        nextRound="uhc:round{}".format(i+1)
        states["default"]["transitions"].append({stateName:"query.variant=={}".format(i)})
        states[stateName]={}
        states[stateName]["on_entry"]=commands
        states[stateName]["transitions"]=[{"default": "math.mod(query.time_stamp,10)==1"}]
        
        componentGroups[currentRound]={}
        componentGroups[currentRound]["minecraft:is_baby"]={}
        componentGroups[currentRound]["minecraft:scale"]={"value": (i+3)/(numRounds+3)}
        componentGroups[currentRound]["minecraft:variant"]={"value": i}
        componentGroups[currentRound]["minecraft:ageable"]={}
        componentGroups[currentRound]["minecraft:ageable"]["duration"]=roundTime
        componentGroups[currentRound]["minecraft:ageable"]["feed_items"]="wheat"
        componentGroups[currentRound]["minecraft:ageable"]["grow_up"]={}
        componentGroups[currentRound]["minecraft:ageable"]["grow_up"]["event"]=nextEventName
        componentGroups[currentRound]["minecraft:ageable"]["grow_up"]["target"]="self"
        events[nextEventName]={"add": {"component_groups":[nextRound]},"remove": {"component_groups": [currentRound]}}

    i+=1
    commands=[]
    commands.append("/scoreboard players set @e[name=zero] detect_health {}".format(rSteps[i]))
    commands.append("/effect @a[rm={}] wither 2 1".format(rSteps[i]))
    
    currentRound="uhc:round{}".format(i)
    
    states["default"]["transitions"].append({stateName:"query.variant=={}".format(1)})
    
    stateName="round{}".format(i)
    states[stateName]={}
    states[stateName]["on_entry"]=commands
    states[stateName]["transitions"]=[{"default": "math.mod(query.time_stamp,10)==1"}]
    
    componentGroups[currentRound]={}
    componentGroups[currentRound]["minecraft:scale"]={"value": (i+3)/(numRounds+3)}
    componentGroups[currentRound]["minecraft:variant"]={"value": i}
        
    return {"component_groups":componentGroups,"events":events,"states":states}

def makeStartFunction(packName,controllerName,safeTime,maxR):
    fileName="{}/functions/startUHC.mcfunction".format(packName)
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName,"w+") as functionFile:
        functionFile.write("tickingarea add circle 0 0 0 2 zeroTicking\n")
        functionFile.write("spreadplayers 0 0 1 20 @a\n")
        functionFile.write("gamerule showcoordinates true\n")
        functionFile.write("fill -1 65 -1 1 63 1 barrier\n")
        functionFile.write("fill 0 64 0 0 64 0 air\n")
        functionFile.write("summon uhc:{} zero 0 64 0\n".format(controllerName))
        functionFile.write("scoreboard objectives add detect_health dummy Health\n")
        functionFile.write("scoreboard players set @a detect_health 20\n")
        functionFile.write("scoreboard objectives setdisplay sidebar detect_health descending\n")
        functionFile.write("gamerule naturalregeneration false\n")
        functionFile.write("tag @a remove dead\n")
        functionFile.write("effect @a slow_falling 90 1 true\n")
        functionFile.write("spreadplayers 0 0 200 {} @a\n".format(maxR*.7))
        functionFile.write("gamerule pvp false\n")
        functionFile.write("gamemode s @a\n")
        functionFile.write("effect @a instant_health 1 255 true\n")
        functionFile.write("effect @a saturation 1 5 true\n")
        functionFile.write("title @a actionbar Game Start {:.1f} min of No PVP starts now\n".format(safeTime/60))
        functionFile.write("\n")
def makeStopFunction(packName):
    fileName="{}/functions/stopUHC.mcfunction".format(packName)
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName,"w+") as functionFile:
        functionFile.write("tickingarea remove zeroTicking\n")
        functionFile.write("kill @e[name=zero]\n")
        functionFile.write("gamerule naturalregeneration true\n")
        functionFile.write("effect @a slow_falling 30 1 true\n")
        functionFile.write("spreadplayers 0 0 1 20 @a\n")
        functionFile.write("gamerule pvp true\n")
        functionFile.write("title @a actionbar UHC over. all game rules set back to normal\n")
        functionFile.write("gamemode s @a\n")
        functionFile.write("tag @a remove dead\n")
        functionFile.write("effect @a instant_health 1 255 true\n")
        functionFile.write("effect @a saturation 1 5 true\n")
        
        functionFile.write("clear @a\n")
        functionFile.write("\n")
def makeFillInventoryFunction(packName):
    fileName="{}/functions/lock_inventory.mcfunction".format(packName)
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName,"w+") as functionFile:
        for i in range(27):
            functionFile.write('replaceitem entity @a[tag=dead] slot.inventory '+str(i)+' barrier 1 1 {"keep_on_death": {}, "item_lock": {"mode": "lock_in_slot"}}\n')
        for i in range(9):
            functionFile.write('replaceitem entity @a[tag=dead] slot.hotbar '+str(i)+' barrier 1 1 {"keep_on_death": {}, "item_lock": {"mode": "lock_in_slot"}}\n')
            
        functionFile.write("effect @a[tag=dead] weakness 10 255 false\n")
        functionFile.write("effect @a[tag=dead] invisibility 10 255 false\n")
        functionFile.write("\n")
def makeManifest(packName,roundTime,totalGameTime,safeTime,startR,stopR):
    manifest={}
    manifest["format_version"]=2
    manifest["header"]={}
    manifest["modules"]={}
    manifest["header"]["description"]="This is a UHC with the rules: Total Game Time: {}, Shrink Interval: {}, PVP off Timer: {}, Max Radius: {}, Min Radius: {}".format(totalGameTime,roundTime,safeTime,startR,stopR)
    manifest["header"]["name"]="Custom Hatter UHC:{}".format(packName)
    manifest["header"]["uuid"]= str(uuid.uuid4())
    manifest["header"]["version"]=[0,0,1]
    manifest["header"]["min_engine_version"]=[1,16,0]
    
    manifest["modules"]["description"]="Custom Hatter UHC"
    module={}
    module["uuid"]= str(uuid.uuid4())
    module["type"]="data"
    module["version"]=[1,0,0]
    manifest["modules"]=[module]
    fileName="{}/manifest.json".format(packName)
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName,"w+") as json_file:
              json.dump(manifest,json_file,indent=2)

def animationsFromStates(states,controllerName,packName):
    
    controllerPath="controller.animation.uhc.{}".format(controllerName)
    animationController={controllerPath:{"initial_state": "default","states":states}}
    jsonObject={"format_version": "1.10.0","animation_controllers": animationController}
    path="{}/animation_controllers/uhc/{}.json".format(packName,controllerName)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w+") as json_file:
        json.dump(jsonObject,json_file,indent=2)
    return {"name":controllerName,"handle":controllerPath}
def makeTick(packName):
    tick={"values":["lock_inventory"]}
    path="{}/functions/tick.json".format(packName)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w+") as json_file:
        json.dump(tick,json_file,indent=2)
def startAnimation(packName):
    start={
	"format_version": "1.10.0",
	"animations": {
		"animation.start": {
			"timeline": {
				"0.0": [
					"/scoreboard objectives add detect_health dummy health",
					"/scoreboard players set @s detect_health 20"
				]
			},
			"animation_length": 1.0,
			"loop": False
		}
            }
        }
    path="{}/animations/uhc/start.json".format(packName)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w+") as json_file:
        json.dump(start,json_file,indent=2)
    
def makePack():
    roundTime=roundTimeVar.get()
    totalGameTime=totalGameTimeVar.get()
    safeTime=safeTimeVar.get()
    startR=startRVar.get()
    stopR=stopRVar.get()
    packName=packNameVar.get()
    parts=gameControllerParts(packName,roundTime,totalGameTime,safeTime,startR,stopR)
    animations={"one":animationsFromStates(parts["states"],"game_manager",packName)}
    events=parts["events"]
    components=standComponents()
    componentGroups=parts["component_groups"]
    makeStand(packName,"game_controller",animations,componentGroups,components,events)
    makeStartFunction(packName,"game_controller",safeTime,startR)
    makeStopFunction(packName)
    makeManifest(packName,roundTime,totalGameTime,safeTime,startR,stopR)
    startAnimation(packName)
    makeFillInventoryFunction(packName)
    path="{}/entities/uhc/playter.json".format(packName)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w+") as json_file:
        json.dump(player.player,json_file,indent=2)
    path="{}/animation_controllers/uhc/health.json".format(packName)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w+") as json_file:
        json.dump(health.health,json_file,indent=2)
    copyfile("pack_icon.png", "{}/pack_icon.png".format(packName))
    file_paths=[]
    for directory,_,_ in os.walk(packName):
        file_paths.extend(glob.glob(os.path.join(directory,"*.*"))) 
    with ZipFile("{}.mcpack".format(packName),'x') as zip: 
        # writing each file one by one 
        for file in file_paths:
            print(file)
            zip.write(file)
root = Tk()

root.title("Madhatter's UHC Maker")

roundTimeLb=Label(root, text="Round Time")
totalGameTimeLb=Label(root, text="Total Game Time")
safeTimeLb=Label(root, text="No PVP time")
startRLb=Label(root, text="Starting Border")
stopRLb=Label(root, text="Ending Border")
packNameLb=Label(root, text="Pack Name")
roundTimeVar=IntVar()
roundTimeVar.set(300)
roundTimeEntry = Entry(root,textvariable=roundTimeVar)

totalGameTimeVar=IntVar()
totalGameTimeVar.set(int(60*60*1.5))
totalGameTimeEntry = Entry(root,textvariable=totalGameTimeVar)
safeTimeVar=IntVar()
safeTimeVar.set(300)#seconds
safeTimeEntry = Entry(root,textvariable=safeTimeVar)
startRVar=IntVar()
startRVar.set(1500)
startREntry = Entry(root,textvariable=startRVar)
stopRVar=IntVar()
stopRVar.set(50)
stopREntry = Entry(root,textvariable=stopRVar)
gameRules={}
packNameVar=StringVar()
packNameVar.set("test")
packNameEntry = Entry(root,textvariable=packNameVar)
saveButton=Button(root,text="Make Pack",command=makePack)




r=0
packNameEntry.grid(row=r,column=1)
packNameLb.grid(row=r,column=0)

r+=1
totalGameTimeEntry.grid(row=r,column=1)
totalGameTimeLb.grid(row=r,column=0)
r+=1
safeTimeLb.grid(row=r,column=0)
safeTimeEntry.grid(row=r,column=1)
r+=1
roundTimeLb.grid(row=r,column=0)
roundTimeEntry.grid(row=r,column=1)
r+=1
startRLb.grid(row=r,column=0)
startREntry.grid(row=r,column=1)
r+=1
stopRLb.grid(row=r,column=0)
stopREntry.grid(row=r,column=1)
r+=1

saveButton.grid(row=r,column=1)
r+=1
