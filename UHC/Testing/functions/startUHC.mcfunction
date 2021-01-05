tickingarea add circle 0 0 0 2 zeroTicking
spreadplayers 0 0 1 20 @a
gamerule showcoordinates true
fill -1 65 -1 1 63 1 barrier
fill 0 64 0 0 64 0 air
summon uhc:game_controller zero 0 64 0
scoreboard objectives add detect_health dummy Health
scoreboard players set @a detect_health 20
scoreboard objectives setdisplay sidebar detect_health descending
gamerule naturalregeneration false
tag @a remove dead
effect @a slow_falling 90 1 true
spreadplayers 0 0 200 1050.0 @a
gamerule pvp false
gamemode s @a
event entity @a hc:remove_spectator
effect @a instant_health 1 255 false
effect @a saturation 1 20 false
title @a actionbar Game Start 5.0 min of No PVP starts now

