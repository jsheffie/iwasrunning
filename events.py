#!/usr/bin/env python

import json
import datetime

events = []

event_1={ 
	"name":                "VAGABOND TIME TRIALS - 2019",
	"date":                datetime.datetime(2019,10,1,7,0,0).isoformat(),
	"location":            "1",
	"website":             "https://www.spectrumtrailracing.com/events/vagabond-time-trials-2019",
	"distance":            "8",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1",
}

event_2={ 
	"name":                "Bigfoot Trail Race",
	"date":                datetime.datetime(2019,10,5,7,0,0).isoformat(),
	"location":            "1",
	"website":             "https://backonmyfeet.org/events/bigfoot/",
	"distance":            "30k",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1",
}



event_3={ 
	"name":                "WONDERLAND",
	"date":                datetime.datetime(2019,11,2,7,30,0).isoformat(),
	"location":            "Muleshoe Bend Recreation Area - 2820 Co Rd 414, Spicewood, TX 78669",
	"website":             "https://www.spectrumtrailracing.com/events/wonderland",
	"distance":            "marathon",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1 hour drive ( cost is $115 for full and $85 for half )",
}

event_4={ 
	"name":                "HUMANA ROCK 'N' ROLL SAN ANTONIO",
	"date":                datetime.datetime(2019,12,8,7,15,0).isoformat(),
	"location":            "W. Market St. & S. Alamo St.",
	"website":             "https://www.runrocknroll.com/en/Events/San-Antonio/The-Races/Marathon",
	"distance":            "marathon",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "$122.00 Finish Line: Cesar Chavez BLVD by UTSA institute of Texan Cultures ( have to be registered by Dec 1 ) ",
}
event_5={ 
	"name":                "Austin Marathon",
	"date":                datetime.datetime(2020,2,16,7,0,0).isoformat(),
	"location":            "1",
	"website":             "https://youraustinmarathon.com/",
	"distance":            "marathon",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1",
}

event_6={ 
	"name":                "The Maze @Walnut Creek",
	"date":                datetime.datetime(2020,03,1,7,0,0).isoformat(),
	"location":            "Walnut Creek Metropolitan Park - 12138 N Lamar Blvd Austin, TX 78753",
	"website":             "https://www.roguetrailseries.com/maze",
	"distance":            "30k",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "30k $76 before February 1;  $83 until March 1 @ noon (when registration closes);  NO RACE DAY REGISTRATION ( $64  ($194) for all three ) 3 10k loops ",
}
event_7={ 
	"name":                "The Tangle @ Flat Creek",
	"date":                datetime.datetime(2020,03,29,7,0,0).isoformat(),
	"location":            "339 Ulrich Road Johnson City, TX 78636",
	"website":             "https://www.roguetrailseries.com/tangle",
	"distance":            "30k",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "30k",
}

event_8={ 
	"name":                "The Stampede @ ROAM Ranch",
	"date":                datetime.datetime(2020,04,26,7,0,0).isoformat(),
	"location":            "ROAM Ranch - 2417 Pfeiffer Rd. Fredericksburg, TX 78624",
	"website":             "https://www.roguetrailseries.com/stampede",
	"distance":            "30k",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "",
}
# event_9={ 
# 	"name":                "1",
# 	"date":                "1",
# 	"location":            "1",
# 	"website":             "1",
# 	"distance":            "1",
# 	"GPS_points":          "1",
# 	"race_director_name":  "1",
# 	"race_director_phone": "1",
# 	"signed_up":           "1",
# 	"description":         "1",
# 	"notes":               "1",
# }






for i in range(15):
	try:
		events.append(eval('event_'+str(i)))
	except NameError:
		pass


print json.dumps(events, indent=4)


for event in events:
	print("{:50}{:20}{}".format(event['name'], event['distance'], event['date']))

