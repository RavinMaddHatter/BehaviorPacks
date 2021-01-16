import json
true=True
false=False

test={
	"format_version": "1.13.0",
	"minecraft:entity": {
		"description": {
			"identifier": "fmb:acacia_leaves",
			"is_spawnable": true,
			"is_summonable": true,
			"is_experimental": false,
			"scripts": {
				"animate": [
					"fmb:rotateAlign",
					"fmb:positionX",
					"fmb:positionY",
					"fmb:positionZ"
				]
			},
			"animations": {
				"fmb:rotateAlign" : "controller.animation.fmb.rotateAlign",
				"fmb:positionX" : "controller.animation.fmb.positionX",
				"fmb:positionY" : "controller.animation.fmb.positionY",
				"fmb:positionZ" : "controller.animation.fmb.positionZ"
			}
		},
		"component_groups": {
			"fmb:default": {
				"minecraft:environment_sensor": {
					"triggers": [
						{
							"filters": {
								"any_of": [
									{
										"test": "is_altitude",
										"subject": "self",
										"operator": ">=",
										"value": 255
									},
									{
										"test": "is_altitude",
										"subject": "self",
										"operator": "<=",
										"value": 4
									}
								]
							},
							"target": "self",
							"event": "fmb:pickup"
						}
					]
				}
			},
			"fmb:pickup": {
				"minecraft:despawn": {}
			},
			"fmb:scaleS": {				
				"minecraft:rideable": {
					"seat_count": 1,
					"interact_text": "Sit",
					"pull_in_entities": false,
					"crouching_skip_interact": true,
					"family_types": [
						"player"
					],
					"seats": {
						"position": [
							0.0,
							0.2,
							0.0
						]
					}
				},
				"minecraft:scale": {
					"value": 0.25
				}
			},
			"fmb:scaleM": {				
				"minecraft:rideable": {
					"seat_count": 1,
					"interact_text": "Sit",
					"pull_in_entities": false,
					"crouching_skip_interact": true,
					"family_types": [
						"player"
					],
					"seats": {
						"position": [
							0.0,
							0.5,
							0.0
						]
					}
				},
				"minecraft:scale": {
					"value": 0.5
				}
			},
			"fmb:scaleL": {		
				"minecraft:rideable": {
					"seat_count": 1,
					"interact_text": "Sit",
					"pull_in_entities": false,
					"crouching_skip_interact": true,
					"family_types": [
						"player"
					],
					"seats": {
						"position": [
							0.0,
							0.8,
							0.0
						]
					}
				},
				"minecraft:scale": {
					"value": 1.0
				}
			},
			"fmb:rotateAlign": {		
				"minecraft:is_illager_captain": {}
			},
			"fmb:rotateX": {					
				"minecraft:environment_sensor": {
					"triggers": [
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 0
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_45"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 45
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_90"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 90
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_135"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 135
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_180"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 180
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_225"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 225
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_270"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 270
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_315"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_variant",
										"value": 315
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateX_0"
						}
					]
				}
			},
			"fmb:rotateX_0": {
				"minecraft:variant": {
					"value": 0
				}
			},
			"fmb:rotateX_45": {
				"minecraft:variant": {
					"value": 45
				}
			},
			"fmb:rotateX_90": {
				"minecraft:variant": {
					"value": 90
				}
			},
			"fmb:rotateX_135": {
				"minecraft:variant": {
					"value": 135
				}
			},
			"fmb:rotateX_180": {
				"minecraft:variant": {
					"value": 180
				}
			},
			"fmb:rotateX_225": {
				"minecraft:variant": {
					"value": 225
				}
			},
			"fmb:rotateX_270": {
				"minecraft:variant": {
					"value": 270
				}
			},
			"fmb:rotateX_315": {
				"minecraft:variant": {
					"value": 315
				}
			},		
			"fmb:rotateY": {					
				"minecraft:environment_sensor": {
					"triggers": [
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 0
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_45"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 45
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_90"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 90
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_135"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 135
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_180"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 180
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_225"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 225
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_270"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 270
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_315"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_skin_id",
										"value": 315
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateY_0"
						}
					]
				}
			},
			"fmb:rotateY_0": {
				"minecraft:skin_id": {
					"value": 0
				}
			},
			"fmb:rotateY_45": {
				"minecraft:skin_id": {
					"value": 45
				}
			},
			"fmb:rotateY_90": {
				"minecraft:skin_id": {
					"value": 90
				}
			},
			"fmb:rotateY_135": {
				"minecraft:skin_id": {
					"value": 135
				}
			},
			"fmb:rotateY_180": {
				"minecraft:skin_id": {
					"value": 180
				}
			},
			"fmb:rotateY_225": {
				"minecraft:skin_id": {
					"value": 225
				}
			},
			"fmb:rotateY_270": {
				"minecraft:skin_id": {
					"value": 270
				}
			},
			"fmb:rotateY_315": {
				"minecraft:skin_id": {
					"value": 315
				}
			},
			"fmb:rotateZ": {					
				"minecraft:environment_sensor": {
					"triggers": [
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 0
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_45"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 45
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_90"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 90
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_135"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 135
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_180"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 180
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_225"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 225
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_270"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 270
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_315"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_mark_variant",
										"value": 315
									}
								]
							},
							"target": "self",
							"event": "fmb:rotateZ_0"
						}
					]
				}
			},
			"fmb:rotateZ_0": {
				"minecraft:mark_variant": {
					"value": 0
				}
			},
			"fmb:rotateZ_45": {
				"minecraft:mark_variant": {
					"value": 45
				}
			},
			"fmb:rotateZ_90": {
				"minecraft:mark_variant": {
					"value": 90
				}
			},
			"fmb:rotateZ_135": {
				"minecraft:mark_variant": {
					"value": 135
				}
			},
			"fmb:rotateZ_180": {
				"minecraft:mark_variant": {
					"value": 180
				}
			},
			"fmb:rotateZ_225": {
				"minecraft:mark_variant": {
					"value": 225
				}
			},
			"fmb:rotateZ_270": {
				"minecraft:mark_variant": {
					"value": 270
				}
			},
			"fmb:rotateZ_315": {
				"minecraft:mark_variant": {
					"value": 315
				}
			},
			"fmb:positionX": {		
				"minecraft:is_sheared": {},
				"minecraft:timer": {
					"time": 0.1,
					"time_down_event": {
						"event": "fmb:positionXStop",
						"target": "self"
					}
				}
			},
			"fmb:positionXM": {		
				"minecraft:is_stunned": {},
				"minecraft:timer": {
					"time": 0.1,
					"time_down_event": {
						"event": "fmb:positionXStop",
						"target": "self"
					}
				}
			},
			"fmb:positionY": {		
				"minecraft:is_baby": {},
				"minecraft:timer": {
					"time": 0.1,
					"time_down_event": {
						"event": "fmb:positionYStop",
						"target": "self"
					}
				}
			},
			"fmb:positionYM": {		
				"minecraft:is_stackable": {},
				"minecraft:timer": {
					"time": 0.1,
					"time_down_event": {
						"event": "fmb:positionYStop",
						"target": "self"
					}
				}
			},
			"fmb:positionZ": {		
				"minecraft:is_tamed": {},
				"minecraft:timer": {
					"time": 0.1,
					"time_down_event": {
						"event": "fmb:positionZStop",
						"target": "self"
					}
				}
			},
			"fmb:positionZM": {		
				"minecraft:is_saddled": {},
				"minecraft:timer": {
					"time": 0.1,
					"time_down_event": {
						"event": "fmb:positionZStop",
						"target": "self"
					}
				}
			},
			"fmb:changeTexture": {
				"minecraft:environment_sensor": {
					"triggers": [
						{
							"filters": {
								"any_of": [
									{
										"test": "is_family",
										"value": "16Bit"
									}
								]
							},
							"target": "self",
							"event": "fmb:alternateTexture"
						},
						{
							"filters": {
								"any_of": [
									{
										"test": "is_family",
										"value": "8Bit"
									}
								]
							},
							"target": "self",
							"event": "fmb:defaultTexture"
						}
					]
				}
			},
			"fmb:defaultTexture": {	
				"minecraft:type_family": {
					"family": [
						"fmb_skull",
						"inanimate",
						"16Bit"
					]
				}
			},
			"fmb:alternateTexture": {	
				"minecraft:is_chested": {},
				"minecraft:type_family": {
					"family": [
						"fmb_skull",
						"inanimate",
						"8Bit"
					]
				}
			}
		},
		"components": { 
			"minecraft:variant": {
				"value": 0
			},		
			"minecraft:mark_variant": {
				"value": 0
			},	
			"minecraft:skin_id": {
				"value": 0
			},	
			"minecraft:rideable": {
				"seat_count": 1,
				"interact_text": "Sit",
				"pull_in_entities": false,
				"crouching_skip_interact": true,
				"family_types": [
					"player"
				],
				"seats": {
					"position": [
						0.0,
						0.5,
						0.0
					]
				}
			},
			"minecraft:scale": {
				"value": 0.5
			},
			"minecraft:navigation.generic": {
				"can_sink": false
			},
			"minecraft:environment_sensor": {
				"triggers": [
					{
						"filters": {
							"any_of": [
								{
									"test": "is_altitude",
									"subject": "self",
									"operator": ">=",
									"value": 255
								},
								{
									"test": "is_altitude",
									"subject": "self",
									"operator": "<=",
									"value": 4
								}
							]
						},
						"target": "self",
						"event": "fmb:pickup"
					}
				]
			},
			"minecraft:damage_sensor": {
				"triggers": {
					"cause": "all",
					"deals_damage": false
				}
			},
			"minecraft:interact": {
				"interactions": [
					{
						"hurt_item": 0,
						"interact_text": "Scale Micro",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:19"
									}
								]
							},
							"event": "fmb:scaleS",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Scale Mini",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:8"
									}
								]
							},
							"event": "fmb:scaleM",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Scale Large",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:16"
									}
								]
							},
							"event": "fmb:scaleL",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Rotation Align",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:1"
									}
								]
							},
							"event": "fmb:rotateAlign",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Rotate X",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:2"
									}
								]
							},
							"event": "fmb:rotateX",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Rotate Y",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:18"
									}
								]
							},
							"event": "fmb:rotateY",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Rotate Z",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:11"
									}
								]
							},
							"event": "fmb:rotateZ",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Position X",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:14"
									}
								]
							},
							"event": "fmb:positionX",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Position -X",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:17"
									}
								]
							},
							"event": "fmb:positionXM",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Position Y",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:9"
									}
								]
							},
							"event": "fmb:positionY",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Position -Y",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:5"
									}
								]
							},
							"event": "fmb:positionYM",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Position Z",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:10"
									}
								]
							},
							"event": "fmb:positionZ",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Position -Z",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:6"
									}
								]
							},
							"event": "fmb:positionZM",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Switch Texture",
						"on_interact": {
							"filters": {
								"all_of": [
									{
										"test": "has_equipment",
										"subject": "player",
										"value": "dye:13"
									}
								]
							},
							"event": "fmb:changeTexture",
							"target": "self"
						},
						"play_sounds": "drop.slot",
						"swing": true,
						"use_item": false
					},
					{
						"hurt_item": 0,
						"interact_text": "Pick Up",
						"on_interact": {
							"filters": {
								"any_of": [
									{
										"test": "is_sneaking",
										"subject": "player"
									}
								]
							},
							"event": "fmb:pickup",
							"target": "self"
						},
						"play_sounds": "pop",
						"swing": true,
						"use_item": false,
						"spawn_items": {
							"table": "loot_tables/fmb/acacia_leaves.json"
						}
					}
				]
			},
			"minecraft:type_family": {
				"family": [
					"fmb_skull",
					"inanimate",
					"16Bit"
				]
			},
			"minecraft:collision_box": {
				"width": 0.5,
				"height": 0.5
			},
			"minecraft:health": {
				"value": 0.5,
				"max": 0.5
			},
			"minecraft:nameable": {},
			"minecraft:persistent": {},
			"minecraft:physics": {
				"has_gravity": false,
				"has_collision": false
			},
			"minecraft:pushable": {
				"is_pushable": false,
				"is_pushable_by_piston": true
			},
			"minecraft:fire_immune": true
		},
		"events": {
			"minecraft:entity_spawned": {
				"add": {
					"component_groups": [
						"fmb:default",
						"fmb:scaleM"
					]
				}
			},
			"fmb:pickup": {
				"add": {
					"component_groups": [
						"fmb:pickup"
					]
				}
			},
			"fmb:scaleS": {
				"remove": {
					"component_groups": [
						"fmb:scaleM",
						"fmb:scaleL"
					]
				},
				"add": {
					"component_groups": [
						"fmb:scaleS"
					]
				}
			},
			"fmb:scaleM": {
				"remove": {
					"component_groups": [
						"fmb:scaleS",
						"fmb:scaleL"
					]
				},
				"add": {
					"component_groups": [
						"fmb:scaleM"
					]
				}
			},
			"fmb:scaleL": {
				"remove": {
					"component_groups": [
						"fmb:scaleS",
						"fmb:scaleM"
					]
				},
				"add": {
					"component_groups": [
						"fmb:scaleL"
					]
				}
			},
			"fmb:rotateAlign": {
				"add": {
					"component_groups": [
						"fmb:rotateAlign"
					]
				}
			},
			"fmb:rotateAlignStop": {
				"remove": {
					"component_groups": [
						"fmb:rotateAlign"
					]
				}
			},
			"fmb:rotateX": {
				"add": {
					"component_groups": [
						"fmb:rotateX"
					]
				}
			},
			"fmb:rotateX_0": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_0"
					]
				}
			},
			"fmb:rotateX_45": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_45"
					]
				}
			},
			"fmb:rotateX_90": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_90"
					]
				}
			},
			"fmb:rotateX_135": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_135"
					]
				}
			},
			"fmb:rotateX_180": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_180"
					]
				}
			},
			"fmb:rotateX_225": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_225"
					]
				}
			},
			"fmb:rotateX_270": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_270"
					]
				}
			},
			"fmb:rotateX_315": {
				"remove": {
					"component_groups": [
						"fmb:rotateX"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateX_315"
					]
				}
			},
			"fmb:rotateY": {
				"add": {
					"component_groups": [
						"fmb:rotateY"
					]
				}
			},
			"fmb:rotateY_0": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_0"
					]
				}
			},
			"fmb:rotateY_45": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_45"
					]
				}
			},
			"fmb:rotateY_90": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_90"
					]
				}
			},
			"fmb:rotateY_135": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_135"
					]
				}
			},
			"fmb:rotateY_180": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_180"
					]
				}
			},
			"fmb:rotateY_225": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_225"
					]
				}
			},
			"fmb:rotateY_270": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_270"
					]
				}
			},
			"fmb:rotateY_315": {
				"remove": {
					"component_groups": [
						"fmb:rotateY"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateY_315"
					]
				}
			},
			"fmb:rotateZ": {
				"add": {
					"component_groups": [
						"fmb:rotateZ"
					]
				}
			},
			"fmb:rotateZ_0": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_0"
					]
				}
			},
			"fmb:rotateZ_45": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_45"
					]
				}
			},
			"fmb:rotateZ_90": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_90"
					]
				}
			},
			"fmb:rotateZ_135": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_135"
					]
				}
			},
			"fmb:rotateZ_180": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_180"
					]
				}
			},
			"fmb:rotateZ_225": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_225"
					]
				}
			},
			"fmb:rotateZ_270": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_270"
					]
				}
			},
			"fmb:rotateZ_315": {
				"remove": {
					"component_groups": [
						"fmb:rotateZ"
					]
				},
				"add": {
					"component_groups": [
						"fmb:rotateZ_315"
					]
				}
			},
			"fmb:positionX": {
				"add": {
					"component_groups": [
						"fmb:positionX"
					]
				}
			},
			"fmb:positionXM": {
				"add": {
					"component_groups": [
						"fmb:positionXM"
					]
				}
			},
			"fmb:positionXStop": {
				"remove": {
					"component_groups": [
						"fmb:positionX",
						"fmb:positionXM"
					]
				}
			},
			"fmb:positionY": {
				"add": {
					"component_groups": [
						"fmb:positionY"
					]
				}
			},
			"fmb:positionYM": {
				"add": {
					"component_groups": [
						"fmb:positionYM"
					]
				}
			},
			"fmb:positionYStop": {
				"remove": {
					"component_groups": [
						"fmb:positionY",
						"fmb:positionYM"
					]
				}
			},
			"fmb:positionZ": {
				"add": {
					"component_groups": [
						"fmb:positionZ"
					]
				}
			},
			"fmb:positionZM": {
				"add": {
					"component_groups": [
						"fmb:positionZM"
					]
				}
			},
			"fmb:positionZStop": {
				"remove": {
					"component_groups": [
						"fmb:positionZ",
						"fmb:positionZM"
					]
				}
			},
			"fmb:changeTexture": {
				"add": {
					"component_groups": [
						"fmb:changeTexture"
					]
				}
			},
			"fmb:alternateTexture": {
				"remove": {
					"component_groups": [
						"fmb:changeTexture",
						"fmb:defaultTexture"
					]
				},
				"add": {
					"component_groups": [
						"fmb:alternateTexture"
					]
				}
			},
			"fmb:defaultTexture": {
				"remove": {
					"component_groups": [
						"fmb:changeTexture",
						"fmb:alternateTexture"
					]
				},
				"add": {
					"component_groups": [
						"fmb:defaultTexture"
					]
				}
			}
		}
	}
}
json.dumps(test)
import pprint
for i in test["minecraft:entity"]["components"]["minecraft:interact"]["interactions"]:
    pprint.pprint(i)
