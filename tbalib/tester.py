import tba

# USE This To Include a Sample Use of the API

KEY = open("auth.key","r").readlines()[0].replace("\n","")

tba.TBACommunication.setKey(KEY)

print "Test: getExtension() Method: "
print tba.TBACommunication.getExtension("/team/frc254")

print "Test: Getting team"
print tba.TBARequestCoordinator.get_team("frc254") 

print "Test: Getting awards"
print [i.get_name() for i in tba.TBARequestCoordinator.get_awards("frc8").get_all_awards()]