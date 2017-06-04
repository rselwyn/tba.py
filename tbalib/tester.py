import tba

# USE This To Include a Sample Use of the API

KEY = open("auth.key","r").readlines()[0].replace("\n","")

tba.TBACommunication.setKey(KEY)
print tba.TBACommunication.getExtension("/team/frc254")