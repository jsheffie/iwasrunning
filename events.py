#!/usr/bin/env python

import json
from datetime import datetime

events = []

event_1={ 
    "name":                "VAGABOND TIME TRIALS - Oct - Dec 2019",
    "date":                datetime(2019,10,1,7,0,0).isoformat(),
    "website":             "https://www.spectrumtrailracing.com/events/vagabond-time-trials-2019",
    "distance":            "8",
    "registered":          True,
    "cost":                "$15",
    # "location":            "1",
    # "GPS_points":          "1",
    # "race_director_name":  "1",
    # "race_director_phone": "1",
    # "signed_up":           "1",
    # "description":         "1",
    # "notes":               "1",
}

event_2={ 
    "name":                "Bigfoot Trail Race",
    "date":                datetime(2019,10,5,7,0,0).isoformat(),
    "location":            "Spring Lake Preserve, Co Rd 225, San Marcos, TX 78666",
    "website":             "https://backonmyfeet.org/events/bigfoot/",
    "distance":            "30k",
    "registered":          True,
    "drive_time":          "1 hour",
    "cost":                "$50",
}


event_3={ 
    "name":                "WONDERLAND",
    "date":                datetime(2019,11,2,7,30,0).isoformat(),
    "location":            "Muleshoe Bend Recreation Area - 2820 Co Rd 414, Spicewood, TX 78669",
    "website":             "https://www.spectrumtrailracing.com/events/wonderland",
    "distance":            "marathon",
    "registered":          False,
    "cost":                "$115",
    "drive_time":          "1 hour",
    "notes":               "1 hour drive ( cost is $115 for full and $85 for half )",
}

event_4={ 
    "name":                "HUMANA ROCK 'N' ROLL SAN ANTONIO",
    "date":                datetime(2019,12,8,7,15,0).isoformat(),
    "location":            "W. Market St. & S. Alamo St.",
    "website":             "https://www.runrocknroll.com/en/Events/San-Antonio/The-Races/Marathon",
    "distance":            "marathon",
    "registered":          False,
    "cost":                "$122",
    "notes":               "Have to be registered by Dec 1",
}
event_5={ 
    "name":                "Austin Marathon",
    "date":                datetime(2020,2,16,7,0,0).isoformat(),
    "location":            "1",
    "website":             "https://youraustinmarathon.com/",
    "distance":            "marathon",
    "registered":          False,
    "cost":                "$149",
    "notes":               "till 10/29",
}

event_6={ 
    "name":                "The Maze @Walnut Creek",
    "date":                datetime(2020,03,1,7,0,0).isoformat(),
    "location":            "Walnut Creek Metropolitan Park - 12138 N Lamar Blvd Austin, TX 78753",
    "website":             "https://www.roguetrailseries.com/maze",
    "distance":            "30k",
    "registered":          False,
    "cost":                "$76",
    "notes":               "$76 before February 1;  $83 until March 1 @ noon (when registration closes);  NO RACE DAY REGISTRATION ( $64  ($194) for all three ) 3 10k loops ",
}
event_7={ 
    "name":                "The Tangle @ Flat Creek",
    "date":                datetime(2020,03,29,7,0,0).isoformat(),
    "location":            "339 Ulrich Road Johnson City, TX 78636",
    "website":             "https://www.roguetrailseries.com/tangle",
    "distance":            "30k",
    "registered":          False,
    "cost":                "$76",
    "notes":               "$76 before February 28; $83 until March 28; $90 on race day.",
}

event_8={ 
    "name":                "The Stampede @ ROAM Ranch",
    "date":                datetime(2020,04,26,7,0,0).isoformat(),
    "location":            "ROAM Ranch - 2417 Pfeiffer Rd. Fredericksburg, TX 78624",
    "website":             "https://www.roguetrailseries.com/stampede",
    "distance":            "30k",
    "registered":          False,
    "cost":                "$76",
    "notes":               "$76 before March 25; $83 until April 25; $90 on race day",
}
event_9={ 
    "name":                "El Taco Loco",
    "date":                datetime(2019,10,26,6,30,0).isoformat(),
    "location":            "SA",
    "website":             "http://www.trailracingovertexas.com/el-taco-loco",
    "distance":            "50k",
    "registered":          False,
    "cost":                "$100",
    "notes":               "https://calendar.ultrarunning.com/event/el-taco-loco",
}
event_10={ 
    "name":                "Cactus Rose",
    "date":                datetime(2019,10,26,6,30,0).isoformat(),
    "location":            "Bandara, TX",
    "website":             "https://www.tejastrails.com/",
    "distance":            "50 Miles",
    "registered":          False,
    "cost":                "$100",
    "notes":               "https://calendar.ultrarunning.com/event/cactus-rose",
}
event_11={ 
    "name":                "Gassy Goat",
    "date":                datetime(2019,10,12,6,30,0).isoformat(),
    "location":            "Comfort, TX US 78013",
    "website":             "https://www.tejastrails.com/gassygoat/",
    "distance":            "20k/40k",
    "registered":          False,
    "cost":                "$80/$90",
    "notes":               "",
    "drive_time":          "2 hours",
}
event_12={ 
    "name":                "Trivium (Road Race)",
    "date":                datetime(2019,11,10,6,30,0).isoformat(),
    "location":            "Marble Falls",
    "website":             "https://www.tejastrails.com/gassygoat/",
    "distance":            "20k/40k",
    "registered":          False,
    "cost":                "$80/$90",
    "notes":               "",
}



# event_9={ 
#   "name":                "1",
#   "date":                "1",
#   "location":            "1",
#   "website":             "1",
#   "distance":            "1",
#   "GPS_points":          "1",
#   "race_director_name":  "1",
#   "race_director_phone": "1",
#   "signed_up":           "1",
#   "description":         "1",
#   "notes":               "1",
# }






for i in range(55):
    try:
        events.append(eval('event_'+str(i)))
    except NameError:
        pass


# print json.dumps(events, indent=4)

sorted_events = sorted(events, key=lambda k: k['date']) 

print("{:50}{:20}{:15}{:8}{:15}{:10}{:68}".format("Event Name","Distance", "Race Date",  "Cost", "Registered", "Drive Time", "Website"))
print("{:50}{:20}{:15}{:8}{:15}{:10}{:68}".format("-"*25,"-"*18,"-"*10,"-"*4,"-"*8, "-"*8,"-"*60))

for event in sorted_events:
    date_time_obj = datetime.strptime(event['date'], '%Y-%m-%dT%H:%M:%S')
    print("{:50}{:20}{:15}{:8}{:15}{:10}{:68}".format(event.get('name',None), 
                                                event.get('distance', None), 
                                                date_time_obj.strftime('%Y-%m-%d'), 
                                                event.get('cost', None), 
                                                str(event.get('registered', None)),
                                                event.get('drive_time', None),
                                                event.get('website', None),
                                                ))

