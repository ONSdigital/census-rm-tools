import uuid
from datetime import datetime
from datetime import timedelta
import csv
import json

# create uuids required
# one collection exercise, one survey, one collection instrument, one action plan and one rule
collectionexerciseid   = uuid.uuid4()
surveyid               = uuid.uuid4()
collectioninstrumentid = uuid.uuid4()
actionplanid           = uuid.uuid4()
actionruleid           = uuid.uuid4()

# hardcoded values
today       = datetime.now()
createdby   = 'SYSTEM'
count = 0
total_records = 100# number of cases required
selectors = json.dumps({})


# actionrule will trigger an hour from now, change if required
future_time = today + timedelta(seconds=3600)  # set to an hours time

# open all the csv files for writing
casegroup  =  open("casegroup.csv", "w")
case       =  open("case.csv", "w")
caseevent  =  open("caseevent.csv", "w")
actionplan =  open("actionplan.csv", "w")
actionrule =  open("actionrule.csv", "w")
actiontype =  open("actiontype.csv", "w")

print ("\ncreating data...")

# Create action plan
actionplan.write (str(actionplanid) + "," +      # id uuid
                 str(1) + "," +                  # actionplanpk
                 str("Initial contact") + "," +  # name
                 str("Initial contact")+ "," +   # description
                 str(createdby) + "," +          # createdby
                 str(today)  +  "," +             # lastrundatetime
                 str(selectors) +                 # selectors
                 "\n")
print ("\naction plan file created (" + str(datetime.now()) + ")")

# Create action rule for the action plan
# one rule to create an initial contact letter
actionrule.write(str(1) + "," +                         # actionrulepk
                 str(1) + "," +                         # actionplanfk
                 str(1) + "," +                         # actiontypefk
                 str("Initial contact") + "," +         # name
                 str("Initial contact letter") + "," +  # description
                 str(3) + "," +                         # priority
                 str(actionruleid) + "," +              # id uuid
                 str(future_time)  +                    # triggerdatetime
                 "\n")

print ("action rule file created (" + str(datetime.now()) + ")")

# Create actiontype
actiontype.write(str(1) + "," +                         # actiontypepk
                 str("Initial Contact") + "," +         # name
                 str("Initial contact letter") + "," +  # description
                 str("Printer") + "," +                 # handler
                 str("f") + "," +                       # cancancel
                 str("f") +                             # responserequired
                 "\n")

print ("action type file created (" + str(datetime.now()) + ")")

# Loop for how ever many casegroups/cases/caseevents you would like created (total_records set above)
# Note: They will all be attached to the actionplan which contains one actionrule to create a print file for initial contact

for casegrouppk in range(1,total_records+1):
    # progress
    count+=1
    if count % 10000 == 0:
       print("\r" + str(count) + " cases loaded")

    # each casegroup, case and sample get a unique uuid
    cgid          = uuid.uuid4()
    cid           = uuid.uuid4()
    sampleunitid  = uuid.uuid4()
    partyid       = uuid.uuid4()

    # Create case group
    casegroup.write(str(casegrouppk) + "," +           # casegrouppk
                    str(cgid) + "," +                  # id uuid
                    str(partyid) + "," +               # partyid uuid
                    str(collectionexerciseid) + "," +  # collectionexerciseid uuid
                    str("SARAHSAMPLE") + "," +         # sampleunitref
                    str("H")  + "," +                  # sampleunittype
                    str("NOTSTARTED") + "," +          # status
                    str(surveyid) +                    # surveyid uuid
                    "\n")                              # new line

    # Create case
    case.write(str(casegrouppk) + "," +                   # casepk
               str(cid) + "," +                           # id uuid
               str(casegrouppk+1000000000000000) + "," +  # caseref
               str(casegrouppk) + "," +                   # casegroupfk
               str(cgid) + "," +                          # casegroupid uuid
               str(partyid) + "," +                       # partyid uuid
               str("H")  + "," +                          # sampleunittype
               str(collectioninstrumentid) + "," +        # collectioninstrumentid uuid
               str("ACTIONABLE") + "," +                  # statefk
               str(actionplanid) + "," +                  # actionplanid uuid
               str(today)  + "," +                        # createddatetime
               str(createdby) + "," +                     # createdby
               str(0) + "," +                             # sourcecase
               str(1) + "," +                             # optlockversion
               str(sampleunitid) +                        # sampleunit_id uuid
               "\n")                                      # new line

    # Create case event
    caseevent.write(str(casegrouppk) + "," +                                  # caseevenpk
                    str(casegrouppk) + "," +                                  # casefk
                    str("Case created when initial creation of case") + "," + # description
                    str(createdby) + "," +                                    # createdby
                    str(today)  + "," +                                       # createddatetime
                    str("CASE_CREATED")  + "," +                              # categoryfk
                    str("") +                                                 # subcategory
                    "\n")                                                     # new line

print ("case group, case and case events files created (" + str(datetime.now()) + ")")

# close the files
casegroup.close()
case.close()
caseevent.close()
actionplan.close()
actionrule.close()
actiontype.close()


print (str(total_records) + ' cases created')
print ("\nfiles created...\n")
print ("casegroup.csv")
print ("case.csv")
print ("caseevent.csv")
print ("actionplan.csv")
print ("actionrule.csv")
print ("actiontype.csv")
