#!/usr/bin/env python

import json
import datetime

events = []

event_1={ 
	"name":                "VAGABOND TIME TRIALS - 2019",
	"date":                "1",
	"location":            "1",
	"website":             "https://www.spectrumtrailracing.com/events/vagabond-time-trials-2019",
	"distance":            "1",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1",
}

event_2={ 
	"name":                "Bigfoot Trail Race",
	"date":                 datetime.datetime(2019,10,5,7,0,0).isoformat(),
	"location":            "1",
	"website":             "https://backonmyfeet.org/events/bigfoot/",
	"distance":            "1",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1",
}



event_3={ 
	"name":                "1",
	"date":                "1",
	"location":            "1",
	"website":             "1",
	"distance":            "1",
	"GPS_points":          "1",
	"race_director_name":  "1",
	"race_director_phone": "1",
	"signed_up":           "1",
	"description":         "1",
	"notes":               "1",
}


for i in range(3):
	try:
		events.append(eval('event_'+str(i)))
	except NameError:
		pass


print json.dumps(events, indent=4)
