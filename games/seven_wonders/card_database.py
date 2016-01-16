from cards import *
from copy import deepcopy


################ AGE 1 CARDS ####################
age_1_cards = []
age = 1
tech_tree = {}
tech_tree['prev'] = []

#Blue cards:
name = "ALTAR"
cost_req = []
tech_tree['next'] = ["TEMPLE",]
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,2)
age_1_cards += [card,]
min_players = 5
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,2)
age_1_cards += [card,]
###
name = "BATHS"
cost_req = ["STONE",]
tech_tree['next'] = ["AQUEDUCT",]
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,3)
age_1_cards += [card,]
min_players = 7
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,3)
age_1_cards += [card,]
###
name = "PAWNSHOP"
cost_req = []
tech_tree['next'] = []
min_players = 4
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,3)
age_1_cards += [card,]
min_players = 7
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,3)
age_1_cards += [card,]
###
name = "THEATER"
cost_req = []
tech_tree['next'] = ['STATUE',]
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,2)
age_1_cards += [card,]
min_players = 6
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,2)
age_1_cards += [card,]

#Brown cards:
name = "CLAY PIT"
cost_req = [1,]
rsrc_list = ['BRICK','ORE']
token = ResourceToken(rsrc_list)
token_list = [token,]
min_players = 3
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "CLAY POOL"
cost_req = []
min_players = 3
rsrc_list = ['BRICK']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
min_players = 5
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "EXCAVATON"
cost_req = [1,]
min_players = 4
rsrc_list = ['STONE','BRICK']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "FOREST CAVE"
cost_req = [1,]
min_players = 5
rsrc_list = ['WOOD','ORE']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "LUMBER YARD"
cost_req = []
min_players = 3
rsrc_list = ['WOOD']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "MINE"
cost_req = [1,]
min_players = 6
rsrc_list = ['STONE','ORE']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "ORE VEIN"
cost_req = []
min_players = 3
rsrc_list = ['ORE']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "STONE PIT"
cost_req = []
min_players = 3
rsrc_list = ['STONE']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
min_players = 5
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "TIMBER YARD"
cost_req = [1,]
min_players = 3
rsrc_list = ['STONE','WOOD']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]
###
name = "TREE FARM"
cost_req = [1,]
min_players = 6
rsrc_list = ['WOOD','BRICK']
token = ResourceToken(rsrc_list)
token_list = [token,]
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_1_cards += [card,]


#Gray cards:
name = "GLASSWORKS"
min_players = 3
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
min_players = 6
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
###
name = "LOOM"
min_players = 3
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
min_players = 6
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
###
name = "PRESS"
min_players = 3
card = GrayResource(name, age, min_players)
age_1_cards += [card,]
min_players = 6
card = GrayResource(name, age, min_players)
age_1_cards += [card,]

#Green cards:
name = "APOTHECARY"
cost_req = ['LOOM']
tech_tree['next'] = ["STABLES","DISPENSARY"]
min_players = 3
science_type = "COMPASS"
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_1_cards += [card,]
min_players = 5
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_1_cards += [card,]
###
name = "SCRIPTORIUM"
cost_req = ['GLASSWORKS']
tech_tree['next'] = ["COURTHOUSE","LIBRARY"]
min_players = 3
science_type = "TABLET"
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_1_cards += [card,]
min_players = 4
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_1_cards += [card,]
###
name = "WORKSHOP"
cost_req = ['PRESS']
tech_tree['next'] = ["LABORATORY","ARCHERY RANGE"]
min_players = 3
science_type = "WHEEL"
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_1_cards += [card,]

#Red cards:
name = "BARRACKS"
cost_req = ["ORE",]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_1_cards += [card,]
min_players = 5
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_1_cards += [card,]
###
name = "GUARD TOWER"
cost_req = ["BRICK",]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_1_cards += [card,]
min_players = 4
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_1_cards += [card,]
###
name = "STOCKADE"
cost_req = ["WOOD",]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_1_cards += [card,]
min_players = 7
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_1_cards += [card,]

#Yellow cards:
name = "MARKETPLACE"
cost_req = []
tech_tree['next'] = ["CARAVANSERY",]
min_players = 3
descrip = "Allows you to buy gray resources from either of your "
descrip += "two neighbors for 1 coin instead of 2"
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 6
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
####
name = "TAVERN"
cost_req = []
tech_tree['next'] = []
min_players = 4
descrip = "Gives 5 gold instantly."
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 5
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
###
name = "EAST TRADING POST"
cost_req = []
tech_tree['next'] = ["FORUM",]
min_players = 3
descrip = "Allows you to buy brown resources from your "
descrip += "right neighbor for 1 coin instead of 2"
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
###
name = "WEST TRADING POST"
cost_req = []
tech_tree['next'] = ["FORUM",]
min_players = 3
descrip = "Allows you to buy brown resources from your "
descrip += "left neighbor for 1 coin instead of 2"
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_1_cards += [card,]
###

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################
###############################################################

age_2_cards = []
age = 2
tech_tree = {}

#Blue Cards:
name = "AQUEDUCT"
cost_req = ["STONE","STONE","STONE"]
tech_tree['prev'] = []
tech_tree['next'] = ["BATHS",]
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,5)
age_2_cards += [card,]
min_players = 7
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,5)
age_2_cards += [card,]
###
name = "COURTHOUSE"
cost_req = ["BRICK","BRICK","LOOM"]
tech_tree['prev'] = ["SCRIPTORIUM",]
tech_tree['next'] = []
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,4)
age_2_cards += [card,]
min_players = 5
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,4)
age_2_cards += [card,]
###
name = "STATUE"
cost_req = ["ORE","ORE","WOOD"]
tech_tree['prev'] = ["THEATER",]
tech_tree['next'] = ["GARDENS",]
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,4)
age_2_cards += [card,]
min_players = 7
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,4)
age_2_cards += [card,]
###
name = "TEMPLE"
cost_req = ["WOOD","BRICK","GLASSWORKS"]
tech_tree['prev'] = ["ALTAR",]
tech_tree['next'] = ["PANTHEON",]
min_players = 3
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,3)
age_2_cards += [card,]
min_players = 6
card = BlueCard(name, cost_req, deepcopy(tech_tree), age, min_players,3)
age_2_cards += [card,]

#Brown Cards:
name = "BRICKYARD"
cost_req = [1,]
rsrc_list = ['BRICK']
token = ResourceToken(rsrc_list)
token_list = [deepcopy(token),deepcopy(token),]
min_players = 3
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
###
name = "FOUNDRY"
cost_req = [1,]
rsrc_list = ['ORE']
token = ResourceToken(rsrc_list)
token_list = [deepcopy(token),deepcopy(token),]
min_players = 3
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
###
name = "QUARRY"
cost_req = [1,]
rsrc_list = ['STONE']
token = ResourceToken(rsrc_list)
token_list = [deepcopy(token),deepcopy(token),]
min_players = 3
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
###
name = "SAWMILL"
cost_req = [1,]
rsrc_list = ['WOOD']
token = ResourceToken(rsrc_list)
token_list = [deepcopy(token),deepcopy(token),]
min_players = 3
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]
min_players = 4
card = BrownResource(name, cost_req,  age, min_players, deepcopy(token_list))
age_2_cards += [card,]


#Gray cards:
name = "GLASSWORKS"
min_players = 3
card = GrayResource(name, age, min_players)
age_2_cards += [card,]
min_players = 5
card = GrayResource(name, age, min_players)
age_2_cards += [card,]
###
name = "LOOM"
min_players = 3
card = GrayResource(name, age, min_players)
age_2_cards += [card,]
min_players = 5
card = GrayResource(name, age, min_players)
age_2_cards += [card,]
###
name = "PRESS"
min_players = 3
card = GrayResource(name, age, min_players)
age_2_cards += [card,]
min_players = 5
card = GrayResource(name, age, min_players)
age_2_cards += [card,]

#Green Cards:
name = "DISPENSARY"
cost_req = ['ORE','ORE','GLASSWORKS']
tech_tree['prev'] = ["APOTHECARY"]
tech_tree['next'] = ["ARENA","LODGE"]
science_type = "COMPASS"
min_players = 3
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
min_players = 4
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
###
name = "LABORATORY"
cost_req = ['BRICK','BRICK','PRESS']
tech_tree['prev'] = ["WORKSHOP"]
tech_tree['next'] = ["SIEGE WORKSHOP","OBSERVATORY"]
science_type = "WHEEL"
min_players = 3
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
min_players = 5
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
###
name = "LIBRARY"
cost_req = ['STONE','STONE','LOOM']
tech_tree['prev'] = ["SCRIPTORIUM"]
tech_tree['next'] = ["SENATE","UNIVERSITY"]
science_type = "TABLET"
min_players = 3
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
min_players = 6
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
###
name = "SCHOOL"
cost_req = ['WOOD','PRESS']
tech_tree['prev'] = []
tech_tree['next'] = ["STUDY","ACADEMY"]
science_type = "TABLET"
min_players = 3
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players, \
		science_type)
age_2_cards += [card,]

#Red Cards:
name = "ARCHERY RANGE"
cost_req = ["WOOD","WOOD","ORE"]
tech_tree['prev'] = ["WORKSHOP"]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
min_players = 6
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
###
name = "STABLES"
cost_req = ["ORE","BRICK","WOOD"]
tech_tree['prev'] = ["APOTHECARY"]
tech_tree['next'] = []
min_players = 3
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
min_players = 5
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
###
name = "TRAINING GROUND"
cost_req = ["ORE","ORE","WOOD",]
tech_tree['prev'] = []
tech_tree['next'] = ["CIRCUS",]
min_players = 4
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
min_players = 6
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
min_players = 7
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
###
name = "WALLS"
cost_req = ["STONE",]*3
tech_tree['prev'] = []
tech_tree['next'] = ["FORTIFICATIONS",]
min_players = 3
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]
min_players = 7
card = RedCard(name, cost_req, deepcopy(tech_tree), age, min_players)
age_2_cards += [card,]


#Yellow Cards:
name = "BAZAR"
cost_req = []
tech_tree['prev'] = []
tech_tree['next'] = []
descrip = "Gives 2 gold for each gray card that you and your 2 neighbors"
descrip += " have."
min_players = 4
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_2_cards += [card,]
min_players = 7
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_2_cards += [card,]
###
name = "CARAVANSERY"
min_players = 3
card = YellowResource(name, min_players)
age_2_cards += [card,]
min_players = 5
card = YellowResource(name, min_players)
age_2_cards += [card,]
min_players = 6
card = YellowResource(name, min_players)
age_2_cards += [card,]
###
name = "FORUM"
min_players = 3
card = YellowResource(name, min_players)
age_2_cards += [card,]
min_players = 6
card = YellowResource(name, min_players)
age_2_cards += [card,]
min_players = 7
card = YellowResource(name, min_players)
age_2_cards += [card,]
###
name = "VINEYARD"
cost_req = []
tech_tree['prev'] = []
tech_tree['next'] = []
descrip = "Gives 1 gold for each brown card that you and your 2 neighbors"
descrip += " have."
min_players = 3
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_2_cards += [card,]
min_players = 6
card = YellowCard(name, cost_req, deepcopy(tech_tree), age, min_players,\
		descrip)
age_2_cards += [card,]

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################

age_3_cards = []
age = 3
tech_tree = {}
tech_tree['next'] = []

###############################################################
###############################################################
###############################################################
###############################################################
###############################################################



