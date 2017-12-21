import tba
import json

# USE This To Include a Sample Use of the API

KEY = open("auth.key","r").readlines()[0].replace("\n","")

tba.TBACommunication.setKey(KEY)

print "Test: getExtension() Method: "
print tba.TBACommunication.getExtension("/team/frc254")

print "Test: Getting team"
print tba.TBARequestCoordinator.get_team("frc254") 

print "Test: Getting awards"
print [i.get_name() for i in tba.TBARequestCoordinator.get_awards("frc8").get_all_awards()]

print "Test: Getting A Team's Matches at Event"
for i in tba.TBARequestCoordinator.get_matches("frc8", "2017casj").get_matches():
	print i

oprs = tba.TBARequestCoordinator.get_oprs("2017casj")
# print json.dumps(oprs, indent=4, sort_keys=True)

casj = tba.TBARequestCoordinator.get_full_event("2017casj")
