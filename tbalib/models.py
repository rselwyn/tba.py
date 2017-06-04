from pprint import pprint
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