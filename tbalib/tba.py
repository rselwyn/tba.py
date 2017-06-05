import urllib2
import json
import collections
import models

class TBACommunication(object):

	X_TBA_KEY = None

	__BASE_URL__ = "http://www.thebluealliance.com/api/v3"

	@staticmethod
	def setKey(tbaHeader):
		# NOTE: Parameter should be formatted in the form of a string that _CAN_ go into a URL.
		TBACommunication.X_TBA_KEY = tbaHeader

	@staticmethod
	def getExtension(ext):
		url = TBACommunication.__BASE_URL__ + ext + "?X-TBA-Auth-Key=" + TBACommunication.X_TBA_KEY
		request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'})
		data = urllib2.urlopen(request).read().decode('utf-8')
		return TBACommunication.__parse_unicode__(json.loads(data))

	@staticmethod
	def __parse_unicode__(data):
		if isinstance(data, basestring):
			return str(data)
		elif isinstance(data, collections.Mapping):
			return dict(map(TBACommunication.__parse_unicode__, data.iteritems()))
		elif isinstance(data, collections.Iterable):
			return type(data)(map(TBACommunication.__parse_unicode__, data))
		else:
			return data

class TBARequestCoordinator(object):
	"""
	Make sure to set the X_TBA_KEY in the TBACommunication class using the method setKey() before making any requests.
	"""

	@staticmethod
	def get_team(team):
		return models.TeamModel(TBACommunication.getExtension("/team/" + team))

	@staticmethod
	def get_awards(team):
		return models.TeamAwardsModel(TBACommunication.getExtension("/team/" + team + "/awards"))
