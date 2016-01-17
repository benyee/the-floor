

class Card(object):
    """Represents a card in the 7 wonders game.  Each type of card (resource,
       military, etc.) will inherit from this class.

    Attributes:
        name: string representing the card name (all caps)
        brwn_rsrc_req: list of brown resources required (empty if free)
        gry_rsrc_req: list of gray resources required (empty if free)
        coins_req: integer representing the # of coins required
        tech_tree['prev']: list of cards that make this card free
        tech_tree['next']: list of cards that this card makes free
        age: 1, 2, or 3
        min_players: 3, 4, 5, 6, or 7
        color: string representing the color of the card (all lowercase)
        descrip: string describing what the card does
    """
    gry_rsrc_list = ['LOOM', 'GLASSWORKS', 'PRESS']
    brwn_rsrc_list = ['WOOD', 'ORE', 'BRICK', 'STONE']

    def __init__(self, name, cost_req, tech_tree, age, min_players, descrip,
                 color=None):
        """cost_req is a list of costs required.  If there is a coin cost,
            enter an integer as one of the list items."""

        self.name = name
        assert(type(name) is str)
        self.tech_tree = tech_tree
        assert(type(tech_tree) is dict)
        assert('prev' in tech_tree.keys())
        assert('next' in tech_tree.keys())
        self.age = age
        assert(age in [1, 2, 3])
        self.min_players = min_players
        assert(min_players in [3, 4, 5, 6, 7])
        self.descrip = descrip
        assert(type(descrip) is str)

        # Color should be assigned by the classes inheriting this one
        self.color = color

        self.brwn_rsrc_req = []
        self.gry_rsrc_req = []
        self.coins_req = 0

        if cost_req is None:
            return
        for cost in cost_req:
            if type(cost) is int:
                self.coins_req = cost
                continue

            assert(type(cost) is str)
            if cost in self.gry_rsrc_list:
                self.gry_rsrc_req += [cost, ]
            elif cost in self.brwn_rsrc_list:
                self.brwn_rsrc_req += [cost, ]

    def __str__(self):
        rsrc_req = self.brwn_rsrc_req+self.gry_rsrc_req
        print len(rsrc_req)
        if self.coins_req > 0:
            rsrc_req += [str(self.coins_req)+" coins", ]

        out_str = "Card name: " + self.name
        out_str += "\n Color: " + self.color
        out_str += "\n Cost: " + str(rsrc_req)
        if len(self.tech_tree['prev']) > 0:
            out_str += "\n This card can be built for free with: "
            for prev_card in self.tech_tree['prev']:
                out_str += prev_card + ', '
        if len(self.tech_tree['next']) > 0:
            out_str += "\n This card allows you to build the following cards "\
                + "for free: "
            for next_card in self.tech_tree['next']:
                out_str += next_card + ', '
        out_str += "\n Description: " + self.descrip
        out_str += "\n Age: "+str(self.age)
        return out_str

    def instant_effect(self, curr_player, left_neighbor, right_neighbor):
        """ Alters the status (e.g., how much gold they have) of a player
             based on the cards he and his neighbor owns.
        """
        # Default is to do nothing
        return

    def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
        """ Returns the number of victory points granted by this card.  Takes
             into account the possessions of the player and his neighbors.
        """
        # Default is 0 victory points
        return 0


class ResourceCard(Card):
    """Represents a brown or gray resource card.

    Attributes:
        token_list: list of ResourceToken pointers associated with this
                    resource card
    """
    def __init__(self, name, cost_req, tech_tree, age, min_players, token_list,
                 color=None):

        assert(len(token_list) > 0)
        assert(age < 3)

        descrip = "Provides"
        for token in token_list:
            descrip += " 1 "+str(token)+', '
        descrip = descrip[:-1]+'.'

        Card.__init__(self, name, cost_req, tech_tree, age, min_players,
                      descrip, color)

        self.token_list = token_list


class BrownResource(ResourceCard):
    """Represents a brown resource card.
    """
    def __init__(self, name, cost_req, age, min_players, token_list):
        """ rsrc_list is a list of rsrcs provided by the card """

        tech_tree = {}
        tech_tree['prev'] = []
        tech_tree['next'] = []
        ResourceCard.__init__(self, name, cost_req, tech_tree, age,
                              min_players, token_list, color="brown")


class GrayResource(ResourceCard):
    """Represents a gray resource card.

    """
    def __init__(self, name, age, min_players):
        """ rsrc_list is a list of rsrcs provided by the card """

        rsrc_list = [name, ]
        cost_req = []
        tech_tree = {}
        tech_tree['prev'] = []
        tech_tree['next'] = []

        token = ResourceToken(rsrc_list)
        token_list = [token, ]

        ResourceCard.__init__(self, name, cost_req, tech_tree, age,
                              min_players, token_list, color="gray")


class YellowCard(Card):
    """Represents a yellow card that does NOT provide resources.

        There are many types of yellow cards, and many classes must be written
        for each of them.
    """

    def __init__(self, name, cost_req, tech_tree, age, min_players, descrip):
        Card.__init__(self, name, cost_req, tech_tree, age, min_players,
                      descrip, color="yellow")

    def instant_effect(self, curr_player, left_neighbor, right_neighbor):
        players = [curr_player, left_neighbor, right_neighbor]
        if self.name == "TAVERN":
            curr_player.gold += 5
        elif self.name == "VINEYARD":
            for player in players:
                curr_player.gold += player.get_num_color("brown")
        elif self.name == "BAZAR":
            for player in players:
                curr_player.gold += 2*player.get_num_color("gray")
        elif self.name == "HAVEN":
            curr_player.gold += curr_player.get_num_color("brown")
        elif self.name == "LIGHTHOUSE":
            # MAKE SURE THIS DOESN'T COUNT ITSELF TWICE!
            # MAKE SURE IT COUNTS ITSELF ONCE!
            curr_player.gold += curr_player.get_num_color("yellow")
        elif self.name == "CHAMBER OF COMMERCE":
            curr_player.gold += 2*curr_player.get_num_color("gray")
        elif self.name == "ARENA":
            curr_player.gold += 3*curr_player.get_wonders_built()

    def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
        if self.name == "HAVEN":
            return curr_player.get_num_color("brown")
        elif self.name == "LIGHTHOUSE":
            # MAKE SURE THIS COUNTS ITSELF!
            return curr_player.get_num_color("yellow")
        elif self.name == "CHAMBER OF COMMERCE":
            return 2*curr_player.get_num_color("gray")
        elif self.name == "ARENA":
            return curr_player.get_wonders_built()
        return 0


class YellowResource(ResourceCard):
    """A yellow card that provides resources.  This must be a FORUM or
        CARAVANSERY"

    """
    def __init__(self, name, min_players):
        """ rsrc_list is a list of rsrcs provided by the card """

        cost_req = ['WOOD', 'WOOD']
        tech_tree = {}

        if name == "FORUM":
            cost_req = ['BRICK', 'BRICK', ]
            tech_tree['prev'] = ['WEST TRADING POST', 'EAST TRADING POST', ]
            tech_tree['next'] = ['HAVEN', ]
        else:
            assert(name == "CARAVANSERY")
            tech_tree['prev'] = ['MARKETPLACE', ]
            tech_tree['next'] = ['LIGHTHOUSE', ]

        token_list = []
        if name == "FORUM":
            token = ResourceToken(self.gry_rsrc_list, is_shareable=False)
            token_list = [token, ]
        elif name == "CARAVANSERY":
            token = ResourceToken(self.brwn_rsrc_list, is_shareable=False)
            token_list = [token, ]

        ResourceCard.__init__(self,
                              name=name,
                              cost_req=cost_req,
                              tech_tree=tech_tree,
                              age=2,
                              min_players=min_players,
                              token_list=token_list,
                              color="yellow")


class RedCard(Card):
    """ Represents a military card.
        Note that military power is equal to age number.
    """

    def __init__(self, name, cost_req, tech_tree, age, min_players):
        descrip = "Provides "+str(age)+" military power."
        Card.__init__(self, name, cost_req, tech_tree, age, min_players,
                      descrip, color="red")


class GreenCard(Card):
    """ Represents a science card.

        Attributes:
         science_type = "TABLET", "COMPASS", or "WHEEL"
    """

    def __init__(self, name, cost_req, tech_tree, age, min_players, sci_type):
        assert(sci_type in ["TABLET", "COMPASS", "WHEEL"])
        descrip = "Provides a " + sci_type
        Card.__init__(self, name, cost_req, tech_tree, age, min_players,
                      descrip, color="green")


class BlueCard(Card):
    """ Represents a blue card.

        Attributes:
        victory_points = victory points provided
    """

    def __init__(self, name, cost_req, tech_tree, age, min_players,
                 victory_points):
        assert(type(victory_points) is int)
        descrip = "Provides " + str(victory_points) + " victory points."
        Card.__init__(self, name, cost_req, tech_tree, age, min_players,
                      descrip, color="blue")

        self.victory_points = victory_points

    def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
        return self.victory_points


class PurpleCard(Card):
    """ Represents a purple card.
    """

    def __init__(self, name, cost_req, tech_tree, age, min_players, descrip):
        assert(name[-6:] == " GUILD")
        Card.__init__(self, name, cost_req, tech_tree, age, min_players,
                      descrip, color="purple")

    def get_victory_points(self, curr_player, left_neighbor, right_neighbor):
        guild_title = self.name[:-6]
        players = [curr_player, left_neighbor, right_neighbor]
        neighbors = [left_neighbor, right_neighbor]

        if guild_title == "BUILDERS":
            vic_pts = 0
            for player in players:
                vic_pts += player.get_wonders_built()
            return vic_pts
        elif guild_title == "CRAFTMENS":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += 2*neighbor.get_num_color("gray")
            return vic_pts
        elif guild_title == "MAGISTRATES":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += neighbor.get_num_color("blue")
            return vic_pts
        elif guild_title == "PHILOSOPHERS":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += neighbor.get_num_color("green")
            return vic_pts
        elif guild_title == "SHIPOWNERS":
            vic_pts = 0
            for color in ["brown", "gray", "purple"]:
                vic_pts += curr_player.get_num_color(color)
            return vic_pts
        elif guild_title == "SPIES":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += neighbor.get_num_color("red")
            return vic_pts
        elif guild_title == "STRATEGISTS":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += neighbor.get_num_military_losses()
            return vic_pts
        elif guild_title == "TRADERS":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += neighbor.get_num_color("yellow")
            return vic_pts
        elif guild_title == "WORKERS":
            vic_pts = 0
            for neighbor in neighbors:
                vic_pts += neighbor.get_num_color("brown")
            return vic_pts
        return 0


class ResourceToken(object):
    """ This class represents a single resource.

        Attributes:
            is_rsrc: dictionary of boolean values
                Each key is either a brown or gray resource
            is_shareable: boolean, whether or not this resource can be bought
                by neighbors
    """

    def __init__(self, rsrc_list, is_shareable=True):
        self.is_shareable = is_shareable

        self.is_rsrc = {'LOOM': False,
                        'GLASSWORKS': False,
                        'PRESS': False,
                        'WOOD': False,
                        'ORE': False,
                        'BRICK': False,
                        'STONE': False,
                        }

        for rsrc in rsrc_list:
            assert(rsrc in self.is_rsrc.keys())
            self.is_rsrc[rsrc] = True

    def __str__(self):
        out_str = ''
        for rsrc in self.is_rsrc.keys():
            if self.is_rsrc[rsrc]:
                out_str += rsrc+'/'
        out_str = out_str[:-1]
        if not self.is_shareable:
            out_str += " (NOT SHAREABLE)"
        return out_str
