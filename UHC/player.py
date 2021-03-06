false=False
true=True
player={
	"format_version": "1.16.0",
	"minecraft:entity": {
		"description": {
			"identifier": "minecraft:player",
			"is_spawnable": false,
			"is_summonable": false,
			"is_experimental": false,
			"scripts": {
				"animate": [
					"health",
					"health",
					"spectator",
					"adventure"
				]
			},
			"animations": {
				"health": "controller.animation.health",
				"start": "animation.start",
				"spectator": "controller.animation.spectator",
				"adventure": "controller.animation.adventure"
			}
		},
		"component_groups": {
			"minecraft:add_bad_omen": {
				"minecraft:spell_effects": {
					"add_effects": [
						{
							"effect": "bad_omen",
							"duration": 6000,
							"display_on_screen_animation": true
						}
					]
				},
				"minecraft:timer": {
					"time": [
						0,
						0
					],
					"looping": false,
					"time_down_event": {
						"event": "minecraft:clear_add_bad_omen",
						"target": "self"
					}
				}
			},
			"minecraft:clear_bad_omen_spell_effect": {
				"minecraft:spell_effects": {}
			},
			"minecraft:raid_trigger": {
				"minecraft:raid_trigger": {
					"triggered_event": {
						"event": "minecraft:remove_raid_trigger",
						"target": "self"
					}
				},
				"minecraft:spell_effects": {
					"remove_effects": "bad_omen"
				}
			},
			"hc:spectator": {
				"minecraft:is_baby": {},
				"minecraft:is_tamed": {},
				"minecraft:is_chested": {},
				"minecraft:type_family": {
					"family": [
						"undead"
					]
				},
				"minecraft:collision_box": {
					"width": 0.01,
					"height": 0.01
				},
				"minecraft:damage_sensor": {
					"triggers": {
						"cause": "all",
						"deals_damage": false
					}
				}
			},
			"hc:player": {
				"minecraft:collision_box": {
					"width": 0.6,
					"height": 1.8
				},
				"minecraft:type_family": {
					"family": [
						"player"
					]
				},
				"minecraft:is_chested": {}
			}
		},
		"components": {
			"minecraft:experience_reward": {
				"on_death": "Math.Min(query.player_level * 7, 100)"
			},
			"minecraft:is_hidden_when_invisible": {},
			"minecraft:loot": {
				"table": "loot_tables/empty.json"
			},
			"minecraft:can_climb": {},
			"minecraft:movement": {
				"value": 0.1
			},
			"minecraft:hurt_on_condition": {
				"damage_conditions": [
					{
						"filters": {
							"test": "in_lava",
							"subject": "self",
							"operator": "==",
							"value": true
						},
						"cause": "lava",
						"damage_per_tick": 4
					}
				]
			},
			"minecraft:attack": {
				"damage": 1
			},
			"minecraft:player.saturation": {
				"value": 20
			},
			"minecraft:player.exhaustion": {
				"value": 0,
				"max": 4
			},
			"minecraft:player.level": {
				"value": 0,
				"max": 24791
			},
			"minecraft:player.experience": {
				"value": 0,
				"max": 1
			},
			"minecraft:breathable": {
				"total_supply": 15,
				"suffocate_time": -1,
				"inhale_time": 3.75,
				"generates_bubbles": false
			},
			"minecraft:nameable": {
				"always_show": true,
				"allow_name_tag_renaming": false
			},
			"minecraft:physics": {},
			"minecraft:pushable": {
				"is_pushable": false,
				"is_pushable_by_piston": true
			},
			"minecraft:insomnia": {
				"days_until_insomnia": 3
			},
			"minecraft:rideable": {
				"seat_count": 2,
				"family_types": [
					"parrot_tame"
				],
				"pull_in_entities": true,
				"seats": [
					{
						"position": [
							0.4,
							-0.2,
							-0.1
						],
						"min_rider_count": 0,
						"max_rider_count": 0,
						"lock_rider_rotation": 0
					},
					{
						"position": [
							-0.4,
							-0.2,
							-0.1
						],
						"min_rider_count": 1,
						"max_rider_count": 2,
						"lock_rider_rotation": 0
					}
				]
			},
			"minecraft:conditional_bandwidth_optimization": {},
			"minecraft:scaffolding_climber": {},
			"minecraft:environment_sensor": {
				"triggers": {
					"filters": {
						"all_of": [
							{
								"test": "has_mob_effect",
								"subject": "self",
								"value": "bad_omen"
							},
							{
								"test": "is_in_village",
								"subject": "self",
								"value": true
							}
						]
					},
					"event": "minecraft:trigger_raid"
				}
			}
		},
		"events": {
			"minecraft:gain_bad_omen": {
				"add": {
					"component_groups": [
						"minecraft:add_bad_omen"
					]
				}
			},
			"minecraft:clear_add_bad_omen": {
				"remove": {
					"component_groups": [
						"minecraft:add_bad_omen"
					]
				},
				"add": {
					"component_groups": [
						"minecraft:clear_bad_omen_spell_effect"
					]
				}
			},
			"minecraft:trigger_raid": {
				"add": {
					"component_groups": [
						"minecraft:raid_trigger"
					]
				}
			},
			"minecraft:remove_raid_trigger": {
				"remove": {
					"component_groups": [
						"minecraft:raid_trigger"
					]
				}
			},
			"hc:add_spectator": {
				"add": {
					"component_groups": [
						"hc:spectator"
					]
				},
				"remove": {
					"component_groups": [
						"hc:player"
					]
				}
			},
			"hc:remove_spectator": {
				"remove": {
					"component_groups": [
						"hc:spectator"
					]
				},
				"add": {
					"component_groups": [
						"hc:player"
					]
				}
			}
		}
	}
}


spectator={
	"format_version": "1.10.0",
	"animation_controllers": {
		"controller.animation.spectator": {
			"initial_state": "default",
			"states": {
				"default": {
					"transitions": [
						{
							"in_spectator": "query.is_baby"
						}
					]
				},
				"in_spectator": {
					"on_entry": [
						"/function lock_inventory"
					],
					"transitions": [
						{
							"default": "math.mod(query.time_stamp,10)==1"
						}
					]
				}
			}
		},
		"controller.animation.adventure": {
			"initial_state": "survival",
			"states": {
				"survival": {
					"transitions": [
						{
							"adventure": "query.is_tamed"
						},
						{
							"default": "!query.is_chested\t"
						}
					]
				},
				"adventure": {
					"on_entry": [
						"/gamemode a @s",
						"/tag @s add dead",
						"/ability @s mayfly true"
					],
					"transitions": [
						{
							"survival": "!query.is_tamed"
						}
					],
					"on_exit": [
						"/gamemode s @s",
						"/tag @s remove dead",
						"/ability @s mayfly false",
						"/clear @s"
					]
				},
				"default": {
					"on_entry": [
						"@s hc:remove_spectator"
					],
					"transitions": [
						{
							"survival": "1==1"
						}
					]
				}
			}
		}
	}
}
