# Code for Data Process Server of SHES

The Data Process Server of our Smart Home Emergency System (SHES) is developed with python and sql, and is deployed on IBM FYRE Cloud.

The python file "sqlupdate_success.py" is used to fetch voice data of Google Assistant from Google Firebase in real-time, and then merge this data with the simulated location data to update our SHES SQL databse, which is used for IBM Cognos Analytics modelling and dashboard display. The initial SQL data can be generated with "sqlupdate.py" and Microsoft sql server.