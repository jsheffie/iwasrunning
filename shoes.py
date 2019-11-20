#!/usr/bin/env python

import json
from datetime import datetime

shoes = []

shoe_1={ 
    "name":                "Brooks Ghost 11",
    "release_date":        datetime(2018,1,1,7,0,0).isoformat(),
    "purchase_date":       datetime(2019,8,21,7,0,0).isoformat(),
    "website":             "https://www.brooksrunning.com/en_us/brooks-running-shoes-ghost-11-mens/1102881D037.100.html?gclid=Cj0KCQiA5dPuBRCrARIsAJL7oehTH3A6PSKLD3GS41kP2VrhYaZo88f3NWOpy34HUBgXkaCc1iQLOeEaAotgEALw_wcB&gclsrc=aw.ds",
    "weight":              "10.9oz/309g",
    "stack_height":        "29mm",
    "drop":                "12",  # in mm
    "cost":                99,  # in $
    "notes":               "https://www.amazon.com/gp/product/B077K3XF83/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1",
    "sku":                 "114920569",
    "support":             "Neutral",
    "arch":                "Medium, High",
    "experience type":     "Cushion",
    "technology":          "DNA LOFT",
    "use":                 "Road Running",
    "size":                "11 EE/Wide"
}

shoe_2={ 
    "name":                "Oranginer Barefoot Running",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    "purchase_date":       datetime(2019,10,11,7,0,0).isoformat(),
    "website":             "",
    "weight":              "",
    "stack_height":        "",
    "drop":                "0",  # in mm
    "cost":                32,  # in $
    "notes":               "https://www.amazon.com/gp/product/B07QSPZL95/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "",
    "size":                "11"
}

shoe_3={ 
    "name":                "Vibram Men's V-Run Running Shoe",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    "purchase_date":       datetime(2019,11,7,7,0,0).isoformat(),
    "website":             "https://us.vibram.com/shop/fivefingers/men/running/v-run-mens-M31_2.html?dwvar_M31__2_color=North%20Sea%20%2F%20Navy#start=1",
    "weight":              "4.8oz (M43)",
    "stack_height":        "",
    "drop":                "0",  # in mm
    "cost":                104,  # in $
    "notes":               "TOO BIG",
    "sku":                 "M31_2",
    "support":             "",
    "arch":                "",
    "experience type":     "Cushion",
    "technology":          "VI-LITE, XS RUN, MONT",
    "use":                 "Road Running",
    "size":                "10.5-11.5 43EU"
}

shoe_5={ 
    "name":                "Vibram Men's V-Run Running Shoe",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://us.vibram.com/shop/fivefingers/men/running/v-run-mens-M31_2.html?dwvar_M31__2_color=North%20Sea%20%2F%20Navy#start=1",
    "weight":              "4.8oz (M43)",
    "stack_height":        "",
    "drop":                "0",  # in mm
    "cost":                116,  # in $
    "notes":               "These Fit me: https://www.amazon.com/gp/product/B0114CI4AK/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1",
    "sku":                 "M31_2",
    "support":             "",
    "arch":                "",
    "experience type":     "Cushion",
    "technology":          "VI-LITE, XS RUN, MONT",
    "use":                 "Road Running",
    "size":                "9.5-10 43EU"
}

shoe_6={ 
    "name":                "HOKA ONE ONE EVO SPEEDGOAT",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,12,1,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/hoka-one-one-evo-speedgoat/",
    "weight":              "9.9oz (9)",
    "stack_height":        "32mm/28mm",
    "drop":                "4",  # in mm
    "cost":                160,  # in $
    "notes":               "",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_7={ 
    "name":                "LA SPORTIVA LYCAN",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/la-sportiva-lycan/",
    "weight":              "9.5 oz",
    "stack_height":        "18mm/12mm",
    "drop":                "6",  # in mm
    "cost":                115,  # in $
    "notes":               "Fit Wide",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Hybrid",
    "size":                ""
}
shoe_8={ 
    "name":                "LA SPORTIVA KAPTIVA 2",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/la-sportiva-kaptiva-2-m/",
    "weight":              "9 oz",
    "stack_height":        "18mm/12mm",
    "drop":                "6",  # in mm
    "cost":                139,  # in $
    "notes":               "",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_9={ 
    "name":                "INOV-8 TERRAULTRA G 260",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/inov-8-terraultra-g-260-series/",
    "weight":              "9.17 oz",
    "stack_height":        "",
    "drop":                "0",  # in mm
    "cost":                127,  # in $
    "notes":               "Zero Drop / Last forever",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}

shoe_10={ 
    "name":                "HOKA ONE ONE SPEEDGOAT 3",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/hoka-one-one-speedgoat-3-mens/",
    "weight":              "10.3 oz",
    "stack_height":        "32mm/28mm",
    "drop":                "4",  # in mm
    "cost":                140,  # in $
    "notes":               "Karl Meltzer aka 'The Speedgoat'",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_11={ 
    "name":                "HOKA ONE ONE BONDI 6",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/hoka-one-one-bondi-6-mens/",
    "weight":              "10.9 oz",
    "stack_height":        "33mm/29mm",
    "drop":                "4",  # in mm
    "cost":                150,  # in $
    "notes":               "Most cushioned shoe",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Road/Light Trail",
    "size":                ""
}
shoe_12={ 
    "name":                "HOKA ONE ONE TORRENT",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/hoka-one-one-torrent-mens/",
    "weight":              "9 oz",
    "stack_height":        "24mm/19mm",
    "drop":                "4",  # in mm
    "cost":                120,  # in $
    "notes":               "lightweight, speedy",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}

shoe_13={ 
    "name":                "HOKA ONE ONE EVO MAFATE",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/hoka-one-one-evo-mafate/",
    "weight":              "9.6 oz",
    "stack_height":        "33mm/29mm",
    "drop":                "4",  # in mm
    "cost":                130,  # in $
    "notes":               "",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_14={ 
    "name":                "TOPO ULTRAFLY 2",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/topo-ultrafly-2-mens/",
    "weight":              "10 oz",
    "stack_height":        "28mm/23mm",
    "drop":                "5",  # in mm
    "cost":                120,  # in $
    "notes":               "",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_15={ 
    "name":                "INOV-8 F-LITE 290 G SERIES",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/inov8-f-lite-290-g-series/",
    "weight":              "10.3 oz",
    "stack_height":        "",
    "drop":                "0",  # in mm
    "cost":                136,  # in $
    "notes":               "Kevlar in the upper",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Gym Shoe",
    "size":                ""
}

shoe_16={ 
    "name":                "LA SPORTIVA UNIKA",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/la-sportiva-unika/",
    "weight":              "11.6 oz",
    "stack_height":        "31mm/23mm",
    "drop":                "8",  # in mm
    "cost":                199,  # in $
    "notes":               "Mountain Running made in europ ( long wear )",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_17={ 
    "name":                "LA SPORTIVA MUTANT",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/la-sportiva-mutant-m/",
    "weight":              "11.29",
    "stack_height":        "24mm/14mm",
    "drop":                "10",  # in mm
    "cost":                135,  # in $
    "notes":               "longest runs, nastiest terrain",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_18={ 
    "name":                "LA SPORTIVA AKASHA",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/la-sportiva-akasha-mens/",
    "weight":              "11.35 oz",
    "stack_height":        "26mm/20mm",
    "drop":                "4",  # in mm
    "cost":                140,  # in $
    "notes":               "Long Distance",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
shoe_19={ 
    "name":                "LA SPORTIVA VK",
    "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
    # "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
    "website":             "https://austintrailrunning.com/product/la-sportiva-vk/",
    "weight":              "6.9 oz",
    "stack_height":        "16mm/12mm",
    "drop":                "4",  # in mm
    "cost":                135,  # in $
    "notes":               "designed to fly-up-mountians",
    "sku":                 "",
    "support":             "",
    "arch":                "",
    "experience type":     "",
    "technology":          "",
    "use":                 "Trail Running",
    "size":                ""
}
# shoe_20={ 
#     "name":                "",
#     "release_date":        datetime(2019,1,1,7,0,0).isoformat(),
#     "purchase_date":       datetime(2019,11,9,7,0,0).isoformat(),
#     "website":             "",
#     "weight":              "",
#     "stack_height":        "",
#     "drop":                "0",  # in mm
#     "cost":                0,  # in $
#     "notes":               "",
#     "sku":                 "",
#     "support":             "",
#     "arch":                "",
#     "experience type":     "",
#     "technology":          "",
#     "use":                 "",
#     "size":                ""
# }


for i in range(55):
    try:
        shoes.append(eval('shoe_'+str(i)))
    except NameError:
        pass


# print json.dumps(events, indent=4)

# sorted_shoe = sorted(shoes, key=lambda k: k['release_date']) 
# sorted_shoe = sorted(shoes, key=lambda k: k['weight'])
sorted_shoe = sorted(shoes, key=lambda k: int(k['drop']))

print("{:35}{:15}{:5}{:10}{:10}{:15}{:15}{:68}".format("Shoe Name","Weight", "Drop", "Stack", "Cost", "Purchased Date", "Use", "Notes"))
print("{:35}{:15}{:5}{:10}{:10}{:15}{:15}{:68}".format("-"*34,"-"*14,"-"*5,"-"*9,"-"*9,"-"*14,"-"*14, "-"*68))

for shoe in sorted_shoe:
    release_date_obj = datetime.strptime(shoe['release_date'], '%Y-%m-%dT%H:%M:%S')
    purchased_date_str=""
    if 'purchase_date' in shoe:
        purchase_date_obj = datetime.strptime(shoe['purchase_date'], '%Y-%m-%dT%H:%M:%S')
        purchased_date_str=purchase_date_obj.strftime('%Y-%m-%d')

    print("{:35}{:15}{:5}{:10}{:10}{:15}{:15}{:68}".format(shoe.get('name',None),
                                                shoe.get('weight', None),
                                                shoe.get('drop', None),
                                                shoe.get('stack_height', None),
                                                "${}".format(shoe.get('cost', None)),
                                                purchased_date_str,
                                                shoe.get('use', None),
                                                shoe.get('notes', None),
                                                ))

