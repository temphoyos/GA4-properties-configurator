# GA4 Properties configurator
## Purpose of this application
This Python application has been developed with the aim of dynamically configuring GA4 properties. 
It has been developed using Pycharm and is intended to be executed locally, directly from the code editor. 

At the time of creation of this repo, the code makes use of the Google Analytics Admin API Python client to dynamically 
configured and populate a given GA4 property's custom dimensions (event params, user properties and items). This is done
by means of accessing and leveraging a .csv file with these custom dimensions information with the Pandas Python library.
Authentication with the GA Admin API in Google Cloud is accomplished through a Service Account.

The dependencies of this Python application are listed in this repo's requirements.txt file. Following are the links to 
the used Python libraries :

[google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/)

[google-analytics-admin](https://pypi.org/project/google-analytics-admin/)

[pandas](https://pypi.org/project/pandas/)

## Steps to implement this development
Enable the [Google Analytics Admin API](https://developers.google.com/analytics/devguides/config/admin/v1?hl=es_419) in your Google Cloud Project. Create a Service Account within the
same project and set its permissions accordingly so that it can interact with the GA Admin API (Eg Editor role).
You will need to enable a JSON credential file within this Service Account and download it to keep it in a safe place.
Do not share these credentials.

Grant access to this Service Account to the GA4 property you wish to dynamically configure with and editor role.