#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:09:11 2018

@author: Laurawatkin
"""

import pandas as pd
checks = pd.read_csv("/Users/Laurawatkin/Desktop/School/U2/INSY336/Project/data.csv")  
gun_violence = pd.read_csv("/Users/Laurawatkin/Desktop/School/U2/INSY336/Project/gun_violence_data.csv")  
#separate the year and month of the checks
checks["year_int"] = checks["month"].apply(lambda x: int(x.split("-")[0]))
checks["month_int"] = checks["month"].apply(lambda x: int(x.split("-")[1]))

checks_state_year = checks.groupby(["year_int","state"])["totals"].sum()
print(checks_state_year)






#separate the year and month of the incidents
gun_violence["month_int"] = gun_violence["date"].apply(lambda x: int(x.split("-")[1]))
gun_violence["year_int"] = gun_violence["date"].apply(lambda x: int(x.split("-")[0]))

incidents_state_year = gun_violence.groupby(["year_int","state"])["incident_id"].count()
print(incidents_state_year)