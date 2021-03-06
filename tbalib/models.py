
import json

class TeamModel(object):

	def __init__(self, data):

		self.key = data["key"]
		self.team_number = data["team_number"]
		self.nickname = data["nickname"]
		self.name = data["name"]
		self.city = data["city"]
		self.state_prov = data["state_prov"]
		self.country = data["country"]
		self.address = data["address"]
		self.postal_code = data["postal_code"]
		self.gmaps_place_id = data["gmaps_place_id"]
		self.gmaps_url = data["gmaps_url"]
		self.lat = data["lat"]
		self.lng = data["lng"]
		self.location_name = data["location_name"]
		self.website = data["website"]
		self.rookie_year = data["rookie_year"]
		self.motto = data["motto"]
		self.home_championship = data["home_championship"]

	def get_key():
		return self.key
	def get_team_number():
		return self.team_number
	def get_nickname():
		return self.nickname
	def get_name():
		return self.name
	def get_city():
		return self.city
	def get_state_prov():
		return self.state_prov
	def get_country():
		return self.country
	def get_address():
		return self.address
	def get_postal_code():
		return self.postal_code
	def get_gmaps_place_id():
		return self.gmaps_place_id
	def get_gmaps_url():
		return self.gmaps_url
	def get_lat():
		return self.lat
	def get_lng():
		return self.lng
	def get_location_name():
		return self.location_name
	def get_website():
		return self.website
	def get_rookie_year():
		return self.rookie_year
	def get_motto():
		return self.motto
	def get_home_championship():
		return self.home_championship

	def __str__(self):
		return "Information about This Team Object: " + str(vars(self))

class TeamAwardsModel(object):

	def __init__(self, data):
		self.award_list = []
		for i in data:
			self.award_list.append(TBAAward(i["name"], i["event_key"], i["year"]))

	def get_all_awards(self):
		return self.award_list

	def get_award_during_year(self, year):
		return filter(lambda x: x.get_year() == year, self.award_list)


class TBAAward(object):

	def __init__(self, name, event, year):
		self.name = name
		self.event = event
		self.year = int(year)

	def get_name(self):
		return self.name

	def get_event(self):
		return self.event

	def get_year(self):
		return self.year

class MatchModel(object):

	def __init__(self, data):
		self.match_number = data["match_number"]
		self.comp_level = data["comp_level"]
		self.key = data["key"]

		self.blue_alliance = Alliance(data["alliances"]["blue"]["team_keys"][0],data["alliances"]["blue"]["team_keys"][1], data["alliances"]["blue"]["team_keys"][2])
		self.red_alliance = Alliance(data["alliances"]["red"]["team_keys"][0],data["alliances"]["red"]["team_keys"][1], data["alliances"]["red"]["team_keys"][2])
		self.winner = data["winning_alliance"]

		self.score_breakdown = data["score_breakdown"] # For Game Independence

	def __str__(self):
		return self.winner

	def get_blue_alliance():
		return self.blue_alliance.get_teams()

	def get_red_alliance():
		return self.red_alliance.get_teams()

	def get_breakdown():
		return self.score_breakdown

	def get_key():
		return self.key


class TeamMatchAtEventModel(object):

	def __init__(self, data):
		self.matches = []
		for i in data:
			self.matches.append(MatchModel(i))

	def get_matches(self):
		return self.matches

class Events(object):

	def __init__(self, matches, teams):
		# ppjson(matches)
		self.matches = [MatchModel(i) for i in matches]
		self.teams = [i["team_number"] for i in teams]
		self.awards = None
		self.rankings = None
		self.districtpoints = None

	def returnable(self):
		dct = {}
		dct["matches"] =  {i.get_key() : {"blue" : i.get_blue_alliance(), "red" : i.get_red_alliance(), "score_breakdown" : i.get_breakdown()} for i in matches}		
		dct["teams"] = self.teams

		return dct

	def get_teams(self):
		return self.teams

class Alliance(object):

	def __init__(self, *teams):
		if len(teams) == 3:
			self.NUM_TEAMS = 3
		else:
			self.NUM_TEAMS = 4

		self.teams = teams

	def get_teams(self):
		return self.teams

def ppjson(top):
	print json.dumps(top, indent=4, sort_keys=True)
